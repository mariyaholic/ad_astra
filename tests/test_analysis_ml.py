"""ML ranking controls: deterministic and deliberately not significance claims."""

import pytest

np = pytest.importorskip("numpy")
from cygnus.analysis.ml import rank_control_trained_anomalies


def test_control_trained_rank_is_repeatable_and_unchanged_inputs():
    x = np.array([[i / 100, (i % 3) / 100] for i in range(40)], dtype=float)
    y = np.array([[0.21, 0.01], [9.0, 9.0]], dtype=float)
    before = x.copy(), y.copy()
    kw = dict(feature_names=["dimensionless_a", "dimensionless_b"],
              control_ids=[f"control-{i}" for i in range(40)],
              target_ids=["normal", "extreme"], seed=7)
    first = rank_control_trained_anomalies(x, y, **kw)
    second = rank_control_trained_anomalies(x, y, **kw)
    assert first == second
    assert first.status == "inconclusive"
    assert first.ordered_ids == ("extreme", "normal")
    assert "Uncalibrated" in first.caveat
    assert np.array_equal(x, before[0]) and np.array_equal(y, before[1])


def test_no_overlapping_training_and_target_ids():
    x = np.arange(8, dtype=float).reshape(-1, 1)
    with pytest.raises(ValueError, match="overlap"):
        rank_control_trained_anomalies(x, [[1]], feature_names=["a"],
                                       control_ids=[str(i) for i in range(8)], target_ids=["1"])


@pytest.mark.parametrize("invalid", [np.nan, np.inf])
def test_nonfinite_features_are_not_silently_imputed(invalid):
    x = np.zeros((8, 1))
    y = np.array([[invalid]])
    with pytest.raises(ValueError, match="finite"):
        rank_control_trained_anomalies(x, y, feature_names=["a"],
                                       control_ids=[str(i) for i in range(8)], target_ids=["target"])
