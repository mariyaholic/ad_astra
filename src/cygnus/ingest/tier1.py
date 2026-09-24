"""Tier-1 baseline data pack: provenance-logged retrievals from the eight
anonymous-access deep-sky archives catalogued in ``DATA_SOURCES.md`` §1.

Services (run order): MAST, Gaia, SkyView, CDS (VizieR TAP + SIMBAD), NED,
ESO, IRSA, Legacy Survey.

Design rules (AGENTS.md):

* every endpoint, query text and fetch is recorded verbatim in manifest +
  ledger rows — nothing is invented;
* coordinates are resolved at runtime through the CDS Sesame name resolver;
  unresolved names are logged as failures, never guessed;
* byte totals are bounded per service (budgets); overflows are *recorded*
  as ``excluded`` rows, not silently truncated;
* failures produce manifest rows (state ``failed`` with error text), so an
  incomplete service stays visible in the pack;
* heavy imports (astroquery/pyvo/astropy) are inside collector bodies.

CLI::

    python -m cygnus.ingest.tier1 --services mast,gaia
    python -m cygnus.ingest.tier1 --services all
    python -m cygnus.ingest.tier1 --pp        # preview budgets/target lists
"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import urllib.parse
from pathlib import Path
from typing import Any

from .pack import PackBuilder, ledger_products_csv, now_iso
from .netio import session as cyg_session
from ..config import ledger_path
from ..ledger import Ledger

# --------------------------------------------------------------------------- pack configuration

PACK_DIRS = {
    "mast": "01_mast",
    "gaia": "02_gaia",
    "skyview": "03_skyview",
    "cds": "04_cds",
    "ned": "05_ned",
    "eso": "06_eso",
    "irsa": "07_irsa",
    "legacysurvey": "08_legacy_survey",
}

SERVICE_ORDER = ["mast", "gaia", "skyview", "cds", "ned", "eso", "irsa", "legacysurvey"]

# Ledger archive keys (stable names used across runs).
ARCHIVE_KEY = {
    "mast": "MAST",
    "gaia": "Gaia",
    "skyview": "SkyView",
    "cds": "CDS",
    "ned": "NED",
    "eso": "ESO",
    "irsa": "IRSA",
    "legacysurvey": "LegacySurvey",
}

# Per-service caps in GiB (sum 9.65 GB) within the user's 5–10 GB request.
# Budgets are caps, not quotas; actual totals are reported per run.
DEFAULT_BUDGETS_GB = {
    "mast": 3.5,
    "gaia": 2.2,
    "skyview": 0.6,
    "cds": 0.6,
    "ned": 0.15,
    "eso": 0.5,
    "irsa": 1.2,
    "legacysurvey": 0.9,
}

# Test fields: dense, well-characterized regions spanning both hemispheres
# (Pleiades cluster; Praesepe cluster; Omega Centauri globular cluster).
FIELD_NAMES = ["Pleiades", "M44", "NGC 5139"]

# Benchmark target names (TESS hosts + famous variables + cluster centers).
# Only names are declared here; positions/sizes are always queried live.
TESS_TARGET_NAMES = [
    "Pi Mensae",
    "HD 209458",
    "WASP-12",
    "TRAPPIST-1",
    "GJ 1214",
    "51 Peg",
    "KIC 8462852",
    "T Tau",
    "AU Mic",
    "WASP-126",
    "DS Tuc",
    "Iota Horologii",
]

BENCH_OBJECT_NAMES = [
    *TESS_TARGET_NAMES,
    "NGC 6819",
    "Pleiades",
    "M44",
    "NGC 5139",
    "Proxima Centauri",
    "T CrB",
    "SS Cyg",
    "Algol",
    "Cygnus X-1",
]

MAST_API_DL = "https://mast.stsci.edu/api/v0.1/Download/file"
TESSCUT_EP = "astroquery.mast Tesscut (REST https://mast.stsci.edu/tesscut/api/v0.1/)"
_GAIA_EP = "Gaia DR3 TAP+ via astroquery.gaia (server https://gea.esac.esa.int/tap-server/tap)"
_VIZIER_TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap"
_SIMBAD_EP = "SIMBAD TAP via astroquery.simbad (https://simbad.cds.unistra.fr/simbad/sim-tap)"
_IRSA_TAP = "https://irsa.ipac.caltech.edu/TAP"
_ZTF_NPH = "https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"
_ESO_TAP = "https://archive.eso.org/tap_obs"
_LS_BASE = "https://www.legacysurvey.org"

_name_cache: dict[str, dict[str, Any]] = {}


# --------------------------------------------------------------------------- name resolution


def resolve_name(name: str) -> tuple[float, float] | None:
    """Resolve a name via CDS Sesame (astropy ``SkyCoord.from_name``).

    Every attempt (success or failure) is cached with a timestamp and dumped
    into the pack for provenance. No coordinates are ever fabricated here.
    """
    if name in _name_cache:
        hit = _name_cache[name]
        return (hit["ra_deg"], hit["dec_deg"]) if hit.get("ok") else None
    entry: dict[str, Any] = {
        "name": name,
        "resolver": "CDS Sesame via astropy SkyCoord.from_name",
        "resolved_utc": now_iso(),
    }
    try:
        from astropy.coordinates import SkyCoord

        c = SkyCoord.from_name(name)
        entry.update(
            ok=True,
            ra_deg=float(c.ra.deg),
            dec_deg=float(c.dec.deg),
            frame="ICRS (resolver epoch default J2000)",
        )
        _name_cache[name] = entry
        return float(c.ra.deg), float(c.dec.deg)
    except Exception as exc:  # noqa: BLE001
        entry.update(ok=False, error=f"{type(exc).__name__}: {exc}")
        _name_cache[name] = entry
        return None


def write_name_cache(pack_root: Path) -> Path:
    pack_root.mkdir(parents=True, exist_ok=True)
    p = pack_root / "NAME_RESOLUTIONS.json"
    p.write_text(json.dumps(_name_cache, indent=1, ensure_ascii=True), encoding="utf-8")
    return p


# --------------------------------------------------------------------------- helpers


def slug(text: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in text).strip("_")[:80]


def table_to_csv(table: Any, path: Path) -> Path:
    """Write an astropy Table to CSV; zero rows become a recorded empty file.

    VOTable-derived tables may carry masked columns; on any writer failure the
    table is filled (masks -> NaN/empty) and rewritten with the slow writer so
    a real CSV still lands instead of a lost file.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    if table is None or len(table) == 0:
        path.write_text("query returned zero rows\n", encoding="utf-8")
        return path
    try:
        table.write(path, format="ascii.csv", overwrite=True)
        return path
    except Exception:  # noqa: BLE001 - masked/awkward columns: fill + python writer
        from astropy.io import ascii as ascii_io

        try:
            tab2 = table.filled() if hasattr(table, "filled") else table
        except Exception:  # noqa: BLE001
            tab2 = table
        ascii_io.write(tab2, str(path), format="csv", overwrite=True, fast_writer=False)
        return path


def stack_versions() -> dict[str, str]:
    out: dict[str, str] = {}
    for pkg in ("cygnus", "astropy", "astroquery", "pyvo", "numpy", "scipy", "requests"):
        try:
            out[pkg] = importlib.metadata.version(pkg)
        except Exception:
            out[pkg] = "(absent)"
    return out


def run_service(builder: PackBuilder, key: str, fn) -> None:
    import traceback

    builder.log(key, f">>> service start (pack_dir={PACK_DIRS[key]})")
    try:
        fn(builder)
    except Exception as exc:  # noqa: BLE001 - record the service-level failure itself
        tb = traceback.format_exc(limit=10)
        builder.log(key, f"SERVICE-LEVEL FAILURE: {type(exc).__name__}: {exc}\n{tb}")
        builder._rows.setdefault(key, []).append(  # noqa: SLF001 - same package
            builder._row(  # noqa: SLF001
                key,
                f"SERVICE_ERROR_{key.upper()}",
                dest_rel="",
                state="failed",
                url="",
                endpoint="service collector",
                query="",
                license_="",
                extra={"collector": getattr(fn, "__name__", "?"), "traceback": tb[:1900]},
                note=f"{type(exc).__name__}: {str(exc)[:600]}",
            )
        )
    finally:
        builder.log(key, f"<<< service end; bytes_used={builder.bytes_used(key)}")


# --------------------------------------------------------------------------- MAST


def collect_mast(builder: PackBuilder) -> None:
    from astroquery.mast import Observations, Tesscut

    svc = "mast"
    lic = "public archive data (NASA; see mast.stsci.edu for terms)"

    def obs_extra(row: Any) -> dict[str, Any]:
        ex: dict[str, Any] = {}
        for col in ("obs_id", "target_name", "obs_collection", "provenance_name",
                    "proposal_id", "instrument_name", "filters", "t_exptime",
                    "t_min", "t_max", "project"):
            try:
                if col in row.colnames:
                    v = row[col]
                    ex[col] = v.item() if hasattr(v, "item") else v
            except Exception:
                pass
        return ex

    def fetch_product_row(svc_obs: Any, prod: Any, dest_dir: str, tag: str,
                          query_record: dict[str, Any]) -> None:
        uri = str(prod["dataURI"])
        fname = str(prod["productFilename"]) or uri.rsplit("/", 1)[-1]
        url = f"{MAST_API_DL}?uri={urllib.parse.quote(uri)}"
        size_hint: int | None = None
        try:
            if "size" in prod.colnames and prod["size"] is not None:
                size_hint = int(prod["size"])
        except Exception:
            size_hint = None
        ex = obs_extra(svc_obs)
        ex.update({"productFilename": fname, "dataURI": uri, "tag": tag})
        builder.try_fetch(
            svc,
            fname,
            url=url,
            dest_rel=f"{dest_dir}/{fname}",
            endpoint=f"MAST download API {MAST_API_DL} (dataURI: {uri})",
            query=json.dumps(query_record, sort_keys=True)[:2000],
            license_=lic,
            size_hint=size_hint,
            extra=ex,
        )

    # -- TESS SPOC 2-min light curves ---------------------------------------------------
    # Live probe 2026-09-23: exact target_name probes ("Pi Mensae") returned zero
    # rows — CAOM target_name is the TIC id (e.g. '261136679' for Pi Mensae) —
    # so the search is cone-based on the Sesame-resolved position, selecting the
    # nearest-target group via the query's 'distance' column.
    import re

    import astropy.units as u
    from astropy.coordinates import SkyCoord

    def group_nearest_by_target(obs: Any) -> tuple[str | None, list[Any]]:
        """Group CAOM rows by target_name; return the group nearest the cone
        center (minimum 'distance' of the group, when that column exists)."""
        import numpy as np

        targets = [str(t) for t in obs["target_name"]]
        if "distance" in obs.colnames and len(obs) > 0:
            def _to_float(v: Any) -> float:
                try:
                    return float(v)
                except Exception:
                    return 1e9  # sentinel: unset distance ranks last
            dist = [_to_float(d) for d in obs["distance"]]
        else:
            dist = [0.0] * len(obs)
        best: dict[str, float] = {}
        for t, d in zip(targets, dist):
            best.setdefault(t, d)
            if d < best[t]:
                best[t] = d
        if not best:
            return None, []
        pick = sorted(best.items(), key=lambda kv: (kv[1], kv[0]))[0][0]
        sub = obs[[t == pick for t in targets]]
        return pick, list(sub)

    def sector_of(obs_id: str) -> int | None:
        m = re.search(r"s(\d{4})", str(obs_id))
        return int(m.group(1)) if m else None

    for name in TESS_TARGET_NAMES:
        c = resolve_name(name)
        if not c:
            builder.log(svc, f"TESS: name unresolved: {name!r}")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, f"NAME_RESOLVE_FAIL_{slug(name)}", dest_rel="",
                             state="excluded", url="CDS Sesame via astropy",
                             endpoint="SkyCoord.from_name", query=name, license_="",
                             note="for TESS SPOC cone search; no query issued"))
            continue
        coord = SkyCoord(c[0] * u.deg, c[1] * u.deg, frame="icrs")
        qrec = {
            "interface": "astroquery.mast Observations.query_criteria",
            "filters": {
                "coordinates": list(c),
                "radius_deg": 0.05,
                "provenance_name": "SPOC",
                "dataproduct_type": "timeseries",
                "obs_collection": "TESS",
            },
            "note": "cone search chosen after exact-name probe returned zero rows",
        }
        obs = Observations.query_criteria(
            coordinates=coord, radius=0.05 * u.deg, provenance_name="SPOC",
            dataproduct_type="timeseries", obs_collection="TESS",
        )
        if len(obs) == 0:
            builder.log(svc, f"no SPOC timeseries obs within 0.05 deg of {name!r}; probe recorded")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, f"QUERY_PROBE_TESS_{slug(name)}", dest_rel="",
                             state="excluded", url="MAST CAOM portal",
                             endpoint="astroquery.mast Observations.query_criteria",
                             query=json.dumps(qrec, sort_keys=True), license_="",
                             note="zero SPOC timeseries observations matched in cone"))
            continue
        pick_tgt, rows_g = group_nearest_by_target(obs)
        if not rows_g:
            builder.log(svc, f"no grouped target for {name!r}")
            continue
        qrec["cone_selected_caom_target_name"] = pick_tgt
        rows_g = sorted(
            rows_g,
            key=lambda r: (sector_of(r["obs_id"]) is None,
                           sector_of(r["obs_id"]) or 0, str(r["obs_id"])),
        )
        picks = rows_g if len(rows_g) <= 6 else [
            rows_g[0], rows_g[len(rows_g) // 5], rows_g[2 * len(rows_g) // 5],
            rows_g[3 * len(rows_g) // 5], rows_g[4 * len(rows_g) // 5], rows_g[-1]]
        for row in picks:
            products = Observations.get_product_list(row)
            picked = Observations.filter_products(products, productSubGroupDescription="LC")
            lcrows = [
                r for r in picked
                if str(r["dataURI"]).startswith("mast:TESS/product")
                and str(r["productFilename"]).endswith(".fits")
            ]
            if not lcrows:
                builder.log(svc, f"no TESS LC product for obs {row['obs_id']}")
                continue
            fetch_product_row(row, lcrows[0], "tess_spoc_lc", f"TESS SPOC LC | {name}", qrec)

    # -- Kepler long-cadence sample near NGC 6819 ----------------------------------------
    c6819 = resolve_name("NGC 6819")
    if not c6819:
        builder.log(svc, "NGC 6819 unresolved; Kepler sample skipped (logged)")
    else:
        coord = SkyCoord(c6819[0] * u.deg, c6819[1] * u.deg, frame="icrs")
        qrec = {
            "interface": "astroquery.mast Observations.query_criteria",
            "filters": {
                "coordinates": list(c6819), "radius_deg": 0.1,
                "dataproduct_type": "timeseries", "obs_collection": "Kepler",
            },
        }
        obs = Observations.query_criteria(
            coordinates=coord, radius=0.1 * u.deg,
            dataproduct_type="timeseries", obs_collection="Kepler",
        )
        if len(obs) == 0:
            builder.log(svc, "no Kepler timeseries obs within 0.1 deg of NGC 6819")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, "QUERY_PROBE_KEPLER_ngc6819", dest_rel="",
                             state="excluded", url="MAST CAOM portal",
                             endpoint="astroquery.mast Observations.query_criteria",
                             query=json.dumps(qrec, sort_keys=True), license_="",
                             note="zero Kepler timeseries observations matched in cone"))
        else:
            from collections import Counter

            counts = Counter(str(t) for t in obs["target_name"])
            # deterministic: the 8 targets with the most observations
            # (ties -> name order); 4 quarters each via LLC files
            top_targets = [t for t, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:8]]
            for pick_target in top_targets:
                star_rows = obs[[str(t) == pick_target for t in obs["target_name"]]]
                star_rows = sorted(star_rows, key=lambda r: str(r["obs_id"]))
                quarter_rows = (star_rows if len(star_rows) <= 4 else
                                [star_rows[0], star_rows[1],
                                 star_rows[len(star_rows) // 2], star_rows[-1]])
                for row in quarter_rows:
                    products = Observations.get_product_list(row)
                    # Kepler long-cadence light curves are subgroup 'LLC'
                    # (TESS SPOC LCs are 'LC'); live-probed 2026-09-23.
                    picked = Observations.filter_products(products, productSubGroupDescription="LLC")
                    lcrows = [
                        r for r in picked
                        if str(r["productFilename"]).lower().startswith("kplr")
                        and str(r["productFilename"]).endswith(".fits")
                    ]
                    if not lcrows:
                        builder.log(svc, f"no Kepler LC product for obs {row['obs_id']}")
                        continue
                    fetch_product_row(row, lcrows[0], "kepler_lc",
                                      f"Kepler LC | {pick_target}", qrec)

    # -- TESS FFI cutouts for the three test fields ---------------------------------------
    known_ids = {p["product_id"] for p in (builder.ledger.products("mast") if builder.ledger else [])}
    for fname in FIELD_NAMES:
        c = resolve_name(fname)
        if not c:
            builder.log(svc, f"Tesscut skipped; name unresolved: {fname!r}")
            continue
        import astropy.units as u
        from astropy.coordinates import SkyCoord

        coord = SkyCoord(c[0] * u.deg, c[1] * u.deg, frame="icrs")
        try:
            sectab = Tesscut.get_sectors(coordinates=coord)
            sectors = sorted({int(s) for s in sectab["sector"]})
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"Tesscut.get_sectors failed {fname!r}: {type(exc).__name__}: {exc}")
            continue
        if not sectors:
            builder.log(svc, f"Tesscut: no sectors cover {fname!r}")
            continue
        for sector_id in (sectors[0], sectors[-1]):
            planned_pid = f"tesscut-{slug(fname)}-sec{sector_id}-30px"
            if planned_pid in known_ids:
                builder.log(svc, f"REUSE (ledger): {planned_pid} already staged; not refetched")
                continue
            qrec = {"field_name": fname, "resolved_ra_dec": list(c),
                    "sector": sector_id, "size_px": 30, "product": "TESS FFI cutout"}
            try:
                hduls = Tesscut.get_cutouts(coordinates=coord, size=30, sector=sector_id)
            except Exception as exc:  # noqa: BLE001
                builder.log(svc, f"Tesscut.get_cutouts failed {fname!r} s{sector_id}: {type(exc).__name__}: {exc}")
                continue
            out_dir = builder.pack_dir(svc) / "tesscut"
            out_dir.mkdir(parents=True, exist_ok=True)
            for hdul in hduls:
                hdr = hdul[0].header
                out = out_dir / f"tesscut_{slug(fname)}_sec{hdr.get('SECTOR', sector_id)}_30px.fits"
                hdul.writeto(out, overwrite=True)
                builder.register(
                    svc,
                    planned_pid,
                    path=out,
                    url=f"https://mast.stsci.edu/tesscut/api/v0.1/ (astroquery Tesscut.get_cutouts; sector={sector_id}; 30 px)",
                    endpoint=TESSCUT_EP,
                    query=json.dumps(qrec, sort_keys=True),
                    license_=lic,
                    extra={
                        "sector": hdr.get("SECTOR"), "camera": hdr.get("CAMERA"),
                        "ccd": hdr.get("CCD"), "naxis1": hdr.get("NAXIS1"),
                        "naxis2": hdr.get("NAXIS2"),
                        "wcs_note": "from FITS header (CRVAL/CDELT)",
                    },
                )

    # -- JWST + HST representative samples -------------------------------------------------
    def mission_smallest(cand_names: list[str], mission: str, radius_deg: float,
                         dest_dir: str, mount: int, budget_each: int) -> None:
        # Live probe 2026-09-23: a 'provenance_name="JWST"' filter returned zero
        # rows (actual CAOM provenance is 'CALJWST'); cone + obs_collection
        # matches (400 rows for SMACS J0723.3-7327). Same pattern used for HST.
        prod_meta: dict[str, Any] = {
            "interface": "astroquery.mast Observations.query_criteria + get_product_list(+filter size pick)",
            "obs_collection": mission,
            "name_probe_candidates": cand_names,
            "radius_deg": radius_deg,
            "pick": f"smallest {mount} fits product(s) <= {budget_each} bytes, earliest obs_id first",
        }
        got = 0
        for name in cand_names:
            c = resolve_name(name)
            if not c:
                builder.log(svc, f"{mission}: name unresolved: {name!r}")
                continue
            import astropy.units as u
            from astropy.coordinates import SkyCoord

            coord = SkyCoord(c[0] * u.deg, c[1] * u.deg, frame="icrs")
            for dptype in ("spectrum", "image"):
                prod_meta_this: dict[str, Any] = dict(prod_meta)
                prod_meta_this.update({"resolved_name": name, "resolved_ra_dec": list(c),
                                       "dataproduct_type": dptype})
                obs = Observations.query_criteria(
                    coordinates=coord, radius=radius_deg * u.deg,
                    obs_collection=mission, dataproduct_type=dptype)
                if len(obs) == 0:
                    builder.log(svc, f"{mission} {dptype}: zero obs within {radius_deg} deg of {name!r}")
                    builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                        builder._row(svc, f"QUERY_PROBE_{mission}_{dptype}_{slug(name)}",  # noqa: SLF001
                                     dest_rel="", state="excluded", url="MAST CAOM portal",
                                     endpoint="astroquery.mast Observations.query_criteria",
                                     query=json.dumps(prod_meta_this, sort_keys=True), license_="",
                                     note="zero observations matched in cone"))
                    continue
                obs.sort("obs_id")
                products = Observations.get_product_list(obs[0])
                keep: list[tuple[int, Any, int | None]] = []
                for r in products:
                    size: int | None
                    try:
                        size = int(r["size"]) if r["size"] is not None else None
                    except Exception:
                        size = None
                    fname_p = str(r["productFilename"])
                    if not (fname_p.endswith(".fits") or fname_p.endswith(".fits.gz")):
                        continue
                    if size is not None and size > budget_each:
                        continue
                    keep.append((size if size is not None else budget_each * 10, r, size))
                if not keep:
                    builder.log(svc, f"{mission} {dptype}: no fits products under cap; logged")
                    continue
                keep.sort(key=lambda t: (t[0], str(t[1]["obs_id"])))
                for _, prod, size in keep[:mount]:
                    uri = str(prod["dataURI"])
                    fname2 = str(prod["productFilename"])
                    url = f"{MAST_API_DL}?uri={urllib.parse.quote(uri)}"
                    ex = obs_extra(obs[0])
                    ex.update({"dataURI": uri, "dataproduct_type": dptype,
                               "pick_rule": prod_meta_this["pick"]})
                    builder.try_fetch(
                        svc, fname2, url=url, dest_rel=f"{dest_dir}/{fname2}",
                        endpoint=f"MAST download API {MAST_API_DL} (dataURI: {uri})",
                        query=json.dumps(prod_meta_this, sort_keys=True)[:2000],
                        license_=lic, size_hint=size, extra=ex,
                    )
                    got += 1
                if got >= mount:
                    builder.log(svc, f"{mission} sample complete ({dptype})")
                    return
        builder.log(svc, f"{mission}: no sample product secured; every probe is manifest-recorded")

    mission_smallest(["SMACS 0723", "SMACS J0723.3-7327"], "JWST", 0.05, "jwst_sample", 2, 45_000_000)
    mission_smallest(["M42", "Orion Nebula"], "HST", 0.05, "hst_sample", 2, 25_000_000)


# --------------------------------------------------------------------------- Gaia DR3

_GAIA_SRC_COLS = (
    "source_id, ra, ra_error, dec, dec_error, parallax, parallax_error, "
    "parallax_over_error, pm, pmra, pmra_error, pmdec, pmdec_error, "
    "radial_velocity, radial_velocity_error, phot_g_mean_mag, "
    "phot_g_mean_flux_over_error, phot_bp_mean_mag, phot_rp_mean_mag, bp_rp, "
    "ruwe, astrometric_params_solved, visibility_periods_used, "
    "astrometric_chi2_al, astrometric_n_good_obs_al, phot_g_n_obs, "
    "ecl_lon, ecl_lat, has_xp_continuous, has_rvs"
)


def collect_gaia(builder: PackBuilder) -> None:
    """Gaia DR3 via TapDirect (byte-safe TAP; see cygnus.ingest.tap rationale).

    Both astroquery.gaia (text results) and pyvo (VOTables) failed live for
    tap_schema descriptions on 2026-09-23; the direct byte-safe client is used
    instead for every Gaia DR3 query in this pack.
    """
    from .tap import TapDirect

    svc = "gaia"
    lic = "ESA Gaia DR3 archive data; archive terms apply (license recorded after live verification)"
    tap = TapDirect("https://gea.esac.esa.int/tap-server/tap")

    prior = {(p["product_id"], (p["checksum"] or "")): p for p in builder.ledger.products("gaia")} \
        if builder.ledger else {}

    def reuse_if_cached(pid: str, drel: str, adql: str,
                        extra: dict[str, Any] | None = None) -> dict[str, Any] | None:
        for (cpid, ck), prow in prior.items():
            if cpid == pid and ck:
                path = builder.pack_dir(svc) / drel
                if path.exists() and path.stat().st_size > 0:
                    from cygnus.ingest.netio import sha256_file as cyg_sha
                    if cyg_sha(path) == ck:
                        mrow = builder.register_table(svc, pid, path=path,
                                                      endpoint=_GAIA_EP, query=adql,
                                                      license_=lic,
                                                      extra={**(extra or {}),
                                                             "reuse": "checksum-matched prior stage"})
                        builder.log(svc, f"REUSE (staged match): {pid}")
                        return mrow
        return None

    def run_table(pid: str, drel: str, adql: str, extra: dict[str, Any] | None = None) -> None:
        mrow = reuse_if_cached(pid, drel, adql, extra)
        if mrow is not None:
            return
        try:
            tab, status, route = tap.run(adql)
            p = table_to_csv(tab, builder.pack_dir(svc) / drel)
            builder.register_table(
                svc, pid, path=p, endpoint=_GAIA_EP, query=adql, license_=lic,
                extra={**(extra or {}),
                       "nrows": int(len(tab)) if tab is not None else 0,
                       "ncols": int(len(tab.colnames)) if tab is not None else 0,
                       "route": route, "status": status,
                       "format": "TAP VOTable bytes -> astropy Table -> ascii.csv"},
            )
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"query failed ({pid}): {type(exc).__name__}: {exc}")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, pid, dest_rel=drel, state="failed", url=_GAIA_EP,  # noqa: SLF001
                             endpoint=_GAIA_EP, query=adql, license_=lic,
                             note=f"query error: {type(exc).__name__}: {str(exc)[:500]}"))

    # tap_schema dump first: proves which tables the release exposed on the date.
    run_table(
        "tap_schema_gaiadr3_tables", "tap_schema_gaiadr3_tables.csv",
        "SELECT TOP 200 table_name, description FROM tap_schema.tables "
        "WHERE schema_name='gaiadr3'",
        extra={"note": "schema state of gaiadr3 at retrieval date"},
    )

    # Core astrometric/photometric cones over the three test fields.
    for fname in FIELD_NAMES:
        c = resolve_name(fname)
        if not c:
            builder.log(svc, f"field unresolved: {fname!r}")
            continue
        run_table(
            f"gaia_source_cone_{slug(fname)}_r0d5",
            f"gaia_source/cone_{slug(fname)}_r0d5_top100k.csv",
            f"SELECT TOP 100000 {_GAIA_SRC_COLS} FROM gaiadr3.gaia_source "
            f"WHERE 1 = CONTAINS(POINT('ICRS', ra, dec), "
            f"CIRCLE('ICRS', {c[0]:.6f}, {c[1]:.6f}, 0.5))",
        )

    # Wide 1.0-degree cones (volume lever; the 0.5-degree cores stay as-is).
    for fname in FIELD_NAMES:
        c = resolve_name(fname)
        if not c:
            continue
        run_table(
            f"gaia_source_cone_{slug(fname)}_r1d0",
            f"gaia_source/cone_{slug(fname)}_r1d0_top200k.csv",
            f"SELECT TOP 200000 {_GAIA_SRC_COLS} FROM gaiadr3.gaia_source "
            f"WHERE 1 = CONTAINS(POINT('ICRS', ra, dec), "
            f"CIRCLE('ICRS', {c[0]:.6f}, {c[1]:.6f}, 1.0))",
        )

    # Known-Object Gate prerequisites: NSS two-body orbits (dark-companion domain).
    # Table names verified against the live tap_schema dump (2026-09-23):
    # 'nss_acceleration' does not exist; the acceleration table is
    # 'nss_acceleration_astro'; 'vari_eb' is 'vari_eclipsing_binary'; and
    # 'xp_sampled_mean_spectrum' is absent from the live gaiadr3 schema dump
    # (xp_summary is queried instead).
    run_table("nss_two_body_orbit_top100k", "nss/nss_two_body_orbit_top100k.csv",
              "SELECT TOP 100000 * FROM gaiadr3.nss_two_body_orbit")
    run_table("nss_acceleration_astro_top100k", "nss/nss_acceleration_astro_top100k.csv",
              "SELECT TOP 100000 * FROM gaiadr3.nss_acceleration_astro")

    # Variable-star samples (screening prerequisites).
    run_table("vari_rrlyrae_top50k", "vari/vari_rrlyrae_top50k.csv",
              "SELECT TOP 50000 * FROM gaiadr3.vari_rrlyrae")
    run_table("vari_eclipsing_binary_top50k", "vari/vari_eclipsing_binary_top50k.csv",
              "SELECT TOP 50000 * FROM gaiadr3.vari_eclipsing_binary")
    run_table("vari_summary_top10k", "vari/vari_summary_top10k.csv",
              "SELECT TOP 10000 * FROM gaiadr3.vari_summary")
    run_table("xp_summary_top5000", "xp/xp_summary_top5000.csv",
              "SELECT TOP 5000 * FROM gaiadr3.xp_summary")


# --------------------------------------------------------------------------- SkyView


def collect_skyview(builder: PackBuilder) -> None:
    from astroquery.skyview import SkyView

    svc = "skyview"
    lic = "survey data redistributed via NASA SkyView; per-survey terms apply"

    try:
        d = SkyView.survey_dict
        # values are the requestable survey names; keys carry group labels
        flat: list[str] = sorted({str(n).strip() for vals in (d or {}).values()
                                  for n in (vals or [])})
        pl = builder.pack_dir(svc) / "skyview_survey_list.txt"
        pl.write_text("\n".join(flat), encoding="utf-8")
        builder.register_table(svc, "skyview_survey_list", path=pl,
                               endpoint="astroquery.skyview SkyView.survey_dict",
                               query="surveys available at SkyView on the retrieval date; "
                                     "selection below records exact chosen names",
                               license_="", extra={"n_surveys": len(flat)})
    except Exception as exc:  # noqa: BLE001
        flat = []
        builder.log(svc, f"survey_dict failed: {type(exc).__name__}: {exc}; using requested names directly")

    def pick_survey(candidates: list[str]) -> str:
        for cand in candidates:
            for s in flat:
                if s.lower() == cand.lower():
                    return s
        return candidates[0]

    known_ids = {p["product_id"] for p in (builder.ledger.products("skyview") if builder.ledger else [])}

    bands = {
        "DSS2_Blue": ["DSS2 Blue"],
        "2MASS_K": ["2MASS-K"],
        "WISE_12": ["WISE 12"],
        "GALEX_NUV": ["GALEX Near UV", "GALEX NUV"],
        "SDSS_g": ["SDSSg"],
    }
    for fname in FIELD_NAMES:
        c = resolve_name(fname)
        if not c:
            builder.log(svc, f"field unresolved: {fname!r}")
            continue
        position = f"{c[0]:.6f} {c[1]:.6f}"  # degrees, ICRS (Sesame-resolved)
        for band, cands in bands.items():
            planned_pid = f"skyview_{slug(fname)}_{band}_0"
            if planned_pid in known_ids:
                # already staged + ledgered in a prior round; reuse after checksum
                prio = {p["product_id"]: p for p in builder.ledger.products("skyview")} if builder.ledger else {}
                prow = prio.get(planned_pid)
                path = builder.pack_dir(svc) / "cutouts" / f"skyview_{slug(fname)}_{band}_0.fits"
                if prow and prow["checksum"] and path.exists():
                    from cygnus.ingest.netio import sha256_file as cyg_sha
                    try:
                        if cyg_sha(path) == prow["checksum"]:
                            builder.register(
                                svc, planned_pid, path=path,
                                url="astroquery.skyview (reuse from staged prior round)",
                                endpoint="astroquery.skyview SkyView.get_images",
                                query=json.dumps({"field": fname, "band": band,
                                                  "pixels": [1400, 1400]}, sort_keys=True),
                                license_=lic,
                                extra={"reuse": "checksum-matched prior stage"})
                            builder.log(svc, f"REUSE (staged match): {planned_pid}")
                            continue
                    except OSError:
                        pass
            survey = pick_survey(cands)
            try:
                imgs = SkyView.get_images(position=position, survey=[survey],
                                          pixels=(1400, 1400), size="0.5 degrees")
            except Exception:  # noqa: BLE001 - retry without explicit size
                try:
                    imgs = SkyView.get_images(position=position, survey=[survey],
                                              pixels=(1400, 1400))
                except Exception as exc:  # noqa: BLE001
                    builder.log(svc, f"{band} failed for {fname!r}: {type(exc).__name__}: {exc}")
                    builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                        builder._row(svc, f"skyview_{slug(fname)}_{band}", dest_rel="",  # noqa: SLF001
                                     state="failed", url="astroquery.skyview get_images",
                                     endpoint="astroquery.skyview SkyView.get_images",
                                     query=json.dumps({"position": position, "survey": survey,
                                                       "field": fname}, sort_keys=True),
                                     license_="", note=f"error: {type(exc).__name__}: {str(exc)[:400]}"))
                    continue
            out_dir = builder.pack_dir(svc) / "cutouts"
            out_dir.mkdir(parents=True, exist_ok=True)
            if not imgs:
                builder.log(svc, f"{band} {fname!r}: zero images returned (coverage?)")
                builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                    builder._row(svc, f"skyview_{slug(fname)}_{band}", dest_rel="",  # noqa: SLF001
                                 state="excluded", url="astroquery.skyview",
                                 endpoint="astroquery.skyview SkyView.get_images",
                                 query=json.dumps({"position": position, "survey": survey, "field": fname},
                                                  sort_keys=True),
                                 license_="", note="zero images returned"))
                continue
            for i, hdul in enumerate(imgs):
                hdr = hdul[0].header
                out = out_dir / f"skyview_{slug(fname)}_{band}_{i}.fits"
                hdul.writeto(out, overwrite=True)
                builder.register(
                    svc, f"skyview_{slug(fname)}_{band}_{i}", path=out,
                    url=f"astroquery.skyview SkyView.get_images (position={position}, survey={survey!r}, pixels=1400x1400, size=0.5deg)",
                    endpoint="astroquery.skyview SkyView.get_images",
                    query=json.dumps({"position_degrees": position, "survey_requested": survey,
                                      "survey_list_used": bool(flat), "field": fname,
                                      "pixels": [1400, 1400]}, sort_keys=True),
                    license_=lic,
                    extra={"crval1": hdr.get("CRVAL1"), "crval2": hdr.get("CRVAL2"),
                           "cdelt1": hdr.get("CDELT1"), "cdelt2": hdr.get("CDELT2"),
                           "naxis1": hdr.get("NAXIS1"), "naxis2": hdr.get("NAXIS2"),
                           "wcs_note": "actual pixel grid comes from the returned FITS header"},
                )


# --------------------------------------------------------------------------- CDS (VizieR + SIMBAD)

_CDS_KEYWORDS = ("vsx", "eclipsing binary", "variable star", "period", "ztf", "tic")

_LICENSE_CDS = "(CDS distribution; catalog-specific terms apply)"


def collect_cds(builder: PackBuilder) -> None:
    from .tap import TapDirect

    svc = "cds"
    tap = TapDirect(_VIZIER_TAP)

    def run_table(pid: str, drel: str, adql: str, extra: dict[str, Any] | None = None,
                  license_: str = _LICENSE_CDS) -> None:
        try:
            tab, status, route = tap.run(adql)
            p = table_to_csv(tab, builder.pack_dir(svc) / drel)
            builder.register_table(
                svc, pid, path=p, endpoint=_VIZIER_TAP, query=adql, license_=license_,
                extra={**(extra or {}),
                       "nrows": int(len(tab)) if tab is not None else 0,
                       "route": route, "status": status})
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"query failed ({pid}): {type(exc).__name__}: {exc}")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, pid, dest_rel=drel, state="failed", url=_VIZIER_TAP,  # noqa: SLF001
                             endpoint=_VIZIER_TAP, query=adql, license_=license_,
                             note=f"query error: {type(exc).__name__}: {str(exc)[:500]}"))

    # (1) schema probe to identify the watchlist tables actually served today
    probe_q = (
        "SELECT TOP 120 table_name, description FROM tap_schema.tables WHERE "
        + "(" + " OR ".join(f"description LIKE '%{k}%'" for k in _CDS_KEYWORDS) + ")"
    )
    probe_tab = None
    try:
        tab, status, route = tap.run(probe_q)
        probe_tab = tab
        p = table_to_csv(tab, builder.pack_dir(svc) / "tap_schema_probe.csv")
        builder.register_table(svc, "tap_schema_probe", path=p, endpoint=_VIZIER_TAP,
                               query=probe_q, license_=_LICENSE_CDS,
                               extra={"note": "watchlist-discovery probe (ANALYSIS_STACK.md Gate 1)",
                                      "nrows": int(len(tab)), "route": route, "status": status})
    except Exception as exc:  # noqa: BLE001
        builder.log(svc, f"tap_schema probe failed: {type(exc).__name__}: {exc}")

    # (2) deterministic picks from the probe (VSX first), else fall back to known ids
    # TAPVizieR returns tap_schema.table_name values already wrapped in quotes
    # (e.g. "'I/357/tboes'" or '"B/vsx"'); strip them before wrapping in the
    # ADQL double quotes the FROM clause needs.
    picks: list[tuple[str, str]] = []
    if probe_tab is not None and len(probe_tab) > 0:
        scored = []
        for r in probe_tab:
            tname = str(r["table_name"]).strip("'\" ").strip()
            if not tname:
                continue
            desc = str(r["description"] or "")
            hay = (tname + " " + desc).lower()
            score = max((1000 - i for i, kw in enumerate(_CDS_KEYWORDS) if kw in hay), default=0)
            scored.append((score, tname, desc))
        scored.sort(key=lambda t: (-t[0], t[1]))
        picks = [(t[1], t[2]) for t in scored[:8]]
    # 'B/vsx/vsx' verified live in TAPVizieR tap_schema (2026-09-24):
    # 'B/vsx' alone does not resolve ("table B/vsx is not found").
    fallback = [("B/vsx/vsx", "Variable Star indeX (VSX), Version 2026-08-09 (Watson+, CDS B/vsx)")]
    for fb in fallback:
        if fb[0] not in [p[0] for p in picks]:
            picks.append(fb)

    for tname, desc in picks:
        run_table(
            f"vizier_extract_{slug(tname)}",
            f"watchlists/{slug(tname)}_top20k.csv",
            f'SELECT TOP 20000 * FROM "{tname}"',
            extra={"catalog_description": desc[:400],
                   "gate_role": "Known-Object Gate 1 watchlist"},
        )

    # (3) SIMBAD object table for the benchmark list
    from astroquery.simbad import Simbad

    rows = []
    fail_notes = []
    for name in BENCH_OBJECT_NAMES:
        q = {"interface": "astroquery.simbad Simbad.query_object", "object": name}
        try:
            t = Simbad.query_object(name)
            if t is None or len(t) == 0:
                fail_notes.append(f"{name}: zero rows")
                continue
            d = {c: (t[c][0].item() if hasattr(t[c][0], "item") else t[c][0]) for c in t.colnames}
            d["queried_name"] = name
            rows.append(d)
        except Exception as exc:  # noqa: BLE001
            fail_notes.append(f"{name}: {type(exc).__name__}: {str(exc)[:180]}")
    if rows:
        import astropy.table

        atab = astropy.table.Table(rows)
        p3 = table_to_csv(atab, builder.pack_dir(svc) / "simbad_benchmark_objects.csv")
        builder.register_table(
            svc, "simbad_benchmark_objects", path=p3, endpoint=_SIMBAD_EP,
            query="Simbad.query_object(name) for each of BENCH_OBJECT_NAMES; see NAME_RESOLUTIONS.json",
            license_=_LICENSE_CDS,
            extra={"objects_requested": len(BENCH_OBJECT_NAMES), "objects_matched": len(rows),
                   "failures": fail_notes[:60]}
        )
    else:
        builder.log(svc, "SIMBAD: no benchmark object resolved "
                         f"(failures: {'; '.join(fail_notes[:8])})")


# --------------------------------------------------------------------------- NED


def collect_ned(builder: PackBuilder) -> None:
    svc = "ned"
    lic = "public (NED; cite NED in derived work)"
    from astroquery.ned import Ned

    rows: list[dict[str, Any]] = []
    err: list[str] = []
    for name in BENCH_OBJECT_NAMES[:10]:
        try:
            t = Ned.query_object(name)
            if t is None or len(t) == 0:
                err.append(f"{name}: zero rows")
                continue
            dd = {c: (t[c][0].item() if hasattr(t[c][0], "item") else t[c][0]) for c in t.colnames}
            dd["queried_name"] = name
            rows.append(dd)
        except Exception as exc:  # noqa: BLE001
            err.append(f"{name}: {type(exc).__name__}: {str(exc)[:200]}")
    if rows:
        import astropy.table

        atab = astropy.table.Table(rows)
        p = table_to_csv(atab, builder.pack_dir(svc) / "ned_benchmark_objects.csv")
        builder.register_table(
            svc, "ned_benchmark_objects", path=p,
            endpoint="astroquery.ned Ned.query_object (ned.ipac.caltech.edu)",
            query="Ned.query_object(name) for the first 10 BENCH_OBJECT_NAMES",
            license_=lic,
            extra={"objects_requested": min(10, len(BENCH_OBJECT_NAMES)),
                   "objects_matched": len(rows), "failures": err[:40]},
        )
    else:
        builder.log(svc, f"NED: no object resolved (failures: {'; '.join(err[:8])})")
        builder._rows.setdefault(svc, []).append(  # noqa: SLF001
            builder._row(svc, "QUERY_PROBE_NED", dest_rel="", state="excluded",  # noqa: SLF001
                         url="ned.ipac.caltech.edu", endpoint="astroquery.ned Ned.query_object",
                         query="first 10 BENCH_OBJECT_NAMES", license_="",
                         note=f"all probes failed/empty: {'; '.join(err[:10])}"))


# --------------------------------------------------------------------------- ESO


def collect_eso(builder: PackBuilder) -> None:
    from .tap import TapDirect

    svc = "eso"
    lic = "public release products; per ESO Scientific Data Policy (license recorded honestly)"
    tap = TapDirect(_ESO_TAP)

    base_cols = ("obs_publisher_did, instrument_name, dataproduct_type, target_name, "
                 "access_url, access_estsize, t_min, t_max, em_min, em_max, proposal_id")
    # Live-probed 2026-09-24: ESO ObsCore has no 'dataRights' column (400), and
    # sync with the plain filter succeeds, so query directly without async.
    query = (f"SELECT TOP 100 {base_cols} FROM ivoa.ObsCore WHERE "
             "instrument_name = 'HARPS' AND dataproduct_type = 'spectrum'")
    try:
        res, status = tap.sync_table(query, timeout_s=420.0, max_retries=2)
        route = "sync"
        builder.log(svc, "ObsCore metadata sync OK (no dataRights filter; column absent)")
    except Exception as exc:  # noqa: BLE001
        builder.log(svc, f"ESO TAP failed: {type(exc).__name__}: {exc}")
        builder._rows.setdefault(svc, []).append(  # noqa: SLF001
            builder._row(svc, "ESO_TAP_PROBE", dest_rel="", state="failed",  # noqa: SLF001
                         url=_ESO_TAP, endpoint=_ESO_TAP, query=base_cols, license_="",
                         note=f"TAP error: {type(exc).__name__}: {str(exc)[:400]}"))
        return
    p = table_to_csv(res, builder.pack_dir(svc) / "eso_harps_metadata.csv")
    builder.register_table(svc, "eso_harps_metadata", path=p, endpoint=_ESO_TAP,
                           query=query, license_=lic,
                           extra={"nrows": int(len(res)) if res is not None else 0,
                                  "route": route, "status": status})
    if res is None or len(res) == 0:
        builder.log(svc, "ESO: zero HARPS public spectra rows; product fetch skipped")
        return

    # access_url values are ESO DATALINK pointers (verified live), so resolve
    # each product through the datalink service first, then fetch the science
    # FITS it points at.
    est: list[tuple[int | None, Any]] = []
    for r in res:
        try:
            v = r["access_estsize"]
            est.append((int(v) if v is not None else None, r))
        except Exception:
            est.append((None, r))
    known = [t for t in est if t[0] is not None]
    known.sort(key=lambda t: t[0])
    chosen = [r for _, r in known[:3]]
    if not chosen:
        chosen = list(res[:3])
    fetched = 0
    for r in chosen:
        pid = str(r["obs_publisher_did"]) or "eso_product"
        url = str(r["access_url"]) if r["access_url"] is not None else ""
        if not url:
            builder.log(svc, f"no access_url for {pid}; recorded excluded (metadata-only)")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, f"eso_product_{slug(pid)}", dest_rel="products",  # noqa: SLF001
                             state="excluded", url="", endpoint=_ESO_TAP,
                             query="access_url absent", license_="",
                             note="ObsCore row lacks access_url; not fetched"))
            continue
        if fetched >= 2:
            builder.log(svc, f"ESO product quota reached; skipping {pid} (recorded)")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, f"eso_product_{slug(pid)}", dest_rel="products",  # noqa: SLF001
                             state="excluded", url=url, endpoint=_ESO_TAP,
                             query="datalink not resolved (2-product quota)", license_="",
                             note="not fetched; datalink pointer recorded"))
            continue
        try:
            from .tap import parse_votable_bytes

            dl = cyg_session().get(url, timeout=300.0)
            dl.raise_for_status()
            dtab = parse_votable_bytes(dl.content)
            if dtab is None or len(dtab) == 0:
                builder.log(svc, f"datalink empty for {pid}")
                continue
            # deterministic: smallest .fits science URL in the datalink response
            cands: list[tuple[int, str]] = []
            for drow in dtab:
                durl = str(drow["access_url"]) if "access_url" in dtab.colnames else ""
                if not durl:
                    continue
                clen = None
                if "content_length" in dtab.colnames:
                    try:
                        clen = int(drow["content_length"])
                    except Exception:
                        clen = None
                if clen is None:
                    clen = 10**9
                ctype = str(drow["content_type"]) if "content_type" in dtab.colnames else ""
                if ".fits" in durl.lower() or "fits" in ctype.lower():
                    cands.append((clen, durl))
            if not cands:
                builder.log(svc, f"datalink for {pid}: no fits links")
                builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                    builder._row(svc, f"eso_product_{slug(pid)}", dest_rel="products",  # noqa: SLF001
                                 state="excluded", url=url, endpoint="ESO datalink",
                                 query=json.dumps({"datalink": url}), license_="",
                                 note="datalink response contains no .fits links"))
                continue
            cands.sort(key=lambda t: t[0])
            fits_url = cands[0][1]
            builder.try_fetch(svc, f"eso_product_{slug(pid)}", url=fits_url,
                              dest_rel=f"products/{slug(pid)}.fits",
                              endpoint="ESO datalink resolution -> product file",
                              query=json.dumps({"obs_publisher_did": pid,
                                                "datalink_url": url,
                                                "fits_url": fits_url,
                                                "selection": "2 smallest science fits via datalink"}, sort_keys=True),
                              license_=lic,
                              extra={"target_name": str(r["target_name"]),
                                     "instrument_name": str(r["instrument_name"])})
            fetched += 1
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"ESO product fetch error {pid}: {type(exc).__name__}: {exc}")


# --------------------------------------------------------------------------- IRSA


def collect_irsa(builder: PackBuilder) -> None:
    from .tap import TapDirect

    svc = "irsa"
    lic = "public (IPAC/IRSA services; cite IRSA)"
    tap = TapDirect(_IRSA_TAP)

    # tap_schema probe: AllWISE + 2MASS + ZTF table inventory as of today
    probe_q = ("SELECT TOP 120 table_name, description FROM tap_schema.tables WHERE "
               "table_name LIKE '%allwise%' OR table_name LIKE '%twomass%' OR table_name LIKE 'ztf%'")
    res = None
    try:
        res, status, route = tap.run(probe_q)
        p = table_to_csv(res, builder.pack_dir(svc) / "tap_schema_probe.csv")
        builder.register_table(svc, "tap_schema_probe", path=p, endpoint=_IRSA_TAP,
                               query=probe_q, license_="",
                               extra={"n_tables": int(len(res)) if res is not None else 0,
                                      "route": route, "status": status})
    except Exception as exc:  # noqa: BLE001
        builder.log(svc, f"tap_schema probe failed: {type(exc).__name__}: {exc}")
        res = None

    def pick_table(prefix: str, default: str) -> str:
        # IRSA's tap_schema VOTable exposes unnamed columns (col_0, col_1...);
        # use positional access instead of fixed column names.
        if res is not None and len(res) > 0:
            for r in res:
                n = str(r[0])
                if n.startswith(prefix):
                    return n
        return default

    allwise_tbl = pick_table("allwise_p3as_psd", "allwise_p3as_psd")
    twomass_tbl = pick_table("twomass", "twomass_psc")

    # Live-probed 2026-09-24: the 20-column request (with w1sat, pmra, pmdec,
    # pmraerr, pmdecerr) is rejected server-side (async phase=ERROR); the
    # six-column list below is the verified-working set for allwise_p3as_psd.
    aw_cols = "designation, ra, dec, w1mpro, w2mpro, cc_flags"
    for fname in FIELD_NAMES:
        c = resolve_name(fname)
        if not c:
            builder.log(svc, f"field unresolved: {fname!r}")
            continue
        adql = (f"SELECT TOP 200000 {aw_cols} FROM {allwise_tbl} "
                f"WHERE CONTAINS(POINT('J2000', ra, dec), "
                f"CIRCLE('J2000', {c[0]:.6f}, {c[1]:.6f}, 0.5)) = 1")
        try:
            tab, status, route = tap.run(adql)
            p = table_to_csv(tab, builder.pack_dir(svc) / "allwise" / f"allwise_{slug(fname)}_r0d5_top200k.csv")
            builder.register_table(svc, f"allwise_{slug(fname)}_r0d5", path=p, endpoint=_IRSA_TAP,
                                   query=adql, license_=lic,
                                   extra={"table": allwise_tbl, "nrows": int(len(tab)),
                                          "route": route, "status": status,
                                          "note": "single-query path after server rejected the "
                                                  "20-column list (recorded in prior run logs)"})
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"AllWISE cone failed {fname!r}: {type(exc).__name__}: {exc}")
            builder._rows.setdefault(svc, []).append(  # noqa: SLF001
                builder._row(svc, f"allwise_{slug(fname)}_r0d5", dest_rel="allwise/"
                             f"allwise_{slug(fname)}_r0d5_top200k.csv", state="failed",
                             url=_IRSA_TAP, endpoint=_IRSA_TAP, query=adql, license_="",
                             note=f"query error: {type(exc).__name__}: {str(exc)[:400]}"))

    # 2MASS point-source catalog: IRSA TAP exposes image-metadata tables only
    # (twomass.*_images; verified via tap_schema probe on 2026-09-23), so the
    # 2MASS PS cone is recorded as excluded rather than guessed.
    builder._rows.setdefault(svc, []).append(  # noqa: SLF001
        builder._row(svc, "twomass_psc_cone", dest_rel="", state="excluded",  # noqa: SLF001
                     url=_IRSA_TAP, endpoint=_IRSA_TAP,
                     query="2MASS point-source cone (dropped: table not in IRSA TAP)",
                     license_="", note="tap_schema probe lists twomass image tables only; "
                                       "no point-source table served via TAP"))

    # ZTF light-curve service (CGI) — live-probed 2026-09-23: only POS and
    # FORMAT are accepted; 'MERGE'/'BAD_DATA' raise UsageFault 400.
    for fname in ("Pleiades", "M44", "NGC 5139", "NGC 6819"):
        c = resolve_name(fname)
        if not c:
            builder.log(svc, f"ZTF anchor unresolved: {fname!r}")
            continue
        pos = f"CIRCLE {c[0]:.6f} {c[1]:.6f} 0.0046"
        builder.try_fetch(
            svc, f"ztf_lc_{slug(fname)}_16as",
            url=_ZTF_NPH,
            params={"POS": pos, "FORMAT": "csv"},
            dest_rel=f"ztf_lc/{slug(fname)}_r0d0026.csv",
            endpoint=f"IRSA ZTF CGIS {_ZTF_NPH} (POS={pos}; FORMAT=csv)",
            query="IRSA ZTF light-curve CGI: all matched light curves within 0.0046 deg (16.6 arcsec) of the Sesame-resolved anchor",
            license_=lic,
            extra={"radius_deg": 0.0046, "anchor": fname},
        )
        # wider extraction (72 arcsec) for more matched objects per anchor
        pos2 = f"CIRCLE {c[0]:.6f} {c[1]:.6f} 0.02"
        builder.try_fetch(
            svc, f"ztf_lc_{slug(fname)}_72as",
            url=_ZTF_NPH,
            params={"POS": pos2, "FORMAT": "csv"},
            dest_rel=f"ztf_lc/{slug(fname)}_r0d02.csv",
            endpoint=f"IRSA ZTF CGIS {_ZTF_NPH} (POS={pos2}; FORMAT=csv)",
            query="IRSA ZTF light-curve CGI: all matched light curves within 0.02 deg (72 arcsec) of the Sesame-resolved anchor",
            license_=lic,
            extra={"radius_deg": 0.02, "anchor": fname},
        )


# --------------------------------------------------------------------------- Legacy Survey


def collect_legacysurvey(builder: PackBuilder) -> None:
    svc = "legacysurvey"
    lic = "(license per legacysurvey.org terms; recorded after live verification)"

    # The old /api/region/tractor service is retired (nginx 404s observed
    # 2026-09-23). Current documented access (verified live):
    #   * brick lookup  : /viewer/bricks/?ralo=..&rahi=..&declo=..&dechi=..&layer=ls-dr9
    #   * tractor files : https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr9/{north|south}/tractor/{AAA}/tractor-{brick}.fits
    #   * cutouts       : /viewer/fits-cutout, /viewer/jpeg-cutout
    bricks_url = f"{_LS_BASE}/viewer/bricks/"
    portal = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr9"
    boxes = [
        ("M44", 0.5, "ls-dr9", "dr9"),
        ("Pleiades", 0.5, "ls-dr9", "dr9"),
        ("NGC 5139", 0.5, "ls-dr10", "dr10"),
    ]
    for fname, halfside, layer, drtag in boxes:
        c = resolve_name(fname)
        if not c:
            builder.log(svc, f"field unresolved: {fname!r}")
            continue
        params = {"ralo": f"{c[0] - halfside:.6f}", "rahi": f"{c[0] + halfside:.6f}",
                  "declo": f"{c[1] - halfside:.6f}", "dechi": f"{c[1] + halfside:.6f}",
                  "layer": layer}
        full_url = f"{bricks_url}?{urllib.parse.urlencode(params)}"
        try:
            brk = builder.try_fetch(
                svc, f"bricks_listing_{slug(fname)}_{drtag}",
                url=bricks_url, params=params,
                dest_rel=f"bricks/{slug(fname)}_{drtag}_bricks.json",
                endpoint=full_url,
                query=f"brick polygons in a {2*halfside}x{2*halfside} deg box around Sesame-resolved {fname} ({layer} layer)",
                license_="", extra={"field": fname, "layer": layer}, timeout_s=300.0,
            )
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"bricks listing failed {fname!r}: {type(exc).__name__}: {exc}")
            brk = None
        if not brk or brk.get("state") != "local":
            builder.log(svc, f"bricks listing unavailable for {fname!r}; tractor fetch skipped")
            continue
        drel = str(brk.get("dest_rel") or "")
        pfile = builder.pack_dir(svc) / drel
        try:
            polys = json.loads(pfile.read_text(encoding="utf-8")).get("polys", [])
        except Exception as exc:  # noqa: BLE001
            builder.log(svc, f"bricks JSON parse failed {fname!r}: {type(exc).__name__}: {exc}")
            continue
        names = sorted(str(p["name"]) for p in polys if p.get("name"))
        if not names:
            builder.log(svc, f"no bricks listed for {fname!r} ({layer})")
            continue
        builder.log(svc, f"bricks in box {fname!r} ({layer}): {len(names)}; first: {', '.join(names[:4])}")
        portal_dr = f"https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/{drtag}"
        for brick in names[:2]:  # deterministic: lowest-named bricks in the box
            aaa = brick[:3]
            got = False
            for region in ("north", "south"):
                t_url = f"{portal_dr}/{region}/tractor/{aaa}/tractor-{brick}.fits"
                res = builder.try_fetch(
                    svc, f"tractor_{drtag}_{region}_{brick}",
                    url=t_url, dest_rel=f"tractor/{drtag}/{region}/{brick}.fits",
                    endpoint=f"{portal_dr} ({region}) tractor catalog (documented {drtag} layout)",
                    query=f"tractor-{brick}.fits for a brick overlapping the {fname} box",
                    license_="", extra={"field": fname, "brick": brick,
                                        "layer": layer,
                                        "region_candidates": ["north", "south"]},
                    size_hint=None, timeout_s=600.0,
                )
                if res and res.get("state") in ("local", "excluded"):
                    got = True
                    break
            if not got:
                builder.log(svc, f"tractor file for {brick!r} not found in either region")

    # image cutouts: g,r,z JPEG tricolor + r-band FITS per field, DR9 then DR10 fallback
    for field_avail in ("M44", "NGC 5139", "Pleiades"):
        c = resolve_name(field_avail)
        if not c:
            continue
        for layer in ("ls-dr9", "ls-dr10"):
            fits_url = (f"{_LS_BASE}/viewer/fits-cutout?ra={c[0]:.6f}&dec={c[1]:.6f}"
                        f"&pixscale=0.262&size=300&layer={layer}&bands=r")
            res = builder.try_fetch(
                svc, f"cutout_{slug(field_avail)}_r_{layer}",
                url=fits_url, dest_rel=f"cutouts/{slug(field_avail)}_r_{layer}.fits",
                endpoint="legacysurvey.org viewer fits-cutout",
                query=f"ra/dec from Sesame-resolved {field_avail}; pixscale 0.262 as; size 300 px; band r",
                license_="", extra={"field": field_avail, "layer": layer},
                timeout_s=300.0)
            if res and res.get("state") == "local":
                break  # one DR layer per field is enough for the pack
        jpeg_url = (f"{_LS_BASE}/viewer/jpeg-cutout?ra={c[0]:.6f}&dec={c[1]:.6f}"
                    f"&pixscale=0.262&size=300&layer=ls-dr9&bands=grz")
        builder.try_fetch(
            svc, f"cutout_{slug(field_avail)}_grz_jpeg_ls-dr9",
            url=jpeg_url, dest_rel=f"cutouts/{slug(field_avail)}_grz.jpeg",
            endpoint="legacysurvey.org viewer jpeg-cutout",
            query=f"ra/dec from Sesame-resolved {field_avail}; pixscale 0.262 as; 300 px; bands g,r,z",
            license_="", extra={"field": field_avail, "layer": "ls-dr9", "bands": "grz"})

    # unWISE cutouts (try documented unWISE layer names)
    c = resolve_name("M44")
    if c:
        for layer in ("unwise-neo7", "unwise-neo6", "unwise-dr9"):
            u_url = (f"{_LS_BASE}/viewer/fits-cutout?ra={c[0]:.6f}&dec={c[1]:.6f}"
                     f"&pixscale=2.75&size=100&layer={layer}&bands=1")
            res = builder.try_fetch(
                svc, f"unwise_cutout_{slug('M44')}_{layer}",
                url=u_url, dest_rel=f"cutouts/{slug('M44')}_{layer}_w1.fits",
                endpoint="legacysurvey.org viewer fits-cutout (unWISE layer)",
                query=f"ra/dec from Sesame-resolved M44; pixscale 2.75 as; 100 px; band 1; layer {layer}",
                license_="", extra={"field": "M44", "layer": layer})
            if res and res.get("state") in ("local", "excluded"):
                break


# --------------------------------------------------------------------------- CLI


COLLECTORS = {
    "mast": collect_mast,
    "gaia": collect_gaia,
    "skyview": collect_skyview,
    "cds": collect_cds,
    "ned": collect_ned,
    "eso": collect_eso,
    "irsa": collect_irsa,
    "legacysurvey": collect_legacysurvey,
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="cygnus.ingest.tier1",
                                 description="Build the Tier-1 provenance-logged data pack.")
    ap.add_argument("--services", default="all",
                    help="comma list to run (default: all); 'all' = SERVICE_ORDER")
    ap.add_argument("--budgets", default=None,
                    help="JSON per-service GiB override, e.g. '{\"mast\": 0.1}'")
    ap.add_argument("--ledger", default=None, help="override ledger DB path")
    ap.add_argument("--pack-root", default=None, help="override staging root (default scratch tier1_pack)")
    ap.add_argument("--pp", action="store_true", help="preview configuration and exit")
    args = ap.parse_args(argv)

    services = SERVICE_ORDER if args.services == "all" else [
        s.strip() for s in args.services.split(",") if s.strip()]
    for s in services:
        if s not in COLLECTORS:
            raise SystemExit(f"unknown service '{s}'; known: {', '.join(COLLECTORS)}")

    budgets = dict(DEFAULT_BUDGETS_GB)
    if args.budgets and args.budgets.strip() not in ("", "{}"):
        overrides = json.loads(args.budgets)
        for k, v in overrides.items():
            budgets[k] = float(v)

    payload = {
        "services": services,
        "budgets_gb": budgets,
        "field_names": FIELD_NAMES,
        "tess_target_names": TESS_TARGET_NAMES,
        "bench_object_names": BENCH_OBJECT_NAMES,
        "pack_dirs": PACK_DIRS,
        "versions": stack_versions(),
        "generated_utc": now_iso(),
    }
    if args.pp:
        print(json.dumps(payload, indent=1))
        return 0

    ledger = Ledger(args.ledger or ledger_path())
    builder = PackBuilder(ledger, budgets=budgets, dirmap=PACK_DIRS,
                          pack_root=Path(args.pack_root) if args.pack_root else None)
    run_id = ledger.log_run("cygnus.ingest.tier1", config_hash=builder.run_config_sha(payload))
    cfg_path = builder.root / "RUN_CONFIG.json"
    cfg_path.write_text(json.dumps({"run_id": run_id, **payload}, indent=1), encoding="utf-8")
    builder.log("run", f"run_id={run_id} config_hash={builder.run_config_sha(payload)}")

    for key in services:
        run_service(builder, key, COLLECTORS[key])
        builder.write_manifest(key)

    master = builder.write_master()
    search_log = builder.write_search_log()
    name_cache = write_name_cache(builder.root)
    prov = ledger_products_csv(ledger, builder.root / "PROVENANCE_ledger_products.csv")

    counts: dict[str, int] = {}
    for r in builder.all_rows():
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    summary = "; ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    # Ledger run statuses: completed|failed|aborted. Exclusions (budget/zero
    # results) are normal completed-run outcomes; they live in the manifest.
    n_failed_rows = counts.get("failed", 0)
    n_full = counts.get("local", 0) + counts.get("drive_only", 0)
    run_status = "failed" if n_failed_rows > n_full else "completed"
    ledger.close_run(run_id, run_status, summary)
    print(f"DONE states: {summary}")
    print(f"master manifest: {master}")
    print(f"search log: {search_log}")
    print(f"name resolutions: {name_cache}")
    print(f"ledger export: {prov}")
    ledger.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

