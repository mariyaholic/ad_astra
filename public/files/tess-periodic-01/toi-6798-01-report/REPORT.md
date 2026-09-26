<!-- [private Drive store] -->
# Known-object test, TOI-6798.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6798-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #778, calibrate_screen #728, event_census #733, fetch_products #727, known_signal_recovery #729, moving_objects #735, period_aliases #734, prior_art #780, residual_screen #732, stellar_context #730, variability_guard #779
- Runner finished (UTC): 2026-09-26T10:18:48Z

## Bottom line

Positive control **inconclusive**: BJD 2460136.5746: gap (catalogue 6829 ppm).
Outside the catalogued epoch the screen left 907 threshold entries forming **185 distinct event(s)**, **73 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6798.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 290403522 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 330.958061 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -72.44083 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460136.574569 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6829.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 11.966 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.2912 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | lightcurve | 67 | True | `7e7a071c5cc355f0` | True |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | lightcurve | 27 | False | `95af535763b00f99` | True |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | lightcurve | 94 | False | `8108057226796390` | True |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | lightcurve | 95 | False | `11f51fa4457ad2ea` | True |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | lightcurve | 101 | False | `125bab08801372cd` | True |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | lightcurve | 102 | False | `9ff539152bfadfbc` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | 2460136.57457 | gap | 0 | — | 6829 | — |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | — | epoch not in this light curve | — | — | 6829 | — |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | — | epoch not in this light curve | — | — | 6829 | — |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | — | epoch not in this light curve | — | — | 6829 | — |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 6829 | — |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 6829 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.98088 | -0.00999 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.73782 | -0.00910 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.85727 | -0.00903 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.84893 | -0.00895 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.90102 | -0.00883 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.97463 | -0.00869 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.76491 | -0.00858 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.92463 | -0.00856 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.69407 | -0.00844 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.94963 | -0.00835 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.81213 | -0.00829 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.02671 | -0.00824 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.07046 | -0.00814 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.88782 | -0.00812 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.87046 | -0.00809 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.75102 | -0.00806 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.94407 | -0.00798 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.91074 | -0.00797 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.82949 | -0.00789 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.04893 | -0.00787 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.10518 | -0.00762 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.93713 | -0.00747 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.09824 | -0.00743 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.71768 | -0.00738 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.96838 | -0.00737 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.96005 | -0.00731 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.98921 | -0.00721 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460897.19106 | -0.00717 | 127 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.78782 | -0.00691 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460897.45772 | -0.00681 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460897.26536 | -0.00660 | 146 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460897.44314 | -0.00659 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.18909 | -0.00656 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.00449 | -0.00647 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.20359 | -0.00644 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.12651 | -0.00640 | 82 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460897.46953 | -0.00622 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.97102 | -0.00616 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460897.48619 | -0.00616 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.36112 | -0.00611 | 228 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.11686 | -0.00608 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.05783 | -0.00607 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.24742 | -0.00604 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.01269 | -0.00602 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.28068 | -0.00590 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.14811 | -0.00589 | 21 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.11421 | -0.00586 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.85435 | -0.00585 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461121.20714 | -0.00584 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.84671 | -0.00582 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.02651 | -0.00580 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.86407 | -0.00572 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.59863 | -0.00569 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.24097 | -0.00560 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.87726 | -0.00558 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.37929 | -0.00558 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.00428 | -0.00549 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.20972 | -0.00530 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459039.98762 | -0.00516 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.62433 | -0.00506 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.83073 | -0.00496 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.82379 | -0.00484 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.19583 | -0.00484 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461111.91502 | -0.00481 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.40429 | -0.00478 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.88986 | -0.00448 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461120.83907 | -0.00446 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.20347 | -0.00446 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.93223 | -0.00444 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459039.97928 | -0.00429 | 5 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.41887 | -0.00396 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459040.42443 | -0.00387 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.93986 | -0.00375 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.52780 | -0.01146 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.39516 | -0.01094 | 2 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.89338 | -0.01061 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.87015 | -0.01049 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.38961 | -0.01036 | 4 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.48405 | -0.00928 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.83574 | -0.00869 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.37294 | -0.00834 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.20628 | -0.00827 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.45211 | -0.00825 | 4 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.41947 | -0.00820 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.21531 | -0.00820 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.46322 | -0.00817 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.77849 | -0.00812 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.57085 | -0.00811 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.63960 | -0.00801 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.42780 | -0.00791 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.90210 | -0.00782 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.44308 | -0.00781 | 7 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.06739 | -0.00775 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.75768 | -0.00774 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.26600 | -0.00766 | 4 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.36183 | -0.00743 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.43475 | -0.00735 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.82293 | -0.00734 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.70449 | -0.00719 | 7 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.40627 | -0.00705 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.50141 | -0.00705 | 5 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.51252 | -0.00702 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.78404 | -0.00697 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.56599 | -0.00693 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.02503 | -0.00682 | 3 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.08991 | -0.00681 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.15420 | -0.00675 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.26044 | -0.00668 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.30211 | -0.00658 | 4 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.38197 | -0.00657 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.22156 | -0.00650 | 4 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.62988 | -0.00644 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.74793 | -0.00642 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.25558 | -0.00640 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.34794 | -0.00639 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.69794 | -0.00635 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.77432 | -0.00633 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461119.85291 | -0.00628 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461119.81263 | -0.00627 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.47155 | -0.00626 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.59516 | -0.00611 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.33961 | -0.00598 | 4 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.83893 | -0.00596 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.57988 | -0.00595 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.54516 | -0.00594 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.82710 | -0.00581 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.81738 | -0.00578 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.73266 | -0.00576 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.50766 | -0.00565 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.92017 | -0.00562 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.01045 | -0.00553 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.08128 | -0.00543 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.99101 | -0.00541 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.28683 | -0.00540 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.68335 | -0.00536 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.90629 | -0.00535 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.97851 | -0.00532 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461119.86610 | -0.00530 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.24378 | -0.00529 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.76460 | -0.00528 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.79029 | -0.00515 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.65557 | -0.00515 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.09864 | -0.00512 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.51808 | -0.00508 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.04725 | -0.00502 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.89238 | -0.00493 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461119.85846 | -0.00492 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.24794 | -0.00491 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.93545 | -0.00484 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461119.69595 | -0.00484 | 2 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.08157 | -0.00481 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.97434 | -0.00478 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.13267 | -0.00476 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.94656 | -0.00472 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.54099 | -0.00470 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460862.56066 | -0.00467 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.19239 | -0.00464 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.66321 | -0.00459 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.29308 | -0.00453 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460899.88823 | -0.00451 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460906.78665 | -0.00447 | 2 | SAP | 1 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461111.81779 | -0.00441 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 2460900.83127 | -0.00438 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460875.12532 | -0.00431 | 7 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461151.12266 | -0.00425 | 2 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.66695 | -0.00420 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 2461119.64178 | -0.00419 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461151.08655 | -0.00412 | 2 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.67463 | -0.00406 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.45518 | -0.00404 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.67598 | -0.00398 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461127.84914 | -0.00395 | 2 | PDCSAP | 2, 3 | no |
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | 2460146.65873 | -0.00393 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461151.04488 | -0.00383 | 2 | SAP | 3 | no |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 2459060.35497 | -0.00378 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461144.31117 | -0.00371 | 2 | SAP | 1 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461133.18139 | -0.00368 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460874.53018 | -0.00360 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.81348 | -0.00352 | 2 | SAP | 2 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.63986 | -0.00349 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 2460867.79264 | -0.00345 | 2 | SAP | 2 | no |
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | 2460149.98927 | -0.00342 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461145.83209 | -0.00335 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 2461143.18888 | -0.00330 | 2 | PDCSAP | 2, 3 | no |
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | 2460148.87261 | -0.00329 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6798.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:18:40Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:18:41Z: TOI-6798.01 (TIC 290403522, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:18:47Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:18:48Z: TYC 9332-703-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460136.5746: gap (catalogue 6829 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 60%, 40%, 30%, 10%, 10%, 60% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6798.01: Gaia DR3 6383086975484001664 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6798.01: Teff 6501 K, R* 1.45 ± 0.12, M* 1.31 ± 0.13, ρ* 0.43 ± 0.11 ρ☉ (dwarf sequence, M_G 3.32, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-6798.01: 5 Gaia neighbour(s) within 52.5", contamination 0.65%; depth 6829 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 73 persistent event(s), 23 clean; BJD 2459040.3793 suspect: SAP_BKG z=-5.4; BJD 2459040.4043 suspect: SAP_BKG z=-5.4; BJD 2459040.4189 suspect: SAP_BKG z=-5.4; BJD 2459040.4244 suspect: SAP_BKG z=-5.6 |
| Moving objects at screen-event epochs | inconclusive | 73 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6798.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6798.01: TYC 9332-703-1 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6798-01.yaml
python -m cygnus.multi report campaigns/toi-6798-01.yaml
```
