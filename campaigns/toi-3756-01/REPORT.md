<!-- cygnus:generated-draft -->
# Known-object test, TOI-3756.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3756-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4162, calibrate_screen #4108, event_census #4124, fetch_independent #4141, fetch_products #4102, known_signal_recovery #4109, moving_objects #4134, period_aliases #4125, prior_art #4165, residual_screen #4117, stellar_context #4111, variability_guard #4163
- Runner finished (UTC): 2026-09-30T21:40:43Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3756.01 (BJD 2459912.4500: recovered, depth 8541 ± 487 ppm (catalogue 10682 ppm); BJD 2459916.8736: gap (catalogue 10682 ppm); BJD 2459921.2973: recovered, depth 8537 ± 427 ppm (catalogue 10682 ppm); BJD 2459925.7210: recovered, depth 7911 ± 568 ppm (catalogue 10682 ppm); BJD 2459930.1447: recovered, depth 9032 ± 541 ppm (catalogue 10682 ppm); BJD 2459934.5683: recovered, depth 11261 ± 549 ppm (catalogue 10682 ppm); BJD 2460288.4622: gap (catalogue 10682 ppm); BJD 2460292.8859: recovered, depth 6312 ± 567 ppm (catalogue 10682 ppm); BJD 2460297.3095: recovered, depth 6777 ± 480 ppm (catalogue 10682 ppm); BJD 2460301.7332: gap (catalogue 10682 ppm); BJD 2460306.1569: gap (catalogue 10682 ppm); BJD 2460310.5806: recovered, depth 3780 ± 582 ppm (catalogue 10682 ppm); BJD 2460637.9324: gap (catalogue 10682 ppm); BJD 2460642.3561: partial, depth -1050 ± 1476 ppm (catalogue 10682 ppm); BJD 2460646.7797: recovered, depth 261 ± 486 ppm (catalogue 10682 ppm); BJD 2460651.2034: gap (catalogue 10682 ppm); BJD 2460655.6271: gap (catalogue 10682 ppm); BJD 2460660.0507: recovered, depth 3588 ± 482 ppm (catalogue 10682 ppm)).
Outside the catalogued epoch the screen left 279 threshold entries forming **139 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460286.0496 matches the catalogued transit's depth (6016 vs 8541 ppm), 373.591 d later; 0 of 373 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3756.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 67300566 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 83.653007 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 36.939626 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459912.449974 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.4236732 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10682.1531772 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.4711492 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.5552 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-08 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | lightcurve | 59 | True | `53c00ce3f661cc28` | True |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | lightcurve | 73 | False | `54eaba410e9cc74f` | True |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | lightcurve | 86 | False | `4d395a00f331868f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459912.44997 | recovered | 44 | 8541 ± 487 | 10682 | 0.21 |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459916.87365 | gap | 0 | — | 10682 | — |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459921.29732 | recovered | 44 | 8537 ± 427 | 10682 | 0.08 |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459925.72099 | recovered | 44 | 7911 ± 568 | 10682 | 0.05 |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459930.14467 | recovered | 44 | 9032 ± 541 | 10682 | -0.13 |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459934.56834 | recovered | 44 | 11261 ± 549 | 10682 | 0.12 |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460288.46220 | gap | 0 | — | 10682 | — |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460292.88587 | recovered | 44 | 6312 ± 567 | 10682 | -0.45 |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460297.30954 | recovered | 44 | 6777 ± 480 | 10682 | -0.37 |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460301.73322 | gap | 0 | — | 10682 | — |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460306.15689 | gap | 0 | — | 10682 | — |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460310.58056 | recovered | 44 | 3780 ± 582 | 10682 | -0.41 |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460637.93238 | gap | 0 | — | 10682 | — |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460642.35605 | partial | 5 | -1050 ± 1476 | 10682 | -0.23 |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460646.77973 | recovered | 44 | 261 ± 486 | 10682 | -1.01 |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460651.20340 | gap | 0 | — | 10682 | — |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460655.62707 | gap | 0 | — | 10682 | — |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460660.05074 | recovered | 44 | 3588 ± 482 | 10682 | -0.97 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.08014 | -0.01086 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460299.27603 | -0.01069 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.87736 | -0.00967 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.07458 | -0.00936 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.06069 | -0.00933 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.08569 | -0.00842 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.04958 | -0.00839 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.83291 | -0.00768 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.36558 | -0.01786 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.16975 | -0.01574 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.54128 | -0.01508 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.42044 | -0.01508 | 12 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.55426 | -0.01483 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.27669 | -0.01418 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.58204 | -0.01378 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.60309 | -0.01370 | 12 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.56211 | -0.01368 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.38225 | -0.01356 | 6 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.18086 | -0.01351 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.51420 | -0.01322 | 4 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.21350 | -0.01289 | 5 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.35656 | -0.01286 | 3 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.39058 | -0.01270 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.37392 | -0.01265 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.28086 | -0.01261 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.03641 | -0.01249 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.12391 | -0.01249 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.15286 | -0.01231 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.07022 | -0.01219 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.48503 | -0.01193 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.02391 | -0.01181 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.07530 | -0.01165 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.34753 | -0.01164 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.14891 | -0.01158 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.45447 | -0.01128 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.43225 | -0.01124 | 4 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.34197 | -0.01100 | 4 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.46350 | -0.01093 | 3 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.52670 | -0.01084 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.94201 | -0.01077 | 3 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.12947 | -0.01076 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.33294 | -0.01075 | 3 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.58920 | -0.01075 | 4 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459932.31790 | -0.01074 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.09336 | -0.01073 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.14475 | -0.01059 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.31489 | -0.01043 | 3 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.86353 | -0.01030 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.47808 | -0.01030 | 4 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.57253 | -0.01024 | 4 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.24058 | -0.01024 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.16558 | -0.01020 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.85798 | -0.01016 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.43919 | -0.01011 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460290.73158 | -0.01011 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.63159 | -0.00998 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.91214 | -0.00998 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.19683 | -0.00996 | 3 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.42509 | -0.00990 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.44406 | -0.00984 | 3 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460648.88641 | -0.00979 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.56954 | -0.00976 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.92742 | -0.00972 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.96902 | -0.00967 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460648.86835 | -0.00964 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.11697 | -0.00959 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.23641 | -0.00954 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.25378 | -0.00951 | 3 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459916.48164 | -0.00944 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.52787 | -0.00943 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460648.91558 | -0.00941 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.03569 | -0.00936 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.70798 | -0.00932 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.55378 | -0.00924 | 7 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.94125 | -0.00923 | 7 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.49892 | -0.00916 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.92256 | -0.00912 | 3 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459923.04008 | -0.00910 | 2 | SAP | 1, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.39454 | -0.00907 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459925.08593 | -0.00904 | 2 | PDCSAP | 1, 2 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.02041 | -0.00904 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460312.33552 | -0.00904 | 2 | PDCSAP | 1, 2 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.58017 | -0.00901 | 3 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.90451 | -0.00892 | 5 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.75034 | -0.00889 | 7 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.31975 | -0.00886 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.34176 | -0.00872 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460648.98849 | -0.00869 | 3 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.47232 | -0.00867 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.53086 | -0.00856 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460299.45797 | -0.00853 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.90652 | -0.00851 | 2 | SAP | 1, 2 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459928.01234 | -0.00847 | 2 | PDCSAP | 1, 2 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460299.39964 | -0.00845 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459929.99916 | -0.00845 | 3 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.79872 | -0.00841 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.73854 | -0.00840 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.90097 | -0.00836 | 5 | SAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459911.53844 | -0.00835 | 2 | PDCSAP | 1 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459923.33591 | -0.00833 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.29197 | -0.00832 | 4 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.82742 | -0.00829 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.93506 | -0.00827 | 5 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459929.70263 | -0.00822 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.71492 | -0.00821 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.99472 | -0.00820 | 3 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.02875 | -0.00813 | 4 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.00169 | -0.00809 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.87319 | -0.00809 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.95722 | -0.00807 | 3 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.06625 | -0.00805 | 4 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.04403 | -0.00805 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.91770 | -0.00800 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.84687 | -0.00798 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.64409 | -0.00796 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459923.33036 | -0.00795 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.89062 | -0.00789 | 3 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459923.21786 | -0.00787 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460641.09383 | -0.00787 | 3 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.86909 | -0.00786 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460299.31770 | -0.00786 | 4 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459930.00541 | -0.00784 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460640.93619 | -0.00775 | 2 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.91208 | -0.00774 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.49336 | -0.00768 | 4 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000067300566-0283-s_lc.fits` | 2460649.44892 | -0.00766 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000067300566-0248-s_lc.fits` | 2459923.13869 | -0.00762 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.09958 | -0.00757 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.70243 | -0.00752 | 4 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460298.88298 | -0.00750 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.93430 | -0.00749 | 4 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.09403 | -0.00745 | 3 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460299.43714 | -0.00743 | 4 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.85236 | -0.00742 | 2 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460292.06215 | -0.00739 | 2 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460286.00375 | -0.00734 | 6 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.92180 | -0.00714 | 2 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.98986 | -0.00690 | 2 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000067300566-0268-s_lc.fits` | 2460285.91625 | -0.00684 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460286.04958 | 6016 | 8541 | 373.5910 | 0 / 373 |  |
| 2460286.06069 | 6016 | 8541 | 373.6021 | 0 / 373 |  |
| 2460286.07458 | 6344 | 8541 | 373.6160 | 0 / 373 |  |
| 2460286.08014 | 6052 | 8541 | 373.6215 | 0 / 373 |  |
| 2460286.08569 | 6139 | 8541 | 373.6271 | 0 / 373 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3756.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:40:37Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:40:39Z: TOI-3756.01 (TIC 67300566, disposition APC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:40:40Z
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:40:41Z: 2MASS J05343562+3656099 (*); TOI-3756.01 (Pl?); TOI-3756 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459912.4500: recovered, depth 8541 ± 487 ppm (catalogue 10682 ppm); BJD 2459916.8736: gap (catalogue 10682 ppm); BJD 2459921.2973: recovered, depth 8537 ± 427 ppm (catalogue 10682 ppm); BJD 2459925.7210: recovered, depth 7911 ± 568 ppm (catalogue 10682 ppm); BJD 2459930.1447: recovered, depth 9032 ± 541 ppm (catalogue 10682 ppm); BJD 2459934.5683: recovered, depth 11261 ± 549 ppm (catalogue 10682 ppm); BJD 2460288.4622: gap (catalogue 10682 ppm); BJD 2460292.8859: recovered, depth 6312 ± 567 ppm (catalogue 10682 ppm); BJD 2460297.3095: recovered, depth 6777 ± 480 ppm (catalogue 10682 ppm); BJD 2460301.7332: gap (catalogue 10682 ppm); BJD 2460306.1569: gap (catalogue 10682 ppm); BJD 2460310.5806: recovered, depth 3780 ± 582 ppm (catalogue 10682 ppm); BJD 2460637.9324: gap (catalogue 10682 ppm); BJD 2460642.3561: partial, depth -1050 ± 1476 ppm (catalogue 10682 ppm); BJD 2460646.7797: recovered, depth 261 ± 486 ppm (catalogue 10682 ppm); BJD 2460651.2034: gap (catalogue 10682 ppm); BJD 2460655.6271: gap (catalogue 10682 ppm); BJD 2460660.0507: recovered, depth 3588 ± 482 ppm (catalogue 10682 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2460286.0496, ΔT = 373.591 d, 0 of 373 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3756.01: Gaia DR3 189461074831319680 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3756.01: Teff 5586 K, R* 1.07 ± 0.09, M* 1.04 ± 0.10, ρ* 0.85 ± 0.22 ρ☉ (dwarf sequence, M_G 4.43, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3756.01: 30 Gaia neighbour(s) within 52.5", contamination 37.90%; depth 8541 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 189461044769259648, 18.3", ΔG 0.83); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 0 clean; BJD 2460285.8329 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-8.8, MOM_CENTR2 z=+21.7, POS_CORR1 z=-11.5, POS_CORR2 z=+49.0, SAP_BKG z=-8.6; BJD 2460285.8774 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-7.9, MOM_CENTR2 z=+19.4, POS_CORR1 z=-22.5, POS_CORR2 z=+53.2, SAP_BKG z=-36.1; BJD 2460286.0496 caution: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), scattered light 2 (within ±0.25 d); BJD 2460286.0607 caution: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), scattered light 2 (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3756.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-3756.01: TOI-3756 otype SB* (multiple) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3756-01.yaml
python -m cygnus.multi report campaigns/toi-3756-01.yaml
```
