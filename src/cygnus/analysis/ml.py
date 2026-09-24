"""Bounded control-trained nearest-neighbor anomaly ranking (NumPy only).

This unsupervised ranking is not a detection, calibrated probability or novelty
classifier. Caller must keep controls independent by source/field/epoch and use
scientifically comparable, documented features. Do not fit on candidate data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class AnomalyRanking:
    target_ids: tuple[str, ...]
    scores: tuple[float, ...]
    ordered_ids: tuple[str, ...]
    feature_names: tuple[str, ...]
    seed: int
    status: str = "inconclusive"
    caveat: str = "Uncalibrated ML priority only; artifacts, selection and prior art not tested"


def rank_control_trained_anomalies(
    control_features, target_features, *, feature_names: Sequence[str],
    control_ids: Sequence[str], target_ids: Sequence[str], seed: int = 0,
) -> AnomalyRanking:
    """Rank nearest-control distances, high first; controls alone define scale.

    Standardize by the controls' robust median and MAD. Constant control
    dimensions use unit scale, explicitly not a probabilistic uncertainty. This
    descriptive k=1 novelty ranking is intentionally small and CPU-only.
    `seed` is recorded for compatible campaign records, though this particular
    deterministic method uses no RNG. Independent controls remain caller's duty.
    """
    try:
        import numpy as np
    except ImportError as exc:
        raise RuntimeError("ML ranking requires the cygnus[analysis] NumPy extra") from exc
    x = np.asarray(control_features, dtype=float)
    y = np.asarray(target_features, dtype=float)
    if x.ndim != 2 or y.ndim != 2 or not 8 <= len(x) <= 1_000 or not 1 <= len(y) <= 1_000:
        raise ValueError("provide 8..1000 controls and 1..1000 targets as 2D arrays")
    if not 1 <= x.shape[1] <= 64 or x.shape[1] != y.shape[1]:
        raise ValueError("control and target feature dimensions must match (1..64)")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("all features must be finite; record missing measurements separately")
    names, controls, targets = tuple(feature_names), tuple(control_ids), tuple(target_ids)
    if (len(names) != x.shape[1] or len(set(names)) != len(names)
            or not all(isinstance(s, str) and s.strip() for s in names)
            or len(controls) != len(x) or len(targets) != len(y)
            or any(not isinstance(s, str) or not s.strip() for s in controls + targets)
            or len(set(controls)) != len(controls) or len(set(targets)) != len(targets)):
        raise ValueError("feature names and control/target identifiers must be complete and unique")
    if set(controls) & set(targets):
        raise ValueError("control and target identifiers overlap; avoid direct training leakage")
    if not isinstance(seed, int) or isinstance(seed, bool) or seed < 0 or seed > 2**32 - 1:
        raise ValueError("seed must be a nonnegative 32-bit integer")
    center = np.median(x, axis=0)
    mad = 1.4826 * np.median(np.abs(x - center), axis=0)
    scale = np.where(mad > 0, mad, 1.0)
    reference = (x - center) / scale
    target = (y - center) / scale
    # Process one candidate at a time; no N_control x N_target distance matrix.
    scores = tuple(float(np.min(np.linalg.norm(reference - row, axis=1))) for row in target)
    ordering = tuple(targets[i] for i in sorted(range(len(targets)), key=lambda i: (-scores[i], targets[i])))
    return AnomalyRanking(targets, scores, ordering, names, seed)
