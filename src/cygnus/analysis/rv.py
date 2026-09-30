"""Epoch-RV orbit fits tied to a transit time. Units: km/s, days, radians."""

from __future__ import annotations

import numpy as np


def rv_template(time, period, transit, eccentricity=0.0, omega=0.0):
    """Unit-amplitude RV curve; zero velocity at transit for a circular orbit."""
    time = np.asarray(time, float)
    f_tr = np.pi / 2 - omega
    E_tr = 2 * np.arctan2(np.sqrt(1 - eccentricity) * np.sin(f_tr / 2), np.sqrt(1 + eccentricity) * np.cos(f_tr / 2))
    M_tr = E_tr - eccentricity * np.sin(E_tr)
    M = (2 * np.pi * (time - transit) / period + M_tr + np.pi) % (2 * np.pi) - np.pi
    E = M.copy()
    for _ in range(60):
        E -= np.clip((E - eccentricity * np.sin(E) - M) / (1 - eccentricity * np.cos(E)), -1, 1)
    if np.max(np.abs(E - eccentricity * np.sin(E) - M)) > 1e-8:
        raise ValueError("Kepler solver did not converge")
    f = 2 * np.arctan2(np.sqrt(1 + eccentricity) * np.sin(E / 2), np.sqrt(1 - eccentricity) * np.cos(E / 2))
    return np.cos(f + omega) + eccentricity * np.cos(omega)


def rv_linear_fit(rv, sigma, template, nuisance):
    rv, sigma = np.asarray(rv, float), np.asarray(sigma, float)
    D = np.column_stack([nuisance, template])
    W = D / sigma[:, None]
    coef = np.linalg.lstsq(W, rv / sigma, rcond=None)[0]
    r = rv - D @ coef
    cov = np.linalg.pinv(W.T @ W)
    return {"semiamplitude_kms": float(coef[-1]), "formal_error_kms": float(np.sqrt(cov[-1, -1])),
            "residual_rms_kms": float(np.sqrt(np.mean(r**2))), "chi2": float(np.sum((r / sigma) ** 2)),
            "dof": int(len(rv) - D.shape[1])}


def fit_transit_tied_orbit(time, rv, sigma, transit, periods, *, jitters_kms=(0.0,), fwhm=None,
                           eccentricity=0.0, omega=0.0):
    """Fit each trial period x jitter x nuisance model; reports the RV-FWHM correlation if given.

    Rows carry dof; fits with no spare dof are skipped. Never selects a period.
    """
    time, rv, sigma = (np.asarray(a, float) for a in (time, rv, sigma))
    corr = float(np.corrcoef(rv, np.asarray(fwhm, float))[0, 1]) if fwhm is not None else None
    nuisances = (("offset", np.ones((len(time), 1))),
                 ("offset+slope", np.column_stack([np.ones(len(time)), time - time.mean()])))
    out = []
    for P in periods:
        tmpl = rv_template(time, P, transit, eccentricity, omega)
        for j in jitters_kms:
            s = np.sqrt(sigma**2 + j**2)
            for name, nuis in nuisances:
                if len(time) - nuis.shape[1] - 1 < 1:
                    continue
                out.append({"period_days": P, "jitter_kms": j, "nuisance": name,
                            **rv_linear_fit(rv, s, tmpl, nuis)})
    return {"fits": out, "rv_fwhm_correlation": corr,
            "note": "conditional on the assumed orbit; not an alias exclusion or a mass"}
