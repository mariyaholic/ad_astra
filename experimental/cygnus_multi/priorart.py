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

from cygnus.candidate_record import CandidateRecord
from cygnus.ledger import Ledger, now_utc

# Domain -> services whose catalog results must be pinned (incl. versions).
SERVICES_BY_DOMAIN: dict[str, tuple[str, ...]] = {
    "planetary": (
        "NASA_Exoplanet_Archive",
        "TESS_TOI",
        "SIMBAD",
        "ExoFOP",
        "SPOC_DV_reports",
        "VSX",
        "Villanova_Kepler_EB",
        "ADS_literature",
    ),
    "variables": (
        "VSX",
        "SIMBAD",
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


CATALOGUE_SERVICES = ("NASA_Exoplanet_Archive", "TESS_TOI", "VSX", "SIMBAD")


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
        elif svc in CATALOGUE_SERVICES:
            if not allow_network:
                results[svc] = "not_tested (offline; rerun with allow_network=True)"
            elif ra_deg is None or dec_deg is None:
                results[svc] = "not_tested (cone search needs ra/dec)"
            else:
                results[svc] = catalogue_audit(ra_deg, dec_deg, services=[svc])[svc]["result"]
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


# ------------------------------------------------------------------ catalogue cone-search adapters
# Anonymous TAP services (DATA_SOURCES.md). Each returns a dated result line and the query verbatim,
# so the ledger's prior_art table records exactly what was asked and when. Errors are reported as
# errors (state 'error'), never as 'no match'.
_EXO_TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
_VIZIER_TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
_SIMBAD_TAP = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"


def _tap_csv(url: str, adql: str, timeout: float = 60.0) -> list[dict]:
    import csv
    import io

    import requests

    r = requests.post(url, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": adql},
                      headers={"User-Agent": "cygnus-priorart/0.1"}, timeout=timeout)
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):
        raise RuntimeError(f"TAP error response: {r.text[:300]}")
    return list(csv.DictReader(io.StringIO(r.text)))


def _sep_arcsec(ra1, dec1, ra2, dec2) -> float:
    import math

    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(r1 - r2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c)))) * 3600


def _cone(ra, dec, r_deg, racol, deccol, frame="ICRS"):
    return f"CONTAINS(POINT('{frame}', {racol}, {deccol}), CIRCLE('{frame}', {ra:.7f}, {dec:.7f}, {r_deg:.7f})) = 1"


def _adapters(ra: float, dec: float, radius_arcsec: float) -> dict:
    import math

    r = radius_arcsec / 3600
    dra = r / max(0.01, math.cos(math.radians(dec)))
    return {
        "NASA_Exoplanet_Archive": (_EXO_TAP, f"SELECT pl_name, hostname, ra, dec FROM pscomppars WHERE {_cone(ra, dec, r, 'ra', 'dec')}",
                                   lambda row: f"{row['pl_name']} (host {row['hostname']})", ("ra", "dec")),
        # the TOI table does not support CONTAINS; box query then an exact separation cut below
        "TESS_TOI": (_EXO_TAP, f"SELECT toi, tid, tfopwg_disp, ra, dec FROM toi WHERE ra BETWEEN {ra - dra:.7f} AND {ra + dra:.7f} "
                               f"AND dec BETWEEN {dec - r:.7f} AND {dec + r:.7f}",
                     lambda row: f"TOI-{row['toi']} (TIC {row['tid']}, disposition {row['tfopwg_disp'] or 'none'})", ("ra", "dec")),
        "VSX": (_VIZIER_TAP, f'SELECT "Name", "Type", "Period", RAJ2000, DEJ2000 FROM "B/vsx/vsx" WHERE {_cone(ra, dec, r, "RAJ2000", "DEJ2000")}',
                lambda row: f"{row['Name'].strip()} (type {row['Type'].strip() or '?'}, P {row['Period'] or '—'} d)", ("RAJ2000", "DEJ2000")),
        "SIMBAD": (_SIMBAD_TAP, f"SELECT main_id, otype, ra, dec FROM basic WHERE {_cone(ra, dec, r, 'ra', 'dec')}",
                   lambda row: f"{row['main_id']} ({row['otype']})", ("ra", "dec")),
    }


def catalogue_audit(ra_deg: float, dec_deg: float, *, radius_arcsec: float = 30.0,
                    services: list[str] | None = None, fetch=_tap_csv) -> dict[str, dict]:
    """Cone-search known-object catalogues around a position (ICRS, J2000; no proper-motion propagation
    is applied, so fast movers can fall outside a small radius — use ≥ 30″ for nearby stars).

    Returns ``{service: {state, result, query, retrieved_utc, matches}}``. ``state`` is ``done`` or
    ``error``; a ``done`` result with no rows reads "no match in <service> within r″ as of <date>".
    """
    out = {}
    for svc, (url, adql, fmt, (rc, dc)) in _adapters(ra_deg, dec_deg, radius_arcsec).items():
        if services and svc not in services:
            continue
        ts = now_utc()
        try:
            rows = fetch(url, adql)
            rows = [x for x in rows if x.get(rc) not in (None, "") and
                    _sep_arcsec(ra_deg, dec_deg, float(x[rc]), float(x[dc])) <= radius_arcsec]
            names = [fmt(x) for x in rows]
            if names:
                res = f"{len(names)} match(es) in {svc} within {radius_arcsec:g}\" as of {ts}: " + "; ".join(names[:12]) + \
                      ("" if len(names) <= 12 else f"; +{len(names) - 12} more")
            else:
                res = f"no match in {svc} within {radius_arcsec:g}\" as of {ts}"
            out[svc] = {"state": "done", "result": res, "query": adql, "retrieved_utc": ts, "matches": names}
        except Exception as exc:  # noqa: BLE001 - an outage is inconclusive, never 'no match'
            out[svc] = {"state": "error", "result": f"inconclusive ({svc} query failed as of {ts}: {type(exc).__name__}: {str(exc)[:200]})",
                        "query": adql, "retrieved_utc": ts, "matches": []}
    return out
