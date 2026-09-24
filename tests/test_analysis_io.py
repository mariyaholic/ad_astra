"""Manifest-driven read-only product access; no network or Drive calls."""

import csv
import hashlib
from pathlib import Path

import pytest

from cygnus.analysis.io import (PackIntegrityError, PackProduct,
                                checked_product_path, read_manifest)


def _product(**overrides):
    fields = dict(service="mast", product_id="toy", dest_rel="lc/toy.fits",
                  state="drive_only", sha256=hashlib.sha256(b"toy").hexdigest(),
                  bytes_expected=3)
    fields.update(overrides)
    return PackProduct(**fields)


def test_manifest_reads_retained_and_excluded_rows(tmp_path):
    path = tmp_path / "MASTER_MANIFEST.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["service", "product_id", "dest_rel", "state", "sha256", "bytes"])
        writer.writeheader()
        writer.writerow(dict(service="mast", product_id="p", dest_rel="x", state="drive_only",
                             sha256="a" * 64, bytes=""))
        writer.writerow(dict(service="mast", product_id="probe", dest_rel="", state="excluded",
                             sha256="", bytes=""))
    products = read_manifest(path)
    assert [(p.product_id, p.bytes_expected, p.state) for p in products] == [
        ("p", None, "drive_only"), ("probe", None, "excluded")]


def test_product_verified_without_mutation(tmp_path):
    target = tmp_path / "01_mast" / "lc" / "toy.fits"
    target.parent.mkdir(parents=True)
    target.write_bytes(b"toy")
    assert checked_product_path(tmp_path, _product()) == target
    assert target.read_bytes() == b"toy"
    with pytest.raises(PackIntegrityError, match="checksum"):
        checked_product_path(tmp_path, _product(sha256="0" * 64))
    assert target.read_bytes() == b"toy"


@pytest.mark.parametrize("relative", ["../escape", "lc/../../escape", "/etc/passwd",
                                       "C:/escape", r"..\escape", "lc//toy.fits"])
def test_unsafe_manifest_paths_never_read_outside(tmp_path, relative):
    outside = tmp_path / "escape"
    outside.write_bytes(b"toy")
    with pytest.raises(PackIntegrityError):
        checked_product_path(tmp_path / "pack", _product(dest_rel=relative))
    assert outside.read_bytes() == b"toy"


def test_symlink_escape_rejected_where_supported(tmp_path):
    outside = tmp_path / "outside"
    outside.write_bytes(b"toy")
    parent = tmp_path / "01_mast" / "lc"
    parent.mkdir(parents=True)
    try:
        (parent / "toy.fits").symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks unavailable")
    with pytest.raises(PackIntegrityError, match="outside"):
        checked_product_path(tmp_path, _product())


def test_missing_hash_and_non_product_are_not_passed(tmp_path):
    with pytest.raises(PackIntegrityError, match="SHA-256"):
        checked_product_path(tmp_path, _product(sha256=""))
    with pytest.raises(PackIntegrityError, match="not a retained"):
        checked_product_path(tmp_path, _product(state="excluded"))


def test_lightcurve_reader_has_explicit_optional_dependency(tmp_path):
    pytest.importorskip("astropy")
    import numpy as np
    from astropy.io import fits
    from cygnus.analysis.io import read_spoc_lightcurve
    hdu = fits.BinTableHDU.from_columns([
        fits.Column(name="TIME", format="D", array=np.array([1.0, 2.0])),
        fits.Column(name="QUALITY", format="J", array=np.array([0, 1])),
        fits.Column(name="SAP_FLUX", format="D", array=np.array([5.0, 6.0])),
        fits.Column(name="PDCSAP_FLUX", format="D", array=np.array([4.0, 5.0])),
    ])
    hdu.header["TIMESYS"] = "TDB"
    path = tmp_path / "lc.fits"
    fits.HDUList([fits.PrimaryHDU(), hdu]).writeto(path)
    result = read_spoc_lightcurve(path)
    assert result["timing"]["TIMESYS"] == "TDB"
    assert result["quality"].tolist() == [0, 1]
    assert result["pdcsap_flux"].tolist() == [4.0, 5.0]


def test_tesscut_window_is_bounded_and_retains_quality(tmp_path):
    pytest.importorskip("astropy")
    import numpy as np
    from astropy.io import fits
    from cygnus.analysis.io import read_tesscut_window
    cube = np.arange(36, dtype=float).reshape(4, 3, 3)
    hdu = fits.BinTableHDU.from_columns([
        fits.Column(name="TIME", format="D", array=np.arange(4, dtype=float)),
        fits.Column(name="QUALITY", format="J", array=np.array([0, 1, 0, 0])),
        fits.Column(name="FLUX", format="9D", dim="(3,3)", array=cube),
    ])
    hdu.header["TIMESYS"] = "TDB"
    path = tmp_path / "cutout.fits"
    fits.HDUList([fits.PrimaryHDU(), hdu]).writeto(path)
    window = read_tesscut_window(path, start=1, stop=3, max_elements=18)
    assert window["flux"].shape == (2, 3, 3)
    assert window["flux"][0].tolist() == cube[1].tolist()
    assert window["quality"].tolist() == [1, 0]
    assert window["timing"]["TIMESYS"] == "TDB"
    with pytest.raises(ValueError, match="budget"):
        read_tesscut_window(path, start=0, stop=4, max_elements=18)
