"""Offline tests for the lead-vetting helpers (cygnus.campaign.vet)."""

import math

import numpy as np

from cygnus.campaign import vet


class FakeLC:
    def __init__(self, t, flux, seed=0):
        rng = np.random.default_rng(seed)
        self.t = t
        self.q = np.zeros(t.size, int)
        f = flux + rng.normal(0, 3e-4, t.size)
        self.col = {"PDCSAP_FLUX": f, "SAP_FLUX": f.copy()}
        self.ok = np.ones(t.size, bool)
        self.sector, self.camera, self.ccd = 1, 1, 1


def _transit(t, mid, dur, depth):
    return np.where(np.abs(t - mid) <= dur / 2, 1 - depth, 1.0)


def test_box_fit_recovers_depth_duration_and_mid():
    t = np.arange(0, 3, 120 / 86400)
    rng = np.random.default_rng(1)
    y = _transit(t, 1.5, 4 / 24, 0.005) + rng.normal(0, 3e-4, t.size)
    f = vet.box_fit(t, y, 1.52, 3 / 24, 1.0)
    assert abs(f["depth_ppm"] - 5000) < 5 * f["depth_err_ppm"] + 150
    assert abs(f["mid_bjd"] - 1.5) < 10 / 1440
    assert 0.75 <= f["duration_h"] / 4 <= 1.3


def test_ephemeris_hits_flags_a_sibling_transit():
    sibs = [{"toi": "1.01", "tfopwg_disp": "KP", "pl_orbper": "10.0", "pl_orbpererr1": "0.0001", "pl_tranmid": "100.0",
             "pl_tranmiderr1": "0.001", "pl_trandurh": "3", "pl_trandep": "8000"},
            {"toi": "1.02", "tfopwg_disp": "PC", "pl_orbper": "0", "pl_orbpererr1": "", "pl_tranmid": "100.0",
             "pl_tranmiderr1": "", "pl_trandurh": "3", "pl_trandep": "500"}]
    hit = vet.ephemeris_hits(sibs, 150.01, 3.0)
    assert len(hit) == 1 and hit[0]["coincides"] and abs(hit[0]["offset_h"] - 0.24) < 0.01
    assert not vet.ephemeris_hits(sibs, 153.0, 3.0)[0]["coincides"]


def test_data_aliases_excludes_periods_with_flat_predicted_transits():
    t = np.arange(0, 27, 120 / 86400)
    dur, depth = 3 / 24, 0.01
    lc = FakeLC(t, _transit(t, 2.0, dur, depth) * _transit(t, 22.0, dur, depth))
    rows = {r["n"]: r["verdict"] for r in vet.data_aliases({"a": lc}, 2.0, 22.0, dur, depth)}
    assert rows[1] == "allowed"     # P = 20 d: no other predicted transit inside the data
    assert rows[2] == "excluded"    # P = 10 d predicts a transit at 12.0 d on flat data
    assert rows[4] == "excluded"


def test_cluster_merges_screen_candidates_of_one_dip():
    c = [{"product": "p", "event_bjd": x, "depth_ppm": d, "n_allowed": n}
         for x, d, n in ((10.00, 900, 3), (10.05, 1000, 4), (10.10, 800, 3), (15.0, 700, 1))]
    ev = vet.cluster(c, 0.2)
    assert [len(e["members"]) for e in ev] == [3, 1]
    assert ev[0]["max_allowed"] == 4 and math.isclose(ev[0]["guess_bjd"], 10.05)


def test_central_duration_scales_as_period_to_one_third():
    d1 = vet.max_central_duration_h(10, 1.0, 1.0, 0.1)
    d8 = vet.max_central_duration_h(80, 1.0, 1.0, 0.1)
    assert 4.0 < d1 < 4.6            # ~4.3 h (T14, k = 0.1) for a Sun-like star at 10 d
    assert math.isclose(d8 / d1, 2.0, rel_tol=0.02)


def test_weighted_box_fit_cross_checks_the_pipeline_errors():
    rng = np.random.default_rng(3)
    t = np.arange(0, 3, 2 / 1440)
    y = (1 + rng.normal(0, 1e-3, t.size)) * _transit(t, 1.5, 3 / 24, 3e-3)
    good = vet.box_fit(t, y, 1.5, 3 / 24, 1.0, yerr=np.full(t.size, 1e-3))["weighted"]
    assert 0.8 < good["scatter_over_quoted_error"] < 1.25 and 0.8 < good["chi2_reduced"] < 1.25
    assert abs(good["depth_ppm"] - 3000) < 4 * good["depth_err_formal_ppm"]
    low = vet.box_fit(t, y, 1.5, 3 / 24, 1.0, yerr=np.full(t.size, 2.5e-4))["weighted"]   # errors understated 4x
    assert low["scatter_over_quoted_error"] > 3 and low["depth_err_scaled_ppm"] > 3 * low["depth_err_formal_ppm"]
    assert "weighted" not in vet.box_fit(t, y, 1.5, 3 / 24, 1.0)
