"""Spectroscopy archives beyond ESO ObsCore: Keck Observatory Archive (HIRES) and Gaia exact-source rows.

Metadata visibility is not public-data eligibility; a timeout or HTTP 401 is an access limit, not absence.
"""

from __future__ import annotations

from typing import Any

from .base import AdapterUnavailable, ArchiveAdapter, Target, as_products, register

KOA_TAP = "https://koa.ipac.caltech.edu/TAP/sync"
KOA_GET = "https://koa.ipac.caltech.edu/cgi-bin/getKOA/nph-getKOA"          # raw product; ignores Range (HTTP 200)
KOA_CALIB = "https://koa.ipac.caltech.edu/cgi-bin/KoaAPI/nph-getCaliblist"  # association list, not suitability


@register
class KoaAdapter(ArchiveAdapter):
    """Keck Observatory Archive HIRES metadata via anonymous TAP (box query on the target position)."""

    name = "koa"
    description = "Keck Observatory Archive HIRES observation metadata (anonymous TAP)"
    formats = ("table",)
    capabilities = ("spectroscopy", "context")
    verified = "[V]"
    row_limited = True

    def discover(self, target: Target, *, limit: int = 50, box_arcsec: float = 30.0, **opts: Any):
        d = box_arcsec / 3600
        adql = (f"SELECT TOP {int(limit)} koaid, object, targname, ra, dec, date_obs, exptime, filehand "
                f"FROM koa_hires WHERE ra BETWEEN {target.ra_deg - d:.6f} AND {target.ra_deg + d:.6f} "
                f"AND dec BETWEEN {target.dec_deg - d:.6f} AND {target.dec_deg + d:.6f}")
        try:
            rows = self.tap_csv(KOA_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"KOA TAP failed: {type(exc).__name__}: {exc}") from exc
        out = [{"product_id": "koa_hires_%s_r%gas.csv" % (target.name.replace(" ", "_"), box_arcsec), "format": "table",
                "kind": "table", "url": None, "inline": True, "rows": rows,
                "description": f"KOA HIRES metadata box +/-{box_arcsec:g}\" ({len(rows)} rows); "
                               "identity, calibration and download untested"}]
        return as_products(out, self.name, "table")


GAIA_EXACT_COLS = ("source_id, ra, dec, pmra, pmdec, parallax, ref_epoch, phot_g_mean_mag, ruwe, "
                   "radial_velocity, radial_velocity_error, rv_nb_transits, rv_visibility_periods_used, "
                   "rv_amplitude_robust, rv_expected_sig_to_noise, non_single_star")


def gaia_exact_source(adapter, source_id: int) -> dict:
    """RUWE/RV-quality row plus the NSS two-body orbit count for one Gaia DR3 source.

    Zero NSS rows is a release-bounded null, not 'not binary'. Null RV columns mean no RVS solution.
    """
    src = adapter.tap_csv("https://gea.esac.esa.int/tap-server/tap/sync",
                          f"SELECT {GAIA_EXACT_COLS} FROM gaiadr3.gaia_source WHERE source_id = {int(source_id)}")
    nss = adapter.tap_csv("https://gea.esac.esa.int/tap-server/tap/sync",
                          f"SELECT source_id, nss_solution_type, period FROM gaiadr3.nss_two_body_orbit "
                          f"WHERE source_id = {int(source_id)}")
    return {"source_id": int(source_id), "row": src[0] if src else None, "nss_two_body_rows": len(nss),
            "note": "release-bounded; zero NSS rows does not establish a single star"}
