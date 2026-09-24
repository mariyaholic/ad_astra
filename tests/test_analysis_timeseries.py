"""Synthetic, offline ranking contracts; no astronomical significance calibration."""

import builtins

import pytest

from cygnus.analysis import mine_reduction_disagreements

np = pytest.importorskip("numpy")


PARAMS = dict(flux_unit="electron/s", time_unit="day", time_scale="BJD_TDB")


def test_isolated_reduction_disagreement_and_mask():
    t = np.arange(12, dtype=float)
    a = np.full(12, 100.0)
    b = a.copy()
    c = a.copy()
    b[4:6] -= 9
    c[9] += 3
    result = mine_reduction_disagreements(t, {"a": a, "b": b, "c": c}, **PARAMS)
    assert result.status == "inconclusive"
    assert result.usable_cadences == 12
    assert [(x.start_index, x.stop_index) for x in result.candidates] == [(4, 6), (9, 10)]
    assert result.candidates[0].reductions_at_peak == ("b", "a")
    assert result.candidates[0].peak_spread == 9
    assert result.candidates[0].rank_score > result.candidates[1].rank_score
    assert all(x.status == "inconclusive" for x in result.candidates)
    mask = np.ones(12, bool)
    mask[4:6] = False
    masked = mine_reduction_disagreements(t, {"a": a, "b": b, "c": c}, mask=mask, **PARAMS)
    assert masked.excluded_cadences == 2
    assert len(masked.candidates) == 1 and masked.candidates[0].peak_index == 9


def test_common_signal_not_misrepresented_as_disagreement():
    a = np.full(8, 100.0)
    a[3] = 70.0
    result = mine_reduction_disagreements(np.arange(8), {"x": a, "y": a + 17}, **PARAMS)
    assert result.status == "inconclusive" and result.candidates == ()
    assert result.reference_spread == 0


def test_missing_and_invalid_inputs():
    t = np.arange(5, dtype=float)
    a = np.arange(5, dtype=float)
    b = a.copy()
    a[1] = np.nan
    b[1] = np.nan
    result = mine_reduction_disagreements(t, {"a": a, "b": b}, **PARAMS)
    assert result.excluded_cadences == 1
    absent = mine_reduction_disagreements(t, {"a": a, "b": b}, mask=np.zeros(5, bool), **PARAMS)
    assert absent.status == "not_tested"
    assert absent.candidates == ()
    for bad_time in ([0, 1, 1, 2, 3], [0, 1, np.nan, 3, 4]):
        with pytest.raises(ValueError, match="time"):
            mine_reduction_disagreements(bad_time, {"a": a, "b": b}, **PARAMS)
    with pytest.raises(ValueError, match="shape"):
        mine_reduction_disagreements(t, {"a": a, "b": b[:4]}, **PARAMS)
    with pytest.raises(ValueError, match="mask"):
        mine_reduction_disagreements(t, {"a": a, "b": b}, mask=np.ones(5, int), **PARAMS)
    with pytest.raises(ValueError, match="flux_unit"):
        mine_reduction_disagreements(t, {"a": a, "b": b}, flux_unit="", time_unit="day", time_scale="UTC")
    with pytest.raises(ValueError, match="max_cadences"):
        mine_reduction_disagreements(t, {"a": a, "b": b}, max_cadences=4, **PARAMS)


def test_numpy_dependency_error_is_lazy(monkeypatch):
    real_import = builtins.__import__

    def block(name, *args, **kwargs):
        if name == "numpy":
            raise ImportError("mock missing numpy")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", block)
    with pytest.raises(ImportError, match="install numpy"):
        mine_reduction_disagreements([0, 1], {"a": [1, 2], "b": [1, 2]}, **PARAMS)
