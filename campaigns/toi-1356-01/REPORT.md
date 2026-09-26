<!-- cygnus:generated-draft -->
# Known-object test, TOI-1356.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1356-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #65, calibrate_screen #19, event_census #40, fetch_products #5, known_signal_recovery #20, moving_objects #61, period_aliases #42, prior_art #67, residual_screen #29, stellar_context #21, variability_guard #66
- Runner finished (UTC): 2026-09-26T09:54:03Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1356.01 (BJD 2459849.2422: recovered, depth 6768 ± 27 ppm (catalogue 8802 ppm)).
Outside the catalogued epoch the screen left 245 threshold entries forming **85 distinct event(s)**, **16 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459800.7338 matches the catalogued transit's depth (6594 vs 6768 ppm), 48.509 d later; 2 of 48 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1356.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 277566483 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 311.19458 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 54.502161 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459849.242233 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8802.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 17.486 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.9468 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-05-19 10:10:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | lightcurve | 56 | True | `4651dbebf25ae770` | True |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | lightcurve | 55 | False | `065ebae741c7a50f` | True |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | lightcurve | 57 | False | `e1b28f3341c4919a` | True |
| `tess2024030031500-s0075-0000000277566483-0270-s_lc.fits` | lightcurve | 75 | False | `8da908eb43fb60f7` | True |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | lightcurve | 76 | False | `2a7fffea0ccbba02` | True |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | lightcurve | 77 | False | `ae8268ef7dbf6de4` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459849.24223 | recovered | 524 | 6768 ± 27 | 8802 | 0.00 |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | — | epoch not in this light curve | — | — | 8802 | — |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | — | epoch not in this light curve | — | — | 8802 | — |
| `tess2024030031500-s0075-0000000277566483-0270-s_lc.fits` | — | epoch not in this light curve | — | — | 8802 | — |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | — | epoch not in this light curve | — | — | 8802 | — |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | — | epoch not in this light curve | — | — | 8802 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2024030031500-s0075-0000000277566483-0270-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024030031500-s0075-0000000277566483-0270-s_lc.fits` | 2460358.58924 | -0.00753 | 500 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460382.84465 | -0.00685 | 492 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | 2459873.50163 | -0.00685 | 476 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459800.73379 | -0.00668 | 492 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | 2459873.16553 | -0.00294 | 6 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.63639 | -0.00294 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | 2459873.83635 | -0.00287 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.62042 | -0.00267 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.52805 | -0.00266 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.70028 | -0.00261 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.43916 | -0.00232 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.54611 | -0.00232 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.65028 | -0.00223 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.60861 | -0.00217 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.74611 | -0.00216 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.76556 | -0.00208 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.06155 | -0.00467 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.34009 | -0.00460 | 3 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.96572 | -0.00436 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.85738 | -0.00414 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.82960 | -0.00393 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.01989 | -0.00381 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.89627 | -0.00380 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.86363 | -0.00377 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.84211 | -0.00377 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.93308 | -0.00374 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.82127 | -0.00373 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459802.77550 | -0.00370 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.88099 | -0.00368 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.90738 | -0.00366 | 2 | PDCSAP | 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.12961 | -0.00365 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.97058 | -0.00363 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.18794 | -0.00363 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.93933 | -0.00363 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.86988 | -0.00359 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.05739 | -0.00356 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.79905 | -0.00356 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459838.14522 | -0.00353 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.16572 | -0.00348 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460406.97822 | -0.00347 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.19628 | -0.00347 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.00739 | -0.00338 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.11017 | -0.00330 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.10044 | -0.00329 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.04489 | -0.00325 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460407.03516 | -0.00322 | 2 | PDCSAP | 2, 3 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459838.46188 | -0.00314 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460401.85869 | -0.00311 | 2 | SAP | 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.09772 | -0.00296 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460401.68924 | -0.00293 | 2 | SAP | 1 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.40328 | -0.00291 | 2 | SAP | 2, 3 | no |
| `tess2024085201119-s0077-0000000277566483-0272-s_lc.fits` | 2460417.21547 | -0.00291 | 2 | SAP | 1 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459838.08550 | -0.00284 | 2 | SAP | 1, 2, 3 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459836.97994 | -0.00275 | 2 | SAP | 1, 2, 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.31023 | -0.00266 | 2 | SAP | 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.41092 | -0.00261 | 3 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000277566483-0245-s_lc.fits` | 2459873.15859 | -0.00259 | 2 | SAP | 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.49079 | -0.00258 | 2 | SAP | 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.12133 | -0.00257 | 2 | SAP | 2, 3 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459838.48966 | -0.00257 | 2 | SAP | 1, 2, 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.50190 | -0.00255 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460382.49812 | -0.00251 | 3 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.71556 | -0.00250 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459838.47300 | -0.00249 | 2 | SAP | 1, 2 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459853.02565 | -0.00242 | 2 | PDCSAP | 2, 3 | no |
| `tess2022217014003-s0055-0000000277566483-0242-s_lc.fits` | 2459803.47412 | -0.00241 | 2 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.68500 | -0.00230 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.67944 | -0.00230 | 2 | PDCSAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.68917 | -0.00223 | 2 | PDCSAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.45166 | -0.00219 | 2 | PDCSAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.72944 | -0.00217 | 4 | PDCSAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460381.32243 | -0.00214 | 2 | PDCSAP | 1, 2 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460373.03633 | -0.00209 | 2 | SAP | 1 | no |
| `tess2022244194134-s0056-0000000277566483-0243-s_lc.fits` | 2459838.44939 | -0.00207 | 2 | SAP | 1, 2 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.59889 | -0.00206 | 2 | PDCSAP | 2 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.70444 | -0.00203 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000277566483-0270-s_lc.fits` | 2460367.41137 | -0.00202 | 2 | PDCSAP | 1 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.71139 | -0.00199 | 2 | PDCSAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.46625 | -0.00198 | 3 | PDCSAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.55722 | -0.00196 | 2 | PDCSAP | 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.43500 | -0.00193 | 2 | PDCSAP | 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460393.70860 | -0.00185 | 2 | SAP | 1, 3 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460394.73917 | -0.00184 | 2 | SAP | 1, 2 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460367.78081 | -0.00176 | 2 | SAP | 1 | no |
| `tess2024058030222-s0076-0000000277566483-0271-s_lc.fits` | 2460373.65716 | -0.00172 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459800.73379 | 6594 | 6768 | 48.5086 | 2 / 48 | 48.5086, 24.2543 |
| 2459873.50163 | 6676 | 6768 | 24.2593 | 1 / 24 | 24.2593 |
| 2460358.58924 | 7075 | 6768 | 509.3469 | 9 / 509 | 509.347, 254.673, 169.782, 127.337, 101.869, 84.8911, 72.7638, 56.5941, 24.2546 |
| 2460382.84465 | 6586 | 6768 | 533.6023 | 12 / 533 | 533.602, 266.801, 177.867, 133.401, 106.721, 88.9337, 76.2289, 66.7003, 59.2891, 53.3602, 48.5093, 24.2546 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1356.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:53:59Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:54:01Z: TOI-1356.01 (TIC 277566483, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:54:02Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T09:54:02Z: HD 235349 (*); IRAS 20433+5418 (IR); TOI-1356.01 (Pl?); 2MASS J20444733+5430077 (NIR)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459849.2422: recovered, depth 6768 ± 27 ppm (catalogue 8802 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3.5, 3, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 80%, 100%, 70%, 100%, 100%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2459800.7338, ΔT = 48.509 d, 2 of 48 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (48.5086, 24.2543 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1356.01: Gaia DR3 2183687855788172672 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1356.01: dwarf priors not applied — RUWE 2.8424566 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1356.01: 66 Gaia neighbour(s) within 52.5", contamination 2.55%; depth 6768 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 16 persistent event(s), 3 clean; BJD 2459800.7338 suspect: SAP_BKG z=+6.8; BJD 2459873.5016 suspect: SAP_BKG z=-6.8; BJD 2460358.5892 suspect: MOM_CENTR1 z=-8.1, MOM_CENTR2 z=-8.0, POS_CORR1 z=-9.0, POS_CORR2 z=-7.4, SAP_BKG z=-8.2; BJD 2460382.8447 suspect: MOM_CENTR2 z=-6.9, POS_CORR2 z=-7.6, SAP_BKG z=-10.6 |
| Moving objects at screen-event epochs | inconclusive | 16 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 6 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1356.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1356.01: HD 235349 otype * (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1356-01.yaml
python -m cygnus.multi report campaigns/toi-1356-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** Both events land within 0.04 h (sigma 0.01 h) of predicted TOI-1356.01 transits at the catalogued P 24.2545 d. No new signal.

Source: `campaigns/toi-1356-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
