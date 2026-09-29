"""Bounded two-source separability test for TOI-3500.02.

The test compares pixel-integrated Gaussian templates fixed at the refreshed
Gaia DR3 positions of the target and its 3.74-arcsec neighbour.  It scans a
declared PRF-width and common-registration grid and fits a planar background.
This is a sensitivity/identifiability test, not a calibrated TESS PRF model.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.special import erf


ROOT = Path(r"D:\Ad Astra")
SCRATCH = Path(r"D:\AO_Artifacts\cygnus_scratch\campaign_toi-3500-02\tpf")
CATALOG = ROOT / "reports" / "lead-followup-2026-09-27" / "catalog_followup.json"
OUT = ROOT / "reports" / "lead-followup-2026-09-27" / "toi3500_two_source_results.json"
TARGET_ID = 3471495415361216512
NEIGHBOUR_ID = 3471495419656596352
EVENTS = {
    "S64_reference": (64, 2460056.6956505855, 7.9079384),
    "E1_S90": (90, 2460757.3198817656, 7.9079384),
}
FWHM_GRID_PIX = np.arange(0.8, 2.01, 0.2)
REGISTRATION_GRID_PIX = (-0.10, 0.0, 0.10)


def catalog_rows() -> dict[int, dict[str, float]]:
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    result = payload["queries"]["gaia_dr3"]["result"]
    names = [item["name"] for item in result["metadata"]]
    rows = {int(row[0]): dict(zip(names, row)) for row in result["data"]}
    return {source_id: rows[source_id] for source_id in (TARGET_ID, NEIGHBOUR_ID)}


def target_tpf(sector: int) -> Path:
    matches = sorted(SCRATCH.glob(f"*s{sector:04d}-*.fits"))
    if len(matches) != 1:
        raise FileNotFoundError(f"expected one S{sector} TPF, got {matches}")
    return matches[0]


def event_selection(time: np.ndarray, mid: float, duration_h: float, quality: np.ndarray):
    duration = duration_h / 24.0
    good = (quality == 0) & np.isfinite(time)
    event = good & (np.abs(time - mid) <= duration * 0.4)
    flank = good & (np.abs(time - mid) > duration / 2.0 + 1.0 / 48.0)
    flank &= np.abs(time - mid) <= duration / 2.0 + max(duration, 0.25)
    return event, flank


def difference_and_noise(time, flux, event, flank):
    center = float(time[event].mean())
    x = time[flank]
    design = np.vstack([np.ones_like(x), x - center]).T
    flat = flux.reshape(len(time), -1)
    coeff, *_ = np.linalg.lstsq(design, flat[flank], rcond=None)
    event_baseline = coeff[0] + np.outer(time[event] - center, coeff[1]).mean(axis=0)
    difference = event_baseline - flat[event].mean(axis=0)
    flank_model = design @ coeff
    residual = flat[flank] - flank_model
    cadence_sigma = np.nanstd(residual, axis=0, ddof=2)
    noise = cadence_sigma * math.sqrt(1.0 / event.sum() + 1.0 / flank.sum())
    positive = noise[np.isfinite(noise) & (noise > 0)]
    floor = float(np.nanmedian(positive)) if positive.size else 1.0
    noise = np.where(np.isfinite(noise) & (noise > floor * 0.05), noise, floor)
    return difference.reshape(flux.shape[1:]), noise.reshape(flux.shape[1:])


def integrated_gaussian(xx, yy, x0, y0, fwhm):
    sigma = fwhm / 2.354820045
    scale = math.sqrt(2.0) * sigma
    xpart = 0.5 * (erf((xx + 0.5 - x0) / scale) - erf((xx - 0.5 - x0) / scale))
    ypart = 0.5 * (erf((yy + 0.5 - y0) / scale) - erf((yy - 0.5 - y0) / scale))
    model = xpart * ypart
    return model / model.sum()


def weighted_fit(values, noise, columns):
    design = np.column_stack(columns)
    weighted_design = design / noise[:, None]
    weighted_values = values / noise
    coeff, *_ = np.linalg.lstsq(weighted_design, weighted_values, rcond=None)
    residual = weighted_values - weighted_design @ coeff
    return coeff, float(residual @ residual)


def residualized_source_correlation(source_a, source_b, background, noise):
    wb = background / noise[:, None]
    wa = source_a / noise
    wn = source_b / noise
    proj_a = wa - wb @ np.linalg.lstsq(wb, wa, rcond=None)[0]
    proj_n = wn - wb @ np.linalg.lstsq(wb, wn, rcond=None)[0]
    denom = np.linalg.norm(proj_a) * np.linalg.norm(proj_n)
    corr = float((proj_a @ proj_n) / denom) if denom else float("nan")
    condition = float(np.linalg.cond(np.column_stack([proj_a, proj_n])))
    return corr, condition


def measure(path: Path, mid: float, duration_h: float, rows: dict[int, dict[str, float]]):
    with fits.open(path, memmap=False) as hdul:
        table = hdul[1].data
        time = np.asarray(table["TIME"], dtype=float)
        time += float(hdul[1].header.get("BJDREFI", 0.0)) + float(hdul[1].header.get("BJDREFF", 0.0))
        flux = np.asarray(table["FLUX"], dtype=float)
        quality = np.asarray(table["QUALITY"], dtype=int)
        wcs = WCS(hdul[2].header)

    event, flank = event_selection(time, mid, duration_h, quality)
    finite = np.all(np.isfinite(flux.reshape(len(time), -1)), axis=1)
    event &= finite
    flank &= finite
    difference, noise = difference_and_noise(time, flux, event, flank)

    target = rows[TARGET_ID]
    neighbour = rows[NEIGHBOUR_ID]
    target_xy = np.asarray(wcs.world_to_pixel_values(target["ra"], target["dec"]), dtype=float)
    neighbour_xy = np.asarray(wcs.world_to_pixel_values(neighbour["ra"], neighbour["dec"]), dtype=float)
    yy, xx = np.indices(difference.shape)
    midpoint = (target_xy + neighbour_xy) / 2.0
    fit_mask = np.hypot(xx - midpoint[0], yy - midpoint[1]) <= 3.0
    fit_mask &= np.isfinite(difference) & np.isfinite(noise)
    values = difference[fit_mask]
    sigma_values = noise[fit_mask]
    xvalues = xx[fit_mask].astype(float)
    yvalues = yy[fit_mask].astype(float)
    background = np.column_stack(
        [
            np.ones(fit_mask.sum()),
            xvalues - midpoint[0],
            yvalues - midpoint[1],
        ]
    )

    trials = []
    for fwhm in FWHM_GRID_PIX:
        for dx in REGISTRATION_GRID_PIX:
            for dy in REGISTRATION_GRID_PIX:
                t_model = integrated_gaussian(xx, yy, target_xy[0] + dx, target_xy[1] + dy, fwhm)[fit_mask]
                n_model = integrated_gaussian(xx, yy, neighbour_xy[0] + dx, neighbour_xy[1] + dy, fwhm)[fit_mask]
                t_coeff, t_chi2 = weighted_fit(values, sigma_values, [t_model, *background.T])
                n_coeff, n_chi2 = weighted_fit(values, sigma_values, [n_model, *background.T])
                both_coeff, both_chi2 = weighted_fit(values, sigma_values, [t_model, n_model, *background.T])
                corr, condition = residualized_source_correlation(
                    t_model, n_model, background, sigma_values
                )
                trials.append(
                    {
                        "fwhm_pix": float(fwhm),
                        "registration_dx_pix": dx,
                        "registration_dy_pix": dy,
                        "target_only_amplitude": float(t_coeff[0]),
                        "target_only_chi2": t_chi2,
                        "neighbour_only_amplitude": float(n_coeff[0]),
                        "neighbour_only_chi2": n_chi2,
                        "delta_chi2_neighbour_minus_target": n_chi2 - t_chi2,
                        "two_source_target_amplitude": float(both_coeff[0]),
                        "two_source_neighbour_amplitude": float(both_coeff[1]),
                        "two_source_chi2": both_chi2,
                        "source_template_correlation": corr,
                        "source_template_condition": condition,
                    }
                )

    best_target = min(trials, key=lambda row: row["target_only_chi2"])
    best_neighbour = min(trials, key=lambda row: row["neighbour_only_chi2"])
    best_two = min(trials, key=lambda row: row["two_source_chi2"])
    deltas = np.asarray([row["delta_chi2_neighbour_minus_target"] for row in trials])
    correlations = np.asarray([row["source_template_correlation"] for row in trials])
    conditions = np.asarray([row["source_template_condition"] for row in trials])
    return {
        "tpf": str(path),
        "mid_bjd_tdb": mid,
        "duration_h": duration_h,
        "event_cadences": int(event.sum()),
        "flank_cadences": int(flank.sum()),
        "fit_pixels": int(fit_mask.sum()),
        "target_pixel_xy": target_xy.tolist(),
        "neighbour_pixel_xy": neighbour_xy.tolist(),
        "separation_pix": float(np.linalg.norm(target_xy - neighbour_xy)),
        "separation_arcsec_from_gaia": 3.739111999455713,
        "best_target_only": best_target,
        "best_neighbour_only": best_neighbour,
        "best_two_source": best_two,
        "grid_summary": {
            "trials": len(trials),
            "target_favoured_fraction": float(np.mean(deltas > 0)),
            "delta_chi2_neighbour_minus_target_min": float(deltas.min()),
            "delta_chi2_neighbour_minus_target_median": float(np.median(deltas)),
            "delta_chi2_neighbour_minus_target_max": float(deltas.max()),
            "source_template_correlation_min": float(np.nanmin(correlations)),
            "source_template_correlation_max": float(np.nanmax(correlations)),
            "source_template_condition_min": float(np.nanmin(conditions)),
            "source_template_condition_max": float(np.nanmax(conditions)),
        },
        "interpretation_rule": (
            "A source assignment is inconclusive when target-vs-neighbour preference "
            "changes over the declared PRF/registration grid or the residualized source "
            "templates are nearly collinear; chi-square values are descriptive because "
            "the Gaussian template is not the calibrated sector/camera/CCD TESS PRF."
        ),
    }


def main() -> None:
    rows = catalog_rows()
    output = {
        "method": {
            "software": str(Path(__file__).relative_to(ROOT)).replace("\\", "/"),
            "gaia_source": str(CATALOG.relative_to(ROOT)).replace("\\", "/"),
            "gaia_release": "DR3",
            "prf_model": "pixel-integrated circular Gaussian sensitivity grid",
            "fwhm_grid_pix": FWHM_GRID_PIX.tolist(),
            "registration_grid_pix": list(REGISTRATION_GRID_PIX),
            "background": "constant plus x/y plane",
            "quality_rule": "QUALITY == 0 and all TPF pixels finite",
            "caveat": "not a calibrated TESS PRF; descriptive source-identifiability test",
        },
        "events": {},
    }
    for label, (sector, mid, duration_h) in EVENTS.items():
        output["events"][label] = measure(target_tpf(sector), mid, duration_h, rows)
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
