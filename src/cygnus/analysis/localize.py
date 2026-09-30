"""Block-bootstrap significance for an event-minus-control centroid offset.

A centroid excursion at >= ``fail_ratio`` bootstrap sigma is a FAILED/unresolved localization even
when a coarse pixel-radius rule passes (AGENTS.md lead-promotion gate).
"""

from __future__ import annotations

import numpy as np

from .pixels import event_control_centroid


def _blocks(idx, length):
    idx = np.asarray(idx)
    return [idx[i:i + length] for i in range(0, len(idx), length) if len(idx[i:i + length]) == length] or [idx]


def block_bootstrap_offset(cube, event, control, aperture, background, *, flux_unit, block=5, draws=300,
                           seed=0, signal="dim", fail_ratio=3.0) -> dict:
    """Resample contiguous event/control cadence blocks with replacement; report offset / sigma."""
    cube = np.asarray(cube, float)
    ev = np.flatnonzero(np.asarray(event, bool)) if np.asarray(event).dtype == bool else np.asarray(event)
    co = np.flatnonzero(np.asarray(control, bool)) if np.asarray(control).dtype == bool else np.asarray(control)
    base = event_control_centroid(cube, event, control, aperture, background, flux_unit=flux_unit, signal=signal)
    if base.offset_xy is None:
        return {"state": "not_tested", "reason": base.reason}
    rng = np.random.default_rng(seed)
    eb, cb = _blocks(ev, block), _blocks(co, block)
    offs = []
    for _ in range(draws):
        e = np.concatenate([eb[i] for i in rng.integers(0, len(eb), len(eb))])
        c = np.concatenate([cb[i] for i in rng.integers(0, len(cb), len(cb))])
        me, mc = np.zeros(len(cube), bool), np.zeros(len(cube), bool)
        me[e], mc[c] = True, True
        m = event_control_centroid(cube, me, mc & ~me, aperture, background, flux_unit=flux_unit, signal=signal)
        if m.offset_xy is not None:
            offs.append(m.offset_xy)
    if len(offs) < 10:
        return {"state": "inconclusive", "reason": "too few valid bootstrap draws", "n_valid": len(offs)}
    sig = np.std(np.array(offs), axis=0, ddof=1)
    dist = float(base.offset_pixels)
    ratio = float(dist / max(np.hypot(*sig), 1e-12))
    return {"state": "failed_localization" if ratio >= fail_ratio else "inconclusive",
            "offset_pix": list(base.offset_xy), "distance_pix": dist, "bootstrap_sigma_pix": sig.tolist(),
            "offset_over_bootstrap_sigma": ratio, "n_valid": len(offs), "block": block,
            "note": "'passed' is never returned: this test cannot prove localization"}
