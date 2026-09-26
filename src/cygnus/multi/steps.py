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

from .lightcurve import (contiguous_runs, in_veto, local_resid, phase_of, read_campaign_lc, read_spoc, robust_sigma,
                         screen_events)
from . import systematics

MAST_DOWNLOAD = "https://mast.stsci.edu/api/v0.1/Download/file?uri=mast%3ATESS%2Fproduct%2F{pid}"


def portable(path: Path) -> str:
    """Store scratch paths as ``scratch:<relative>`` so saved outputs carry no machine-specific paths."""
    from cygnus.config import scratch_dir

    root = scratch_dir().resolve()
    try:
        return "scratch:" + Path(path).resolve().relative_to(root).as_posix()
    except ValueError:
        return Path(path).name   # outside scratch: keep only the file name


def resolve(stored: str) -> Path:
    from cygnus.config import scratch_dir

    return scratch_dir() / stored[8:] if stored.startswith("scratch:") else Path(stored)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _excluded(ctx) -> dict | None:
    """The ``fetch_products`` result when it found nothing (a documented exclusion), else None.

    A target whose archives answered but hold no product is a recorded null, not a red run: steps
    that need products leave their checks ``not_tested`` with the exclusion note instead of raising
    (as the ``cygnus.campaign`` twin does). An archive that could not be queried is not an exclusion.
    """
    res = ctx.optional_result("fetch_products", {}) or {}
    return res if res.get("excluded") else None


# ------------------------------------------------------------------ products
# note markers that mean an archive could not answer (an outage or a misconfiguration), never "no data"
UNAVAILABLE_NOTE, DISCOVERY_FAILED_NOTE, NOT_FETCHED_NOTE = "archive unavailable", "discovery failed", "not fetched"
NOT_REGISTERED_NOTE = "is not registered"
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


def _read_lc(path, prod: dict):
    """Read a fetched product into the screen's light-curve shape, honouring its archive format.

    A pinned/discovered SPOC product keeps the exact old reader; anything from a
    non-MAST archive goes through the generic reader, which records which columns
    became SAP and PDCSAP.
    """
    fmt = prod.get("format") or "spoc_lc"
    if fmt in ("spoc_lc", "tess_lc") and prod.get("archive") in (None, "MAST"):
        try:
            return read_spoc(path)
        except ValueError:
            pass   # fall through to the generic reader
    return read_campaign_lc(path, fmt=fmt)


def _discover_via_adapters(ctx, t: dict, opts: dict) -> list[dict]:
    """Discover products for one target from every archive named in ``opts['archives']``.

    Returns a flat list of product dicts ready for the fetch loop. Each names its
    archive and format so the download and read paths can dispatch correctly. An
    archive that cannot be queried is recorded as a note (not tested), never as an
    empty result.
    """
    from .archives import base as _base

    names = opts.get("archives")
    if not names:
        return []
    target = _base.Target.from_mapping({**t, **{k: opts.get(k) for k in
                                                 ("t0_bjd", "period_days", "depth_ppm", "duration_h") if opts.get(k) is not None}})
    out = []
    for name in names:
        try:
            adapter = _base.get(name)
        except KeyError:
            ctx.note(f"{t['name']}: archive adapter {name!r} {NOT_REGISTERED_NOTE}; skipped.")
            continue
        per = dict(opts.get("options", {}).get(name, {}))
        if not adapter.row_limited:
            # a product count; catalogue adapters read ``limit`` as a TOP row cap and keep their own default
            per.setdefault("limit", int(opts.get("max_products_per_target", 3)))
        try:
            refs = adapter.discover(target, **per)
        except _base.AdapterUnavailable as exc:
            ctx.note(f"{t['name']}/{name}: {UNAVAILABLE_NOTE} — {exc}")
            continue
        except Exception as exc:  # noqa: BLE001
            ctx.note(f"{t['name']}/{name}: {DISCOVERY_FAILED_NOTE} — {type(exc).__name__}: {exc}")
            continue
        row_cap = None
        if adapter.row_limited:
            import inspect

            row_cap = per.get("limit", inspect.signature(adapter.discover).parameters["limit"].default)
        for ref in refs:
            d = ref.as_dict()
            rows = (d.get("extra") or {}).get("rows")
            if row_cap is not None and isinstance(rows, list) and len(rows) >= int(row_cap):
                d["truncated"] = f"{len(rows)} rows returned = the TOP {row_cap} cap; the table may be incomplete"
                ctx.note(f"{t['name']}/{name}: {ref.product_id} hit the TOP {row_cap} row cap; the table may be incomplete.")
            # flatten the adapter's extra fields (inline rows, ZTF cone parameters, sector, ...) so the fetch
            # loop hands them back to adapter.fetch as ProductRef.extra, not nested one level deeper
            for k, v in d.pop("extra", {}).items():
                d.setdefault(k, v)
            d["target"] = t["name"]
            d["tic"] = t.get("tic")
            d["archive"] = ref.archive
            out.append(d)
    return out


def step_fetch_products(ctx, params: dict) -> dict:
    """Locate or download each product, verify it, and register it in the ledger.

    Pinned products (``input.products`` with ``expected_sha256``) must match exactly. Products
    discovered from a target queue are recorded with the SHA-256 of their first retrieval. Products
    may come from any registered archive (``from_targets.archives``/``from_queue.archives``); MAST
    SPOC light curves keep their original discovery path when no archives are named.
    """
    from cygnus.ingest.netio import fetch_to_file

    from .archives import base as _base

    wanted = [dict(p) for p in ctx.spec.get("input", {}).get("products", [])]
    for p in wanted:
        p.setdefault("archive", "MAST")
        p.setdefault("format", "spoc_lc")
        p.setdefault("kind", _base.kind_for_format(p["format"]))
    q = params.get("from_queue")
    pool = []
    if q:
        pool += [(t, q) for t in ctx.result("target_queue")["queue"][: int(q.get("top", 5))]]
    ft = params.get("from_targets")
    if ft:
        pool += [(t, ft) for t in ctx.spec.get("targets", []) if t.get("tic") or ft.get("archives")]
    for t, opts in pool:
        # explicit archive selection goes through adapters; otherwise keep the MAST SPOC path
        if opts.get("archives"):
            found = _discover_via_adapters(ctx, t, opts)
            if not found:
                ctx.note(f"{t['name']}: no products discovered from archives {opts['archives']}.")
            wanted.extend(found)
        elif t.get("tic"):
            found = _discover_spoc_lcs(int(t["tic"]), int(opts.get("max_products_per_target", 2)), t.get("t0_bjd"))
            if not found:
                ctx.note(f"{t['name']}: no SPOC 120-s light curve found at MAST for TIC {t['tic']}.")
            for p in found:
                p["target"] = t["name"]
                p["archive"] = "MAST"
                p["format"] = "spoc_lc"
                p["kind"] = "lightcurve"
                wanted.append(p)
    from cygnus.config import scratch_dir

    # "scratch:<subdir>" keeps machine-specific paths out of committed specs
    dirs = [ctx.scratch] + [scratch_dir(d[8:]) if str(d).startswith("scratch:") else Path(d)
                            for d in params.get("search_dirs", [])]
    out = {}
    n_notes_before_fetch = len(ctx.notes)
    max_bytes = params.get("max_product_bytes")      # optional pre-download size gate (archives that state sizes)
    for p in wanted:
        pid = p["product_id"]
        archive = p.get("archive") or "MAST"
        if max_bytes and p.get("size_bytes") and int(p["size_bytes"]) > int(max_bytes):
            ctx.note(f"{p.get('target') or pid}/{archive}: {pid} skipped before download — archive states "
                     f"{int(p['size_bytes'])} bytes > max_product_bytes {int(max_bytes)}.")
            continue
        fmt = p.get("format") or "spoc_lc"
        # namespace scratch file names by archive so same-named products cannot collide
        fname = pid if archive == "MAST" else f"{archive}__{pid}"
        # an inline product is a query result carried by discovery: always rewrite it, so a cached file from an
        # earlier (different or truncated) query is never reused under the same name
        path = None if p.get("inline") else next((d / fname for d in dirs if (d / fname).is_file()), None)
        fetched = False
        if path is None:
            path = ctx.scratch / fname
            url = p.get("url")
            if archive.upper() == "MAST" and not url:
                url = MAST_DOWNLOAD.format(pid=pid)
            try:
                adapter = _base.get(archive.lower() if archive.lower() in _base.available() else archive)
            except KeyError:
                adapter = None
            # a bare MAST product with no explicit URL keeps the original downloader
            if url and (archive.upper() == "MAST" or adapter is None):
                fetch_to_file(url, path, timeout_s=120)
            elif adapter is not None:
                extra = {k: v for k, v in p.items()
                         if k not in ("product_id", "url", "format", "expected_sha256", "description", "target")}
                try:
                    adapter.fetch(_base.ProductRef(archive=archive, product_id=pid, url=url, format=fmt,
                                                   expected_sha256=p.get("expected_sha256"), extra=extra),
                                  path, timeout_s=120)
                except _base.AdapterUnavailable as exc:
                    # e.g. observing routes (a request queue, nothing archived yet): a note, not a crash
                    ctx.note(f"{p.get('target') or pid}/{archive}: {NOT_FETCHED_NOTE} — {exc}")
                    continue
            else:
                raise RuntimeError(f"{pid}: no URL and no adapter for archive {archive!r}")
            fetched = True
        digest, size = _sha256(path), path.stat().st_size
        if p.get("expected_sha256") and (digest != p["expected_sha256"] or
                                         (p.get("expected_bytes") and size != int(p["expected_bytes"]))):
            raise RuntimeError(f"{pid}: checksum/size mismatch (sha256 {digest}, {size} bytes); refusing to analyse")
        if not ctx.ledger_has_product(archive, pid):
            ledger_url = p.get("url") or (MAST_DOWNLOAD.format(pid=pid) if archive.upper() == "MAST" else None)
            ctx.ledger.add_product(archive, pid, url=ledger_url, local_path=path,
                                   checksum=digest, license_=p.get("license", "see DATA_SOURCES.md"),
                                   extra={"campaign": ctx.campaign_id, "tic": p.get("tic"),
                                          "sector": p.get("sector"), "format": fmt})
        out[pid] = {"path": portable(path), "sha256": digest, "bytes": size, "fetched_now": fetched,
                    "pinned": bool(p.get("expected_sha256")), "target": p.get("target"), "tic": p.get("tic"),
                    "sector": p.get("sector"), "covers_known_epoch": p.get("covers_known_epoch"),
                    "archive": archive, "format": fmt, "url": p.get("url"),
                    "kind": p.get("kind") or _base.kind_for_format(fmt),
                    "description": p.get("description", ""),
                    **({"truncated": p["truncated"]} if p.get("truncated") else {})}
    if not out:
        detail = "; ".join(ctx.notes[-4:]) if ctx.notes else "no archives produced a product"
        # every archive answered and none holds a product: a documented exclusion. An archive that
        # could not be queried or fetched (an outage) is a failure, so a retry can still find data.
        outage = any(m in n for n in ctx.notes for m in (UNAVAILABLE_NOTE, DISCOVERY_FAILED_NOTE, NOT_FETCHED_NOTE, NOT_REGISTERED_NOTE))
        if outage or not pool or len(ctx.notes) > n_notes_before_fetch:
            raise RuntimeError(f"no products to analyse (none pinned, none discovered) — {detail}")
        note = "no products to analyse: none pinned and none found for the requested targets (" + detail + ")"
        ctx.note(note)
        ctx.check("Product integrity (SHA-256)", "not_tested", note)
        ctx.outcome = ("pipeline_check", None)   # a no-data target is a pipeline outcome, not a bound
        return {"products": {}, "lightcurve_products": [], "excluded": True, "exclusion": note}
    archives = sorted({v["archive"] for v in out.values()})
    # the residual screen needs a densely sampled series: an empty or sparse/irregular light curve
    # (e.g. a ZTF magnitude series of a bright star) stays a fetched product but is not screened
    min_usable = int(params.get("min_usable_cadences", 100))
    max_cadence = float(params.get("max_cadence_s", 1800.0))
    unsuitable = {}
    for pid, v in out.items():
        if v["kind"] != "lightcurve":
            continue
        try:
            lc = _read_lc(resolve(v["path"]), v)
            n_ok, cad = int(lc.usable.sum()), float(lc.cadence_s)
            why = (f"{n_ok} usable cadence(s) < {min_usable}" if n_ok < min_usable else
                   f"cadence {cad:.0f} s > {max_cadence:.0f} s (sparse/irregular sampling; the contiguous-cadence "
                   "screen does not apply)" if cad > max_cadence else None)
            v["screen_suitability"] = {"usable_cadences": n_ok, "cadence_s": cad, "screenable": why is None,
                                       **({"reason": why} if why else {})}
        except Exception as exc:  # noqa: BLE001 - an unreadable product is reported, not screened
            why = f"unreadable as a light curve: {type(exc).__name__}: {str(exc)[:160]}"
            v["screen_suitability"] = {"screenable": False, "reason": why}
        if why:
            unsuitable[pid] = why
            ctx.note(f"{pid}: not screened — {why}.")
    lightcurves = [pid for pid, v in out.items() if v["kind"] == "lightcurve" and pid not in unsuitable]
    if any(v["kind"] == "lightcurve" for v in out.values()):
        ctx.check("Light-curve suitability for the residual screen", "passed" if not unsuitable else "inconclusive",
                  f"{len(lightcurves)} light curve(s) screenable"
                  + (f"; {len(unsuitable)} excluded: " + "; ".join(f"{k}: {w}" for k, w in list(unsuitable.items())[:3])
                     if unsuitable else ""))
    ctx.check("Product integrity (SHA-256)", "passed",
              f"{len(out)} product(s) from {', '.join(archives)} verified; pinned checksums matched"
              if any(v["pinned"] for v in out.values())
              else f"{len(out)} product(s) from {', '.join(archives)} checksummed at first retrieval")
    if not lightcurves:
        ctx.note("No light-curve product was retrieved; only image/table/text products are available to screen."
                 if not any(v["kind"] == "lightcurve" for v in out.values()) else
                 "Every retrieved light curve was unsuitable for the residual screen (reasons above); none was screened.")
    return {"products": out, "lightcurve_products": lightcurves}


def _lightcurve_products(ctx) -> dict[str, dict]:
    """The fetched products that are analysable time series, keyed by product id.

    Image, table and text products are context only; the screen steps never try to
    read them as light curves. Falling back to all products keeps old specs, whose
    entries predate the ``kind`` field, working.
    """
    prods = ctx.result("fetch_products")["products"]
    lc = ctx.optional_result("fetch_products", {}).get("lightcurve_products")
    if lc is None:
        return prods
    return {pid: prods[pid] for pid in lc if pid in prods}


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


def _channel_info(lc) -> dict:
    return (getattr(lc, "primary", None) or {}).get("_channels", {})


def _independent(lc) -> bool:
    """Whether the two channels are genuinely different reductions.

    A single-channel archive product (e.g. a CSV with one flux column) is read with
    ``sap == pdc`` and ``independent=False``; the screen then treats it as one
    channel and says so, instead of pretending to have an independent check.
    """
    return bool(_channel_info(lc).get("independent", True))


def _screen_channels(lc):
    """The (label, flux) pairs to screen: SAP+PDCSAP when independent, else the single channel."""
    if _independent(lc):
        return (("SAP", lc.sap), ("PDCSAP", lc.pdc))
    return ((_channel_info(lc).get("pdc") or "FLUX", lc.pdc),)


def group_entries(entries: list[dict], n_windows: int, *, single_channel: bool = False) -> list[dict]:
    """Merge screen entries that overlap in time (entries repeat across baselines and flux types)
    into distinct events. ``persistent`` = seen in SAP and PDCSAP at two or more baselines; for a
    single-channel product persistence is only repeatability across baselines, and is labelled so.
    """
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
        enough_baselines = len(bl) >= min(2, n_windows)
        persistent = (enough_baselines and fl == ["PDCSAP", "SAP"]) or (single_channel and enough_baselines)
        events.append({"mid_time_BJD_like": deepest["mid_time_BJD_like"], "deepest_median_residual": deepest["median_fractional_residual"],
                       "max_cadences": max(e["n_cadences"] for e in es), "span_days": float(g["_end"] - g["_start"]),
                       "flux_types": fl, "baselines_days": bl,
                       "n_entries": len(es), "persistent": persistent,
                       "persistence_basis": "baseline repeatability (single channel; not independent)" if single_channel
                                            else "SAP and PDCSAP at >=2 baselines"})
    return events


# ------------------------------------------------------------------ residual screen
def significance_state(fap: float, empirical_p: float, n_random: int) -> tuple[str, bool]:
    """Check state for a single-channel event's red-noise significance.

    ``passed`` needs both the parametric trial-corrected FAP ≤ 0.01 *and* empirical agreement (at
    most one random epoch of the same light curve as deep as the event): the parametric value is a
    Gaussian tail and alone cannot pass an event. FAP ≤ 0.1, or a parametric pass the empirical
    test does not confirm, is ``inconclusive``; otherwise ``failed``.
    """
    agrees = empirical_p <= 2.0 / (n_random + 1)
    if fap <= 0.01 and agrees:
        return "passed", agrees
    return ("inconclusive" if fap <= 0.1 else "failed"), agrees


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
    for pid, prod in _lightcurve_products(ctx).items():
        lc = _read_lc(resolve(prod["path"]), prod)
        k, k_src = _threshold(ctx, pid, k_decl)
        target = _target_for(ctx, pid)
        vmask, ph = _veto_mask(lc, veto, target)
        finite = lc.usable
        single = not _independent(lc)
        events = []
        for e in screen_events(lc, windows_days=windows, k_mad=k, min_cadences=int(params.get("min_cadences", 2)),
                               channels=_screen_channels(lc)):
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
               "channel_mode": "single channel (no independent comparison)" if single else "SAP and PDCSAP",
               "channels": _channel_info(lc),
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
        outside = [e for e in events if not e["inside_veto"]]
        grouped = group_entries(outside, len(windows), single_channel=single)
        try:
            sysmod = systematics.product_summary(lc, lc.pdc, grouped,
                                                 seed=int(ctx.seed or 0) + 1,
                                                 n_random=int(params.get("rednoise_trials", 300)))
        except Exception as exc:  # noqa: BLE001 - the noise model must not break the screen
            sysmod = {"error": f"{type(exc).__name__}: {str(exc)[:200]}"}
        res["systematics_model"] = sysmod
        (sub / "screen.json").write_text(json.dumps(res, indent=2, allow_nan=False), encoding="utf-8")
        summary[pid] = {"distinct_events_outside_veto": grouped,
                        "persistent_events_outside_veto": sum(g["persistent"] for g in grouped),"dir": ctx.rel(sub), "rows": res["rows"], "usable": res["usable"], "k_mad": k,
                        "channel_mode": "single" if single else "SAP+PDCSAP",
                        "systematics_model": sysmod,
                        **({} if k_src.startswith(("calibrated", "declared")) else {"threshold_note": k_src}),
                        "entries": len(events), "entries_outside_veto": len(outside),
                        "outside_veto": [{k2: e[k2] for k2 in ("detrend_days", "flux_type", "mid_time_BJD_like", "n_cadences",
                                                               "median_fractional_residual")} for e in outside]}
        ctx.measure("screen_entries", len(events), unit="count",
                    method=f"-{k} MAD, windows {list(windows)} d, " +
                           ("single channel (not independent)" if single else "SAP+PDCSAP"), products=[pid])
        ctx.measure("screen_entries_outside_veto", len(outside), unit="count", method="same, outside known-signal veto", products=[pid])
    n_out = sum(s["entries_outside_veto"] for s in summary.values())
    n_ev = sum(len(s["distinct_events_outside_veto"]) for s in summary.values())
    n_pers = sum(s["persistent_events_outside_veto"] for s in summary.values())
    ctx.note(f"Residual screen: {n_out} threshold entr{'y' if n_out == 1 else 'ies'} outside the known-signal veto across "
             f"{len(summary)} light curve(s)" + (f", forming {n_ev} distinct event(s), {n_pers} persistent in SAP and PDCSAP at "
                                                 f"two or more baselines." if n_out else "."))
    single_pids = [pid for pid, s in summary.items() if s.get("channel_mode") == "single"]
    if single_pids:
        strongest = None
        for pid in single_pids:
            st = (summary[pid].get("systematics_model") or {}).get("strongest")
            fap_of = lambda s: 1.0 if s["trial_corrected_fap"] is None else s["trial_corrected_fap"]
            if st and (strongest is None or fap_of(st) < fap_of(strongest)):
                strongest = {**st, "product": pid}
        if strongest is None:
            ctx.check("Single-channel event significance (red noise)", "not_tested",
                      f"{len(single_pids)} single-channel product(s); no event outside the veto to assess")
        else:
            fap = strongest["trial_corrected_fap"]
            if fap is None:
                ctx.check("Single-channel event significance (red noise)", "inconclusive",
                          f"strongest {strongest['product']} event BJD {strongest['event_bjd']:.4f}: "
                          "the red-noise model could not assign a parametric significance")
            else:
                state, empirical_agrees = significance_state(fap, strongest["empirical_p"], strongest["n_random"])
                ctx.check("Single-channel event significance (red noise)", state,
                          f"strongest {strongest['product']} event BJD {strongest['event_bjd']:.4f}: box "
                          f"{strongest['box_statistic']:+.4f}, z vs random-epoch null "
                          f"{strongest['parametric_z']:+.1f}, empirical p {strongest['empirical_p']:.3g}, "
                          f"FAP {fap:.3g} (n_eff {strongest['n_effective_trials']:.0f}, tau {strongest['tau_days']})"
                          + ("" if empirical_agrees else "; the empirical random-epoch test does not confirm it"))
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
    lc = _read_lc(resolve(prod["path"]), prod)
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
def _persistent_intervals(lc, sap, pdc, finite, window_days, k, sign, veto_mask, *, single=False):
    """Intervals flagged at one baseline, outside the veto. Returns index pairs.

    Multi-channel: flagged in BOTH SAP and PDCSAP (the persistence rule). Single-channel:
    flagged in the one channel, with the loss of independence carried by the caller.
    """
    flags = []
    for flux in ((pdc,) if single else (sap, pdc)):
        rr = local_resid(flux, finite, lc.cadence_s, window_days)
        sig = robust_sigma(rr[finite])
        hit = finite & np.isfinite(rr) & ((rr < -k * sig) if sign < 0 else (rr > k * sig))
        flags.append(hit)
    both = flags[0] & flags[1] & ~veto_mask if not single else flags[0] & ~veto_mask
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
    for pid, prod in _lightcurve_products(ctx).items():
        lc = _read_lc(resolve(prod["path"]), prod)
        finite = lc.usable
        single = not _independent(lc)
        vmask, _ = _veto_mask(lc, veto, _target_for(ctx, pid))
        null = {k: len(_persistent_intervals(lc, lc.sap, lc.pdc, finite, window, k, +1, vmask, single=single)) for k in grid}
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
                    found = _persistent_intervals(lc, sap, pdc, finite, window, k, -1, vmask, single=single)
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
                    "channel_mode": "single" if single else "SAP+PDCSAP",
                    "reference": {"cell": refkey, **{lab: comp.get(refkey, {}).get(lab) for lab in ("declared", "calibrated")}}}
        ctx.measure("calibrated_k_mad", (f"<= {k_star:g}" if at_floor else k_star) if k_star is not None else "none on grid",
                    unit="robust sigma",
                    method=f"sign-flip null, {'single channel' if single else 'SAP∧PDCSAP'} at {window} d baseline, "
                           f"≤{max_null} null events outside veto", products=[pid])
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
    for pid, prod in _lightcurve_products(ctx).items():
        lc = _read_lc(resolve(prod["path"]), prod)
        target = _target_for(ctx, pid) or {}
        k, k_src = _threshold(ctx, pid, k_decl)
        dur_h = target.get("duration_h") or veto.get("duration_h")
        dur_d = float(dur_h) / 24 if dur_h else 2 / 24
        cat_depth = target.get("depth_ppm") or veto.get("depth_ppm")
        epochs = _known_epochs(lc, veto, target)
        single = not _independent(lc)
        entry = {"k_mad": k, "threshold_source": k_src, "target": target.get("name"),
                 "channel_mode": "single" if single else "SAP+PDCSAP",
                 "catalogue": {"epoch_source": "target t0_bjd" if veto.get("kind") == "single_epoch" else veto.get("source"),
                               "depth_ppm": cat_depth, "duration_h": dur_h},
                 "time_span_bjd": [float(np.nanmin(lc.time_bjd)), float(np.nanmax(lc.time_bjd))], "epochs": []}
        if epochs:
            events = screen_events(lc, windows_days=windows, k_mad=k, min_cadences=int(params.get("min_cadences", 2)),
                                   channels=_screen_channels(lc))
            usable = lc.usable
            resid = local_resid(lc.pdc, usable, lc.cadence_s, series_w)
            required = {label for label, _ in _screen_channels(lc)}
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
                ep["state"] = ("gap" if n_in < 2 else "recovered" if set(fluxes) >= required else
                               "partial" if hits else "not_recovered")
                entry["epochs"].append(ep)
                epochs_all.append((pid, ep))
        per[pid] = entry
        for ep in entry["epochs"]:
            ctx.measure("known_epoch_state", ep["state"], method=f"-{k:g} MAD screen without veto, "
                        f"{'single channel' if single else 'SAP and PDCSAP'} within "
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
    Aliases whose predicted transits all fall in gaps stay allowed. The exclusion constrains the
    period only within the retrieved sectors and uses no priors. When ``stellar_context`` ran first
    with usable Gaia priors, each candidate also carries ``duration_likelihood``: how well each allowed
    alias's circular-orbit transit duration matches the catalogued one, given the stellar density
    (``measures.alias_duration_likelihood``; its assumptions are listed beside the numbers).
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
    series, cadence_s = {}, {}
    for pid, prod in _lightcurve_products(ctx).items():
        lc = _read_lc(resolve(prod["path"]), prod)
        series[pid] = (lc.time_bjd, lc.usable, local_resid(lc.pdc, lc.usable, lc.cadence_s, 2.0))
        cadence_s[pid] = float(lc.cadence_s) if lc.cadence_s and lc.cadence_s > 0 else 120.0
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
                        # coverage relative to the cadences a full transit window holds at this product's cadence
                        if n_w == 0 or n_u < cover * max(n_w, dur_d * 86400 / cadence_s[qid]):
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
            if ctx.optional_result("stellar_context", None) is not None:
                from .measure_steps import duration_likelihood_for

                dl = duration_likelihood_for(ctx, tgt or {}, [a["period_days"] for a in allowed], params)
                if dl is not None:
                    cands[-1]["duration_likelihood"] = dl
            ctx.measure("repeat_event_delta_t", dT, unit="d", method="catalogued transit to persistent screen event of matching depth",
                        products=[rpid, pid])
            ctx.measure("allowed_period_aliases", len(allowed), unit="count",
                        method=f"P = ΔT/n ≥ {pmin:g} d not excluded by usable retrieved data", products=list(series))
    (ctx.outdir / "period_aliases.json").write_text(json.dumps({"reference_epoch_bjd": t0, "candidates": cands}, separators=(",", ":")),
                                                     encoding="utf-8")
    if cands:
        c = cands[0]
        shown = ", ".join(f"{p:g}" for p in c["allowed_periods_days"][:12]) + (" …" if c["n_allowed"] > 12 else "")
        dl = c.get("duration_likelihood")
        best = (max(dl["aliases"], key=lambda a: a["weight_likelihood_only"] or 0) if dl and dl["aliases"] else None)
        ctx.check("Period aliases (repeat events)", "inconclusive",
                  f"{len(cands)} repeat-candidate event(s); first at BJD {c['event_bjd']:.4f}, ΔT = {c['delta_t_days']:.3f} d, "
                  f"{c['n_allowed']} of {c['n_aliases']} aliases P = ΔT/n ≥ {pmin:g} d allowed by the retrieved data ({shown} d)"
                  + (f"; duration likelihood under Gaia priors (circular orbits) peaks at {best['period_days']:.3g} d "
                     f"(weight {best['weight_likelihood_only']:.2f})" if best and best["weight_likelihood_only"] else ""))
        ctx.flag_lead(f"Repeat candidate: a persistent event matching the catalogued depth at BJD {c['event_bjd']:.4f} "
                 f"(ΔT {c['delta_t_days']:.2f} d); {c['n_allowed']} period aliases remain. Unverified lead until vetted.")
    else:
        ctx.check("Period aliases (repeat events)", "not_tested", "no persistent screen event matches the catalogued depth")
    return {"candidates": [{k: v for k, v in c.items() if k != "aliases"} for c in cands],
            "file": ctx.rel(ctx.outdir / "period_aliases.json")}


# ------------------------------------------------------------------ prior art
def step_prior_art(ctx, params: dict) -> dict:
    """Catalogue cross-match for every campaign target through the Known-Object Gate adapters."""
    from cygnus.priorart import catalogue_audit

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
    from cygnus.targets import build_queue

    q = build_queue(params)
    path = ctx.outdir / "target_queue.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(q["queue"][0].keys()) if q["queue"] else ["name"])
        w.writeheader()
        w.writerows(q["queue"])
    ctx.measure("target_pool_size", q["pool_size"], unit="count", method=q["query"])
    ctx.note(f"Target queue: {len(q['queue'])} of {q['pool_size']} pool members ranked by {q['ranking']['formula']}.")
    return {**q, "csv": ctx.rel(path)}


# ------------------------------------------------------------------ context products
def step_context_products(ctx, params: dict) -> dict:
    """Record the non-light-curve products a multi-archive fetch retrieved.

    A campaign that names several archives usually gets context as well as time
    series: Gaia neighbours, a SkyView/Legacy cutout, NED matches. Those are read
    (so a malformed file is caught) and summarised — row counts, image shapes,
    byte sizes — but they are never screened as light curves. Writes
    ``context.json``; the check is ``not_tested`` when the campaign fetched no
    context products, rather than ``passed`` on an empty set.
    """
    from .readers import read_product

    prods = ctx.result("fetch_products")["products"]
    others = {pid: p for pid, p in prods.items() if p.get("kind") != "lightcurve"}
    out = {}
    for pid, p in others.items():
        entry = {"archive": p["archive"], "format": p["format"], "kind": p.get("kind"),
                 "description": p.get("description", ""), "bytes": p.get("bytes"), "sha256": p.get("sha256")}
        try:
            obj = read_product(resolve(p["path"]), fmt=p["format"])
            if isinstance(obj, dict) and "rows" in obj:
                entry.update({"n_rows": int(obj["rows"] if isinstance(obj["rows"], int) else len(obj["rows"])),
                              "columns": [str(c) for c in obj.get("columns", [])][:20]})
            elif isinstance(obj, dict) and "shape" in obj:
                entry.update({"image_shape": [int(s) for s in obj["shape"]]})
                phot = _cutout_photometry(ctx, pid, obj, float(params.get("aperture_arcsec", 5.0)))
                if phot:
                    entry["photometry"] = phot
                    for b in phot.get("bands", []):
                        if b.get("mag") is not None:
                            ctx.measure("cutout_aperture_mag", b["mag"], unit="mag",
                                        method=f"{b['band']}: {phot['aperture_arcsec']:g}\" aperture, annulus sky; {b['zeropoint']}",
                                        products=[pid])
            elif isinstance(obj, dict) and "text" in obj:
                entry.update({"text_bytes": len(obj["text"])})
            else:
                entry.update({"object": type(obj).__name__})
        except Exception as exc:  # noqa: BLE001 - a context product that will not read is recorded as such
            entry["read_error"] = f"{type(exc).__name__}: {str(exc)[:200]}"
        out[pid] = entry
        ctx.measure("context_product_bytes", int(p.get("bytes") or 0), unit="byte",
                    method="fetched context product size", products=[pid])
    (ctx.outdir / "context.json").write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    if others:
        kinds = sorted({v["kind"] for v in others.values()})
        errs = [pid for pid, v in out.items() if "read_error" in v]
        ctx.check("Context products read", "passed" if not errs else "inconclusive",
                  f"{len(others)} non-light-curve product(s) ({', '.join(kinds)}) recorded in context.json"
                  + (f"; {len(errs)} failed to read: {', '.join(errs[:3])}" if errs else ""))
    else:
        ctx.check("Context products read", "not_tested", "the campaign fetched no non-light-curve products")
    return {"products": out, "file": ctx.rel(ctx.outdir / "context.json")}


def _cutout_photometry(ctx, pid: str, img: dict, aperture_arcsec: float) -> dict | None:
    """Aperture photometry of the target on an image cutout with a celestial WCS.

    Magnitudes only where the header states a zero point (Legacy Survey/SDSS nanomaggies, 2MASS
    MAGZP); otherwise instrumental counts. A 3-D cutout (one plane per band, as Legacy Survey
    returns) is measured plane by plane, named from ``BAND<i>`` keywords when present. Colours are
    formed only between calibrated bands of the same product.
    """
    from . import measures as _m

    wcs, data, hdr = img.get("wcs"), np.asarray(img["data"], float), img["header"]
    tgt = _target_for(ctx, pid) or next((t for t in ctx.spec.get("targets", []) if t.get("ra_deg") is not None), None)
    if tgt is None:
        return None
    if wcs is None:
        return {"measured": False, "reason": img.get("wcs_note") or "no celestial WCS"}
    x, y = (float(v) for v in wcs.celestial.world_to_pixel_values(float(tgt["ra_deg"]), float(tgt["dec_deg"])))
    try:
        from astropy.wcs.utils import proj_plane_pixel_scales

        scale = float(np.mean(np.abs(proj_plane_pixel_scales(wcs.celestial))) * 3600)   # arcsec per pixel (plain degrees)
    except Exception:  # noqa: BLE001
        return {"measured": False, "reason": "pixel scale unreadable from the WCS"}
    r = aperture_arcsec / scale
    zp, zp_note = _m.image_zeropoint(hdr)
    planes = [data] if data.ndim == 2 else list(data) if data.ndim == 3 else []
    bands = []
    for i, plane in enumerate(planes):
        name = str(hdr.get(f"BAND{i}", "")).strip() or (str(hdr.get("FILTER", "")).strip() if len(planes) == 1 else f"plane{i}")
        ph = _m.aperture_photometry(plane, x, y, r, 2.5 * r, 4 * r)
        b = {"band": name or "unnamed", **ph, "zeropoint": zp_note, "mag": None}
        if ph.get("measured") and zp is not None and ph["flux"] > 0:
            b["mag"] = zp - 2.5 * math.log10(ph["flux"])
            b["mag_err"] = 1.0857 * ph["flux_err_sky"] / ph["flux"] if ph["flux_err_sky"] else None
        bands.append(b)
    cal = [b for b in bands if b["mag"] is not None]
    colours = {f"{a['band']}-{c['band']}": a["mag"] - c["mag"] for i, a in enumerate(cal) for c in cal[i + 1:]}
    return {"measured": any(b.get("measured") for b in bands), "target_pixel_xy": [x, y], "pixel_scale_arcsec": scale,
            "aperture_arcsec": aperture_arcsec, "bands": bands, "colours": colours,
            "caveat": "blended light inside the aperture is included; no aperture correction"}


# ------------------------------------------------------------------ per-source checks
def _aggregate_state(states: list[str]) -> str:
    if not states:
        return "not_tested"
    for s in ("failed", "inconclusive", "not_tested"):
        if s in states:
            return s
    return "passed"


def step_source_checks(ctx, params: dict) -> dict:
    """Run each archive adapter's own checks on its fetched products.

    This is where per-source vetting lives: Gaia returns astrometric fidelity
    flags, MAST its quality-flag census, MPC the observation count from its data
    API, catalogue adapters the nearest match, image archives the finite-pixel and
    background census. One check per archive is written to the sky record; the full
    per-product detail goes to ``source_checks.json``. An archive with no
    registered adapter, or a check that raises, is recorded as not tested or
    inconclusive — never passed.
    """
    from .archives import base as _base

    prods = ctx.result("fetch_products")["products"]
    out: dict[str, list[dict]] = {}
    by_archive: dict[str, list[str]] = {}
    for pid, p in prods.items():
        archive = p.get("archive") or "MAST"
        fmt = p.get("format") or "spoc_lc"
        try:
            adapter = _base.get(archive.lower() if archive.lower() in _base.available() else archive)
        except KeyError:
            checks = [{"name": f"{archive} adapter", "state": "not_tested", "note": "no adapter registered"}]
        else:
            target = _target_for(ctx, pid)
            tgt = _base.Target.from_mapping(target) if target else None
            ref = _base.ProductRef(archive=archive, product_id=pid, url=p.get("url"), format=fmt,
                                   kind=p.get("kind") or _base.kind_for_format(fmt),
                                   expected_sha256=p.get("sha256"))
            try:
                checks = [c.as_dict() for c in adapter.source_checks(tgt, ref, resolve(p["path"]), p)]
            except Exception as exc:  # noqa: BLE001
                checks = [{"name": f"{archive} source checks", "state": "inconclusive",
                           "note": f"{type(exc).__name__}: {str(exc)[:200]}"}]
        if p.get("truncated"):
            checks.append({"name": f"{archive} row cap", "state": "inconclusive", "note": p["truncated"]})
        out[pid] = checks
        by_archive.setdefault(archive, []).extend(c["state"] for c in checks)
        for c in checks:
            ctx.measure("source_check", c["state"], method=f"{archive}: {c['name']}", products=[pid], notes=c.get("note"))
    (ctx.outdir / "source_checks.json").write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    for archive, states in sorted(by_archive.items()):
        state = _aggregate_state(states)
        n_pass = sum(1 for s in states if s == "passed")
        failing = [f"{pid}:{c['name']}" for pid, cs in out.items() for c in cs
                   if c["state"] != "passed" and (prods[pid].get("archive") or "MAST") == archive]
        ctx.check(f"Source checks ({archive})", state,
                  f"{n_pass}/{len(states)} passed"
                  + (f"; non-passing: {', '.join(failing[:4])}" if failing else ""))
    return {"products": out, "file": ctx.rel(ctx.outdir / "source_checks.json")}


# ------------------------------------------------------------------ astrometric vetting (Gaia NSS)
def step_astrometric_vetting(ctx, params: dict) -> dict:
    """Cross-match every campaign target against Gaia DR3 NSS two-body solutions.

    This is source-scientific vetting rather than an integrity check: a significant
    NSS solution means the companion is already known to Gaia, which refutes a
    new-unseen-companion hypothesis for that target (state ``failed``). No solution
    is reported ``inconclusive`` — Gaia sensitivity is incomplete, so absence is not
    proof of a single star. Writes ``nss.json``; unavailable Gaia is ``not_tested``.
    """
    from . import nss as _nss
    from .archives import base as _base

    radius = float(params.get("radius_arcsec", 5.0))
    sig_min = float(params.get("significance_min", 5.0))
    max_sol = int(params.get("max_solutions", 10))
    out: dict[str, dict] = {}
    states: list[str] = []
    for t in ctx.targets():
        target = _base.Target.from_mapping(t)
        try:
            res = _nss.nss_vetting(_base.get("gaia"), target, radius_arcsec=radius, significance_min=sig_min,
                                   max_solutions=max_sol)
        except _base.AdapterUnavailable as exc:
            res = {"state": "not_tested", "note": f"Gaia unavailable: {exc}", "solutions": [], "nss_solutions": 0}
        except Exception as exc:  # noqa: BLE001
            res = {"state": "not_tested", "note": f"{type(exc).__name__}: {str(exc)[:200]}",
                   "solutions": [], "nss_solutions": 0}
        out[t["name"]] = res
        states.append(res["state"])
        if res.get("nss_solutions"):
            ctx.measure("nss_solutions", res["nss_solutions"], unit="count",
                        method="Gaia DR3 nss_two_body_orbit cross-match", notes=res.get("note"))
        if res.get("top_mass_function_msun") is not None:
            ctx.measure("nss_spectroscopic_mass_function", res["top_mass_function_msun"], unit="Msun",
                        method="f(M) = P K1^3 (1-e^2)^1.5 / (2 pi G) from NSS period, K1 and e")
    (ctx.outdir / "nss.json").write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    ids = []
    for name, r in out.items():
        m = r.get("target_match")
        if not m:
            ids.append(("not_tested", f"{name}: no Gaia DR3 source matched"))
            continue
        dg = m.get("min_delta_g_to_others")
        ids.append(("passed" if m.get("identification") == "unique" else "inconclusive",
                    f"{name}: Gaia DR3 {m['source_id']} at {m['sep_arcsec']:.2f}\", G {m.get('phot_g_mean_mag')}; "
                    f"{m['n_sources_in_radius']} source(s) within {radius:g}\""
                    + (f", nearest other ΔG {dg:.2f}" if dg is not None else "")))
    ctx.check("Target-to-Gaia source identification", _aggregate_state([st for st, _ in ids]),
              "; ".join(n for _, n in ids)[:900])
    state = _aggregate_state(states)
    ctx.check("Gaia NSS astrometric vetting", state,
              "; ".join(f"{name}: {r['note']}" for name, r in out.items())[:900])
    return {"targets": out, "file": ctx.rel(ctx.outdir / "nss.json")}


STEPS: dict[str, Callable[[Any, dict], dict]] = {
    "target_queue": step_target_queue,
    "fetch_products": step_fetch_products,
    "context_products": step_context_products,
    "source_checks": step_source_checks,
    "astrometric_vetting": step_astrometric_vetting,
    "calibrate_screen": step_calibrate_screen,
    "residual_screen": step_residual_screen,
    "bls_recovery": step_bls_recovery,
    "known_signal_recovery": step_known_signal_recovery,
    "period_aliases": step_period_aliases,
    "prior_art": step_prior_art,
}

from .measure_steps import MEASURE_STEPS  # noqa: E402 - the measure steps import helpers defined above

STEPS.update(MEASURE_STEPS)
