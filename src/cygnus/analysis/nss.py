"""Offline Gaia NSS lead triage: explicit negative controls, no discovery claims.

Do not turn an astrometric photocentre orbit into a primary-star orbit or a
companion mass. Spectroscopic binary mass functions below require measured
primary RV amplitude and a justified primary-mass interval. These calculations
exclude systematics, covariances, third light and selection effects.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, pi, sqrt
from typing import Mapping

# Each control is an externally performed check, not an automated Gaia quality test.
NEGATIVE_CONTROLS = ("known_object_literature", "scan_law_alias",
                     "blend_or_triple", "solution_quality", "rv_systematics")
G_KM3_PER_MSUN_S2 = 1.32712440018e11
SECONDS_PER_DAY = 86400


@dataclass(frozen=True)
class SpectroscopicOrbit:
    period_days: float
    period_error_days: float
    rv_amplitude_kms: float
    rv_amplitude_error_kms: float
    eccentricity: float
    eccentricity_error: float
    primary_mass_msun: float
    primary_mass_error_msun: float
    primary_rv_is_measured: bool = False


@dataclass(frozen=True)
class MassConstraint:
    mass_function_msun: float
    mass_function_interval_msun: tuple[float, float]
    minimum_companion_msun: float
    minimum_companion_interval_msun: tuple[float, float]
    caveat: str = "Edge-on lower bound under single, dark companion and adopted primary mass; not a measured companion mass."


@dataclass(frozen=True)
class NSSTriage:
    source_id: str
    status: str
    controls: tuple[tuple[str, str], ...]
    mass_constraint: MassConstraint | None
    caveats: tuple[str, ...]


def _minimum_mass(f: float, m1: float) -> float:
    # f = m2**3/(m1+m2)**2 at sin(i)=1; monotonic for m2 > 0.
    low, high = 0.0, max(1.0, m1, f)
    while high ** 3 / (m1 + high) ** 2 < f:
        high *= 2
    for _ in range(100):
        mid = (low + high) / 2
        if mid ** 3 / (m1 + mid) ** 2 < f:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def spectroscopic_mass_constraint(orbit: SpectroscopicOrbit) -> MassConstraint:
    """Conservative input-interval extrema, not a posterior or confidence interval.

    Uses f = P K1^3 (1-e²)^(3/2) / (2 pi G). All four reported 1-sigma
    input error widths must be finite and nonnegative; interval is merely the
    simultaneous +/- supplied-error envelope, NOT a 68% probability interval.
    """
    p, pe, k, ke, e, ee, m, me = (orbit.period_days, orbit.period_error_days,
        orbit.rv_amplitude_kms, orbit.rv_amplitude_error_kms, orbit.eccentricity,
        orbit.eccentricity_error, orbit.primary_mass_msun, orbit.primary_mass_error_msun)
    if not orbit.primary_rv_is_measured:
        raise ValueError("primary RV amplitude must be measured; photocentre orbit is insufficient")
    if not all(isfinite(x) for x in (p, pe, k, ke, e, ee, m, me)) or any(x < 0 for x in (pe, ke, ee, me)):
        raise ValueError("finite values and nonnegative uncertainties required")
    if p - pe <= 0 or k - ke <= 0 or m - me <= 0 or e - ee < 0 or e + ee >= 1:
        raise ValueError("invalid orbit or interval extends outside physical domain")
    def mf(period: float, amplitude: float, ecc: float) -> float:
        return period * SECONDS_PER_DAY * amplitude ** 3 * (1 - ecc ** 2) ** 1.5 / (2 * pi * G_KM3_PER_MSUN_S2)
    f = mf(p, k, e)
    lo, hi = mf(p - pe, k - ke, e + ee), mf(p + pe, k + ke, e - ee)
    return MassConstraint(f, (lo, hi), _minimum_mass(f, m),
                          (_minimum_mass(lo, m - me), _minimum_mass(hi, m + me)))


def triage_nss(source_id: str, controls: Mapping[str, str], *,
               orbit: SpectroscopicOrbit | None = None) -> NSSTriage:
    """Require all named controls: clear / triggered / unknown (not tested).

    Triggered controls reject a lead; absent/unknown controls remain unknown.
    A reviewed lead is not a vetted candidate or a new object. The mass-function
    calculation is independent of triage outcome but allowed only for measured
    spectroscopic primary RVs. No Gaia data are retrieved or implied.
    """
    if not source_id or not source_id.strip():
        raise ValueError("source_id required")
    if set(controls) - set(NEGATIVE_CONTROLS) or any(v not in ("clear", "triggered", "unknown") for v in controls.values()):
        raise ValueError("unrecognized negative control or state")
    ordered = tuple((key, controls.get(key, "unknown")) for key in NEGATIVE_CONTROLS)
    status = ("rejected" if any(v == "triggered" for _, v in ordered) else
              "unknown" if any(v == "unknown" for _, v in ordered) else "review_only")
    constraint = spectroscopic_mass_constraint(orbit) if orbit is not None else None
    return NSSTriage(source_id, status, ordered, constraint,
                     ("Controls are caller-supplied; clear must mean independently checked against the documented Gaia release and literature.",
                      "Review only is not a discovery or independent validation; inclination, luminous companions and triples remain unresolved."))
