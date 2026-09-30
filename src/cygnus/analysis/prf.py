"""TESS PRF sampling and a source-preference model with registration and model-floor profiling.

Official UPDATED_2.0 PRF layout: 9x9 subpixel sampling, CRPIX 59 (1-based). A source preference that
flips within allowed registrations/floors is INCONCLUSIVE.
"""

from __future__ import annotations

import numpy as np


def sample_prf(image, xx, yy, x0, y0):
    """Bilinear sample of a pixel-integrated PRF (centre index 58, 9 samples per pixel)."""
    from scipy.ndimage import map_coordinates

    return map_coordinates(image, [(yy - y0) * 9 + 58, (xx - x0) * 9 + 58], order=1, mode="constant", cval=0.0)


def source_model(prf, shape, x0, y0):
    ys, xs = np.mgrid[0:shape[0], 0:shape[1]].astype(float)
    m = sample_prf(prf, xs, ys, x0, y0)
    s = m.sum()
    return m / s if s > 0 else m


def fit_deficit(diff, sigma, models, *, floor=0.0):
    """Linear fit of a difference image to source models; ``floor`` adds a fractional model systematic."""
    d = np.asarray(diff, float).ravel()
    A = np.column_stack([np.asarray(m, float).ravel() for m in models])
    sig = np.sqrt(np.asarray(sigma, float).ravel() ** 2 + (floor * np.abs(d).max()) ** 2)
    c, *_ = np.linalg.lstsq(A / sig[:, None], d / sig, rcond=None)
    return {"amplitudes": c.tolist(), "chi2": float(np.sum(((d - A @ c) / sig) ** 2))}


def profile_source_preference(diff, sigma, prf, positions, *, shifts, floors=(0.01, 0.03, 0.05)):
    """Single-source hypotheses over a registration grid and model floors.

    ``positions`` = {name: (x, y)} in cutout pixels; ``shifts`` = iterable of (dx, dy) offsets.
    """
    shifts = list(shifts)
    per_floor = {}
    for fl in floors:
        scores = {name: min(fit_deficit(diff, sigma, [source_model(prf, np.shape(diff), x + dx, y + dy)],
                                        floor=fl)["chi2"] for dx, dy in shifts)
                  for name, (x, y) in positions.items()}
        per_floor[str(fl)] = {"chi2": scores, "best": min(scores, key=scores.get)}
    flips = len({v["best"] for v in per_floor.values()}) > 1
    return {"per_floor": per_floor, "preference_flips": flips,
            "state": "inconclusive" if flips else "single_preference",
            "note": "a flip under allowed floors/registration is the result; do not assign the source"}
