"""L1: seeded synthetic calibration of the screen, its significance and the new measures.

Slow (``pytest -m slow``; not in the offline gate). Every test draws a population of synthetic
light curves or stars from a fixed seed, measures a rate or a coverage, prints it on one
``L1 <name>: ...`` line (run with ``-s`` to see them) and asserts it lies in the range the method
claims. The numbers recorded in ``docs/SUITE_EXPANSION.md`` come from these lines.
"""

from __future__ import annotations

import math
import types

import pytest

np = pytest.importorskip("numpy")
pytest.importorskip("scipy")

from cygnus.multi import measures as M

pytestmark = pytest.mark.slow

CAD_S = 120.0


def _red_noise(rng, n, sigma, tau_d, cad_s=CAD_S):
    """AR(1) noise of total rms ``sigma`` and correlation time ``tau_d``."""
    phi = math.exp(-cad_s / 86400 / tau_d) if tau_d > 0 else 0.0
    e = rng.normal(0, sigma * math.sqrt(1 - phi ** 2), n)
    x = np.empty(n)
    x[0] = rng.normal(0, sigma)
    for i in range(1, n):
        x[i] = phi * x[i - 1] + e[i]
    return x


def _lc(t, flux, sap=None):
    from cygnus.campaign.lightcurve import SpocLightCurve

    return SpocLightCurve(path=None, time=t - 2457000.0, sap=flux if sap is None else sap, pdc=flux,
                          quality=np.zeros(t.size, int), bjdref=2457000.0, cadence_s=CAD_S)


def _ks_uniform(p):
    p = np.sort(np.asarray(p))
    n = p.size
    return float(max(np.max(np.arange(1, n + 1) / n - p), np.max(p - np.arange(n) / n)))


# ------------------------------------------------------------------ red-noise significance under the null
def test_empirical_p_is_uniform_on_red_noise_nulls_and_parametric_p_is_reported():
    from cygnus.multi import systematics

    rng = np.random.default_rng(20260926)
    emp, par = [], []
    for _ in range(150):
        n = 4000
        t = 2459000.0 + np.arange(n) * CAD_S / 86400
        f = 1 + rng.normal(0, 5e-4, n) + _red_noise(rng, n, 5e-4, 0.05)
        lc = _lc(t, f)
        from cygnus.multi.lightcurve import local_resid

        resid = local_resid(f, lc.usable, CAD_S, 2.0)
        rn = systematics.correlation_timescale(resid, lc.usable, CAD_S)
        tm = float(rng.uniform(t[0] + 1, t[-1] - 1))
        s = systematics.event_significance(lc, f, resid, rn, t_mid=tm, dur_d=2 / 24, seed=int(rng.integers(1e9)), n_random=200)
        if s:
            emp.append(s["empirical_p"])
            par.append(s["parametric_p"])
    emp, par = np.array(emp), np.array(par)
    ks = _ks_uniform(emp)
    print(f"\nL1 null significance: n={emp.size}; empirical p KS D={ks:.3f} (crit 5% {1.36 / math.sqrt(emp.size):.3f}); "
          f"P(emp p<=0.05)={np.mean(emp <= 0.05):.3f}; P(param p<=0.05)={np.mean(par <= 0.05):.3f}; "
          f"P(param p<=0.01)={np.mean(par <= 0.01):.3f}")
    assert emp.size >= 140
    assert ks < 1.36 / math.sqrt(emp.size)             # the random-epoch null is calibrated on its own light curve
    assert 0.0 <= np.mean(emp <= 0.05) <= 0.10


# ------------------------------------------------------------------ calibrated threshold on held-out noise
def test_calibrated_k_star_controls_persistent_false_alarms_on_held_out_noise():
    from cygnus.multi.steps import _persistent_intervals

    rng = np.random.default_rng(7)
    grid = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0]
    n_lc, fa, ks = 60, 0, []
    for _ in range(n_lc):
        n = 5000
        t = 2459000.0 + np.arange(n) * CAD_S / 86400

        def draw():
            common = _red_noise(rng, n, 1.2e-3, 0.08)        # shared systematics seen by both reductions
            return (1 + common + rng.normal(0, 3e-4, n), 1 + common + rng.normal(0, 3e-4, n))

        sap, pdc = draw()
        lc = _lc(t, pdc, sap)
        fin, veto = lc.usable, np.zeros(n, bool)
        ok = [k for k in grid if len(_persistent_intervals(lc, sap, pdc, fin, 2.0, k, +1, veto)) == 0]
        k_star = min(ok) if ok else None
        if k_star is None or k_star == grid[0]:
            continue                                          # no k*, or only an upper bound at the grid floor
        ks.append(k_star)
        sap2, pdc2 = draw()                                   # held out: same noise process, new realisation
        lc2 = _lc(t, pdc2, sap2)
        fa += len(_persistent_intervals(lc2, sap2, pdc2, lc2.usable, 2.0, k_star, -1, veto)) > 0
    rate = fa / len(ks)
    print(f"\nL1 held-out false alarms: {len(ks)} light curves, median k*={np.median(ks):.2g}; "
          f"fraction with >=1 persistent dip at k* on held-out noise = {rate:.2f}")
    assert len(ks) >= 20
    assert rate <= 0.6          # k* is the smallest grid value with no null event: about a coin flip per light curve


# ------------------------------------------------------------------ completeness floors on a grid
def test_completeness_rises_with_depth_for_each_duration():
    from cygnus.multi.steps import _persistent_intervals

    rng = np.random.default_rng(11)
    n = 6000
    t = 2459000.0 + np.arange(n) * CAD_S / 86400
    base_s, base_p = 1 + rng.normal(0, 1e-3, n), 1 + rng.normal(0, 1e-3, n)
    lc = _lc(t, base_p, base_s)
    veto = np.zeros(n, bool)
    table = {}
    for dur_h in (1.0, 2.0, 4.0):
        row = []
        for depth in (1000, 2000, 3000, 5000, 8000):
            rec = 0
            for _ in range(12):
                c = float(rng.uniform(t[0] + 1, t[-1] - 1))
                box = np.abs(t - c) <= dur_h / 48
                s, p = base_s.copy(), base_p.copy()
                s[box] *= 1 - depth * 1e-6
                p[box] *= 1 - depth * 1e-6
                ii = np.flatnonzero(box)
                found = _persistent_intervals(lc, s, p, lc.usable, 2.0, 5.0, -1, veto)
                rec += any(a <= ii[-1] and ii[0] <= b for a, b in found)
            row.append(rec / 12)
        table[dur_h] = row
    print("\nL1 completeness at k=5, sigma 1000 ppm per 2-min cadence (depths 1000,2000,3000,5000,8000 ppm): "
          + "; ".join(f"{d:g} h {', '.join(f'{x:.2f}' for x in r)}" for d, r in table.items()))
    for r in table.values():
        assert r[-1] >= 0.9 and r[0] <= 0.5
        assert all(b >= a - 0.17 for a, b in zip(r, r[1:]))   # monotone up to binomial noise of 12 draws


# ------------------------------------------------------------------ stellar priors coverage and extinction bias
def test_dwarf_prior_coverage_and_extinction_bias():
    tab = M.dwarf_table()
    rng = np.random.default_rng(3)
    b, stop = M._colour_range()
    inside, n, bias = 0, 0, []
    for _ in range(400):
        abs_g = float(rng.uniform(tab["abs_g"][10], tab["abs_g"][stop - 5]))
        bp_rp = float(np.interp(abs_g, tab["abs_g"][:stop], b))
        r_true = float(np.interp(abs_g, tab["abs_g"], tab["radius_rsun"])) * (1 + rng.normal(0, 0.05))   # intrinsic width 5%
        d_pc = float(rng.uniform(20, 300))
        plx = 1000 / d_pc
        eplx = plx / float(rng.uniform(10, 50))
        row = {"phot_g_mean_mag": abs_g + 5 * math.log10(d_pc / 10), "bp_rp": bp_rp, "parallax": plx + rng.normal(0, eplx),
               "parallax_error": eplx, "ruwe": 1.0}
        p = M.stellar_priors(row)
        if not p["usable"]:
            continue
        n += 1
        inside += abs(p["radius_rsun"] - r_true) <= p["radius_err_rsun"]
        ext = M.stellar_priors({**row, "phot_g_mean_mag": row["phot_g_mean_mag"] + 0.3})   # 0.3 mag of unmodelled A_G
        if ext["usable"]:
            bias.append(ext["radius_rsun"] / p["radius_rsun"] - 1)
    cov = inside / n
    print(f"\nL1 dwarf priors: {n} usable of 400; R* within 1 sigma for {cov:.2f} (5% intrinsic width, declared 8% floor); "
          f"0.3 mag unmodelled extinction biases R* by {np.median(bias):+.1%} (median)")
    assert n >= 300 and 0.68 <= cov <= 0.99
    assert np.median(bias) < 0


# ------------------------------------------------------------------ alias duration likelihood: reliability
def test_duration_likelihood_ranks_the_true_alias_better_than_chance():
    rng = np.random.default_rng(5)
    top, n, wtrue = 0, 0, []
    for _ in range(150):
        dT = float(rng.uniform(20, 60))
        aliases = [dT / k for k in range(1, 8) if dT / k >= 2.0]
        true = aliases[int(rng.integers(len(aliases)))]
        rho, erho = float(rng.uniform(0.5, 2.0)), None
        erho = 0.2 * rho
        rho_true = rho * (1 + rng.normal(0, 0.2))
        if rho_true <= 0:
            continue
        b = float(rng.uniform(0, 0.9))
        dur = float(M.transit_duration_days(np.array([true]), np.array([rho_true * M.RHO_SUN]), np.array([b]), 0.1)[0] * 24)
        dur_obs = dur * (1 + rng.normal(0, 0.1))
        rows = M.alias_duration_likelihood(aliases, dur_obs, 0.1 * dur_obs, rho, erho, n=2000, seed=int(rng.integers(1e9)))
        w = [r["weight_likelihood_only"] or 0 for r in rows]
        n += 1
        top += aliases[int(np.argmax(w))] == true
        wtrue.append(w[aliases.index(true)])
    chance = float(np.mean([1 / len([dT / k for k in range(1, 8) if dT / k >= 2.0]) for dT in rng.uniform(20, 60, 1000)]))
    print(f"\nL1 duration likelihood: true alias ranked first in {top / n:.2f} of {n} draws (chance ~{chance:.2f}); "
          f"median weight on the truth {np.median(wtrue):.2f}")
    assert top / n > 1.5 * chance


# ------------------------------------------------------------------ dilution census closure
def test_dilution_cap_bounds_every_planted_blend():
    rng = np.random.default_rng(9)
    worst = 0.0
    for _ in range(1000):
        k = int(rng.integers(1, 6))
        dg = rng.uniform(0, 8, k)
        rows = [{"source_id": "t", "ra": 10.0, "dec": 20.0, "phot_g_mean_mag": 10.0}] + [
            {"source_id": f"n{i}", "ra": 10.0 + float(rng.uniform(-40, 40)) / 3600, "dec": 20.0, "phot_g_mean_mag": 10.0 + float(g)}
            for i, g in enumerate(dg)]
        c = M.dilution_census(rows, "t", 10.0, ra=10.0, dec=20.0, aperture_arcsec=60, depth_ppm=None)
        f = 10 ** (-0.4 * dg)
        j = int(rng.integers(k))
        ecl = float(rng.uniform(0, 1))                       # neighbour j eclipsed by a fraction ecl
        observed = ecl * f[j] / (1 + f.sum())
        cap = next(x["max_depth_ppm_if_fully_eclipsed"] for x in c["neighbours"] if x["source_id"] == f"n{j}") * 1e-6
        worst = max(worst, observed / cap)
    print(f"\nL1 dilution closure: max observed/cap over 1000 planted blends = {worst:.4f}")
    assert worst <= 1 + 1e-9


# ------------------------------------------------------------------ secondary-eclipse false positives on red noise
def test_secondary_eclipse_false_positive_rate_on_red_noise():
    from cygnus.campaign import vet

    rng = np.random.default_rng(13)
    fp, n = 0, 0
    for _ in range(40):
        m = 12000
        t = 2459000.0 + np.arange(m) * CAD_S / 86400
        f = 1 + rng.normal(0, 8e-4, m) + _red_noise(rng, m, 4e-4, 0.08)
        lc = types.SimpleNamespace(t=t, ok=np.ones(m, bool), col={"PDCSAP_FLUX": f}, sector=1)
        t_ref = t[0] + 1.0
        periods = [float(p) for p in rng.uniform(1.0, 8.0, 10)]
        rows, _ = vet.secondary_eclipse_rows({"a": lc}, t_ref, periods, 2 / 24)
        if not rows:
            continue
        n += 1
        fp += any(r["secondary_depth_ppm"] > 4 * r["err_ppm"] for r in rows)
    print(f"\nL1 secondary eclipse: {n} red-noise light curves x 10 aliases; fraction with any >=4 sigma phase-0.5 dip = {fp / n:.3f}")
    assert n >= 35 and fp / n <= 0.15
