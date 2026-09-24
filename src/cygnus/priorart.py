"""Prior-Art / Known-Object Gate.

Detects 'already known' collisions before any candidate leaves the worktree
(AGENTS.md protocol step 6; design & gates in ``ANALYSIS_STACK.md § Prior-Art``).

Contract:

* every candidate passes through this gate before evidence can rise above
  ``unverified_lead``;
* offline mode (``allow_network=False``) records every network service as
  ``not_tested`` — never ``passed`` — matching the audit-state discipline;
* each service adapter result string carries the epoch-relative phrasing
  ('no match / match detail as of <date>'), never a bare 'uncataloged'.
"""

from __future__ import annotations

from typing import Any

from .candidate_record import CandidateRecord
from .ledger import Ledger, now_utc

# Domain -> services whose catalog results must be pinned (incl. versions).
SERVICES_BY_DOMAIN: dict[str, tuple[str, ...]] = {
    "planetary": (
        "NASA_Exoplanet_Archive",
        "ExoFOP",
        "SPOC_DV_reports",
        "VSX",
        "Villanova_Kepler_EB",
        "ADS_literature",
    ),
    "variables": (
        "VSX",
        "GCVS",
        "ASAS_SN_variable_catalog",
        "ZTF_periodic_catalogs",
        "ADS_literature",
    ),
    "dark_companion": (
        "Gaia_NSS_TAP",
        "Gaia_black_hole_papers_ADS",
        "ADS_literature",
    ),
    "brown_dwarf": (
        "UltracoolSheet_style_compilations",
        "Montreal_White_Dwarf_DB",
        "ADS_literature",
    ),
    "solar_system": ("MPC", "SkyBoT", "NEOCP"),
    "lsb": ("SMUDGes_and_UDG_catalogs", "ADS_literature"),
    "transient": ("TNS", "ATel", "ALeRCE", "Gaia_alerts", "ADS_literature"),
    "microlensing": ("OGLE_EWS", "KMTNet_events", "ADS_literature"),
    "any": (),
}


def check_skybot(
    ra_deg: float | None,
    dec_deg: float | None,
    epoch_iso: str | None,
    *,
    radius_as: float = 10.0,
) -> str:
    """SkyBoT known-solar-system-object cone search (astroquery.imcce).

    Anonymous VO service [see DATA_SOURCES.md]. Must be called with the exact
    observation epoch because encoded trails are epoch-dependent.
    """
    if ra_deg is None or dec_deg is None or epoch_iso is None:
        return "not_tested (SkyBoT requires ra/dec/epoch inputs)"
    try:
        from astroquery.imcce import Skybot  # type: ignore
    except Exception:
        return "not_tested (astroquery extras not installed)"
    try:
        import astropy.units as u
        from astropy.coordinates import SkyCoord
        from astropy.time import Time

        coord = SkyCoord(ra_deg * u.deg, dec_deg * u.deg, frame="icrs")
        table = Skybot.cone_search(
            coord,
            radius=u.Quantity(radius_as, u.arcsec),
            epoch=Time(epoch_iso, scale="utc"),
        )
        n = 0 if table is None else len(table)
        if n == 0:
            return f"no known SSO within {radius_as}\" (retrieved {now_utc()})"
        return (
            f"MATCH: {n} known SSO(s) within {radius_as}\" at epoch "
            f"{epoch_iso} — treat as known object, not a new discovery"
        )
    except Exception as exc:  # network/API failure is inconclusive, not 'no match'
        return f"inconclusive (SkyBoT error: {exc.__class__.__name__}: {exc})"


def apply_gate(
    candidate: CandidateRecord,
    *,
    domain: str = "any",
    allow_network: bool = False,
    ledger: Ledger | None = None,
    ra_deg: float | None = None,
    dec_deg: float | None = None,
    epoch_iso: str | None = None,
) -> dict[str, str]:
    """Run the prior-art gate and return {service: result-line} for the record.

    Offline scaffold default: every network-backed service is recorded
    ``not_tested`` with its concrete blocker, so the audit trail is explicit
    rather than silently skipped. Ledger rows are written when available.
    """
    results: dict[str, str] = {}
    services = tuple(SERVICES_BY_DOMAIN.get(domain, ()))
    for svc in services:
        if svc == "SkyBoT":
            if not allow_network:
                results[svc] = "not_tested (offline scaffold; rerun with allow_network=True)"
            else:
                results[svc] = check_skybot(ra_deg, dec_deg, epoch_iso)
        else:
            results[svc] = "not_tested (adapter not implemented in scaffold)"
    if ledger is not None:
        for svc, res in results.items():
            ledger.add_prior_art(
                service=svc,
                result=res,
                gate="prior_art",
                query=f"domain={domain}",
                candidate_id=candidate.candidate_id,
            )
    return results
