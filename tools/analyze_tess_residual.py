"""SUPERSEDED (2026-09-24): run `python -m cygnus.campaign run campaigns/tess-wasp12-residual-01.yaml` instead. The runner reproduces this
script exactly (checked on the real products; see docs/CAMPAIGNS.md) and records every step in the ledger.
Kept unchanged so the original record can still be reproduced as documented in its SEARCH_LOG.

Checksum-gated one-product TESS excursion triage; outputs are not detections."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter

MANIFEST_PRODUCTS = {
    "tess2019357164649-s0020-0000000086396382-0165-s_lc.fits": ("bf74a16f6e0c40b693a66de922e142d446cb44cee5bb7f26843062e436957f63", 1926720),
    "tess2021258175143-s0043-0000000086396382-0214-s_lc.fits": ("e3d5c6f76884014ec1dec1eb60f04eaf734330a7abd8eef99141f49df03b2493", 1811520),
}
PERIOD_D = 1.09141890100  # NASA Exoplanet Archive pscomppars, queried 2026-09-24
EPOCH_BJD = 2457607.51930500  # archive pl_tranmid; see report for epoch caveat


def robust_sigma(x):
    x = np.asarray(x, float)
    med = np.nanmedian(x)
    return 1.4826 * np.nanmedian(np.abs(x - med))


def local_resid(y, valid, seconds, window_days):
    # NaNs interpolated only for baseline estimation; returned residuals remain masked.
    idx = np.arange(y.size)
    good = valid & np.isfinite(y)
    filled = np.interp(idx, idx[good], y[good])
    width = max(3, int(round(window_days * 86400 / seconds)))
    if width % 2 == 0:
        width += 1
    base = median_filter(filled, size=width, mode="nearest")
    resid = y / base - 1.0
    resid[~good] = np.nan
    return resid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fits_path", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    p = a.fits_path
    if p.name not in MANIFEST_PRODUCTS:
        raise SystemExit(f"product not in pinned manifest allowlist: {p.name}")
    expected_sha, expected_bytes = MANIFEST_PRODUCTS[p.name]
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    if p.stat().st_size != expected_bytes or digest != expected_sha:
        raise SystemExit(f"manifest mismatch: bytes={p.stat().st_size} sha256={digest}")
    a.out.mkdir(parents=True, exist_ok=True)
    with fits.open(p, memmap=True) as hdul:
        hdr = dict(hdul[0].header)
        tab = hdul[1].data
        names = set(tab.names)
        required = {"TIME", "SAP_FLUX", "PDCSAP_FLUX", "QUALITY"}
        if not required <= names:
            raise SystemExit(f"missing columns: {sorted(required - names)}")
        time = np.asarray(tab["TIME"], float)
        sap = np.asarray(tab["SAP_FLUX"], float)
        pdc = np.asarray(tab["PDCSAP_FLUX"], float)
        quality = np.asarray(tab["QUALITY"], int)
        centroid_cols = [n for n in ("MOM_CENTR1", "MOM_CENTR2") if n in names]
        centroids = {n: np.asarray(tab[n], float) for n in centroid_cols}
        cadence = float(hdr.get("TIMEDEL", 120 / 86400)) * 86400
        basevalid = np.isfinite(time) & (quality == 0)
        finite = basevalid & np.isfinite(sap) & np.isfinite(pdc) & (sap != 0) & (pdc != 0)
        # Time is preserved as stored; no conversion beyond documented BJDREFI/F.
        bjdref = float(hdul[1].header.get("BJDREFI", 0)) + float(hdul[1].header.get("BJDREFF", 0))
        time_bjd = time + bjdref
        results = {"input": {"file": p.name, "bytes": p.stat().st_size, "sha256": digest},
                   "headers": {k: hdr.get(k) for k in ("OBJECT", "TICID", "SECTOR", "CAMERA", "CCD", "RA_OBJ", "DEC_OBJ", "DATE-OBS", "DATE-END", "TIMESYS", "TIMEUNIT", "TELESCOP", "INSTRUME", "FILTER")},
                   "table_header": {k: hdul[1].header.get(k) for k in ("BJDREFI", "BJDREFF", "TIMEZERO", "TIMESYS", "TIMEUNIT", "TUNIT1")},
                   "rows": int(len(time)), "quality_zero": int(np.count_nonzero(basevalid)), "usable": int(np.count_nonzero(finite)),
                   "time_min_stored": float(np.nanmin(time[finite])), "time_max_stored": float(np.nanmax(time[finite])),
                   "bjdref": bjdref, "time_scale": hdul[1].header.get("TIMESYS"), "cadence_seconds_header": cadence,
                   "coordinate_convention": "header RA_OBJ/DEC_OBJ as supplied; frame not independently established"}
        def runs(mask):
            ii = np.flatnonzero(mask)
            if not len(ii): return []
            cuts = np.flatnonzero(np.diff(ii) > 1) + 1
            return [g for g in np.split(ii, cuts) if len(g) >= 2]
        for days in (1.0, 2.0, 3.0):
            r_sap = local_resid(sap, finite, cadence, days)
            r_pdc = local_resid(pdc, finite, cadence, days)
            for label, rr in (("SAP", r_sap), ("PDCSAP", r_pdc)):
                sig = robust_sigma(rr[finite])
                neg = finite & np.isfinite(rr) & (rr < -5 * sig)
                for g in runs(neg):
                    epoch = float(np.nanmedian(time_bjd[g]))
                    phase = ((epoch - EPOCH_BJD) / PERIOD_D) % 1
                    event = {"detrend_days": days, "flux_type": label, "start_index": int(g[0]), "stop_index": int(g[-1]),
                             "n_cadences": int(len(g)), "start_time_stored": float(time[g[0]]), "end_time_stored": float(time[g[-1]]),
                             "mid_time_BJD_like": epoch, "phase_from_provisional_ephemeris": float(phase),
                             "median_fractional_residual": float(np.nanmedian(rr[g])), "robust_sigma_fraction": float(sig),
                             "min_quality": int(np.min(quality[g])), "centroids": {n: float(np.nanmedian(v[g])) for n,v in centroids.items()}}
                    results.setdefault("screened_excursions", []).append(event)
        # Save paired normalized residuals at 2 d; retain every quality-0 usable row.
        rs = local_resid(sap, finite, cadence, 2.0)
        rp = local_resid(pdc, finite, cadence, 2.0)
        out = np.column_stack((time, time_bjd, quality, sap, pdc, rs, rp))
        np.savetxt(a.out / "normalized_series.csv", out, delimiter=",", header="TIME_stored,BJD_like,QUALITY,SAP_FLUX,PDCSAP_FLUX,SAP_frac_resid_2d,PDCSAP_frac_resid_2d", comments="")
        # phase off-transit distribution supplies descriptive control scatter only.
        phase = ((time_bjd - EPOCH_BJD) / PERIOD_D) % 1
        control = finite & ((phase > 0.08) & (phase < 0.92))
        results["controls"] = {"definition": "same LC phase outside ±0.08-cycle window about provisional transit", "n": int(control.sum()),
                              "sap_control_robust_sigma": float(robust_sigma(rs[control])), "pdc_control_robust_sigma": float(robust_sigma(rp[control]))}
        results["interpretation_limit"] = "-5 robust-MAD threshold is an uncalibrated screen; no trial-factor or correlated-noise calibration."
    (a.out / "screen.json").write_text(json.dumps(results, indent=2, allow_nan=False), encoding="utf-8")
    print(json.dumps({"out": str(a.out), "sha256": digest, "rows": results["rows"], "usable": results["usable"], "excursion_rows": len(results.get("screened_excursions", []))}, indent=2))

if __name__ == "__main__":
    main()
