"""Descriptive reduction-disagreement mining on aligned in-memory light curves.

No interpolation, detrending model, null calibration, or astrophysical classification
is performed. Values must already share a flux unit, time system and cadence grid.
A common signal in every reduction is invisible to this comparison. A large score
is a *ranking*, not a statistical significance or a false-alarm probability.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Disagreement:
    start_index: int
    stop_index: int  # exclusive; adjacent flagged cadences form one interval
    peak_index: int
    peak_time: float
    peak_spread: float
    rank_score: float
    reductions_at_peak: tuple[str, ...]
    status: str = "inconclusive"  # disagreement alone cannot identify its cause


@dataclass(frozen=True)
class DisagreementResult:
    status: str
    reason: str
    flux_unit: str
    time_unit: str
    time_scale: str
    usable_cadences: int
    excluded_cadences: int
    reference_spread: float | None
    candidates: tuple[Disagreement, ...]


def _numpy():
    try:
        import numpy as np
    except ImportError as exc:
        raise ImportError("cygnus.analysis requires optional NumPy; install numpy to run scientific diagnostics") from exc
    return np


def mine_reduction_disagreements(
    time, reductions: Mapping[str, object], *, flux_unit: str, time_unit: str,
    time_scale: str, mask=None, max_candidates: int = 10,
    max_cadences: int = 100_000,
) -> DisagreementResult:
    """Rank cadence groups by disagreement after removing each reduction's median.

    `mask` is a shared boolean include-mask (True keeps a cadence); nonfinite flux
    is excluded separately per reduction. At least two reductions must survive a
    cadence. The spread is max-minus-min of median-centered flux at that cadence.
    A reference spread (median of positive spreads) scales ranks; when all spreads
    are zero no candidates are returned. Adjacent positive-spread cadences are
    grouped, and at most `max_candidates` groups are retained. Max sizes bound
    memory and runtime; inputs are never modified. No automatic threshold is used.
    """
    np = _numpy()
    for key, value in (("flux_unit", flux_unit), ("time_unit", time_unit), ("time_scale", time_scale)):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key} must be a nonempty declared unit/system")
    if not isinstance(max_cadences, int) or isinstance(max_cadences, bool) or not 1 <= max_cadences <= 100_000:
        raise ValueError("max_cadences must be in 1..100000")
    if not isinstance(max_candidates, int) or isinstance(max_candidates, bool) or not 1 <= max_candidates <= 1000:
        raise ValueError("max_candidates must be in 1..1000")
    t = np.asarray(time, dtype=float)
    if t.ndim != 1 or not 2 <= t.size <= max_cadences or not np.all(np.isfinite(t)) or not np.all(np.diff(t) > 0):
        raise ValueError("time must be 1D, finite, strictly increasing, with 2..max_cadences elements")
    if not isinstance(reductions, Mapping) or not 2 <= len(reductions) <= 32:
        raise ValueError("provide 2..32 named aligned reductions")
    names = tuple(reductions)
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError("reduction names must be nonempty strings")
    if mask is None:
        included = np.ones(t.size, dtype=bool)
    else:
        included = np.asarray(mask)
        if included.shape != t.shape or included.dtype.kind != "b":
            raise ValueError("mask must be a boolean array matching time")
    curves = []
    for name in names:
        curve = np.asarray(reductions[name], dtype=float)
        if curve.shape != t.shape:
            raise ValueError(f"reduction {name!r} must match time shape")
        curves.append(curve)
    data = np.stack(curves)
    valid = np.isfinite(data) & included[None, :]
    # Center on each reduction's own valid cadences; never substitute missing data.
    centered = np.full(data.shape, np.nan)
    for j in range(len(names)):
        if np.any(valid[j]):
            centered[j, valid[j]] = data[j, valid[j]] - np.median(data[j, valid[j]])
    sufficient = np.sum(np.isfinite(centered), axis=0) >= 2
    usable = int(np.count_nonzero(sufficient))
    excluded = int(t.size - usable)
    if not usable:
        return DisagreementResult("not_tested", "no cadence has two usable reductions", flux_unit,
                                  time_unit, time_scale, 0, excluded, None, ())
    indices = np.flatnonzero(sufficient)
    spread = np.zeros(t.size)
    for i in indices:
        observed = centered[:, i]
        observed = observed[np.isfinite(observed)]
        spread[i] = float(np.max(observed) - np.min(observed))
    positives = spread[spread > 0]
    if not positives.size:
        return DisagreementResult("inconclusive", "no nonzero reduction disagreement", flux_unit,
                                  time_unit, time_scale, usable, excluded, 0.0, ())
    reference = float(np.median(positives))
    active = np.flatnonzero(spread > 0)
    groups = np.split(active, np.flatnonzero(np.diff(active) > 1) + 1)
    candidates = []
    for group in groups:
        peak = int(group[np.argmax(spread[group])])
        observed = centered[:, peak]
        present = np.flatnonzero(np.isfinite(observed))
        low = present[np.argmin(observed[present])]
        high = present[np.argmax(observed[present])]
        candidates.append(Disagreement(int(group[0]), int(group[-1]) + 1, peak,
                                       float(t[peak]), float(spread[peak]),
                                       float(spread[peak] / reference),
                                       (names[low], names[high])))
    candidates.sort(key=lambda c: (-c.rank_score, c.peak_index))
    return DisagreementResult("inconclusive", "descriptive ranking only; attribution and null calibration not tested",
                              flux_unit, time_unit, time_scale, usable, excluded,
                              reference, tuple(candidates[:max_candidates]))
