import pytest

from cygnus.instruments import InstrumentUnknownError, get, require_psf_fwhm


def test_tess_profile_lookup():
    prof = get("TESS")
    assert prof.pixel_scale_as == pytest.approx(21.0)
    assert prof.cadence_s_default == pytest.approx(120.0)
    assert any("scattered light" in q for q in prof.quirks)


def test_kepler_profile_and_k2_alias():
    prof = get("Kepler")
    assert prof.pixel_scale_as == pytest.approx(3.98)
    assert get("K2") is prof


def test_unknown_instrument_is_loud():
    with pytest.raises(InstrumentUnknownError):
        get("VOYAGER_XYZ")


def test_no_universal_psf_cutoff_policy():
    # psf_fwhm_px is deliberately None for real instruments: threshold-based
    # artifact tests must pin a measured/library PSF per campaign.
    assert get("TESS").psf_fwhm_px is None
    with pytest.raises(RuntimeError, match="no pinned PSF FWHM"):
        require_psf_fwhm(get("TESS"))
