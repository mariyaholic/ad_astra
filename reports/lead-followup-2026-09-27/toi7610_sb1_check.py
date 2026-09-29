"""Quantify the Gaia DR3 SB1 evidence for TOI-7610.01.

The calculation uses the exact Gaia DR3 NSS row refreshed by
``catalog_followup.py`` and the campaign's declared stellar-mass prior.  The
minimum companion mass is conditional on that prior and sin(i)=1; the binary
mass function itself is the more direct measurement.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from astropy.constants import G, M_sun


ROOT = Path(r"D:\Ad Astra")
REPORT_DIR = ROOT / "reports" / "lead-followup-2026-09-27"
CATALOG = REPORT_DIR / "catalog_followup.json"
STELLAR = ROOT / "campaigns" / "toi-7610-01" / "stellar_context.json"
OUT = REPORT_DIR / "toi7610_sb1_results.json"
SEED = 20260927
MONTE_CARLO_DRAWS = 200_000
EVENTS_BJD_TDB = [2460700.9700970678, 2461066.3486342016]


def table_rows(result: dict) -> list[dict]:
    names = [column["name"] for column in result["metadata"]]
    return [dict(zip(names, row)) for row in result["data"]]


def companion_mass_from_function(mass_function, primary_mass):
    # Newton solve x^3 / (M1 + x)^2 = f for sin(i)=1.
    x = np.maximum(primary_mass, mass_function) + mass_function ** (1.0 / 3.0)
    for _ in range(30):
        value = x**3 / (primary_mass + x) ** 2 - mass_function
        derivative = x**2 * (3.0 * primary_mass + x) / (primary_mass + x) ** 3
        x = np.maximum(x - value / derivative, 1e-6)
    return x


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    nss_result = catalog["queries"]["gaia_nss"]["nss_two_body_orbit"]["result"]
    rows = table_rows(nss_result)
    if len(rows) != 1 or rows[0]["nss_solution_type"] != "SB1":
        raise RuntimeError(f"expected one Gaia SB1 row, got {rows}")
    row = rows[0]

    stellar = json.loads(STELLAR.read_text(encoding="utf-8"))["TOI-7610.01"]["priors"]
    primary_mass = float(stellar["mass_msun"])
    primary_mass_error = float(stellar["mass_err_msun"])

    period_s = float(row["period"]) * 86400.0
    semi_amplitude_m_s = float(row["semi_amplitude_primary"]) * 1000.0
    eccentricity = float(row["eccentricity"])
    mass_function_msun = (
        period_s
        * semi_amplitude_m_s**3
        * (1.0 - eccentricity**2) ** 1.5
        / (2.0 * math.pi * G.value)
        / M_sun.value
    )

    rng = np.random.default_rng(SEED)
    period = rng.normal(row["period"], row["period_error"], MONTE_CARLO_DRAWS)
    semi_amplitude = rng.normal(
        row["semi_amplitude_primary"],
        row["semi_amplitude_primary_error"],
        MONTE_CARLO_DRAWS,
    )
    ecc = rng.normal(row["eccentricity"], row["eccentricity_error"], MONTE_CARLO_DRAWS)
    m1 = rng.normal(primary_mass, primary_mass_error, MONTE_CARLO_DRAWS)
    valid = (period > 0) & (semi_amplitude > 0) & (ecc >= 0) & (ecc < 1) & (m1 > 0)
    period = period[valid]
    semi_amplitude = semi_amplitude[valid]
    ecc = ecc[valid]
    m1 = m1[valid]
    sampled_function = (
        period
        * 86400.0
        * (semi_amplitude * 1000.0) ** 3
        * (1.0 - ecc**2) ** 1.5
        / (2.0 * math.pi * G.value)
        / M_sun.value
    )
    minimum_companion = companion_mass_from_function(sampled_function, m1)

    interval = EVENTS_BJD_TDB[1] - EVENTS_BJD_TDB[0]
    cycle_ratio = interval / float(row["period"])
    nearest_cycles = int(round(cycle_ratio))
    timing_residual = interval - nearest_cycles * float(row["period"])
    timing_sigma = nearest_cycles * float(row["period_error"])

    def quantiles(values):
        return [float(value) for value in np.quantile(values, [0.16, 0.5, 0.84])]

    selected_fields = [
        "solution_id",
        "source_id",
        "nss_solution_type",
        "period",
        "period_error",
        "t_periastron",
        "t_periastron_error",
        "eccentricity",
        "eccentricity_error",
        "center_of_mass_velocity",
        "center_of_mass_velocity_error",
        "semi_amplitude_primary",
        "semi_amplitude_primary_error",
        "arg_periastron",
        "arg_periastron_error",
        "rv_n_obs_primary",
        "rv_n_good_obs_primary",
        "goodness_of_fit",
        "efficiency",
        "significance",
        "flags",
    ]
    output = {
        "method": {
            "software": str(Path(__file__).relative_to(ROOT)).replace("\\", "/"),
            "gaia_query_artifact": str(CATALOG.relative_to(ROOT)).replace("\\", "/"),
            "gaia_release": "DR3",
            "mass_function": "P K1^3 (1-e^2)^(3/2) / (2 pi G)",
            "minimum_mass_assumption": "sin(i)=1 and campaign stellar-mass prior",
            "monte_carlo_draws": MONTE_CARLO_DRAWS,
            "seed": SEED,
        },
        "gaia_sb1": {field: row[field] for field in selected_fields},
        "derived": {
            "mass_function_msun_direct": mass_function_msun,
            "mass_function_msun_q16_q50_q84": quantiles(sampled_function),
            "primary_mass_prior_msun": primary_mass,
            "primary_mass_prior_error_msun": primary_mass_error,
            "minimum_companion_mass_msun_q16_q50_q84": quantiles(minimum_companion),
            "event_interval_days": interval,
            "event_interval_over_sb1_period": cycle_ratio,
            "nearest_integer_sb1_cycles": nearest_cycles,
            "event_interval_minus_integer_cycles_days": timing_residual,
            "formal_period_only_residual_sigma": timing_residual / timing_sigma,
        },
        "interpretation": {
            "sb1_status": "confirmed catalog row with an orbital solution, not an untraced SIMBAD label",
            "planetary_reading": (
                "The host has a stellar-mass spectroscopic companion. The two TESS events are "
                "not securely localized and their separation is not exactly four Gaia periods. "
                "A circumbinary or tertiary transit is not mathematically excluded, but the "
                "original target-planet interpretation is not supportable."
            ),
            "timing_caveat": (
                "The phase comparison uses only the event interval and Gaia period; the quoted "
                "sigma propagates the formal period error over four cycles and is not a full "
                "Gaia orbital covariance or TESS timing-error calculation."
            ),
        },
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
