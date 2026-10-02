<!-- cygnus:generated-draft -->
# Known-object test, TOI-4012.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4012-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4889, calibrate_screen #4872, event_census #4881, fetch_independent #4884, fetch_products #4864, known_signal_recovery #4878, moving_objects #4883, period_aliases #4882, prior_art #4893, residual_screen #4880, stellar_context #4879, variability_guard #4890
- Runner finished (UTC): 2026-09-30T22:35:44Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4012.01 (BJD 2459883.1270: recovered, depth 22427 ± 1530 ppm (catalogue 21650 ppm); BJD 2459884.9524: recovered, depth 17861 ± 1314 ppm (catalogue 21650 ppm); BJD 2459886.7779: recovered, depth 18212 ± 1304 ppm (catalogue 21650 ppm); BJD 2459888.6033: recovered, depth 14913 ± 1334 ppm (catalogue 21650 ppm); BJD 2459890.4288: partial, depth 15449 ± 1344 ppm (catalogue 21650 ppm); BJD 2459892.2542: recovered, depth 17189 ± 1307 ppm (catalogue 21650 ppm); BJD 2459894.0796: recovered, depth 16081 ± 1285 ppm (catalogue 21650 ppm); BJD 2459895.9051: recovered, depth 14698 ± 1264 ppm (catalogue 21650 ppm); BJD 2459897.7305: recovered, depth 17958 ± 1415 ppm (catalogue 21650 ppm); BJD 2459899.5560: recovered, depth 20393 ± 1346 ppm (catalogue 21650 ppm); BJD 2459901.3814: recovered, depth 18737 ± 1300 ppm (catalogue 21650 ppm); BJD 2459903.2068: recovered, depth 18330 ± 1302 ppm (catalogue 21650 ppm); BJD 2459905.0323: recovered, depth 18948 ± 1271 ppm (catalogue 21650 ppm); BJD 2459906.8577: recovered, depth 22077 ± 1366 ppm (catalogue 21650 ppm); BJD 2459908.6832: recovered, depth 19702 ± 1371 ppm (catalogue 21650 ppm); BJD 2459718.8374: not recovered, depth 13214 ± 1814 ppm (catalogue 21650 ppm); BJD 2459720.6628: recovered, depth 19328 ± 1951 ppm (catalogue 21650 ppm); BJD 2459722.4883: recovered, depth 21589 ± 1750 ppm (catalogue 21650 ppm); BJD 2459724.3137: recovered, depth 19967 ± 1675 ppm (catalogue 21650 ppm); BJD 2459726.1392: recovered, depth 23533 ± 1588 ppm (catalogue 21650 ppm); BJD 2459727.9646: recovered, depth 19968 ± 1569 ppm (catalogue 21650 ppm); BJD 2459729.7900: recovered, depth 18647 ± 1497 ppm (catalogue 21650 ppm); BJD 2459731.6155: not recovered, depth 12287 ± 1915 ppm (catalogue 21650 ppm); BJD 2459733.4409: recovered, depth 14086 ± 1703 ppm (catalogue 21650 ppm); BJD 2459735.2664: not recovered, depth 17697 ± 1682 ppm (catalogue 21650 ppm); BJD 2459737.0918: recovered, depth 20428 ± 1623 ppm (catalogue 21650 ppm); BJD 2459738.9172: not recovered, depth 17355 ± 1625 ppm (catalogue 21650 ppm); BJD 2459740.7427: not recovered, depth 15862 ± 1543 ppm (catalogue 21650 ppm); BJD 2459742.5681: not recovered, depth 15903 ± 1483 ppm (catalogue 21650 ppm); BJD 2459910.5086: gap (catalogue 21650 ppm); BJD 2459912.3340: recovered, depth 29879 ± 1563 ppm (catalogue 21650 ppm); BJD 2459914.1595: recovered, depth 17974 ± 1362 ppm (catalogue 21650 ppm); BJD 2459915.9849: recovered, depth 17380 ± 1330 ppm (catalogue 21650 ppm); BJD 2459917.8104: not recovered, depth 18583 ± 1305 ppm (catalogue 21650 ppm); BJD 2459919.6358: not recovered, depth 18241 ± 1325 ppm (catalogue 21650 ppm); BJD 2459921.4612: partial, depth 14597 ± 1218 ppm (catalogue 21650 ppm); BJD 2459923.2867: recovered, depth 29856 ± 1375 ppm (catalogue 21650 ppm); BJD 2459925.1121: gap (catalogue 21650 ppm); BJD 2459926.9376: not recovered, depth 20661 ± 1466 ppm (catalogue 21650 ppm); BJD 2459928.7630: recovered, depth 24072 ± 1293 ppm (catalogue 21650 ppm); BJD 2459930.5884: recovered, depth 19572 ± 1374 ppm (catalogue 21650 ppm); BJD 2459932.4139: recovered, depth 18848 ± 1284 ppm (catalogue 21650 ppm); BJD 2459934.2393: recovered, depth 19696 ± 1347 ppm (catalogue 21650 ppm); BJD 2459936.0648: recovered, depth 17941 ± 1422 ppm (catalogue 21650 ppm); BJD 2460637.0337: recovered, depth 23891 ± 1301 ppm (catalogue 21650 ppm); BJD 2460638.8592: gap (catalogue 21650 ppm); BJD 2460640.6846: gap (catalogue 21650 ppm); BJD 2460642.5100: not recovered, depth 25558 ± 3275 ppm (catalogue 21650 ppm); BJD 2460644.3355: recovered, depth 20544 ± 1440 ppm (catalogue 21650 ppm); BJD 2460646.1609: not recovered, depth 16025 ± 1373 ppm (catalogue 21650 ppm); BJD 2460647.9864: recovered, depth 21909 ± 1306 ppm (catalogue 21650 ppm); BJD 2460649.8118: not recovered, depth 9093 ± 2671 ppm (catalogue 21650 ppm); BJD 2460651.6372: gap (catalogue 21650 ppm); BJD 2460653.4627: gap (catalogue 21650 ppm); BJD 2460655.2881: gap (catalogue 21650 ppm); BJD 2460657.1136: gap (catalogue 21650 ppm); BJD 2460658.9390: not recovered, depth 910 ± 5524 ppm (catalogue 21650 ppm); BJD 2460660.7644: recovered, depth 14067 ± 1360 ppm (catalogue 21650 ppm); BJD 2460662.5899: recovered, depth 26778 ± 1515 ppm (catalogue 21650 ppm)).
Outside the catalogued epoch the screen left 25 threshold entries forming **7 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4012.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 280315875 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 41.39883 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 66.359231 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459883.126997 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1.82544 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 21650.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.744 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.3507 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | lightcurve | 58 | True | `c3ceb0fdd95d46dc` | True |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | lightcurve | 52 | False | `b1b5b55e15f2e420` | True |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | lightcurve | 59 | False | `04fdadf6334fe4a5` | True |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | lightcurve | 86 | False | `10ee7467099cafe6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459883.12700 | recovered | 52 | 22427 ± 1530 | 21650 | 0.05 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459884.95244 | recovered | 52 | 17861 ± 1314 | 21650 | 0.49 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459886.77788 | recovered | 53 | 18212 ± 1304 | 21650 | 0.01 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459888.60332 | recovered | 52 | 14913 ± 1334 | 21650 | 0.27 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459890.42876 | partial | 52 | 15449 ± 1344 | 21650 | 0.45 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459892.25420 | recovered | 53 | 17189 ± 1307 | 21650 | 0.12 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459894.07964 | recovered | 52 | 16081 ± 1285 | 21650 | -0.17 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459895.90508 | recovered | 52 | 14698 ± 1264 | 21650 | -0.53 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459897.73052 | recovered | 52 | 17958 ± 1415 | 21650 | 0.06 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459899.55596 | recovered | 53 | 20393 ± 1346 | 21650 | 0.16 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459901.38140 | recovered | 52 | 18737 ± 1300 | 21650 | -0.43 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459903.20684 | recovered | 52 | 18330 ± 1302 | 21650 | -0.26 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459905.03228 | recovered | 53 | 18948 ± 1271 | 21650 | -0.08 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459906.85772 | recovered | 52 | 22077 ± 1366 | 21650 | -0.21 |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459908.68316 | recovered | 52 | 19702 ± 1371 | 21650 | -0.21 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459718.83740 | not_recovered | 52 | 13214 ± 1814 | 21650 | — |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459720.66284 | recovered | 52 | 19328 ± 1951 | 21650 | 0.60 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459722.48828 | recovered | 53 | 21589 ± 1750 | 21650 | -0.03 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459724.31372 | recovered | 52 | 19967 ± 1675 | 21650 | 0.23 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459726.13916 | recovered | 52 | 23533 ± 1588 | 21650 | 0.16 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459727.96460 | recovered | 53 | 19968 ± 1569 | 21650 | -0.45 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459729.79004 | recovered | 52 | 18647 ± 1497 | 21650 | -0.16 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459731.61548 | not_recovered | 52 | 12287 ± 1915 | 21650 | — |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459733.44092 | recovered | 52 | 14086 ± 1703 | 21650 | -0.54 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459735.26636 | not_recovered | 53 | 17697 ± 1682 | 21650 | — |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459737.09180 | recovered | 52 | 20428 ± 1623 | 21650 | -0.26 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459738.91724 | not_recovered | 52 | 17355 ± 1625 | 21650 | — |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459740.74268 | not_recovered | 53 | 15862 ± 1543 | 21650 | — |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459742.56812 | not_recovered | 52 | 15903 ± 1483 | 21650 | — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459910.50860 | gap | 0 | — | 21650 | — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459912.33404 | recovered | 52 | 29879 ± 1563 | 21650 | 0.01 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459914.15948 | recovered | 52 | 17974 ± 1362 | 21650 | -0.10 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459915.98492 | recovered | 53 | 17380 ± 1330 | 21650 | -0.03 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459917.81036 | not_recovered | 49 | 18583 ± 1305 | 21650 | — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459919.63580 | not_recovered | 52 | 18241 ± 1325 | 21650 | — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459921.46124 | partial | 53 | 14597 ± 1218 | 21650 | -0.18 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459923.28668 | recovered | 52 | 29856 ± 1375 | 21650 | 0.06 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459925.11212 | gap | 0 | — | 21650 | — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459926.93756 | not_recovered | 53 | 20661 ± 1466 | 21650 | — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459928.76300 | recovered | 52 | 24072 ± 1293 | 21650 | 0.22 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459930.58844 | recovered | 52 | 19572 ± 1374 | 21650 | 0.09 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459932.41388 | recovered | 53 | 18848 ± 1284 | 21650 | -0.53 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459934.23932 | recovered | 52 | 19696 ± 1347 | 21650 | -0.13 |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459936.06476 | recovered | 52 | 17941 ± 1422 | 21650 | 0.45 |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460637.03372 | recovered | 52 | 23891 ± 1301 | 21650 | -0.04 |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460638.85916 | gap | 0 | — | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460640.68460 | gap | 0 | — | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460642.51004 | not_recovered | 11 | 25558 ± 3275 | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460644.33548 | recovered | 53 | 20544 ± 1440 | 21650 | 0.12 |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460646.16092 | not_recovered | 52 | 16025 ± 1373 | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460647.98636 | recovered | 52 | 21909 ± 1306 | 21650 | -0.24 |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460649.81180 | not_recovered | 16 | 9093 ± 2671 | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460651.63724 | gap | 0 | — | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460653.46268 | gap | 0 | — | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460655.28812 | gap | 0 | — | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460657.11356 | gap | 0 | — | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460658.93900 | not_recovered | 4 | 910 ± 5524 | 21650 | — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460660.76444 | recovered | 53 | 14067 ± 1360 | 21650 | 0.28 |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 2460662.58988 | recovered | 52 | 26778 ± 1515 | 21650 | 0.14 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024326142117-s0086-0000000280315875-0283-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000280315875-0248-s_lc.fits` | 2459922.13143 | -0.03659 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000280315875-0224-s_lc.fits` | 2459721.09185 | -0.03458 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459896.46061 | -0.02887 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459896.37172 | -0.02872 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459882.47835 | -0.02666 | 2 | PDCSAP | 3 | no |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459882.71377 | -0.02635 | 3 | PDCSAP | 3 | no |
| `tess2022302161335-s0058-0000000280315875-0247-s_lc.fits` | 2459882.33807 | -0.02105 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4012.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:35:12Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:35:21Z: TOI-4012.01 (TIC 280315875, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:35:30Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:35:37Z: TOI-4012 (*); TOI-4012.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459883.1270: recovered, depth 22427 ± 1530 ppm (catalogue 21650 ppm); BJD 2459884.9524: recovered, depth 17861 ± 1314 ppm (catalogue 21650 ppm); BJD 2459886.7779: recovered, depth 18212 ± 1304 ppm (catalogue 21650 ppm); BJD 2459888.6033: recovered, depth 14913 ± 1334 ppm (catalogue 21650 ppm); BJD 2459890.4288: partial, depth 15449 ± 1344 ppm (catalogue 21650 ppm); BJD 2459892.2542: recovered, depth 17189 ± 1307 ppm (catalogue 21650 ppm); BJD 2459894.0796: recovered, depth 16081 ± 1285 ppm (catalogue 21650 ppm); BJD 2459895.9051: recovered, depth 14698 ± 1264 ppm (catalogue 21650 ppm); BJD 2459897.7305: recovered, depth 17958 ± 1415 ppm (catalogue 21650 ppm); BJD 2459899.5560: recovered, depth 20393 ± 1346 ppm (catalogue 21650 ppm); BJD 2459901.3814: recovered, depth 18737 ± 1300 ppm (catalogue 21650 ppm); BJD 2459903.2068: recovered, depth 18330 ± 1302 ppm (catalogue 21650 ppm); BJD 2459905.0323: recovered, depth 18948 ± 1271 ppm (catalogue 21650 ppm); BJD 2459906.8577: recovered, depth 22077 ± 1366 ppm (catalogue 21650 ppm); BJD 2459908.6832: recovered, depth 19702 ± 1371 ppm (catalogue 21650 ppm); BJD 2459718.8374: not recovered, depth 13214 ± 1814 ppm (catalogue 21650 ppm); BJD 2459720.6628: recovered, depth 19328 ± 1951 ppm (catalogue 21650 ppm); BJD 2459722.4883: recovered, depth 21589 ± 1750 ppm (catalogue 21650 ppm); BJD 2459724.3137: recovered, depth 19967 ± 1675 ppm (catalogue 21650 ppm); BJD 2459726.1392: recovered, depth 23533 ± 1588 ppm (catalogue 21650 ppm); BJD 2459727.9646: recovered, depth 19968 ± 1569 ppm (catalogue 21650 ppm); BJD 2459729.7900: recovered, depth 18647 ± 1497 ppm (catalogue 21650 ppm); BJD 2459731.6155: not recovered, depth 12287 ± 1915 ppm (catalogue 21650 ppm); BJD 2459733.4409: recovered, depth 14086 ± 1703 ppm (catalogue 21650 ppm); BJD 2459735.2664: not recovered, depth 17697 ± 1682 ppm (catalogue 21650 ppm); BJD 2459737.0918: recovered, depth 20428 ± 1623 ppm (catalogue 21650 ppm); BJD 2459738.9172: not recovered, depth 17355 ± 1625 ppm (catalogue 21650 ppm); BJD 2459740.7427: not recovered, depth 15862 ± 1543 ppm (catalogue 21650 ppm); BJD 2459742.5681: not recovered, depth 15903 ± 1483 ppm (catalogue 21650 ppm); BJD 2459910.5086: gap (catalogue 21650 ppm); BJD 2459912.3340: recovered, depth 29879 ± 1563 ppm (catalogue 21650 ppm); BJD 2459914.1595: recovered, depth 17974 ± 1362 ppm (catalogue 21650 ppm); BJD 2459915.9849: recovered, depth 17380 ± 1330 ppm (catalogue 21650 ppm); BJD 2459917.8104: not recovered, depth 18583 ± 1305 ppm (catalogue 21650 ppm); BJD 2459919.6358: not recovered, depth 18241 ± 1325 ppm (catalogue 21650 ppm); BJD 2459921.4612: partial, depth 14597 ± 1218 ppm (catalogue 21650 ppm); BJD 2459923.2867: recovered, depth 29856 ± 1375 ppm (catalogue 21650 ppm); BJD 2459925.1121: gap (catalogue 21650 ppm); BJD 2459926.9376: not recovered, depth 20661 ± 1466 ppm (catalogue 21650 ppm); BJD 2459928.7630: recovered, depth 24072 ± 1293 ppm (catalogue 21650 ppm); BJD 2459930.5884: recovered, depth 19572 ± 1374 ppm (catalogue 21650 ppm); BJD 2459932.4139: recovered, depth 18848 ± 1284 ppm (catalogue 21650 ppm); BJD 2459934.2393: recovered, depth 19696 ± 1347 ppm (catalogue 21650 ppm); BJD 2459936.0648: recovered, depth 17941 ± 1422 ppm (catalogue 21650 ppm); BJD 2460637.0337: recovered, depth 23891 ± 1301 ppm (catalogue 21650 ppm); BJD 2460638.8592: gap (catalogue 21650 ppm); BJD 2460640.6846: gap (catalogue 21650 ppm); BJD 2460642.5100: not recovered, depth 25558 ± 3275 ppm (catalogue 21650 ppm); BJD 2460644.3355: recovered, depth 20544 ± 1440 ppm (catalogue 21650 ppm); BJD 2460646.1609: not recovered, depth 16025 ± 1373 ppm (catalogue 21650 ppm); BJD 2460647.9864: recovered, depth 21909 ± 1306 ppm (catalogue 21650 ppm); BJD 2460649.8118: not recovered, depth 9093 ± 2671 ppm (catalogue 21650 ppm); BJD 2460651.6372: gap (catalogue 21650 ppm); BJD 2460653.4627: gap (catalogue 21650 ppm); BJD 2460655.2881: gap (catalogue 21650 ppm); BJD 2460657.1136: gap (catalogue 21650 ppm); BJD 2460658.9390: not recovered, depth 910 ± 5524 ppm (catalogue 21650 ppm); BJD 2460660.7644: recovered, depth 14067 ± 1360 ppm (catalogue 21650 ppm); BJD 2460662.5899: recovered, depth 26778 ± 1515 ppm (catalogue 21650 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4012.01: Gaia DR3 516549879835233408 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4012.01: Teff 4129 K, R* 0.66 ± 0.05, M* 0.67 ± 0.07, ρ* 2.38 ± 0.62 ρ☉ (dwarf sequence, M_G 7.20, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4012.01: 29 Gaia neighbour(s) within 52.5", contamination 58.46%; depth 22427 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 516549776756027520, 50.9", ΔG 0.31); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 2 clean; BJD 2459896.4606 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+6.4, POS_CORR1 z=+10.7, SAP_BKG z=+36.4 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-4012.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4012.01: TOI-4012 otype * (star_or_other) at 0.4" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4012-01.yaml
python -m cygnus.multi report campaigns/toi-4012-01.yaml
```
