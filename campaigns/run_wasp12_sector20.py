"""SUPERSEDED (2026-09-24): run `python -m cygnus.campaign run campaigns/wasp12-sector20-recovery.yaml` instead. The runner reproduces this
script exactly (checked on the real products; see docs/CAMPAIGNS.md) and records every step in the ledger.
Kept unchanged so the original record can still be reproduced as documented in its SEARCH_LOG.

Small validation campaign: recover WASP-12b in TESS Sector 20.

Downloads one public MAST SPOC product to CYGNUS scratch, verifies SHA-256,
then runs a bounded BLS search and permutation null. Not a discovery search.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares

PRODUCT = "tess2019357164649-s0020-0000000086396382-0165-s_lc.fits"
URL = "https://mast.stsci.edu/api/v0.1/Download/file?uri=mast%3ATESS%2Fproduct%2F" + PRODUCT
EXPECTED_SHA256 = "bf74a16f6e0c40b693a66de922e142d446cb44cee5bb7f26843062e436957f63"
SEED = 20260925


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out = root / "campaigns" / "wasp12_sector20"
    out.mkdir(parents=True, exist_ok=True)
    scratch = Path(os.environ.get("CYGNUS_SCRATCH", r"D:\AO_Artifacts\cygnus_scratch")) / "campaign_wasp12"
    scratch.mkdir(parents=True, exist_ok=True)
    local = scratch / PRODUCT
    if not local.exists():
        request = urllib.request.Request(URL, headers={"User-Agent": "Cygnus-reproducible-campaign/0.1"})
        with urllib.request.urlopen(request, timeout=90) as response, local.open("wb") as f:
            while True:
                data = response.read(1024 * 1024)
                if not data:
                    break
                f.write(data)
    digest = sha256(local)
    if digest != EXPECTED_SHA256:
        raise RuntimeError(f"SHA-256 mismatch for {PRODUCT}: {digest}")

    with fits.open(local, memmap=True) as hdul:
        h = hdul[0].header
        tab = hdul[1].data
        time = np.asarray(tab["TIME"], dtype=float)
        flux = np.asarray(tab["PDCSAP_FLUX"], dtype=float)
        quality = np.asarray(tab["QUALITY"], dtype=np.int64)
        sap = np.asarray(tab["SAP_FLUX"], dtype=float)
        ext = hdul[1].header
        cadence = ext.get("TIMEDEL")
        target = {k: h.get(k) for k in ("TICID", "OBJECT", "RA_OBJ", "DEC_OBJ", "SECTOR", "CAMERA", "CCD", "TSTART", "TSTOP")}
        time_metadata = {k: ext.get(k, h.get(k)) for k in ("TIMESYS", "BJDREFI", "BJDREFF", "TIMEUNIT", "TIMEDEL", "TIMEPIXR")}
    finite = np.isfinite(time) & np.isfinite(flux) & (flux > 0)
    good = finite & (quality == 0)
    t, f = time[good], flux[good]
    s = sap[good]
    if len(t) < 100:
        raise RuntimeError("Too few quality-zero cadences for this test")
    # Robust sector normalization; an affine offset does not change BLS shape.
    f = f / np.nanmedian(f)
    durations = np.arange(0.06, 0.161, 0.02)
    bls = BoxLeastSquares(t, f)
    periods = np.linspace(0.5, 5.0, 5000)
    result = bls.power(periods, durations, objective="likelihood")
    best = int(np.nanargmax(result.power))
    period = float(result.period[best])
    epoch = float(result.transit_time[best])
    duration = float(result.duration[best])
    depth = float(result.depth[best])

    # Naive permutation null, preserving actual times/gaps but destroying temporal structure.
    # Report this only as a diagnostic: it does not preserve correlated/red noise.
    rng = np.random.default_rng(SEED)
    null_max = []
    for _ in range(20):
        shuffled = rng.permutation(f)
        perm_result = BoxLeastSquares(t, shuffled).power(periods, durations, objective="likelihood")
        null_max.append(float(np.nanmax(perm_result.power)))
    null_max_arr = np.asarray(null_max)
    fap_emp = float((1 + np.sum(null_max_arr >= float(result.power[best]))) / (len(null_max_arr) + 1))

    # Compare SAP and PDCSAP at the fitted ephemeris; diagnostic against PDC-only artifact.
    s = s / np.nanmedian(s)
    sap_fit = BoxLeastSquares(t, s).power(np.array([period]), np.array([duration]), objective="likelihood")
    payload = {
        "campaign": "wasp12-sector20-validation", "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "archive": "MAST/STScI", "release_product": PRODUCT, "product_url": URL,
        "query_provenance": "Tier-1 manifest row: TESS/SPOC timeseries cone around TIC 86396382; 0.05 deg; LC product",
        "sha256": digest, "expected_sha256_manifest": EXPECTED_SHA256,
        "target_header": target, "time_metadata": time_metadata, "cadence_day": cadence, "n_rows": int(len(time)), 
        "n_quality_zero_finite": int(len(t)), "n_excluded_quality_or_nonfinite": int(len(time)-len(t)),
        "time_range_btjd": [float(np.min(t)), float(np.max(t))], "baseline_days": float(np.ptp(t)),
        "search": {"period_days": [0.5, 5.0], "period_grid_count": len(periods), "durations_days": durations.tolist(), "objective": "likelihood", "seed": SEED, "permutation_trials": 20},
        "best_bls": {"period_days": period, "transit_epoch_btjd": epoch, "duration_hours": duration*24,
                     "depth_fraction": depth, "depth_ppm": depth*1e6, "power": float(result.power[best]),
                     "empirical_permutation_fap": fap_emp, "null_max_power_95pct": float(np.quantile(null_max_arr, 0.95))},
        "sap_at_pdc_ephemeris": {"power": float(sap_fit.power[0]), "depth_fraction": float(sap_fit.depth[0])},
        "interpretation": "Known-planet recovery / software validation only; no novelty claim.",
        "caveats": ["Single sector; no independent epoch processed in this campaign.",
                    "Permutation null destroys time correlation and is not a calibrated red-noise false-alarm probability.",
                    "No pixel-level centroid/difference-image, aperture, or pointing-jitter artifact audit was run.",
                    "Reported period is a discovery-grid estimate, not a refined ephemeris."],
        "software": {"python": sys.version.split()[0], "numpy": np.__version__, "astropy": __import__("astropy").__version__},
    }
    (out / "results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
