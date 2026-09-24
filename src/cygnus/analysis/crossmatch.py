"""Small, offline, epoch-aware optical/IR positional candidate matching.

ICRS positions and Julian-year epochs; proper motions in mas/year, RA* =
mu_alpha cos(delta). Linear tangent-plane propagation deliberately omits parallax,
radial velocity, perspective acceleration and full covariance. Do not use for
nearby objects with appreciable parallax or long baselines without a full model.
A missing measurement is unknown, never a nondetection.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, hypot, isfinite, pi
from typing import Sequence

MAX_CATALOG = 10_000
MAX_PAIRS = 1_000_000
MAX_BASELINE_YEARS = 100.0


@dataclass(frozen=True)
class Source:
    identifier: str
    ra_deg: float
    dec_deg: float
    epoch_jyear: float
    position_sigma_arcsec: float | None = None
    pm_ra_cosdec_masyr: float | None = None
    pm_dec_masyr: float | None = None
    pm_sigma_masyr: float | None = None
    magnitude: float | None = None
    quality_ok: bool | None = None

    def __post_init__(self) -> None:
        if not self.identifier or not all(isfinite(v) for v in
                                      (self.ra_deg, self.dec_deg, self.epoch_jyear)):
            raise ValueError("source requires identity, finite ICRS coordinates and epoch")
        if not 0 <= self.ra_deg < 360 or not -85 < self.dec_deg < 85:
            raise ValueError("invalid position; |declination| >= 85 degrees unsupported")
        for value in (self.position_sigma_arcsec, self.pm_ra_cosdec_masyr,
                      self.pm_dec_masyr, self.pm_sigma_masyr, self.magnitude):
            if value is not None and not isfinite(value):
                raise ValueError("nonfinite source metadata")
        if self.position_sigma_arcsec is not None and self.position_sigma_arcsec < 0:
            raise ValueError("negative position uncertainty")
        if self.pm_sigma_masyr is not None and self.pm_sigma_masyr < 0:
            raise ValueError("negative proper-motion uncertainty")
        if (self.pm_ra_cosdec_masyr is None) != (self.pm_dec_masyr is None):
            raise ValueError("both proper-motion components required together")
        if self.quality_ok is not None and not isinstance(self.quality_ok, bool):
            raise ValueError("quality_ok must be bool or None")


@dataclass(frozen=True)
class Pair:
    optical_id: str
    infrared_id: str
    separation_arcsec: float
    combined_sigma_arcsec: float | None
    position_check: str
    color_mag: float | None
    color_check: str
    quality_check: str
    verdict: str


def _at_epoch(source: Source, epoch: float) -> tuple[float, float]:
    if source.pm_ra_cosdec_masyr is None:
        return source.ra_deg, source.dec_deg
    dt = epoch - source.epoch_jyear
    if abs(dt) > MAX_BASELINE_YEARS:
        raise ValueError("linear propagation exceeds 100-year baseline")
    dec = source.dec_deg + dt * source.pm_dec_masyr / 3_600_000
    if not -85 < dec < 85:
        raise ValueError("linear propagation enters unsupported polar region")
    mid = (source.dec_deg + dec) / 2
    delta_ra = dt * source.pm_ra_cosdec_masyr / (3_600_000 * cos(mid * pi / 180))
    if hypot(delta_ra * cos(mid * pi / 180), dec - source.dec_deg) > 1:
        raise ValueError("linear proper-motion displacement exceeds one degree")
    return (source.ra_deg + delta_ra) % 360, dec


def match_optical_infrared(optical: Sequence[Source], infrared: Sequence[Source], *,
                           radius_arcsec: float, sigma_limit: float = 3.0,
                           color_range: tuple[float, float] | None = None) -> tuple[Pair, ...]:
    """Enumerate all pairs within fixed search radius, without forced one-to-one IDs.

    Both positions propagate to the IR observation epoch; uncertainty from each
    catalog and PM uncertainty is quadrature-combined. Unknown PM across differing
    epochs, missing positional errors, quality or photometry block a clear verdict.
    Color is optical magnitude minus IR magnitude in caller-provided systems;
    color_range is an explicit optional screening hypothesis, not classification.
    """
    if len(optical) > MAX_CATALOG or len(infrared) > MAX_CATALOG or len(optical) * len(infrared) > MAX_PAIRS:
        raise ValueError("catalog or pair budget exceeded")
    if len({s.identifier for s in optical}) != len(optical) or len({s.identifier for s in infrared}) != len(infrared):
        raise ValueError("duplicate identifiers within catalog")
    if not all(isfinite(v) and v > 0 for v in (radius_arcsec, sigma_limit)):
        raise ValueError("radius and sigma_limit must be positive")
    if color_range is not None and (len(color_range) != 2 or
                                    not all(isfinite(v) for v in color_range) or
                                    color_range[0] > color_range[1]):
        raise ValueError("invalid color range")
    pairs: list[Pair] = []
    for a in optical:
        for b in infrared:
            epoch = b.epoch_jyear
            if abs(epoch - a.epoch_jyear) > MAX_BASELINE_YEARS:
                raise ValueError("matching exceeds 100-year baseline")
            ra1, dec1 = _at_epoch(a, epoch)
            ra2, dec2 = _at_epoch(b, epoch)
            dra = ((ra1 - ra2 + 180) % 360) - 180
            sep = hypot(dra * cos((dec1 + dec2) * pi / 360), dec1 - dec2) * 3600
            if sep > radius_arcsec:
                continue
            dt = abs(epoch - a.epoch_jyear)
            pm_unknown = dt > 0 and a.pm_ra_cosdec_masyr is None
            if a.position_sigma_arcsec is None or b.position_sigma_arcsec is None or pm_unknown or (dt > 0 and a.pm_sigma_masyr is None):
                sigma = None
                position = "unknown"
            else:
                sigma = hypot(a.position_sigma_arcsec, b.position_sigma_arcsec,
                              dt * (a.pm_sigma_masyr or 0) / 1000)
                position = "consistent" if sep <= sigma_limit * sigma else "inconsistent"
            color = a.magnitude - b.magnitude if a.magnitude is not None and b.magnitude is not None else None
            color_check = ("unknown" if color is None or color_range is None else
                           "consistent" if color_range[0] <= color <= color_range[1] else "inconsistent")
            quality = ("unknown" if a.quality_ok is None or b.quality_ok is None else
                       "consistent" if a.quality_ok and b.quality_ok else "inconsistent")
            checks = (position, color_check, quality)
            verdict = "inconsistent" if "inconsistent" in checks else "consistent" if all(x == "consistent" for x in checks) else "unknown"
            pairs.append(Pair(a.identifier, b.identifier, sep, sigma, position, color,
                              color_check, quality, verdict))
    # Multiple neighbors are explicitly ambiguous, including otherwise clear pairs.
    optical_counts: dict[str, int] = {}
    infrared_counts: dict[str, int] = {}
    for pair in pairs:
        optical_counts[pair.optical_id] = optical_counts.get(pair.optical_id, 0) + 1
        infrared_counts[pair.infrared_id] = infrared_counts.get(pair.infrared_id, 0) + 1
    from dataclasses import replace
    pairs = [replace(p, verdict="unknown") if p.verdict != "inconsistent" and
             (optical_counts[p.optical_id] > 1 or infrared_counts[p.infrared_id] > 1)
             else p for p in pairs]
    return tuple(sorted(pairs, key=lambda p: (p.separation_arcsec, p.optical_id, p.infrared_id)))
