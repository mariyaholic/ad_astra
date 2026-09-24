"""Campaign steps. Each takes (ctx, params) and returns a JSON-serialisable result.

Steps write measurements to the ledger through ``ctx.measure`` and update the campaign's
record checks through ``ctx.check``; they never invent a value, and an unavailable test is
left ``not_tested``. Register new steps in ``STEPS``.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np

from .lightcurve import (contiguous_runs, in_veto, local_resid, phase_of, read_spoc, robust_sigma,
                         screen_events)

MAST_DOWNLOAD = "https://mast.stsci.edu/api/v0.1/Download/file?uri=mast%3ATESS%2Fproduct%2F{pid}"


def portable(path: Path) -> str:
    """Store scratch paths as ``scratch:<relative>`` so saved outputs carry no machine-specific paths."""
    from ..config import scratch_dir

    root = scratch_dir().resolve()
    try:
        return "scratch:" + Path(path).resolve().relative_to(root).as_posix()
    except ValueError:
        return Path(path).name   # outside scratch: keep only the file name


def resolve(stored: str) -> Path:
    from ..config import scratch_dir

    return scratch_dir() / stored[8:] if stored.startswith("scratch:") else Path(stored)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------ products
def _discover_spoc_lcs(tic: int, max_products: int) -> list[dict]:
    """SPOC 120-s light curves for a TIC id, via the MAST Observations API (astroquery)."""
    from astroquery.mast import Observations

    obs = Observations.query_criteria(target_name=str(tic), obs_collection="TESS", provenance_name="SPOC",
                                      dataproduct_type="timeseries")
    if len(obs) == 0:
        return []
    prods = Observations.filter_products(Observations.get_product_list(obs), productSubGroupDescription="LC")
    out = []
    for r in prods:
        fn = str(r["productFilename"])
        if fn.endswith("-s_lc.fits") and "fast" not in fn:
            out.append({"product_id": fn, "tic": tic, "sector": int(fn.split("-s")[1][:4]) if "-s0" in fn else None,
                        "data_uri": str(r["dataURI"])})
    out.sort(key=lambda d: d["product_id"])
    return out[:max_products]


def step_fetch_products(ctx, params: dict) -> dict:
    """Locate or download each product, verify it, and register it in the ledger.

    Pinned products (``input.products`` with ``expected_sha256``) must match exactly. Products
    discovered from a target queue are recorded with the SHA-256 of their first retrieval.
    """
    from ..ingest.netio import fetch_to_file

    wanted = [dict(p) for p in ctx.spec.get("input", {}).get("products", [])]
    q = params.get("from_queue")
    if q:
        queue = ctx.result("target_queue")["queue"][: int(q.get("top", 5))]
        for t in queue:
            for p in _discover_spoc_lcs(int(t["tic"]), int(q.get("max_products_per_target", 2))):
                p["target"] = t["name"]
                wanted.append(p)
    from ..config import scratch_dir

    # "scratch:<subdir>" keeps machine-specific paths out of committed specs
    dirs = [ctx.scratch] + [scratch_dir(d[8:]) if str(d).startswith("scratch:") else Path(d)
                            for d in params.get("search_dirs", [])]
    out = {}
    for p in wanted:
        pid = p["product_id"]
        path = next((d / pid for d in dirs if (d / pid).is_file()), None)
        fetched = False
        if path is None:
            path = ctx.scratch / pid
            fetch_to_file(MAST_DOWNLOAD.format(pid=pid), path, timeout_s=120)
            fetched = True
        digest, size = _sha256(path), path.stat().st_size
        if p.get("expected_sha256") and (digest != p["expected_sha256"] or
                                         (p.get("expected_bytes") and size != int(p["expected_bytes"]))):
            raise RuntimeError(f"{pid}: checksum/size mismatch (sha256 {digest}, {size} bytes); refusing to analyse")
        if not ctx.ledger_has_product("MAST", pid):
            ctx.ledger.add_product("MAST", pid, url=MAST_DOWNLOAD.format(pid=pid), local_path=path, checksum=digest,
                                   license_="public MAST", extra={"campaign": ctx.campaign_id, "tic": p.get("tic"),
                                                                  "sector": p.get("sector")})
        out[pid] = {"path": portable(path), "sha256": digest, "bytes": size, "fetched_now": fetched,
                    "pinned": bool(p.get("expected_sha256")), "target": p.get("target"), "tic": p.get("tic"),
                    "sector": p.get("sector")}
    ctx.check("Product integrity (SHA-256)", "passed",
              f"{len(out)} product(s) verified; pinned checksums matched" if any(v["pinned"] for v in out.values())
              else f"{len(out)} product(s) checksummed at first retrieval")
    return {"products": out}


# ------------------------------------------------------------------ veto windows
def _veto_mask(lc, veto: dict | None, target: dict | None):
    """Cadences inside the known-signal veto. ``ephemeris``: ±veto_phase of a periodic transit;
    ``single_epoch``: ±veto_hours around a single known transit time (e.g. a TOI monotransit)."""
    if not veto:
        return np.zeros(lc.time.size, bool), None
    if veto["kind"] == "ephemeris":
        ph = phase_of(lc.time_bjd, veto["period_days"], veto["t0_bjd"])
        return in_veto(ph, veto["veto_phase"]), ph
    if veto["kind"] == "single_epoch":
        t0 = float((target or {}).get("t0_bjd", veto.get("t0_bjd")))
        half = float(veto["veto_hours"]) / 24
        return np.abs(lc.time_bjd - t0) <= half, None
    raise ValueError(f"unknown veto kind {veto['kind']!r}")


def _target_for(ctx, pid: str) -> dict | None:
    prod = ctx.result("fetch_products")["products"][pid]
    if not prod.get("target"):
        return None
    for t in ctx.optional_result("target_queue", {}).get("queue", []):
        if t["name"] == prod["target"]:
            return t
    return None


# ------------------------------------------------------------------ residual screen
def step_residual_screen(ctx, params: dict) -> dict:
    """Negative excursions ≥ k robust-MAD, ≥ min_cadences, SAP and PDCSAP, several baselines,
    outside the known-signal veto. Writes screen.json and normalized_series.csv per product."""
    veto = ctx.spec.get("veto")
    windows = tuple(params.get("windows_days", (1.0, 2.0, 3.0)))
    k_decl = params.get("k_mad", 5.0)
    calib = ctx.optional_result("calibrate_screen", {}).get("per_product", {})
    summary = {}
    for pid, prod in ctx.result("fetch_products")["products"].items():
        lc = read_spoc(resolve(prod["path"]))
        k = calib[pid]["k_star"] if k_decl == "calibrated" else float(k_decl)
        target = _target_for(ctx, pid)
        vmask, ph = _veto_mask(lc, veto, target)
        finite = lc.usable
        events = []
        for e in screen_events(lc, windows_days=windows, k_mad=k, min_cadences=int(params.get("min_cadences", 2))):
            g = np.arange(e["start_index"], e["stop_index"] + 1)
            epoch = float(np.nanmedian(lc.time_bjd[g]))
            ev = {"detrend_days": e["detrend_days"], "flux_type": e["flux_type"], "start_index": e["start_index"],
                  "stop_index": e["stop_index"], "n_cadences": e["n_cadences"],
                  "start_time_stored": float(lc.time[g[0]]), "end_time_stored": float(lc.time[g[-1]]),
                  "mid_time_BJD_like": epoch}
            if veto and veto["kind"] == "ephemeris":
                ev["phase_from_provisional_ephemeris"] = float(((epoch - veto["t0_bjd"]) / veto["period_days"]) % 1)
            ev.update({"median_fractional_residual": e["median_fractional_residual"],
                       "robust_sigma_fraction": e["robust_sigma_fraction"], "min_quality": int(np.min(lc.quality[g])),
                       "centroids": {n: float(np.nanmedian(v[g])) for n, v in lc.centroids.items()},
                       "inside_veto": bool(vmask[g].any())})
            events.append(ev)
        res = {"input": {"file": lc.path.name, "bytes": prod["bytes"], "sha256": prod["sha256"]},
               "headers": {k2: lc.primary.get(k2) for k2 in ("OBJECT", "TICID", "SECTOR", "CAMERA", "CCD", "RA_OBJ", "DEC_OBJ",
                                                             "DATE-OBS", "DATE-END", "TIMESYS", "TIMEUNIT", "TELESCOP",
                                                             "INSTRUME", "FILTER")},
               "table_header": {k2: lc.table_header.get(k2) for k2 in ("BJDREFI", "BJDREFF", "TIMEZERO", "TIMESYS", "TIMEUNIT", "TUNIT1")},
               "rows": int(lc.time.size), "quality_zero": int(np.count_nonzero(np.isfinite(lc.time) & (lc.quality == 0))),
               "usable": int(finite.sum()), "time_min_stored": float(np.nanmin(lc.time[finite])),
               "time_max_stored": float(np.nanmax(lc.time[finite])), "bjdref": lc.bjdref,
               "time_scale": lc.table_header.get("TIMESYS"), "cadence_seconds_header": lc.cadence_s,
               "coordinate_convention": "header RA_OBJ/DEC_OBJ as supplied; frame not independently established",
               "threshold": {"k_mad": k, "source": "calibrated (calibrate_screen)" if k_decl == "calibrated" else "declared in campaign spec"}}
        if events:
            res["screened_excursions"] = events
        sw = float(params.get("series_window_days", 2.0))
        rs, rp = local_resid(lc.sap, finite, lc.cadence_s, sw), local_resid(lc.pdc, finite, lc.cadence_s, sw)
        sub = ctx.product_dir(pid, lc)
        np.savetxt(sub / "normalized_series.csv", np.column_stack((lc.time, lc.time_bjd, lc.quality, lc.sap, lc.pdc, rs, rp)),
                   delimiter=",", header="TIME_stored,BJD_like,QUALITY,SAP_FLUX,PDCSAP_FLUX,SAP_frac_resid_2d,PDCSAP_frac_resid_2d",
                   comments="")
        if ph is not None:
            control = finite & ~vmask
            res["controls"] = {"definition": f"same LC phase outside ±{veto['veto_phase']}-cycle window about provisional transit",
                               "n": int(control.sum()), "sap_control_robust_sigma": robust_sigma(rs[control]),
                               "pdc_control_robust_sigma": robust_sigma(rp[control])}
        res["interpretation_limit"] = (f"-{k} robust-MAD threshold "
                                       + ("from the campaign's sign-flip calibration" if k_decl == "calibrated"
                                          else "is an uncalibrated screen unless calibrate_screen ran")
                                       + "; entries overlap across recipes and are not independent events.")
        (sub / "screen.json").write_text(json.dumps(res, indent=2, allow_nan=False), encoding="utf-8")
        outside = [e for e in events if not e["inside_veto"]]
        summary[pid] = {"dir": ctx.rel(sub), "rows": res["rows"], "usable": res["usable"], "k_mad": k,
                        "entries": len(events), "entries_outside_veto": len(outside),
                        "outside_veto": [{k2: e[k2] for k2 in ("detrend_days", "flux_type", "mid_time_BJD_like", "n_cadences",
                                                               "median_fractional_residual")} for e in outside]}
        ctx.measure("screen_entries", len(events), unit="count", method=f"-{k} MAD, windows {list(windows)} d, SAP+PDCSAP", products=[pid])
        ctx.measure("screen_entries_outside_veto", len(outside), unit="count", method="same, outside known-signal veto", products=[pid])
    n_out = sum(s["entries_outside_veto"] for s in summary.values())
    ctx.note(f"Residual screen: {n_out} threshold entr{'y' if n_out == 1 else 'ies'} outside the known-signal veto across "
             f"{len(summary)} light curve(s).")
    return {"per_product": summary, "entries_outside_veto_total": n_out}


# ------------------------------------------------------------------ BLS recovery
def step_bls_recovery(ctx, params: dict) -> dict:
    """Box least squares on one PDCSAP light curve plus a permutation diagnostic (as the 2026-09-24
    recovery test). Writes results.json in the campaign output directory."""
    import sys
    from datetime import datetime, timezone

    import astropy
    from astropy.timeseries import BoxLeastSquares

    pid = params["product"]
    prod = ctx.result("fetch_products")["products"][pid]
    lc = read_spoc(resolve(prod["path"]))
    finite = np.isfinite(lc.time) & np.isfinite(lc.pdc) & (lc.pdc > 0)
    good = finite & (lc.quality == 0)
    t, f, s = lc.time[good], lc.pdc[good], lc.sap[good]
    if len(t) < 100:
        raise RuntimeError("too few quality-zero cadences")
    f = f / np.nanmedian(f)
    lo, hi, n = params.get("period_grid", [0.5, 5.0, 5000])
    durations = np.arange(*params.get("duration_arange", [0.06, 0.161, 0.02]))
    periods = np.linspace(lo, hi, int(n))
    result = BoxLeastSquares(t, f).power(periods, durations, objective="likelihood")
    b = int(np.nanargmax(result.power))
    period, epoch, duration, depth = (float(result.period[b]), float(result.transit_time[b]),
                                      float(result.duration[b]), float(result.depth[b]))
    rng = np.random.default_rng(ctx.seed)
    trials = int(params.get("permutation_trials", 20))
    null_max = np.asarray([float(np.nanmax(BoxLeastSquares(t, rng.permutation(f)).power(periods, durations, objective="likelihood").power))
                           for _ in range(trials)])
    fap = float((1 + np.sum(null_max >= float(result.power[b]))) / (len(null_max) + 1))
    s = s / np.nanmedian(s)
    sap_fit = BoxLeastSquares(t, s).power(np.array([period]), np.array([duration]), objective="likelihood")
    payload = {
        "campaign": params.get("legacy_campaign_label", ctx.campaign_id), "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "archive": "MAST/STScI", "release_product": pid, "product_url": MAST_DOWNLOAD.format(pid=pid),
        "query_provenance": params.get("query_provenance", ""), "sha256": prod["sha256"],
        "expected_sha256_manifest": prod["sha256"] if prod["pinned"] else None,
        "target_header": {k: lc.primary.get(k) for k in ("TICID", "OBJECT", "RA_OBJ", "DEC_OBJ", "SECTOR", "CAMERA", "CCD", "TSTART", "TSTOP")},
        "time_metadata": {k: lc.table_header.get(k) for k in ("TIMESYS", "BJDREFI", "BJDREFF", "TIMEUNIT", "TIMEDEL", "TIMEPIXR")},
        "cadence_day": lc.table_header.get("TIMEDEL"), "n_rows": int(lc.time.size), "n_quality_zero_finite": int(len(t)),
        "n_excluded_quality_or_nonfinite": int(lc.time.size - len(t)), "time_range_btjd": [float(np.min(t)), float(np.max(t))],
        "baseline_days": float(np.ptp(t)),
        "search": {"period_days": [lo, hi], "period_grid_count": len(periods), "durations_days": durations.tolist(),
                   "objective": "likelihood", "seed": ctx.seed, "permutation_trials": trials},
        "best_bls": {"period_days": period, "transit_epoch_btjd": epoch, "duration_hours": duration * 24, "depth_fraction": depth,
                     "depth_ppm": depth * 1e6, "power": float(result.power[b]), "empirical_permutation_fap": fap,
                     "null_max_power_95pct": float(np.quantile(null_max, 0.95))},
        "sap_at_pdc_ephemeris": {"power": float(sap_fit.power[0]), "depth_fraction": float(sap_fit.depth[0])},
        "interpretation": params.get("interpretation", "BLS search result; not a detection claim."),
        "caveats": params.get("caveats", []),
        "software": {"python": sys.version.split()[0], "numpy": np.__version__, "astropy": astropy.__version__},
    }
    (ctx.outdir / "results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for name, val, unit in (("bls_period", period, "d"), ("bls_duration", duration * 24, "h"), ("bls_depth", depth * 1e6, "ppm"),
                            ("bls_power", float(result.power[b]), None), ("permutation_fap_diagnostic", fap, None)):
        ctx.measure(name, val, unit=unit, method="astropy BoxLeastSquares, likelihood objective", products=[pid])
    return {"best_bls": payload["best_bls"], "results_json": ctx.rel(ctx.outdir / "results.json")}


# ------------------------------------------------------------------ calibration (null + injection–recovery)
def _persistent_intervals(lc, sap, pdc, finite, window_days, k, sign, veto_mask):
    """Intervals flagged in BOTH SAP and PDCSAP at one baseline (the screen's persistence rule),
    outside the veto. Returns a list of (start, stop) index pairs."""
    flags = []
    for flux in (sap, pdc):
        rr = local_resid(flux, finite, lc.cadence_s, window_days)
        sig = robust_sigma(rr[finite])
        hit = finite & np.isfinite(rr) & ((rr < -k * sig) if sign < 0 else (rr > k * sig))
        flags.append(hit)
    both = flags[0] & flags[1] & ~veto_mask
    return [(int(g[0]), int(g[-1])) for g in contiguous_runs(both, 2)]


def step_calibrate_screen(ctx, params: dict) -> dict:
    """Calibrate the residual screen on each real light curve.

    * Null: flip the sign of the residual test (search for brightenings with the same rule). Real
      dips cannot produce these, so their rate estimates the screen's false-alarm rate from this
      light curve's own noise and systematics. k* is the smallest threshold on the grid with at most
      ``max_null_events`` persistent null events outside the veto.
    * Injection–recovery: box dips of given depth and duration injected multiplicatively into SAP and
      PDCSAP at random usable times outside the veto (seeded), recovered if a persistent dip interval
      overlaps the box. Completeness is reported at the declared threshold and at k*.
    """
    veto = ctx.spec.get("veto")
    window = float(params.get("window_days", 2.0))
    grid = [float(x) for x in params.get("k_grid", [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0])]
    max_null = int(params.get("max_null_events", 0))
    k_decl = float(params.get("declared_k", 5.0))
    depths = [float(x) for x in params.get("depths_ppm", [500, 1000, 2000, 5000, 10000])]
    durs = [float(x) for x in params.get("durations_h", [1.0, 2.0, 4.0])]
    n_inj = int(params.get("injections_per_cell", 10))
    ref = params.get("reference_signal", {"depth_ppm": 2000, "duration_h": 2.0})
    rng = np.random.default_rng(ctx.seed)
    per = {}
    for pid, prod in ctx.result("fetch_products")["products"].items():
        lc = read_spoc(resolve(prod["path"]))
        finite = lc.usable
        vmask, _ = _veto_mask(lc, veto, _target_for(ctx, pid))
        null = {k: len(_persistent_intervals(lc, lc.sap, lc.pdc, finite, window, k, +1, vmask)) for k in grid}
        ok = [k for k in grid if null[k] <= max_null]
        k_star = min(ok) if ok else None
        at_floor = k_star is not None and k_star == min(grid)   # then k* is only an upper bound
        # injection–recovery
        usable_idx = np.flatnonzero(finite & ~vmask)
        cad_d = lc.cadence_s / 86400
        comp = {}
        for dep in depths:
            for dur in durs:
                half = dur / 48
                starts, tries = [], 0
                while len(starts) < n_inj and tries < 5000:   # non-overlapping boxes, ≥ 1 d apart, fully usable
                    tries += 1
                    c = lc.time[rng.choice(usable_idx)]
                    if any(abs(c - s) < 1.0 for s in starts):
                        continue
                    box = (lc.time >= c - half) & (lc.time <= c + half)
                    if box.sum() >= max(2, int(0.8 * dur / 24 / cad_d)) and (finite[box] & ~vmask[box]).all():
                        starts.append(c)
                sap, pdc = lc.sap.copy(), lc.pdc.copy()
                boxes = []
                for c in starts:
                    box = (lc.time >= c - half) & (lc.time <= c + half)
                    sap[box] *= 1 - dep * 1e-6
                    pdc[box] *= 1 - dep * 1e-6
                    ii = np.flatnonzero(box)
                    boxes.append((int(ii[0]), int(ii[-1])))
                cell = {}
                for label, k in (("declared", k_decl), ("calibrated", k_star)):
                    if k is None:
                        cell[label] = None
                        continue
                    found = _persistent_intervals(lc, sap, pdc, finite, window, k, -1, vmask)
                    rec = sum(any(a <= b1 and b0 <= bb for a, bb in found) for b0, b1 in boxes)
                    cell[label] = rec / len(boxes) if boxes else None
                comp[f"{int(dep)}ppm_{dur:g}h"] = {"depth_ppm": dep, "duration_h": dur, "n_injected": len(boxes), **cell}
        refkey = f"{int(ref['depth_ppm'])}ppm_{float(ref['duration_h']):g}h"
        depth90 = {}
        for dur in durs:
            for label in ("declared", "calibrated"):
                ok90 = [c["depth_ppm"] for c in comp.values() if c["duration_h"] == dur and (c.get(label) or 0) >= 0.9]
                depth90.setdefault(f"{dur:g}h", {})[label] = min(ok90) if ok90 else None
        per[pid] = {"null_events_by_k": {f"{k:g}": v for k, v in null.items()}, "k_star": k_star,
                    "k_star_at_grid_floor": at_floor, "depth_for_90pct_completeness_ppm": depth90, "completeness": comp,
                    "reference": {"cell": refkey, **{lab: comp.get(refkey, {}).get(lab) for lab in ("declared", "calibrated")}}}
        ctx.measure("calibrated_k_mad", (f"<= {k_star:g}" if at_floor else k_star) if k_star is not None else "none on grid",
                    unit="robust sigma",
                    method=f"sign-flip null, SAP∧PDCSAP at {window} d baseline, ≤{max_null} null events outside veto", products=[pid])
        ctx.measure("null_events_at_declared_k", null.get(k_decl, "k not on grid"), unit="count",
                    method=f"sign-flip null at k={k_decl}", products=[pid])
        rc = per[pid]["reference"]
        ctx.measure("depth_for_90pct_completeness", json.dumps(depth90), unit="ppm by duration",
                    method=f"smallest injected depth with ≥90% recovery; grid {depths} ppm", products=[pid])
        ctx.measure("completeness_reference_signal", json.dumps({"cell": refkey, "declared": rc["declared"], "calibrated": rc["calibrated"]}),
                    method=f"{n_inj} injected boxes per cell, seed {ctx.seed}", products=[pid])
        (ctx.product_dir(pid, lc) / "calibration.json").write_text(json.dumps(per[pid], indent=2), encoding="utf-8")
    # checks
    ks = [v["k_star"] for v in per.values()]
    kfmt = lambda v: "—" if v["k_star"] is None else (f"≤{v['k_star']:g}" if v["k_star_at_grid_floor"] else f"{v['k_star']:g}")
    if ks and all(k is not None for k in ks):
        worst = max(ks)
        state = "passed" if k_decl >= worst else "failed"
        ctx.check("Calibrated false-alarm threshold (sign-flip null)", state,
                  f"k* = {', '.join(kfmt(v) for v in per.values())} per light curve (≤{max_null} persistent null events outside the veto); "
                  f"declared k = {k_decl:g} " + ("is at or above it" if state == "passed"
                                                 else "is below it, so crossings at the declared k are expected from noise"))
    else:
        ctx.check("Calibrated false-alarm threshold (sign-flip null)", "inconclusive",
                  "no threshold on the grid reached the null-event limit for every light curve")
    refs = [v["reference"]["declared"] for v in per.values() if v["reference"]["declared"] is not None]
    if refs:
        lo = min(refs)
        ctx.check("Synthetic signal injection–recovery", "passed" if lo >= 0.9 else "inconclusive",
                  f"completeness for {ref['depth_ppm']} ppm, {ref['duration_h']} h boxes at the declared threshold: "
                  + ", ".join(f"{r:.0%}" for r in refs) + " per light curve (pass mark 90%)")
    d90 = []
    for v in per.values():
        dd = v["depth_for_90pct_completeness_ppm"].get(f"{float(ref['duration_h']):g}h", {}).get("declared")
        d90.append("none on grid" if dd is None else f"{dd / 1e4:g}%")
    ctx.note("Calibration on each light curve (sign-flip null, injection–recovery): k* " + ", ".join(kfmt(v) for v in per.values())
             + f"; at the declared k = {k_decl:g} the screen recovers ≥90% of {ref['duration_h']:g}-h dips only from depth "
             + ", ".join(d90) + f" (completeness for {ref['depth_ppm']} ppm: " + (", ".join(f"{r:.0%}" for r in refs) if refs else "n/a")
             + "). The null result excludes only dips deeper than that.")
    return {"per_product": per}


# ------------------------------------------------------------------ prior art
def step_prior_art(ctx, params: dict) -> dict:
    """Catalogue cross-match for every campaign target through the Known-Object Gate adapters."""
    from ..priorart import catalogue_audit

    targets = ctx.targets()
    radius = float(params.get("radius_arcsec", 30.0))
    services = params.get("services")
    out = {}
    for t in targets:
        res = catalogue_audit(t["ra_deg"], t["dec_deg"], radius_arcsec=radius, services=services)
        for svc, r in res.items():
            ctx.ledger.add_prior_art(service=svc, result=r["result"], gate="catalog", query=r["query"],
                                     candidate_id=f"target:{t['name']}", retrieved_utc=r["retrieved_utc"])
        out[t["name"]] = res
    states = [r["state"] for res in out.values() for r in res.values()]
    if states:
        ctx.check("Catalogue cross-match", "passed" if all(s == "done" for s in states) else "inconclusive",
                  f"{len(out)} target(s) × {len(states) // max(1, len(out))} services, radius {radius:g}″; "
                  f"{states.count('done')} answered, {len(states) - states.count('done')} errored; results in the ledger prior_art table")
    return {"targets": out}


# ------------------------------------------------------------------ target queue
def step_target_queue(ctx, params: dict) -> dict:
    from ..targets import build_queue

    q = build_queue(params)
    path = ctx.outdir / "target_queue.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(q["queue"][0].keys()) if q["queue"] else ["name"])
        w.writeheader()
        w.writerows(q["queue"])
    ctx.measure("target_pool_size", q["pool_size"], unit="count", method=q["query"])
    ctx.note(f"Target queue: {len(q['queue'])} of {q['pool_size']} pool members ranked by {q['ranking']['formula']}.")
    return {**q, "csv": ctx.rel(path)}


STEPS: dict[str, Callable[[Any, dict], dict]] = {
    "target_queue": step_target_queue,
    "fetch_products": step_fetch_products,
    "calibrate_screen": step_calibrate_screen,
    "residual_screen": step_residual_screen,
    "bls_recovery": step_bls_recovery,
    "prior_art": step_prior_art,
}
