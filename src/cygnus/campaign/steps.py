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


def _excluded(ctx) -> dict | None:
    """The ``fetch_products`` result when it found nothing (a documented exclusion), else None.

    A target with no available products is a recorded null, not a red run: steps that need
    products leave their checks ``not_tested`` with the exclusion note instead of raising.
    """
    res = ctx.optional_result("fetch_products", {}) or {}
    return res if res.get("excluded") else None


# ------------------------------------------------------------------ products
MAST_TIMEOUT_S = 120   # per MAST request; a hung service fails the step (retryable) instead of stalling it

def _discover_spoc_lcs(tic: int, max_products: int, t0_bjd: float | None = None) -> list[dict]:
    """SPOC 120-s light curves for a TIC id, via the MAST Observations API (astroquery).

    With ``t0_bjd`` (a catalogued transit), sectors whose observation window covers that epoch come
    first, so a known-signal check has the light curve it needs. Coverage uses MAST's ``t_min``/
    ``t_max`` (MJD); BJD - 2400000.5 differs from MJD by minutes, well inside a 27-d sector.

    Each SPOC 120-s timeseries observation's ``dataURL`` is its ``-s_lc.fits`` light curve, so the
    list comes from the one observation query; MAST's separate product-list service
    (``get_product_list``) is not needed and has hung for minutes at a time (2026-09-26).
    """
    from astroquery.mast import Observations, conf

    conf.timeout = MAST_TIMEOUT_S   # astroquery's default is 600 s per request
    obs = Observations.query_criteria(target_name=str(tic), obs_collection="TESS", provenance_name="SPOC",
                                      dataproduct_type="timeseries")
    if len(obs) == 0:
        return []
    out, seen = [], set()
    for o in obs:
        uri = str(o["dataURL"])
        fn = uri.rsplit("/", 1)[-1]
        if not fn.endswith("-s_lc.fits") or "fast" in fn or fn in seen:
            continue
        seen.add(fn)
        lo, hi = float(o["t_min"]), float(o["t_max"])
        covers = None if t0_bjd is None else bool(lo <= t0_bjd - 2400000.5 <= hi)
        out.append({"product_id": fn, "tic": tic, "sector": int(fn.split("-s")[1][:4]) if "-s0" in fn else None,
                    "data_uri": uri, "covers_known_epoch": covers})
    out.sort(key=lambda d: (not d["covers_known_epoch"], d["product_id"]))
    return out[:max_products]


def step_fetch_products(ctx, params: dict) -> dict:
    """Locate or download each product, verify it, and register it in the ledger.

    Pinned products (``input.products`` with ``expected_sha256``) must match exactly. Products
    discovered from a target queue are recorded with the SHA-256 of their first retrieval.
    """
    from ..ingest.netio import fetch_to_file

    wanted = [dict(p) for p in ctx.spec.get("input", {}).get("products", [])]
    q = params.get("from_queue")
    pool = []
    if q:
        pool += [(t, q) for t in ctx.result("target_queue")["queue"][: int(q.get("top", 5))]]
    ft = params.get("from_targets")
    if ft:
        pool += [(t, ft) for t in ctx.spec.get("targets", []) if t.get("tic")]
    for t, opts in pool:
        found = _discover_spoc_lcs(int(t["tic"]), int(opts.get("max_products_per_target", 2)), t.get("t0_bjd"))
        if not found:
            ctx.note(f"{t['name']}: no SPOC 120-s light curve found at MAST for TIC {t['tic']}.")
        for p in found:
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
                    "sector": p.get("sector"), "covers_known_epoch": p.get("covers_known_epoch")}
    if not out:
        note = "no products to analyse: none pinned and none found at MAST for the requested targets"
        ctx.note(note)
        ctx.check("Product integrity (SHA-256)", "not_tested", note)
        ctx.outcome = ("pipeline_check", None)   # a no-data target is a pipeline outcome, not a bound
        return {"products": {}, "excluded": True, "exclusion": note}
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
    for t in list(ctx.spec.get("targets", [])) + ctx.optional_result("target_queue", {}).get("queue", []):
        if t["name"] == prod["target"]:
            return t
    return None


def group_entries(entries: list[dict], n_windows: int) -> list[dict]:
    """Merge screen entries that overlap in time (entries repeat across baselines and flux types)
    into distinct events. ``persistent`` = seen in SAP and PDCSAP at two or more baselines."""
    out = []
    for e in sorted(entries, key=lambda e: e["start_time_stored"]):
        if out and e["start_time_stored"] <= out[-1]["_end"]:
            g = out[-1]
            g["_end"] = max(g["_end"], e["end_time_stored"])
            g["entries"].append(e)
        else:
            out.append({"_start": e["start_time_stored"], "_end": e["end_time_stored"], "entries": [e]})
    events = []
    for g in out:
        es = g["entries"]
        deepest = min(es, key=lambda e: e["median_fractional_residual"])
        fl, bl = sorted({e["flux_type"] for e in es}), sorted({e["detrend_days"] for e in es})
        events.append({"mid_time_BJD_like": deepest["mid_time_BJD_like"], "deepest_median_residual": deepest["median_fractional_residual"],
                       "max_cadences": max(e["n_cadences"] for e in es), "flux_types": fl, "baselines_days": bl,
                       "n_entries": len(es), "persistent": fl == ["PDCSAP", "SAP"] and len(bl) >= min(2, n_windows)})
    return events


# ------------------------------------------------------------------ residual screen
def _threshold(ctx, pid: str, k_param) -> tuple[float, str]:
    """The screen threshold for one light curve and where it came from. ``calibrated`` uses
    calibrate_screen's k*; when no grid value reached the null-event limit the declared k is used
    and labelled uncalibrated, so the run continues but the record says so."""
    if k_param != "calibrated":
        return float(k_param), "declared in campaign spec"
    cal = ctx.optional_result("calibrate_screen", {})
    if not cal:
        raise RuntimeError("k_mad 'calibrated' needs a calibrate_screen step before this one")
    k = (cal["per_product"].get(pid) or {}).get("k_star")
    if k is not None:
        return float(k), "calibrated (calibrate_screen)"
    decl = float(cal.get("declared_k", 5.0))
    return decl, "UNCALIBRATED: no k on the calibration grid met the null-event limit; declared k used"


def step_residual_screen(ctx, params: dict) -> dict:
    """Negative excursions ≥ k robust-MAD, ≥ min_cadences, SAP and PDCSAP, several baselines,
    outside the known-signal veto. Writes screen.json and normalized_series.csv per product."""
    if (ex := _excluded(ctx)):
        ctx.check("Calibrated false-alarm threshold (sign-flip null)", "not_tested", ex["exclusion"])
        ctx.check("Synthetic signal injection–recovery", "not_tested", ex["exclusion"])
        return {"per_product": {}, "entries_outside_veto_total": 0, "distinct_events_outside_veto_total": 0,
                "persistent_events_outside_veto_total": 0, "excluded": True}
    veto = ctx.spec.get("veto")
    windows = tuple(params.get("windows_days", (1.0, 2.0, 3.0)))
    k_decl = params.get("k_mad", 5.0)
    summary = {}
    for pid, prod in ctx.result("fetch_products")["products"].items():
        lc = read_spoc(resolve(prod["path"]))
        k, k_src = _threshold(ctx, pid, k_decl)
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
               "threshold": {"k_mad": k, "source": k_src}}
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
                                       + ("from the campaign's sign-flip calibration" if k_src.startswith("calibrated")
                                          else "is an uncalibrated screen unless calibrate_screen ran")
                                       + "; entries overlap across recipes and are not independent events.")
        (sub / "screen.json").write_text(json.dumps(res, indent=2, allow_nan=False), encoding="utf-8")
        outside = [e for e in events if not e["inside_veto"]]
        grouped = group_entries(outside, len(windows))
        summary[pid] = {"distinct_events_outside_veto": grouped,
                        "persistent_events_outside_veto": sum(g["persistent"] for g in grouped),"dir": ctx.rel(sub), "rows": res["rows"], "usable": res["usable"], "k_mad": k,
                        **({} if k_src.startswith(("calibrated", "declared")) else {"threshold_note": k_src}),
                        "entries": len(events), "entries_outside_veto": len(outside),
                        "outside_veto": [{k2: e[k2] for k2 in ("detrend_days", "flux_type", "mid_time_BJD_like", "n_cadences",
                                                               "median_fractional_residual")} for e in outside]}
        ctx.measure("screen_entries", len(events), unit="count", method=f"-{k} MAD, windows {list(windows)} d, SAP+PDCSAP", products=[pid])
        ctx.measure("screen_entries_outside_veto", len(outside), unit="count", method="same, outside known-signal veto", products=[pid])
    n_out = sum(s["entries_outside_veto"] for s in summary.values())
    n_ev = sum(len(s["distinct_events_outside_veto"]) for s in summary.values())
    n_pers = sum(s["persistent_events_outside_veto"] for s in summary.values())
    ctx.note(f"Residual screen: {n_out} threshold entr{'y' if n_out == 1 else 'ies'} outside the known-signal veto across "
             f"{len(summary)} light curve(s)" + (f", forming {n_ev} distinct event(s), {n_pers} persistent in SAP and PDCSAP at "
                                                 f"two or more baselines." if n_out else "."))
    if k_decl == "calibrated":
        cal = ctx.result("calibrate_screen")["per_product"]
        unc = [pid for pid in summary if cal.get(pid, {}).get("k_star") is None]
        kf = lambda c: "none" if c["k_star"] is None else (f"≤{c['k_star']:g}" if c["k_star_at_grid_floor"] else f"{c['k_star']:g}")
        ctx.check("Calibrated false-alarm threshold (sign-flip null)", "inconclusive" if unc else "passed",
                  "screen run at each light curve's own k* (" + ", ".join(kf(cal[pid]) for pid in summary) + "; ≤ "
                  f"{ctx.spec_step_param('calibrate_screen', 'max_null_events', 0)} persistent null events outside the veto)"
                  + (f"; {len(unc)} light curve(s) reached no k* on the grid and used the declared k, uncalibrated" if unc else ""))
        refs = [cal[pid]["reference"] for pid in summary if pid in cal]
        vals = [r.get("calibrated") for r in refs]
        if refs and all(v is not None for v in vals):
            ctx.check("Synthetic signal injection–recovery", "passed" if min(vals) >= 0.9 else "inconclusive",
                      f"completeness for the reference box ({refs[0]['cell']}) at each light curve's k*: "
                      + ", ".join(f"{v:.0%}" for v in vals) + " (pass mark 90%); 90%-completeness depths are in calibration.json")
    return {"per_product": summary, "entries_outside_veto_total": n_out, "distinct_events_outside_veto_total": n_ev,
            "persistent_events_outside_veto_total": n_pers}


# ------------------------------------------------------------------ BLS recovery
def step_bls_recovery(ctx, params: dict) -> dict:
    """Box least squares on one PDCSAP light curve plus a permutation diagnostic (as the 2026-09-24
    recovery test). Writes results.json in the campaign output directory."""
    import sys
    from datetime import datetime, timezone

    import astropy
    from astropy.timeseries import BoxLeastSquares

    if (ex := _excluded(ctx)):
        ctx.note(ex["exclusion"])
        return {"excluded": True, "exclusion": ex["exclusion"]}
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
    if (ex := _excluded(ctx)):
        ctx.check("Calibrated false-alarm threshold (sign-flip null)", "not_tested", ex["exclusion"])
        ctx.check("Synthetic signal injection–recovery", "not_tested", ex["exclusion"])
        return {"per_product": {}, "declared_k": float(params.get("declared_k", 5.0)), "excluded": True}
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
    return {"per_product": per, "declared_k": k_decl}


# ------------------------------------------------------------------ positive control: the catalogued signal
def _known_epochs(lc, veto: dict | None, target: dict | None) -> list[float]:
    """Catalogued transit times (BJD) inside this light curve's time span."""
    t = lc.time_bjd[np.isfinite(lc.time_bjd)]
    if not t.size or not veto:
        return []
    lo, hi = float(t.min()), float(t.max())
    if veto["kind"] == "single_epoch":
        t0 = (target or {}).get("t0_bjd", veto.get("t0_bjd"))
        return [float(t0)] if t0 is not None and lo <= float(t0) <= hi else []
    if veto["kind"] == "ephemeris":
        p, t0 = float(veto["period_days"]), float(veto["t0_bjd"])
        n = np.arange(math.ceil((lo - t0) / p), math.floor((hi - t0) / p) + 1)
        return [float(t0 + i * p) for i in n]
    return []


def step_known_signal_recovery(ctx, params: dict) -> dict:
    """Positive control on a known object: does the screen find the catalogued transit where the
    catalogue puts it, and how deep is it?

    For every light curve that covers a catalogued epoch (the target's ``t0_bjd`` for a single-epoch
    veto, every predicted transit for an ephemeris veto), run the residual screen *without* the veto
    at the calibrated threshold (or ``k_mad``). The epoch counts as recovered when entries in both SAP
    and PDCSAP overlap ±(duration/2 + ``epoch_tolerance_hours``). The in-transit depth is measured
    from the PDCSAP residual. No light curve covering the epoch leaves the check ``not_tested``;
    missing cadences at the epoch make it ``inconclusive``; covered, usable and not found makes it
    ``failed``. The catalogue depth is quoted beside the measurement but is not a pass mark: it comes
    from another reduction with its own dilution correction.
    """
    veto = ctx.spec.get("veto") or {}
    windows = tuple(params.get("windows_days", (1.0, 2.0, 3.0)))
    k_decl = params.get("k_mad", "calibrated")
    tol_d = float(params.get("epoch_tolerance_hours", 2.0)) / 24
    series_w = float(params.get("depth_window_days", 2.0))
    per, epochs_all = {}, []
    for pid, prod in ctx.result("fetch_products")["products"].items():
        lc = read_spoc(resolve(prod["path"]))
        target = _target_for(ctx, pid) or {}
        k, k_src = _threshold(ctx, pid, k_decl)
        dur_h = target.get("duration_h") or veto.get("duration_h")
        dur_d = float(dur_h) / 24 if dur_h else 2 / 24
        cat_depth = target.get("depth_ppm") or veto.get("depth_ppm")
        epochs = _known_epochs(lc, veto, target)
        entry = {"k_mad": k, "threshold_source": k_src, "target": target.get("name"),
                 "catalogue": {"epoch_source": "target t0_bjd" if veto.get("kind") == "single_epoch" else veto.get("source"),
                               "depth_ppm": cat_depth, "duration_h": dur_h},
                 "time_span_bjd": [float(np.nanmin(lc.time_bjd)), float(np.nanmax(lc.time_bjd))], "epochs": []}
        if epochs:
            events = screen_events(lc, windows_days=windows, k_mad=k, min_cadences=int(params.get("min_cadences", 2)))
            usable = lc.usable
            resid = local_resid(lc.pdc, usable, lc.cadence_s, series_w)
            for e in epochs:
                inwin = np.abs(lc.time_bjd - e) <= dur_d / 2
                n_in = int((inwin & usable).sum())
                lo, hi = e - dur_d / 2 - tol_d, e + dur_d / 2 + tol_d
                hits = [ev for ev in events if lc.time_bjd[ev["start_index"]] <= hi and lc.time_bjd[ev["stop_index"]] >= lo]
                fluxes = sorted({ev["flux_type"] for ev in hits})
                ep = {"epoch_bjd": e, "usable_in_transit_cadences": n_in, "screen_entries": len(hits), "flux_types": fluxes}
                if n_in >= 2:
                    near = (np.abs(lc.time_bjd - e) > dur_d) & (np.abs(lc.time_bjd - e) < dur_d + 1.0) & usable
                    depth = -float(np.nanmedian(resid[inwin & usable])) * 1e6
                    err = robust_sigma(resid[near]) * 1e6 / math.sqrt(n_in) if near.sum() > 10 else None
                    ep.update({"measured_depth_ppm": depth, "depth_err_ppm": err,
                               "depth_ratio_to_catalogue": depth / float(cat_depth) if cat_depth else None})
                    if hits:
                        mids = [float(np.nanmedian(lc.time_bjd[ev["start_index"]:ev["stop_index"] + 1])) for ev in hits]
                        ep["entry_offset_hours"] = float(np.median(mids) - e) * 24
                ep["state"] = ("gap" if n_in < 2 else "recovered" if fluxes == ["PDCSAP", "SAP"] else
                               "partial" if hits else "not_recovered")
                entry["epochs"].append(ep)
                epochs_all.append((pid, ep))
        per[pid] = entry
        for ep in entry["epochs"]:
            ctx.measure("known_epoch_state", ep["state"], method=f"-{k:g} MAD screen without veto, SAP and PDCSAP within "
                        f"±(dur/2 + {tol_d * 24:g} h) of catalogued epoch {ep['epoch_bjd']:.5f}", products=[pid])
            if "measured_depth_ppm" in ep:
                ctx.measure("known_transit_depth", ep["measured_depth_ppm"], unit="ppm",
                            method=f"median PDCSAP residual within ±dur/2 of the catalogued epoch ({series_w:g}-d running median)",
                            products=[pid], notes=f"catalogue depth {cat_depth} ppm; statistical error {ep.get('depth_err_ppm')}")
    states = [ep["state"] for _, ep in epochs_all]
    name = "Known-signal recovery (positive control)"
    if not states:
        ctx.check(name, "not_tested", "no retrieved light curve covers a catalogued transit epoch")
    else:
        def fmt(pid, ep):
            d, err, cat = ep.get("measured_depth_ppm"), ep.get("depth_err_ppm"), per[pid]["catalogue"]["depth_ppm"]
            out = f"BJD {ep['epoch_bjd']:.4f}: {ep['state'].replace('_', ' ')}"
            if d is not None:
                out += f", depth {d:.0f}" + (f" ± {err:.0f}" if err else "") + " ppm"
            if cat:
                out += f" (catalogue {float(cat):.0f} ppm)"
            return out
        if "recovered" in states:
            state = "passed"
        elif "not_recovered" in states and "partial" not in states:
            state = "failed"
        else:
            state = "inconclusive"
        ctx.check(name, state, "; ".join(fmt(pid, ep) for pid, ep in epochs_all))
        ctx.note(f"Positive control: catalogued transit {', '.join(s.replace('_', ' ') for s in sorted(set(states)))} "
                 f"({len(states)} covered epoch{'s' if len(states) != 1 else ''}).")
    return {"per_product": per, "states": states}


# ------------------------------------------------------------------ repeat events and period aliases
def step_period_aliases(ctx, params: dict) -> dict:
    """For a single-transit target: find screen events that look like a repeat of the catalogued
    transit, and for each list the periods ΔT/n still allowed by the retrieved light curves.

    A *repeat candidate* is a persistent screen event whose depth is within ``depth_ratio`` of the
    measured catalogued transit. For each, P_n = ΔT/n (``min_period_days`` ≤ P_n); an alias is
    *excluded* when a predicted transit falls on usable data (≥ ``min_coverage`` of the transit
    window) and the mean residual there is shallower than ``excluded_below`` × the catalogued depth.
    Aliases whose predicted transits all fall in gaps stay allowed. This constrains the period only
    within the retrieved sectors; it is not a posterior (no stellar density, no priors).
    """
    known = ctx.result("known_signal_recovery")["per_product"]
    screen = ctx.result("residual_screen")["per_product"]
    ref = [(pid, ep) for pid, v in known.items() for ep in v["epochs"] if ep["state"] == "recovered" and ep.get("measured_depth_ppm")]
    if not ref:
        ctx.check("Period aliases (repeat events)", "not_tested", "catalogued transit not recovered; no reference depth")
        return {"candidates": []}
    rpid, rep = ref[0]
    t0 = rep["epoch_bjd"] + (rep.get("entry_offset_hours") or 0) / 24
    ref_depth = rep["measured_depth_ppm"] * 1e-6
    tgt = _target_for(ctx, rpid) or {}
    dur_d = float(tgt.get("duration_h") or 2.0) / 24
    lo_r, hi_r = params.get("depth_ratio", [0.5, 2.0])
    pmin = float(params.get("min_period_days", 1.0))
    cover = float(params.get("min_coverage", 0.5))
    below = float(params.get("excluded_below", 0.3))
    # light curves and residuals once
    series = {}
    for pid, prod in ctx.result("fetch_products")["products"].items():
        lc = read_spoc(resolve(prod["path"]))
        series[pid] = (lc.time_bjd, lc.usable, local_resid(lc.pdc, lc.usable, lc.cadence_s, 2.0))
    cands = []
    for pid, v in screen.items():
        for ev in v.get("distinct_events_outside_veto", []):
            if not ev["persistent"]:
                continue
            t, u, r = series[pid]
            win = u & (np.abs(t - ev["mid_time_BJD_like"]) <= dur_d / 2)
            if win.sum() < 2:
                continue
            depth = -float(np.nanmedian(r[win]))
            if not (lo_r * rep["measured_depth_ppm"] * 1e-6 <= depth <= hi_r * rep["measured_depth_ppm"] * 1e-6):
                continue
            dT = abs(ev["mid_time_BJD_like"] - t0)
            aliases = []
            for n in range(1, int(dT / pmin) + 1):
                P = dT / n
                verdict, evidence = "allowed", []
                for qid, (tq, uq, rq) in series.items():
                    span = tq[np.isfinite(tq)]
                    k0, k1 = math.ceil((span.min() - t0) / P), math.floor((span.max() - t0) / P)
                    for k in range(k0, k1 + 1):
                        tp = t0 + k * P
                        if abs(tp - t0) < dur_d or abs(tp - ev["mid_time_BJD_like"]) < dur_d:
                            continue   # the two observed transits themselves
                        w = np.abs(tq - tp) <= dur_d / 2
                        n_w, n_u = int(w.sum()), int((w & uq).sum())
                        if n_w == 0 or n_u < cover * max(n_w, dur_d * 86400 / 120):
                            continue
                        d = -float(np.nanmedian(rq[w & uq]))
                        evidence.append({"product": qid, "predicted_bjd": tp, "usable_cadences": n_u, "depth_ppm": d * 1e6})
                        if d < below * ref_depth:
                            verdict = "excluded"
                a = {"n": n, "period_days": P, "verdict": verdict}
                if verdict == "allowed":
                    a["tested_epochs"] = evidence          # full evidence only where the alias survives
                else:
                    a["excluded_by"] = next(e for e in evidence if e["depth_ppm"] < below * ref_depth * 1e6)
                aliases.append(a)
            allowed = [a for a in aliases if a["verdict"] == "allowed"]
            cands.append({"product": pid, "event_bjd": ev["mid_time_BJD_like"], "depth_ppm": depth * 1e6,
                          "reference_depth_ppm": rep["measured_depth_ppm"], "delta_t_days": dT,
                          "n_aliases": len(aliases), "n_allowed": len(allowed),
                          "allowed_periods_days": [round(a["period_days"], 4) for a in allowed], "aliases": aliases})
            ctx.measure("repeat_event_delta_t", dT, unit="d", method="catalogued transit to persistent screen event of matching depth",
                        products=[rpid, pid])
            ctx.measure("allowed_period_aliases", len(allowed), unit="count",
                        method=f"P = ΔT/n ≥ {pmin:g} d not excluded by usable retrieved data", products=list(series))
    (ctx.outdir / "period_aliases.json").write_text(json.dumps({"reference_epoch_bjd": t0, "candidates": cands}, separators=(",", ":")),
                                                     encoding="utf-8")
    if cands:
        c = cands[0]
        shown = ", ".join(f"{p:g}" for p in c["allowed_periods_days"][:12]) + (" …" if c["n_allowed"] > 12 else "")
        ctx.check("Period aliases (repeat events)", "inconclusive",
                  f"{len(cands)} repeat-candidate event(s); first at BJD {c['event_bjd']:.4f}, ΔT = {c['delta_t_days']:.3f} d, "
                  f"{c['n_allowed']} of {c['n_aliases']} aliases P = ΔT/n ≥ {pmin:g} d allowed by the retrieved data ({shown} d)")
        ctx.flag_lead(f"Repeat candidate: a persistent event matching the catalogued depth at BJD {c['event_bjd']:.4f} "
                 f"(ΔT {c['delta_t_days']:.2f} d); {c['n_allowed']} period aliases remain. Unverified lead until vetted.")
    else:
        ctx.check("Period aliases (repeat events)", "not_tested", "no persistent screen event matches the catalogued depth")
    return {"candidates": [{k: v for k, v in c.items() if k != "aliases"} for c in cands],
            "file": ctx.rel(ctx.outdir / "period_aliases.json")}


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
    "known_signal_recovery": step_known_signal_recovery,
    "period_aliases": step_period_aliases,
    "prior_art": step_prior_art,
}
