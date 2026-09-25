"""MAST client tests — live-network smoke runs explicitly (-m network).

Sentinel: nothing in the layer's unit suite touches the network.
"""

import pytest

from cygnus.ingest import mast
from cygnus.ledger import Ledger


def _corners_clause(ra_deg, dec_deg):
    # pi Men: RA 14:39, Dec -80:31 (southern continuous view; SPOC/LC rich)
    return ra_deg, dec_deg


def test_dependency_error_is_explained(tmp_path):
    """If the optional stack is absent we say exactly what to install."""
    try:
        Observations, Tesscut = mast._astroquery_mast()
    except mast.DependencyError as exc:
        assert "cygnus[mast]" in str(exc)
        pytest.skip(f"optional stack not installed: {exc}")
    else:
        assert Observations is not None and Tesscut is not None


@pytest.mark.network
def test_tesscut_live_roundtrip(tmp_path, tmp_scratch):
    try:
        mast._astroquery_mast()
    except mast.DependencyError as exc:
        pytest.skip(f"optional stack not installed: {exc}")

    led = Ledger(tmp_path / "net.sqlite")
    try:
        # Sector=None resolves live from get_sectors (teaches nothing assumed).
        paths = mast.download_tesscut(
            ra_deg=219.757,
            dec_deg=-80.531,  # pi Men region
            ledger=led,
            size_px=5,
        )
        assert len(paths) >= 1
        for p in paths:
            assert p.exists() and p.stat().st_size > 0, f"empty cutout: {p}"
        assert led.count_products("MAST") >= 1
        row = led.products("MAST")[0]
        assert row["checksum"] and len(row["checksum"]) == 64

        from astropy.io import fits

        with fits.open(paths[0]) as hdul:
            assert "SECTOR" in hdul[0].header
            assert hdul[1].data is not None and len(hdul[1].data) > 0
    finally:
        led.close()


@pytest.mark.network
def test_tesscut_wrong_sector_raises_loudly(tmp_path, tmp_scratch):
    try:
        mast._astroquery_mast()
    except mast.DependencyError as exc:
        pytest.skip(f"optional stack not installed: {exc}")

    led = Ledger(tmp_path / "net.sqlite")
    try:
        with pytest.raises(ValueError, match="available sectors"):
            mast.download_tesscut(
                ra_deg=219.757,
                dec_deg=-80.531,
                ledger=led,
                size_px=5,
                sector=1,  # does not cover this position (verified live vs get_sectors)
            )
        assert led.count_products("MAST") == 0
    finally:
        led.close()
