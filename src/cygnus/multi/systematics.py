"""Red-noise systematics model for single-channel light curves.

A two-channel product is vetted by requiring an event in both reductions. A
single-channel archive product (a CSV, a ZTF magnitude series) has no such
independent comparison, so this module builds the next best thing from the light
curve itself:

* the residual autocorrelation gives a red-noise correlation timescale ``tau``;
* a box statistic measured at the event is calibrated against the *same* light
  curve at random epochs, giving an empirical per-epoch p-value;
* the number of independent resolution elements in the baseline
  (``span / max(duration, tau)``) converts that to a look-elsewhere-corrected
  false-alarm probability.

This is a noise model, not an artifact-free channel: a correlated systematic that
recurs on the event's timescale can still mimic a dip. The record keeps the raw
statistic, the empirical p-value, the trial-corrected FAP and ``tau`` so the claim
can be challenged.

No scipy dependency is required (numpy only).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from .lightcurve import local_resid, robust_sigma


@dataclass
class RedNoise:
    tau_days: float | None
    n_valid: int
    method: str = "residual autocorrelation integral to first zero crossing"


def correlation_timescale(resid: np.ndarray, valid: np.ndarray, cadence_s: float, *, min_points: int = 50) -> RedNoise:
    """Red-noise correlation timescale from the residual autocorrelation function."""
    r = np.asarray(resid, float)[valid]
    r = r[np.isfinite(r)]
    n = r.size
    if n < min_points:
        return RedNoise(None, n)
    x = r - r.mean()
    ac = np.fft.irfft(np.fft.rfft(x, 2 * n) * np.conj(np.fft.rfft(x, 2 * n)))[:n]
    if ac[0] <= 0:
        return RedNoise(None, n)
    ac = ac / ac[0]
    tau = 0.0
    for i in range(1, n):
        if ac[i] <= 0:
            break
        tau += ac[i]
    return RedNoise(float(tau * cadence_s / 86400), n)


def box_statistic(t: np.ndarray, y: np.ndarray, valid: np.ndarray, t_mid: float, dur_d: float,
                  half_window_d: float) -> float | None:
    """In-box mean minus a local quadratic baseline (same sign as the screen: negative = dip)."""
    near = valid & np.isfinite(y) & (np.abs(t - t_mid) <= half_window_d)
    inb = near & (np.abs(t - t_mid) <= dur_d / 2)
    fit = near & ~inb
    if inb.sum() < 3 or fit.sum() < 20:
        return None
    x = t - t_mid
    c = np.polyfit(x[fit], y[fit], 2)
    return float(np.mean(y[inb] - np.polyval(c, x[inb])))


def event_significance(lc, channel: np.ndarray, resid: np.ndarray, rednoise: RedNoise, *, t_mid: float, dur_d: float,
                       events_present: list[float] | None = None, seed: int = 0, n_random: int = 300,
                       duration_label: str = "") -> dict | None:
    """Empirical dip significance of one event against the light curve's own red noise.

    Returns the statistic, its robust z, the empirical per-epoch p-value, the number
    of independent resolution elements and the trial-corrected FAP. ``None`` when the
    event window has too few usable cadences.
    """
    valid = lc.usable
    t = lc.time_bjd
    half = max(1.5 * dur_d, dur_d / 2 + 0.6)
    stat = box_statistic(t, channel, valid, t_mid, dur_d, half)
    if stat is None:
        return None
    span = t[valid]
    lo, hi = float(span.min()) + half, float(span.max()) - half
    if hi <= lo:
        return None
    rng = np.random.default_rng(seed)
    exclude = list(events_present or []) + [t_mid]
    trials = []
    for _ in range(n_random * 4):
        if len(trials) >= n_random:
            break
        tc = float(rng.uniform(lo, hi))
        if any(abs(tc - e) < half + dur_d for e in exclude):
            continue
        if (valid & (np.abs(t - tc) <= dur_d / 2)).sum() < 3:
            continue
        trials.append(tc)
    null = np.array([s for s in (box_statistic(t, channel, valid, tc, dur_d, half) for tc in trials) if s is not None])
    if null.size < 30:
        return None
    p = float((1 + np.sum(null <= stat)) / (null.size + 1))       # dips are negative
    s = robust_sigma(null)
    z = float((stat - np.median(null)) / s) if s > 0 else None
    span_d = hi - lo
    tau = rednoise.tau_days
    cad_d = lc.cadence_s / 86400
    # The null is the same box statistic at random epochs of this light curve, so its spread
    # already contains the correlated (red) noise at this duration; dividing z again by
    # sqrt(tau/cadence) would count red noise twice. ``rednoise_inflation`` is reported as a
    # diagnostic only. The parametric p is a Gaussian tail on that z (it can reach below the
    # empirical floor 1/(n_random+1)), so the campaign check passes an event only when the
    # empirical test agrees.
    inflation = (max(1.0, (tau or 0.0) / cad_d)) ** 0.5 if cad_d > 0 else 1.0
    z_eff = z
    p_param = (0.5 * math.erfc(-z_eff / math.sqrt(2))) if z_eff is not None else None
    element = max(dur_d, tau or 0.0, cad_d)
    n_eff = max(1.0, span_d / element)
    fap = float(1 - (1 - p_param) ** n_eff) if p_param is not None else None
    empirical_fap = float(1 - (1 - p) ** n_eff)
    return {"duration_label": duration_label, "box_statistic": stat, "robust_z": z,
            "parametric_z_rednoise_inflated": z_eff, "rednoise_inflation": inflation,
            "rednoise_inflation_applied": False, "duration_days": dur_d,
            "empirical_p": p, "empirical_trial_corrected_fap": empirical_fap, "n_random": int(null.size),
            "n_effective_trials": round(n_eff, 1), "tau_days": tau,
            "parametric_p": p_param, "trial_corrected_fap": fap,
            "interpretation": "empirical dip statistic at the event vs random epochs of the same light curve; "
                              "parametric p from the robust z against that red-noise-bearing null (Gaussian tail), "
                              "corrected for the independent resolution elements at this duration. The empirical p "
                              "cannot go below 1/(n_random+1)."}


def product_summary(lc, channel: np.ndarray, events: list[dict], *, seed: int = 0, n_random: int = 300) -> dict:
    """Red-noise summary for one product and its distinct events (strongest event named).

    ``events`` items need ``mid_time_BJD_like`` and one of ``duration_h``, ``span_days`` (the
    grouped event's time span, preferred) or ``max_cadences`` (fallback).
    """
    resid = local_resid(channel, lc.usable, lc.cadence_s, 2.0)
    rednoise = correlation_timescale(resid, lc.usable, lc.cadence_s)
    mids = [e["mid_time_BJD_like"] for e in events]
    per_event = []
    for e in events:
        cad_d = lc.cadence_s / 86400
        if e.get("duration_h"):
            dur_d = float(e["duration_h"]) / 24
        elif e.get("span_days") is not None:
            # the event's full time span (first to last flagged cadence, plus one cadence), not the
            # cadence count of its longest single screen entry, which can be a small part of the dip
            dur_d = max(2 * cad_d, float(e["span_days"]) + cad_d)
        else:
            dur_d = max(2, int(e.get("max_cadences", 2))) * cad_d
        sig = event_significance(lc, channel, resid, rednoise, t_mid=e["mid_time_BJD_like"], dur_d=dur_d,
                                 events_present=mids, seed=seed, n_random=n_random)
        if sig:
            sig["event_bjd"] = e["mid_time_BJD_like"]
            per_event.append(sig)
    strongest = min(per_event, key=lambda s: (s["trial_corrected_fap"] if s["trial_corrected_fap"] is not None else 1.0)) if per_event else None
    return {"method": rednoise.method, "tau_days": rednoise.tau_days, "n_events": len(events),
            "events": per_event, "strongest": strongest,
            "caveat": "A correlated systematic repeating on the event timescale can mimic a dip; "
                      "this model constrains noise, it does not prove astrophysical origin."}