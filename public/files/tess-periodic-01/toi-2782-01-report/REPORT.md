<!-- [private Drive store] -->
# Known-object test, TOI-2782.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2782-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1084, calibrate_screen #948, event_census #960, fetch_products #941, known_signal_recovery #949, moving_objects #984, period_aliases #961, prior_art #1086, residual_screen #953, stellar_context #950, variability_guard #1085
- Runner finished (UTC): 2026-09-26T10:33:23Z

## Bottom line

Positive control **inconclusive**: BJD 2460234.2555: gap (catalogue 39315 ppm).
Outside the catalogued epoch the screen left 642 threshold entries forming **112 distinct event(s)**, **105 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2782.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 306903715 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 98.004524 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 16.585417 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460234.255467 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 39314.879177 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.7630352 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.3612 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-15 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | lightcurve | 71 | True | `cfae05fe97f32e30` | True |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | lightcurve | 72 | False | `e5572099c9d5f36c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460234.25547 | gap | 0 | — | 39315 | — |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | — | epoch not in this light curve | — | — | 39315 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460251.73126 | -0.06559 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460283.92705 | -0.06347 | 158 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.25192 | -0.05801 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460245.21195 | -0.05790 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460245.19042 | -0.05700 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460238.70720 | -0.05522 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460245.20084 | -0.05451 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460245.18278 | -0.05404 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460251.69584 | -0.05353 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460238.69608 | -0.05332 | 15 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.24428 | -0.05320 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.23317 | -0.05261 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460251.71945 | -0.05259 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.26025 | -0.05237 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460271.27363 | -0.05193 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460238.67733 | -0.05183 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460239.17252 | -0.05113 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.21303 | -0.05037 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460264.74960 | -0.05016 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460245.22237 | -0.04967 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.31596 | -0.04962 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460264.77182 | -0.04926 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460251.73890 | -0.04915 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460244.01602 | -0.04850 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460251.75140 | -0.04848 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460238.71692 | -0.04837 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460243.98407 | -0.04814 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.20886 | -0.04806 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460277.78649 | -0.04799 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460251.70000 | -0.04777 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.26581 | -0.04758 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460244.05491 | -0.04706 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460238.71206 | -0.04670 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.04373 | -0.04668 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.08998 | -0.04665 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.05623 | -0.04659 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460277.81149 | -0.04638 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460243.94796 | -0.04627 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.28387 | -0.04569 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.60472 | -0.04554 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.50437 | -0.04551 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.47451 | -0.04548 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.94646 | -0.04546 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.31095 | -0.04524 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.45020 | -0.04524 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460271.30280 | -0.04520 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.95757 | -0.04510 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.91243 | -0.04509 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.05317 | -0.04500 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.93813 | -0.04491 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.30401 | -0.04486 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.36026 | -0.04470 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.90201 | -0.04434 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.11220 | -0.04433 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.08026 | -0.04413 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.29929 | -0.04409 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.34360 | -0.04376 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.06289 | -0.04365 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.37276 | -0.04334 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.01428 | -0.04332 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.43423 | -0.04287 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.07331 | -0.04246 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.09762 | -0.04239 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.27692 | -0.04227 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.91868 | -0.04227 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.39429 | -0.04205 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.40714 | -0.04205 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.48145 | -0.04189 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460277.76149 | -0.04130 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.03164 | -0.04099 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.49812 | -0.04098 | 8 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.92563 | -0.04091 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.97979 | -0.04082 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.02539 | -0.04078 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.45923 | -0.04041 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.90757 | -0.04034 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.32568 | -0.04022 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.97563 | -0.03960 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.98535 | -0.03913 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.29498 | -0.03905 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.46548 | -0.03848 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.42312 | -0.03846 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.26790 | -0.03833 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460271.23891 | -0.03816 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.41617 | -0.03808 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.33749 | -0.03803 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.04275 | -0.03758 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.12540 | -0.03747 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.00178 | -0.03725 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.88257 | -0.03714 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.51201 | -0.03701 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460268.38457 | -0.03677 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.27568 | -0.03670 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460277.82260 | -0.03669 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460271.31044 | -0.03661 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.89090 | -0.03572 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460277.75177 | -0.03511 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.96382 | -0.03457 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460264.72460 | -0.03432 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460264.80377 | -0.03391 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460282.87562 | -0.03371 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460278.10595 | -0.03349 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460275.92805 | -0.03342 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460275.95722 | -0.03314 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460263.52173 | -0.03244 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460244.00352 | -0.05410 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460258.23942 | -0.04795 | 2 | PDCSAP | 2 | no |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460239.14613 | -0.04652 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023289093419-s0071-0000000306903715-0266-s_lc.fits` | 2460239.09334 | -0.04531 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460284.28540 | -0.03602 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460271.22502 | -0.03047 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000306903715-0267-s_lc.fits` | 2460277.83927 | -0.02836 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2782.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:33:19Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:33:21Z: TOI-2782.01 (TIC 306903715, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:33:22Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:33:22Z: TOI-2782 (*); TOI-2782.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460234.2555: gap (catalogue 39315 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (4, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2782.01: Gaia DR3 3369407242490695168 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2782.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2782.01: 35 Gaia neighbour(s) within 52.5", contamination 48.01%; depth 39315 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 3369407311210163456, 41.5", ΔG 1.20); a centroid test is needed |
| Pointing and quality census per event | failed | 105 persistent event(s), 94 clean; BJD 2460245.1828 suspect: SAP_BKG z=-5.2; BJD 2460275.9281 suspect: scattered light 2 (in event), MOM_CENTR1 z=-7.2, POS_CORR1 z=-9.2, SAP_BKG z=+18.8; BJD 2460275.9572 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=-5.0, POS_CORR1 z=-10.8, SAP_BKG z=+19.5; BJD 2460283.9271 suspect: MOM_CENTR1 z=-10.4, MOM_CENTR2 z=-5.7, SAP_BKG z=+167.1 |
| Moving objects at screen-event epochs | failed | 105 event epoch(s) queried in SkyBoT (observer C57, r=600"); 2 with a known object bright enough (≥0.1× the depth in flux) within 63" plus its motion over 1 h; 13 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2782.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2782.01: TOI-2782.01 otype Pl? (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2782-01.yaml
python -m cygnus.multi report campaigns/toi-2782-01.yaml
```
