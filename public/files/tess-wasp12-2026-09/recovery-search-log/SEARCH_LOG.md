# Search Log — WASP-12 Sector 20 Validation

**Search date:** 2026-09-24 UTC  
**Search class:** one-product, known-signal recovery test; not a candidate survey.

## Scope and query

- Archive: MAST/STScI; TESS SPOC, Sector 20, TIC 86396382 (WASP-12).
- Product: `tess2019357164649-s0020-0000000086396382-0165-s_lc.fits`.
- Selection inherited from `docs/tier1_pack/MASTER_MANIFEST.csv`: TESS timeseries cone at RA 97.63665254°, Dec +29.67229542°, 0.05° radius, provenance SPOC; product subgroup LC.
- Exact download endpoint: `https://mast.stsci.edu/api/v0.1/Download/file?uri=mast%3ATESS%2Fproduct%2Ftess2019357164649-s0020-0000000086396382-0165-s_lc.fits`.
- SHA-256 expected from manifest and observed after retrieval: `bf74a16f6e0c40b693a66de922e142d446cb44cee5bb7f26843062e436957f63`.

## Screened data and cuts

One FITS light curve; 18,954 rows; quality-zero, finite, positive PDCSAP flux rows retained: 16,551. Excluded by combined quality/validity criteria: 2,403. Time span 1842.509510–1868.827130 BTJD, TDB; 120 s cadence. No other targets/products were processed and no candidate selection pool was constructed.

## Analysis

- Median normalize PDCSAP; BLS likelihood objective.
- Period 0.5–5.0 d, 5,000 linearly spaced trials; durations 0.06, 0.08, 0.10, 0.12, 0.14, 0.16 d.
- Best grid peak: P=1.0914182837 d, transit epoch=1843.0045102 BTJD, duration=2.448 h, depth=14,228 ppm, power=0.15507.
- SAP check at this same period and duration: power=0.14996, depth=13,987 ppm.
- Null diagnostic: 20 flux permutations (seed 20260925), each maximized over same BLS search. Zero null maxima >= observed; add-one Monte Carlo estimate 1/21=0.0476, floor-limited and not red-noise calibrated.

## Outcome and gaps

Recovered expected known transiting-system periodicity. This is a software/provenance smoke test, not a new object or vetted candidate. No null field population, search-wide completeness, injection/recovery calibration, detrending variants, independent epoch, pixel-level blend/centroid test, pointing audit, catalog sweep, or literature audit was performed. No rejected leads. Full interpretation and limitations are in `REPORT.md`; exact machine results are in `results.json`.
