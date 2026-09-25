"""Gaia NSS astrometric vetting.

Queries Gaia DR3 ``gaiadr3.nss_two_body_orbit`` for the campaign target and
interprets any non-single-star solution: solution type, period, eccentricity,
significance and — for solutions with a measured primary RV amplitude — the
spectroscopic mass function

    f(M) = P K1^3 (1 - e^2)^(3/2) / (2 pi G).

Interpretation discipline (matching ``cygnus.analysis.nss``): the table gives the
*photocentre* orbit and, where measured, the primary RV amplitude. A significant
NSS solution means the companion is already known to Gaia; that refutes a "new
unseen companion" hypothesis for this target. **No NSS solution is not proof of a
single star** — Gaia's sensitivity is incomplete — so an empty result is recorded
``inconclusive``, never ``passed``. A minimum companion mass would additionally
require an adopted primary mass and inclination, and is not claimed here.
"""

from __future__ import annotations

import math
from typing import Any

GAIA_TAP = "https://gea.esac.esa.int/tap-server/tap"
NSS_COLUMNS = ("source_id, nss_solution_type, ra, dec, parallax, period, period_error, eccentricity, "
               "eccentricity_error, semi_amplitude_primary, semi_amplitude_primary_error, mass_ratio, "
               "inclination, inclination_error, significance, goodness_of_fit, flags, astrometric_jitter")
G_KM3_PER_MSUN_S2 = 1.32712440018e11
SECONDS_PER_DAY = 86400.0


def _f(v: Any) -> float | None:
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def mass_function_msun(period_days: float, k1_kms: float, eccentricity: float) -> float | None:
    """Spectroscopic mass function f(M) in solar masses (None when the inputs are non-physical)."""
    if period_days <= 0 or k1_kms <= 0 or not (0.0 <= eccentricity < 1.0):
        return None
    return (period_days * SECONDS_PER_DAY * k1_kms ** 3 * (1 - eccentricity ** 2) ** 1.5
            / (2 * math.pi * G_KM3_PER_MSUN_S2))


def _sep_arcsec(ra1, dec1, ra2, dec2) -> float:
    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(r1 - r2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c)))) * 3600


def nearest_gaia_source(adapter, target, radius_arcsec: float) -> dict | None:
    """The closest Gaia source to the target within ``radius_arcsec`` (or None)."""
    r = radius_arcsec / 3600
    adql = (f"SELECT TOP 20 source_id, ra, dec, phot_g_mean_mag, parallax FROM gaiadr3.gaia_source WHERE "
            f"1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f}))")
    rows = adapter.tap_csv(f"{GAIA_TAP}/sync", adql)
    best = None
    for row in rows:
        ra, dec = _f(row.get("ra")), _f(row.get("dec"))
        if ra is None or dec is None:
            continue
        sep = _sep_arcsec(target.ra_deg, target.dec_deg, ra, dec)
        if sep <= radius_arcsec and (best is None or sep < best["sep_arcsec"]):
            best = {"source_id": str(row["source_id"]), "ra_deg": ra, "dec_deg": dec, "sep_arcsec": sep,
                    "phot_g_mean_mag": _f(row.get("phot_g_mean_mag")), "parallax": _f(row.get("parallax"))}
    return best


def query_nss(adapter, source_id: str, *, limit: int = 10) -> list[dict]:
    adql = f"SELECT TOP {int(limit)} {NSS_COLUMNS} FROM gaiadr3.nss_two_body_orbit WHERE source_id = {int(source_id)}"
    return adapter.tap_csv(f"{GAIA_TAP}/sync", adql)


def summarise_solution(row: dict) -> dict:
    """One NSS row as a typed summary, with the mass function where the inputs allow it."""
    period = _f(row.get("period"))
    ecc = _f(row.get("eccentricity"))
    k1 = _f(row.get("semi_amplitude_primary"))
    mf = mass_function_msun(period, k1, ecc) if (period is not None and k1 is not None and ecc is not None) else None
    return {"source_id": str(row.get("source_id")), "solution_type": (row.get("nss_solution_type") or "").strip(),
            "period_days": period, "period_error_days": _f(row.get("period_error")),
            "eccentricity": ecc, "semi_amplitude_primary_kms": k1,
            "mass_ratio": _f(row.get("mass_ratio")), "inclination_deg": _f(row.get("inclination")),
            "significance": _f(row.get("significance")), "goodness_of_fit": _f(row.get("goodness_of_fit")),
            "flags": row.get("flags"), "astrometric_jitter_mas": _f(row.get("astrometric_jitter")),
            "photocentre_mass_function_msun": mf,
            "mass_function_caveat": ("f(M) uses the NSS primary RV amplitude; a minimum companion mass additionally "
                                     "needs an adopted primary mass and inclination and is not claimed here."
                                     if mf is not None else None)}


def nss_vetting(adapter, target, *, radius_arcsec: float = 5.0, significance_min: float = 5.0,
                max_solutions: int = 10) -> dict:
    """Cross-match a target against Gaia DR3 NSS two-body solutions.

    State: ``failed`` when a solution at or above ``significance_min`` exists (the
    companion is already known, refuting novelty), ``inconclusive`` when the target
    is matched but no significant solution is present (absence is not proof),
    ``not_tested`` when the target cannot be matched at all.
    """
    nearest = nearest_gaia_source(adapter, target, radius_arcsec)
    if nearest is None:
        return {"state": "not_tested", "note": f"no Gaia DR3 source within {radius_arcsec:g}\" of the target",
                "solutions": [], "nss_solutions": 0}
    rows = query_nss(adapter, nearest["source_id"], limit=max_solutions)
    sols = [summarise_solution(r) for r in rows]
    significant = [s for s in sols if (s["significance"] or 0.0) >= significance_min]
    top = max(sols, key=lambda s: s["significance"] or 0.0) if sols else None
    out = {"target_match": nearest, "solutions": sols, "nss_solutions": len(sols),
           "significant_solutions": len(significant), "significance_min": significance_min,
           "top_mass_function_msun": top["photocentre_mass_function_msun"] if top else None}
    if significant:
        s = significant[0]
        out.update(state="failed",
                   note=(f"known astrometric companion: {s['solution_type']} significance {s['significance']:.1f}, "
                         f"P {s['period_days']:.3f} d, e {s['eccentricity']:.2f}"
                         + (f", f(M) {s['photocentre_mass_function_msun']:.3g} Msun"
                            if s["photocentre_mass_function_msun"] else "")
                         + "; a new-unseen-companion hypothesis for this target is refuted"))
    elif sols:
        out.update(state="inconclusive",
                   note=f"{len(sols)} NSS solution(s) below the significance {significance_min:g} threshold; "
                        "not treated as a companion")
    else:
        out.update(state="inconclusive",
                   note=f"no Gaia DR3 NSS two-body solution for source {nearest['source_id']} "
                        f"({nearest['sep_arcsec']:.2f}\" away); Gaia sensitivity is incomplete, so this is not proof of a single star")
    return out