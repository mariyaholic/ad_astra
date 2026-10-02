<!-- cygnus:generated-draft -->
# Known-object test, TOI-5237.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5237-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4979, calibrate_screen #4957, event_census #4964, fetch_independent #4975, fetch_products #4948, known_signal_recovery #4960, moving_objects #4966, period_aliases #4965, prior_art #4981, residual_screen #4962, stellar_context #4961, variability_guard #4980
- Runner finished (UTC): 2026-09-30T22:46:22Z

## Bottom line

Positive control **failed**: BJD 2460314.6676: not recovered, depth -402 ± 1353 ppm (catalogue 13920 ppm); BJD 2460317.6565: not recovered, depth -483 ± 1444 ppm (catalogue 13920 ppm); BJD 2460320.6455: not recovered, depth 1053 ± 1252 ppm (catalogue 13920 ppm); BJD 2460323.6345: not recovered, depth -720 ± 1290 ppm (catalogue 13920 ppm); BJD 2460326.6235: not recovered, depth 2655 ± 1337 ppm (catalogue 13920 ppm); BJD 2460329.6125: not recovered, depth 54 ± 1355 ppm (catalogue 13920 ppm); BJD 2460332.6015: not recovered, depth -1526 ± 1309 ppm (catalogue 13920 ppm); BJD 2460335.5904: not recovered, depth -427 ± 1212 ppm (catalogue 13920 ppm); BJD 2460338.5794: not recovered, depth 236 ± 1237 ppm (catalogue 13920 ppm); BJD 2460341.5684: gap (catalogue 13920 ppm); BJD 2460344.5574: not recovered, depth 2533 ± 1563 ppm (catalogue 13920 ppm); BJD 2460347.5464: not recovered, depth 1524 ± 1377 ppm (catalogue 13920 ppm); BJD 2460350.5354: not recovered, depth 7521 ± 1423 ppm (catalogue 13920 ppm); BJD 2460353.5244: not recovered, depth -4406 ± 1601 ppm (catalogue 13920 ppm); BJD 2460356.5133: not recovered, depth -1280 ± 1714 ppm (catalogue 13920 ppm); BJD 2460359.5023: not recovered, depth -3016 ± 1438 ppm (catalogue 13920 ppm); BJD 2460362.4913: not recovered, depth 518 ± 1324 ppm (catalogue 13920 ppm); BJD 2460365.4803: not recovered, depth -2042 ± 1317 ppm (catalogue 13920 ppm); BJD 2460508.9515: not recovered, depth 3743 ± 1428 ppm (catalogue 13920 ppm); BJD 2460511.9405: not recovered, depth -1988 ± 1425 ppm (catalogue 13920 ppm); BJD 2460514.9295: gap (catalogue 13920 ppm); BJD 2460517.9185: gap (catalogue 13920 ppm); BJD 2460520.9075: not recovered, depth 1170 ± 1263 ppm (catalogue 13920 ppm); BJD 2460523.8965: not recovered, depth 3374 ± 1357 ppm (catalogue 13920 ppm); BJD 2460526.8855: not recovered, depth -2465 ± 1318 ppm (catalogue 13920 ppm); BJD 2460529.8744: not recovered, depth 786 ± 1322 ppm (catalogue 13920 ppm); BJD 2460532.8634: not recovered, depth -735 ± 1342 ppm (catalogue 13920 ppm).
Outside the catalogued epoch the screen left 434 threshold entries forming **194 distinct event(s)**, **16 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5237.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 435740442 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 297.495261 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 29.891252 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459444.873065 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.9889845 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13920.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.858 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.4705 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | lightcurve | 74 | False | `b01fdf7c0e85c843` | True |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | lightcurve | 75 | False | `23e0158abbea1052` | True |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | lightcurve | 81 | False | `b28358235fb28261` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460314.66755 | not_recovered | 56 | -402 ± 1353 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460317.65654 | not_recovered | 55 | -483 ± 1444 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460320.64552 | not_recovered | 55 | 1053 ± 1252 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460323.63451 | not_recovered | 55 | -720 ± 1290 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460326.62349 | not_recovered | 56 | 2655 ± 1337 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460329.61248 | not_recovered | 56 | 54 ± 1355 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460332.60146 | not_recovered | 56 | -1526 ± 1309 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460335.59045 | not_recovered | 56 | -427 ± 1212 | 13920 | — |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460338.57943 | not_recovered | 56 | 236 ± 1237 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.56842 | gap | 0 | — | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460344.55740 | not_recovered | 56 | 2533 ± 1563 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460347.54638 | not_recovered | 56 | 1524 ± 1377 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460350.53537 | not_recovered | 56 | 7521 ± 1423 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.52435 | not_recovered | 48 | -4406 ± 1601 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460356.51334 | not_recovered | 56 | -1280 ± 1714 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460359.50232 | not_recovered | 55 | -3016 ± 1438 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460362.49131 | not_recovered | 55 | 518 ± 1324 | 13920 | — |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460365.48029 | not_recovered | 55 | -2042 ± 1317 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460508.95155 | not_recovered | 56 | 3743 ± 1428 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460511.94053 | not_recovered | 56 | -1988 ± 1425 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460514.92952 | gap | 0 | — | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460517.91850 | gap | 0 | — | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460520.90748 | not_recovered | 56 | 1170 ± 1263 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460523.89647 | not_recovered | 56 | 3374 ± 1357 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460526.88545 | not_recovered | 55 | -2465 ± 1318 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460529.87444 | not_recovered | 55 | 786 ± 1322 | 13920 | — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460532.86342 | not_recovered | 55 | -735 ± 1342 | 13920 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: —, 8h: 20000 |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: 20000, 8h: — |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460524.41614 | -0.04083 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460521.44184 | -0.03975 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460327.06277 | -0.03754 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460336.03768 | -0.03719 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460521.43351 | -0.03655 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460327.04472 | -0.03529 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.97947 | -0.03477 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460339.01477 | -0.03464 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460315.08732 | -0.03440 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460321.07536 | -0.03363 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460318.07335 | -0.03253 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460324.06281 | -0.03234 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460321.06564 | -0.03057 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460318.08515 | -0.02871 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.49604 | -0.02826 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460328.75441 | -0.02784 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460356.96563 | -0.04897 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460342.00644 | -0.04759 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460509.45564 | -0.04231 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460509.46398 | -0.04142 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460351.00303 | -0.03989 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460512.46956 | -0.03927 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.99185 | -0.03917 | 2 | PDCSAP | 1, 2 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460530.38207 | -0.03889 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.96824 | -0.03885 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460344.97867 | -0.03878 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460362.95465 | -0.03873 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460339.85574 | -0.03834 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460356.97952 | -0.03794 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.98769 | -0.03706 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460356.95105 | -0.03696 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460521.41267 | -0.03695 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460530.37235 | -0.03682 | 2 | PDCSAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460509.47231 | -0.03647 | 2 | PDCSAP | 2 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460356.94411 | -0.03612 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460365.91585 | -0.03552 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460342.02033 | -0.03533 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.87796 | -0.03469 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460350.96275 | -0.03466 | 2 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.99671 | -0.03436 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460347.97661 | -0.03392 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460350.97664 | -0.03390 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460512.44595 | -0.03389 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460527.41890 | -0.03380 | 3 | PDCSAP | 2 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.84602 | -0.03375 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460350.95442 | -0.03372 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460527.38904 | -0.03365 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460359.94278 | -0.03347 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460362.94215 | -0.03345 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460362.91298 | -0.03339 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460359.95458 | -0.03339 | 2 | PDCSAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460512.45568 | -0.03313 | 2 | PDCSAP | 2 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460347.96688 | -0.03287 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460340.93769 | -0.03286 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460344.98908 | -0.03268 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460365.93391 | -0.03200 | 2 | PDCSAP | 2 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460365.92696 | -0.03188 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460345.02103 | -0.03151 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460347.98633 | -0.03070 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460339.86546 | -0.03046 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460339.85991 | -0.03023 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460359.93236 | -0.03017 | 5 | PDCSAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460318.09071 | -0.02972 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460338.98907 | -0.02960 | 2 | PDCSAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460324.06698 | -0.02885 | 2 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460341.97727 | -0.02882 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460339.00990 | -0.02860 | 2 | PDCSAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460337.11962 | -0.02778 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460362.92826 | -0.02776 | 2 | PDCSAP | 1 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460324.05725 | -0.02757 | 2 | PDCSAP | 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460324.03225 | -0.02743 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460315.10190 | -0.02685 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460321.07120 | -0.02609 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460330.24745 | -0.02501 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460361.06433 | -0.02315 | 18 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.92322 | -0.02267 | 3 | SAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460312.92558 | -0.02251 | 2 | SAP | 1, 2 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.89891 | -0.02213 | 2 | SAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460312.91863 | -0.02154 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.86003 | -0.02132 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.90447 | -0.02049 | 4 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.05933 | -0.02040 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.05100 | -0.01974 | 7 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.03989 | -0.01966 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.58354 | -0.01965 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.07878 | -0.01953 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.40854 | -0.01948 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.01419 | -0.01932 | 14 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.55298 | -0.01915 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.82947 | -0.01914 | 6 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.60298 | -0.01897 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.88503 | -0.01884 | 12 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.68771 | -0.01882 | 4 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.74187 | -0.01854 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.11489 | -0.01846 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460361.22753 | -0.01844 | 7 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.10170 | -0.01836 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.12114 | -0.01833 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.81975 | -0.01832 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.12739 | -0.01826 | 5 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.83711 | -0.01812 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.67868 | -0.01809 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.87114 | -0.01792 | 4 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.39118 | -0.01786 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.56293 | -0.01771 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.66687 | -0.01765 | 4 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.86489 | -0.01762 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.15656 | -0.01753 | 7 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.55993 | -0.01745 | 6 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.59348 | -0.01744 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.06767 | -0.01742 | 5 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.03086 | -0.01739 | 8 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.91003 | -0.01723 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.19892 | -0.01722 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.53632 | -0.01717 | 4 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.23850 | -0.01708 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.14336 | -0.01698 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.64187 | -0.01698 | 4 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.70298 | -0.01697 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.91628 | -0.01696 | 5 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.13711 | -0.01695 | 5 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.21420 | -0.01695 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.74604 | -0.01694 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.61548 | -0.01686 | 8 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460361.04905 | -0.01679 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.62937 | -0.01678 | 4 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.08433 | -0.01676 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.14892 | -0.01676 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.20725 | -0.01669 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.78007 | -0.01668 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.57382 | -0.01664 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.67382 | -0.01664 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.60251 | -0.01663 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.10934 | -0.01655 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460361.30878 | -0.01653 | 2 | SAP | 1, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.80655 | -0.01648 | 5 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.09336 | -0.01636 | 8 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.72937 | -0.01635 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.25448 | -0.01634 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.76757 | -0.01629 | 3 | SAP | 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460312.86308 | -0.01629 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.51965 | -0.01629 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.85516 | -0.01627 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.52520 | -0.01625 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.50020 | -0.01614 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.17809 | -0.01614 | 4 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.50576 | -0.01613 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.56709 | -0.01605 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.65159 | -0.01598 | 4 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.87660 | -0.01594 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.59765 | -0.01583 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.18920 | -0.01582 | 4 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.58979 | -0.01582 | 5 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.79614 | -0.01578 | 4 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460361.07961 | -0.01578 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.50182 | -0.01573 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.54882 | -0.01572 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.81271 | -0.01568 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.32809 | -0.01567 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.73771 | -0.01567 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.71062 | -0.01561 | 7 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.54326 | -0.01552 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.18364 | -0.01550 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.22045 | -0.01550 | 5 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.72173 | -0.01536 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.34753 | -0.01533 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.60715 | -0.01530 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.75646 | -0.01508 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.77243 | -0.01507 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.47243 | -0.01504 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460354.27253 | -0.01500 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.50993 | -0.01493 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.81419 | -0.01492 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.56757 | -0.01492 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.95460 | -0.01490 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.55876 | -0.01469 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460346.80576 | -0.01467 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460353.79058 | -0.01455 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.55390 | -0.01427 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000435740442-0270-s_lc.fits` | 2460360.54487 | -0.01420 | 2 | SAP | 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460318.07821 | -0.01328 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460312.89016 | -0.01277 | 3 | SAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000435740442-0276-s_lc.fits` | 2460524.42656 | -0.01258 | 2 | SAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460333.14048 | -0.01217 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460312.89919 | -0.01211 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460333.12173 | -0.01143 | 3 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460319.49068 | -0.01130 | 2 | SAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460330.06273 | -0.01063 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460319.47956 | -0.01053 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460312.95474 | -0.01049 | 2 | SAP | 1, 2 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460333.18909 | -0.01039 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460319.47123 | -0.01020 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460319.52540 | -0.01016 | 2 | SAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000435740442-0269-s_lc.fits` | 2460336.01407 | -0.00975 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5237.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:46:12Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:46:15Z: TOI-5237.01 (TIC 435740442, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:46:18Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:46:20Z: UCAC4 600-098358 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2460314.6676: not recovered, depth -402 ± 1353 ppm (catalogue 13920 ppm); BJD 2460317.6565: not recovered, depth -483 ± 1444 ppm (catalogue 13920 ppm); BJD 2460320.6455: not recovered, depth 1053 ± 1252 ppm (catalogue 13920 ppm); BJD 2460323.6345: not recovered, depth -720 ± 1290 ppm (catalogue 13920 ppm); BJD 2460326.6235: not recovered, depth 2655 ± 1337 ppm (catalogue 13920 ppm); BJD 2460329.6125: not recovered, depth 54 ± 1355 ppm (catalogue 13920 ppm); BJD 2460332.6015: not recovered, depth -1526 ± 1309 ppm (catalogue 13920 ppm); BJD 2460335.5904: not recovered, depth -427 ± 1212 ppm (catalogue 13920 ppm); BJD 2460338.5794: not recovered, depth 236 ± 1237 ppm (catalogue 13920 ppm); BJD 2460341.5684: gap (catalogue 13920 ppm); BJD 2460344.5574: not recovered, depth 2533 ± 1563 ppm (catalogue 13920 ppm); BJD 2460347.5464: not recovered, depth 1524 ± 1377 ppm (catalogue 13920 ppm); BJD 2460350.5354: not recovered, depth 7521 ± 1423 ppm (catalogue 13920 ppm); BJD 2460353.5244: not recovered, depth -4406 ± 1601 ppm (catalogue 13920 ppm); BJD 2460356.5133: not recovered, depth -1280 ± 1714 ppm (catalogue 13920 ppm); BJD 2460359.5023: not recovered, depth -3016 ± 1438 ppm (catalogue 13920 ppm); BJD 2460362.4913: not recovered, depth 518 ± 1324 ppm (catalogue 13920 ppm); BJD 2460365.4803: not recovered, depth -2042 ± 1317 ppm (catalogue 13920 ppm); BJD 2460508.9515: not recovered, depth 3743 ± 1428 ppm (catalogue 13920 ppm); BJD 2460511.9405: not recovered, depth -1988 ± 1425 ppm (catalogue 13920 ppm); BJD 2460514.9295: gap (catalogue 13920 ppm); BJD 2460517.9185: gap (catalogue 13920 ppm); BJD 2460520.9075: not recovered, depth 1170 ± 1263 ppm (catalogue 13920 ppm); BJD 2460523.8965: not recovered, depth 3374 ± 1357 ppm (catalogue 13920 ppm); BJD 2460526.8855: not recovered, depth -2465 ± 1318 ppm (catalogue 13920 ppm); BJD 2460529.8744: not recovered, depth 786 ± 1322 ppm (catalogue 13920 ppm); BJD 2460532.8634: not recovered, depth -735 ± 1342 ppm (catalogue 13920 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5237.01: Gaia DR3 2031857841338250240 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-5237.01: dwarf priors not applied — 1.01 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5237.01: 251 Gaia neighbour(s) within 52.5", contamination 94.24%; depth 13920 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 2031857841338047744, 41.9", ΔG -2.87); a centroid test is needed |
| Pointing and quality census per event | failed | 16 persistent event(s), 11 clean; BJD 2460324.0628 caution: manual exclude (within ±0.25 d); BJD 2460328.7544 suspect: SAP_BKG z=+7.6; BJD 2460339.0148 suspect: MOM_CENTR2 z=-5.7, POS_CORR1 z=+6.4, POS_CORR2 z=-8.2; BJD 2460346.4960 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 16 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5237.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5237.01: UCAC4 600-098358 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5237-01.yaml
python -m cygnus.multi report campaigns/toi-5237-01.yaml
```
