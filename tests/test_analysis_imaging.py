"""Deterministic, toy-pixel contracts; not survey false-positive calibration."""

import pytest

from cygnus.analysis.imaging import independent_band_consistency, triage_residual


def _cutout(band="g", location=(2, 2), mask_pixel=None):
    image = [[10.0] * 5 for _ in range(5)]
    image[location[0]][location[1]] = 18.0
    mask = [[False] * 5 for _ in range(5)]
    if mask_pixel is not None:
        mask[mask_pixel[0]][mask_pixel[1]] = True
    return triage_residual(image, [[8.0] * 5 for _ in range(5)],
                           [[1.0] * 5 for _ in range(5)], mask, band=band, threshold_sigma=5.0)


def test_median_sky_model_residual_and_feature():
    result = _cutout()
    assert result.background == 2
    assert result.tested_pixels == 25
    assert len(result.features) == 1
    feature = result.features[0]
    assert feature.pixels == ((2, 2),)
    assert feature.peak_sigma == 8
    assert feature.summed_residual == 8
    assert not feature.touches_edge
    assert "trials" in result.caveats[0]


def test_mask_and_edge_and_connected_feature():
    assert not _cutout(mask_pixel=(2, 2)).features
    image = [[0.0] * 4 for _ in range(4)]
    image[0][1] = image[1][1] = 8
    result = triage_residual(image, [[0.0] * 4 for _ in range(4)],
                             [[1.0] * 4 for _ in range(4)],
                             [[False] * 4 for _ in range(4)], band="r", threshold_sigma=5.0)
    assert result.features[0].pixels == ((0, 1), (1, 1))
    assert result.features[0].touches_edge


def test_independent_band_only_and_unknown():
    a, b = _cutout(), _cutout("r")
    assert independent_band_consistency(a, b, independent=True, radius_pixels=1) == "consistent"
    assert independent_band_consistency(a, b, independent=False, radius_pixels=1) == "unknown"
    assert independent_band_consistency(a, _cutout("g"), independent=True, radius_pixels=1) == "unknown"
    assert independent_band_consistency(a, _cutout("r", (0, 0)), independent=True, radius_pixels=1) == "inconsistent"
    assert independent_band_consistency(a, _cutout("r", mask_pixel=(2, 2)), independent=True, radius_pixels=1) == "unknown"


def test_numpy_boolean_mask_is_accepted_when_available():
    np = pytest.importorskip("numpy")
    image = np.zeros((5, 5))
    image[2, 2] = 9
    result = triage_residual(image, np.zeros_like(image), np.ones_like(image),
                             np.zeros(image.shape, dtype=bool), band="r", threshold_sigma=5.0)
    assert result.features[0].pixels == ((2, 2),)


def test_invalid_shapes_and_feature_budget_fail_loudly():
    with pytest.raises(ValueError, match="mismatched"):
        triage_residual([[1, 2]], [[1]], [[1, 1]], [[False, False]], band="g", threshold_sigma=5.0)
    with pytest.raises(ValueError, match="budget"):
        triage_residual([[8, 0, 8], [0, 0, 0], [8, 0, 8]], [[0] * 3] * 3,
                        [[1] * 3] * 3, [[False] * 3] * 3, band="g", threshold_sigma=5.0, max_features=1)
