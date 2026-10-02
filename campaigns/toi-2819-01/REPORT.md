<!-- cygnus:generated-draft -->
# Known-object test, TOI-2819.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2819-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4634, calibrate_screen #4617, event_census #4625, fetch_independent #4629, fetch_products #4612, known_signal_recovery #4619, moving_objects #4627, period_aliases #4626, prior_art #4637, residual_screen #4621, stellar_context #4620, variability_guard #4636
- Runner finished (UTC): 2026-09-30T22:07:08Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2819.01 (BJD 2460236.7328: recovered, depth 5634 ± 317 ppm (catalogue 8721 ppm); BJD 2460241.1234: recovered, depth 5916 ± 323 ppm (catalogue 8721 ppm); BJD 2460245.5140: recovered, depth 5951 ± 327 ppm (catalogue 8721 ppm); BJD 2460249.9046: recovered, depth 7531 ± 330 ppm (catalogue 8721 ppm); BJD 2460254.2952: recovered, depth 7768 ± 328 ppm (catalogue 8721 ppm); BJD 2460258.6858: recovered, depth 7957 ± 369 ppm (catalogue 8721 ppm); BJD 2460263.0764: recovered, depth 6263 ± 350 ppm (catalogue 8721 ppm); BJD 2460267.4670: recovered, depth 6889 ± 330 ppm (catalogue 8721 ppm); BJD 2460271.8576: recovered, depth 5417 ± 308 ppm (catalogue 8721 ppm); BJD 2460276.2482: recovered, depth 1833 ± 353 ppm (catalogue 8721 ppm); BJD 2460280.6388: recovered, depth 4742 ± 308 ppm (catalogue 8721 ppm); BJD 2460285.0294: recovered, depth 3256 ± 395 ppm (catalogue 8721 ppm); BJD 2460667.0114: recovered, depth 7179 ± 358 ppm (catalogue 8721 ppm); BJD 2460671.4020: recovered, depth 7003 ± 318 ppm (catalogue 8721 ppm); BJD 2460675.7926: recovered, depth 4636 ± 319 ppm (catalogue 8721 ppm); BJD 2460680.1832: recovered, depth 5914 ± 359 ppm (catalogue 8721 ppm); BJD 2460684.5738: recovered, depth 5980 ± 300 ppm (catalogue 8721 ppm); BJD 2460688.9644: partial, depth 1954 ± 2164 ppm (catalogue 8721 ppm)).
Outside the catalogued epoch the screen left 133 threshold entries forming **60 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2819.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 387275908 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 109.783871 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 12.776861 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460236.732778 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.3905983 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8720.9304105 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.3792658 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6805 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-04-17 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | lightcurve | 71 | True | `8103881838c267d9` | True |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | lightcurve | 72 | False | `d526305134e50d9b` | True |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | lightcurve | 87 | False | `57f52096678cd740` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.73278 | recovered | 71 | 5634 ± 317 | 8721 | 0.02 |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460241.12338 | recovered | 71 | 5916 ± 323 | 8721 | 0.17 |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460245.51397 | recovered | 71 | 5951 ± 327 | 8721 | -0.06 |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460249.90457 | recovered | 72 | 7531 ± 330 | 8721 | 0.01 |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460254.29517 | recovered | 72 | 7768 ± 328 | 8721 | -0.32 |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460258.68577 | recovered | 72 | 7957 ± 369 | 8721 | 0.34 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460263.07637 | recovered | 72 | 6263 ± 350 | 8721 | -0.03 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460267.46697 | recovered | 72 | 6889 ± 330 | 8721 | 0.26 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460271.85756 | recovered | 72 | 5417 ± 308 | 8721 | -0.05 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460276.24816 | recovered | 72 | 1833 ± 353 | 8721 | -0.03 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460280.63876 | recovered | 72 | 4742 ± 308 | 8721 | -0.13 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460285.02936 | recovered | 72 | 3256 ± 395 | 8721 | 0.27 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460667.01141 | recovered | 72 | 7179 ± 358 | 8721 | -0.14 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460671.40201 | recovered | 71 | 7003 ± 318 | 8721 | 0.04 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460675.79261 | recovered | 71 | 4636 ± 319 | 8721 | -0.10 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460680.18321 | recovered | 71 | 5914 ± 359 | 8721 | -0.22 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460684.57380 | recovered | 71 | 5980 ± 300 | 8721 | -0.20 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.96440 | partial | 2 | 1954 ± 2164 | 8721 | -2.27 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460249.67377 | -0.01090 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.41159 | -0.01863 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.39979 | -0.01794 | 3 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.64771 | -0.01534 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.75326 | -0.01507 | 4 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.46993 | -0.01427 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.38868 | -0.01406 | 3 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.70604 | -0.01328 | 4 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.36854 | -0.01312 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.44354 | -0.01311 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.44909 | -0.01252 | 2 | SAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460676.23931 | -0.01174 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.46021 | -0.01162 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.31715 | -0.01157 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.40673 | -0.01156 | 3 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.43521 | -0.01143 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460676.29070 | -0.01126 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.20951 | -0.01120 | 3 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.42687 | -0.01084 | 2 | SAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.29493 | -0.01053 | 2 | SAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.37826 | -0.01044 | 4 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460675.96292 | -0.01011 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.43937 | -0.01011 | 2 | SAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460682.28728 | -0.01005 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460258.88432 | -0.00982 | 2 | PDCSAP | 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.01438 | -0.00982 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460669.23221 | -0.00976 | 2 | PDCSAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460682.77409 | -0.00971 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.46139 | -0.00968 | 2 | SAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460665.79738 | -0.00959 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.17525 | -0.00957 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460258.85654 | -0.00955 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460253.07825 | -0.00951 | 2 | SAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.35027 | -0.00936 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460249.38068 | -0.00933 | 2 | SAP | 2 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.29679 | -0.00932 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460258.92182 | -0.00931 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460258.99683 | -0.00917 | 2 | PDCSAP | 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460683.47687 | -0.00916 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460259.28296 | -0.00914 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.42389 | -0.00898 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460259.13990 | -0.00889 | 2 | PDCSAP | 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460665.73210 | -0.00877 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460676.01431 | -0.00875 | 2 | SAP | 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460665.80988 | -0.00874 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460253.01852 | -0.00856 | 2 | SAP | 2 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.65743 | -0.00852 | 2 | SAP | 1, 2 | no |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460263.60139 | -0.00830 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460272.81321 | -0.00826 | 2 | SAP | 1, 2, 3 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.13799 | -0.00823 | 2 | SAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.57390 | -0.00822 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460236.37111 | -0.00813 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460253.02825 | -0.00813 | 2 | SAP | 1, 2 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.69215 | -0.00811 | 2 | SAP | 1, 2 | no |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460265.74046 | -0.00804 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460258.97738 | -0.00796 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460272.78960 | -0.00792 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000387275908-0266-s_lc.fits` | 2460253.07131 | -0.00788 | 2 | SAP | 1, 2 | no |
| `tess2024353092137-s0087-0000000387275908-0284-s_lc.fits` | 2460688.54493 | -0.00718 | 2 | SAP | 1 | no |
| `tess2023315124025-s0072-0000000387275908-0267-s_lc.fits` | 2460272.88544 | -0.00703 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2819.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:06:46Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:06:49Z: TOI-2819.01 (TIC 387275908, disposition APC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:06:51Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:06:53Z: TOI-2819.01 (Pl?); TOI-2819 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460236.7328: recovered, depth 5634 ± 317 ppm (catalogue 8721 ppm); BJD 2460241.1234: recovered, depth 5916 ± 323 ppm (catalogue 8721 ppm); BJD 2460245.5140: recovered, depth 5951 ± 327 ppm (catalogue 8721 ppm); BJD 2460249.9046: recovered, depth 7531 ± 330 ppm (catalogue 8721 ppm); BJD 2460254.2952: recovered, depth 7768 ± 328 ppm (catalogue 8721 ppm); BJD 2460258.6858: recovered, depth 7957 ± 369 ppm (catalogue 8721 ppm); BJD 2460263.0764: recovered, depth 6263 ± 350 ppm (catalogue 8721 ppm); BJD 2460267.4670: recovered, depth 6889 ± 330 ppm (catalogue 8721 ppm); BJD 2460271.8576: recovered, depth 5417 ± 308 ppm (catalogue 8721 ppm); BJD 2460276.2482: recovered, depth 1833 ± 353 ppm (catalogue 8721 ppm); BJD 2460280.6388: recovered, depth 4742 ± 308 ppm (catalogue 8721 ppm); BJD 2460285.0294: recovered, depth 3256 ± 395 ppm (catalogue 8721 ppm); BJD 2460667.0114: recovered, depth 7179 ± 358 ppm (catalogue 8721 ppm); BJD 2460671.4020: recovered, depth 7003 ± 318 ppm (catalogue 8721 ppm); BJD 2460675.7926: recovered, depth 4636 ± 319 ppm (catalogue 8721 ppm); BJD 2460680.1832: recovered, depth 5914 ± 359 ppm (catalogue 8721 ppm); BJD 2460684.5738: recovered, depth 5980 ± 300 ppm (catalogue 8721 ppm); BJD 2460688.9644: partial, depth 1954 ± 2164 ppm (catalogue 8721 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2819.01: Gaia DR3 3166138805578006016 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2819.01: Teff 6119 K, R* 1.57 ± 0.13, M* 1.43 ± 0.14, ρ* 0.37 ± 0.10 ρ☉ (dwarf sequence, M_G 3.00, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2819.01: 13 Gaia neighbour(s) within 52.5", contamination 6.17%; depth 5634 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 3166138741154825728, 36.1", ΔG 3.65); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460249.6738 suspect: MOM_CENTR1 z=+7.3, MOM_CENTR2 z=-8.3, POS_CORR1 z=+11.0, POS_CORR2 z=-10.7, SAP_BKG z=+67.5 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2819.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2819.01: TOI-2819.01 otype Pl? (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2819-01.yaml
python -m cygnus.multi report campaigns/toi-2819-01.yaml
```
