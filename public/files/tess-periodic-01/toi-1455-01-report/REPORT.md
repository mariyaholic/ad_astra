<!-- [private Drive store] -->
# Known-object test, TOI-1455.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1455-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #755, calibrate_screen #422, event_census #433, fetch_products #421, known_signal_recovery #426, moving_objects #723, period_aliases #434, prior_art #759, residual_screen #428, stellar_context #427, variability_guard #757
- Runner finished (UTC): 2026-09-26T10:18:04Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1455.01 (BJD 2460656.3959: recovered, depth 15025 ± 151 ppm (catalogue 17749 ppm)).
Outside the catalogued epoch the screen left 324 threshold entries forming **58 distinct event(s)**, **50 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460645.5292 matches the catalogued transit's depth (14627 vs 15025 ppm), 10.867 d later; 0 of 10 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1455.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 387259626 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 308.670288 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 66.440384 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460656.395911 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 17749.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.385 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.1543 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-07-23 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | lightcurve | 86 | True | `b95b7fff2f125376` | True |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | lightcurve | 17 | False | `fa216e865e32fa8d` | True |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | lightcurve | 18 | False | `82e806a653707d5f` | True |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | lightcurve | 52 | False | `d54ab7821fd92750` | True |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | lightcurve | 56 | False | `46389352cc2b4f94` | True |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | lightcurve | 58 | False | `2e061b0adeeffadd` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460656.39591 | recovered | 72 | 15025 ± 151 | 17749 | 0.01 |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | — | epoch not in this light curve | — | — | 17749 | — |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | — | epoch not in this light curve | — | — | 17749 | — |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | — | epoch not in this light curve | — | — | 17749 | — |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | — | epoch not in this light curve | — | — | 17749 | — |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | — | epoch not in this light curve | — | — | 17749 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458768.74774 | -0.01690 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.17147 | -0.01681 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458765.09219 | -0.01661 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.18397 | -0.01627 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458765.13663 | -0.01614 | 44 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.14230 | -0.01613 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458804.97241 | -0.01610 | 72 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458772.34842 | -0.01599 | 47 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459830.31994 | -0.01594 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459884.67004 | -0.01593 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459728.87468 | -0.01592 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459906.40861 | -0.01590 | 65 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459833.94360 | -0.01584 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459826.69976 | -0.01576 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459891.91509 | -0.01574 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459888.29222 | -0.01574 | 66 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458783.23447 | -0.01572 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458808.59387 | -0.01567 | 73 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458779.61020 | -0.01565 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459721.62732 | -0.01565 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458794.10381 | -0.01560 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458797.72459 | -0.01554 | 73 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459899.16012 | -0.01551 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459841.19229 | -0.01550 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459844.81454 | -0.01538 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459736.12343 | -0.01537 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459902.78367 | -0.01536 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459725.25238 | -0.01522 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458786.85944 | -0.01521 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459895.53866 | -0.01520 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458768.71093 | -0.01513 | 31 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459739.74017 | -0.01497 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458812.21810 | -0.01491 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460660.02051 | -0.01487 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459848.43748 | -0.01482 | 72 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460645.52918 | -0.01475 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459732.48377 | -0.01468 | 48 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459837.56726 | -0.01423 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.11591 | -0.01336 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458801.34538 | -0.01309 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458768.77621 | -0.01297 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458772.39911 | -0.01218 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.19161 | -0.01016 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459736.07829 | -0.00849 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.10689 | -0.00755 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459739.78809 | -0.00743 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458765.07274 | -0.00713 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460649.19924 | -0.00685 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 2458786.80875 | -0.00604 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 2459826.64976 | -0.00459 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459910.02035 | -0.00649 | 10 | PDCSAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459909.99952 | -0.00627 | 2 | PDCSAP | 1, 2 | no |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459910.00438 | -0.00610 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 2459910.02452 | -0.00540 | 2 | PDCSAP | 1, 2 | no |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460636.48770 | -0.00508 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 2459736.16996 | -0.00466 | 2 | PDCSAP | 1 | no |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 2458791.09552 | -0.00413 | 4 | SAP | 1, 2 | no |
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 2460636.46756 | -0.00410 | 3 | PDCSAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460645.52918 | 14627 | 15025 | 10.8671 | 0 / 10 |  |
| 2460649.11591 | 12812 | 15025 | 7.2804 | 0 / 7 |  |
| 2460649.14230 | 14817 | 15025 | 7.2540 | 0 / 7 |  |
| 2460649.17147 | 14790 | 15025 | 7.2248 | 0 / 7 |  |
| 2460649.18397 | 13941 | 15025 | 7.2123 | 0 / 7 |  |
| 2460649.19161 | 8245 | 15025 | 7.2047 | 0 / 7 |  |
| 2460660.02051 | 14710 | 15025 | 3.6242 | 0 / 3 |  |
| 2458765.09219 | 15440 | 15025 | 1891.3041 | 21 / 1891 | 1891.3, 945.652, 630.435, 472.826, 315.217, 236.413, 210.145, 171.937, 157.609, 145.485, 111.253, 105.073, 99.5423, 78.8043, 72.7425, 65.2174, 55.6266, 52.5362, 32.6087, 21.7391 |
| 2458765.13663 | 15562 | 15025 | 1891.2597 | 21 / 1891 | 1891.26, 945.63, 630.42, 472.815, 315.21, 236.407, 210.14, 171.933, 157.605, 145.482, 111.251, 105.07, 99.54, 78.8025, 72.7408, 65.2159, 55.6253, 52.535, 32.6079, 21.7386 |
| 2458768.71093 | 15038 | 15025 | 1887.6854 | 19 / 1887 | 1887.69, 943.843, 629.229, 471.921, 314.614, 235.961, 209.743, 171.608, 157.307, 145.207, 111.04, 104.871, 99.3519, 78.6536, 72.6033, 65.0926, 55.5202, 52.4357, 49.6759 |
| 2458768.74774 | 15671 | 15025 | 1887.6486 | 19 / 1887 | 1887.65, 943.824, 629.216, 471.912, 314.608, 235.956, 209.739, 171.604, 157.304, 145.204, 111.038, 104.869, 99.3499, 78.652, 72.6019, 65.0913, 55.5191, 52.4347, 49.675 |
| 2458768.77621 | 12354 | 15025 | 1887.6201 | 20 / 1887 | 1887.62, 943.81, 629.207, 471.905, 314.603, 235.952, 209.736, 171.602, 157.302, 145.202, 111.037, 104.868, 99.3484, 78.6508, 72.6008, 65.0903, 55.5182, 52.4339, 49.6742, 3.6231 |
| 2458772.34842 | 15098 | 15025 | 1884.0479 | 30 / 1884 | 1884.05, 942.024, 628.016, 471.012, 376.81, 314.008, 235.506, 209.339, 188.405, 171.277, 157.004, 144.927, 125.603, 110.826, 104.669, 99.1604, 94.2024, 81.9151, 78.502, 72.4634 |
| 2458772.39911 | 11928 | 15025 | 1883.9972 | 32 / 1883 | 1884, 941.999, 627.999, 470.999, 376.799, 314, 235.5, 209.333, 188.4, 171.273, 157, 144.923, 125.6, 110.823, 104.666, 99.1577, 94.1999, 81.9129, 78.4999, 72.4614 |
| 2458779.61020 | 15153 | 15025 | 1876.7861 | 26 / 1876 | 1876.79, 938.393, 625.595, 469.197, 312.798, 268.112, 234.598, 208.532, 170.617, 156.399, 144.368, 134.056, 104.266, 98.7782, 89.3708, 78.1994, 72.1841, 67.0281, 64.7168, 60.5415 |
| 2458783.23447 | 15611 | 15025 | 1873.1618 | 26 / 1873 | 1873.16, 936.581, 624.387, 468.291, 312.194, 267.594, 234.145, 208.129, 170.287, 156.097, 144.089, 133.797, 117.073, 104.064, 98.5875, 89.1982, 78.0484, 72.0447, 66.8986, 64.5918 |
| 2458786.85944 | 14836 | 15025 | 1869.5368 | 23 / 1869 | 1869.54, 934.768, 623.179, 467.384, 311.589, 267.077, 233.692, 169.958, 155.795, 143.81, 133.538, 98.3967, 89.0256, 77.8974, 71.9053, 66.7692, 60.3076, 56.6526, 49.1983, 43.4776 |
| 2458794.10381 | 15601 | 15025 | 1862.2925 | 30 / 1862 | 1862.29, 931.146, 620.764, 465.573, 372.459, 310.382, 266.042, 232.787, 186.229, 169.299, 155.191, 143.253, 133.021, 124.153, 109.547, 98.0154, 93.1146, 88.6806, 77.5955, 74.4917 |
| 2458797.72459 | 15558 | 15025 | 1858.6717 | 18 / 1858 | 1858.67, 619.557, 371.734, 265.524, 206.519, 168.97, 142.975, 123.911, 97.8248, 88.5082, 74.3469, 68.8397, 59.9572, 56.3234, 53.1049, 41.3038, 32.6083, 10.8694 |
| 2458801.34538 | 8512 | 15025 | 1855.0509 | 30 / 1855 | 1855.05, 927.525, 618.35, 463.763, 371.01, 309.175, 265.007, 231.881, 206.117, 185.505, 168.641, 142.696, 132.504, 123.67, 115.941, 103.058, 97.6343, 92.7525, 88.3358, 71.3481 |
| 2458804.97241 | 15795 | 15025 | 1851.4239 | 24 / 1851 | 1851.42, 925.712, 617.141, 462.856, 370.285, 308.571, 264.489, 231.428, 185.142, 168.311, 142.417, 132.245, 123.428, 97.4434, 92.5712, 88.163, 71.2086, 66.1223, 61.7141, 59.7234 |
| 2458808.59387 | 15562 | 15025 | 1847.8024 | 30 / 1847 | 1847.8, 923.901, 615.934, 461.951, 369.56, 307.967, 263.972, 230.975, 184.78, 167.982, 142.139, 131.986, 123.187, 108.694, 97.2528, 92.3901, 87.9906, 71.0693, 65.9929, 61.5934 |
| 2458812.21810 | 14855 | 15025 | 1844.1782 | 13 / 1844 | 1844.18, 614.726, 368.836, 263.454, 204.909, 167.653, 141.86, 122.945, 97.062, 87.818, 80.1817, 55.8842, 52.6908 |
| 2459721.62732 | 15473 | 15025 | 934.7690 | 12 / 934 | 934.769, 467.385, 311.59, 233.692, 155.795, 133.538, 77.8974, 71.9053, 66.7692, 49.1984, 21.7388, 10.8694 |
| 2459725.25238 | 15056 | 15025 | 931.1439 | 14 / 931 | 931.144, 465.572, 310.381, 232.786, 186.229, 155.191, 133.021, 93.1144, 77.5953, 71.6265, 66.5103, 49.0076, 46.5572, 37.2458 |
| 2459728.87468 | 15765 | 15025 | 927.5216 | 15 / 927 | 927.522, 463.761, 309.174, 231.88, 185.504, 132.503, 115.94, 103.058, 92.7522, 71.3478, 66.2515, 57.9701, 46.3761, 28.9851, 14.4925 |
| 2459732.48377 | 14243 | 15025 | 923.9125 | 14 / 923 | 923.913, 461.956, 307.971, 230.978, 184.782, 131.988, 92.3913, 71.0702, 65.9938, 61.5942, 54.3478, 46.1956, 18.1159, 10.8696 |
| 2459736.07829 | 8229 | 15025 | 920.3180 | 13 / 920 | 920.318, 460.159, 306.773, 230.079, 184.064, 153.386, 131.474, 83.6653, 76.6932, 70.7937, 65.737, 61.3545, 40.0138 |
| 2459736.12343 | 15018 | 15025 | 920.2729 | 13 / 920 | 920.273, 460.136, 306.758, 230.068, 184.055, 153.379, 131.468, 83.6612, 76.6894, 70.7902, 65.7338, 61.3515, 40.0119 |
| 2459739.74017 | 14837 | 15025 | 916.6561 | 12 / 916 | 916.656, 458.328, 305.552, 229.164, 183.331, 130.951, 114.582, 83.3324, 70.512, 65.4754, 61.1104, 39.8546 |
| 2459826.69976 | 15605 | 15025 | 829.6965 | 8 / 829 | 829.697, 414.848, 276.565, 207.424, 165.939, 138.283, 118.528, 55.3131 |
| 2459830.31994 | 15852 | 15025 | 826.0763 | 13 / 826 | 826.076, 413.038, 275.359, 206.519, 165.215, 137.679, 82.6076, 68.8397, 43.4777, 41.3038, 21.7389, 14.4926, 10.8694 |
| 2459833.94360 | 15844 | 15025 | 822.4527 | 7 / 822 | 822.453, 411.226, 274.151, 164.49, 137.075, 117.493, 39.1644 |
| 2459837.56726 | 13978 | 15025 | 818.8290 | 7 / 818 | 818.829, 409.414, 272.943, 163.766, 136.471, 90.981, 43.0963 |
| 2459841.19229 | 15345 | 15025 | 815.2040 | 11 / 815 | 815.204, 407.602, 271.735, 203.801, 163.041, 135.867, 90.5782, 54.3469, 32.6082, 18.1156, 10.8694 |
| 2459844.81454 | 15377 | 15025 | 811.5818 | 16 / 811 | 811.582, 405.791, 270.527, 202.895, 162.316, 135.264, 115.94, 101.448, 90.1758, 81.1582, 67.6318, 57.9701, 50.7239, 28.9851, 25.3619, 14.4925 |
| 2459848.43748 | 14771 | 15025 | 807.9588 | 6 / 807 | 807.959, 403.979, 201.99, 161.592, 100.995, 73.4508 |
| 2459884.67004 | 15721 | 15025 | 771.7263 | 8 / 771 | 771.726, 385.863, 257.242, 192.932, 128.621, 96.4658, 70.1569, 10.8694 |
| 2459888.29222 | 15361 | 15025 | 768.1041 | 7 / 768 | 768.104, 384.052, 256.035, 192.026, 128.017, 96.013, 14.4925 |
| 2459891.91509 | 15577 | 15025 | 764.4812 | 6 / 764 | 764.481, 382.241, 254.827, 191.12, 127.413, 95.5601 |
| 2459895.53866 | 14808 | 15025 | 760.8576 | 16 / 760 | 760.858, 380.429, 253.619, 190.214, 152.172, 126.81, 108.694, 95.1072, 76.0858, 54.347, 50.7238, 36.2313, 25.3619, 21.7388, 18.1157, 10.8694 |
| 2459899.16012 | 15242 | 15025 | 757.2362 | 11 / 757 | 757.236, 378.618, 252.412, 189.309, 151.447, 126.206, 108.177, 94.6545, 75.7236, 68.8397, 39.8545 |
| 2459902.78367 | 14981 | 15025 | 753.6126 | 12 / 753 | 753.613, 376.806, 251.204, 188.403, 150.722, 125.602, 107.659, 94.2016, 57.9702, 47.1008, 28.9851, 14.4926 |
| 2459906.40861 | 15399 | 15025 | 749.9877 | 7 / 749 | 749.988, 249.996, 149.998, 107.141, 83.332, 32.6082, 10.8694 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1455.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:18:01Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:18:02Z: TOI-1455.01 (TIC 387259626, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:18:03Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:18:04Z: TOI-1455.01 (err); BD+65  1481 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460656.3959: recovered, depth 15025 ± 151 ppm (catalogue 17749 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, 3.5, 3, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 20%, 10%, 0%, 30%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 44 repeat-candidate event(s); first at BJD 2460645.5292, ΔT = 10.867 d, 0 of 10 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1455.01: Gaia DR3 2246355002042750976 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-1455.01: Teff 6419 K, R* 1.37 ± 0.11, M* 1.26 ± 0.13, ρ* 0.49 ± 0.13 ρ☉ (dwarf sequence, M_G 3.54, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1455.01: 9 Gaia neighbour(s) within 52.5", contamination 5.02%; depth 15025 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 2246372628588699648, 30.7", ΔG 3.50); a centroid test is needed |
| Pointing and quality census per event | failed | 50 persistent event(s), 14 clean; BJD 2460649.1069 suspect: manual exclude (in event), MOM_CENTR1 z=-5.2, POS_CORR1 z=-5.3; BJD 2460649.1159 suspect: manual exclude (in event), MOM_CENTR1 z=-5.2, POS_CORR1 z=-5.2; BJD 2460649.1423 suspect: manual exclude (in event), MOM_CENTR1 z=-5.1, POS_CORR1 z=-6.0; BJD 2460649.1715 suspect: manual exclude (in event), MOM_CENTR1 z=-5.8, POS_CORR1 z=-6.3 |
| Moving objects at screen-event epochs | inconclusive | 50 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 7 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1455.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-1455.01: BD+65  1481 otype SB* (multiple) at 0.6" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1455-01.yaml
python -m cygnus.multi report campaigns/toi-1455-01.yaml
```
