<!-- cygnus:generated-draft -->
# Known-object test, TOI-1351.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1351-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #827, calibrate_screen #692, event_census #699, fetch_products #688, known_signal_recovery #693, moving_objects #804, period_aliases #700, prior_art #829, residual_screen #695, stellar_context #694, variability_guard #828
- Runner finished (UTC): 2026-09-26T10:20:49Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1351.01 (BJD 2460654.5656: recovered, depth 13887 ± 210 ppm (catalogue 14536 ppm)).
Outside the catalogued epoch the screen left 342 threshold entries forming **60 distinct event(s)**, **38 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460636.7790 matches the catalogued transit's depth (9057 vs 13887 ppm), 17.786 d later; 0 of 17 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1351.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 1718201850 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 286.746549 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 71.712195 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460654.56565 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14536.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.928 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.3267 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-18 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | lightcurve | 86 | True | `07e7470eaf8e61ce` | True |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | lightcurve | 40 | False | `2516a74b7811ca62` | True |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | lightcurve | 41 | False | `83c7452b95ad14e6` | True |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | lightcurve | 47 | False | `29fcea879215e975` | True |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | lightcurve | 48 | False | `7f24fe25db5afa4a` | True |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | lightcurve | 49 | False | `570f25f28ed78231` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460654.56565 | recovered | 87 | 13887 ± 210 | 14536 | -0.01 |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | — | epoch not in this light curve | — | — | 14536 | — |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | — | epoch not in this light curve | — | — | 14536 | — |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | — | epoch not in this light curve | — | — | 14536 | — |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | — | epoch not in this light curve | — | — | 14536 | — |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | — | epoch not in this light curve | — | — | 14536 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 4 | False | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459403.45733 | -0.01791 | 74 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459397.56212 | -0.01741 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | 2459658.42102 | -0.01681 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459415.34774 | -0.01597 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459409.39697 | -0.01582 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459605.09465 | -0.01550 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | 2459646.58644 | -0.01538 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459427.17844 | -0.01511 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459634.70952 | -0.01497 | 83 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459397.52115 | -0.01451 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459439.03484 | -0.01399 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459421.23808 | -0.01388 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459628.77765 | -0.01345 | 77 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460636.77903 | -0.01341 | 72 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459599.12876 | -0.01333 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459616.91948 | -0.01329 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459587.28377 | -0.01316 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459444.97172 | -0.01293 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460660.49555 | -0.01254 | 78 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460648.63522 | -0.01226 | 73 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459605.10299 | -0.01121 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459439.08414 | -0.01054 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459444.92103 | -0.01045 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459444.92658 | -0.01042 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459397.58018 | -0.01028 | 10 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459599.08154 | -0.00989 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459403.51010 | -0.00943 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460640.99011 | -0.00915 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459415.26787 | -0.00889 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | 2459646.51839 | -0.00887 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459409.34280 | -0.00878 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459393.13430 | -0.00871 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460641.06511 | -0.00835 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459616.96810 | -0.00762 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459628.83459 | -0.00730 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459616.86532 | -0.00694 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460660.55110 | -0.00660 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460636.83250 | -0.00573 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459586.27267 | -0.01130 | 5 | PDCSAP | 1, 2 | no |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459586.28239 | -0.01114 | 2 | PDCSAP | 1, 2 | no |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459586.28795 | -0.01037 | 3 | PDCSAP | 1, 2 | no |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459586.32128 | -0.00913 | 2 | PDCSAP | 1 | no |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459605.11271 | -0.00886 | 2 | PDCSAP | 1 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460640.67345 | -0.00820 | 2 | PDCSAP+SAP | 3 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460641.04706 | -0.00808 | 2 | PDCSAP+SAP | 3 | no |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459614.72507 | -0.00602 | 2 | PDCSAP | 2 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460641.14845 | -0.00465 | 2 | SAP | 3 | no |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459599.17459 | -0.00394 | 3 | SAP | 1 | no |
| `tess2021175071901-s0040-0000001718201850-0211-s_lc.fits` | 2459397.48018 | -0.00379 | 2 | SAP | 1, 2 | no |
| `tess2021204101404-s0041-0000001718201850-0212-s_lc.fits` | 2459427.22913 | -0.00377 | 2 | SAP | 1, 2 | no |
| `tess2021364111932-s0047-0000001718201850-0218-s_lc.fits` | 2459599.18223 | -0.00365 | 2 | SAP | 1 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460641.01650 | -0.00364 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460641.12206 | -0.00331 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459631.62622 | -0.00318 | 2 | SAP | 3 | no |
| `tess2022057073128-s0049-0000001718201850-0221-s_lc.fits` | 2459646.51075 | -0.00311 | 2 | SAP | 1 | no |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459631.68594 | -0.00310 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460636.72625 | -0.00296 | 2 | SAP | 1 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460648.58036 | -0.00274 | 2 | SAP | 1, 2 | no |
| `tess2024326142117-s0086-0000001718201850-0283-s_lc.fits` | 2460646.32620 | -0.00257 | 2 | SAP | 1, 2 | no |
| `tess2022027120115-s0048-0000001718201850-0219-s_lc.fits` | 2459628.72209 | -0.00222 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460636.77903 | 9057 | 13887 | 17.7864 | 0 / 17 |  |
| 2460648.63522 | 11486 | 13887 | 5.9302 | 0 / 5 |  |
| 2460660.49555 | 11790 | 13887 | 5.9302 | 0 / 5 |  |
| 2459397.52115 | 12843 | 13887 | 1257.0442 | 17 / 1257 | 1257.04, 628.522, 419.015, 314.261, 209.507, 179.578, 157.131, 139.672, 114.277, 104.754, 89.7889, 69.8358, 59.8592, 57.1384, 23.7178, 11.8589, 5.9295 |
| 2459397.56212 | 12450 | 13887 | 1257.0033 | 17 / 1257 | 1257, 628.502, 419.001, 314.251, 209.5, 179.572, 157.125, 139.667, 114.273, 104.75, 89.7859, 69.8335, 59.8573, 57.1365, 23.717, 11.8585, 5.9293 |
| 2459403.45733 | 15556 | 13887 | 1251.1081 | 13 / 1251 | 1251.11, 625.554, 417.036, 312.777, 250.222, 156.388, 139.012, 125.111, 96.2391, 83.4072, 78.1943, 73.5946, 5.9294 |
| 2459403.51010 | 9432 | 13887 | 1251.0553 | 14 / 1251 | 1251.06, 625.528, 417.018, 312.764, 250.211, 156.382, 139.006, 125.106, 96.235, 83.4037, 78.191, 73.5915, 29.0943, 5.9292 |
| 2459409.34280 | 8348 | 13887 | 1245.2226 | 27 / 1245 | 1245.22, 622.611, 415.074, 311.306, 249.044, 207.537, 177.889, 155.653, 138.358, 124.522, 103.769, 88.9445, 83.0148, 69.179, 62.2611, 59.2963, 54.1401, 51.8843, 49.8089, 46.1194 |
| 2459409.39697 | 12615 | 13887 | 1245.1684 | 27 / 1245 | 1245.17, 622.584, 415.056, 311.292, 249.034, 207.528, 177.881, 155.646, 138.352, 124.517, 103.764, 88.9406, 83.0112, 69.176, 62.2584, 59.2937, 54.1378, 51.882, 49.8067, 46.1173 |
| 2459415.26787 | 7749 | 13887 | 1239.2975 | 12 / 1239 | 1239.3, 619.649, 413.099, 309.824, 206.55, 154.912, 137.7, 112.663, 103.275, 68.8499, 65.2262, 51.6374 |
| 2459415.34774 | 11530 | 13887 | 1239.2176 | 13 / 1239 | 1239.22, 619.609, 413.072, 309.804, 206.536, 154.902, 137.691, 112.656, 103.268, 68.8454, 65.222, 51.6341, 5.9293 |
| 2459421.23808 | 12925 | 13887 | 1233.3273 | 15 / 1233 | 1233.33, 616.664, 411.109, 308.332, 246.666, 154.166, 137.036, 123.333, 94.8713, 77.083, 72.5487, 47.4357, 23.7178, 11.8589, 5.9295 |
| 2459427.17844 | 13368 | 13887 | 1227.3869 | 16 / 1227 | 1227.39, 613.693, 409.129, 306.847, 245.477, 153.423, 136.376, 122.739, 76.7117, 61.3693, 53.3646, 49.0955, 45.4588, 42.3237, 17.7882, 5.9294 |
| 2459439.03484 | 12409 | 13887 | 1215.5305 | 15 / 1215 | 1215.53, 607.765, 405.177, 303.883, 243.106, 202.588, 135.059, 121.553, 101.294, 93.5023, 67.5295, 46.7512, 33.7647, 29.6471, 5.9294 |
| 2459439.08414 | 9266 | 13887 | 1215.4812 | 14 / 1215 | 1215.48, 607.741, 405.16, 303.87, 243.096, 202.58, 135.054, 121.548, 101.29, 93.4986, 67.5267, 33.7634, 29.6459, 5.9292 |
| 2459444.92658 | 8982 | 13887 | 1209.6388 | 21 / 1209 | 1209.64, 604.819, 403.213, 302.41, 241.928, 201.607, 151.205, 134.404, 120.964, 109.967, 100.803, 75.6024, 71.1552, 67.2022, 60.4819, 54.9836, 35.5776, 23.7184, 17.7888, 11.8592 |
| 2459444.97172 | 10381 | 13887 | 1209.5937 | 21 / 1209 | 1209.59, 604.797, 403.198, 302.398, 241.919, 201.599, 151.199, 134.399, 120.959, 109.963, 100.799, 75.5996, 71.1526, 67.1996, 60.4797, 54.9815, 35.5763, 23.7175, 17.7881, 11.8588 |
| 2459587.28377 | 11633 | 13887 | 1067.2816 | 20 / 1067 | 1067.28, 533.641, 355.76, 266.82, 213.456, 177.88, 133.41, 118.587, 106.728, 88.9401, 71.1521, 66.7051, 59.2934, 53.3641, 35.5761, 29.6467, 23.7174, 17.788, 11.8587, 5.9293 |
| 2459599.12876 | 11200 | 13887 | 1055.4366 | 13 / 1055 | 1055.44, 527.718, 351.812, 263.859, 211.087, 150.777, 131.93, 117.271, 105.544, 75.3883, 70.3624, 11.8588, 5.9294 |
| 2459605.09465 | 11643 | 13887 | 1049.4707 | 12 / 1049 | 1049.47, 524.735, 349.824, 262.368, 149.924, 131.184, 116.608, 74.9622, 61.7336, 49.9748, 17.7876, 5.9292 |
| 2459605.10299 | 9662 | 13887 | 1049.4624 | 12 / 1049 | 1049.46, 524.731, 349.821, 262.366, 149.923, 131.183, 116.607, 74.9616, 61.7331, 49.9744, 17.7875, 5.9292 |
| 2459616.91948 | 11137 | 13887 | 1037.6459 | 16 / 1037 | 1037.65, 518.823, 345.882, 259.411, 207.529, 148.235, 129.706, 115.294, 103.765, 79.8189, 69.1764, 51.8823, 49.4117, 41.5058, 29.647, 5.9294 |
| 2459628.77765 | 12580 | 13887 | 1025.7877 | 12 / 1025 | 1025.79, 512.894, 341.929, 256.447, 170.965, 146.541, 128.224, 85.4823, 78.9067, 60.3405, 48.847, 5.9294 |
| 2459634.70952 | 14106 | 13887 | 1019.8559 | 12 / 1019 | 1019.86, 509.928, 339.952, 254.964, 169.976, 145.694, 127.482, 92.7142, 84.988, 23.7176, 11.8588, 5.9294 |
| 2459646.51839 | 8299 | 13887 | 1008.0470 | 6 / 1008 | 1008.05, 504.024, 336.016, 168.008, 144.007, 91.6406 |
| 2459646.58644 | 11760 | 13887 | 1007.9789 | 13 / 1007 | 1007.98, 503.99, 335.993, 201.596, 167.996, 143.997, 100.798, 91.6344, 67.1986, 59.2929, 29.6464, 11.8586, 5.9293 |
| 2459658.42102 | 14286 | 13887 | 996.1444 | 21 / 996 | 996.144, 498.072, 332.048, 249.036, 199.229, 166.024, 142.306, 124.518, 99.6144, 90.5586, 83.012, 71.1532, 62.259, 49.8072, 47.4354, 41.506, 35.5766, 23.7177, 17.7883, 11.8589 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1351.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:20:46Z
- TESS_TOI (done, 2026-09-26): 3 match(es) in TESS_TOI within 30" as of 2026-09-26T10:20:47Z: TOI-1183.01 (TIC 258777137, disposition FP); TOI-1299.01 (TIC 258777134, disposition FP); TOI-1351.01 (TIC 1718201850, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:20:48Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T10:20:49Z: BD+71   931 (**); BD+71   931A (*); BD+71   931B (*); TOI-1299 (err)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460654.5656: recovered, depth 13887 ± 210 ppm (catalogue 14536 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 4, 3.5, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 20%, 0%, 0%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 27 repeat-candidate event(s); first at BJD 2460636.7790, ΔT = 17.786 d, 0 of 17 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | not_tested | TOI-1351.01: gaia unavailable: Gaia TAP failed: HTTPError: 500 Server Error: 500 for url: https://gea.esac.esa.int/tap-server/tap/sync |
| Stellar priors (Gaia colour and parallax) | not_tested | TOI-1351.01: gaia unavailable: Gaia TAP failed: HTTPError: 500 Server Error: 500 for url: https://gea.esac.esa.int/tap-server/tap/sync |
| Blend and dilution census (Gaia DR3 cone) | not_tested | TOI-1351.01: gaia unavailable: Gaia TAP failed: HTTPError: 500 Server Error: 500 for url: https://gea.esac.esa.int/tap-server/tap/sync |
| Pointing and quality census per event | failed | 38 persistent event(s), 25 clean; BJD 2460636.7790 suspect: MOM_CENTR2 z=+5.4, POS_CORR2 z=+5.2; BJD 2460640.9901 caution: manual exclude (within ±0.25 d); BJD 2460641.0651 caution: manual exclude (within ±0.25 d); BJD 2460648.6352 suspect: manual exclude (within ±0.25 d), SAP_BKG z=-5.8 |
| Moving objects at screen-event epochs | inconclusive | 38 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 5 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1351.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1351.01: BD+71   931B otype * (star_or_other) at 0.6" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1351-01.yaml
python -m cygnus.multi report campaigns/toi-1351-01.yaml
```
