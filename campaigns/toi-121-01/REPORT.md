<!-- cygnus:generated-draft -->
# Known-object test, TOI-121.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-121-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #239, calibrate_screen #193, event_census #208, fetch_products #191, known_signal_recovery #197, moving_objects #210, period_aliases #209, prior_art #241, residual_screen #200, stellar_context #199, variability_guard #240
- Runner finished (UTC): 2026-09-26T09:58:00Z

## Bottom line

Positive control **inconclusive**: BJD 2459074.3291: gap (catalogue 15041 ppm).
Outside the catalogued epoch the screen left 297 threshold entries forming **91 distinct event(s)**, **30 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-121.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 207081058 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 331.867517 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -41.815511 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459074.32911 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15041.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.504 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.9358 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-11-15 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000207081058-0190-s_lc.fits` | lightcurve | 28 | True | `44dc2a6ad3d8c506` | True |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | lightcurve | 1 | False | `b5222bed1c8f3162` | True |
| `tess2023209231226-s0068-0000000207081058-0262-s_lc.fits` | lightcurve | 68 | False | `dd32eea49c03d18c` | True |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | lightcurve | 95 | False | `35a6b02b54aab1ce` | True |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | lightcurve | 105 | False | `1bafe6af2e2144b6` | True |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | lightcurve | 106 | False | `ad71e8c60b2e35d5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000207081058-0190-s_lc.fits` | 2459074.32911 | gap | 0 | — | 15041 | — |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | — | epoch not in this light curve | — | — | 15041 | — |
| `tess2023209231226-s0068-0000000207081058-0262-s_lc.fits` | — | epoch not in this light curve | — | — | 15041 | — |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | — | epoch not in this light curve | — | — | 15041 | — |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | — | epoch not in this light curve | — | — | 15041 | — |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | — | epoch not in this light curve | — | — | 15041 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020212050318-s0028-0000000207081058-0190-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2 | True | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2023209231226-s0068-0000000207081058-0262-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 5 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461232.00192 | -0.01415 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.81003 | -0.01414 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.87879 | -0.01404 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.76837 | -0.01397 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461232.05193 | -0.01383 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.78989 | -0.01381 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.85587 | -0.01376 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.83226 | -0.01373 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461232.02415 | -0.01339 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460892.21731 | -0.01332 | 145 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458350.96188 | -0.01321 | 45 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461231.97692 | -0.01320 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.82740 | -0.01310 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.76003 | -0.01302 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461217.26505 | -0.01298 | 153 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458336.13972 | -0.01296 | 151 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.74267 | -0.01290 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458350.86952 | -0.01288 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461231.98248 | -0.01282 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.88434 | -0.01278 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.75031 | -0.01255 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.89615 | -0.01171 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.72809 | -0.01126 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461232.11582 | -0.01084 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461231.95053 | -0.00972 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458351.00702 | -0.00940 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.91351 | -0.00741 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461231.94637 | -0.00704 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461246.71142 | -0.00369 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458352.83338 | -0.00315 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.51386 | -0.00960 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.44303 | -0.00892 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.52983 | -0.00814 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.42081 | -0.00797 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.39719 | -0.00758 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.44719 | -0.00737 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.06942 | -0.00734 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.48608 | -0.00733 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.26803 | -0.00707 | 4 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.38331 | -0.00702 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.73469 | -0.00690 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.39303 | -0.00689 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.91101 | -0.00669 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.02636 | -0.00659 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.95685 | -0.00642 | 2 | PDCSAP | 1 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.59719 | -0.00638 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.90407 | -0.00609 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.45553 | -0.00599 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.42914 | -0.00596 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.93323 | -0.00595 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.78053 | -0.00582 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460900.22358 | -0.00570 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.91518 | -0.00567 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.92490 | -0.00564 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.33344 | -0.00552 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000207081058-0292-s_lc.fits` | 2460906.97351 | -0.00537 | 2 | PDCSAP | 1, 2 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.36886 | -0.00492 | 3 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.27650 | -0.00490 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.37511 | -0.00487 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.33899 | -0.00481 | 4 | SAP | 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461230.65187 | -0.00457 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.43622 | -0.00403 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.45428 | -0.00399 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.83284 | -0.00395 | 3 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.38768 | -0.00391 | 2 | SAP | 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.58630 | -0.00389 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.58213 | -0.00386 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.83343 | -0.00380 | 2 | SAP | 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.46123 | -0.00367 | 3 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458349.10982 | -0.00361 | 4 | SAP | 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.52796 | -0.00359 | 2 | SAP | 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.05293 | -0.00348 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458325.38609 | -0.00341 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461231.21856 | -0.00337 | 2 | SAP | 1 | no |
| `tess2026164183000-s0105-0000000207081058-0307-s_lc.fits` | 2461224.60158 | -0.00336 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458349.05982 | -0.00335 | 2 | SAP | 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.47859 | -0.00323 | 3 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.52163 | -0.00321 | 3 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458325.37776 | -0.00307 | 2 | PDCSAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.49248 | -0.00304 | 3 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.50289 | -0.00304 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458325.76666 | -0.00299 | 2 | PDCSAP | 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.68483 | -0.00290 | 2 | SAP | 1, 2 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.84246 | -0.00289 | 3 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458337.37931 | -0.00288 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458335.07651 | -0.00285 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458352.63616 | -0.00282 | 2 | PDCSAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.38969 | -0.00282 | 3 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458347.61400 | -0.00282 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000207081058-0120-s_lc.fits` | 2458348.48344 | -0.00278 | 2 | SAP | 3 | no |
| `tess2026192185000-s0106-0000000207081058-0308-s_lc.fits` | 2461239.78554 | -0.00258 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-121.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:57:56Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:57:58Z: TOI-121.01 (TIC 207081058, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:57:59Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:58:00Z: CD-42 15773 (SB*); TOI-121.01 (err)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2459074.3291: gap (catalogue 15041 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, 5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 60%, 20%, 0%, 70%, 80% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-121.01: Gaia DR3 6571502449115103232 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.03") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-121.01: Teff 6029 K, R* 1.19 ± 0.10, M* 1.15 ± 0.12, ρ* 0.68 ± 0.18 ρ☉ (dwarf sequence, M_G 4.01, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-121.01: 4 Gaia neighbour(s) within 52.5", contamination 3.07%; depth 15041 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 6568500026457126400, 21.4", ΔG 3.79); a centroid test is needed |
| Pointing and quality census per event | failed | 30 persistent event(s), 2 clean; BJD 2458336.1397 suspect: SAP_BKG z=-5.6; BJD 2458350.8695 suspect: manual exclude (in event), SAP_BKG z=-7.5; BJD 2458350.9619 caution: manual exclude (within ±0.25 d); BJD 2458351.0070 suspect: manual exclude (in event) |
| Moving objects at screen-event epochs | inconclusive | 30 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 7 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-121.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-121.01: CD-42 15773 otype SB* (multiple) at 0.8" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-121-01.yaml
python -m cygnus.multi report campaigns/toi-121-01.yaml
```
