"""Small deterministic counterfactual and centroid tests, no survey data."""

import pytest

from cygnus.analysis import aperture_counterfactuals, event_control_centroid

np = pytest.importorskip("numpy")


def masks():
    ap = np.zeros((3, 3), bool)
    ap[1, 1] = True
    wide = ap.copy()
    wide[1, 2] = True
    bg = np.zeros((3, 3), bool)
    bg[0, :] = True
    alternate_bg = np.zeros((3, 3), bool)
    alternate_bg[2, :] = True
    return ap, wide, bg, alternate_bg


def test_aperture_and_background_counterfactuals():
    ap, wide, bg, other_bg = masks()
    cube = np.full((3, 3, 3), 2.0)
    cube[:, 1, 1] = [12, 10, 12]
    cube[:, 1, 2] = [7, 7, 7]
    cube[:, 2, :] = 3.0
    original = cube.copy()
    result = aperture_counterfactuals(cube, [1, 2, 3], {"core": ap, "wide": wide},
                                       {"sky": bg, "other": other_bg}, flux_unit="e-/s",
                                       time_unit="day", time_scale="BJD_TDB")
    lookup = {(an, bn): label for label, an, bn in result.choices}
    assert result.flux_by_choice[lookup["core", "sky"]] == (10.0, 8.0, 10.0)
    assert result.flux_by_choice[lookup["wide", "sky"]] == (15.0, 13.0, 15.0)
    assert result.flux_by_choice[lookup["core", "other"]] == (9.0, 7.0, 9.0)
    assert np.array_equal(cube, original)
    assert result.status == "inconclusive"
    pixel_mask = np.ones(cube.shape, bool)
    pixel_mask[1, :, :] = False
    missing = aperture_counterfactuals(cube, [1, 2, 3], {"core": ap}, {"sky": bg},
                                        pixel_mask=pixel_mask, flux_unit="e-/s",
                                        time_unit="day", time_scale="UTC")
    label = missing.choices[0][0]
    assert missing.flux_by_choice[label] == (10.0, None, 10.0)
    assert missing.valid_by_choice[label] == (True, False, True)


def test_centroid_deficit_and_no_claim_of_detection():
    _, ap, bg, _ = masks()
    cube = np.zeros((4, 3, 3), float)
    cube[:, 1, 1] = 10
    cube[:, 1, 2] = [5, 5, 1, 1]
    result = event_control_centroid(cube, [False, False, True, True], [True, True, False, False],
                                    ap, bg, flux_unit="e-/s")
    assert result.status == "inconclusive"
    assert result.event_count == 2 and result.control_count == 2
    assert result.residual_xy == pytest.approx((2, 1))
    assert result.control_xy == pytest.approx((4 / 3, 1))
    assert result.offset_xy == pytest.approx((2 / 3, 0))
    assert result.offset_pixels == pytest.approx(2 / 3)
    no_event = event_control_centroid(cube, [False] * 4, [True] * 4, ap, bg, flux_unit="e-/s")
    assert no_event.status == "not_tested" and no_event.offset_pixels is None
    same = event_control_centroid(cube[:2], [True, False], [False, True], ap, bg, flux_unit="e-/s")
    assert same.status == "inconclusive" and same.residual_xy is None


def test_bright_residual_with_background_shift():
    _, ap, bg, _ = masks()
    cube = np.zeros((2, 3, 3))
    cube[0] += 3
    cube[1] += 8
    cube[:, 1, 1] += 10
    cube[1, 1, 2] += 4
    result = event_control_centroid(cube, [False, True], [True, False], ap, bg,
                                    signal="bright", flux_unit="count")
    assert result.residual_xy == pytest.approx((2, 1))
    assert result.offset_pixels == pytest.approx(1)
    assert result.status == "inconclusive"


def test_validation_and_missing_pixels():
    ap, wide, bg, _ = masks()
    cube = np.ones((2, 3, 3))
    kwargs = dict(flux_unit="count", time_unit="second", time_scale="UTC")
    with pytest.raises(ValueError, match="overlaps"):
        aperture_counterfactuals(cube, [0, 1], {"a": wide}, {"b": wide}, **kwargs)
    with pytest.raises(ValueError, match="time"):
        aperture_counterfactuals(cube, [1, 0], {"a": ap}, {"b": bg}, **kwargs)
    with pytest.raises(ValueError, match="pixel_mask"):
        aperture_counterfactuals(cube, [0, 1], {"a": ap}, {"b": bg}, pixel_mask=np.ones((3, 3), bool), **kwargs)
    with pytest.raises(ValueError, match="max_pixels"):
        aperture_counterfactuals(cube, [0, 1], {"a": ap}, {"b": bg}, max_pixels=2, **kwargs)
    with pytest.raises(ValueError, match="disjoint"):
        event_control_centroid(cube, [True, False], [True, False], ap, bg, flux_unit="count")
    with pytest.raises(ValueError, match="signal"):
        event_control_centroid(cube, [True, False], [False, True], ap, bg, signal="unknown", flux_unit="count")
    cube[:, 1, 1] = np.nan
    result = event_control_centroid(cube, [True, False], [False, True], ap, bg, flux_unit="count")
    assert result.status == "inconclusive" and result.offset_xy is None
    all_masked = aperture_counterfactuals(cube, [0, 1], {"a": ap}, {"b": bg},
                                           pixel_mask=np.zeros(cube.shape, bool), **kwargs)
    assert all_masked.status == "not_tested"
