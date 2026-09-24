# Small TESS Campaign Report: WASP-12, Sector 20

**Run date:** 2026-09-24 UTC  
**Campaign type:** bounded software/recovery validation, not a novelty search  
**Evidence classification:** established target used as a validation case; this run itself is not a new candidate assessment.

## Executive result

A single MAST TESS SPOC 2-minute light curve for TIC 86396382 (WASP-12) was searched with a box least-squares (BLS) periodogram. The strongest grid peak is at **1.0914183 d**. Its fitted box has a **2.448 h** duration and **1.4228%** depth (14,228 ppm) in PDC-SAP flux. The feature is also present at the same ephemeris in SAP flux: BLS power 0.1500 and depth 1.3987%, versus 0.1551 and 1.4228% for PDC-SAP. This successful recovery of the well-known transiting system is a useful smoke test of the retrieval and basic extraction, not a discovery.

There were 18,954 light-curve rows; 16,551 finite, positive-flux, quality-zero cadences were analyzed. The data span 26.318 days. Timestamps are **BTJD = BJD − 2457000**, with `TIMESYS=TDB`; the FITS header gives 120-second cadence. The recovered grid period agrees with the expected approximately 1.09-day WASP-12 b signal, but this campaign did not perform a literature/ephemeris fit or refine the period.

## Ranked leads

| Rank | Target / product | Result | Evidence level | Main concern | Next test |
|---|---|---|---|---|---|
| Validation only | WASP-12 / TIC 86396382; TESS Sector 20; `tess2019357164649-s0020-0000000086396382-0165-s_lc.fits` | BLS P=1.0914183 d, duration=2.448 h, depth=1.4228%; SAP independently retains a similar box at this fitted ephemeris | Known-object recovery; **not a candidate** | One sector; no pixel-level or pointing/systematics audit; simplistic permutation null | Repeat at another TESS epoch and carry out centroid/difference-image, detrending, and calibrated injection/recovery tests |

No other targets were screened; there are no rejected astrophysical leads to rank. This tiny campaign makes no claim of completeness.

## Data provenance and reduction

- **Archive/release:** Mikulski Archive for Space Telescopes (MAST), TESS SPOC light curve, Sector 20, 120-s cadence.
- **Product ID:** `tess2019357164649-s0020-0000000086396382-0165-s_lc.fits`.
- **Product URL:** [MAST file download](https://mast.stsci.edu/api/v0.1/Download/file?uri=mast%3ATESS%2Fproduct%2Ftess2019357164649-s0020-0000000086396382-0165-s_lc.fits).
- **Selection provenance:** existing Tier-1 manifest records a TESS/SPOC timeseries cone selection around TIC 86396382, radius 0.05 degree, product subgroup LC. Product re-downloaded 2026-09-24 UTC into the configured scratch area; no bulk data retained in this report folder.
- **Coordinates:** FITS `RA_OBJ=97.6366528 deg`, `DEC_OBJ=+29.6722962 deg`; these are product-header coordinates. No epoch propagation or independent astrometric match was needed/performed.
- **Checksum:** observed SHA-256 `bf74a16f6e0c40b693a66de922e142d446cb44cee5bb7f26843062e436957f63`, exactly matching `docs/tier1_pack/MASTER_MANIFEST.csv`.
- **Time standard:** FITS extension reports `TIMESYS=TDB`, `BJDREFI=2457000`, `BJDREFF=0`; `TIME` values below are therefore BTJD. Usable timestamp range is 1842.509510–1868.827130 BTJD (baseline 26.317620 d).
- **Flux and filters:** used `PDCSAP_FLUX`, requiring finite positive flux and `QUALITY == 0`; excluded 2,403 rows from 18,954 on those combined criteria. Normalized by the median of retained flux. No additional outlier clipping or detrending was applied. SAP flux was median-normalized and checked at the PDC best-fit period/duration.

## Search and measurements

BLS was evaluated using Astropy `BoxLeastSquares`, likelihood objective, 5,000 linearly spaced trial periods from 0.5 through 5.0 d and six trial durations from 0.06 through 0.16 d. The maximum was at P=1.0914182837 d and transit epoch BTJD 1843.0045102. The grid period spacing is about 0.0009002 d (about 78 s), so the quoted period is only a coarse grid estimate. The epoch is the fitted periodic-box reference in BTJD, not a precision transit-time measurement. Fitted depth is 0.0142284 in normalized PDC-SAP flux; the reported BLS power is 0.15507 (algorithm objective, not a sigma).

A seeded permutation diagnostic shuffled the retained flux values relative to the observed timestamps 20 times and recorded each shuffled series' maximum over the *same* BLS search. None of the 20 null maxima reached the observed power; the 95th percentile of null maxima was 0.0003795. With the add-one estimator this is reported as 1/21 = 0.0476, which mostly reflects the coarse 20-trial Monte Carlo floor. It is **not a calibrated false-alarm probability**: shuffling destroys time-correlated stellar/instrumental noise, and 20 trials are inadequate for a tail estimate. Do not interpret it as astrophysical significance.

## Artifact audit / limitations

| Test | State | Result / limitation |
|---|---|---|
| Product integrity | passed | SHA-256 matches the existing manifest. |
| Cadence quality mask and finite-flux selection | passed | Exact selection and row counts recorded above. Quality flags were not individually decoded. |
| PDC versus SAP persistence | partial diagnostic | Comparable depth and BLS power at the PDC ephemeris; useful but not an independent reduction or pixel-level validation. |
| Alternative detrending/aperture | not tested | No custom detrending, aperture photometry, or extraction comparison. |
| Transit centroid / difference image / blend audit | not tested | No pixel-level data analyzed. |
| Pointing/centroid-jitter correlation | not tested | No engineering/centroid vectors inspected. |
| Red-noise-aware null or search-wide calibrated FAP | not tested | Permutation null is deliberately labeled inadequate above. |
| Independent epoch/instrument | not tested | One sector only. |
| Catalog/literature audit | not performed in this run | Target was chosen as a known-planet recovery test; no novelty inference is made. |

Accordingly, this is a positive **pipeline smoke test**, not a vetted candidate dossier. Reproducibly recovering a known signal does not demonstrate completeness, reliability against all artifacts, or sensitivity to isolated/nonperiodic transits.

## Reproduction and artifacts

From the worktree root, with the project science environment installed:

```powershell
& 'D:\AO_Artifacts\cygnus_scratch\venv\Scripts\python.exe' campaigns\run_wasp12_sector20.py
```

The script reuses the cached scratch FITS file if present, otherwise fetches the exact public MAST product; it fails closed if the SHA-256 differs. It writes machine-readable output to `campaigns/wasp12_sector20/results.json`. The scratch FITS is disposable under the existing worktree policy and is not a deliverable. The code records the random seed (20260925), search bounds, grid, masks, checksum, and software versions. Runtime environment observed: Python 3.13.3, NumPy 2.5.3, Astropy 8.0.1 (the script uses Astropy BLS/FITS); SciPy was present but not used. No unit test suite for this campaign-specific analysis was added; the run itself and checksum are the validation record.

## Recommended follow-up

1. Repeat the exact BLS and transit-window check on another, temporally separated SPOC sector for TIC 86396382; compare depth/shape while accounting for dilution and stellar variability.
2. Run a calibrated local injection/recovery grid in this light curve, including transit-like signals across periods/durations and realistic correlated noise; report completeness rather than relying on this single successful recovery.
3. Inspect pixel-level products and difference-image centroids, and compare SAP/PDC and at least one alternate detrending recipe before using this workflow on unknown targets.
4. For an actual discovery campaign, freeze a target pool and selection before viewing results, pin known-object watchlists, establish a null population, and record all exclusions/rejections.

## Addendum (2026-09-24, later): ledgered re-run

Re-run through the campaign runner (`python -m cygnus.campaign run campaigns/wasp12-sector20-recovery.yaml`; ledger runs #35–#37) with the same seed (20260925) and environment. `results.json` is identical to the original except its run timestamp. The catalogue cross-match found WASP-12 b (NASA Exoplanet Archive), TOI-1725.01 (disposition KP), the VSX entry and the SIMBAD system, as expected for a known-planet test; results are in the ledger `prior_art` table.
