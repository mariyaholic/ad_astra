"""MAST client: search + idempotent downloads into scratch, ledgered.

Heavy imports (astroquery/astropy) happen inside function bodies; see
``pyproject.toml`` extras ``cygnus[mast]``. Every product is checksummed and
registered in the ledger with its retrieval timestamp — AGENTS.md provenance
rules. Downloads land in the scratch tree only.
"""

from __future__ import annotations

import logging
from pathlib import Path

from ..ledger import Ledger, file_sha256
from .scratch import resolve_scratch

logger = logging.getLogger(__name__)

_TESSCUT_URL = "https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html"


class DependencyError(RuntimeError):
    """Raised when the optional science stack is not installed."""


def _astroquery_mast():
    try:  # pragma: no cover - exercised only in network smoke tests
        from astroquery.mast import Observations, Tesscut  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise DependencyError(
            "astroquery/MAST unavailable — install extras: "
            "pip install 'cygnus[mast]' (astroquery + astropy)"
        ) from exc
    return Observations, Tesscut


def search_and_download_lightcurves(
    target_name: str,
    *,
    ledger: Ledger,
    mission: str = "TESS",
    dataproduct_type: str = "timeseries",
    product_subgroup: str = "LC",
    limit: int = 5,
    download_dir: str | Path | None = None,
) -> dict[str, str]:
    """Search SPOC light-curve products for ``target_name`` and cache them.

    Returns a mapping ``product_id -> local path``. Requires the MAST extras.
    Downloads are idempotent: products are re-registered in the ledger with
    fresh checksums rather than re-fetched blindly.
    """
    Observations, _ = _astroquery_mast()

    dest = Path(download_dir) if download_dir is not None else resolve_scratch("mast") / (
        "lc_" + mission.lower() + "_" + target_name.strip().replace(" ", "_").lower()
    )
    dest.mkdir(parents=True, exist_ok=True)

    obs_table = Observations.query_criteria(
        target_name=target_name,
        dataproduct_type=dataproduct_type,
        obs_collection=mission,
    )
    if len(obs_table) == 0:
        logger.warning("MAST: no %s observations match %r", mission, target_name)
        return {}

    products = Observations.get_product_list(obs_table)
    picked = Observations.filter_products(
        products, productSubGroupDescription=product_subgroup
    )
    if len(picked) == 0:
        logger.warning("MAST: no products with subgroup %r for %r", product_subgroup, target_name)
        return {}

    local_table = Observations.download_products(picked[:limit], download_dir=str(dest))

    out: dict[str, str] = {}
    for row in local_table:
        cols = row.colnames
        path_value = None
        for col in ("Local Path", "local_path"):
            if col in cols:
                path_value = str(row[col])
                break
        if not path_value:
            logger.warning("MAST: download row without 'Local Path' column: %s", cols)
            continue
        p = Path(path_value)
        if not p.exists():
            logger.warning("MAST: download reported but file missing: %s", p)
            continue
        pid = p.name
        for col in ("Product Name", "productFilename", "obsID"):
            if col in cols and str(row[col]).strip() and pid == p.name:
                pid = str(row[col])
                break
        ledger.add_product(
            archive="MAST",
            product_id=pid,
            url=str(row["Local URL"]) if "Local URL" in cols else None,
            local_path=p,
            checksum=file_sha256(p),
            license_="public MAST",
        )
        out[pid] = str(p)
    return out


def download_tesscut(
    ra_deg: float,
    dec_deg: float,
    *,
    ledger: Ledger,
    size_px: int = 5,
    sector: int | None = None,
    product: str = "SPOC",
) -> list[Path]:
    """Download TESS cutouts at (ra, dec) via astroquery Tesscut.

    Returns the local FITS paths, one per requested sector; every cutout is
    checksummed and ledgered. With ``sector=None`` the earliest sector covering
    the coordinates is used (resolved live — never assumed). A requested sector
    that does not cover the position raises loudly instead of returning nothing.
    """
    _, Tesscut = _astroquery_mast()
    from astropy.coordinates import SkyCoord  # local import: heavy stack

    import astropy.units as u

    coord = SkyCoord(ra_deg * u.deg, dec_deg * u.deg, frame="icrs")
    sectors_table = Tesscut.get_sectors(coordinates=coord)
    if sectors_table is None or len(sectors_table) == 0:
        logger.warning("MAST Tesscut: no sectors cover (ra=%s, dec=%s)", ra_deg, dec_deg)
        return []
    available = sorted(int(s) for s in sectors_table["sector"])
    if sector is None:
        sector = available[0]
    elif int(sector) not in available:
        raise ValueError(
            f"sector {sector} does not cover (ra={ra_deg}, dec={dec_deg}); "
            f"available sectors: {available}"
        )
    hduls = Tesscut.get_cutouts(
        coordinates=coord, size=size_px, product=product, sector=sector
    )

    out_dir = resolve_scratch("mast") / "tesscut"
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for hdul in hduls:
        header = hdul[0].header
        sector_id = header.get("SECTOR", "unknown")
        camera = header.get("CAMERA", "?")
        ccd = header.get("CCD", "?")
        out = out_dir / f"tesscut_{ra_deg:.4f}_{dec_deg:+.4f}_sec{sector_id}.fits"
        hdul.writeto(out, overwrite=True)
        ledger.add_product(
            archive="MAST",
            product_id=f"tesscut-{ra_deg:.4f}-{dec_deg:+.4f}-sec{sector_id}-cam{camera}-ccd{ccd}",
            url=_TESSCUT_URL,
            local_path=out,
            checksum=file_sha256(out),
            license_="public MAST",
        )
        paths.append(out)
    return paths
