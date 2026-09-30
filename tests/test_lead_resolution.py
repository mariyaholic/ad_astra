"""Synthetic falsification controls for the bounded follow-up box experiment."""

import importlib.util
from pathlib import Path

import numpy as np


def test_integrated_line_mask_recovers_signed_doppler_centroid():
    m = module()
    wave = np.arange(4800.0, 4806.0, 0.002)
    mask = np.array([[4802.98, 4803.02]])
    velocities = np.arange(-80.0, 80.01, 0.2)
    for injected in (34.04, -12.3):
        center = 4803.0 * np.sqrt(
            (1 + injected / 299792.458) / (1 - injected / 299792.458)
        )
        flux = 1 - 0.4 * np.exp(-0.5 * ((wave - center) / 0.055) ** 2)
        ccf = m.integrated_mask_ccf(wave, flux, mask, velocities)
        fit = m.fit_mask_ccf(velocities, ccf)
        assert abs(fit["center_kms"] - injected) < 0.01


def test_line_mask_excludes_detector_gap_without_filling_it():
    m = module()
    wave = np.arange(4800.0, 4820.0, 0.002)
    center = 4804.0 * np.sqrt((1 + 34.0 / 299792.458) / (1 - 34.0 / 299792.458))
    flux = 1 - 0.4 * np.exp(-0.5 * ((wave - center) / 0.055) ** 2)
    valid = (wave < 4813.0) | (wave > 4817.0)
    flux[~valid] = 0.0
    velocity = np.arange(-80.0, 80.01, 0.2)
    ccf = m.integrated_mask_ccf(
        wave,
        flux,
        np.array([[4803.98, 4804.02], [4814.98, 4815.02]]),
        velocity,
        valid=valid,
    )
    assert abs(m.fit_mask_ccf(velocity, ccf)["center_kms"] - 34.0) < 0.01


def test_relative_ccf_alignment_preserves_static_asymmetry():
    m = module()
    velocity = np.arange(-30.0, 80.01, 0.25)

    def profile(x):
        return (
            1
            - 0.2 * np.exp(-0.5 * ((x - 34) / 3.0) ** 2)
            - 0.03 * np.exp(-0.5 * ((x - 37) / 1.5) ** 2)
        )

    observed = 1.1 * profile(velocity - 0.04) + 0.03 + 0.0001 * (velocity - 34.0)
    result = m.relative_ccf_shift(velocity, profile(velocity), observed, 34.0)
    assert abs(result["shift_kms"] - 0.04) < 0.001


def test_spectral_shift_sign_and_subpixel_recovery():
    m = module()
    velocity = np.arange(-100.0, 100.0, 0.5)

    def lines(x):
        return -np.exp(-0.5 * ((x + 30) / 3) ** 2) - 0.6 * np.exp(
            -0.5 * ((x - 20) / 4) ** 2
        )

    for injected in (0.04, -12.3):
        result = m.spectral_shift(velocity, lines(velocity), lines(velocity - injected))
        assert abs(result - injected) < 0.01


def module():
    path = (
        Path(__file__).parents[1]
        / "reports/lead-resolution-2026-09-30/resolve_leads.py"
    )
    assert path.exists(), "follow-up implementation has not been written"
    spec = importlib.util.spec_from_file_location("resolve_leads", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_joint_baseline_recovers_box_on_curved_variable_star():
    m = module()
    t = np.arange(-1.0, 1.0, 1 / 720)
    y = 1 + 0.003 * t + 0.007 * t**2
    y[np.abs(t) <= 0.025] -= 0.015
    result = m.box_measure(t, y, 0.0, 0.05, 2)
    assert result["state"] == "measured"
    assert abs(result["depth_ppm"] - 15000) < 20


def test_missing_event_window_is_not_a_nondetection():
    m = module()
    t = np.arange(-1.0, 1.0, 1 / 720)
    t = t[np.abs(t) > 0.02]
    result = m.box_measure(t, np.ones_like(t), 0.0, 0.05, 1)
    assert result["state"] == "uncovered"


def test_box_does_not_turn_positive_flare_into_dip():
    m = module()
    t = np.arange(-1.0, 1.0, 1 / 720)
    y = np.ones_like(t)
    y[np.abs(t) <= 0.025] += 0.01
    assert m.box_measure(t, y, 0.0, 0.05, 1)["depth_ppm"] < 0


def test_prf_sampling_recovers_known_subpixel_shift():
    m = module()
    grid = (np.arange(117) - 58) / 9
    xx, yy = np.meshgrid(grid, grid)
    image = np.exp(-0.5 * (xx**2 + yy**2))
    y, x = np.indices((9, 9))
    model = m.sample_prf(image, x, y, 4.2, 3.7)
    assert np.unravel_index(model.argmax(), model.shape) == (4, 4)
    cx = float((model * x).sum() / model.sum())
    cy = float((model * y).sum() / model.sum())
    assert abs(cx - 4.2) < 0.01 and abs(cy - 3.7) < 0.01


def test_exposure_integrated_box_recovers_short_event_at_coarse_cadence():
    m = module()
    t = np.arange(-1.0, 1.0, 1 / 48)
    duration = 0.048
    overlap = (
        np.clip(
            np.minimum(t + 1 / 96, 0.003 + duration / 2)
            - np.maximum(t - 1 / 96, 0.003 - duration / 2),
            0,
            1 / 48,
        )
        * 48
    )
    y = 1 - 0.015 * overlap
    result = m.box_measure(t, y, 0.003, duration, 1, exposure=1 / 48, min_points=2)
    assert result["state"] == "measured"
    assert abs(result["depth_ppm"] - 15000) < 1


def test_weighted_rv_orbit_preserves_kms_units_and_recovers_amplitude():
    m = module()
    t = np.linspace(0, 200, 53)
    template = np.sin(2 * np.pi * t / 37)
    nuisance = np.column_stack([np.ones(len(t)), t / 200])
    rv = 34.0 + 0.02 * template + 0.003 * t / 200
    result = m.rv_linear_fit(rv, np.full(len(t), 0.002), template, nuisance)
    assert abs(result["semiamplitude_kms"] - 0.02) < 1e-10
    assert result["residual_rms_kms"] < 1e-10


def test_circular_transit_tied_rv_has_zero_velocity_at_transit():
    m = module()
    v = m.rv_template(np.array([0.0, 2.5, 5.0]), 10.0, 0.0, 0.0, 0.0)
    assert np.allclose(v, [0.0, -1.0, 0.0], atol=1e-10)
