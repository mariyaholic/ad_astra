"""Astronomy archive adapters (DATA_SOURCES.md section 1).

Each adapter implements ``discover`` (product list for a target) and inherits
``fetch``/``read`` from :class:`cygnus.multi.archives.base.ArchiveAdapter`.
Endpoints and quirks follow the verified notes in ``DATA_SOURCES.md``.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

from .base import AdapterError, AdapterUnavailable, ArchiveAdapter, ProductRef, SourceCheck, Target, as_products, register

# --------------------------------------------------------------------------- helpers


def _sep_arcsec(ra1, dec1, ra2, dec2) -> float:
    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(r1 - r2)
    return math.degrees(math.acos(max(-1.0, min(1.0, c)))) * 3600


# --------------------------------------------------------------------------- MAST
MAST_API = "https://mast.stsci.edu/api/v0/invoke"
MAST_DL = "https://mast.stsci.edu/api/v0.1/Download/file"
_TESS_NO_AUTH = "https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:TESS/product/"


def _nearest(frame: str, target) -> str:
    """ADQL distance from the target, selected as a column so cones come back nearest-first in a fixed
    order: the same query then gives the same file and checksum, and a TOP cap keeps the nearest rows
    (TAP services return rows in no fixed order otherwise). Services reject the function inside ORDER BY."""
    return f"DISTANCE(POINT('{frame}', ra, dec), POINT('{frame}', {target.ra_deg:.7f}, {target.dec_deg:.7f}))"


@register
class MastAdapter(ArchiveAdapter):
    """MAST (STScI): HST, JWST, TESS, Kepler/K2, Pan-STARRS, GALEX, HLSPs.

    Discovery uses the portal Mashup API directly (no astroquery), so it works
    in a bare environment; the TIC id is the ``target_name`` for TESS SPOC.
    """

    name = "mast"
    description = "STScI MAST: TESS/Kepler/K2 light curves, HST/JWST, Pan-STARRS, GALEX, HLSPs"
    formats = ("spoc_lc", "kepler_lc", "tess_lc", "fits_table", "fits_image")
    verified = "[V]"

    def source_checks(self, target, ref, path, product=None):
        """Default checks plus the SPOC quality-flag census for TESS/Kepler light curves."""
        checks = super().source_checks(target, ref, path, product)
        if (product or {}).get("kind") == "lightcurve":
            try:
                from ..readers import read_lightcurve

                lc = read_lightcurve(path, fmt=ref.format)
                q = lc.quality
                bad = int((q != 0).sum()) if q is not None and q.size else 0
                # flagged cadences are excluded from the screen by design; only a mostly-flagged series is a concern
                frac = bad / lc.time.size if lc.time.size else 1.0
                checks.append(SourceCheck("MAST quality flags", "passed" if frac <= 0.5 else "inconclusive",
                                          f"{bad} of {lc.time.size} cadence(s) ({frac:.0%}) with QUALITY != 0, "
                                          "excluded from the screen"))
            except Exception as exc:  # noqa: BLE001
                checks.append(SourceCheck("MAST quality flags", "failed", f"{type(exc).__name__}: {str(exc)[:160]}"))
        return checks

    def _mashup(self, service: str, params: dict, *, pagesize: int = 200) -> dict:
        import json as _json

        payload = {"service": service, "params": params, "format": "json", "pagesize": pagesize}
        r = self.http_post(MAST_API, data={"request": _json.dumps(payload)}, timeout=120.0)
        r.raise_for_status()
        body = r.json()
        if body.get("status") not in (None, "COMPLETE"):
            raise AdapterUnavailable(f"MAST {service}: status {body.get('status')} {body.get('msg')}")
        return body

    def discover(self, target: Target, *, limit: int = 5, collection: str = "TESS",
                 provenance: str = "SPOC", subgroup: str = "LC", **opts) -> list[ProductRef]:
        # TESS SPOC timeseries searches need the bare TIC number as target_name.
        key = str(target.tic) if (collection == "TESS" and target.tic) else target.name
        # Mast.Caom.Filtered takes column filters; Mast.Caom.Cone takes only ra/dec/radius and
        # rejects these parameters ("Missing Required Parameter: RA"), so it is not used here.
        filters = {"target_name": key, "obs_collection": collection, "dataproduct_type": "timeseries"}
        if provenance:
            filters["provenance_name"] = provenance
        params = {"columns": "*", "filters": [{"paramName": k, "values": [v]} for k, v in filters.items()]}
        try:
            obs = self._mashup("Mast.Caom.Filtered", params)
        except AdapterUnavailable:
            raise
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"MAST query failed: {type(exc).__name__}: {exc}") from exc
        data = obs.get("data", [])
        if not data:
            return []
        obsids = [d.get("obsid") for d in data if d.get("obsid")]
        try:
            prods = self._mashup("Mast.Caom.Products", {"obsid": ",".join(str(o) for o in obsids)}, pagesize=1000)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"MAST product list failed: {exc}") from exc
        rows, seen = [], set()
        for p in prods.get("data", []):
            fn = str(p.get("productFilename", ""))
            sub = str(p.get("productSubGroupDescription", ""))
            if not fn or fn in seen:
                continue
            if subgroup and sub != subgroup:
                continue
            if fn.endswith("fast") or "-fast" in fn:
                continue
            seen.add(fn)
            uri = p.get("dataURI") or f"mast:{collection}/product/{fn}"
            rows.append({"product_id": fn, "url": f"{MAST_DL}?uri={uri}",
                         "format": self._fmt_for(fn, collection),
                         "description": f"MAST {collection} {sub} {fn}",
                         "obsid": p.get("obsID"), "sector": _sector_of(fn), "tic": target.tic})
        return as_products(rows[:limit], self.name, "fits_table")

    @staticmethod
    def _fmt_for(fn: str, collection: str) -> str:
        if collection == "TESS":
            return "spoc_lc" if fn.endswith(("-s_lc.fits", "-lc.fits")) else "fits_table"
        if collection in ("Kepler", "K2"):
            return "kepler_lc"
        if fn.endswith((".fits", ".fits.gz")):
            return "fits_table"
        return "fits_image"


def _sector_of(fn: str) -> int | None:
    if "-s0" in fn:
        try:
            return int(fn.split("-s")[1][:4])
        except (IndexError, ValueError):
            return None
    return None


# --------------------------------------------------------------------------- Gaia
GAIA_TAP = "https://gea.esac.esa.int/tap-server/tap"
_GAIA_COLS = ("source_id, ra, dec, parallax, pmra, pmdec, phot_g_mean_mag, bp_rp, ruwe, "
              "radial_velocity, non_single_star")


@register
class GaiaAdapter(ArchiveAdapter):
    """Gaia DR3 (ESA): astrometry, photometry, RV, NSS. CSV-formatted TAP (byte-safe)."""
    row_limited = True   # ``limit`` is the ADQL TOP row cap, not a product count

    name = "gaia"
    description = "Gaia DR3 astrometry, photometry, RV and NSS tables (cone search + source rows)"
    formats = ("csv", "table")
    capabilities = ("astrometry", "catalog")
    verified = "[V]"

    def source_checks(self, target, ref, path, product=None):
        """Gaia-specific astrometric fidelity: RUWE, non-single-star flags, parallax."""
        from ..source_checks import gaia_checks

        return gaia_checks(path, target)

    def _tap(self, adql: str) -> list[dict]:
        return self.tap_csv(f"{GAIA_TAP}/sync", adql)

    def discover(self, target: Target, *, limit: int = 200, radius_arcsec: float = 30.0, **opts) -> list[ProductRef]:
        r = radius_arcsec / 3600
        adql = (f"SELECT TOP {int(limit)} {_GAIA_COLS}, {_nearest('ICRS', target)} AS sep_deg FROM gaiadr3.gaia_source "
                f"WHERE 1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f})) "
                f"ORDER BY sep_deg, source_id")
        try:
            rows = self._tap(adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"Gaia TAP failed: {type(exc).__name__}: {exc}") from exc
        # Persist the cone as one CSV product so the runner has a real file to checksum.
        out = [{"product_id": f"gaia_cone_{target.name.replace(' ', '_')}_r{radius_arcsec:g}as.csv",
                "format": "csv", "url": None, "description": f"Gaia DR3 cone r={radius_arcsec:g}\" ({len(rows)} rows)",
                "rows": rows, "inline": True}]
        return as_products(out, self.name, "csv")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 120.0) -> Path:
        if ref.extra.get("inline"):
            import json as _json

            rows = ref.extra.get("rows", [])
            columns = list(rows[0].keys()) if rows else []
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=columns)
                w.writeheader()
                w.writerows(rows)
            return dest
        return super().fetch(ref, dest, timeout_s=timeout_s)


# --------------------------------------------------------------------------- SkyView
SKYVIEW_CGI = "https://skyview.gsfc.nasa.gov/current/cgi/runquery.pl"


@register
class SkyViewAdapter(ArchiveAdapter):
    """SkyView (NASA GSFC): multi-survey image cutouts (DSS, 2MASS, SDSS, GALEX, WISE...).

    WISE requests returned 404 on 2026-09-23; per-survey terms apply.
    """

    name = "skyview"
    description = "SkyView image cutouts: DSS, 2MASS, SDSS, GALEX, WISE, UKIDSS, FIRST, AKARI"
    formats = ("fits_image",)
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 5, surveys: list[str] | None = None,
                 size_deg: float = 0.5, pixels: int = 500, **opts) -> list[ProductRef]:
        surveys = surveys or ["DSS2 Blue"]
        rows = []
        for sv in surveys[:limit]:
            pid = f"skyview_{target.name.replace(' ', '_')}_{sv.replace(' ', '')}_0.fits"
            rows.append({"product_id": pid, "url": None, "format": "fits_image",
                         "description": f"SkyView {sv} cutout {size_deg} deg",
                         "survey": sv, "size_deg": size_deg, "pixels": pixels})
        return as_products(rows, self.name, "fits_image")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 180.0) -> Path:
        params = {"Survey": ref.extra["survey"], "Position": ref.extra.get("position"),
                  "Size": ref.extra.get("size_deg", 0.5), "Pixels": ref.extra.get("pixels", 500),
                  "Return": "FITS", "coordinates": "J2000", "projection": "Tan", "scaling": "Linear"}
        r = self.http_get(SKYVIEW_CGI, params=params, timeout=timeout_s)
        r.raise_for_status()
        if r.content[:6] not in (b"SIMPLE", b"\x00\x00\x00\x00") and not r.content.startswith(b"SIMPLE"):
            raise AdapterError(f"SkyView returned non-FITS content for {ref.product_id}: {r.content[:80]!r}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        return dest


# --------------------------------------------------------------------------- CDS (VizieR + SIMBAD)
VIZIER_TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
SIMBAD_TAP = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"


@register
class VizierAdapter(ArchiveAdapter):
    """CDS VizieR: tens of thousands of catalogues via anonymous TAP. Default table VSX."""
    row_limited = True   # ``limit`` is the ADQL TOP row cap, not a product count

    name = "vizier"
    description = "CDS VizieR TAP catalogue cone searches (default table: B/vsx/vsx variables)"
    formats = ("csv", "table")
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 500, radius_arcsec: float = 30.0,
                 table: str = "B/vsx/vsx", **opts) -> list[ProductRef]:
        r = radius_arcsec / 3600
        racol, deccol = ("RAJ2000", "DEJ2000") if table == "B/vsx/vsx" else ("RAJ2000", "DEJ2000")
        adql = (f'SELECT TOP {int(limit)} * FROM "{table}" WHERE '
                f'1=CONTAINS(POINT(\'ICRS\', {racol}, {deccol}), CIRCLE(\'ICRS\', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f}))')
        try:
            rows = self.tap_csv(VIZIER_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"VizieR TAP failed: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"vizier_{table.replace('/', '_')}_{target.name.replace(' ', '_')}.csv",
                             "format": "csv", "description": f"VizieR {table} cone r={radius_arcsec:g}\" ({len(rows)} rows)",
                             "rows": rows, "inline": True}], self.name, "csv")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 120.0) -> Path:
        if ref.extra.get("inline"):
            rows = ref.extra.get("rows", [])
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else [])
                w.writeheader()
                w.writerows(rows)
            return dest
        return super().fetch(ref, dest, timeout_s=timeout_s)


@register
class SimbadAdapter(ArchiveAdapter):
    """CDS SIMBAD: object cross-IDs and types via anonymous TAP."""
    row_limited = True   # ``limit`` is the ADQL TOP row cap, not a product count

    name = "simbad"
    description = "CDS SIMBAD TAP object identifications around a position"
    formats = ("csv", "table")
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 200, radius_arcsec: float = 30.0, **opts) -> list[ProductRef]:
        r = radius_arcsec / 3600
        adql = (f"SELECT TOP {int(limit)} main_id, otype, ra, dec, pmra, pmdec, {_nearest('ICRS', target)} AS sep_deg FROM basic WHERE "
                f"1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f})) "
                f"ORDER BY sep_deg, main_id")
        try:
            rows = self.tap_csv(SIMBAD_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"SIMBAD TAP failed: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"simbad_{target.name.replace(' ', '_')}.csv", "format": "csv",
                             "description": f"SIMBAD cone r={radius_arcsec:g}\" ({len(rows)} rows)",
                             "rows": rows, "inline": True}], self.name, "csv")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 120.0) -> Path:
        return VizierAdapter.fetch(self, ref, dest, timeout_s=timeout_s)


# --------------------------------------------------------------------------- NED
NED_TAP = "https://ned.ipac.caltech.edu/tap/sync"   # lowercase path; /TAP/sync is 404 (checked 2026-09-25)


@register
class NedAdapter(ArchiveAdapter):
    """NED (NASA/IPAC): extragalactic identifications and references via TAP."""
    row_limited = True   # ``limit`` is the ADQL TOP row cap, not a product count

    name = "ned"
    description = "NASA/IPAC NED extragalactic object search (cone via TAP)"
    formats = ("csv", "table")
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 200, radius_arcsec: float = 60.0, **opts) -> list[ProductRef]:
        r = radius_arcsec / 3600
        adql = (f"SELECT TOP {int(limit)} prefname, ra, dec, prefphytype, {_nearest('ICRS', target)} AS sep_deg FROM objdir WHERE "
                f"1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f})) "
                f"ORDER BY sep_deg, prefname")
        try:
            rows = self.tap_csv(NED_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"NED TAP failed: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"ned_{target.name.replace(' ', '_')}.csv", "format": "csv",
                             "description": f"NED cone r={radius_arcsec:g}\" ({len(rows)} rows)",
                             "rows": rows, "inline": True}], self.name, "csv")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 120.0) -> Path:
        return VizierAdapter.fetch(self, ref, dest, timeout_s=timeout_s)


# --------------------------------------------------------------------------- ESO
ESO_OBS_TAP = "https://archive.eso.org/tap_obs/sync"


@register
class EsoAdapter(ArchiveAdapter):
    """ESO Science Archive: VLT/ALMA etc. ObsCore rows; DATALINK resolves the actual FITS."""

    name = "eso"
    description = "ESO Science Archive ObsCore products (VLT/ALMA/large programs)"
    formats = ("fits_table", "fits_image", "table")
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 20, radius_arcsec: float = 30.0, **opts) -> list[ProductRef]:
        r = radius_arcsec / 3600
        adql = (f"SELECT TOP {int(limit)} dp_id, obs_collection, instrument_name, access_url, access_format, "
                f"dataproduct_type, s_ra, s_dec FROM ivoa.ObsCore WHERE "
                f"1=CONTAINS(POINT('ICRS', s_ra, s_dec), CIRCLE('ICRS', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f}))")
        try:
            rows = self.tap_csv(ESO_OBS_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"ESO TAP failed: {type(exc).__name__}: {exc}") from exc
        out = [{"product_id": str(x.get("dp_id") or f"eso_{i}"), "url": x.get("access_url"),
                "format": "fits_image" if x.get("dataproduct_type") == "image" else "fits_table",
                "description": f"ESO {x.get('obs_collection')} {x.get('instrument_name')}",
                "obs_collection": x.get("obs_collection"), "instrument": x.get("instrument_name")} for i, x in enumerate(rows)]
        return as_products(out[:limit], self.name, "fits_table")


# --------------------------------------------------------------------------- IRSA
IRSA_TAP = "https://irsa.ipac.caltech.edu/TAP/sync"
IRSA_ZTF = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"


@register
class IrsaAdapter(ArchiveAdapter):
    """IRSA (NASA/IPAC): AllWISE/2MASS catalogues via TAP and ZTF light curves via CGI.

    ZTF CGI accepts only ``POS=CIRCLE ra dec radius`` and ``FORMAT`` (MERGE/BAD_DATA 400).
    """
    row_limited = True   # ``limit`` is the ADQL TOP row cap, not a product count

    name = "irsa"
    description = "IRSA: AllWISE/2MASS catalogues (TAP) and ZTF light curves (CGI)"
    formats = ("csv", "table", "ztf_lc")
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 5, radius_arcsec: float = 10.0,
                 mode: str = "wise", **opts) -> list[ProductRef]:
        if mode == "ztf":
            return as_products([{"product_id": f"ztf_{target.name.replace(' ', '_')}.vot",
                                 "url": None, "format": "ztf_lc",
                                 "description": f"ZTF light curves within {radius_arcsec:g}\"",
                                 "ra": target.ra_deg, "dec": target.dec_deg, "radius": radius_arcsec}],
                               self.name, "ztf_lc")
        r = radius_arcsec / 3600
        # IRSA's DISTANCE returns arcsec (verified 2026-09-26 against NED's degrees for the same WISE source)
        adql = (f"SELECT TOP {int(limit)} designation, ra, dec, w1mpro, w2mpro, w3mpro, w4mpro, {_nearest('J2000', target)} AS sep_arcsec "
                f"FROM allwise_p3as_psd "
                f"WHERE 1=CONTAINS(POINT('J2000', ra, dec), CIRCLE('J2000', {target.ra_deg:.7f}, {target.dec_deg:.7f}, {r:.7f})) "
                f"ORDER BY sep_arcsec, designation")
        try:
            rows = self.tap_csv(IRSA_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"IRSA TAP failed: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"irsa_allwise_{target.name.replace(' ', '_')}.csv", "format": "csv",
                             "description": f"AllWISE cone r={radius_arcsec:g}\" ({len(rows)} rows)",
                             "rows": rows, "inline": True}], self.name, "csv")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 120.0) -> Path:
        if ref.format == "ztf_lc":
            params = {"POS": f"CIRCLE {ref.extra['ra']} {ref.extra['dec']} {ref.extra['radius'] / 3600}"}
            r = self.http_get(IRSA_ZTF, params=params, timeout=timeout_s)
            r.raise_for_status()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(r.content)
            return dest
        return VizierAdapter.fetch(self, ref, dest, timeout_s=timeout_s)


# --------------------------------------------------------------------------- Legacy Survey
LS_VIEWER = "https://www.legacysurvey.org/viewer"
LS_PORTAL = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey"


@register
class LegacySurveyAdapter(ArchiveAdapter):
    """Legacy Survey DR9/DR10 optical + unWISE IR cutouts (CC BY 4.0).

    Required credit: "Legacy Surveys / D. Lang (Perimeter Institute)".
    """

    name = "legacysurvey"
    description = "Legacy Survey DR9/DR10 optical + unWISE coadds (CC BY 4.0, credit D. Lang)"
    formats = ("fits_image",)
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 4, size_arcsec: float = 60.0,
                 layer: str = "ls-dr10", **opts) -> list[ProductRef]:
        rows = [{"product_id": f"legacysurvey_{layer}_{target.name.replace(' ', '_')}.fits",
                 "url": None, "format": "fits_image",
                 "description": f"Legacy Survey {layer} cutout {size_arcsec}\"",
                 "ra": target.ra_deg, "dec": target.dec_deg, "size_arcsec": size_arcsec, "layer": layer}]
        return as_products(rows, self.name, "fits_image")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 180.0) -> Path:
        params = {"ra": ref.extra["ra"], "dec": ref.extra["dec"], "size": ref.extra["size_arcsec"],
                  "layer": ref.extra["layer"], "fits": "1"}
        r = self.http_get(f"{LS_VIEWER}/cutout.fits", params=params, timeout=timeout_s)
        r.raise_for_status()
        if not r.content.startswith(b"SIMPLE"):
            raise AdapterError(f"Legacy Survey returned non-FITS content: {r.content[:80]!r}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        return dest


# --------------------------------------------------------------------------- NASA Exoplanet Archive
EXO_TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"


@register
class ExoArchiveAdapter(ArchiveAdapter):
    """NASA Exoplanet Archive: TOI table and confirmed-planet composite parameters."""
    row_limited = True   # ``limit`` is the ADQL TOP row cap, not a product count

    name = "exoarchive"
    description = "NASA Exoplanet Archive TAP: TOI table, pscomppars confirmed planets"
    formats = ("csv", "table")
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 10, mode: str = "toi", **opts) -> list[ProductRef]:
        if mode == "toi" and target.tic:
            adql = (f"SELECT toi, tid, tfopwg_disp, ra, dec, st_tmag, pl_trandep, pl_trandurh, pl_tranmid, pl_orbper "
                    f"FROM toi WHERE tid = {int(target.tic)}")
        elif mode == "planet":
            safe = target.name.lower().replace("'", "")
            adql = (f"SELECT pl_name, hostname, tic_id, ra, dec, pl_orbper, pl_tranmid, pl_trandep, pl_trandur, sy_tmag "
                    f"FROM pscomppars WHERE lower(pl_name) = '{safe}'")
        else:
            r = 30.0 / 3600
            dra = r / max(0.01, math.cos(math.radians(target.dec_deg)))
            adql = (f"SELECT top {int(limit)} toi, tid, tfopwg_disp, ra, dec FROM toi WHERE "
                    f"ra BETWEEN {target.ra_deg - dra:.7f} AND {target.ra_deg + dra:.7f} AND "
                    f"dec BETWEEN {target.dec_deg - r:.7f} AND {target.dec_deg + r:.7f}")
        try:
            rows = self.tap_csv(EXO_TAP, adql)
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"Exoplanet Archive TAP failed: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": f"exoarchive_{mode}_{target.name.replace(' ', '_')}.csv", "format": "csv",
                             "description": f"Exoplanet Archive {mode} rows ({len(rows)})",
                             "rows": rows, "inline": True}], self.name, "csv")

    def fetch(self, ref: ProductRef, dest: Path, *, timeout_s: float = 120.0) -> Path:
        return VizierAdapter.fetch(self, ref, dest, timeout_s=timeout_s)