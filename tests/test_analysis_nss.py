"""Synthetic orbital calculations and explicit negative-control state."""

import pytest

from cygnus.analysis.nss import (NEGATIVE_CONTROLS, SpectroscopicOrbit,
                                 spectroscopic_mass_constraint, triage_nss)


def _orbit(**changes):
    args = dict(period_days=365.25, period_error_days=1,
                rv_amplitude_kms=10, rv_amplitude_error_kms=.2,
                eccentricity=.1, eccentricity_error=.02,
                primary_mass_msun=1, primary_mass_error_msun=.1,
                primary_rv_is_measured=True)
    args.update(changes)
    return SpectroscopicOrbit(**args)


def test_no_unearned_clear_controls_and_negative_control_rejection():
    assert triage_nss("synthetic", {}).status == "unknown"
    checked = dict.fromkeys(NEGATIVE_CONTROLS, "clear")
    assert triage_nss("synthetic", checked).status == "review_only"
    checked["scan_law_alias"] = "triggered"
    record = triage_nss("synthetic", checked)
    assert record.status == "rejected"
    assert record.mass_constraint is None
    assert record.controls[1] == ("scan_law_alias", "triggered")
    with pytest.raises(ValueError):
        triage_nss("synthetic", {"unknown_control": "clear"})


def test_spectroscopic_mass_function_and_input_envelope():
    result = spectroscopic_mass_constraint(_orbit())
    assert .03 < result.mass_function_msun < .04
    assert result.mass_function_interval_msun[0] < result.mass_function_msun < result.mass_function_interval_msun[1]
    assert result.minimum_companion_interval_msun[0] < result.minimum_companion_msun < result.minimum_companion_interval_msun[1]
    m2 = result.minimum_companion_msun
    assert m2 ** 3 / (1 + m2) ** 2 == pytest.approx(result.mass_function_msun)
    assert "not a measured companion mass" in result.caveat
    assert triage_nss("synthetic", {}, orbit=_orbit()).mass_constraint == result


def test_photocentre_and_unphysical_input_do_not_yield_mass():
    with pytest.raises(ValueError, match="primary RV"):
        spectroscopic_mass_constraint(_orbit(primary_rv_is_measured=False))
    for params in ({"eccentricity": .99, "eccentricity_error": .02},
                   {"rv_amplitude_kms": 0}, {"primary_mass_error_msun": 2}):
        with pytest.raises(ValueError, match="invalid orbit"):
            spectroscopic_mass_constraint(_orbit(**params))
