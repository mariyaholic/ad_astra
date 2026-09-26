<!-- [private Drive store] -->
# Known-object test, TOI-6806.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6806-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #141, calibrate_screen #31, event_census #56, fetch_products #2, known_signal_recovery #39, moving_objects #110, period_aliases #57, prior_art #145, residual_screen #50, stellar_context #41, variability_guard #142
- Runner finished (UTC): 2026-09-26T09:55:17Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6806.01 (BJD 2460202.8607: recovered, depth 44488 ± 206 ppm (catalogue 48641 ppm)).
Outside the catalogued epoch the screen left 229 threshold entries forming **69 distinct event(s)**, **19 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460156.3648 matches the catalogued transit's depth (44444 vs 44488 ppm), 46.497 d later; 2 of 46 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6806.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 144327080 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 355.545706 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -47.913029 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460202.860746 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 48641.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.914 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.3272 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | lightcurve | 69 | True | `074e913755e936b1` | True |
| `tess2023209231226-s0068-0000000144327080-0262-s_lc.fits` | lightcurve | 68 | False | `8738b258df4ee744` | True |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | lightcurve | 96 | False | `38a037ebc9ff1fdc` | True |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | lightcurve | 103 | False | `fe25e08706628983` | True |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | lightcurve | 104 | False | `d86a42a299c4ba52` | True |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | lightcurve | 105 | False | `8284c22e8eeae980` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460202.86075 | recovered | 118 | 44488 ± 206 | 48641 | 0.02 |
| `tess2023209231226-s0068-0000000144327080-0262-s_lc.fits` | — | epoch not in this light curve | — | — | 48641 | — |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 48641 | — |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | — | epoch not in this light curve | — | — | 48641 | — |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | — | epoch not in this light curve | — | — | 48641 | — |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | — | epoch not in this light curve | — | — | 48641 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2 | True | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023209231226-s0068-0000000144327080-0262-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | 3 | False | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | 2 | True | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000144327080-0262-s_lc.fits` | 2460156.36484 | -0.04705 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | 2461156.06905 | -0.04626 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | 2461202.56610 | -0.04603 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 2461225.78496 | -0.04594 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460923.57829 | -0.04584 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 2461225.83913 | -0.04229 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 2461225.85996 | -0.03304 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 2461225.74329 | -0.00945 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.07599 | -0.00920 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | 2461168.19903 | -0.00830 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000144327080-0305-s_lc.fits` | 2461168.18792 | -0.00812 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.01766 | -0.00780 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460205.97807 | -0.00759 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460191.72907 | -0.00748 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460912.44642 | -0.00741 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460191.70685 | -0.00732 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.05516 | -0.00714 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460191.71310 | -0.00650 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460912.47142 | -0.00615 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.91020 | -0.01040 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.14126 | -0.00906 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.18571 | -0.00884 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.96159 | -0.00878 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.14543 | -0.00849 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.81854 | -0.00832 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460927.06991 | -0.00815 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.75743 | -0.00796 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460191.75546 | -0.00770 | 2 | PDCSAP+SAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.58104 | -0.00769 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460909.68183 | -0.00769 | 3 | PDCSAP+SAP | 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.11210 | -0.00759 | 2 | PDCSAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.13867 | -0.00742 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | 2461197.79840 | -0.00734 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.96157 | -0.00725 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.08988 | -0.00725 | 2 | PDCSAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.12687 | -0.00716 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000144327080-0307-s_lc.fits` | 2461230.65050 | -0.00716 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.15446 | -0.00713 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460909.69780 | -0.00712 | 2 | PDCSAP+SAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460927.10463 | -0.00709 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.27964 | -0.00699 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.85324 | -0.00696 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.97685 | -0.00691 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460927.03935 | -0.00675 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.09543 | -0.00674 | 4 | PDCSAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.80604 | -0.00672 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.26992 | -0.00660 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460919.71722 | -0.00654 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.02460 | -0.00651 | 2 | PDCSAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460912.40615 | -0.00650 | 2 | PDCSAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.91715 | -0.00644 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460191.76518 | -0.00625 | 2 | PDCSAP+SAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460913.47976 | -0.00613 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460920.11166 | -0.00610 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460206.13224 | -0.00609 | 3 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460192.68600 | -0.00607 | 2 | PDCSAP+SAP | 1 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460201.18585 | -0.00606 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | 2461197.48588 | -0.00597 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460205.98432 | -0.00597 | 2 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460191.74574 | -0.00593 | 2 | PDCSAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460912.49087 | -0.00591 | 2 | PDCSAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460925.66576 | -0.00590 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460909.77210 | -0.00576 | 3 | PDCSAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460909.59780 | -0.00569 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000144327080-0306-s_lc.fits` | 2461197.68728 | -0.00559 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.61852 | -0.00545 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460909.71447 | -0.00538 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000144327080-0264-s_lc.fits` | 2460205.76905 | -0.00534 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000144327080-0293-s_lc.fits` | 2460926.59908 | -0.00517 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460156.36484 | 44444 | 44488 | 46.4967 | 2 / 46 | 46.4967, 23.2483 |
| 2460923.57829 | 44904 | 44488 | 720.7168 | 5 / 720 | 720.717, 360.358, 180.179, 102.96, 23.2489 |
| 2461156.06905 | 44738 | 44488 | 953.2075 | 12 / 953 | 953.207, 476.604, 317.736, 190.642, 158.868, 136.173, 105.912, 95.3208, 86.6552, 63.5472, 50.1688, 23.249 |
| 2461202.56610 | 44208 | 44488 | 999.7046 | 18 / 999 | 999.705, 499.852, 333.235, 249.926, 199.941, 166.617, 124.963, 111.078, 99.9705, 83.3087, 76.9004, 66.647, 62.4815, 58.8062, 52.616, 49.9852, 37.0261, 23.2489 |
| 2461225.74329 | 27717 | 44488 | 1022.8818 | 15 / 1022 | 1022.88, 511.441, 340.961, 255.72, 204.576, 170.48, 146.126, 127.86, 113.653, 92.9893, 85.2401, 73.063, 53.8359, 46.4946, 40.9153 |
| 2461225.78496 | 39179 | 44488 | 1022.9235 | 16 / 1022 | 1022.92, 511.462, 340.974, 255.731, 204.585, 170.487, 146.132, 127.865, 113.658, 92.993, 85.2436, 73.066, 53.8381, 46.4965, 40.9169, 23.2483 |
| 2461225.83913 | 44422 | 44488 | 1022.9776 | 16 / 1022 | 1022.98, 511.489, 340.993, 255.744, 204.595, 170.496, 146.14, 127.872, 113.664, 92.998, 85.2481, 73.0698, 53.8409, 46.499, 40.9191, 23.2495 |
| 2461225.85996 | 45678 | 44488 | 1022.9985 | 16 / 1022 | 1023, 511.499, 341, 255.75, 204.6, 170.5, 146.143, 127.875, 113.666, 92.9999, 85.2499, 73.0713, 53.842, 46.4999, 40.9199, 23.25 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6806.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:55:14Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:55:15Z: TOI-6806.01 (TIC 144327080, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T09:55:16Z: KELT KS29C20599 (type EA, P 23.24895 d)
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T09:55:16Z: Gaia DR3 6524854122121032704 (PM*); Gaia DR2 6524854122121032576 (SB*); CF 20441 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460202.8607: recovered, depth 44488 ± 206 ppm (catalogue 48641 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, ≤2.5, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 0%, 10%, 10%, 20%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 8 repeat-candidate event(s); first at BJD 2460156.3648, ΔT = 46.497 d, 2 of 46 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (46.4967, 23.2483 d); duration likelihood under Gaia priors (circular orbits) peaks at 23.2 d (weight 0.74) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6806.01: Gaia DR3 6524854122121032576 at 0.00" (propagated 2016.0 → J2015.5; 0.07" unpropagated, proper-motion shift 0.07") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6806.01: Teff 4928 K, R* 0.73 ± 0.06, M* 0.75 ± 0.07, ρ* 1.93 ± 0.50 ρ☉ (dwarf sequence, M_G 6.40, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6806.01: 2 Gaia neighbour(s) within 52.5", contamination 13.63%; depth 44488 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 6524854122121032704, 2.9", ΔG 2.01); a centroid test is needed |
| Pointing and quality census per event | failed | 19 persistent event(s), 10 clean; BJD 2460205.9781 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+8.6, POS_CORR1 z=+9.7, SAP_BKG z=+53.7; BJD 2460206.0177 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+6.4, POS_CORR1 z=+8.1, SAP_BKG z=+35.2; BJD 2460206.0552 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+8.1, POS_CORR1 z=+8.4, SAP_BKG z=+29.3; BJD 2460206.0760 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+9.0, POS_CORR1 z=+8.1, SAP_BKG z=+27.0 |
| Moving objects at screen-event epochs | inconclusive | 19 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 5 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | failed | TOI-6806.01: KELT KS29C20599                EA                             P=23.24895 at 2.3" (collides with alias 46.4967 d) |
| Object-class guard (SIMBAD) | inconclusive | TOI-6806.01: Gaia DR2 6524854122121032576 otype SB* (multiple) at 2.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6806-01.yaml
python -m cygnus.multi report campaigns/toi-6806-01.yaml
```
