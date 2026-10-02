<!-- cygnus:generated-draft -->
# Known-object test, TOI-3751.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3751-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4788, calibrate_screen #4762, event_census #4778, fetch_independent #4784, fetch_products #4753, known_signal_recovery #4771, moving_objects #4781, period_aliases #4779, prior_art #4790, residual_screen #4773, stellar_context #4772, variability_guard #4789
- Runner finished (UTC): 2026-09-30T22:21:46Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3751.01 (BJD 2459910.8776: gap (catalogue 12630 ppm); BJD 2459913.7933: recovered, depth 11808 ± 613 ppm (catalogue 12630 ppm); BJD 2459916.7090: recovered, depth 9561 ± 725 ppm (catalogue 12630 ppm); BJD 2459919.6247: recovered, depth 11283 ± 614 ppm (catalogue 12630 ppm); BJD 2459922.5404: recovered, depth 9276 ± 617 ppm (catalogue 12630 ppm); BJD 2459925.4561: recovered, depth 12340 ± 631 ppm (catalogue 12630 ppm); BJD 2459928.3718: recovered, depth 10292 ± 576 ppm (catalogue 12630 ppm); BJD 2459931.2875: recovered, depth 11082 ± 619 ppm (catalogue 12630 ppm); BJD 2459934.2032: recovered, depth 10390 ± 596 ppm (catalogue 12630 ppm); BJD 2459476.4377: recovered, depth 9823 ± 576 ppm (catalogue 12630 ppm); BJD 2459479.3534: recovered, depth 11373 ± 622 ppm (catalogue 12630 ppm); BJD 2459482.2691: recovered, depth 10415 ± 592 ppm (catalogue 12630 ppm); BJD 2459485.1848: gap (catalogue 12630 ppm); BJD 2459488.1005: recovered, depth 10216 ± 584 ppm (catalogue 12630 ppm); BJD 2459491.0162: recovered, depth 10976 ± 583 ppm (catalogue 12630 ppm); BJD 2459493.9319: recovered, depth 11282 ± 588 ppm (catalogue 12630 ppm); BJD 2459496.8476: recovered, depth 10212 ± 592 ppm (catalogue 12630 ppm); BJD 2459502.6790: partial, depth 18850 ± 1282 ppm (catalogue 12630 ppm); BJD 2459505.5947: not recovered, depth 14655 ± 1297 ppm (catalogue 12630 ppm); BJD 2459508.5104: recovered, depth 17449 ± 1295 ppm (catalogue 12630 ppm); BJD 2459511.4261: partial, depth 16734 ± 1241 ppm (catalogue 12630 ppm); BJD 2459514.3418: recovered, depth 16621 ± 1319 ppm (catalogue 12630 ppm); BJD 2459517.2575: recovered, depth 23609 ± 1284 ppm (catalogue 12630 ppm); BJD 2459520.1732: not recovered, depth 17931 ± 1355 ppm (catalogue 12630 ppm); BJD 2459523.0889: recovered, depth 18149 ± 1401 ppm (catalogue 12630 ppm); BJD 2460211.1951: partial, depth 11201 ± 693 ppm (catalogue 12630 ppm); BJD 2460214.1108: partial, depth 11304 ± 751 ppm (catalogue 12630 ppm); BJD 2460217.0265: not recovered, depth 11990 ± 712 ppm (catalogue 12630 ppm); BJD 2460219.9422: gap (catalogue 12630 ppm); BJD 2460222.8579: not recovered, depth 9571 ± 728 ppm (catalogue 12630 ppm); BJD 2460225.7736: not recovered, depth 10147 ± 691 ppm (catalogue 12630 ppm); BJD 2460228.6893: not recovered, depth 12037 ± 714 ppm (catalogue 12630 ppm); BJD 2460231.6050: recovered, depth 11889 ± 773 ppm (catalogue 12630 ppm); BJD 2460234.5207: gap (catalogue 12630 ppm); BJD 2460237.4364: not recovered, depth 12201 ± 811 ppm (catalogue 12630 ppm); BJD 2460240.3521: recovered, depth 13213 ± 801 ppm (catalogue 12630 ppm); BJD 2460243.2678: not recovered, depth 7548 ± 814 ppm (catalogue 12630 ppm); BJD 2460246.1835: not recovered, depth 10015 ± 865 ppm (catalogue 12630 ppm); BJD 2460249.0992: partial, depth 9444 ± 825 ppm (catalogue 12630 ppm); BJD 2460252.0149: not recovered, depth 11896 ± 775 ppm (catalogue 12630 ppm); BJD 2460254.9306: not recovered, depth 10935 ± 778 ppm (catalogue 12630 ppm); BJD 2460257.8463: not recovered, depth 11169 ± 805 ppm (catalogue 12630 ppm); BJD 2460636.8879: not recovered, depth 7764 ± 682 ppm (catalogue 12630 ppm); BJD 2460639.8036: gap (catalogue 12630 ppm); BJD 2460642.7193: not recovered, depth 12910 ± 4713 ppm (catalogue 12630 ppm); BJD 2460645.6350: not recovered, depth 14178 ± 658 ppm (catalogue 12630 ppm); BJD 2460648.5507: not recovered, depth 10189 ± 645 ppm (catalogue 12630 ppm); BJD 2460651.4664: gap (catalogue 12630 ppm); BJD 2460654.3821: gap (catalogue 12630 ppm); BJD 2460657.2978: gap (catalogue 12630 ppm); BJD 2460660.2135: not recovered, depth 10949 ± 669 ppm (catalogue 12630 ppm)).
Outside the catalogued epoch the screen left 26 threshold entries forming **12 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3751.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 284173938 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 68.629023 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 32.476637 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459910.877562 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.9157041 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12630.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.375 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8826 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-08-06 12:03:27 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | lightcurve | 59 | True | `fbaf7ea354bef69a` | True |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | lightcurve | 43 | False | `9c24e74eaefc9e7b` | True |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | lightcurve | 44 | False | `4254f7352949eae5` | True |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | lightcurve | 70 | False | `64c2fa2337864ef6` | True |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | lightcurve | 71 | False | `77a32777ff442177` | True |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | lightcurve | 86 | False | `44fc533db5be7e04` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459910.87756 | gap | 0 | — | 12630 | — |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459913.79327 | recovered | 101 | 11808 ± 613 | 12630 | 0.43 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459916.70897 | recovered | 79 | 9561 ± 725 | 12630 | -0.38 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459919.62467 | recovered | 101 | 11283 ± 614 | 12630 | -0.61 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459922.54038 | recovered | 101 | 9276 ± 617 | 12630 | -0.09 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459925.45608 | recovered | 101 | 12340 ± 631 | 12630 | 0.45 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459928.37179 | recovered | 101 | 10292 ± 576 | 12630 | -0.39 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459931.28749 | recovered | 101 | 11082 ± 619 | 12630 | -0.07 |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459934.20319 | recovered | 101 | 10390 ± 596 | 12630 | -0.08 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459476.43765 | recovered | 102 | 9823 ± 576 | 12630 | 0.27 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459479.35336 | recovered | 101 | 11373 ± 622 | 12630 | 0.16 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459482.26906 | recovered | 94 | 10415 ± 592 | 12630 | 0.46 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459485.18476 | gap | 0 | — | 12630 | — |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459488.10047 | recovered | 101 | 10216 ± 584 | 12630 | -0.08 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459491.01617 | recovered | 101 | 10976 ± 583 | 12630 | 0.11 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459493.93188 | recovered | 101 | 11282 ± 588 | 12630 | -0.19 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2459496.84758 | recovered | 102 | 10212 ± 592 | 12630 | 0.44 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459502.67899 | partial | 101 | 18850 ± 1282 | 12630 | -0.51 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459505.59469 | not_recovered | 101 | 14655 ± 1297 | 12630 | — |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459508.51040 | recovered | 101 | 17449 ± 1295 | 12630 | 0.15 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459511.42610 | partial | 101 | 16734 ± 1241 | 12630 | -1.16 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459514.34180 | recovered | 101 | 16621 ± 1319 | 12630 | 0.30 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459517.25751 | recovered | 102 | 23609 ± 1284 | 12630 | -0.48 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459520.17321 | not_recovered | 101 | 17931 ± 1355 | 12630 | — |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459523.08892 | recovered | 101 | 18149 ± 1401 | 12630 | -0.38 |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460211.19508 | partial | 101 | 11201 ± 693 | 12630 | 0.15 |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460214.11079 | partial | 101 | 11304 ± 751 | 12630 | -0.68 |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460217.02649 | not_recovered | 101 | 11990 ± 712 | 12630 | — |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460219.94220 | gap | 0 | — | 12630 | — |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460222.85790 | not_recovered | 101 | 9571 ± 728 | 12630 | — |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460225.77360 | not_recovered | 102 | 10147 ± 691 | 12630 | — |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460228.68931 | not_recovered | 101 | 12037 ± 714 | 12630 | — |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460231.60501 | recovered | 101 | 11889 ± 773 | 12630 | 0.94 |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460234.52072 | gap | 0 | — | 12630 | — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460237.43642 | not_recovered | 101 | 12201 ± 811 | 12630 | — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460240.35213 | recovered | 101 | 13213 ± 801 | 12630 | -0.96 |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460243.26783 | not_recovered | 102 | 7548 ± 814 | 12630 | — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460246.18353 | not_recovered | 102 | 10015 ± 865 | 12630 | — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460249.09924 | partial | 101 | 9444 ± 825 | 12630 | 0.59 |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460252.01494 | not_recovered | 101 | 11896 ± 775 | 12630 | — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460254.93065 | not_recovered | 101 | 10935 ± 778 | 12630 | — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 2460257.84635 | not_recovered | 102 | 11169 ± 805 | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460636.88788 | not_recovered | 102 | 7764 ± 682 | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460639.80359 | gap | 0 | — | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460642.71929 | not_recovered | 2 | 12910 ± 4713 | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460645.63500 | not_recovered | 101 | 14178 ± 658 | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460648.55070 | not_recovered | 99 | 10189 ± 645 | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460651.46640 | gap | 0 | — | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460654.38211 | gap | 0 | — | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460657.29781 | gap | 0 | — | 12630 | — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 2460660.21352 | not_recovered | 101 | 10949 ± 669 | 12630 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2021258175143-s0043-0000000284173938-0214-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2023289093419-s0071-0000000284173938-0266-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2024326142117-s0086-0000000284173938-0283-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459912.25822 | -0.02085 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460232.58109 | -0.02748 | 2 | PDCSAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460232.61860 | -0.02707 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460232.62276 | -0.02705 | 2 | PDCSAP | 3 | no |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460232.63040 | -0.02685 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460232.61304 | -0.02545 | 2 | PDCSAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460232.64082 | -0.02537 | 2 | PDCSAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000284173938-0265-s_lc.fits` | 2460209.07910 | -0.02350 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459911.77350 | -0.01899 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459912.00683 | -0.01872 | 2 | PDCSAP | 2, 3 | no |
| `tess2021284114741-s0044-0000000284173938-0215-s_lc.fits` | 2459513.25722 | -0.01871 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000284173938-0248-s_lc.fits` | 2459912.46934 | -0.01851 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3751.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:21:29Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:21:34Z: TOI-3751.01 (TIC 284173938, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:21:38Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:21:41Z: TOI-3751.01 (Pl?); TOI-3751 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459910.8776: gap (catalogue 12630 ppm); BJD 2459913.7933: recovered, depth 11808 ± 613 ppm (catalogue 12630 ppm); BJD 2459916.7090: recovered, depth 9561 ± 725 ppm (catalogue 12630 ppm); BJD 2459919.6247: recovered, depth 11283 ± 614 ppm (catalogue 12630 ppm); BJD 2459922.5404: recovered, depth 9276 ± 617 ppm (catalogue 12630 ppm); BJD 2459925.4561: recovered, depth 12340 ± 631 ppm (catalogue 12630 ppm); BJD 2459928.3718: recovered, depth 10292 ± 576 ppm (catalogue 12630 ppm); BJD 2459931.2875: recovered, depth 11082 ± 619 ppm (catalogue 12630 ppm); BJD 2459934.2032: recovered, depth 10390 ± 596 ppm (catalogue 12630 ppm); BJD 2459476.4377: recovered, depth 9823 ± 576 ppm (catalogue 12630 ppm); BJD 2459479.3534: recovered, depth 11373 ± 622 ppm (catalogue 12630 ppm); BJD 2459482.2691: recovered, depth 10415 ± 592 ppm (catalogue 12630 ppm); BJD 2459485.1848: gap (catalogue 12630 ppm); BJD 2459488.1005: recovered, depth 10216 ± 584 ppm (catalogue 12630 ppm); BJD 2459491.0162: recovered, depth 10976 ± 583 ppm (catalogue 12630 ppm); BJD 2459493.9319: recovered, depth 11282 ± 588 ppm (catalogue 12630 ppm); BJD 2459496.8476: recovered, depth 10212 ± 592 ppm (catalogue 12630 ppm); BJD 2459502.6790: partial, depth 18850 ± 1282 ppm (catalogue 12630 ppm); BJD 2459505.5947: not recovered, depth 14655 ± 1297 ppm (catalogue 12630 ppm); BJD 2459508.5104: recovered, depth 17449 ± 1295 ppm (catalogue 12630 ppm); BJD 2459511.4261: partial, depth 16734 ± 1241 ppm (catalogue 12630 ppm); BJD 2459514.3418: recovered, depth 16621 ± 1319 ppm (catalogue 12630 ppm); BJD 2459517.2575: recovered, depth 23609 ± 1284 ppm (catalogue 12630 ppm); BJD 2459520.1732: not recovered, depth 17931 ± 1355 ppm (catalogue 12630 ppm); BJD 2459523.0889: recovered, depth 18149 ± 1401 ppm (catalogue 12630 ppm); BJD 2460211.1951: partial, depth 11201 ± 693 ppm (catalogue 12630 ppm); BJD 2460214.1108: partial, depth 11304 ± 751 ppm (catalogue 12630 ppm); BJD 2460217.0265: not recovered, depth 11990 ± 712 ppm (catalogue 12630 ppm); BJD 2460219.9422: gap (catalogue 12630 ppm); BJD 2460222.8579: not recovered, depth 9571 ± 728 ppm (catalogue 12630 ppm); BJD 2460225.7736: not recovered, depth 10147 ± 691 ppm (catalogue 12630 ppm); BJD 2460228.6893: not recovered, depth 12037 ± 714 ppm (catalogue 12630 ppm); BJD 2460231.6050: recovered, depth 11889 ± 773 ppm (catalogue 12630 ppm); BJD 2460234.5207: gap (catalogue 12630 ppm); BJD 2460237.4364: not recovered, depth 12201 ± 811 ppm (catalogue 12630 ppm); BJD 2460240.3521: recovered, depth 13213 ± 801 ppm (catalogue 12630 ppm); BJD 2460243.2678: not recovered, depth 7548 ± 814 ppm (catalogue 12630 ppm); BJD 2460246.1835: not recovered, depth 10015 ± 865 ppm (catalogue 12630 ppm); BJD 2460249.0992: partial, depth 9444 ± 825 ppm (catalogue 12630 ppm); BJD 2460252.0149: not recovered, depth 11896 ± 775 ppm (catalogue 12630 ppm); BJD 2460254.9306: not recovered, depth 10935 ± 778 ppm (catalogue 12630 ppm); BJD 2460257.8463: not recovered, depth 11169 ± 805 ppm (catalogue 12630 ppm); BJD 2460636.8879: not recovered, depth 7764 ± 682 ppm (catalogue 12630 ppm); BJD 2460639.8036: gap (catalogue 12630 ppm); BJD 2460642.7193: not recovered, depth 12910 ± 4713 ppm (catalogue 12630 ppm); BJD 2460645.6350: not recovered, depth 14178 ± 658 ppm (catalogue 12630 ppm); BJD 2460648.5507: not recovered, depth 10189 ± 645 ppm (catalogue 12630 ppm); BJD 2460651.4664: gap (catalogue 12630 ppm); BJD 2460654.3821: gap (catalogue 12630 ppm); BJD 2460657.2978: gap (catalogue 12630 ppm); BJD 2460660.2135: not recovered, depth 10949 ± 669 ppm (catalogue 12630 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 3, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3751.01: Gaia DR3 171829207584663808 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3751.01: dwarf priors not applied — 1.45 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3751.01: 16 Gaia neighbour(s) within 52.5", contamination 39.88%; depth 11808 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 171829207584664448, 32.6", ΔG 0.80); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2459912.2582 suspect: SAP_BKG z=+10.6 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3751.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3751.01: TOI-3751 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3751-01.yaml
python -m cygnus.multi report campaigns/toi-3751-01.yaml
```
