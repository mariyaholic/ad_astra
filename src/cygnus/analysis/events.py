"""Predicted-epoch event measurement, null/injection counts and alias coverage classification."""

from __future__ import annotations

import numpy as np


def box_measure(t, y, mid, duration, degree, *, half_window=0.75, min_coverage=0.8,
                exposure=None, min_points=4, min_flank=10) -> dict:
    """Joint polynomial + box fit at a predicted epoch (days). Positive depth = dimming.

    Returns state ``uncovered`` (not a null), ``invalid_baseline`` or ``measured``. ``exposure``
    integrates the box over each exposure for coarse cadence. Nothing is interpolated across gaps.
    """
    t, y = np.asarray(t, float), np.asarray(y, float)
    ok = np.isfinite(t) & np.isfinite(y)
    t, y = t[ok], y[ok]
    cadence = float(np.median(np.diff(np.sort(t)))) if len(t) > 1 else np.inf
    x = t - mid
    loc = np.abs(x) <= half_window
    x, yy = x[loc], y[loc]
    w = (np.abs(x) <= duration / 2).astype(float)
    if exposure is not None:
        w = np.clip(np.minimum(x + exposure / 2, duration / 2) - np.maximum(x - exposure / 2, -duration / 2),
                    0, exposure) / exposure
    ev = w > 0
    cov = float(w.sum() / (duration / cadence)) if np.isfinite(cadence) and cadence > 0 else 0.0
    if cov < min_coverage or ev.sum() < min_points or (x < -duration / 2).sum() < min_flank \
            or (x > duration / 2).sum() < min_flank:
        return {"state": "uncovered", "coverage": cov, "n_event": int(ev.sum())}
    A = np.column_stack([x**i for i in range(degree + 1)] + [-w])
    c, *_ = np.linalg.lstsq(A, yy, rcond=None)
    if c[0] <= 0:
        return {"state": "invalid_baseline", "coverage": cov}
    r = yy - A @ c
    return {"state": "measured", "depth_ppm": float(c[-1] / c[0] * 1e6), "coverage": cov,
            "n_event": int(ev.sum()), "n_flank": int((~ev).sum()),
            "residual_rms_ppm": float(np.std(r) / c[0] * 1e6)}


def null_exceedance(t, y, duration, degree, depth_ppm, *, centres, half_window=0.75, **kw) -> dict:
    """Empirical null: box depth at event-free ``centres``. Counts, never a Gaussian sigma.

    k of N covered nulls with depth >= ``depth_ppm``; uncovered centres are excluded from N.
    """
    centres = list(centres)
    covered = [m for m in (box_measure(t, y, c, duration, degree, half_window=half_window, **kw)
                           for c in centres) if m["state"] == "measured"]
    k = sum(1 for m in covered if m["depth_ppm"] >= depth_ppm)
    return {"n_drawn": len(centres), "n_covered": len(covered), "n_exceed": k,
            "resolution": (1.0 / len(covered)) if covered else None,
            "note": "k/N with finite resolution; 0/N is not zero probability"}


def injection_recovery(t, y, duration, degree, depth_ppm, *, epochs, half_window=0.75, frac=0.5, **kw) -> dict:
    """Inject a multiplicative box at each epoch; count recoveries >= frac*depth among covered epochs."""
    t, y = np.asarray(t, float), np.asarray(y, float)
    rec = n = 0
    for e in epochs:
        yi = y * np.where(np.abs(t - e) <= duration / 2, 1 - depth_ppm * 1e-6, 1.0)
        m = box_measure(t, yi, e, duration, degree, half_window=half_window, **kw)
        if m["state"] == "measured":
            n += 1
            rec += m["depth_ppm"] >= frac * depth_ppm
    return {"n_covered": n, "n_recovered": int(rec), "note": "uncovered epochs excluded, not counted as misses"}


def classify_aliases(aliases, windows, t, y, duration, degree, depth_ppm, *, epoch0, **kw) -> list[dict]:
    """Per period alias: predicted epochs on new data, each present / absent / uncovered.

    ``excluded`` only if a predicted window is covered and shows no dip; if every predicted window
    is uncovered the alias stays ``untested``. ``windows`` = [(tmin, tmax)] of usable data.
    """
    out = []
    lo, hi = min(a for a, _ in windows), max(b for _, b in windows)
    for P in aliases:
        rows = []
        for n in range(int(np.ceil((lo - epoch0) / P)), int(np.floor((hi - epoch0) / P)) + 1):
            mid = epoch0 + n * P
            m = box_measure(t, y, mid, duration, degree, **kw)
            if m["state"] != "measured":
                rows.append({"epoch": mid, "result": "uncovered"})
            else:
                rows.append({"epoch": mid, "depth_ppm": m["depth_ppm"],
                             "result": "present" if m["depth_ppm"] >= 0.5 * depth_ppm else "absent"})
        res = {r["result"] for r in rows}
        status = "present" if "present" in res else "excluded" if "absent" in res else "untested"
        out.append({"period_days": P, "status": status, "predicted": rows})
    return out


def null_verdict(k: int, n: int, *, min_n: int = 100, max_frac: float = 0.05) -> dict:
    """State for an empirical null exceedance k/N (never a Gaussian sigma or p=0).

    ``inconclusive`` if fewer than ``min_n`` covered nulls (resolution too coarse); ``failed`` if more than
    ``max_frac`` of event-free windows are as deep as the event (not distinguishable from noise);
    otherwise ``passed``. The resolution 1/N is always reported.
    """
    if n < 1 or not 0 <= k <= n:
        return {"state": "not_tested", "k": k, "n": n, "reason": "no valid null windows"}
    frac = k / n
    state = "inconclusive" if n < min_n else ("failed" if frac > max_frac else "passed")
    return {"state": state, "k": int(k), "n": int(n), "fraction": frac, "resolution": 1.0 / n,
            "min_n": min_n, "max_frac": max_frac,
            "note": f"{k}/{n} event-free windows at least as deep; resolution 1/{n}, not a probability of zero"}
