<!-- cygnus:generated-draft -->
# Known-object test, TOI-3487.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3487-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #346, calibrate_screen #331, event_census #337, fetch_products #329, known_signal_recovery #332, moving_objects #339, period_aliases #338, prior_art #348, residual_screen #335, stellar_context #333, variability_guard #347
- Runner finished (UTC): 2026-09-26T10:03:26Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 404 threshold entries forming **149 distinct event(s)**, **29 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3487.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 301160638 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 255.113012 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -67.781031 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459378.988034 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14340.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.452 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.1862 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | lightcurve | 12 | False | `a52ace1cf6b288c4` | True |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | lightcurve | 66 | False | `8c3c5250c1e39553` | True |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | lightcurve | 93 | False | `35ac9e9be8d1acd7` | True |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | lightcurve | 100 | False | `8a323ad68e81cb67` | True |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | lightcurve | 101 | False | `099e2e786c5fa5d5` | True |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | lightcurve | 102 | False | `a1d47110dda13f3b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | — | epoch not in this light curve | — | — | 14340 | — |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 14340 | — |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | — | epoch not in this light curve | — | — | 14340 | — |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 14340 | — |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 14340 | — |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 14340 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461076.11526 | -0.01435 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461108.13540 | -0.01411 | 99 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460851.96979 | -0.01387 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461124.15041 | -0.01382 | 102 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460115.48035 | -0.01351 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461092.13084 | -0.01290 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460099.47060 | -0.01265 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460835.95460 | -0.01251 | 99 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461085.83042 | -0.01109 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458636.19201 | -0.01091 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461149.86802 | -0.01061 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458652.20945 | -0.01035 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461133.86843 | -0.01026 | 66 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461117.85206 | -0.00990 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460845.67055 | -0.00952 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458636.23785 | -0.00932 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461101.84328 | -0.00917 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461108.20832 | -0.00667 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461124.07749 | -0.00643 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460851.89896 | -0.00603 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460851.89410 | -0.00572 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461119.80497 | -0.00543 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458652.15737 | -0.00538 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461119.81539 | -0.00529 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460836.02821 | -0.00493 | 6 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461119.82650 | -0.00486 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461101.79120 | -0.00482 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458652.26292 | -0.00456 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461117.80066 | -0.00435 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461150.45138 | -0.00741 | 2 | PDCSAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461151.17364 | -0.00701 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.79009 | -0.00661 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.77759 | -0.00655 | 10 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461146.39005 | -0.00634 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461146.43519 | -0.00628 | 3 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461146.38033 | -0.00624 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.56222 | -0.00610 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461144.97885 | -0.00599 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.79071 | -0.00596 | 3 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460849.73232 | -0.00596 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.63176 | -0.00590 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.51787 | -0.00587 | 6 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.75884 | -0.00581 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461119.85428 | -0.00578 | 3 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.72412 | -0.00568 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.71926 | -0.00565 | 3 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.48791 | -0.00561 | 3 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.10803 | -0.00550 | 2 | PDCSAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.38027 | -0.00542 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.42749 | -0.00542 | 2 | PDCSAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.73654 | -0.00542 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.80954 | -0.00529 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.73037 | -0.00525 | 2 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.45110 | -0.00525 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.65389 | -0.00523 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.77065 | -0.00521 | 2 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461144.94413 | -0.00520 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.68454 | -0.00518 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461092.81700 | -0.00516 | 2 | SAP | 1 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.21637 | -0.00515 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.16636 | -0.00509 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.74287 | -0.00504 | 8 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.23998 | -0.00503 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.14553 | -0.00502 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.69417 | -0.00499 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.75120 | -0.00497 | 2 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.55806 | -0.00496 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461092.20168 | -0.00495 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.61787 | -0.00491 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.34346 | -0.00489 | 3 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461085.77208 | -0.00486 | 2 | PDCSAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461149.82357 | -0.00484 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.73454 | -0.00484 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.64426 | -0.00482 | 4 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460849.77468 | -0.00481 | 3 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.59972 | -0.00481 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458636.24479 | -0.00480 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.55250 | -0.00480 | 2 | PDCSAP | 1 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.92891 | -0.00472 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461108.22083 | -0.00470 | 2 | PDCSAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.79565 | -0.00469 | 4 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.67751 | -0.00469 | 6 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.75112 | -0.00467 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.32610 | -0.00464 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.59070 | -0.00464 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460118.63449 | -0.00462 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.44069 | -0.00461 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.60398 | -0.00461 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.40249 | -0.00460 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.09275 | -0.00460 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460115.40119 | -0.00457 | 2 | PDCSAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461114.21429 | -0.00456 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458632.00166 | -0.00453 | 2 | SAP | 2 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461074.28529 | -0.00452 | 2 | PDCSAP+SAP | 1 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.38454 | -0.00451 | 4 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.48731 | -0.00450 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.54842 | -0.00444 | 2 | SAP | 2 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461092.82950 | -0.00443 | 3 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.85946 | -0.00443 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.43444 | -0.00442 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.45954 | -0.00442 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.59981 | -0.00436 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.46638 | -0.00433 | 4 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.81015 | -0.00433 | 3 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.06636 | -0.00432 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461092.87672 | -0.00432 | 2 | SAP | 1 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461137.51658 | -0.00431 | 3 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461144.78579 | -0.00429 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461149.92636 | -0.00424 | 2 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461133.81426 | -0.00423 | 2 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.47749 | -0.00422 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.60954 | -0.00421 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460099.39490 | -0.00421 | 3 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461151.31532 | -0.00419 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.80113 | -0.00418 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.49277 | -0.00417 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.60945 | -0.00414 | 4 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460841.44487 | -0.00411 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.70537 | -0.00411 | 4 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461119.78206 | -0.00409 | 3 | PDCSAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461137.47282 | -0.00408 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.87057 | -0.00406 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461137.49644 | -0.00403 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458645.04070 | -0.00403 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.99280 | -0.00400 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458637.52537 | -0.00399 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.63592 | -0.00398 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.17470 | -0.00398 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461145.52403 | -0.00395 | 3 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461133.81009 | -0.00394 | 2 | SAP | 1, 2 | no |
| `tess2026033082000-s0100-0000000301160638-0302-s_lc.fits` | 2461093.52399 | -0.00392 | 2 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461137.71867 | -0.00391 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000301160638-0303-s_lc.fits` | 2461119.86053 | -0.00387 | 2 | SAP | 1 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460117.75672 | -0.00382 | 2 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461144.91357 | -0.00381 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461144.93580 | -0.00381 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461133.91288 | -0.00380 | 2 | SAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460117.13728 | -0.00376 | 2 | SAP | 1 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.51092 | -0.00373 | 2 | SAP | 2 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458643.74486 | -0.00370 | 2 | PDCSAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.20537 | -0.00364 | 2 | SAP | 1, 2 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458631.65304 | -0.00362 | 2 | SAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.94565 | -0.00361 | 2 | SAP | 2 | no |
| `tess2025154050500-s0093-0000000301160638-0290-s_lc.fits` | 2460835.88237 | -0.00361 | 2 | SAP | 1 | no |
| `tess2019140104343-s0012-0000000301160638-0144-s_lc.fits` | 2458629.00854 | -0.00361 | 2 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000301160638-0304-s_lc.fits` | 2461144.47466 | -0.00356 | 2 | SAP | 1 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.34565 | -0.00353 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.80537 | -0.00351 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000301160638-0260-s_lc.fits` | 2460111.56370 | -0.00339 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3487.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:03:23Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:03:24Z: TOI-3487.01 (TIC 301160638, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:03:25Z: Gaia DR3 5814384445957932416 (type ROT, P — d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:03:26Z: TOI-3487 (*); TOI-3487.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10%, 0%, 30%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3487.01: Gaia DR3 5814384445957932416 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3487.01: Teff 5927 K, R* 1.08 ± 0.09, M* 1.05 ± 0.10, ρ* 0.83 ± 0.22 ρ☉ (dwarf sequence, M_G 4.39, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3487.01: 49 Gaia neighbour(s) within 52.5", contamination 10.08%; depth 14340 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 5814384549034537088, 40.2", ΔG 3.85); a centroid test is needed |
| Pointing and quality census per event | failed | 29 persistent event(s), 16 clean; BJD 2458636.1920 suspect: manual exclude (in event); BJD 2458636.2378 suspect: manual exclude (in event); BJD 2460099.4706 suspect: SAP_BKG z=-8.2; BJD 2460835.9546 suspect: POS_CORR2 z=+5.4, SAP_BKG z=-7.0 |
| Moving objects at screen-event epochs | inconclusive | 29 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 6 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3487.01: Gaia DR3 5814384445957932416   ROT                            P=None at 0.1" |
| Object-class guard (SIMBAD) | passed | TOI-3487.01: TOI-3487 otype * (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3487-01.yaml
python -m cygnus.multi report campaigns/toi-3487-01.yaml
```
