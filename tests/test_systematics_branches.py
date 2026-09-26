"""Early-return matrix of ``cygnus.multi.systematics`` and ``product_summary``'s duration fallback.

Every branch must return a structured value (``None`` or a dict with ``None`` fields), never raise.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from cygnus.multi import systematics
from cygnus.multi.lightcurve import SpocLightCurve

CAD_S = 120.0
CAD_D = CAD_S / 86400


def _lc(n: int, *, seed: int = 0, t0: float = 1500.0, gap: tuple[float, float] | None = None):
    rng = np.random.default_rng(seed)
    t = t0 + np.arange(n) * CAD_D
    flux = 1.0 + rng.normal(0, 1e-3, n)
    if gap is not None:
        flux[(t > gap[0]) & (t < gap[1])] = np.nan
    lc = SpocLightCurve(path=Path("synthetic.csv"), time=t, sap=flux, pdc=flux, quality=np.zeros(n, int),
                        bjdref=0.0, cadence_s=CAD_S, primary={}, table_header={}, centroids={})
    return lc, flux


# ---------------------------------------------------------------------------- correlation_timescale
def test_correlation_timescale_too_few_points():
    r = np.arange(10.0)
    rn = systematics.correlation_timescale(r, np.ones(10, bool), CAD_S)
    assert rn.tau_days is None and rn.n_valid == 10 and "autocorrelation" in rn.method


def test_correlation_timescale_counts_only_valid_finite_points():
    r = np.r_[np.ones(60), np.full(10, np.nan)]
    valid = np.r_[np.ones(40, bool), np.zeros(30, bool)]
    rn = systematics.correlation_timescale(r, valid, CAD_S)
    assert rn.tau_days is None and rn.n_valid == 40


def test_correlation_timescale_constant_residuals_have_no_scale():
    rn = systematics.correlation_timescale(np.full(100, 0.5), np.ones(100, bool), CAD_S)
    assert rn.tau_days is None and rn.n_valid == 100          # ac[0] == 0 branch


def test_correlation_timescale_white_noise_is_short():
    r = np.random.default_rng(5).normal(0, 1, 2000)
    rn = systematics.correlation_timescale(r, np.ones(r.size, bool), CAD_S)
    assert rn.tau_days is not None and 0.0 <= rn.tau_days < 5 * CAD_D


# ---------------------------------------------------------------------------- box_statistic
def test_box_statistic_needs_in_box_and_baseline_points():
    lc, flux = _lc(600)
    t, valid = lc.time, lc.usable
    mid = float(t[300])
    assert systematics.box_statistic(t, flux, valid, mid, CAD_D, 0.3) is None        # < 3 in the box
    assert systematics.box_statistic(t, flux, valid, mid, 0.1, 0.06) is None          # < 20 outside it
    assert isinstance(systematics.box_statistic(t, flux, valid, mid, 0.05, 0.3), float)
    # an event inside a data gap has no in-box cadences
    lc2, f2 = _lc(600, gap=(float(t[280]), float(t[320])))
    assert systematics.box_statistic(lc2.time, f2, lc2.usable, mid, 0.05, 0.3) is None


# ---------------------------------------------------------------------------- event_significance
def _sig(lc, flux, mid, dur_d, **kw):
    resid = systematics.local_resid(flux, lc.usable, lc.cadence_s, 2.0)
    rn = systematics.correlation_timescale(resid, lc.usable, lc.cadence_s)
    return systematics.event_significance(lc, flux, resid, rn, t_mid=mid, dur_d=dur_d, **kw)


def test_event_significance_none_when_the_event_has_no_statistic():
    lc, flux = _lc(4000)
    t = lc.time
    lc2, f2 = _lc(4000, gap=(float(t[1990]), float(t[2010])))
    assert _sig(lc2, f2, float(t[2000]), 0.02) is None


def test_event_significance_none_when_the_span_is_too_short():
    lc, flux = _lc(720)                                  # 1 d at 2 min: shorter than 2 x half-window (~1.28 d)
    assert _sig(lc, flux, float(lc.time[360]), 2 / 24) is None


def test_event_significance_none_with_fewer_than_30_null_trials():
    lc, flux = _lc(1080)                                 # 1.5 d: every random epoch falls in the event exclusion
    assert _sig(lc, flux, float(lc.time[540]), 2 / 24) is None


def test_event_significance_non_positive_scale_keeps_empirical_fields(monkeypatch):
    lc, flux = _lc(6000, seed=2)
    monkeypatch.setattr(systematics, "robust_sigma", lambda x: 0.0)
    s = _sig(lc, flux, float(lc.time[3000]), 2 / 24, seed=1, n_random=60)
    assert s is not None
    assert s["robust_z"] is None and s["parametric_z"] is None
    assert s["parametric_p"] is None and s["trial_corrected_fap"] is None
    assert 0 < s["empirical_p"] <= 1 and 0 <= s["empirical_trial_corrected_fap"] <= 1
    assert s["n_random"] >= 30 and s["n_effective_trials"] >= 1


def test_event_significance_is_seed_deterministic():
    lc, flux = _lc(6000, seed=3)
    a = _sig(lc, flux, float(lc.time[3000]), 2 / 24, seed=9, n_random=60)
    b = _sig(lc, flux, float(lc.time[3000]), 2 / 24, seed=9, n_random=60)
    assert a == b and a["n_random"] == 60


# ---------------------------------------------------------------------------- product_summary
def test_product_summary_with_no_events():
    lc, flux = _lc(500)
    s = systematics.product_summary(lc, flux, [])
    assert s["n_events"] == 0 and s["events"] == [] and s["strongest"] is None
    assert "caveat" in s and "method" in s


def test_product_summary_when_every_event_is_unmeasurable():
    lc, flux = _lc(720)
    s = systematics.product_summary(lc, flux, [{"mid_time_BJD_like": float(lc.time[360]), "duration_h": 2.0}])
    assert s["n_events"] == 1 and s["events"] == [] and s["strongest"] is None
    assert s["tau_days"] is not None                     # 720 points: the red-noise scale is still estimated


@pytest.mark.parametrize("event,expected_dur_d", [
    ({"duration_h": 3.0}, 3.0 / 24),
    ({"duration_h": 3.0, "span_days": 1.0, "max_cadences": 99}, 3.0 / 24),       # duration_h wins
    ({"duration_h": 0, "span_days": 0.1}, 0.1 + CAD_D),                           # zero duration falls through
    ({"span_days": 0.0}, 2 * CAD_D),                                              # span floor: two cadences
    ({"span_days": None, "max_cadences": 30}, 30 * CAD_D),                        # cadence-count fallback
    ({"max_cadences": 1}, 2 * CAD_D),                                             # at least two cadences
    ({}, 2 * CAD_D),                                                              # nothing: two cadences
])
def test_product_summary_duration_fallbacks(monkeypatch, event, expected_dur_d):
    lc, flux = _lc(500)
    seen = []

    def fake(lc_, channel, resid, rn, *, t_mid, dur_d, events_present, seed, n_random):
        seen.append({"t_mid": t_mid, "dur_d": dur_d, "events_present": events_present})
        return {"trial_corrected_fap": None}

    monkeypatch.setattr(systematics, "event_significance", fake)
    ev = {"mid_time_BJD_like": 1500.3, **event}
    s = systematics.product_summary(lc, flux, [ev, {"mid_time_BJD_like": 1500.5, "duration_h": 1.0}])
    assert seen[0]["dur_d"] == pytest.approx(expected_dur_d)
    assert seen[0]["events_present"] == [1500.3, 1500.5]
    assert [e["event_bjd"] for e in s["events"]] == [1500.3, 1500.5]
    assert s["strongest"] is s["events"][0]                 # both FAPs None -> ranked as 1.0, first kept


def test_product_summary_cadence_count_fallback_end_to_end():
    lc, flux = _lc(6000, seed=4)
    mid = float(lc.time[3000])
    flux = flux.copy()
    flux[np.abs(lc.time - mid) < 0.02] *= 0.98
    s = systematics.product_summary(lc, flux, [{"mid_time_BJD_like": mid, "max_cadences": 30}], seed=2, n_random=60)
    ev = s["strongest"]
    assert ev is not None and ev["duration_days"] == pytest.approx(30 * CAD_D)
    assert ev["event_bjd"] == mid and ev["box_statistic"] < 0
