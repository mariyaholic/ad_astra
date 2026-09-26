"""Campaign steps for the measures in ``measures.py`` (docs/SUITE_EXPANSION.md §4.2).

Each step reads what earlier steps saved, queries at most the services it names, writes one JSON
file in the campaign output directory and sets its record checks. An unreachable service leaves a
check ``not_tested`` (never passed); the steps never change a record's outcome or evidence level.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from . import measures as M

CHECK_PRIORS = "Stellar priors (Gaia colour and parallax)"
CHECK_IDENT_PM = "Target-to-Gaia identification (proper motion propagated)"
CHECK_BLEND = "Blend and dilution census (Gaia DR3 cone)"
CHECK_CENSUS = "Pointing and quality census per event"
CHECK_MOVING = "Moving objects at screen-event epochs"
CHECK_VSX = "Variable-catalogue collision (VSX)"
CHECK_SIMBAD = "Object-class guard (SIMBAD)"
CHECK_REPEAT_OTHER = "Independent repetition (other MAST collections)"
CHECK_ZTF = "Independent-epoch confirmation (ZTF)"
CHECK_RV = "Stellar-companion exclusion (archival RVs)"


# ------------------------------------------------------------------ shared helpers
def _positioned_targets(ctx) -> list[dict]:
    """Spec targets that carry a position, with every catalogue field they declare."""
    return [dict(t) for t in ctx.spec.get("targets", []) if t.get("ra_deg") is not None and t.get("dec_deg") is not None]


def _query(adapter_name: str, target: dict, **opts) -> tuple[list[dict] | None, str]:
    """Rows from an inline catalogue adapter, or (None, why) when the service could not answer."""
    from .archives import base as _base

    try:
        refs = _base.get(adapter_name).discover(_base.Target.from_mapping(target), **opts)
    except _base.AdapterUnavailable as exc:
        return None, f"{adapter_name} unavailable: {str(exc)[:200]}"
    except Exception as exc:  # noqa: BLE001 - a failed query is recorded, never read as 'no rows'
        return None, f"{adapter_name} query failed: {type(exc).__name__}: {str(exc)[:200]}"
    rows = []
    for r in refs:
        rows += list((r.extra or {}).get("rows") or [])
    return rows, f"{len(rows)} row(s)"


def _rows_digest(rows: list[dict]) -> str:
    return hashlib.sha256(json.dumps(rows, sort_keys=True, default=str).encode()).hexdigest()


def _depth_ppm(ctx, target: dict) -> tuple[float | None, str]:
    """The event depth to test against: the measured catalogued transit if recovered, else the catalogue's."""
    known = ctx.optional_result("known_signal_recovery", {}).get("per_product", {})
    for v in known.values():
        if v.get("target") in (None, target["name"]):
            for ep in v.get("epochs", []):
                if ep.get("state") == "recovered" and ep.get("measured_depth_ppm"):
                    return float(ep["measured_depth_ppm"]), "measured depth of the recovered catalogued transit"
    d = M._f(target.get("depth_ppm"))
    return d, ("catalogue depth" if d else "no depth available")


def _persistent_events(ctx) -> list[dict]:
    out = []
    for pid, v in ctx.optional_result("residual_screen", {}).get("per_product", {}).items():
        for ev in v.get("distinct_events_outside_veto", []):
            if ev.get("persistent"):
                out.append({"product": pid, **ev})
    return out


def _write(ctx, name: str, payload: Any) -> str:
    path = ctx.outdir / name
    path.write_text(json.dumps(payload, indent=2, default=str, allow_nan=False), encoding="utf-8")
    return ctx.rel(path)


def _clean_json(x):
    if isinstance(x, float) and not math.isfinite(x):
        return None
    if isinstance(x, dict):
        return {k: _clean_json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean_json(v) for v in x]
    return x


# ------------------------------------------------------------------ 1, 4, 11: Gaia cone → priors, identification, blends
def step_stellar_context(ctx, params: dict) -> dict:
    """One Gaia DR3 cone per target: proper-motion-propagated identification, dwarf priors from colour
    and parallax, and the neighbour flux inside a TESS-scale aperture. Writes ``stellar_context.json``.

    The result feeds ``period_aliases`` (duration likelihood per alias) when this step runs first.
    """
    radius = float(params.get("radius_arcsec", 3 * M.TESS_PIX_ARCSEC))
    aperture = float(params.get("aperture_arcsec", 2.5 * M.TESS_PIX_ARCSEC))
    match_max = float(params.get("match_arcsec", 2.0))
    prior_opts = {k: params[k] for k in ("min_parallax_over_error", "ruwe_max", "radius_frac_floor", "mass_frac_floor",
                                         "max_offset_from_sequence_mag") if k in params}
    out, st = {}, {"priors": [], "ident": [], "blend": []}
    for t in _positioned_targets(ctx):
        name = t["name"]
        rows, why = _query("gaia", t, radius_arcsec=radius, limit=int(params.get("limit", 500)))
        if rows is None:
            out[name] = {"error": why}
            for k in st:
                st[k].append(("not_tested", f"{name}: {why}"))
            continue
        ctx.measure("gaia_cone_rows", len(rows), unit="count", method=f"Gaia DR3 gaia_source cone r={radius:g}\"",
                    notes=f"rows sha256 {_rows_digest(rows)}")
        pos_epoch = M.julian_year(t.get("epoch"))
        match = M.identify(rows, float(t["ra_deg"]), float(t["dec_deg"]), position_epoch=pos_epoch)
        entry: dict[str, Any] = {"cone_radius_arcsec": radius, "n_rows": len(rows), "rows_sha256": _rows_digest(rows),
                                 "position_epoch": t.get("epoch"), "match": None}
        if match is None or match["sep_arcsec"] > match_max:
            entry["match"] = None if match is None else {k: v for k, v in match.items() if k != "row"}
            note = (f"{name}: no Gaia DR3 source within {match_max:g}\" after propagation to {t.get('epoch')}"
                    + (f" (nearest {match['sep_arcsec']:.2f}\")" if match else ""))
            st["ident"].append(("inconclusive" if match else "not_tested", note))
            st["priors"].append(("not_tested", f"{name}: no identified Gaia source"))
            st["blend"].append(("not_tested", f"{name}: no identified Gaia source"))
            out[name] = entry
            continue
        row = match.pop("row")
        entry["match"] = match
        nxt = match.get("next") or {}
        ambiguous = bool(nxt and nxt.get("sep_arcsec") is not None and nxt["sep_arcsec"] <= match_max
                         and (nxt.get("delta_g") is None or nxt["delta_g"] < 2.5))
        epoch_txt = (f"propagated 2016.0 → {t.get('epoch')}" if pos_epoch is not None
                     else f"target epoch {t.get('epoch')!r} not a Julian epoch; compared at 2016.0")
        st["ident"].append(("inconclusive" if ambiguous or pos_epoch is None else "passed",
                            f"{name}: Gaia DR3 {match['source_id']} at {match['sep_arcsec']:.2f}\" ({epoch_txt}; "
                            f"{match['sep_unpropagated_arcsec']:.2f}\" unpropagated"
                            + (f", proper-motion shift {match['pm_shift_arcsec']:.2f}\"" if match.get("pm_shift_arcsec") is not None else "")
                            + (", high proper motion" if match["high_proper_motion"] else "")
                            + (f"; another source {nxt['sep_arcsec']:.2f}\" away, ΔG {nxt['delta_g']}" if ambiguous else "") + ")"))
        pri = M.stellar_priors(row, **prior_opts)
        entry["priors"] = pri
        if pri["usable"]:
            st["priors"].append(("passed", f"{name}: Teff {pri['teff_k']:.0f} K, R* {pri['radius_rsun']:.2f} ± "
                                           f"{pri['radius_err_rsun']:.2f}, M* {pri['mass_msun']:.2f} ± {pri['mass_err_msun']:.2f}, "
                                           f"ρ* {pri['density_rho_sun']:.2f} ± {pri['density_err_rho_sun']:.2f} ρ☉ "
                                           f"(dwarf sequence, M_G {pri['abs_g']:.2f}, no extinction)"))
            for q, unit in (("teff_k", "K"), ("radius_rsun", "Rsun"), ("mass_msun", "Msun"), ("density_rho_sun", "rho_sun")):
                ctx.measure(f"stellar_{q}", pri[q], unit=unit, method="Gaia DR3 colour/parallax on the mean dwarf sequence",
                            notes=M.DWARF_TABLE_REF)
        else:
            st["priors"].append(("inconclusive", f"{name}: dwarf priors not applied — {pri.get('reason')}"))
        depth, depth_src = _depth_ppm(ctx, t)
        cen = M.dilution_census(rows, match["source_id"], match.get("phot_g_mean_mag"), ra=float(row["ra"]),
                                dec=float(row["dec"]), aperture_arcsec=aperture, depth_ppm=depth)
        cen["depth_source"] = depth_src
        entry["dilution"] = cen
        if not cen["computed"]:
            st["blend"].append(("not_tested", f"{name}: {cen['reason']}"))
        else:
            ctx.measure("gaia_contamination_fraction", cen["contamination_fraction"], unit="fraction",
                        method=f"Gaia G flux of neighbours within {aperture:g}\" / total")
            mim = [n for n in cen["neighbours"] if n["could_mimic_depth"]]
            txt = (f"{name}: {cen['n_neighbours']} Gaia neighbour(s) within {aperture:g}\", contamination "
                   f"{cen['contamination_fraction']:.2%}; depth {'n/a' if depth is None else f'{depth:.0f} ppm'} ({depth_src})")
            if depth is None:
                st["blend"].append(("inconclusive", txt + "; no depth to compare"))
            elif mim:
                st["blend"].append(("inconclusive", txt + f"; {len(mim)} could produce it if fully eclipsed (brightest "
                                    f"{mim[0]['source_id']}, {mim[0]['sep_arcsec']:.1f}\", ΔG "
                                    f"{mim[0]['phot_g_mean_mag'] - match['phot_g_mean_mag']:.2f}); a centroid test is needed"))
            else:
                st["blend"].append(("passed", txt + "; none bright enough to produce it alone"
                                    + (f"; {len(cen['neighbours_without_g'])} neighbour(s) without G not assessed"
                                       if cen["neighbours_without_g"] else "")))
        out[name] = entry
    from .steps import _aggregate_state

    for check, key in ((CHECK_IDENT_PM, "ident"), (CHECK_PRIORS, "priors"), (CHECK_BLEND, "blend")):
        if st[key]:
            ctx.check(check, _aggregate_state([s for s, _ in st[key]]), "; ".join(n for _, n in st[key])[:900])
    return {"targets": _clean_json(out), "file": _write(ctx, "stellar_context.json", _clean_json(out))}


def duration_likelihood_for(ctx, target: dict, periods: list[float], params: dict) -> dict | None:
    """Per-alias duration likelihood when ``stellar_context`` produced usable priors, else None."""
    sc = ctx.optional_result("stellar_context", {}).get("targets", {}).get(target.get("name"), {})
    pri = sc.get("priors") or {}
    dur = M._f(target.get("duration_h"))
    if not pri.get("usable") or not dur or not periods:
        return None
    derr = M._f(target.get("duration_err_h")) or float(params.get("duration_frac_err", 0.1)) * dur
    depth = M._f(target.get("depth_ppm"))
    k = math.sqrt(depth * 1e-6) if depth and depth > 0 else float(params.get("radius_ratio", 0.1))
    rows = M.alias_duration_likelihood(periods, dur, derr, pri["density_rho_sun"], pri["density_err_rho_sun"], k=k,
                                       seed=int(ctx.seed or 0))
    return {"duration_h": dur, "duration_err_h": derr,
            "duration_err_source": "catalogue" if target.get("duration_err_h") else
            f"declared {params.get('duration_frac_err', 0.1):g} × duration (no catalogue error)",
            "radius_ratio": k, "density_rho_sun": pri["density_rho_sun"], "density_err_rho_sun": pri["density_err_rho_sun"],
            "assumptions": ["circular orbit", "uniform impact parameter 0 ≤ b < 1", "radius ratio √depth (undiluted)",
                            "both transits share the catalogued duration", "no occurrence-rate prior"],
            "aliases": rows}


# ------------------------------------------------------------------ 8: pointing and quality census per event
def _engineering(path: Path, prod: dict):
    """(BJD, QUALITY, {series}) from a FITS light curve's engineering columns; (None, why) otherwise."""
    fmt = prod.get("format") or "spoc_lc"
    if fmt not in ("spoc_lc", "tess_lc", "kepler_lc", "fits_table"):
        return None, f"format {fmt}: no engineering columns"
    from astropy.io import fits

    with fits.open(path, memmap=False) as h:
        d, hd = h[1].data, h[1].header
        names = set(d.names)
        if "TIME" not in names:
            return None, "no TIME column"
        t = np.asarray(d["TIME"], float) + float(hd.get("BJDREFI", 0)) + float(hd.get("BJDREFF", 0))
        q = np.asarray(d["QUALITY"], int) if "QUALITY" in names else np.zeros(t.size, int)
        series = {n: np.asarray(d[n], float) for n in ("MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2", "SAP_BKG")
                  if n in names}
    return (t, q, series), None


def step_event_census(ctx, params: dict) -> dict:
    """For every persistent screen event: quality bits within ±pad, and in-event shifts of centroid,
    pointing and background. Writes ``event_census.json``."""
    from .steps import _lightcurve_products, resolve

    events = _persistent_events(ctx)
    pad, base, zmax = float(params.get("pad_days", 0.25)), float(params.get("baseline_days", 1.0)), float(params.get("z_max", 5.0))
    prods = _lightcurve_products(ctx) if ctx.optional_result("fetch_products", None) else {}
    out, states = [], []
    cache: dict[str, Any] = {}
    for ev in events:
        prod = prods.get(ev["product"])
        if prod is None:
            continue
        if ev["product"] not in cache:
            cache[ev["product"]] = _engineering(resolve(prod["path"]), prod)
        data, why = cache[ev["product"]]
        dur = max(float(ev.get("span_days") or 0), float(params.get("min_window_hours", 1.0)) / 24)
        if data is None:
            out.append({"product": ev["product"], "t_mid": ev["mid_time_BJD_like"], "tested": False, "reason": why})
            states.append("inconclusive")
            continue
        t, q, series = data
        res = M.event_census(t, q, series, t_mid=float(ev["mid_time_BJD_like"]), dur_d=dur, pad_d=pad, baseline_d=base, z_max=zmax)
        res["product"] = ev["product"]
        out.append(res)
        missing = {"MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2", "SAP_BKG"} - set(res["tested_series"])
        states.append("failed" if res["suspect"] else "inconclusive" if (missing or not res["clean"]) else "passed")
    if not events:
        ctx.check(CHECK_CENSUS, "not_tested", "no persistent screen event outside the veto")
    else:
        from .steps import _aggregate_state

        flagged = [e for e in out if e.get("tested", True) and not e.get("clean", False)]
        parts = [f"{len(events)} persistent event(s), {sum(s == 'passed' for s in states)} clean"]
        for e in flagged[:4]:
            parts.append(f"BJD {e['t_mid']:.4f} {'suspect' if e['suspect'] else 'caution'}: "
                         + ", ".join([f"{b} (in event)" for b in e["artifact_bits_in_event"]]
                                     + [f"{b} (within ±{pad:g} d)" for b in e["artifact_bits_near"] if b not in e["artifact_bits_in_event"]]
                                     + [f"{s} z={e['series'][s]['z']:+.1f}" for s in e["flagged_series"]]))
        if not flagged:
            parts.append(f"no artifact quality bit within ±{pad:g} d and no centroid, pointing or background shift beyond {zmax:g}σ")
        ctx.check(CHECK_CENSUS, _aggregate_state(states), "; ".join(parts)[:900])
    return {"events": _clean_json(out), "file": _write(ctx, "event_census.json", _clean_json(out))}


# ------------------------------------------------------------------ 3: moving objects at event epochs
def step_moving_objects(ctx, params: dict) -> dict:
    """SkyBoT cone at each persistent event's epoch (and each repeat candidate). Writes ``moving_objects.json``.

    Positions are computed for TESS (observatory code ``C57``; ``location`` overrides): seen from the
    geocentre a main-belt object can sit arcminutes from where TESS sees it. An object counts when it
    is bright enough and within ``near_arcsec`` (default 63″, three TESS pixels) plus its own motion
    over ``window_h`` hours (default 1) of the target. One that counts supports an asteroid
    explanation of that event; none supports (never proves) a non-asteroid one.
    """
    radius = float(params.get("radius_arcsec", 600.0))
    frac = float(params.get("min_flux_fraction_of_depth", 0.1))
    location = str(params.get("location", "C57"))
    near = float(params.get("near_arcsec", 3 * M.TESS_PIX_ARCSEC))
    window_h = float(params.get("window_h", 1.0))
    events = _persistent_events(ctx)
    for c in ctx.optional_result("period_aliases", {}).get("candidates", []):
        if not any(abs(e["mid_time_BJD_like"] - c["event_bjd"]) < 0.05 for e in events):
            events.append({"product": c["product"], "mid_time_BJD_like": c["event_bjd"], "persistent": True,
                           "deepest_median_residual": -c["depth_ppm"] * 1e-6})
    targets = _positioned_targets(ctx)
    if not events or not targets:
        ctx.check(CHECK_MOVING, "not_tested", "no persistent screen event outside the veto" if targets else "no target position")
        return {"events": [], "file": _write(ctx, "moving_objects.json", [])}
    t = targets[0]
    tmag = M._f(t.get("tmag"))
    out, states = [], []
    for ev in events:
        try:
            iso = M.bjd_tdb_to_utc_iso(float(ev["mid_time_BJD_like"]), float(t["ra_deg"]), float(t["dec_deg"]))
        except Exception as exc:  # noqa: BLE001
            out.append({"bjd": ev["mid_time_BJD_like"], "error": f"time conversion failed: {exc}"})
            states.append("not_tested")
            continue
        rows, why = _query("skybot", t, epoch_iso=iso, radius_arcsec=radius, location=location)
        depth = abs(float(ev.get("deepest_median_residual") or 0)) * 1e6 or None
        if rows is None:
            out.append({"bjd": ev["mid_time_BJD_like"], "utc": iso, "error": why})
            states.append("not_tested")
            continue
        hits = M.moving_object_hits(rows, target_mag=tmag, depth_ppm=depth, min_flux_fraction_of_depth=frac,
                                    near_arcsec=near, window_h=window_h)
        out.append({"bjd": ev["mid_time_BJD_like"], "utc": iso, "location": location, "radius_arcsec": radius,
                    "event_depth_ppm": depth, **hits})
        states.append("failed" if hits["bright_enough"] else
                      "inconclusive" if hits["unknown_brightness"] or hits["unknown_distance"] else "passed")
    n_hit = sum(bool(e.get("bright_enough")) for e in out)
    note = (f"{len(events)} event epoch(s) queried in SkyBoT (observer {location}, r={radius:g}\"); "
            + (f"{n_hit} with a known object bright enough (≥{frac:g}× the depth in flux) within {near:g}\" "
               f"plus its motion over {window_h:g} h" if n_hit else
               f"no known object bright enough within {near:g}\" plus its motion at any queried epoch "
               "(supports, does not prove, a non-asteroid origin)")
            + (f"; {states.count('not_tested')} epoch(s) not answered" if "not_tested" in states else ""))
    # some epochs answered and some not: the check covered part of the events, so it is inconclusive
    state = ("failed" if "failed" in states else "not_tested" if set(states) == {"not_tested"} else
             "inconclusive" if {"not_tested", "inconclusive"} & set(states) else "passed")
    ctx.check(CHECK_MOVING, state, note)
    return {"events": _clean_json(out), "file": _write(ctx, "moving_objects.json", _clean_json(out))}


# ------------------------------------------------------------------ 9: variable-catalogue and object-class guards
def _alias_periods(ctx) -> list[float]:
    ps = []
    for c in ctx.optional_result("period_aliases", {}).get("candidates", []):
        ps += list(c.get("allowed_periods_days") or [])
    veto = ctx.spec.get("veto") or {}
    if veto.get("kind") == "ephemeris":
        ps.append(float(veto["period_days"]))
    return ps


def step_variability_guard(ctx, params: dict) -> dict:
    """VSX types and periods and the SIMBAD object class at each target. Writes ``variability_guard.json``.

    An eclipsing or ellipsoidal variable catalogued at the target fails the VSX check (its dips may
    be eclipses); a catalogued period matching an allowed alias (×½, ×1, ×2) is inconclusive. SIMBAD's
    class of the nearest object fails for eclipsing binaries and galaxies and is inconclusive for
    evolved, multiple, young or accreting stars.
    """
    match = float(params.get("match_arcsec", 10.0))
    radius = float(params.get("radius_arcsec", 30.0))
    periods = _alias_periods(ctx)
    out, vs, sb = {}, [], []
    for t in _positioned_targets(ctx):
        name, ra, dec = t["name"], float(t["ra_deg"]), float(t["dec_deg"])
        entry = {}
        rows, why = _query("vizier", t, radius_arcsec=radius, table="B/vsx/vsx")
        if rows is None:
            entry["vsx"] = {"error": why}
            vs.append(("not_tested", f"{name}: {why}"))
        else:
            g = M.vsx_guard(rows, ra, dec, match_arcsec=match, periods=periods, tol=float(params.get("period_tolerance", 0.01)))
            entry["vsx"] = {**g, "n_rows": len(rows), "rows_sha256": _rows_digest(rows)}
            desc = "; ".join(f"{e['name']} {e['type']} P={e['period_days']} at {e['sep_arcsec']:.1f}\""
                             + (f" (collides with alias {e['period_collisions'][0]['period_days']:g} d)" if e["period_collisions"] else "")
                             for e in g["entries"][:3])
            vs.append((g["state"], f"{name}: " + (desc if g["entries"] else f"no VSX entry within {match:g}\"")))
        rows, why = _query("simbad", t, radius_arcsec=radius)
        if rows is None:
            entry["simbad"] = {"error": why}
            sb.append(("not_tested", f"{name}: {why}"))
        else:
            g = M.simbad_guard(rows, ra, dec, match_arcsec=match)
            entry["simbad"] = {**g, "n_rows": len(rows), "rows_sha256": _rows_digest(rows)}
            e0 = g["entries"][0] if g["entries"] else None
            sb.append((g["state"], f"{name}: " + (f"{e0['main_id']} otype {e0['otype']} ({e0['class']}) at {e0['sep_arcsec']:.1f}\""
                                                  if e0 else g.get("reason", ""))))
        out[name] = entry
    from .steps import _aggregate_state

    if vs:
        ctx.check(CHECK_VSX, _aggregate_state([s for s, _ in vs]), "; ".join(n for _, n in vs)[:900])
    if sb:
        ctx.check(CHECK_SIMBAD, _aggregate_state([s for s, _ in sb]), "; ".join(n for _, n in sb)[:900])
    return {"targets": _clean_json(out), "file": _write(ctx, "variability_guard.json", _clean_json(out))}


# ------------------------------------------------------------------ 5, 6: independent instruments at alias epochs
# Where fetch_independent looks by default. Kepler/K2 files a star under its KIC/EPIC name, so MAST is searched
# by position; LLC is the 30-min long-cadence light curve (Kepler-10: 15 quarters, 5.9 MB, found in 17 s on
# 2026-09-26). ZTF (IRSA) has no light curve for stars bright enough to saturate — Kepler-10 (G ≈ 10.6) returned
# an empty 0-row table at 2″ and at 5″ — which is about half of the TESS TOI hosts: an empty answer is recorded
# as such, never as a pass. A fainter host (T = 14.1) returned 1,721 catflags-0 points of one star at 3″, whose
# five oids (fields/CCDs/filters) all sit ≤ 0.06″ from the position; 3″ covers ZTF's ~0.7″ astrometric scatter
# and the match cut below drops a neighbour's oid.
INDEPENDENT_SOURCES = (
    {"label": "Kepler/K2", "archive": "mast",
     "options": {"collection": "Kepler,K2", "provenance": "", "subgroup": "LLC", "radius_arcsec": 4.0, "limit": 40}},
    {"label": "ZTF", "archive": "irsa", "options": {"mode": "ztf", "radius_arcsec": 3.0}},
)
PALOMAR = (-116.8650, 33.3563, 1712.0)      # ZTF camera on the Samuel Oschin 48-inch: lon, lat (deg), height (m)
ZTF_EXPOSURE_S = 30.0                       # survey exposure; ZTF ``mjd`` is the exposure start (UTC)


def step_fetch_independent(ctx, params: dict) -> dict:
    """Light curves from instruments other than TESS SPOC, for ``alias_cross_instrument``.

    Each source in ``params['sources']`` (default ``INDEPENDENT_SOURCES``) is queried at every positioned
    target and whatever it returns is downloaded, checksummed and ledgered like any other product. Nothing
    fetched here enters the residual screen. Every query's outcome is kept (``answered`` with a product
    count, ``unavailable`` or ``failed`` with the reason), so a service that could not answer is never read
    as "no data". Writes ``independent_lightcurves.json``.
    """
    from .archives import base as _base
    from .steps import NOT_FETCHED_NOTE, _fetch_product

    sources = params.get("sources") or [dict(s) for s in INDEPENDENT_SOURCES]
    products, queries = {}, []
    for t in _positioned_targets(ctx):
        target = _base.Target.from_mapping(t)
        for src in sources:
            label = src.get("label") or src["archive"]
            opts = dict(src.get("options") or {})
            q = {"target": t["name"], "source": label, "archive": src["archive"], "options": opts}
            try:
                refs = _base.get(src["archive"]).discover(target, **opts)
            except _base.AdapterUnavailable as exc:
                queries.append({**q, "state": "unavailable", "detail": str(exc)[:240]})
                continue
            except Exception as exc:  # noqa: BLE001 - a failed query is recorded, never read as 'no data'
                queries.append({**q, "state": "failed", "detail": f"{type(exc).__name__}: {str(exc)[:240]}"})
                continue
            got, errors, skipped = [], [], []
            for ref in refs:
                d = ref.as_dict()
                for k, v in d.pop("extra", {}).items():
                    d.setdefault(k, v)
                d.update(target=t["name"], tic=t.get("tic"), archive=ref.archive)
                n_notes = len(ctx.notes)
                try:
                    r = _fetch_product(ctx, d, [ctx.scratch])
                except Exception as exc:  # noqa: BLE001 - one bad download is recorded, the rest still count
                    errors.append(f"{ref.product_id}: {type(exc).__name__}: {str(exc)[:160]}")
                    continue
                if r:
                    products[r[0]] = {**r[1], "independent_source": label}
                    got.append(r[0])
                else:
                    # _fetch_product skipped it with a note: the size gate (deliberate) or an adapter that
                    # could not deliver it (an outage). Kept here so a query that delivered none of what it
                    # found is never read as a successful empty answer.
                    prefix = f"{d.get('target') or ref.product_id}/{ref.archive}: "
                    note = next((n for n in ctx.notes[n_notes:] if n.startswith(prefix)), "")
                    skipped.append({"product": ref.product_id, **({"detail": note[:240]} if note else {})})
            undelivered = [s for s in skipped if NOT_FETCHED_NOTE in s.get("detail", "")]
            queries.append({**q, "state": "answered" if got or not (errors or undelivered) else "failed",
                            "n_found": len(refs), "products": got,
                            **({"fetch_errors": errors} if errors else {}),
                            **({"not_fetched": skipped} if skipped else {})})
    payload = _clean_json({"queries": queries, "products": products})
    return {**payload, "file": _write(ctx, "independent_lightcurves.json", payload)}


def ztf_series(path: Path, ra_deg: float, dec_deg: float, *, min_points: int = 20,
               max_offset_arcsec: float | None = 2.0) -> list[dict]:
    """One relative-flux series per ZTF object id (a single field, CCD quadrant and filter).

    Only ``catflags == 0`` points are kept. Magnitudes become flux relative to the series median, and
    the time becomes BJD_TDB at mid-exposure: ZTF's ``mjd`` is the UTC exposure start, shifted by half a
    ``ZTF_EXPOSURE_S`` exposure, then light-travel-corrected from Palomar to the target (against a real
    2026-09-26 ZTF fetch this tracks the VOTable's supplied ``hjd`` midpoint to a constant ~72 s, the
    TDB−UTC offset, with ~6 s spread). Series with fewer than ``min_points`` good points are dropped.
    Mixing ids would mix filters, fields and zero points.

    A ``radius_arcsec`` cone matches every ZTF oid inside it, so a neighbour's light curve can ride in
    with the target's: the per-point ``ra``/``dec`` decide, and a series whose median position is more
    than ``max_offset_arcsec`` from the target is dropped with its offset (``None`` when the table
    carries no positions, which is never read as a match).
    """
    import astropy.units as u
    from astropy.coordinates import EarthLocation, SkyCoord
    from astropy.io.votable import parse as votable_parse
    from astropy.time import Time

    tab = votable_parse(str(path)).get_first_table().to_table()
    if not len(tab):
        return []
    mag = np.asarray(tab["mag"], float)
    ok = (np.asarray(tab["catflags"]) == 0) & np.isfinite(mag) & np.isfinite(np.asarray(tab["mjd"], float))
    oids = np.asarray(tab["oid"]).astype(str)
    filters = np.asarray(tab["filtercode"]).astype(str) if "filtercode" in tab.colnames else np.full(len(tab), "?")
    loc = EarthLocation.from_geodetic(PALOMAR[0] * u.deg, PALOMAR[1] * u.deg, PALOMAR[2] * u.m)
    coord = SkyCoord(ra_deg * u.deg, dec_deg * u.deg, frame="icrs")
    has_pos = {"ra", "dec"} <= set(tab.colnames)
    out = []
    for oid in sorted(set(oids[ok])):
        sel = ok & (oids == oid)
        if sel.sum() < min_points:
            continue
        off = None
        if has_pos:
            obj = SkyCoord(np.median(np.asarray(tab["ra"], float)[sel]) * u.deg,
                           np.median(np.asarray(tab["dec"], float)[sel]) * u.deg)
            off = float(coord.separation(obj).arcsec)
            if max_offset_arcsec is not None and off > float(max_offset_arcsec):
                continue
        tm = Time(np.asarray(tab["mjd"], float)[sel] + ZTF_EXPOSURE_S / 2 / 86400, format="mjd", scale="utc", location=loc)
        bjd = (tm.tdb + tm.light_travel_time(coord)).jd
        m = mag[sel]
        out.append({"oid": oid, "filter": str(filters[sel][0]), "n": int(sel.sum()), "t_bjd": bjd,
                    "flux": 10 ** (-0.4 * (m - np.median(m))),
                    **({"offset_arcsec": off} if off is not None else {})})
    return out


def _instrument_of(prod: dict) -> str:
    arch, fmt, pid = (prod.get("archive") or "MAST").upper(), prod.get("format") or "spoc_lc", str(prod.get("product_id", ""))
    if arch == "IRSA" or fmt == "ztf_lc":
        return "ZTF"
    if arch == "MAST" and fmt in ("spoc_lc", "tess_lc") and not pid.startswith(("hlsp_", "kplr", "ktwo")):
        return "TESS-SPOC"
    return f"{arch}:{fmt}"


def step_alias_cross_instrument(ctx, params: dict) -> dict:
    """Test each allowed period alias in light curves from other instruments (Kepler/K2/HLSP via MAST,
    ZTF via IRSA), including sparse ones the residual screen does not use. Writes
    ``alias_cross_instrument.json``. TESS SPOC light curves are already used by ``period_aliases``."""
    from .steps import _read_lc, resolve

    cands = ctx.optional_result("period_aliases", {}).get("candidates", [])
    prods = dict((ctx.optional_result("fetch_products", {}) or {}).get("products", {}))
    indep = ctx.optional_result("fetch_independent", None)
    prods.update((indep or {}).get("products", {}))
    other = {pid: p for pid, p in prods.items() if p.get("kind") == "lightcurve" and _instrument_of({**p, "product_id": pid}) != "TESS-SPOC"}
    tgt = (_positioned_targets(ctx) or [{}])[0]
    dur_d = float(M._f(tgt.get("duration_h")) or 2.0) / 24
    ref_t0 = (json.loads((ctx.outdir / "period_aliases.json").read_text(encoding="utf-8")).get("reference_epoch_bjd")
              if (ctx.outdir / "period_aliases.json").is_file() else None)
    results = []

    def _test(pid, inst, tb, y, time_note, series=None, observed_offset_arcsec=None):
        for c in cands:
            periods = list(c.get("allowed_periods_days") or [])
            if not periods or ref_t0 is None:
                continue
            rows = M.alias_depths_in_series(tb, y, t0=float(ref_t0), periods=periods, dur_d=dur_d,
                                            ref_depth_ppm=float(c["reference_depth_ppm"]),
                                            min_points=int(params.get("min_points", 3)),
                                            excluded_below=float(params.get("excluded_below", 0.3)),
                                            skip=[float(ref_t0), float(c["event_bjd"])])
            results.append({"product": pid, "instrument": inst, "event_bjd": c["event_bjd"], "time_note": time_note,
                            **({"series": series} if series else {}),
                            **({"observed_offset_arcsec": observed_offset_arcsec} if observed_offset_arcsec is not None else {}),
                            "aliases": rows})

    for pid, p in other.items():
        inst = _instrument_of({**p, "product_id": pid})
        try:
            if p.get("format") == "ztf_lc":
                if tgt.get("ra_deg") is None:
                    results.append({"product": pid, "instrument": inst,
                                    "error": "no target position: a ZTF series cannot be tied to the target"})
                    continue
                # one series per ZTF object id: pooling ids would mix filters and zero points
                for s in ztf_series(resolve(p["path"]), float(tgt["ra_deg"]), float(tgt["dec_deg"]),
                                    min_points=int(params.get("ztf_min_points", 20)),
                                    max_offset_arcsec=params.get("max_offset_arcsec", 2.0)):
                    _test(pid, inst, s["t_bjd"], s["flux"],
                          "BJD_TDB at mid-exposure (from ZTF UTC exposure-start mjd)",
                          series={"oid": s["oid"], "filter": s["filter"], "n": s["n"],
                                  **({"offset_arcsec": s["offset_arcsec"]} if "offset_arcsec" in s else {})})
                continue
            lc = _read_lc(resolve(p["path"]), p)
        except Exception as exc:  # noqa: BLE001
            results.append({"product": pid, "instrument": inst, "error": f"{type(exc).__name__}: {str(exc)[:160]}"})
            continue
        good = lc.usable if hasattr(lc, "usable") else np.isfinite(lc.pdc)
        # Kepler/K2 products are discovered by position, so a close neighbour's light curve can be
        # returned: the header's observed position decides whose series this is, and a foreign one
        # never contributes a verdict (a flat neighbour would otherwise "exclude" the alias).
        off = None
        ra_o, dec_o = lc.primary.get("RA_OBJ"), lc.primary.get("DEC_OBJ")
        if ra_o is not None and dec_o is not None and tgt.get("ra_deg") is not None:
            off = M.sep_arcsec(float(ra_o), float(dec_o), float(tgt["ra_deg"]), float(tgt["dec_deg"]))
            if off > float(params.get("max_offset_arcsec", 2.0)):
                results.append({"product": pid, "instrument": inst, "observed_offset_arcsec": off,
                                "error": f"header position {off:.2f}\" from the target (> "
                                         f"{float(params.get('max_offset_arcsec', 2.0)):g}\"); not used"})
                continue
        _test(pid, inst, lc.time_bjd[good], lc.pdc[good], (lc.primary.get("_channels") or {}).get("time_scale"),
              **({"observed_offset_arcsec": off} if off is not None else {}))

    def _looked(labels):
        """What the fetch_independent queries for these sources answered, for a not_tested note."""
        if indep is None:
            return None
        qs = [q for q in indep.get("queries", []) if q["source"] in labels]
        if not qs:
            names = sorted({q["source"] for q in indep.get("queries", [])})
            return (f"fetch_independent ran with sources {', '.join(names)}" if names else
                    "fetch_independent answered with no positioned target")
        return "; ".join(f"{q['source']} {q['state']}" + (f", {len(q.get('products', []))} light curve(s) within "
                                                          f"{q['options'].get('radius_arcsec', '?')}\""
                                                          if q["state"] == "answered" else f": {q.get('detail', '')[:120]}")
                         for q in qs)

    for check, pick, labels in ((CHECK_REPEAT_OTHER, lambda r: r["instrument"] not in ("ZTF",), ("Kepler/K2",)),
                                (CHECK_ZTF, lambda r: r["instrument"] == "ZTF", ("ZTF",))):
        mine = [r for r in results if pick(r) and "aliases" in r]
        if not cands:
            ctx.check(check, "not_tested", "no repeat candidate with allowed period aliases")
            continue
        if not mine:
            looked = _looked(labels)
            broken = [r for r in results if r.get("error") and pick(r)]
            extra = (f"; {len(broken)} fetched series unusable: {broken[0]['error'][:140]}" if broken else "")
            ctx.check(check, "not_tested", f"no usable light curve from this instrument ({looked}){extra}" if looked else
                      "no light curve from this instrument was fetched (no fetch_independent step in this spec)")
            continue
        verdicts = [a["verdict"] for r in mine for a in r.get("aliases", [])]
        sup = sorted({a["period_days"] for r in mine for a in r.get("aliases", []) if a["verdict"] == "supported"})
        exc_ = sorted({a["period_days"] for r in mine for a in r.get("aliases", []) if a["verdict"] == "excluded"})
        tested = [v for v in verdicts if v != "untested"]
        n_all = len({a["period_days"] for r in mine for a in r.get("aliases", [])})
        if not tested:
            state = "inconclusive"
        elif sup:
            state = "passed"
        elif len(exc_) == n_all:
            state = "failed"
        else:
            state = "inconclusive"
        ctx.check(check, state, f"{len(mine)} light curve × candidate pair(s); aliases supported: "
                  f"{', '.join(f'{p:g}' for p in sup[:8]) or 'none'}; excluded: {', '.join(f'{p:g}' for p in exc_[:8]) or 'none'}; "
                  f"{verdicts.count('untested')} alias test(s) without in-transit data")
    return {"results": _clean_json(results), "file": _write(ctx, "alias_cross_instrument.json", _clean_json(results))}


# ------------------------------------------------------------------ 12: RV bounds from archival spectra
def step_rv_bounds(ctx, params: dict) -> dict:
    """Upper bounds on a companion's mass per allowed alias from archival radial velocities.

    Reads every fetched product in an RV-bearing format (``rv_table`` or ESO pipeline spectra with RV
    keywords, via ``readers.read_rv``). Writes ``rv_bounds.json``. ``passed`` means every tested alias
    excludes a stellar-mass companion (M2 < ``stellar_limit_msun``); it bounds the eclipsing-binary
    alternative, it does not detect a planet.
    """
    from .readers import ReaderError, read_rv
    from .steps import resolve

    prods = (ctx.optional_result("fetch_products", {}) or {}).get("products", {})
    t_all, rv_all, e_all, used, skipped = [], [], [], [], []
    for pid, p in prods.items():
        if p.get("format") not in ("rv_table", "eso_spectrum"):
            continue
        try:
            rv = read_rv(resolve(p["path"]), fmt=p.get("format"))
        except ReaderError as exc:
            skipped.append({"product": pid, "reason": str(exc)[:200]})
            continue
        t_all += list(rv["bjd"]); rv_all += list(rv["rv_ms"]); e_all += list(rv["err_ms"])
        used.append({"product": pid, "n": len(rv["bjd"]), "source": rv["source"]})
    min_n = int(params.get("min_points", 6))
    periods = sorted(set(_alias_periods(ctx)))
    tgt = (_positioned_targets(ctx) or [{}])[0]
    sc = ctx.optional_result("stellar_context", {}).get("targets", {}).get(tgt.get("name"), {})
    m1 = (sc.get("priors") or {}).get("mass_msun") if (sc.get("priors") or {}).get("usable") else M._f(params.get("primary_mass_msun"))
    res = {"used": used, "skipped": skipped, "n_rv": len(t_all), "periods": periods, "primary_mass_msun": m1}
    if len(t_all) < min_n or not periods or not m1:
        why = (f"{len(t_all)} RV point(s) < {min_n}" if len(t_all) < min_n else "no allowed alias or catalogued period"
               if not periods else "no primary mass (no usable stellar priors and none declared)")
        ctx.check(CHECK_RV, "not_tested", why)
        return {**res, "file": _write(ctx, "rv_bounds.json", res)}
    bounds = M.rv_companion_bounds(np.array(t_all), np.array(rv_all), np.array(e_all), periods, m1_msun=float(m1),
                                   jitter_ms=float(params.get("jitter_ms", 0.0)), z=float(params.get("z", 3.0)))
    res["bounds"] = bounds
    lim = float(params.get("stellar_limit_msun", 0.08))
    n_ex = sum(b["m2_upper_msun"] < lim for b in bounds)
    ctx.check(CHECK_RV, "passed" if n_ex == len(bounds) else "inconclusive",
              f"{len(t_all)} RVs from {len(used)} product(s); M2 upper bound (K + {params.get('z', 3.0)}σ, circular) "
              f"below {lim:g} M☉ for {n_ex} of {len(bounds)} period(s); tightest {min(b['m2_upper_mjup'] for b in bounds):.1f} MJup")
    for b in bounds:
        ctx.measure("rv_m2_upper", b["m2_upper_msun"], unit="Msun", method=f"circular fit at P={b['period_days']:g} d, K+zσ")
    return {**_clean_json(res), "file": _write(ctx, "rv_bounds.json", _clean_json(res))}


MEASURE_STEPS = {
    "stellar_context": step_stellar_context,
    "event_census": step_event_census,
    "moving_objects": step_moving_objects,
    "variability_guard": step_variability_guard,
    "fetch_independent": step_fetch_independent,
    "alias_cross_instrument": step_alias_cross_instrument,
    "rv_bounds": step_rv_bounds,
}
