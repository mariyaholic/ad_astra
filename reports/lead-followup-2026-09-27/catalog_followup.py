"""Refresh exact catalog rows needed by the surviving-lead follow-up.

This bounded query records the Gaia DR3 astrometry for the TOI-3500 target and
close neighbour and the SIMBAD identity/reference graph for TOI-7610.  It does
not infer that a SIMBAD object type is correct merely because the label exists.
"""

from __future__ import annotations

import json
import ssl
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import certifi


OUT = Path(__file__).with_name("catalog_followup.json")
GAIA_ENDPOINT = "https://gea.esac.esa.int/tap-server/tap/sync"
SIMBAD_ENDPOINT = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"


def tap_json(endpoint: str, query: str) -> dict:
    body = urlencode(
        {
            "REQUEST": "doQuery",
            "LANG": "ADQL",
            "FORMAT": "json",
            "QUERY": query,
        }
    ).encode("utf-8")
    request = Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    tls_context = ssl.create_default_context(cafile=certifi.where())
    try:
        with urlopen(request, timeout=120, context=tls_context) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"TAP HTTP {exc.code}: {detail[:4000]}") from exc


def main() -> None:
    gaia_query = """
        SELECT source_id, ra, dec, ref_epoch, pmra, pmdec, parallax,
               phot_g_mean_mag, ruwe
        FROM gaiadr3.gaia_source
        WHERE source_id IN (
            3471495415361216512,
            3471495419656596352,
            3071787586789910144
        )
        ORDER BY source_id
    """
    simbad_identity_query = """
        SELECT b.oid, b.main_id, b.otype, b.ra, b.dec, i.id
        FROM basic AS b
        JOIN ident AS i ON b.oid = i.oidref
        WHERE b.oid IN (
            SELECT oidref FROM ident
            WHERE id = 'Gaia DR3 3071787586789910144'
        )
    """
    simbad_reference_query = """
        SELECT r.bibcode, r.title, r.journal
        FROM basic AS b
        JOIN has_ref AS h ON b.oid = h.oidref
        JOIN ref AS r ON h.oidbibref = r.oidbib
        WHERE b.oid IN (
            SELECT oidref FROM ident
            WHERE id = 'Gaia DR3 3071787586789910144'
        )
    """
    result = {
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "queries": {
            "gaia_dr3": {
                "endpoint": GAIA_ENDPOINT,
                "query": gaia_query.strip(),
                "result": tap_json(GAIA_ENDPOINT, gaia_query),
            },
            "simbad_identity": {
                "endpoint": SIMBAD_ENDPOINT,
                "query": simbad_identity_query.strip(),
                "result": tap_json(SIMBAD_ENDPOINT, simbad_identity_query),
            },
        },
    }
    result["queries"]["gaia_nss"] = {}
    for table in (
        "nss_two_body_orbit",
        "nss_non_linear_spectro",
        "nss_acceleration_astro",
        "nss_vim_fl",
    ):
        query = (
            f"SELECT * FROM gaiadr3.{table} "
            "WHERE source_id = 3071787586789910144"
        )
        try:
            result["queries"]["gaia_nss"][table] = {
                "endpoint": GAIA_ENDPOINT,
                "query": query,
                "result": tap_json(GAIA_ENDPOINT, query),
            }
        except Exception as exc:
            result["queries"]["gaia_nss"][table] = {
                "endpoint": GAIA_ENDPOINT,
                "query": query,
                "error": f"{type(exc).__name__}: {exc}",
            }
    try:
        result["queries"]["simbad_references"] = {
            "endpoint": SIMBAD_ENDPOINT,
            "query": simbad_reference_query.strip(),
            "result": tap_json(SIMBAD_ENDPOINT, simbad_reference_query),
        }
    except Exception as exc:  # keep the successful exact identity query
        result["queries"]["simbad_references"] = {
            "endpoint": SIMBAD_ENDPOINT,
            "query": simbad_reference_query.strip(),
            "error": f"{type(exc).__name__}: {exc}",
        }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
