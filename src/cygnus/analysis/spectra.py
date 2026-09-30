"""Relative spectral velocities: log-lambda shifts, gap-aware line-mask CCFs, and a mandatory precision gate.

A derived shift is NOT an RV until :func:`precision_gate` passes against an independent pipeline
(default 10 m/s). A failed gate is a stored negative result, not a caveat. Positive velocity = redshift.
No barycentric correction is applied here.
"""

from __future__ import annotations

import numpy as np

C_KMS = 299792.458


def spectral_shift(velocity, template, observed):
    """Relative logarithmic Doppler shift (km/s) of ``observed`` vs ``template`` on a uniform velocity grid."""
    from scipy.optimize import minimize_scalar
    from scipy.signal import correlate, correlation_lags

    template = np.asarray(template, float) - np.mean(template)  # continuum offset must not drive the CCF
    observed = np.asarray(observed, float) - np.mean(observed)
    step = float(np.median(np.diff(velocity)))
    cc = correlate(observed, template, mode="full", method="fft")
    lags = correlation_lags(len(observed), len(template)) * step
    sel = np.abs(lags) < 100.0
    peak = lags[sel][np.argmax(cc[sel])]
    keep = (velocity > velocity.min() + 110) & (velocity < velocity.max() - 110)
    if np.count_nonzero(keep) < 10:
        keep = (velocity > velocity.min() + 20) & (velocity < velocity.max() - 20)

    def obj(s):
        m = np.interp(velocity[keep] - s, velocity, template)
        y = observed[keep]
        return np.mean((y - np.dot(y, m) / np.dot(m, m) * m) ** 2)

    return float(minimize_scalar(obj, bounds=(peak - step, peak + step), method="bounded",
                                 options={"xatol": 1e-7}).x)


def covered_mask_lines(wave, mask, velocities, valid=None):
    """Mask lines fully inside the spectrum (and clear of invalid pixels) at every trial velocity."""
    beta = np.asarray(velocities) / C_KMS
    fac = np.sqrt((1 + beta) / (1 - beta))
    mask = np.asarray(mask, float)
    mask = mask[(mask[:, 0] * fac.min() > wave.min()) & (mask[:, 1] * fac.max() < wave.max())]
    if valid is not None:
        bad = np.concatenate(([0], np.cumsum(~np.asarray(valid, bool))))
        lo = np.clip(np.searchsorted(wave, mask[:, 0] * fac.min()) - 1, 0, len(wave))
        hi = np.clip(np.searchsorted(wave, mask[:, 1] * fac.max()) + 1, 0, len(wave))
        mask = mask[(bad[hi] - bad[lo]) == 0]
    return mask


def integrated_mask_ccf(wave, normalized_flux, mask, velocities, *, valid=None):
    """Integrate a binary line mask over piecewise-linear flux; detector gaps are excluded, never filled."""
    from scipy.integrate import cumulative_trapezoid

    wave, flux = np.asarray(wave, float), np.asarray(normalized_flux, float)
    if np.any(np.diff(wave) <= 0) or not np.all(np.isfinite(flux)):
        raise ValueError("Mask CCF requires sorted finite input")
    cum = cumulative_trapezoid(flux, wave, initial=0.0)
    beta = np.asarray(velocities) / C_KMS
    fac = np.sqrt((1 + beta) / (1 - beta))
    mask = covered_mask_lines(wave, mask, velocities, valid)
    if not len(mask):
        raise ValueError("No fully covered mask lines")

    def antiderivative(x):
        i = np.clip(np.searchsorted(wave, x) - 1, 0, len(wave) - 2)
        d = x - wave[i]
        slope = (flux[i + 1] - flux[i]) / (wave[i + 1] - wave[i])
        return cum[i] + flux[i] * d + 0.5 * slope * d**2

    out = []
    for f in fac:
        e = mask * f
        out.append(np.sum(antiderivative(e[:, 1]) - antiderivative(e[:, 0])) / np.sum(e[:, 1] - e[:, 0]))
    return np.array(out)


def fit_mask_ccf(velocities, ccf):
    """Descriptive Gaussian + slope; covariance is not a calibrated RV error."""
    from scipy.optimize import curve_fit

    v, y = np.asarray(velocities), np.asarray(ccf)
    peak = float(v[np.argmin(y)])
    k = np.abs(v - peak) < 15.0
    x, z = v[k], y[k]

    def model(t, base, slope, depth, center, width):
        return base + slope * (t - peak) - depth * np.exp(-0.5 * ((t - center) / width) ** 2)

    c, cov = curve_fit(model, x, z, p0=[float(np.median(z)), 0.0, float(np.ptp(z)), peak, 3.0],
                       bounds=([0.0, -0.1, 0.0, peak - 5.0, 0.3], [3.0, 0.1, 2.0, peak + 5.0, 15.0]), maxfev=10000)
    return {"center_kms": float(c[3]), "gaussian_sigma_kms": float(c[4]), "contrast": float(c[2]),
            "formal_fit_error_kms": float(np.sqrt(cov[3, 3])),
            "profile_rms": float(np.sqrt(np.mean((z - model(x, *c)) ** 2))), "n_profile_points": int(len(x)),
            "caveat": "CCF points correlated; fit covariance excludes pixel/calibration noise"}


def relative_ccf_shift(velocities, reference, observed, center):
    """Align a static asymmetric profile while profiling scale/offset/slope."""
    from scipy.interpolate import CubicSpline
    from scipy.optimize import minimize_scalar

    v, ref, obs = (np.asarray(a) for a in (velocities, reference, observed))
    k = np.abs(v - center) < 12.0
    x, y = v[k], obs[k]
    tmpl = CubicSpline(v, ref)

    def loss(s):
        D = np.column_stack([np.ones(len(x)), x - center, tmpl(x - s)])
        return float(np.mean((y - D @ np.linalg.lstsq(D, y, rcond=None)[0]) ** 2))

    fit = minimize_scalar(loss, bounds=(-3.0, 3.0), method="bounded", options={"xatol": 1e-8})
    return {"shift_kms": float(fit.x), "profile_rms": float(np.sqrt(fit.fun)),
            "state": "failed_boundary" if abs(fit.x) > 2.9 else "measured_profile",
            "caveat": "descriptive until empirical precision validation"}


def precision_gate(derived_kms, reference_kms, *, required_kms=0.010) -> dict:
    """Compare derived shifts to an independent pipeline (first epoch = zero point, excluded from RMS).

    ``state`` is 'passed' only if RMS < ``required_kms``. Consumers must refuse to label
    derived shifts as RVs, fit orbits or reject aliases unless state == 'passed'.
    """
    d, r = np.asarray(derived_kms, float), np.asarray(reference_kms, float)
    if len(d) != len(r) or len(d) < 3:
        return {"state": "not_tested", "reason": "need >= 3 matched epochs (zero point + 2 comparisons)"}
    diff = (d - d[0]) - (r - r[0])
    rms = float(np.sqrt(np.mean(diff[1:] ** 2)))
    return {"state": "passed" if rms < required_kms else "failed", "rms_difference_kms": rms,
            "required_precision_kms": required_kms, "difference_kms": diff.tolist(),
            "n_comparisons": int(len(diff) - 1)}


def require_gate(gate: dict) -> None:
    """Raise unless the precision gate passed; call before promoting derived shifts to RVs."""
    if gate.get("state") != "passed":
        raise PermissionError(f"precision gate {gate.get('state')}: derived shifts are not radial velocities")
