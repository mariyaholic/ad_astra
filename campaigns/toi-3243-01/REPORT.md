<!-- cygnus:generated-draft -->
# Known-object test, TOI-3243.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3243-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4527, calibrate_screen #4508, event_census #4520, fetch_independent #4523, fetch_products #4501, known_signal_recovery #4515, moving_objects #4522, period_aliases #4521, prior_art #4529, residual_screen #4519, stellar_context #4516, variability_guard #4528
- Runner finished (UTC): 2026-09-30T21:58:39Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3243.01 (BJD 2460069.3079: recovered, depth 9110 ± 442 ppm (catalogue 10320 ppm); BJD 2460071.3598: recovered, depth 8490 ± 433 ppm (catalogue 10320 ppm); BJD 2460073.4117: recovered, depth 9149 ± 451 ppm (catalogue 10320 ppm); BJD 2460075.4636: recovered, depth 8622 ± 442 ppm (catalogue 10320 ppm); BJD 2460077.5155: recovered, depth 7732 ± 468 ppm (catalogue 10320 ppm); BJD 2460079.5674: recovered, depth 10474 ± 482 ppm (catalogue 10320 ppm); BJD 2460081.6193: gap (catalogue 10320 ppm); BJD 2460083.6712: not recovered, depth 6728 ± 1000 ppm (catalogue 10320 ppm); BJD 2460085.7231: recovered, depth 9929 ± 457 ppm (catalogue 10320 ppm); BJD 2460087.7750: recovered, depth 10352 ± 416 ppm (catalogue 10320 ppm); BJD 2460089.8269: recovered, depth 9935 ± 452 ppm (catalogue 10320 ppm); BJD 2460091.8789: recovered, depth 10095 ± 448 ppm (catalogue 10320 ppm); BJD 2460093.9308: recovered, depth 10624 ± 467 ppm (catalogue 10320 ppm); BJD 2460095.9827: gap (catalogue 10320 ppm); BJD 2461048.0682: recovered, depth 12036 ± 517 ppm (catalogue 10320 ppm); BJD 2461050.1201: recovered, depth 12760 ± 485 ppm (catalogue 10320 ppm); BJD 2461052.1720: recovered, depth 10010 ± 542 ppm (catalogue 10320 ppm); BJD 2461054.2239: recovered, depth 11263 ± 488 ppm (catalogue 10320 ppm); BJD 2461056.2758: gap (catalogue 10320 ppm); BJD 2461058.3278: gap (catalogue 10320 ppm); BJD 2461060.3797: gap (catalogue 10320 ppm); BJD 2461062.4316: gap (catalogue 10320 ppm); BJD 2461064.4835: recovered, depth 10661 ± 532 ppm (catalogue 10320 ppm); BJD 2461066.5354: recovered, depth 12364 ± 498 ppm (catalogue 10320 ppm); BJD 2461068.5873: recovered, depth 9460 ± 520 ppm (catalogue 10320 ppm); BJD 2461070.6392: recovered, depth 11989 ± 494 ppm (catalogue 10320 ppm); BJD 2461072.6911: recovered, depth 10775 ± 536 ppm (catalogue 10320 ppm); BJD 2461074.7430: recovered, depth 10611 ± 511 ppm (catalogue 10320 ppm); BJD 2461076.7949: recovered, depth 9545 ± 520 ppm (catalogue 10320 ppm); BJD 2461078.8468: recovered, depth 9334 ± 522 ppm (catalogue 10320 ppm); BJD 2461080.8987: recovered, depth 12551 ± 541 ppm (catalogue 10320 ppm); BJD 2461082.9507: recovered, depth 10286 ± 482 ppm (catalogue 10320 ppm); BJD 2461085.0026: recovered, depth 11014 ± 516 ppm (catalogue 10320 ppm); BJD 2461087.0545: gap (catalogue 10320 ppm); BJD 2461089.1064: recovered, depth 10159 ± 506 ppm (catalogue 10320 ppm); BJD 2461091.1583: recovered, depth 10305 ± 531 ppm (catalogue 10320 ppm); BJD 2461093.2102: recovered, depth 8620 ± 624 ppm (catalogue 10320 ppm); BJD 2461095.2621: recovered, depth 9930 ± 541 ppm (catalogue 10320 ppm); BJD 2461097.3140: recovered, depth 10707 ± 513 ppm (catalogue 10320 ppm); BJD 2461099.3659: recovered, depth 14437 ± 508 ppm (catalogue 10320 ppm); BJD 2461101.4178: recovered, depth 7993 ± 666 ppm (catalogue 10320 ppm); BJD 2461103.4697: recovered, depth 10128 ± 550 ppm (catalogue 10320 ppm); BJD 2461105.5216: recovered, depth 11005 ± 534 ppm (catalogue 10320 ppm); BJD 2461107.5736: recovered, depth 9121 ± 562 ppm (catalogue 10320 ppm); BJD 2461109.6255: recovered, depth 10625 ± 526 ppm (catalogue 10320 ppm); BJD 2461111.6774: recovered, depth 9516 ± 549 ppm (catalogue 10320 ppm); BJD 2461113.7293: gap (catalogue 10320 ppm); BJD 2461115.7812: recovered, depth 11109 ± 575 ppm (catalogue 10320 ppm); BJD 2461117.8331: recovered, depth 9997 ± 546 ppm (catalogue 10320 ppm); BJD 2461119.8850: recovered, depth 9053 ± 622 ppm (catalogue 10320 ppm); BJD 2461121.9369: recovered, depth 9673 ± 575 ppm (catalogue 10320 ppm); BJD 2461123.9888: recovered, depth 10742 ± 575 ppm (catalogue 10320 ppm); BJD 2461126.0407: gap (catalogue 10320 ppm); BJD 2461128.0926: recovered, depth 9356 ± 555 ppm (catalogue 10320 ppm); BJD 2461130.1446: recovered, depth 9657 ± 483 ppm (catalogue 10320 ppm); BJD 2461132.1965: recovered, depth 10112 ± 508 ppm (catalogue 10320 ppm); BJD 2461134.2484: recovered, depth 9382 ± 503 ppm (catalogue 10320 ppm); BJD 2461136.3003: recovered, depth 9555 ± 508 ppm (catalogue 10320 ppm); BJD 2461138.3522: recovered, depth 15851 ± 504 ppm (catalogue 10320 ppm); BJD 2461140.4041: recovered, depth 14475 ± 466 ppm (catalogue 10320 ppm); BJD 2461142.4560: recovered, depth 8753 ± 507 ppm (catalogue 10320 ppm); BJD 2461144.5079: recovered, depth 12335 ± 488 ppm (catalogue 10320 ppm); BJD 2461146.5598: recovered, depth 11409 ± 505 ppm (catalogue 10320 ppm); BJD 2461148.6117: recovered, depth 9912 ± 531 ppm (catalogue 10320 ppm); BJD 2461150.6636: recovered, depth 10281 ± 509 ppm (catalogue 10320 ppm)).
Outside the catalogued epoch the screen left 36 threshold entries forming **23 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3243.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 209707800 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 210.884268 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -55.44311 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459359.347516 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.0519085 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10320.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.778 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.7219 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | lightcurve | 65 | False | `1ffd4fddc576673c` | True |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | lightcurve | 99 | False | `ba0814e5afb8f10b` | True |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | lightcurve | 100 | False | `f9cd9969faec00c0` | True |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | lightcurve | 101 | False | `55b19197126d6e23` | True |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | lightcurve | 102 | False | `a31a9cfadd60ddd6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460069.30786 | recovered | 53 | 9110 ± 442 | 10320 | 0.16 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460071.35977 | recovered | 54 | 8490 ± 433 | 10320 | 0.27 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460073.41167 | recovered | 53 | 9149 ± 451 | 10320 | -0.16 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460075.46358 | recovered | 53 | 8622 ± 442 | 10320 | 0.11 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460077.51549 | recovered | 54 | 7732 ± 468 | 10320 | -0.12 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460079.56740 | recovered | 53 | 10474 ± 482 | 10320 | -0.06 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460081.61931 | gap | 0 | — | 10320 | — |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.67122 | not_recovered | 10 | 6728 ± 1000 | 10320 | — |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460085.72313 | recovered | 53 | 9929 ± 457 | 10320 | 0.11 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460087.77503 | recovered | 54 | 10352 ± 416 | 10320 | 0.07 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460089.82694 | recovered | 50 | 9935 ± 452 | 10320 | 0.04 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460091.87885 | recovered | 53 | 10095 ± 448 | 10320 | -0.09 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460093.93076 | recovered | 54 | 10624 ± 467 | 10320 | 0.09 |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460095.98267 | gap | 0 | — | 10320 | — |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461048.06821 | recovered | 53 | 12036 ± 517 | 10320 | 0.08 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461050.12012 | recovered | 54 | 12760 ± 485 | 10320 | -0.28 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461052.17203 | recovered | 53 | 10010 ± 542 | 10320 | -0.14 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461054.22394 | recovered | 53 | 11263 ± 488 | 10320 | 0.27 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461056.27585 | gap | 0 | — | 10320 | — |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461058.32775 | gap | 0 | — | 10320 | — |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461060.37966 | gap | 0 | — | 10320 | — |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461062.43157 | gap | 0 | — | 10320 | — |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461064.48348 | recovered | 53 | 10661 ± 532 | 10320 | -0.16 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461066.53539 | recovered | 54 | 12364 ± 498 | 10320 | 0.16 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461068.58730 | recovered | 53 | 9460 ± 520 | 10320 | 0.01 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461070.63920 | recovered | 53 | 11989 ± 494 | 10320 | 0.10 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461072.69111 | recovered | 50 | 10775 ± 536 | 10320 | 0.17 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461074.74302 | recovered | 54 | 10611 ± 511 | 10320 | 0.05 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461076.79493 | recovered | 53 | 9545 ± 520 | 10320 | 0.16 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461078.84684 | recovered | 53 | 9334 ± 522 | 10320 | -0.02 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461080.89875 | recovered | 49 | 12551 ± 541 | 10320 | 0.31 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461082.95066 | recovered | 54 | 10286 ± 482 | 10320 | 0.01 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461085.00256 | recovered | 53 | 11014 ± 516 | 10320 | 0.29 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461087.05447 | gap | 0 | — | 10320 | — |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461089.10638 | recovered | 54 | 10159 ± 506 | 10320 | -0.13 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461091.15829 | recovered | 53 | 10305 ± 531 | 10320 | 0.18 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461093.21020 | recovered | 36 | 8620 ± 624 | 10320 | 0.15 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461095.26211 | recovered | 53 | 9930 ± 541 | 10320 | -0.02 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461097.31402 | recovered | 54 | 10707 ± 513 | 10320 | 0.33 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461099.36592 | recovered | 53 | 14437 ± 508 | 10320 | 0.20 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461101.41783 | recovered | 53 | 7993 ± 666 | 10320 | 0.17 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461103.46974 | recovered | 53 | 10128 ± 550 | 10320 | -0.49 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461105.52165 | recovered | 54 | 11005 ± 534 | 10320 | 0.46 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461107.57356 | recovered | 53 | 9121 ± 562 | 10320 | 0.52 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461109.62547 | recovered | 53 | 10625 ± 526 | 10320 | 0.13 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461111.67737 | recovered | 54 | 9516 ± 549 | 10320 | -0.13 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461113.72928 | gap | 0 | — | 10320 | — |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461115.78119 | recovered | 53 | 11109 ± 575 | 10320 | 0.14 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461117.83310 | recovered | 53 | 9997 ± 546 | 10320 | 0.18 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461119.88501 | recovered | 51 | 9053 ± 622 | 10320 | -0.35 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461121.93692 | recovered | 53 | 9673 ± 575 | 10320 | 0.09 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461123.98883 | recovered | 53 | 10742 ± 575 | 10320 | 0.28 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461126.04073 | gap | 0 | — | 10320 | — |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461128.09264 | recovered | 54 | 9356 ± 555 | 10320 | -0.11 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461130.14455 | recovered | 53 | 9657 ± 483 | 10320 | 0.08 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461132.19646 | recovered | 53 | 10112 ± 508 | 10320 | 0.31 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461134.24837 | recovered | 54 | 9382 ± 503 | 10320 | 0.06 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461136.30028 | recovered | 53 | 9555 ± 508 | 10320 | 0.12 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461138.35219 | recovered | 53 | 15851 ± 504 | 10320 | 0.03 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461140.40409 | recovered | 54 | 14475 ± 466 | 10320 | 0.18 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461142.45600 | recovered | 53 | 8753 ± 507 | 10320 | 0.52 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461144.50791 | recovered | 53 | 12335 ± 488 | 10320 | 0.31 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461146.55982 | recovered | 54 | 11409 ± 505 | 10320 | 0.18 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461148.61173 | recovered | 53 | 9912 ± 531 | 10320 | 0.26 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 2461150.66364 | recovered | 53 | 10281 ± 509 | 10320 | 0.38 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 3 | False | 1h: —, 2h: 20000, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026086090000-s0102-0000000209707800-0304-s_lc.fits` | 4 | False | 1h: 20000, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.27191 | -0.01382 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.15570 | -0.01284 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.20524 | -0.01276 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.10987 | -0.01204 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.25362 | -0.01185 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.20362 | -0.01165 | 5 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.11218 | -0.01109 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460089.95561 | -0.01005 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.25987 | -0.00969 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460089.45284 | -0.00957 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000209707800-0259-s_lc.fits` | 2460083.00570 | -0.00948 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000209707800-0303-s_lc.fits` | 2461114.06797 | -0.00926 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.46082 | -0.00914 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.10107 | -0.00885 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000209707800-0302-s_lc.fits` | 2461093.52625 | -0.00866 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.18718 | -0.00827 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461071.93293 | -0.00818 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.29691 | -0.00797 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.16218 | -0.00787 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.14829 | -0.00748 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.28580 | -0.00718 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.03440 | -0.00705 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000209707800-0300-s_lc.fits` | 2461073.01078 | -0.00694 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3243.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:58:28Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:58:30Z: TOI-3243.01 (TIC 209707800, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:58:33Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:58:36Z: TOI-3243 (SB*); TOI-3243.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460069.3079: recovered, depth 9110 ± 442 ppm (catalogue 10320 ppm); BJD 2460071.3598: recovered, depth 8490 ± 433 ppm (catalogue 10320 ppm); BJD 2460073.4117: recovered, depth 9149 ± 451 ppm (catalogue 10320 ppm); BJD 2460075.4636: recovered, depth 8622 ± 442 ppm (catalogue 10320 ppm); BJD 2460077.5155: recovered, depth 7732 ± 468 ppm (catalogue 10320 ppm); BJD 2460079.5674: recovered, depth 10474 ± 482 ppm (catalogue 10320 ppm); BJD 2460081.6193: gap (catalogue 10320 ppm); BJD 2460083.6712: not recovered, depth 6728 ± 1000 ppm (catalogue 10320 ppm); BJD 2460085.7231: recovered, depth 9929 ± 457 ppm (catalogue 10320 ppm); BJD 2460087.7750: recovered, depth 10352 ± 416 ppm (catalogue 10320 ppm); BJD 2460089.8269: recovered, depth 9935 ± 452 ppm (catalogue 10320 ppm); BJD 2460091.8789: recovered, depth 10095 ± 448 ppm (catalogue 10320 ppm); BJD 2460093.9308: recovered, depth 10624 ± 467 ppm (catalogue 10320 ppm); BJD 2460095.9827: gap (catalogue 10320 ppm); BJD 2461048.0682: recovered, depth 12036 ± 517 ppm (catalogue 10320 ppm); BJD 2461050.1201: recovered, depth 12760 ± 485 ppm (catalogue 10320 ppm); BJD 2461052.1720: recovered, depth 10010 ± 542 ppm (catalogue 10320 ppm); BJD 2461054.2239: recovered, depth 11263 ± 488 ppm (catalogue 10320 ppm); BJD 2461056.2758: gap (catalogue 10320 ppm); BJD 2461058.3278: gap (catalogue 10320 ppm); BJD 2461060.3797: gap (catalogue 10320 ppm); BJD 2461062.4316: gap (catalogue 10320 ppm); BJD 2461064.4835: recovered, depth 10661 ± 532 ppm (catalogue 10320 ppm); BJD 2461066.5354: recovered, depth 12364 ± 498 ppm (catalogue 10320 ppm); BJD 2461068.5873: recovered, depth 9460 ± 520 ppm (catalogue 10320 ppm); BJD 2461070.6392: recovered, depth 11989 ± 494 ppm (catalogue 10320 ppm); BJD 2461072.6911: recovered, depth 10775 ± 536 ppm (catalogue 10320 ppm); BJD 2461074.7430: recovered, depth 10611 ± 511 ppm (catalogue 10320 ppm); BJD 2461076.7949: recovered, depth 9545 ± 520 ppm (catalogue 10320 ppm); BJD 2461078.8468: recovered, depth 9334 ± 522 ppm (catalogue 10320 ppm); BJD 2461080.8987: recovered, depth 12551 ± 541 ppm (catalogue 10320 ppm); BJD 2461082.9507: recovered, depth 10286 ± 482 ppm (catalogue 10320 ppm); BJD 2461085.0026: recovered, depth 11014 ± 516 ppm (catalogue 10320 ppm); BJD 2461087.0545: gap (catalogue 10320 ppm); BJD 2461089.1064: recovered, depth 10159 ± 506 ppm (catalogue 10320 ppm); BJD 2461091.1583: recovered, depth 10305 ± 531 ppm (catalogue 10320 ppm); BJD 2461093.2102: recovered, depth 8620 ± 624 ppm (catalogue 10320 ppm); BJD 2461095.2621: recovered, depth 9930 ± 541 ppm (catalogue 10320 ppm); BJD 2461097.3140: recovered, depth 10707 ± 513 ppm (catalogue 10320 ppm); BJD 2461099.3659: recovered, depth 14437 ± 508 ppm (catalogue 10320 ppm); BJD 2461101.4178: recovered, depth 7993 ± 666 ppm (catalogue 10320 ppm); BJD 2461103.4697: recovered, depth 10128 ± 550 ppm (catalogue 10320 ppm); BJD 2461105.5216: recovered, depth 11005 ± 534 ppm (catalogue 10320 ppm); BJD 2461107.5736: recovered, depth 9121 ± 562 ppm (catalogue 10320 ppm); BJD 2461109.6255: recovered, depth 10625 ± 526 ppm (catalogue 10320 ppm); BJD 2461111.6774: recovered, depth 9516 ± 549 ppm (catalogue 10320 ppm); BJD 2461113.7293: gap (catalogue 10320 ppm); BJD 2461115.7812: recovered, depth 11109 ± 575 ppm (catalogue 10320 ppm); BJD 2461117.8331: recovered, depth 9997 ± 546 ppm (catalogue 10320 ppm); BJD 2461119.8850: recovered, depth 9053 ± 622 ppm (catalogue 10320 ppm); BJD 2461121.9369: recovered, depth 9673 ± 575 ppm (catalogue 10320 ppm); BJD 2461123.9888: recovered, depth 10742 ± 575 ppm (catalogue 10320 ppm); BJD 2461126.0407: gap (catalogue 10320 ppm); BJD 2461128.0926: recovered, depth 9356 ± 555 ppm (catalogue 10320 ppm); BJD 2461130.1446: recovered, depth 9657 ± 483 ppm (catalogue 10320 ppm); BJD 2461132.1965: recovered, depth 10112 ± 508 ppm (catalogue 10320 ppm); BJD 2461134.2484: recovered, depth 9382 ± 503 ppm (catalogue 10320 ppm); BJD 2461136.3003: recovered, depth 9555 ± 508 ppm (catalogue 10320 ppm); BJD 2461138.3522: recovered, depth 15851 ± 504 ppm (catalogue 10320 ppm); BJD 2461140.4041: recovered, depth 14475 ± 466 ppm (catalogue 10320 ppm); BJD 2461142.4560: recovered, depth 8753 ± 507 ppm (catalogue 10320 ppm); BJD 2461144.5079: recovered, depth 12335 ± 488 ppm (catalogue 10320 ppm); BJD 2461146.5598: recovered, depth 11409 ± 505 ppm (catalogue 10320 ppm); BJD 2461148.6117: recovered, depth 9912 ± 531 ppm (catalogue 10320 ppm); BJD 2461150.6636: recovered, depth 10281 ± 509 ppm (catalogue 10320 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3243.01: Gaia DR3 5872390109623076992 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3243.01: dwarf priors not applied — parallax/error 0.4 < 5; RUWE 24.905687 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3243.01: 195 Gaia neighbour(s) within 52.5", contamination 46.13%; depth 9110 ppm (measured depth of the recovered catalogued transit); 12 could produce it if fully eclipsed (brightest 5872390109623064832, 28.7", ΔG 2.19); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3243.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-3243.01: TOI-3243 otype SB* (multiple) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3243-01.yaml
python -m cygnus.multi report campaigns/toi-3243-01.yaml
```
