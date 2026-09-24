"""Read-only, checksum-gated adapters for a small Tier-1 reanalysis pilot.

This module never mounts Drive, downloads, writes to the pack, or interprets
an absent manifest row as an absence of a sky object. Use a *copied* local
product for analysis and retain the manifest's original product identifier.
"""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


SERVICE_DIRS = {
    "mast": "01_mast", "gaia": "02_gaia", "skyview": "03_skyview",
    "cds": "04_cds", "ned": "05_ned", "eso": "06_eso", "irsa": "07_irsa",
    "legacysurvey": "08_legacy_survey",
}


class PackIntegrityError(ValueError):
    """A source file cannot be safely matched to a manifest checksum."""


@dataclass(frozen=True)
class PackProduct:
    service: str
    product_id: str
    dest_rel: str
    state: str
    sha256: str
    bytes_expected: int | None


def read_manifest(path: str | Path) -> list[PackProduct]:
    """Parse the exported master CSV without trusting unchecked rows as files."""
    with Path(path).open("r", newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        required = {"service", "product_id", "dest_rel", "state", "sha256", "bytes"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise PackIntegrityError("manifest lacks required product columns")
        rows = []
        for line_no, row in enumerate(reader, 2):
            if not row or not row.get("service") or not row.get("product_id"):
                raise PackIntegrityError(f"malformed manifest row {line_no}")
            size = row.get("bytes", "") or ""
            try:
                parsed_size = int(size) if size.strip() else None
            except ValueError as exc:
                raise PackIntegrityError(f"invalid byte count at row {line_no}") from exc
            if parsed_size is not None and parsed_size < 0:
                raise PackIntegrityError(f"negative byte count at row {line_no}")
            rows.append(PackProduct(
                service=row["service"], product_id=row["product_id"],
                dest_rel=row.get("dest_rel", "") or "", state=row["state"],
                sha256=row.get("sha256", "") or "", bytes_expected=parsed_size,
            ))
        return rows


def checked_product_path(pack_root: str | Path, product: PackProduct) -> Path:
    """Resolve and hash an existing product, rejecting traversal and absent hashes.

    `pack_root` is the Tier-1 root as seen in Colab or a copied local pack. No
    directories are made and nothing is modified. Older manifest rows without
    recorded byte lengths remain usable when their SHA-256 is present.
    """
    if product.service not in SERVICE_DIRS:
        raise PackIntegrityError("unrecognized pack service")
    if product.state not in {"local", "drive_only"}:
        raise PackIntegrityError("manifest row is not a retained product")
    digest = product.sha256.lower()
    if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
        raise PackIntegrityError("product has no valid SHA-256; cannot validate it")
    rel = product.dest_rel
    parts = PurePosixPath(rel).parts
    if (not rel or "\\" in rel or ":" in rel or rel.startswith("/")
            or any(p in {".", ".."} for p in rel.split("/"))
            or not parts or any(p == "" for p in rel.split("/"))):
        raise PackIntegrityError("unsafe product-relative path")
    root = (Path(pack_root) / SERVICE_DIRS[product.service]).resolve()
    path = root.joinpath(*parts).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise PackIntegrityError("product missing or outside service directory")
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            size += len(block)
            h.update(block)
    if h.hexdigest() != digest or (product.bytes_expected is not None and size != product.bytes_expected):
        raise PackIntegrityError("product checksum or byte count mismatch")
    return path


def read_spoc_lightcurve(path: str | Path) -> dict[str, Any]:
    """Copy SPOC TIME, QUALITY, SAP_FLUX and PDCSAP_FLUX from a FITS table.

    Return FITS timing keywords *as recorded*; no conversion to BJD or claim
    about cadence/time standard is made. Installation: ``cygnus[analysis]``.
    """
    try:
        import numpy as np
        from astropy.io import fits
    except ImportError as exc:
        raise RuntimeError("FITS analysis needs the cygnus[analysis] optional extra") from exc
    with fits.open(path, memmap=True) as hdus:
        if len(hdus) < 2 or hdus[1].data is None:
            raise PackIntegrityError("FITS product has no light-curve table")
        table = hdus[1].data
        names = set(table.names or ())
        required = {"TIME", "QUALITY", "SAP_FLUX", "PDCSAP_FLUX"}
        if not required.issubset(names):
            raise PackIntegrityError("FITS light curve lacks required columns")
        output = {key.lower(): np.asarray(table[key]).copy() for key in sorted(required)}
        hdr = hdus[1].header
        primary = hdus[0].header
        output["timing"] = {key: hdr.get(key, primary.get(key)) for key in
                            ("TIMESYS", "BJDREFI", "BJDREFF", "TIMEUNIT", "TIMEDEL")}
        output["identity"] = {key: primary.get(key) for key in
                              ("TICID", "SECTOR", "CAMERA", "CCD")}
        return output


def read_tesscut_window(path: str | Path, *, start: int, stop: int,
                        max_elements: int = 2_000_000) -> dict[str, Any]:
    """Copy a bounded cadence window from a TESScut FLUX cube in FITS.

    The caller must inspect time standard/quality and select event/control
    windows independently; no automatic brightening, transit or centroid claim.
    Only the requested window is copied from the FITS table. Returned pixel
    coordinates are detector-cutout row/column, not celestial coordinates.
    """
    try:
        import numpy as np
        from astropy.io import fits
    except ImportError as exc:
        raise RuntimeError("TESScut analysis needs the cygnus[analysis] optional extra") from exc
    if (not isinstance(start, int) or isinstance(start, bool)
            or not isinstance(stop, int) or isinstance(stop, bool)
            or not isinstance(max_elements, int) or max_elements < 1 or start < 0 or stop <= start):
        raise ValueError("provide a positive bounded cadence window and max_elements")
    with fits.open(path, memmap=True) as hdus:
        if len(hdus) < 2 or hdus[1].data is None:
            raise PackIntegrityError("TESScut FITS has no cadence table")
        table = hdus[1].data
        if not {"TIME", "QUALITY", "FLUX"}.issubset(set(table.names or ())):
            raise PackIntegrityError("TESScut FITS lacks TIME, QUALITY or FLUX")
        if stop > len(table):
            raise ValueError("cadence window exceeds TESScut length")
        shape = table["FLUX"].shape
        if len(shape) != 3 or (stop - start) * shape[1] * shape[2] > max_elements:
            raise ValueError("window exceeds pixel budget or FLUX is not a cube")
        return {
            "time": np.asarray(table["TIME"][start:stop], dtype=float).copy(),
            "quality": np.asarray(table["QUALITY"][start:stop]).copy(),
            "flux": np.asarray(table["FLUX"][start:stop], dtype=float).copy(),
            "timing": {key: hdus[1].header.get(key, hdus[0].header.get(key)) for key in
                       ("TIMESYS", "BJDREFI", "BJDREFF", "TIMEUNIT", "TIMEDEL")},
            "identity": {key: hdus[0].header.get(key) for key in
                         ("SECTOR", "CAMERA", "CCD")},
        }
