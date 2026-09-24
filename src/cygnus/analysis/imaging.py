"""Bounded, in-memory model-residual screening for small Legacy Survey cutouts.

Inputs are already aligned, calibrated arrays in the same linear flux unit; this is
NOT image subtraction, a PSF fit, or a detection-significance calibration. Pixel
noise is supplied by the caller; correlated noise and trials require separate tests.
No survey-specific pixel-width cut is imposed. Pixel coordinates are (row, column).
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from statistics import median
from typing import Sequence

MAX_PIXELS = 262_144


@dataclass(frozen=True)
class Feature:
    pixels: tuple[tuple[int, int], ...]
    centroid_row: float
    centroid_col: float
    peak_sigma: float
    summed_residual: float
    touches_edge: bool


@dataclass(frozen=True)
class ResidualResult:
    band: str
    background: float
    background_pixels: int
    tested_pixels: int
    masked_pixels: int
    features: tuple[Feature, ...]
    caveats: tuple[str, ...]


def triage_residual(
    image: Sequence[Sequence[float]], model: Sequence[Sequence[float]],
    noise: Sequence[Sequence[float]], mask: Sequence[Sequence[bool]], *,
    band: str, threshold_sigma: float, max_features: int = 64,
) -> ResidualResult:
    """Subtract model, estimate constant median residual sky, find 4-connected positive islands.

    Mask True excludes a pixel completely. Background median uses all unmasked
    residuals and can be biased by crowded or extended signals. No detections
    are emitted if fewer than three unmasked pixels remain. Results are sorted by
    peak then pixel location. Raises instead of truncating too many features.
    """
    if not band or not band.strip():
        raise ValueError("band must be identified")
    if not isfinite(threshold_sigma) or threshold_sigma <= 0 or max_features < 1:
        raise ValueError("threshold and max_features must be positive")
    rows = len(image)
    if not rows or not len(image[0]) or rows * len(image[0]) > MAX_PIXELS:
        raise ValueError("empty or oversized cutout")
    cols = len(image[0])
    # NumPy boolean image masks should behave exactly like ordinary Python
    # boolean lists; .tolist() preserves strict rejection of integer masks.
    if hasattr(mask, "tolist"):
        mask = mask.tolist()
    for matrix in (image, model, noise, mask):
        if len(matrix) != rows or any(len(row) != cols for row in matrix):
            raise ValueError("nonrectangular or mismatched cutout")
    residual: dict[tuple[int, int], float] = {}
    for r in range(rows):
        for c in range(cols):
            if not isinstance(mask[r][c], bool):
                raise ValueError("mask must contain bool values")
            if mask[r][c]:
                continue
            a, b, s = float(image[r][c]), float(model[r][c]), float(noise[r][c])
            if not all(map(isfinite, (a, b, s))) or s <= 0:
                raise ValueError("unmasked pixels require finite flux and positive noise")
            residual[r, c] = a - b
    if len(residual) < 3:
        raise ValueError("at least three unmasked background pixels required")
    sky = median(residual.values())
    active = {p for p, value in residual.items()
              if (value - sky) / float(noise[p[0]][p[1]]) >= threshold_sigma}
    features: list[Feature] = []
    while active:
        start = min(active)
        active.remove(start)
        stack, island = [start], []
        while stack:
            r, c = stack.pop()
            island.append((r, c))
            for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if neighbor in active:
                    active.remove(neighbor)
                    stack.append(neighbor)
        if len(features) >= max_features:
            raise ValueError("feature budget exceeded; narrow the cutout")
        ordered = tuple(sorted(island))
        weights = [residual[p] - sky for p in ordered]
        total = sum(weights)
        features.append(Feature(ordered,
                                sum(p[0] * w for p, w in zip(ordered, weights)) / total,
                                sum(p[1] * w for p, w in zip(ordered, weights)) / total,
                                max(w / float(noise[p[0]][p[1]]) for p, w in zip(ordered, weights)),
                                total, any(r in (0, rows - 1) or c in (0, cols - 1)
                                           for r, c in ordered)))
    features.sort(key=lambda f: (-f.peak_sigma, f.pixels[0]))
    return ResidualResult(band, sky, len(residual), len(residual), rows * cols - len(residual),
                          tuple(features), ("Nominal per-pixel sigma only; no correlated-noise or search-trials correction.",
                                            "Median sky may be biased; edge and PSF/cosmic-ray audits remain untested."))


def independent_band_consistency(first: ResidualResult, second: ResidualResult, *,
                                 independent: bool, radius_pixels: float) -> str:
    """Return consistent/inconsistent/unknown for supplied independent-band islands.

    A pair of same-band or nonindependent products cannot corroborate each other.
    Unknown means no test was possible, not that no counterpart exists.
    """
    if not isfinite(radius_pixels) or radius_pixels <= 0:
        raise ValueError("radius_pixels must be positive and finite")
    if first.band == second.band or not independent or not first.features or not second.features:
        return "unknown"
    return "consistent" if any(
        (a.centroid_row - b.centroid_row) ** 2 + (a.centroid_col - b.centroid_col) ** 2
        <= radius_pixels ** 2 for a in first.features for b in second.features
    ) else "inconsistent"
