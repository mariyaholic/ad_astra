<!-- cygnus:generated-draft -->
# Known-object test, TOI-4725.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4725-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4204, calibrate_screen #4173, event_census #4191, fetch_independent #4195, fetch_products #4170, known_signal_recovery #4177, moving_objects #4194, period_aliases #4193, prior_art #4206, residual_screen #4185, stellar_context #4178, variability_guard #4205
- Runner finished (UTC): 2026-09-30T21:42:26Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4725.01 (BJD 2460234.2528: gap (catalogue 16220 ppm); BJD 2460236.3291: recovered, depth 7287 ± 872 ppm (catalogue 16220 ppm); BJD 2460238.4054: recovered, depth 15536 ± 965 ppm (catalogue 16220 ppm); BJD 2460240.4817: partial, depth 1997 ± 1213 ppm (catalogue 16220 ppm); BJD 2460242.5580: recovered, depth 12404 ± 851 ppm (catalogue 16220 ppm); BJD 2460244.6343: recovered, depth 10501 ± 864 ppm (catalogue 16220 ppm); BJD 2460246.7107: gap (catalogue 16220 ppm); BJD 2460248.7870: gap (catalogue 16220 ppm); BJD 2460250.8633: recovered, depth 11158 ± 806 ppm (catalogue 16220 ppm); BJD 2460252.9396: recovered, depth 16466 ± 916 ppm (catalogue 16220 ppm); BJD 2460255.0159: recovered, depth 11406 ± 779 ppm (catalogue 16220 ppm); BJD 2460257.0922: recovered, depth 19462 ± 837 ppm (catalogue 16220 ppm); BJD 2460259.1685: recovered, depth 16712 ± 964 ppm (catalogue 16220 ppm); BJD 2460261.2448: gap (catalogue 16220 ppm); BJD 2460263.3211: recovered, depth 11785 ± 1189 ppm (catalogue 16220 ppm); BJD 2460265.3974: recovered, depth 15216 ± 882 ppm (catalogue 16220 ppm); BJD 2460267.4737: recovered, depth 9103 ± 877 ppm (catalogue 16220 ppm); BJD 2460269.5500: recovered, depth 11085 ± 782 ppm (catalogue 16220 ppm); BJD 2460271.6263: recovered, depth 11922 ± 950 ppm (catalogue 16220 ppm); BJD 2460273.7027: gap (catalogue 16220 ppm); BJD 2460275.7790: partial, depth -2386 ± 2201 ppm (catalogue 16220 ppm); BJD 2460277.8553: recovered, depth 8546 ± 929 ppm (catalogue 16220 ppm); BJD 2460279.9316: recovered, depth 9755 ± 883 ppm (catalogue 16220 ppm); BJD 2460282.0079: recovered, depth 12633 ± 785 ppm (catalogue 16220 ppm); BJD 2460284.0842: recovered, depth 12967 ± 816 ppm (catalogue 16220 ppm)).
Outside the catalogued epoch the screen left 95 threshold entries forming **58 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4725.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 26587613 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 108.008894 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 15.348909 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459546.99513 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.0763072 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16220.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.223 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2651 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-02-05 12:03:06 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | lightcurve | 71 | False | `618f060fccf9fc23` | True |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | lightcurve | 72 | False | `502d195d1a38a749` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460234.25281 | gap | 0 | — | 16220 | — |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460236.32912 | recovered | 37 | 7287 ± 872 | 16220 | -0.19 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460238.40543 | recovered | 37 | 15536 ± 965 | 16220 | -0.05 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460240.48173 | partial | 27 | 1997 ± 1213 | 16220 | -0.12 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460242.55804 | recovered | 36 | 12404 ± 851 | 16220 | -0.03 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460244.63435 | recovered | 37 | 10501 ± 864 | 16220 | -0.23 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460246.71066 | gap | 0 | — | 16220 | — |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460248.78696 | gap | 0 | — | 16220 | — |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460250.86327 | recovered | 37 | 11158 ± 806 | 16220 | -0.07 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.93958 | recovered | 36 | 16466 ± 916 | 16220 | 0.12 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460255.01589 | recovered | 37 | 11406 ± 779 | 16220 | -0.03 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460257.09219 | recovered | 37 | 19462 ± 837 | 16220 | -0.09 |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460259.16850 | recovered | 37 | 16712 ± 964 | 16220 | -0.15 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460261.24481 | gap | 0 | — | 16220 | — |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460263.32111 | recovered | 36 | 11785 ± 1189 | 16220 | 0.05 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460265.39742 | recovered | 36 | 15216 ± 882 | 16220 | -0.01 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460267.47373 | recovered | 37 | 9103 ± 877 | 16220 | -0.09 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460269.55004 | recovered | 37 | 11085 ± 782 | 16220 | -0.29 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460271.62634 | recovered | 37 | 11922 ± 950 | 16220 | -0.01 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460273.70265 | gap | 0 | — | 16220 | — |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460275.77896 | partial | 15 | -2386 ± 2201 | 16220 | 0.26 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460277.85526 | recovered | 36 | 8546 ± 929 | 16220 | 0.04 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460279.93157 | recovered | 37 | 9755 ± 883 | 16220 | 0.14 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460282.00788 | recovered | 37 | 12633 ± 785 | 16220 | -0.10 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460284.08419 | recovered | 37 | 12967 ± 816 | 16220 | -0.05 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.55079 | -0.02457 | 3 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460266.25665 | -0.02274 | 7 | PDCSAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.58760 | -0.02240 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.85707 | -0.02198 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.46451 | -0.02187 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.55982 | -0.02148 | 4 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.51259 | -0.02134 | 4 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.50426 | -0.02130 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.44731 | -0.02120 | 2 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.69559 | -0.02082 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.46953 | -0.02010 | 2 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.79143 | -0.02010 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460266.24207 | -0.01984 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.61607 | -0.01981 | 3 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.62094 | -0.01962 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460266.20318 | -0.01945 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.59802 | -0.01944 | 3 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.61052 | -0.01942 | 3 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.70115 | -0.01931 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460266.21984 | -0.01886 | 2 | PDCSAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460238.89240 | -0.01885 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.57007 | -0.01874 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.49731 | -0.01850 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.52509 | -0.01846 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460259.38039 | -0.01837 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.67337 | -0.01777 | 2 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460266.23651 | -0.01755 | 2 | PDCSAP | 1 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.49176 | -0.01744 | 2 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.82060 | -0.01730 | 2 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.51884 | -0.01674 | 3 | PDCSAP | 2 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460259.34566 | -0.01653 | 2 | PDCSAP | 1, 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.53308 | -0.01637 | 2 | PDCSAP | 2 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460259.27066 | -0.01589 | 2 | PDCSAP | 1, 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.48412 | -0.01580 | 3 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460266.28235 | -0.01551 | 2 | PDCSAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.07845 | -0.01541 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.59350 | -0.01534 | 3 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460276.66851 | -0.01521 | 3 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460262.45217 | -0.01490 | 3 | PDCSAP | 2 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460279.29160 | -0.01388 | 2 | PDCSAP | 1 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.02845 | -0.01139 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.02081 | -0.01122 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.15485 | -0.01091 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.71314 | -0.01072 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.78467 | -0.01063 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.59368 | -0.01050 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.05345 | -0.01047 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.85343 | -0.01045 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.72564 | -0.01031 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.11596 | -0.01023 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.44506 | -0.00985 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.06456 | -0.00982 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.11031 | -0.00967 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460252.76037 | -0.00946 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000026587613-0267-s_lc.fits` | 2460280.33333 | -0.00852 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460238.82156 | -0.00850 | 2 | SAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460249.34616 | -0.00844 | 2 | SAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000026587613-0266-s_lc.fits` | 2460253.17152 | -0.00803 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4725.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:42:19Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:42:21Z: TOI-4725.01 (TIC 26587613, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:42:23Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:42:24Z: UCAC4 527-038840 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460234.2528: gap (catalogue 16220 ppm); BJD 2460236.3291: recovered, depth 7287 ± 872 ppm (catalogue 16220 ppm); BJD 2460238.4054: recovered, depth 15536 ± 965 ppm (catalogue 16220 ppm); BJD 2460240.4817: partial, depth 1997 ± 1213 ppm (catalogue 16220 ppm); BJD 2460242.5580: recovered, depth 12404 ± 851 ppm (catalogue 16220 ppm); BJD 2460244.6343: recovered, depth 10501 ± 864 ppm (catalogue 16220 ppm); BJD 2460246.7107: gap (catalogue 16220 ppm); BJD 2460248.7870: gap (catalogue 16220 ppm); BJD 2460250.8633: recovered, depth 11158 ± 806 ppm (catalogue 16220 ppm); BJD 2460252.9396: recovered, depth 16466 ± 916 ppm (catalogue 16220 ppm); BJD 2460255.0159: recovered, depth 11406 ± 779 ppm (catalogue 16220 ppm); BJD 2460257.0922: recovered, depth 19462 ± 837 ppm (catalogue 16220 ppm); BJD 2460259.1685: recovered, depth 16712 ± 964 ppm (catalogue 16220 ppm); BJD 2460261.2448: gap (catalogue 16220 ppm); BJD 2460263.3211: recovered, depth 11785 ± 1189 ppm (catalogue 16220 ppm); BJD 2460265.3974: recovered, depth 15216 ± 882 ppm (catalogue 16220 ppm); BJD 2460267.4737: recovered, depth 9103 ± 877 ppm (catalogue 16220 ppm); BJD 2460269.5500: recovered, depth 11085 ± 782 ppm (catalogue 16220 ppm); BJD 2460271.6263: recovered, depth 11922 ± 950 ppm (catalogue 16220 ppm); BJD 2460273.7027: gap (catalogue 16220 ppm); BJD 2460275.7790: partial, depth -2386 ± 2201 ppm (catalogue 16220 ppm); BJD 2460277.8553: recovered, depth 8546 ± 929 ppm (catalogue 16220 ppm); BJD 2460279.9316: recovered, depth 9755 ± 883 ppm (catalogue 16220 ppm); BJD 2460282.0079: recovered, depth 12633 ± 785 ppm (catalogue 16220 ppm); BJD 2460284.0842: recovered, depth 12967 ± 816 ppm (catalogue 16220 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4725.01: Gaia DR3 3167706262483225088 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4725.01: Teff 5637 K, R* 0.95 ± 0.08, M* 0.97 ± 0.10, ρ* 1.13 ± 0.30 ρ☉ (dwarf sequence, M_G 4.91, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4725.01: 12 Gaia neighbour(s) within 52.5", contamination 50.86%; depth 7287 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 3167706266779188864, 3.5", ΔG 0.02); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-4725.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4725.01: UCAC4 527-038840 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4725-01.yaml
python -m cygnus.multi report campaigns/toi-4725-01.yaml
```
