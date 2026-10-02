<!-- cygnus:generated-draft -->
# Known-object test, TOI-3559.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3559-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5084, calibrate_screen #5070, event_census #5080, fetch_independent #5083, fetch_products #5067, known_signal_recovery #5073, moving_objects #5082, period_aliases #5081, prior_art #5088, residual_screen #5079, stellar_context #5078, variability_guard #5085
- Runner finished (UTC): 2026-09-30T22:59:50Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3559.01 (BJD 2459770.2538: recovered, depth 7193 ± 367 ppm (catalogue 8273 ppm); BJD 2459772.7940: recovered, depth 6782 ± 346 ppm (catalogue 8273 ppm); BJD 2459775.3343: recovered, depth 6450 ± 385 ppm (catalogue 8273 ppm); BJD 2459777.8745: recovered, depth 5925 ± 391 ppm (catalogue 8273 ppm); BJD 2459780.4147: recovered, depth 7176 ± 372 ppm (catalogue 8273 ppm); BJD 2459782.9550: gap (catalogue 8273 ppm); BJD 2459785.4952: recovered, depth 5695 ± 342 ppm (catalogue 8273 ppm); BJD 2459788.0354: recovered, depth 6178 ± 355 ppm (catalogue 8273 ppm); BJD 2459790.5756: recovered, depth 6772 ± 322 ppm (catalogue 8273 ppm); BJD 2459793.1159: recovered, depth 6298 ± 331 ppm (catalogue 8273 ppm); BJD 2459795.6561: recovered, depth 5339 ± 365 ppm (catalogue 8273 ppm); BJD 2459422.2425: recovered, depth 6156 ± 323 ppm (catalogue 8273 ppm); BJD 2459424.7827: recovered, depth 5933 ± 355 ppm (catalogue 8273 ppm); BJD 2459427.3229: recovered, depth 6892 ± 356 ppm (catalogue 8273 ppm); BJD 2459429.8632: recovered, depth 6406 ± 366 ppm (catalogue 8273 ppm); BJD 2459432.4034: recovered, depth 4944 ± 337 ppm (catalogue 8273 ppm); BJD 2459434.9436: recovered, depth 8379 ± 330 ppm (catalogue 8273 ppm); BJD 2459437.4839: recovered, depth 6442 ± 316 ppm (catalogue 8273 ppm); BJD 2459440.0241: recovered, depth 5936 ± 350 ppm (catalogue 8273 ppm); BJD 2459442.5643: recovered, depth 5857 ± 369 ppm (catalogue 8273 ppm); BJD 2459445.1045: recovered, depth 7150 ± 338 ppm (catalogue 8273 ppm); BJD 2459798.1963: recovered, depth 6353 ± 340 ppm (catalogue 8273 ppm); BJD 2459800.7366: recovered, depth 6902 ± 351 ppm (catalogue 8273 ppm); BJD 2459803.2768: recovered, depth 5265 ± 351 ppm (catalogue 8273 ppm); BJD 2459805.8170: recovered, depth 7270 ± 338 ppm (catalogue 8273 ppm); BJD 2459808.3573: recovered, depth 5152 ± 378 ppm (catalogue 8273 ppm); BJD 2459810.8975: partial, depth 3450 ± 400 ppm (catalogue 8273 ppm); BJD 2459813.4377: recovered, depth 6637 ± 335 ppm (catalogue 8273 ppm); BJD 2459815.9779: not recovered, depth 4884 ± 349 ppm (catalogue 8273 ppm); BJD 2459818.5182: recovered, depth 6891 ± 356 ppm (catalogue 8273 ppm); BJD 2459821.0584: recovered, depth 6014 ± 362 ppm (catalogue 8273 ppm); BJD 2459823.5986: recovered, depth 4260 ± 374 ppm (catalogue 8273 ppm); BJD 2460341.8053: gap (catalogue 8273 ppm); BJD 2460344.3455: recovered, depth 6014 ± 363 ppm (catalogue 8273 ppm); BJD 2460346.8857: recovered, depth 5340 ± 341 ppm (catalogue 8273 ppm); BJD 2460349.4260: recovered, depth 6589 ± 325 ppm (catalogue 8273 ppm); BJD 2460351.9662: recovered, depth 5746 ± 307 ppm (catalogue 8273 ppm); BJD 2460354.5064: recovered, depth 5649 ± 323 ppm (catalogue 8273 ppm); BJD 2460357.0466: recovered, depth 6927 ± 402 ppm (catalogue 8273 ppm); BJD 2460359.5869: recovered, depth 5948 ± 347 ppm (catalogue 8273 ppm); BJD 2460362.1271: recovered, depth 6758 ± 339 ppm (catalogue 8273 ppm); BJD 2460364.6673: recovered, depth 6134 ± 335 ppm (catalogue 8273 ppm); BJD 2460367.2076: recovered, depth 7180 ± 332 ppm (catalogue 8273 ppm); BJD 2460506.9201: recovered, depth 4169 ± 396 ppm (catalogue 8273 ppm); BJD 2460509.4604: recovered, depth 6189 ± 371 ppm (catalogue 8273 ppm); BJD 2460512.0006: recovered, depth 7611 ± 367 ppm (catalogue 8273 ppm); BJD 2460514.5408: recovered, depth 5995 ± 362 ppm (catalogue 8273 ppm); BJD 2460517.0811: recovered, depth 6651 ± 385 ppm (catalogue 8273 ppm); BJD 2460519.6213: gap (catalogue 8273 ppm); BJD 2460522.1615: not recovered, depth 5486 ± 340 ppm (catalogue 8273 ppm); BJD 2460524.7017: recovered, depth 8151 ± 359 ppm (catalogue 8273 ppm); BJD 2460527.2420: partial, depth 5455 ± 371 ppm (catalogue 8273 ppm); BJD 2460529.7822: recovered, depth 7358 ± 343 ppm (catalogue 8273 ppm); BJD 2460532.3224: recovered, depth 7520 ± 376 ppm (catalogue 8273 ppm); BJD 2460534.8627: recovered, depth 6077 ± 342 ppm (catalogue 8273 ppm); BJD 2460537.4029: recovered, depth 7341 ± 336 ppm (catalogue 8273 ppm); BJD 2460539.9431: recovered, depth 5787 ± 324 ppm (catalogue 8273 ppm); BJD 2460542.4833: partial, depth 5943 ± 356 ppm (catalogue 8273 ppm); BJD 2460545.0236: recovered, depth 5365 ± 330 ppm (catalogue 8273 ppm); BJD 2460547.5638: recovered, depth 5437 ± 342 ppm (catalogue 8273 ppm); BJD 2460550.1040: recovered, depth 7006 ± 347 ppm (catalogue 8273 ppm); BJD 2460552.6443: recovered, depth 6894 ± 341 ppm (catalogue 8273 ppm); BJD 2460555.1845: recovered, depth 6442 ± 334 ppm (catalogue 8273 ppm); BJD 2460557.7247: recovered, depth 6922 ± 336 ppm (catalogue 8273 ppm)).
Outside the catalogued epoch the screen left 27 threshold entries forming **14 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3559.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 184468386 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 296.381383 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 39.959925 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459770.25382 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.5402287 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8272.7904433 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.3204775 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.5948 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-07 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | lightcurve | 54 | True | `36822a593b001657` | True |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | lightcurve | 41 | False | `ad5236df364d4f15` | True |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | lightcurve | 55 | False | `355096aafb1587cf` | True |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | lightcurve | 75 | False | `d99d974c91432b71` | True |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | lightcurve | 81 | False | `50c7c7f78021c759` | True |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | lightcurve | 82 | False | `40ba6aab5e151ce5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459770.25382 | recovered | 70 | 7193 ± 367 | 8273 | -0.16 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459772.79405 | recovered | 70 | 6782 ± 346 | 8273 | 0.06 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459775.33428 | recovered | 70 | 6450 ± 385 | 8273 | -0.03 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459777.87451 | recovered | 69 | 5925 ± 391 | 8273 | 0.03 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459780.41473 | recovered | 69 | 7176 ± 372 | 8273 | -0.00 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459782.95496 | gap | 0 | — | 8273 | — |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459785.49519 | recovered | 69 | 5695 ± 342 | 8273 | 0.28 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459788.03542 | recovered | 69 | 6178 ± 355 | 8273 | -0.01 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459790.57565 | recovered | 69 | 6772 ± 322 | 8273 | 0.34 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459793.11588 | recovered | 69 | 6298 ± 331 | 8273 | -0.06 |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459795.65611 | recovered | 69 | 5339 ± 365 | 8273 | -0.14 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459422.24249 | recovered | 69 | 6156 ± 323 | 8273 | -0.25 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459424.78272 | recovered | 69 | 5933 ± 355 | 8273 | 0.10 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459427.32295 | recovered | 69 | 6892 ± 356 | 8273 | -0.11 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459429.86317 | recovered | 70 | 6406 ± 366 | 8273 | 0.02 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459432.40340 | recovered | 70 | 4944 ± 337 | 8273 | 0.17 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459434.94363 | recovered | 70 | 8379 ± 330 | 8273 | -0.11 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459437.48386 | recovered | 70 | 6442 ± 316 | 8273 | -0.04 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459440.02409 | recovered | 70 | 5936 ± 350 | 8273 | 0.03 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459442.56432 | recovered | 70 | 5857 ± 369 | 8273 | 0.08 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459445.10455 | recovered | 70 | 7150 ± 338 | 8273 | 0.11 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459798.19634 | recovered | 70 | 6353 ± 340 | 8273 | 0.32 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459800.73656 | recovered | 70 | 6902 ± 351 | 8273 | -0.21 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459803.27679 | recovered | 70 | 5265 ± 351 | 8273 | 0.09 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459805.81702 | recovered | 70 | 7270 ± 338 | 8273 | -0.09 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459808.35725 | recovered | 70 | 5152 ± 378 | 8273 | -0.07 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459810.89748 | partial | 52 | 3450 ± 400 | 8273 | 0.26 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459813.43771 | recovered | 70 | 6637 ± 335 | 8273 | -0.16 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459815.97794 | not_recovered | 70 | 4884 ± 349 | 8273 | — |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459818.51817 | recovered | 70 | 6891 ± 356 | 8273 | 0.03 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459821.05839 | recovered | 69 | 6014 ± 362 | 8273 | -0.44 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 2459823.59862 | recovered | 70 | 4260 ± 374 | 8273 | 0.22 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460341.80528 | gap | 0 | — | 8273 | — |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460344.34551 | recovered | 70 | 6014 ± 363 | 8273 | -0.00 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460346.88573 | recovered | 70 | 5340 ± 341 | 8273 | -0.16 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460349.42596 | recovered | 70 | 6589 ± 325 | 8273 | 0.10 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460351.96619 | recovered | 70 | 5746 ± 307 | 8273 | 0.14 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460354.50642 | recovered | 70 | 5649 ± 323 | 8273 | 0.05 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460357.04665 | recovered | 70 | 6927 ± 402 | 8273 | -0.18 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460359.58688 | recovered | 70 | 5948 ± 347 | 8273 | 0.11 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460362.12711 | recovered | 70 | 6758 ± 339 | 8273 | -0.06 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460364.66734 | recovered | 69 | 6134 ± 335 | 8273 | -0.09 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460367.20756 | recovered | 69 | 7180 ± 332 | 8273 | 0.18 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460506.92014 | recovered | 70 | 4169 ± 396 | 8273 | -0.52 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460509.46037 | recovered | 70 | 6189 ± 371 | 8273 | 0.02 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460512.00060 | recovered | 70 | 7611 ± 367 | 8273 | -0.07 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460514.54083 | recovered | 70 | 5995 ± 362 | 8273 | -0.63 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460517.08106 | recovered | 70 | 6651 ± 385 | 8273 | -0.23 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460519.62129 | gap | 0 | — | 8273 | — |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460522.16152 | not_recovered | 70 | 5486 ± 340 | 8273 | — |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460524.70174 | recovered | 70 | 8151 ± 359 | 8273 | -0.16 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460527.24197 | partial | 70 | 5455 ± 371 | 8273 | -0.39 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460529.78220 | recovered | 69 | 7358 ± 343 | 8273 | 0.06 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 2460532.32243 | recovered | 69 | 7520 ± 376 | 8273 | -0.12 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460534.86266 | recovered | 69 | 6077 ± 342 | 8273 | -0.00 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460537.40289 | recovered | 69 | 7341 ± 336 | 8273 | 0.15 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460539.94312 | recovered | 69 | 5787 ± 324 | 8273 | -0.27 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460542.48334 | partial | 69 | 5943 ± 356 | 8273 | 0.11 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460545.02357 | recovered | 67 | 5365 ± 330 | 8273 | 0.22 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460547.56380 | recovered | 69 | 5437 ± 342 | 8273 | -0.10 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460550.10403 | recovered | 69 | 7006 ± 347 | 8273 | 0.11 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460552.64426 | recovered | 69 | 6894 ± 341 | 8273 | -0.19 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460555.18449 | recovered | 69 | 6442 ± 334 | 8273 | -0.22 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 2460557.72472 | recovered | 69 | 6922 ± 336 | 8273 | -0.17 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022217014003-s0055-0000000184468386-0242-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024196212429-s0081-0000000184468386-0276-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024223182411-s0082-0000000184468386-0278-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459425.53636 | -0.00898 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.92180 | -0.01017 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.00791 | -0.00949 | 2 | SAP | 1, 2, 3 | no |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459420.87939 | -0.00842 | 2 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.57875 | -0.00842 | 2 | SAP | 2, 3 | no |
| `tess2021204101404-s0041-0000000184468386-0212-s_lc.fits` | 2459441.85714 | -0.00779 | 2 | PDCSAP | 1 | no |
| `tess2022190063128-s0054-0000000184468386-0227-s_lc.fits` | 2459773.47490 | -0.00775 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.62180 | -0.00752 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.78014 | -0.00689 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.91069 | -0.00678 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.13291 | -0.00638 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.93569 | -0.00631 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.81347 | -0.00626 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000184468386-0270-s_lc.fits` | 2460345.43430 | -0.00622 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3559.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:59:37Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:59:41Z: TOI-3559.01 (TIC 184468386, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:59:44Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:59:47Z: TOI-3559 (*); TOI-3559.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459770.2538: recovered, depth 7193 ± 367 ppm (catalogue 8273 ppm); BJD 2459772.7940: recovered, depth 6782 ± 346 ppm (catalogue 8273 ppm); BJD 2459775.3343: recovered, depth 6450 ± 385 ppm (catalogue 8273 ppm); BJD 2459777.8745: recovered, depth 5925 ± 391 ppm (catalogue 8273 ppm); BJD 2459780.4147: recovered, depth 7176 ± 372 ppm (catalogue 8273 ppm); BJD 2459782.9550: gap (catalogue 8273 ppm); BJD 2459785.4952: recovered, depth 5695 ± 342 ppm (catalogue 8273 ppm); BJD 2459788.0354: recovered, depth 6178 ± 355 ppm (catalogue 8273 ppm); BJD 2459790.5756: recovered, depth 6772 ± 322 ppm (catalogue 8273 ppm); BJD 2459793.1159: recovered, depth 6298 ± 331 ppm (catalogue 8273 ppm); BJD 2459795.6561: recovered, depth 5339 ± 365 ppm (catalogue 8273 ppm); BJD 2459422.2425: recovered, depth 6156 ± 323 ppm (catalogue 8273 ppm); BJD 2459424.7827: recovered, depth 5933 ± 355 ppm (catalogue 8273 ppm); BJD 2459427.3229: recovered, depth 6892 ± 356 ppm (catalogue 8273 ppm); BJD 2459429.8632: recovered, depth 6406 ± 366 ppm (catalogue 8273 ppm); BJD 2459432.4034: recovered, depth 4944 ± 337 ppm (catalogue 8273 ppm); BJD 2459434.9436: recovered, depth 8379 ± 330 ppm (catalogue 8273 ppm); BJD 2459437.4839: recovered, depth 6442 ± 316 ppm (catalogue 8273 ppm); BJD 2459440.0241: recovered, depth 5936 ± 350 ppm (catalogue 8273 ppm); BJD 2459442.5643: recovered, depth 5857 ± 369 ppm (catalogue 8273 ppm); BJD 2459445.1045: recovered, depth 7150 ± 338 ppm (catalogue 8273 ppm); BJD 2459798.1963: recovered, depth 6353 ± 340 ppm (catalogue 8273 ppm); BJD 2459800.7366: recovered, depth 6902 ± 351 ppm (catalogue 8273 ppm); BJD 2459803.2768: recovered, depth 5265 ± 351 ppm (catalogue 8273 ppm); BJD 2459805.8170: recovered, depth 7270 ± 338 ppm (catalogue 8273 ppm); BJD 2459808.3573: recovered, depth 5152 ± 378 ppm (catalogue 8273 ppm); BJD 2459810.8975: partial, depth 3450 ± 400 ppm (catalogue 8273 ppm); BJD 2459813.4377: recovered, depth 6637 ± 335 ppm (catalogue 8273 ppm); BJD 2459815.9779: not recovered, depth 4884 ± 349 ppm (catalogue 8273 ppm); BJD 2459818.5182: recovered, depth 6891 ± 356 ppm (catalogue 8273 ppm); BJD 2459821.0584: recovered, depth 6014 ± 362 ppm (catalogue 8273 ppm); BJD 2459823.5986: recovered, depth 4260 ± 374 ppm (catalogue 8273 ppm); BJD 2460341.8053: gap (catalogue 8273 ppm); BJD 2460344.3455: recovered, depth 6014 ± 363 ppm (catalogue 8273 ppm); BJD 2460346.8857: recovered, depth 5340 ± 341 ppm (catalogue 8273 ppm); BJD 2460349.4260: recovered, depth 6589 ± 325 ppm (catalogue 8273 ppm); BJD 2460351.9662: recovered, depth 5746 ± 307 ppm (catalogue 8273 ppm); BJD 2460354.5064: recovered, depth 5649 ± 323 ppm (catalogue 8273 ppm); BJD 2460357.0466: recovered, depth 6927 ± 402 ppm (catalogue 8273 ppm); BJD 2460359.5869: recovered, depth 5948 ± 347 ppm (catalogue 8273 ppm); BJD 2460362.1271: recovered, depth 6758 ± 339 ppm (catalogue 8273 ppm); BJD 2460364.6673: recovered, depth 6134 ± 335 ppm (catalogue 8273 ppm); BJD 2460367.2076: recovered, depth 7180 ± 332 ppm (catalogue 8273 ppm); BJD 2460506.9201: recovered, depth 4169 ± 396 ppm (catalogue 8273 ppm); BJD 2460509.4604: recovered, depth 6189 ± 371 ppm (catalogue 8273 ppm); BJD 2460512.0006: recovered, depth 7611 ± 367 ppm (catalogue 8273 ppm); BJD 2460514.5408: recovered, depth 5995 ± 362 ppm (catalogue 8273 ppm); BJD 2460517.0811: recovered, depth 6651 ± 385 ppm (catalogue 8273 ppm); BJD 2460519.6213: gap (catalogue 8273 ppm); BJD 2460522.1615: not recovered, depth 5486 ± 340 ppm (catalogue 8273 ppm); BJD 2460524.7017: recovered, depth 8151 ± 359 ppm (catalogue 8273 ppm); BJD 2460527.2420: partial, depth 5455 ± 371 ppm (catalogue 8273 ppm); BJD 2460529.7822: recovered, depth 7358 ± 343 ppm (catalogue 8273 ppm); BJD 2460532.3224: recovered, depth 7520 ± 376 ppm (catalogue 8273 ppm); BJD 2460534.8627: recovered, depth 6077 ± 342 ppm (catalogue 8273 ppm); BJD 2460537.4029: recovered, depth 7341 ± 336 ppm (catalogue 8273 ppm); BJD 2460539.9431: recovered, depth 5787 ± 324 ppm (catalogue 8273 ppm); BJD 2460542.4833: partial, depth 5943 ± 356 ppm (catalogue 8273 ppm); BJD 2460545.0236: recovered, depth 5365 ± 330 ppm (catalogue 8273 ppm); BJD 2460547.5638: recovered, depth 5437 ± 342 ppm (catalogue 8273 ppm); BJD 2460550.1040: recovered, depth 7006 ± 347 ppm (catalogue 8273 ppm); BJD 2460552.6443: recovered, depth 6894 ± 341 ppm (catalogue 8273 ppm); BJD 2460555.1845: recovered, depth 6442 ± 334 ppm (catalogue 8273 ppm); BJD 2460557.7247: recovered, depth 6922 ± 336 ppm (catalogue 8273 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3559.01: Gaia DR3 2076337038014603520 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3559.01: Teff 8140 K, R* 1.82 ± 0.15, M* 1.91 ± 0.19, ρ* 0.32 ± 0.08 ρ☉ (dwarf sequence, M_G 1.84, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3559.01: 77 Gaia neighbour(s) within 52.5", contamination 49.91%; depth 7193 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 2076336380874335872, 48.7", ΔG 0.74); a centroid test is needed |
| Pointing and quality census per event | passed | 1 persistent event(s), 1 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | not_tested | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3559.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3559.01: TOI-3559 otype * (star_or_other) at 0.0" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3559-01.yaml
python -m cygnus.multi report campaigns/toi-3559-01.yaml
```
