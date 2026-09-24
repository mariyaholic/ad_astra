"""Deterministic ICRS toy catalog, not true archived sky positions."""

import pytest

from cygnus.analysis.crossmatch import Source, match_optical_infrared


def test_proper_motion_ra_wrap_uncertainty_color_quality():
    # 100 mas/yr over ten years crosses the RA 360-degree seam at dec=0.
    optical = Source("opt", 359.9999, 0, 2000, .1, 100, 0, 10, 18, True)
    infrared = Source("ir", (359.9999 + 1 / 3600) % 360, 0, 2010, .1,
                      magnitude=15, quality_ok=True)
    pair, = match_optical_infrared([optical], [infrared], radius_arcsec=.5,
                                   color_range=(2, 4))
    assert pair.separation_arcsec < 1e-8
    assert pair.combined_sigma_arcsec == pytest.approx((.1 ** 2 * 3) ** .5)
    assert pair.color_mag == 3
    assert pair.verdict == "consistent"


def test_missing_motion_uncertainty_photometry_or_quality_is_unknown():
    a = Source("opt", 10, 20, 2000, .1)
    b = Source("ir", 10, 20, 2010, .1, magnitude=15)
    pair, = match_optical_infrared([a], [b], radius_arcsec=1, color_range=(1, 2))
    assert pair.position_check == pair.color_check == pair.quality_check == "unknown"
    assert pair.verdict == "unknown"
    assert match_optical_infrared([a], [], radius_arcsec=1) == ()  # no match is not a physical upper limit


def test_inconsistent_color_quality_and_ambiguous_neighbor():
    a = Source("o", 10, 0, 2000, .1, magnitude=18, quality_ok=True)
    b = Source("i", 10, 0, 2000, .1, magnitude=15, quality_ok=False)
    pair, = match_optical_infrared([a], [b], radius_arcsec=1, color_range=(0, 1))
    assert pair.verdict == pair.color_check == pair.quality_check == "inconsistent"
    b2 = Source("j", 10.00001, 0, 2000, .1, magnitude=17, quality_ok=True)
    pair1, pair2 = match_optical_infrared([a], [b, b2], radius_arcsec=1, color_range=(0, 5))
    assert pair1.verdict == "inconsistent"  # quality failure cannot become a pass
    assert pair2.verdict == "unknown"  # otherwise plausible but ambiguous


def test_invalid_uncertainties_and_catalog_budget():
    with pytest.raises(ValueError):
        Source("bad", 10, 0, 2000, pm_ra_cosdec_masyr=100)
    with pytest.raises(ValueError):
        Source("bad", 10, 0, 2000, -1)
    with pytest.raises(ValueError, match="budget"):
        match_optical_infrared([Source("s", 10, 0, 2000)] * 10001, [], radius_arcsec=1)
    with pytest.raises(ValueError, match="baseline"):
        match_optical_infrared([Source("a", 10, 0, 1800)],
                               [Source("b", 10, 0, 2000)], radius_arcsec=1)
    with pytest.raises(ValueError, match="duplicate"):
        match_optical_infrared([Source("same", 10, 0, 2000)] * 2, [], radius_arcsec=1)
