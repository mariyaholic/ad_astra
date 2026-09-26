<!-- cygnus:generated-draft -->
# Known-object test, TOI-173.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-173-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #406, calibrate_screen #263, event_census #288, fetch_products #261, known_signal_recovery #269, moving_objects #397, period_aliases #289, prior_art #408, residual_screen #272, stellar_context #270, variability_guard #407
- Runner finished (UTC): 2026-09-26T10:05:59Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-173.01 (BJD 2458333.4101: recovered, depth 5754 ± 37 ppm (catalogue 6351 ppm)).
Outside the catalogued epoch the screen left 340 threshold entries forming **89 distinct event(s)**, **30 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458660.6336 matches the catalogued transit's depth (5416 vs 5754 ppm), 327.227 d later; 3 of 327 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-173.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 270341214 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 33.458853 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -80.582711 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458333.410136 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6350.8299407 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 8.0780445 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.8784 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-03-11 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | lightcurve | 1 | True | `61247b2680e722da` | True |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | lightcurve | 13 | False | `f1361354cd0e579d` | True |
| `tess2020186164531-s0027-0000000270341214-0189-s_lc.fits` | lightcurve | 27 | False | `77cb3d3434144b60` | True |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | lightcurve | 28 | False | `b5f3964498163693` | True |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | lightcurve | 39 | False | `3d536a8522b97319` | True |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | lightcurve | 66 | False | `0a0ad2551616f004` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458333.41014 | recovered | 242 | 5754 ± 37 | 6351 | -0.09 |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | — | epoch not in this light curve | — | — | 6351 | — |
| `tess2020186164531-s0027-0000000270341214-0189-s_lc.fits` | — | epoch not in this light curve | — | — | 6351 | — |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | — | epoch not in this light curve | — | — | 6351 | — |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | — | epoch not in this light curve | — | — | 6351 | — |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 6351 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020186164531-s0027-0000000270341214-0189-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.75508 | -0.00743 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.80022 | -0.00723 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.69121 | -0.00723 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.64190 | -0.00696 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.72107 | -0.00691 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.77800 | -0.00690 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.59885 | -0.00667 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.67593 | -0.00666 | 15 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.77314 | -0.00664 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.70093 | -0.00655 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.55440 | -0.00649 | 34 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.75302 | -0.00630 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000270341214-0189-s_lc.fits` | 2459047.49530 | -0.00620 | 224 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.73702 | -0.00614 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.78564 | -0.00605 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.80855 | -0.00604 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.82730 | -0.00599 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.79466 | -0.00599 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459077.24989 | -0.00595 | 233 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.76550 | -0.00590 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.51412 | -0.00581 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.81897 | -0.00565 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.63355 | -0.00563 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.77871 | -0.00547 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.49051 | -0.00484 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | 2459374.74965 | -0.00483 | 157 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.84328 | -0.00462 | 15 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.78843 | -0.00450 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.85716 | -0.00364 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458660.54952 | -0.00292 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458664.12873 | -0.00372 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.64041 | -0.00367 | 2 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.05032 | -0.00321 | 7 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.72791 | -0.00319 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.01352 | -0.00317 | 12 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458657.48421 | -0.00316 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.90024 | -0.00308 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.75708 | -0.00301 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.03435 | -0.00293 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458681.99685 | -0.00292 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.06907 | -0.00290 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.06074 | -0.00281 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | 2459374.63784 | -0.00281 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.11699 | -0.00280 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.07949 | -0.00280 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.27255 | -0.00274 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.10935 | -0.00273 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.09894 | -0.00271 | 9 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.13435 | -0.00270 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.51402 | -0.00266 | 4 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.19269 | -0.00264 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.28068 | -0.00264 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.03991 | -0.00263 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.79329 | -0.00261 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.57513 | -0.00259 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.20102 | -0.00259 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | 2459386.60053 | -0.00258 | 2 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458681.96005 | -0.00257 | 3 | PDCSAP | 1 | no |
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458348.48004 | -0.00257 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.02741 | -0.00255 | 2 | PDCSAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.68207 | -0.00250 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.23713 | -0.00249 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458681.92602 | -0.00247 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.29269 | -0.00245 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.21769 | -0.00245 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458681.96491 | -0.00245 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.08852 | -0.00241 | 4 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.21074 | -0.00239 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.14269 | -0.00237 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.28713 | -0.00237 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458681.98296 | -0.00232 | 2 | PDCSAP | 1 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.29735 | -0.00232 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.65430 | -0.00224 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 2458682.15380 | -0.00223 | 2 | PDCSAP | 1 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.77583 | -0.00222 | 3 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | 2459382.32547 | -0.00217 | 2 | SAP | 1 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460111.52513 | -0.00212 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 2460118.89330 | -0.00206 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458325.84628 | -0.00193 | 3 | PDCSAP | 3 | no |
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458343.96622 | -0.00192 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458351.56332 | -0.00190 | 2 | SAP | 2, 3 | no |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459081.18871 | -0.00189 | 3 | SAP | 1, 2, 3 | no |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459080.66927 | -0.00185 | 3 | SAP | 2, 3 | no |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459081.05746 | -0.00185 | 2 | SAP | 2, 3 | no |
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458347.68005 | -0.00169 | 2 | SAP | 1, 2 | no |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459080.84774 | -0.00169 | 2 | SAP | 3 | no |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459080.77969 | -0.00166 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 2458325.95600 | -0.00160 | 3 | PDCSAP | 3 | no |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 2459066.98545 | -0.00146 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458660.63355 | 5416 | 5754 | 327.2273 | 3 / 327 | 327.227, 163.614, 109.076 |
| 2458660.73702 | 5493 | 5754 | 327.3307 | 3 / 327 | 327.331, 163.665, 109.11 |
| 2458660.75508 | 5480 | 5754 | 327.3488 | 3 / 327 | 327.349, 163.674, 109.116 |
| 2458660.76550 | 5435 | 5754 | 327.3592 | 3 / 327 | 327.359, 163.68, 109.12 |
| 2458660.77314 | 5405 | 5754 | 327.3668 | 3 / 327 | 327.367, 163.683, 109.122 |
| 2458660.77800 | 5359 | 5754 | 327.3717 | 3 / 327 | 327.372, 163.686, 109.124 |
| 2458660.78564 | 5330 | 5754 | 327.3793 | 3 / 327 | 327.379, 163.69, 109.126 |
| 2458660.79466 | 5257 | 5754 | 327.3884 | 3 / 327 | 327.388, 163.694, 109.129 |
| 2458660.80022 | 5188 | 5754 | 327.3939 | 3 / 327 | 327.394, 163.697, 109.131 |
| 2458660.80855 | 5102 | 5754 | 327.4023 | 3 / 327 | 327.402, 163.701, 109.134 |
| 2458660.81897 | 4728 | 5754 | 327.4127 | 3 / 327 | 327.413, 163.706, 109.138 |
| 2458660.82730 | 4412 | 5754 | 327.4210 | 3 / 327 | 327.421, 163.71, 109.14 |
| 2459047.49530 | 5143 | 5754 | 714.0890 | 13 / 714 | 714.089, 357.045, 238.03, 178.522, 142.818, 119.015, 102.013, 89.2611, 71.4089, 59.5074, 51.0064, 44.6306, 29.7537 |
| 2459077.24989 | 5835 | 5754 | 743.8436 | 10 / 743 | 743.844, 371.922, 247.948, 185.961, 148.769, 123.974, 106.263, 74.3844, 53.1317, 29.7537 |
| 2459374.74965 | 3133 | 5754 | 1041.3434 | 9 / 1041 | 1041.34, 520.672, 260.336, 208.269, 148.763, 130.168, 94.6676, 74.3817, 29.7527 |
| 2460118.49051 | 4002 | 5754 | 1785.0842 | 25 / 1785 | 1785.08, 892.542, 595.028, 446.271, 357.017, 297.514, 255.012, 223.136, 198.343, 178.508, 148.757, 137.314, 127.506, 119.006, 111.568, 99.1713, 89.2542, 77.6124, 74.3785, 71.4034 |
| 2460118.51412 | 4699 | 5754 | 1785.1078 | 25 / 1785 | 1785.11, 892.554, 595.036, 446.277, 357.022, 297.518, 255.015, 223.138, 198.345, 178.511, 148.759, 137.316, 127.508, 119.007, 111.569, 99.1727, 89.2554, 77.6134, 74.3795, 71.4043 |
| 2460118.55440 | 5237 | 5754 | 1785.1481 | 25 / 1785 | 1785.15, 892.574, 595.049, 446.287, 357.03, 297.525, 255.021, 223.143, 198.35, 178.515, 148.762, 137.319, 127.511, 119.01, 111.572, 99.1749, 89.2574, 77.6151, 74.3812, 71.4059 |
| 2460118.59885 | 5472 | 5754 | 1785.1926 | 25 / 1785 | 1785.19, 892.596, 595.064, 446.298, 357.038, 297.532, 255.028, 223.149, 198.355, 178.519, 148.766, 137.322, 127.514, 119.013, 111.575, 99.1774, 89.2596, 77.6171, 74.383, 71.4077 |
| 2460118.64190 | 5491 | 5754 | 1785.2356 | 25 / 1785 | 1785.24, 892.618, 595.078, 446.309, 357.047, 297.539, 255.034, 223.155, 198.359, 178.524, 148.77, 137.326, 127.517, 119.016, 111.577, 99.1798, 89.2618, 77.6189, 74.3848, 71.4094 |
| 2460118.67593 | 5436 | 5754 | 1785.2696 | 25 / 1785 | 1785.27, 892.635, 595.09, 446.317, 357.054, 297.545, 255.038, 223.159, 198.363, 178.527, 148.773, 137.328, 127.519, 119.018, 111.579, 99.1816, 89.2635, 77.6204, 74.3862, 71.4108 |
| 2460118.69121 | 5391 | 5754 | 1785.2849 | 25 / 1785 | 1785.28, 892.643, 595.095, 446.321, 357.057, 297.548, 255.041, 223.161, 198.365, 178.529, 148.774, 137.33, 127.52, 119.019, 111.58, 99.1825, 89.2642, 77.6211, 74.3869, 71.4114 |
| 2460118.70093 | 5370 | 5754 | 1785.2946 | 25 / 1785 | 1785.29, 892.647, 595.098, 446.324, 357.059, 297.549, 255.042, 223.162, 198.366, 178.53, 148.775, 137.33, 127.521, 119.02, 111.581, 99.183, 89.2647, 77.6215, 74.3873, 71.4118 |
| 2460118.72107 | 5245 | 5754 | 1785.3148 | 25 / 1785 | 1785.31, 892.657, 595.105, 446.329, 357.063, 297.553, 255.045, 223.164, 198.368, 178.531, 148.776, 137.332, 127.522, 119.021, 111.582, 99.1842, 89.2657, 77.6224, 74.3881, 71.4126 |
| 2460118.75302 | 4915 | 5754 | 1785.3467 | 25 / 1785 | 1785.35, 892.673, 595.116, 446.337, 357.069, 297.558, 255.049, 223.168, 198.372, 178.535, 148.779, 137.334, 127.525, 119.023, 111.584, 99.1859, 89.2673, 77.6238, 74.3894, 71.4139 |
| 2460118.77871 | 3729 | 5754 | 1785.3724 | 25 / 1785 | 1785.37, 892.686, 595.124, 446.343, 357.075, 297.562, 255.053, 223.172, 198.375, 178.537, 148.781, 137.336, 127.527, 119.025, 111.586, 99.1874, 89.2686, 77.6249, 74.3905, 71.4149 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-173.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:05:55Z
- TESS_TOI (done, 2026-09-26): 2 match(es) in TESS_TOI within 30" as of 2026-09-26T10:05:57Z: TOI-173.01 (TIC 270341214, disposition PC); TOI-173.02 (TIC 270341214, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:05:58Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:05:58Z: TOI-173.01 (Pl?); HD  14603 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458333.4101: recovered, depth 5754 ± 37 ppm (catalogue 6351 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, 3.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 50%, 50%, 100%, 80%, 90% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 26 repeat-candidate event(s); first at BJD 2458660.6336, ΔT = 327.227 d, 3 of 327 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (327.227, 163.614, 109.076 d); duration likelihood under Gaia priors (circular orbits) peaks at 109 d (weight 0.49) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-173.01: Gaia DR3 4631997507182253184 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-173.01: Teff 6528 K, R* 1.45 ± 0.12, M* 1.31 ± 0.13, ρ* 0.43 ± 0.11 ρ☉ (dwarf sequence, M_G 3.32, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-173.01: 6 Gaia neighbour(s) within 52.5", contamination 0.30%; depth 5754 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 30 persistent event(s), 0 clean; BJD 2458660.5495 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2458660.6336 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2458660.7370 suspect: manual exclude (in event), momentum dump (in event), coarse point (within ±0.25 d); BJD 2458660.7551 suspect: manual exclude (in event), coarse point (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 30 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-173.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-173.01: HD  14603 otype * (star_or_other) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-173-01.yaml
python -m cygnus.multi report campaigns/toi-173-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** E1 (BJD 2458660.7014) and E2 (2459047.4937) land within 0.00-0.15 h (sigma 0.01 h) of predicted TOI-173.01 transits at the catalogued P 29.7537 d. (The TIC also carries TOI-173.02, P 9.1702 d, PC — the vet matched the events to 173.01's ephemeris.) No new signal.

Source: `campaigns/toi-173-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
