"""Independent cached-TESS TPF check for the four surviving Cygnus leads.

This is a bounded follow-up reduction, not a replacement for a calibrated SPOC
pipeline.  It deliberately preserves the source FITS files and reports the
choice of aperture, event window, flank window, quality mask and bootstrap
seed.  Each event is measured with four pixel selections and a linear
per-pixel flank baseline.  The output is descriptive evidence for localization
and aperture dependence; it is not a search-wide false-alarm calculation.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS


ROOT = Path(r"D:\Ad Astra")
SCRATCH = Path(r"D:\AO_Artifacts\cygnus_scratch")
OUT = ROOT / "reports" / "lead-followup-2026-09-27" / "independent_tpf_results.json"
PIXEL_ARCSEC = 21.0
BOOTSTRAPS = 300
SEED = 20260927


LEADS = {
    "TOI-224.01": {
        "tic": 70797900,
        "ra": 1.977969,
        "dec": -29.979603,
        "events": {
            "S2_reference": (2458365.8437503786, 1.24729878),
            "E1_S29": (2459092.180262361, 1.24729878),
            "E2_S69": (2460197.471515978, 1.24729878),
            "E3_S96": (2460923.7950245654, 1.24729878),
            "E4_S106": (2461239.586615944, 1.24729878),
        },
    },
    "TOI-2666.01": {
        "tic": 170889511,
        "ra": 139.480865,
        "dec": -3.387525,
        "events": {
            "S35_reference": (2459259.1579404767, 1.156),
            "E1_S99": (2461049.164423826, 1.156),
        },
    },
    "TOI-3500.02": {
        "tic": 443666343,
        "ra": 186.816884,
        "dec": -29.832996,
        "events": {
            "S64_reference": (2460056.6956505855, 7.9079384),
            "E1_S90": (2460757.3198817656, 7.9079384),
            "E2_S101_rejected": (2461107.6406679475, 6.32635072),
        },
    },
    "TOI-7610.01": {
        "tic": 121341000,
        "ra": 129.250045,
        "dec": -3.530909,
        "events": {
            "S88_reference": (2460700.9700970678, 3.76367648),
            "E1_S99": (2461066.3486342016, 3.76367648),
        },
    },
}


def _target_tpf(lead: str, sector: int) -> Path:
    slug = {
        "TOI-224.01": "toi-224-01",
        "TOI-2666.01": "toi-2666-01",
        "TOI-3500.02": "toi-3500-02",
        "TOI-7610.01": "toi-7610-01",
    }[lead]
    folder = SCRATCH / f"campaign_{slug}" / "tpf"
    matches = sorted(folder.glob(f"*s{sector:04d}-*.fits"))
    if len(matches) != 1:
        raise FileNotFoundError(f"expected one target TPF for {lead} S{sector}, got {matches}")
    return matches[0]


def _event_selection(time: np.ndarray, mid: float, duration_h: float, quality: np.ndarray):
    duration = duration_h / 24.0
    good = (quality == 0) & np.isfinite(time)
    in_event = good & (np.abs(time - mid) <= duration * 0.4)
    flank = good & (np.abs(time - mid) > duration / 2.0 + 1.0 / 48.0)
    flank &= np.abs(time - mid) <= duration / 2.0 + max(duration, 0.25)
    return in_event, flank


def _centroid(image: np.ndarray, mask: np.ndarray):
    values = np.where(mask, np.maximum(image, 0.0), 0.0)
    total = float(values.sum())
    if not np.isfinite(total) or total <= 0:
        return None
    yy, xx = np.indices(values.shape)
    return [float((values * xx).sum() / total), float((values * yy).sum() / total)]


def _local_peak_centroid(image: np.ndarray, mask: np.ndarray):
    """Centroid positive weights in the 3x3 neighbourhood of the image peak."""
    masked = np.where(mask, image, -np.inf)
    if not np.any(np.isfinite(masked)):
        return None
    py, px = np.unravel_index(np.nanargmax(masked), masked.shape)
    ys = slice(max(0, py - 1), min(image.shape[0], py + 2))
    xs = slice(max(0, px - 1), min(image.shape[1], px + 2))
    local_mask = np.zeros_like(mask, dtype=bool)
    local_mask[ys, xs] = mask[ys, xs]
    return _centroid(image, local_mask)


def _linear_difference(time, flux, event, flank):
    x = time[flank]
    A = np.vstack([np.ones_like(x), x - time[event].mean()]).T
    coeff, *_ = np.linalg.lstsq(A, flux[flank].reshape(len(x), -1), rcond=None)
    baseline = coeff[0] + np.outer(time[event] - time[event].mean(), coeff[1]).mean(axis=0)
    return (baseline - flux[event].reshape(len(time[event]), -1).mean(axis=0)).reshape(flux.shape[1:])


def _measure(tpf: Path, target: dict, mid: float, duration_h: float, rng: np.random.Generator):
    with fits.open(tpf, memmap=False) as hdul:
        table = hdul[1].data
        time = np.asarray(table["TIME"], dtype=float)
        time += float(hdul[1].header.get("BJDREFI", 0.0)) + float(hdul[1].header.get("BJDREFF", 0.0))
        flux = np.asarray(table["FLUX"], dtype=float)
        quality = np.asarray(table["QUALITY"], dtype=int)
        aperture_flags = np.asarray(hdul[2].data, dtype=int)
        target_xy = WCS(hdul[2].header).world_to_pixel_values(target["ra"], target["dec"])

    event, flank = _event_selection(time, mid, duration_h, quality)
    finite = np.all(np.isfinite(flux.reshape(len(time), -1)), axis=1)
    event &= finite
    flank &= finite
    if event.sum() < 4 or flank.sum() < 10:
        return {"status": "not_tested", "event_cadences": int(event.sum()), "flank_cadences": int(flank.sum())}

    ny, nx = flux.shape[1:]
    yy, xx = np.indices((ny, nx))
    radius = np.hypot(xx - target_xy[0], yy - target_xy[1])
    masks = {
        "optimal_bit2": (aperture_flags & 2) > 0,
        "target_bit8": (aperture_flags & 8) > 0,
        "all_designated": (aperture_flags & 15) > 0,
        "target_radius_2pix": radius <= 2.0,
    }
    result = {
        "status": "done",
        "tpf": str(tpf),
        "mid_bjd_tdb": mid,
        "duration_h": duration_h,
        "event_cadences": int(event.sum()),
        "flank_cadences": int(flank.sum()),
        "quality_rule": "QUALITY == 0 and all TPF pixels finite",
        "target_pixel_xy": [float(target_xy[0]), float(target_xy[1])],
        "aperture_results": {},
    }
    event_image = flux[event].mean(axis=0)
    control_image = flux[flank].mean(axis=0)
    diff_image = _linear_difference(time, flux, event, flank)
    for name, mask in masks.items():
        baseline = control_image[mask].mean()
        event_mean = event_image[mask].mean()
        depth_ppm = (baseline - event_mean) / max(abs(baseline), 1e-12) * 1e6
        diff_centroid = _centroid(diff_image, mask)
        control_centroid = _centroid(control_image - np.nanmedian(control_image[~mask]) if np.any(~mask) else control_image, mask)
        local_diff_centroid = _local_peak_centroid(diff_image, mask)
        local_control_centroid = _local_peak_centroid(control_image, mask)
        offset = None
        if diff_centroid is not None and control_centroid is not None:
            offset = [diff_centroid[0] - control_centroid[0], diff_centroid[1] - control_centroid[1]]
        local_offset = None
        if local_diff_centroid is not None and local_control_centroid is not None:
            local_offset = [local_diff_centroid[0] - local_control_centroid[0], local_diff_centroid[1] - local_control_centroid[1]]

        boot_offsets = []
        local_boot_offsets = []
        event_indices = np.flatnonzero(event)
        flank_indices = np.flatnonzero(flank)
        for _ in range(BOOTSTRAPS):
            bi = rng.choice(event_indices, size=len(event_indices), replace=True)
            bf = rng.choice(flank_indices, size=len(flank_indices), replace=True)
            boot_event = flux[bi].mean(axis=0)
            boot_control = flux[bf].mean(axis=0)
            residual = boot_control - boot_event
            dc = _centroid(residual, mask)
            cc = _centroid(boot_control - np.nanmedian(boot_control[~mask]) if np.any(~mask) else boot_control, mask)
            if dc is not None and cc is not None:
                boot_offsets.append([dc[0] - cc[0], dc[1] - cc[1]])
            bdc = _local_peak_centroid(residual, mask)
            bcc = _local_peak_centroid(boot_control, mask)
            if bdc is not None and bcc is not None:
                local_boot_offsets.append([bdc[0] - bcc[0], bdc[1] - bcc[1]])
        boots = np.asarray(boot_offsets, dtype=float)
        sigma = boots.std(axis=0, ddof=1).tolist() if len(boots) > 10 else None
        local_boots = np.asarray(local_boot_offsets, dtype=float)
        local_sigma = local_boots.std(axis=0, ddof=1).tolist() if len(local_boots) > 10 else None
        offset_over_sigma = None
        if offset is not None and sigma is not None:
            denom = math.hypot(*sigma)
            offset_over_sigma = math.hypot(*offset) / denom if denom > 0 else None
        local_offset_over_sigma = None
        if local_offset is not None and local_sigma is not None:
            denom = math.hypot(*local_sigma)
            local_offset_over_sigma = math.hypot(*local_offset) / denom if denom > 0 else None
        result["aperture_results"][name] = {
            "pixels": int(mask.sum()),
            "depth_ppm_descriptive": float(depth_ppm),
            "difference_centroid_xy": diff_centroid,
            "control_centroid_xy": control_centroid,
            "offset_from_control_pix": offset,
            "offset_from_control_arcsec": math.hypot(*offset) * PIXEL_ARCSEC if offset else None,
            "bootstrap_offset_sigma_pix": sigma,
            "offset_over_bootstrap_sigma": offset_over_sigma,
            "bootstrap_valid": int(len(boots)),
            "local_peak_difference_centroid_xy": local_diff_centroid,
            "local_peak_control_centroid_xy": local_control_centroid,
            "local_peak_offset_from_control_pix": local_offset,
            "local_peak_offset_from_control_arcsec": math.hypot(*local_offset) * PIXEL_ARCSEC if local_offset else None,
            "local_peak_bootstrap_offset_sigma_pix": local_sigma,
            "local_peak_offset_over_bootstrap_sigma": local_offset_over_sigma,
            "local_peak_bootstrap_valid": int(len(local_boots)),
        }
    return result


def main():
    rng = np.random.default_rng(SEED)
    output = {
        "method": {
            "software": "reports/lead-followup-2026-09-27/independent_tpf_check.py",
            "bootstrap_draws": BOOTSTRAPS,
            "seed": SEED,
            "pixel_scale_arcsec": PIXEL_ARCSEC,
            "caveat": "descriptive cached-TPF reduction; no search-wide FAP, PRF fit, WCS registration uncertainty or independent sky epoch",
        },
        "leads": {},
    }
    for lead, target in LEADS.items():
        lead_result = {"tic": target["tic"], "events": {}}
        for label, (mid, duration_h) in target["events"].items():
            sector = int(label.split("S", 1)[1].split("_", 1)[0])
            path = _target_tpf(lead, sector)
            lead_result["events"][label] = _measure(path, target, mid, duration_h, rng)
        output["leads"][lead] = lead_result
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
