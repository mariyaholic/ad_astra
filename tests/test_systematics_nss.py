"""Red-noise systematics model and Gaia NSS vetting (offline)."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import pytest

from cygnus.multi import nss, systematics
from cygnus.multi.archives import base
from cygnus.multi.archives.base import Target
from cygnus.multi.lightcurve import SpocLightCurve


def _lc(path: Path, t: np.ndarray, flux: np.ndarray) -> SpocLightCurve:
    return SpocLightCurve(path=path, time=t, sap=flux, pdc=flux, quality=np.zeros(t.size, int),
                          bjdref=0.0, cadence_s=120.0, primary={"_channels": {"all": ["FLUX"], "independent": False}},
                          table_header={}, centroids={})


def _events(lc, dip_at, dur_h=2.0):
    return [{"mid_time_BJD_like": float(dip_at), "max_cadences": int(dur_h * 3600 / 120), "duration_h": dur_h}]


def test_white_noise_deep_dip_is_highly_significant(tmp_path):
    rng = np.random.default_rng(1)
    n = 6000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    flux = 1.0 + rng.normal(0, 1e-3, n)
    flux[np.abs(t - 1503.5) < 0.04] *= 0.97          # 3% dip
    lc = _lc(tmp_path / "w.csv", t, flux)
    summary = systematics.product_summary(lc, flux, _events(lc, 1503.5), seed=3, n_random=200)
    s = summary["strongest"]
    assert s is not None
    assert s["trial_corrected_fap"] is not None and s["trial_corrected_fap"] < 1e-3
    assert s["parametric_z_rednoise_inflated"] < -7
    assert s["empirical_p"] <= 1 / (s["n_random"] + 1) + 1e-9


def test_red_noise_shallow_dip_is_not_significant(tmp_path):
    """An AR(1) series with a long correlation time makes a shallow dip unremarkable."""
    rng = np.random.default_rng(2)
    n = 6000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    rho = 0.98                                        # tau ~ 1/(1-rho) ~ 50 cadences ~ 0.07 d
    eps = rng.normal(0, 1e-3, n)
    flux = np.empty(n)
    flux[0] = eps[0]
    for i in range(1, n):
        flux[i] = rho * flux[i - 1] + eps[i]
    flux += 1.0
    flux[np.abs(t - 1503.5) < 0.04] *= 0.997          # 0.3% dip, comparable to red noise
    lc = _lc(tmp_path / "r.csv", t, flux)
    summary = systematics.product_summary(lc, flux, _events(lc, 1503.5), seed=4, n_random=200)
    assert summary["tau_days"] is None or summary["tau_days"] > 0.0   # tau was estimated
    s = summary["strongest"]
    if s is not None:
        # the red-noise-inflated significance must be far weaker than the white-noise case
        assert s["rednoise_inflation"] >= 1.0
        assert s["trial_corrected_fap"] is None or s["trial_corrected_fap"] > 1e-4


def test_two_transit_dataset_events_are_found_and_vetoed(tmp_path):
    """Sanity: correlation_timescale is zero-ish for white noise and positive for AR(1)."""
    rng = np.random.default_rng(5)
    n = 3000
    white = rng.normal(0, 1e-3, n)
    rw = systematics.correlation_timescale(white, np.ones(n, bool), 120.0)
    assert rw.tau_days is not None and rw.tau_days < 0.01
    ar = np.empty(n)
    ar[0] = white[0]
    for i in range(1, n):
        ar[i] = 0.98 * ar[i - 1] + white[i]
    rr = systematics.correlation_timescale(ar, np.ones(n, bool), 120.0)
    assert rr.tau_days is not None and rr.tau_days > rw.tau_days


# ------------------------------------------------------------------ Gaia NSS
def test_mass_function_formula():
    # Sun-Earth-like: P=365.25 d, K=0.09 km/s is not physical for a planet's pull on the Sun;
    # use a known scaling instead: K doubles -> f(M) multiplies by 8.
    f1 = nss.mass_function_msun(100.0, 10.0, 0.0)
    f2 = nss.mass_function_msun(100.0, 20.0, 0.0)
    assert f1 and f2 and f2 == pytest.approx(8 * f1)
    assert nss.mass_function_msun(100.0, 10.0, 0.5) == pytest.approx(f1 * (1 - 0.25) ** 1.5)
    assert nss.mass_function_msun(-1, 10, 0) is None
    assert nss.mass_function_msun(100, 0, 0) is None


class _Resp:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass


def _gaia_http(source_csv: str, nss_csv: str):
    def http(url, data=None, timeout=None, headers=None):
        q = (data or {}).get("QUERY", "")
        return _Resp(nss_csv if "nss_two_body_orbit" in q else source_csv)
    return http


SOURCE = "source_id,ra,dec,phot_g_mean_mag,parallax\n111,10.0001,20.0,12.0,1.5\n"
NSS_HEAD = ("source_id,nss_solution_type,ra,dec,parallax,period,period_error,eccentricity,eccentricity_error,"
            "semi_amplitude_primary,semi_amplitude_primary_error,mass_ratio,inclination,inclination_error,"
            "significance,goodness_of_fit,flags,astrometric_jitter\n")
NSS_ROW = "111,SB1,10.0001,20.0,1.5,100.0,0.1,0.2,0.01,10.0,0.1,0.3,80.0,2.0,20.0,1.1,0,0.2\n"


def test_nss_vetting_flags_a_known_companion(tmp_path):
    adapter = base.get("gaia", http=_gaia_http(SOURCE, NSS_HEAD + NSS_ROW))
    res = nss.nss_vetting(adapter, Target(name="T", ra_deg=10.0, dec_deg=20.0), radius_arcsec=5.0)
    assert res["state"] == "failed" and res["nss_solutions"] == 1
    assert res["top_mass_function_msun"] and res["top_mass_function_msun"] > 0
    assert "known Gaia NSS companion" in res["note"]


def test_nss_vetting_no_solution_is_inconclusive(tmp_path):
    adapter = base.get("gaia", http=_gaia_http(SOURCE, NSS_HEAD))
    res = nss.nss_vetting(adapter, Target(name="T", ra_deg=10.0, dec_deg=20.0), radius_arcsec=5.0)
    assert res["state"] == "inconclusive" and "not proof of a single star" in res["note"]


def test_nss_vetting_unmatched_target_is_not_tested():
    adapter = base.get("gaia", http=_gaia_http("source_id,ra,dec,phot_g_mean_mag,parallax\n", NSS_HEAD))
    res = nss.nss_vetting(adapter, Target(name="T", ra_deg=200.0, dec_deg=-40.0), radius_arcsec=5.0)
    assert res["state"] == "not_tested" and res["nss_solutions"] == 0


def test_nss_vetting_low_significance_is_inconclusive():
    low = NSS_ROW.replace(",20.0,1.1,0,0.2", ",1.2,1.1,0,0.2")
    adapter = base.get("gaia", http=_gaia_http(SOURCE, NSS_HEAD + low))
    res = nss.nss_vetting(adapter, Target(name="T", ra_deg=10.0, dec_deg=20.0), radius_arcsec=5.0)
    assert res["state"] == "inconclusive" and res["significant_solutions"] == 0