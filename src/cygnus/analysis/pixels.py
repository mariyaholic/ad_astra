"""Bounded aperture/background alternatives and event-minus-control pixel tests.

Coordinates are zero-based (x=column, y=row). These are in-memory descriptive
checks, not calibrated significance, deblending, or detector-systematics tests.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .timeseries import _numpy


@dataclass(frozen=True)
class ApertureSeries:
    status: str
    reason: str
    flux_unit: str
    time_unit: str
    time_scale: str
    time: tuple[float, ...]
    flux_by_choice: dict[str, tuple[float | None, ...]]
    valid_by_choice: dict[str, tuple[bool, ...]]
    # Missing cadences are None, not zero flux. Each choice is (aperture, sky).
    choices: tuple[tuple[str, str, str], ...]


@dataclass(frozen=True)
class CentroidTest:
    status: str
    reason: str
    flux_unit: str
    event_count: int
    control_count: int
    signal: str
    # Weighted centroid of clipped event-minus-control residual (or its negative).
    residual_xy: tuple[float, float] | None
    # Centroid of positive, sky-subtracted control image in the same aperture.
    control_xy: tuple[float, float] | None
    offset_xy: tuple[float, float] | None
    offset_pixels: float | None


def _cube(cube, *, max_pixels):
    np = _numpy()
    if not isinstance(max_pixels, int) or isinstance(max_pixels, bool) or not 1 <= max_pixels <= 2_000_000:
        raise ValueError("max_pixels must be in 1..2000000")
    arr = np.asarray(cube, dtype=float)
    if arr.ndim != 3 or 0 in arr.shape or arr.size > max_pixels:
        raise ValueError("cube must be nonempty (cadence, row, column) with at most max_pixels elements")
    return arr


def _unit(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty declared unit/system")


def _region(region, shape, name):
    np = _numpy()
    r = np.asarray(region)
    if r.shape != shape or r.dtype.kind != "b" or not np.any(r):
        raise ValueError(f"{name} must be a nonempty boolean image mask matching cube")
    return r


def _valid_mask(mask, shape):
    np = _numpy()
    if mask is None:
        return np.ones(shape, dtype=bool)
    arr = np.asarray(mask)
    if arr.shape != shape or arr.dtype.kind != "b":
        raise ValueError("pixel_mask must be a boolean include-mask matching cube")
    return arr


def _selection(selection, n, name):
    np = _numpy()
    arr = np.asarray(selection)
    if arr.shape != (n,) or arr.dtype.kind != "b":
        raise ValueError(f"{name} must be a boolean cadence mask matching cube")
    return arr


def aperture_counterfactuals(
    cube, time, apertures: Mapping[str, object], backgrounds: Mapping[str, object], *,
    flux_unit: str, time_unit: str, time_scale: str, pixel_mask=None,
    max_pixels: int = 2_000_000,
) -> ApertureSeries:
    """Evaluate every aperture x background choice using median valid sky/pixel.

    Flux is sum(aperture pixels) minus N_valid_aperture * median(background
    pixels), in input per-pixel flux units. Background and aperture masks must
    not overlap. A cadence without a valid aperture *or* valid sky is missing.
    Pixel mask True includes; nonfinite samples are also excluded. No input is
    modified. At most eight apertures and eight backgrounds are accepted.
    """
    np = _numpy()
    for name, value in (("flux_unit", flux_unit), ("time_unit", time_unit), ("time_scale", time_scale)):
        _unit(value, name)
    data = _cube(cube, max_pixels=max_pixels)
    n = data.shape[0]
    t = np.asarray(time, dtype=float)
    if t.shape != (n,) or not np.all(np.isfinite(t)) or (n > 1 and not np.all(np.diff(t) > 0)):
        raise ValueError("time must match cube cadences and be finite and strictly increasing")
    for mapping, label in ((apertures, "apertures"), (backgrounds, "backgrounds")):
        if not isinstance(mapping, Mapping) or not 1 <= len(mapping) <= 8 or any(
            not isinstance(k, str) or not k.strip() for k in mapping
        ):
            raise ValueError(f"{label} must have 1..8 nonempty named masks")
    aps = {key: _region(value, data.shape[1:], f"aperture {key}") for key, value in apertures.items()}
    skies = {key: _region(value, data.shape[1:], f"background {key}") for key, value in backgrounds.items()}
    for an, ap in aps.items():
        for bn, bg in skies.items():
            if np.any(ap & bg):
                raise ValueError(f"aperture {an!r} overlaps background {bn!r}")
    valid = np.isfinite(data) & _valid_mask(pixel_mask, data.shape)
    outputs: dict[str, tuple[float | None, ...]] = {}
    flags: dict[str, tuple[bool, ...]] = {}
    choices = []
    for an, ap in aps.items():
        for bn, bg in skies.items():
            # Length-prefixed labels avoid ambiguity even if user names contain separators.
            label = f"{len(an)}:{an}|{len(bn)}:{bn}"
            values: list[float | None] = []
            for i in range(n):
                av = valid[i] & ap
                bv = valid[i] & bg
                if not np.any(av) or not np.any(bv):
                    values.append(None)
                else:
                    values.append(float(np.sum(data[i][av]) - np.count_nonzero(av) * np.median(data[i][bv])))
            outputs[label] = tuple(values)
            flags[label] = tuple(value is not None for value in values)
            choices.append((label, an, bn))
    any_valid = any(any(x) for x in flags.values())
    return ApertureSeries("inconclusive" if any_valid else "not_tested",
                          "descriptive extraction; systematics and significance not tested" if any_valid else "no valid aperture/background cadence",
                          flux_unit, time_unit, time_scale, tuple(float(x) for x in t),
                          outputs, flags, tuple(choices))


def event_control_centroid(
    cube, event, control, aperture, background, *, flux_unit: str,
    signal: str = "dim", pixel_mask=None, max_pixels: int = 2_000_000,
) -> CentroidTest:
    """Measure event-minus-control deficit/excess centroid in detector pixels.

    Average each pixel only over finite, included cadences in each selection.
    Both averages must exist for *every* aperture pixel; otherwise report
    inconclusive, never silently shrink the aperture. Per-group median sky from
    the background region is subtracted before forming the residual. For `dim`,
    control minus event is clipped to positive weights; for `bright`, event minus
    control is clipped. This conditional centroid is not a localization proof.
    Empty event/control selections are explicitly not_tested.
    """
    np = _numpy()
    _unit(flux_unit, "flux_unit")
    if signal not in ("dim", "bright"):
        raise ValueError("signal must be 'dim' or 'bright'")
    data = _cube(cube, max_pixels=max_pixels)
    ev = _selection(event, data.shape[0], "event")
    co = _selection(control, data.shape[0], "control")
    if np.any(ev & co):
        raise ValueError("event and control must be disjoint")
    ap = _region(aperture, data.shape[1:], "aperture")
    bg = _region(background, data.shape[1:], "background")
    if np.any(ap & bg):
        raise ValueError("aperture and background must not overlap")
    ne, nc = int(np.count_nonzero(ev)), int(np.count_nonzero(co))
    def result(status, reason, residual=None, baseline=None, offset=None, distance=None):
        return CentroidTest(status, reason, flux_unit, ne, nc, signal, residual, baseline, offset, distance)
    if not ne or not nc:
        return result("not_tested", "event and control both require at least one cadence")
    valid = np.isfinite(data) & _valid_mask(pixel_mask, data.shape)
    def image(group):
        subset = data[group]
        good = valid[group]
        count = np.count_nonzero(good, axis=0)
        if np.any(count[ap] == 0) or not np.any(good[:, bg]):
            return None
        mean = np.divide(np.sum(np.where(good, subset, 0.0), axis=0), count,
                         out=np.zeros(data.shape[1:], dtype=float), where=count > 0)
        sky = float(np.median(subset[:, bg][good[:, bg]]))
        return mean - sky
    event_image, control_image = image(ev), image(co)
    if event_image is None or control_image is None:
        return result("inconclusive", "missing valid aperture pixel or background in a group")
    def centroid(weights):
        weights = np.where(ap, np.maximum(weights, 0.0), 0.0)
        total = float(np.sum(weights))
        if not np.isfinite(total) or total <= 0:
            return None
        yy, xx = np.indices(ap.shape)
        return (float(np.sum(weights * xx) / total), float(np.sum(weights * yy) / total))
    baseline = centroid(control_image)
    residual = centroid((control_image - event_image) if signal == "dim" else (event_image - control_image))
    if baseline is None or residual is None:
        return result("inconclusive", "nonpositive control or event-minus-control residual weights", residual, baseline)
    offset = (residual[0] - baseline[0], residual[1] - baseline[1])
    return result("inconclusive", "descriptive pixel offset; pointing, blends and significance not tested",
                  residual, baseline, offset, float(np.hypot(*offset)))
