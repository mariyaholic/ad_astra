"""Measures derived from data the campaign already fetches (docs/SUITE_EXPANSION.md §2, §4.2).

Pure functions, no network: the steps in ``measure_steps.py`` fetch, these compute. Every result
states its assumptions next to the number; a quantity that cannot be computed is ``None`` with a
reason, never a default. Nothing here raises an evidence level or names an object.
"""

from __future__ import annotations

import csv
import math
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

import numpy as np

G_SI, MSUN, RSUN = 6.674e-11, 1.989e30, 6.957e8
RHO_SUN = MSUN / (4 / 3 * math.pi * RSUN ** 3)          # kg m^-3 (≈ 1410)
MJUP_MSUN = 9.5458e-4
TESS_PIX_ARCSEC = 21.0
DWARF_TABLE = Path(__file__).with_name("data") / "mamajek_dwarfs_2022.04.16.csv"
DWARF_TABLE_REF = ("Mamajek mean dwarf sequence v2022.04.16 (Pecaut & Mamajek 2013, ApJS 208, 9); "
                   "Gaia DR2 colours and M_G, applied to DR3 photometry without extinction correction")


def _f(v: Any) -> float | None:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def _q(v: Any) -> float | None:
    """A number that may carry a unit, as SkyBoT/astroquery rows do ('297.8 arcsec', '-36.1 arcsec / h')."""
    x = _f(v)
    if x is not None or v is None:
        return x
    m = re.match(r"\s*([-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)", str(v))
    return _f(m.group(1)) if m else None


def sep_arcsec(ra1, dec1, ra2, dec2) -> float:
    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(r1 - r2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c)))) * 3600


# ------------------------------------------------------------------ stellar priors from Gaia
@lru_cache(maxsize=1)
def dwarf_table() -> dict[str, np.ndarray]:
    rows = [r for r in csv.DictReader(line for line in DWARF_TABLE.read_text(encoding="utf-8").splitlines()
                                      if not line.startswith("#"))]
    out = {k: np.array([float(r[k]) for r in rows]) for k in ("teff_k", "bp_rp", "abs_g", "radius_rsun", "mass_msun")}
    out["spt"] = np.array([r["spt"] for r in rows])
    return out


def _colour_range() -> tuple[np.ndarray, int]:
    """The table rows where Bp-Rp increases monotonically (it turns over after M8.5V)."""
    b = dwarf_table()["bp_rp"]
    stop = next((i for i in range(1, b.size) if b[i] <= b[i - 1]), b.size)
    return b[:stop], stop


def teff_from_bprp(bp_rp: float | None) -> tuple[float | None, str]:
    """Dwarf Teff at a Gaia Bp-Rp colour, interpolated in the mean dwarf sequence."""
    if bp_rp is None:
        return None, "no Bp-Rp colour"
    b, stop = _colour_range()
    if not b[0] <= bp_rp <= b[-1]:
        return None, f"Bp-Rp {bp_rp:.3f} outside the tabulated dwarf range {b[0]:.3f}..{b[-1]:.3f}"
    return float(np.interp(bp_rp, b, dwarf_table()["teff_k"][:stop])), "interpolated in " + DWARF_TABLE_REF


def stellar_priors(row: dict, *, min_parallax_over_error: float = 5.0, ruwe_max: float = 1.4,
                   radius_frac_floor: float = 0.08, mass_frac_floor: float = 0.10,
                   max_offset_from_sequence_mag: float = 1.0) -> dict:
    """Teff, R*, M* and mean density for one Gaia DR3 source, assuming a main-sequence dwarf.

    Absolute G uses the parallax without extinction. R* and M* are interpolated in absolute G on
    the mean dwarf sequence; the stated uncertainty is the parallax-driven spread combined with a
    declared fractional floor (the sequence's intrinsic width is not tabulated). A star more than
    ``max_offset_from_sequence_mag`` from the sequence at its colour is not given dwarf priors.
    """
    g, bp_rp = _f(row.get("phot_g_mean_mag")), _f(row.get("bp_rp"))
    plx, eplx, ruwe = _f(row.get("parallax")), _f(row.get("parallax_error")), _f(row.get("ruwe"))
    out: dict[str, Any] = {"source_id": row.get("source_id"), "phot_g_mean_mag": g, "bp_rp": bp_rp, "parallax_mas": plx,
                           "parallax_error_mas": eplx, "ruwe": ruwe, "usable": False,
                           "assumptions": ["main-sequence dwarf", "no extinction", "single star",
                                           f"fractional floors R {radius_frac_floor:g}, M {mass_frac_floor:g} (declared)"],
                           "table": DWARF_TABLE_REF}
    teff, why = teff_from_bprp(bp_rp)
    out["teff_k"], out["teff_note"] = teff, why
    problems = []
    if g is None or plx is None or plx <= 0:
        problems.append("no positive parallax or G magnitude")
    elif eplx is None or eplx <= 0 or plx / eplx < min_parallax_over_error:
        problems.append(f"parallax/error {'n/a' if not eplx else f'{plx / eplx:.1f}'} < {min_parallax_over_error:g}")
    if ruwe is None or ruwe >= ruwe_max:
        problems.append(f"RUWE {ruwe if ruwe is not None else 'n/a'} ≥ {ruwe_max:g} (or missing): astrometry may be perturbed")
    if teff is None:
        problems.append(why)
    if problems:
        out["reason"] = "; ".join(problems)
        return out
    tab = dwarf_table()
    abs_g = g + 5 * math.log10(plx / 100.0)
    e_abs = 5 / math.log(10) * eplx / plx
    b, stop = _colour_range()
    seq_g = float(np.interp(bp_rp, b, tab["abs_g"][:stop]))
    out.update({"abs_g": abs_g, "abs_g_err": e_abs, "sequence_abs_g_at_colour": seq_g, "offset_from_sequence_mag": abs_g - seq_g})
    if abs(abs_g - seq_g) > max_offset_from_sequence_mag:
        side = "above (brighter: evolved, unresolved binary or young)" if abs_g < seq_g else "below (subdwarf or bad photometry)"
        out["reason"] = f"{abs(abs_g - seq_g):.2f} mag {side} the dwarf sequence at this colour; dwarf priors not applied"
        return out
    ag, rr, mm = tab["abs_g"], tab["radius_rsun"], tab["mass_msun"]
    if not ag[0] <= abs_g <= ag[-1]:
        out["reason"] = f"M_G {abs_g:.2f} outside the tabulated range"
        return out
    r = float(np.interp(abs_g, ag, rr))
    m = float(np.interp(abs_g, ag, mm))
    spread_r = abs(float(np.interp(abs_g - e_abs, ag, rr)) - float(np.interp(abs_g + e_abs, ag, rr))) / 2
    spread_m = abs(float(np.interp(abs_g - e_abs, ag, mm)) - float(np.interp(abs_g + e_abs, ag, mm))) / 2
    er = math.hypot(spread_r, radius_frac_floor * r)
    em = math.hypot(spread_m, mass_frac_floor * m)
    rho = m / r ** 3
    erho = rho * math.sqrt((em / m) ** 2 + (3 * er / r) ** 2)
    out.update({"usable": True, "radius_rsun": r, "radius_err_rsun": er, "mass_msun": m, "mass_err_msun": em,
                "density_rho_sun": rho, "density_err_rho_sun": erho})
    return out


# ------------------------------------------------------------------ epochs and identification
def julian_year(epoch: Any) -> float | None:
    """'J2015.5' / 2015.5 / 'J2000.0' → 2015.5; anything else → None (an unverified epoch is not guessed)."""
    if isinstance(epoch, (int, float)):
        return float(epoch)
    s = str(epoch or "").strip().upper()
    if s.startswith("J"):
        s = s[1:]
    return _f(s)


def bjd_to_jyear(bjd: float) -> float:
    return 2000.0 + (bjd - 2451545.0) / 365.25


def propagate(ra: float, dec: float, pmra_masyr: float | None, pmdec_masyr: float | None, dt_years: float) -> tuple[float, float]:
    """Linear proper-motion propagation (pmra includes cos δ). Adequate for arcsecond matching over decades."""
    if pmra_masyr is None or pmdec_masyr is None or dt_years == 0:
        return ra, dec
    dec2 = dec + pmdec_masyr * dt_years / 3.6e6
    ra2 = ra + pmra_masyr * dt_years / 3.6e6 / max(1e-9, math.cos(math.radians(dec)))
    return ra2 % 360.0, dec2


def identify(rows: list[dict], ra: float, dec: float, *, position_epoch: float | None, gaia_epoch: float = 2016.0,
             high_pm_arcsec: float = 1.0) -> dict | None:
    """Nearest Gaia source to a target position after moving every source to the position's epoch.

    Returns the match with its separation before and after propagation, the proper-motion shift, and
    the next-nearest source. With no epoch for the target position, sources are compared at 2016.0 and
    the result says so.
    """
    cands = []
    for r in rows:
        r_ra, r_dec = _f(r.get("ra")), _f(r.get("dec"))
        if r_ra is None or r_dec is None:
            continue
        pmra, pmdec = _f(r.get("pmra")), _f(r.get("pmdec"))
        raw = sep_arcsec(ra, dec, r_ra, r_dec)
        if position_epoch is not None:
            p_ra, p_dec = propagate(r_ra, r_dec, pmra, pmdec, position_epoch - gaia_epoch)
            sep = sep_arcsec(ra, dec, p_ra, p_dec)
        else:
            sep = raw
        shift = (math.hypot(pmra, pmdec) * abs((position_epoch or gaia_epoch) - gaia_epoch) / 1000
                 if pmra is not None and pmdec is not None else None)
        cands.append({"source_id": r.get("source_id"), "sep_arcsec": sep, "sep_unpropagated_arcsec": raw,
                      "pm_shift_arcsec": shift, "phot_g_mean_mag": _f(r.get("phot_g_mean_mag")), "row": r})
    if not cands:
        return None
    cands.sort(key=lambda c: (c["sep_arcsec"], str(c["source_id"])))
    best = dict(cands[0])
    best["propagated_to"] = position_epoch
    best["high_proper_motion"] = bool(best["pm_shift_arcsec"] is not None and best["pm_shift_arcsec"] >= high_pm_arcsec)
    if len(cands) > 1:
        nxt = cands[1]
        best["next"] = {"source_id": nxt["source_id"], "sep_arcsec": nxt["sep_arcsec"],
                        "delta_g": (None if nxt["phot_g_mean_mag"] is None or best["phot_g_mean_mag"] is None
                                    else nxt["phot_g_mean_mag"] - best["phot_g_mean_mag"])}
    return best


def dilution_census(rows: list[dict], target_source_id: Any, target_g: float | None, *, ra: float, dec: float,
                    aperture_arcsec: float, depth_ppm: float | None) -> dict:
    """Flux from Gaia neighbours inside a TESS-scale aperture, and which could produce the depth alone.

    A neighbour contributing a fraction f of the total flux can produce at most a depth f (if it were
    fully eclipsed). Gaia G stands in for the TESS band (both broad red-optical); positions are Gaia's
    2016.0 values; sources Gaia did not resolve (≲ 1″ pairs, very bright stars' wings) are not counted.
    """
    if target_g is None:
        return {"computed": False, "reason": "target has no Gaia G magnitude"}
    nb, no_g = [], []
    for r in rows:
        if str(r.get("source_id")) == str(target_source_id):
            continue
        r_ra, r_dec, g = _f(r.get("ra")), _f(r.get("dec")), _f(r.get("phot_g_mean_mag"))
        if r_ra is None or r_dec is None:
            continue
        s = sep_arcsec(ra, dec, r_ra, r_dec)
        if s > aperture_arcsec:
            continue
        if g is None:
            no_g.append({"source_id": r.get("source_id"), "sep_arcsec": s})
            continue
        nb.append({"source_id": r.get("source_id"), "sep_arcsec": s, "phot_g_mean_mag": g,
                   "flux_ratio_to_target": 10 ** (-0.4 * (g - target_g))})
    total = 1.0 + sum(n["flux_ratio_to_target"] for n in nb)
    for n in nb:
        n["max_depth_ppm_if_fully_eclipsed"] = n["flux_ratio_to_target"] / total * 1e6
        n["could_mimic_depth"] = bool(depth_ppm is not None and n["max_depth_ppm_if_fully_eclipsed"] >= depth_ppm)
    nb.sort(key=lambda n: -n["flux_ratio_to_target"])
    return {"computed": True, "aperture_arcsec": aperture_arcsec, "depth_ppm": depth_ppm,
            "n_neighbours": len(nb), "neighbours": nb[:25], "neighbours_without_g": no_g[:25],
            "contamination_fraction": 1 - 1 / total,
            "depth_dilution_factor": total,
            "n_could_mimic": sum(n["could_mimic_depth"] for n in nb),
            "assumptions": ["Gaia G as a proxy for the TESS band", "circular aperture of the stated radius",
                            "Gaia DR3 2016.0 positions", "unresolved companions not counted"]}


# ------------------------------------------------------------------ duration likelihood per period alias
def transit_duration_days(period_d: np.ndarray, rho_kgm3: np.ndarray, b: np.ndarray, k: float) -> np.ndarray:
    """Total (T14) duration of a circular orbit, exact geometry (Seager & Mallén-Ornelas 2003, eq. 3)."""
    a_r = (G_SI * rho_kgm3 * (period_d * 86400.0) ** 2 / (3 * math.pi)) ** (1 / 3)
    sin_i = np.sqrt(np.clip(1 - (b / a_r) ** 2, 0, 1))
    arg = np.sqrt(np.clip((1 + k) ** 2 - b ** 2, 0, None)) / (a_r * sin_i)
    return period_d / math.pi * np.arcsin(np.clip(arg, 0, 1))


def alias_duration_likelihood(periods_days: Iterable[float], duration_h: float, duration_err_h: float,
                              rho_sun: float, rho_err_sun: float, *, k: float = 0.1, n: int = 4000,
                              seed: int = 0) -> list[dict]:
    """Likelihood of the observed transit duration under each period alias.

    Marginalises a uniform impact parameter b ∈ [0, 1) and a Gaussian stellar density (truncated at
    zero) for a circular orbit with radius ratio ``k``. Returned per alias: the likelihood, the
    median predicted duration, and two normalised weights across the given aliases — by likelihood
    alone, and by likelihood × geometric transit probability (∝ P^-2/3). No occurrence-rate prior is
    applied, and an eccentric orbit can lengthen or shorten a transit, so a low weight disfavours an
    alias only under these stated assumptions.
    """
    rng = np.random.default_rng(seed)
    rho = rho_sun + rho_err_sun * rng.standard_normal(n)
    rho = np.where(rho > 0, rho, np.nan) * RHO_SUN
    b = rng.uniform(0, 1, n)
    obs, err = duration_h / 24, max(duration_err_h, 1e-6) / 24
    out = []
    for P in periods_days:
        T = transit_duration_days(np.full(n, float(P)), rho, b, k)
        ok = np.isfinite(T) & (T > 0)
        like = float(np.mean(np.where(ok, np.exp(-0.5 * ((T - obs) / err) ** 2) / (err * math.sqrt(2 * math.pi)), 0.0)))
        out.append({"period_days": float(P), "likelihood": like,
                    "predicted_duration_h_median": float(np.nanmedian(T[ok]) * 24) if ok.any() else None,
                    "predicted_duration_h_16_84": ([float(np.nanpercentile(T[ok], 16) * 24), float(np.nanpercentile(T[ok], 84) * 24)]
                                                   if ok.any() else None)})
    tot = sum(a["likelihood"] for a in out)
    geo = [a["likelihood"] * a["period_days"] ** (-2 / 3) for a in out]
    tg = sum(geo)
    for a, g in zip(out, geo):
        a["weight_likelihood_only"] = a["likelihood"] / tot if tot > 0 else None
        a["weight_with_transit_probability"] = g / tg if tg > 0 else None
    return out


# ------------------------------------------------------------------ per-event artifact census
QUALITY_BITS = {1: "attitude tweak", 2: "safe mode", 4: "coarse point", 8: "earth point", 16: "argabrightening",
                32: "momentum dump", 64: "aperture cosmic", 128: "manual exclude", 256: "discontinuity",
                512: "impulsive outlier", 1024: "collateral cosmic", 2048: "scattered light", 4096: "scattered light 2",
                8192: "planet-search exclude", 16384: "bad calibration", 32768: "insufficient targets"}
# bits that can themselves imprint a dip-like feature on the photometry
ARTIFACT_BITS = (1, 2, 4, 8, 16, 32, 128, 256, 2048, 4096, 16384)


def _rsig(x: np.ndarray) -> float:
    x = x[np.isfinite(x)]
    return float(1.4826 * np.median(np.abs(x - np.median(x)))) if x.size else float("nan")


def event_census(t: np.ndarray, quality: np.ndarray, series: dict[str, np.ndarray], *, t_mid: float, dur_d: float,
                 pad_d: float = 0.25, baseline_d: float = 1.0, z_max: float = 5.0) -> dict:
    """Quality bits near an event and in-event shifts of engineering series.

    ``series`` holds e.g. MOM_CENTR1/2, POS_CORR1/2, SAP_BKG. For each, the shift is the in-event
    median minus the median of a local baseline (±``baseline_d`` excluding the event), in units of
    the baseline's robust scatter / √n_in. A shift beyond ``z_max`` is flagged: a real on-target
    transit does not move the pointing or the background, though a blended one can move a centroid.
    """
    def census(mask):
        out: dict[str, int] = {}
        for q in quality[mask]:
            q = int(q)
            for bit, name in QUALITY_BITS.items():
                if q & bit:
                    out[name] = out.get(name, 0) + 1
        return out

    artifact_names = {QUALITY_BITS[b] for b in ARTIFACT_BITS}
    bits = census(np.isfinite(t) & (np.abs(t - t_mid) <= dur_d / 2 + pad_d))
    bits_in = census(np.isfinite(t) & (np.abs(t - t_mid) <= dur_d / 2))
    flagged_bits = sorted(artifact_names & set(bits))
    flagged_in = sorted(artifact_names & set(bits_in))
    inev = np.isfinite(t) & (np.abs(t - t_mid) <= dur_d / 2) & (quality == 0)
    base = np.isfinite(t) & (np.abs(t - t_mid) > dur_d / 2 + pad_d) & (np.abs(t - t_mid) <= baseline_d) & (quality == 0)
    shifts = {}
    for name, y in series.items():
        y = np.asarray(y, float)
        yi, yb = y[inev & np.isfinite(y)], y[base & np.isfinite(y)]
        if yi.size < 2 or yb.size < 10:
            shifts[name] = {"tested": False, "reason": f"{yi.size} in-event / {yb.size} baseline finite cadences"}
            continue
        s = _rsig(yb)
        d = float(np.median(yi) - np.median(yb))
        z = d / (s / math.sqrt(yi.size)) if s > 0 else float("inf") if d else 0.0
        shifts[name] = {"tested": True, "shift": d, "baseline_robust_sigma": s, "z": z, "n_in": int(yi.size),
                        "flagged": bool(abs(z) > z_max)}
    flagged_series = sorted(k for k, v in shifts.items() if v.get("flagged"))
    # an artifact bit on the event's own cadences, or a shifted series, makes the event suspect; a bit only
    # in the surrounding pad is a caution (as vet's quality check reads it), not a failure
    return {"t_mid": t_mid, "window_days": dur_d, "pad_days": pad_d, "quality_bits_near": bits,
            "quality_bits_in_event": bits_in, "artifact_bits_near": flagged_bits, "artifact_bits_in_event": flagged_in,
            "series": shifts, "flagged_series": flagged_series,
            "clean": not flagged_bits and not flagged_series,
            "suspect": bool(flagged_in or flagged_series),
            "tested_series": sorted(k for k, v in shifts.items() if v.get("tested"))}


# ------------------------------------------------------------------ time conversion for ephemeris services
def bjd_tdb_to_utc_iso(bjd_tdb: float, ra_deg: float, dec_deg: float) -> str:
    """Geocentric UTC for a BJD_TDB timestamp (removes the barycentric light-travel time toward the target)."""
    import astropy.units as u
    from astropy.coordinates import EarthLocation, SkyCoord
    from astropy.time import Time

    coord = SkyCoord(ra_deg * u.deg, dec_deg * u.deg, frame="icrs")
    geo = EarthLocation.from_geocentric(0 * u.m, 0 * u.m, 0 * u.m)
    t = Time(bjd_tdb, format="jd", scale="tdb", location=geo)
    ltt = t.light_travel_time(coord, kind="barycentric")
    return (t - ltt).utc.isot


def moving_object_hits(rows: list[dict], *, target_mag: float | None, depth_ppm: float | None,
                       min_flux_fraction_of_depth: float = 0.1, near_arcsec: float | None = None,
                       window_h: float = 1.0) -> dict:
    """Known solar-system objects at an event epoch that are bright enough, and close enough, to matter.

    An object crossing the target or background aperture changes the measured flux by about its flux
    ratio to the target (V against the target's TESS magnitude, a colour-blind approximation). It is
    counted when that ratio is at least ``min_flux_fraction_of_depth`` x the event depth. With
    ``near_arcsec`` set it also has to lie within ``near_arcsec`` plus its own motion over ``window_h``
    hours of the target (positions must then be computed for the right observer: TESS, not the
    geocentre); one whose distance is not given is listed as ``unknown_distance``. An object with no V
    is listed as ``unknown_brightness``. Values may carry units ('297.8 arcsec').
    """
    def col(r, *names):
        for n in names:
            for k in r:
                if k.lower() == n.lower():
                    return r[k]
        return None

    hits, unknown, undist, faint, far = [], [], [], 0, 0
    for r in rows:
        v = _q(col(r, "V", "Vmag", "vmag"))
        d = _q(col(r, "centerdist", "centdist", "posdist"))
        name = col(r, "Name", "name") or col(r, "Number", "num")
        rate = math.hypot(_q(col(r, "RA_rate", "RA_rate_cosdec")) or 0.0, _q(col(r, "DEC_rate")) or 0.0)
        reach = None if near_arcsec is None else near_arcsec + rate * window_h
        if reach is not None and d is not None and d > reach:
            far += 1
            continue
        if v is None:
            unknown.append({"name": name, "dist_arcsec": d})
            continue
        ratio = 10 ** (-0.4 * (v - target_mag)) if target_mag is not None else None
        if not (ratio is None or depth_ppm is None or ratio >= min_flux_fraction_of_depth * depth_ppm * 1e-6):
            faint += 1
            continue
        item = {"name": name, "V": v, "dist_arcsec": d, "flux_ratio_to_target": ratio}
        (undist if reach is not None and d is None else hits).append(item)
    return {"n_rows": len(rows), "bright_enough": hits, "unknown_brightness": unknown, "unknown_distance": undist,
            "too_faint": faint, "too_far": far, "near_arcsec": near_arcsec, "window_h": window_h}


# ------------------------------------------------------------------ catalogue class and variability guards
_ECLIPSING_EXCLUDE = ("EP",)          # VSX "EP" = exoplanet transit, not an eclipsing binary


def vsx_classify(vtype: str | None) -> str:
    t = (vtype or "").strip().upper().rstrip(":")
    if not t:
        return "unclassified"
    parts = [p.strip(":") for p in t.replace("|", "+").replace("/", "+").split("+")]
    if any(p.startswith("EP") for p in parts):
        return "transit"
    if any(p == "ELL" for p in parts):
        return "ellipsoidal"
    if any(p.startswith("E") and p not in _ECLIPSING_EXCLUDE for p in parts):
        return "eclipsing"
    return "other_variable"


def period_collision(p1: float, p2: float, *, tol: float = 0.01, ratios=(0.5, 1.0, 2.0)) -> float | None:
    """The ratio r in ``ratios`` with |p1 / (r p2) − 1| < tol, else None."""
    for r in ratios:
        if p2 > 0 and abs(p1 / (r * p2) - 1) < tol:
            return r
    return None


def vsx_guard(rows: list[dict], ra: float, dec: float, *, match_arcsec: float, periods: Iterable[float] = (),
              tol: float = 0.01) -> dict:
    periods = [float(p) for p in periods if p]
    entries = []
    for r in rows:
        r_ra, r_dec = _f(r.get("RAJ2000") or r.get("ra")), _f(r.get("DEJ2000") or r.get("dec"))
        if r_ra is None or r_dec is None:
            continue
        s = sep_arcsec(ra, dec, r_ra, r_dec)
        if s > match_arcsec:
            continue
        p = _f(r.get("Period") or r.get("period"))
        cls = vsx_classify(r.get("Type") or r.get("type"))
        coll = [{"period_days": q, "ratio": rr} for q in periods if p and (rr := period_collision(q, p, tol=tol))]
        entries.append({"name": r.get("Name") or r.get("name"), "type": r.get("Type") or r.get("type"), "class": cls,
                        "period_days": p, "sep_arcsec": s, "period_collisions": coll})
    state = "passed"
    if any(e["class"] in ("eclipsing", "ellipsoidal") for e in entries):
        state = "failed"
    elif any(e["period_collisions"] for e in entries):
        state = "inconclusive"
    return {"state": state, "entries": entries}


SIMBAD_CLASSES = {
    "eclipsing_or_ellipsoidal": {"EB*", "EB?", "El*", "El?"},
    "multiple": {"SB*", "SB?", "**", "**?"},
    "evolved": {"RG*", "RG?", "AB*", "AB?", "LP*", "LP?", "Mi*", "Mi?", "C*", "C*?", "S*", "S*?", "HB*", "HB?",
                "sg*", "sg?", "s*r", "s?r", "s*y", "s?y", "s*b", "s?b", "Ce*", "Ce?", "RR*", "RR?", "WR*", "WR?"},
    "accreting_or_young": {"CV*", "CV?", "No*", "No?", "Y*O", "Y*?", "YSO", "TT*", "TT?", "Or*", "Ae*", "Ae?", "XB*", "XB?"},
    "extragalactic": {"G", "G?", "GiC", "GiG", "GiP", "AGN", "AG?", "QSO", "Q?", "Sy1", "Sy2", "SyG", "LIN", "BLL", "Bla",
                      "EmG", "SBG", "rG", "H2G", "LSB", "bCG", "IG", "PaG", "BiC", "ClG", "GrG"},
}


def simbad_class(otype: str | None) -> str:
    o = (otype or "").strip()
    for cls, codes in SIMBAD_CLASSES.items():
        if o in codes:
            return cls
    return "star_or_other" if o else "unclassified"


def simbad_guard(rows: list[dict], ra: float, dec: float, *, match_arcsec: float) -> dict:
    near = []
    for r in rows:
        r_ra, r_dec = _f(r.get("ra")), _f(r.get("dec"))
        if r_ra is None or r_dec is None:
            continue
        s = sep_arcsec(ra, dec, r_ra, r_dec)
        if s <= match_arcsec:
            near.append({"main_id": r.get("main_id"), "otype": r.get("otype"), "class": simbad_class(r.get("otype")),
                         "sep_arcsec": s})
    near.sort(key=lambda e: e["sep_arcsec"])
    if not near:
        return {"state": "inconclusive", "entries": [], "reason": f"no SIMBAD object within {match_arcsec:g}″"}
    cls = near[0]["class"]
    state = ("failed" if cls in ("eclipsing_or_ellipsoidal", "extragalactic") else
             "inconclusive" if cls in ("multiple", "evolved", "accreting_or_young", "unclassified") else "passed")
    return {"state": state, "entries": near[:10], "nearest_class": cls}


# ------------------------------------------------------------------ independent data at predicted alias epochs
def alias_depths_in_series(t_bjd: np.ndarray, flux: np.ndarray, *, t0: float, periods: Iterable[float], dur_d: float,
                           ref_depth_ppm: float, min_points: int = 3, excluded_below: float = 0.3,
                           supported_within: float = 0.5, baseline_d: float = 3.0, skip: Iterable[float] = ()) -> list[dict]:
    """Depth at every predicted transit of each alias in an independent light curve.

    For each alias P the predicted epochs t0 + nP inside the series are combined: in-transit points
    (|t − t_n| ≤ 0.4 × duration, the flat bottom for most geometries) against points within
    ``baseline_d`` of the same epochs but outside the transit. The combined depth and its standard
    error decide: ``excluded`` if depth + 2σ < ``excluded_below`` × the reference depth, ``supported``
    if |depth − ref| < ``supported_within`` × ref and depth > 3σ, else ``undecided``; fewer than
    ``min_points`` in-transit points is ``untested``. Epochs in ``skip`` (the transits the alias was
    derived from) are not used.
    """
    t = np.asarray(t_bjd, float)
    y = np.asarray(flux, float)
    ok = np.isfinite(t) & np.isfinite(y)
    t, y = t[ok], y[ok]
    ref = ref_depth_ppm * 1e-6
    skip = [float(s) for s in skip]
    out = []
    if t.size == 0:
        return out
    lo, hi = float(t.min()), float(t.max())
    for P in periods:
        P = float(P)
        n0, n1 = math.ceil((lo - t0) / P - 0.01), math.floor((hi - t0) / P + 0.01)
        ins, outs, used = [], [], []
        for n in range(n0, n1 + 1):
            tp = t0 + n * P
            if any(abs(tp - s) < dur_d for s in skip):
                continue
            din = np.abs(t - tp) <= 0.4 * dur_d
            dout = (np.abs(t - tp) > 0.75 * dur_d) & (np.abs(t - tp) <= baseline_d)
            if din.any() and dout.sum() >= 3:
                base = np.median(y[dout])
                ins.append(y[din] / base)
                outs.append(y[dout] / base)
                used.append({"predicted_bjd": tp, "n_in": int(din.sum())})
        n_in = sum(a.size for a in ins)
        if n_in < min_points:
            out.append({"period_days": P, "verdict": "untested", "n_in": n_in, "epochs": used})
            continue
        yi, yo = np.concatenate(ins), np.concatenate(outs)
        depth = float(1 - np.median(yi))
        sig = _rsig(yo)
        err = 1.2533 * sig / math.sqrt(yi.size) if sig > 0 else float("nan")   # standard error of a median
        if np.isfinite(err) and depth + 2 * err < excluded_below * ref:
            verdict = "excluded"
        elif np.isfinite(err) and abs(depth - ref) < supported_within * ref and depth > 3 * err:
            verdict = "supported"
        else:
            verdict = "undecided"
        out.append({"period_days": P, "verdict": verdict, "depth_ppm": depth * 1e6,
                    "depth_err_ppm": err * 1e6 if np.isfinite(err) else None, "n_in": int(yi.size), "epochs": used})
    return out


# ------------------------------------------------------------------ RV bounds on a companion
def rv_sinusoid_fit(t: np.ndarray, rv: np.ndarray, err: np.ndarray, period_d: float, *, jitter: float = 0.0) -> dict:
    """Weighted least squares rv = c + A sin φ + B cos φ at a fixed period (circular orbit).

    Returns K = √(A² + B²), its 1σ error (linearised), and the reduced χ². Units follow the input.
    """
    t, rv, err = (np.asarray(a, float) for a in (t, rv, err))
    w = 1 / (err ** 2 + jitter ** 2)
    ph = 2 * math.pi * (t - t.min()) / period_d
    X = np.column_stack([np.ones_like(t), np.sin(ph), np.cos(ph)])
    W = np.diag(w)
    cov = np.linalg.pinv(X.T @ W @ X)
    beta = cov @ X.T @ W @ rv
    c, A, B = beta
    K = float(math.hypot(A, B))
    J = np.array([0, A / K, B / K]) if K > 0 else np.array([0, 1.0, 0])
    eK = float(math.sqrt(max(J @ cov @ J, 0)))
    resid = rv - X @ beta
    dof = max(1, t.size - 3)
    return {"K": K, "K_err": eK, "offset": float(c), "chi2_red": float(np.sum(w * resid ** 2) / dof), "n": int(t.size)}


def mass_function_msun(period_d: float, k_ms: float, e: float = 0.0) -> float:
    return (period_d * 86400) * k_ms ** 3 * (1 - e ** 2) ** 1.5 / (2 * math.pi * G_SI) / MSUN


def companion_min_mass_msun(f_m: float, m1: float) -> float:
    """Solve (M2 sin i)^3 / (M1 + M2)^2 = f(M) for M2 with sin i = 1 (the minimum companion mass)."""
    if f_m <= 0:
        return 0.0
    h = lambda m2: m2 ** 3 - f_m * (m1 + m2) ** 2        # negative below the root, positive above it
    lo, hi = 0.0, max(1.0, 2 * m1)
    while h(hi) < 0:
        hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if h(mid) < 0 else (lo, mid)
        if hi - lo < 1e-12 * max(1.0, hi):
            break
    return (lo + hi) / 2


def rv_companion_bounds(t, rv_ms, err_ms, periods_days: Iterable[float], *, m1_msun: float, jitter_ms: float = 0.0,
                        z: float = 3.0) -> list[dict]:
    """Per period alias: the fitted semi-amplitude and the (K + zσ) upper bound turned into an upper
    bound on M2 sin i for a circular orbit. For a transiting companion sin i ≈ 1, so this bounds M2."""
    out = []
    for P in periods_days:
        fit = rv_sinusoid_fit(t, rv_ms, err_ms, float(P), jitter=jitter_ms)
        scale = math.sqrt(max(fit["chi2_red"], 1.0))            # inflate for unmodelled scatter
        k_up = fit["K"] + z * fit["K_err"] * scale
        m2_up = companion_min_mass_msun(mass_function_msun(float(P), k_up), m1_msun)
        out.append({"period_days": float(P), **fit, "K_upper": k_up, "error_scale": scale,
                    "m2_upper_msun": m2_up, "m2_upper_mjup": m2_up / MJUP_MSUN})
    return out


# ------------------------------------------------------------------ calibrated cutout photometry
def image_zeropoint(header) -> tuple[float | None, str]:
    """Magnitude zero point for flux units a header states outright; otherwise None (instrumental only)."""
    bunit = str(header.get("BUNIT", "")).strip().lower()
    if "nanomagg" in bunit:
        return 22.5, "BUNIT nanomaggies: m = 22.5 − 2.5 log10(flux)"
    for key in ("MAGZP", "MAGZERO", "ZEROPT", "PHOTZP"):
        if _f(header.get(key)) is not None:
            return float(header[key]), f"header {key}"
    return None, "no photometric zero point in the header; instrumental counts only"


def aperture_photometry(image: np.ndarray, x: float, y: float, r_pix: float, r_in: float, r_out: float) -> dict:
    yy, xx = np.indices(image.shape)
    rr = np.hypot(xx - x, yy - y)
    ap = rr <= r_pix
    ann = (rr >= r_in) & (rr <= r_out) & np.isfinite(image)
    if not ap.any() or ann.sum() < 10 or not np.isfinite(image[ap]).all():
        return {"measured": False, "reason": "aperture off the image, non-finite pixels, or too small an annulus"}
    sky = float(np.median(image[ann]))
    ssig = _rsig(image[ann])
    flux = float(np.sum(image[ap] - sky))
    err = float(ssig * math.sqrt(ap.sum()))
    return {"measured": True, "flux": flux, "flux_err_sky": err, "sky": sky, "n_pix": int(ap.sum()),
            "snr": flux / err if err > 0 else None}
