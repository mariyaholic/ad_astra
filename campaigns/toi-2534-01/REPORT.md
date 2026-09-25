# Known-object test, TOI-2534.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The reviewer notes below were added by hand; every other number is the runner's.

> **Reviewer flag (2026-09-25):** the positive control is `not_tested` because **no retrieved SPOC light
> curve covers the catalogued epoch** (TIC 219332978 has SPOC data only from sector 28 onward; the
> catalogue's BJD 2458346.58 is a 2018 epoch). Separately, sector 103 contains one clean ~8 h, ~0.5 %
> dip whose depth and duration closely match the catalogue values. Recorded for a reviewer; outcome
> unchanged.

- Campaign spec: `campaigns/toi-2534-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #170, fetch_products #169, known_signal_recovery #171, period_aliases #173, prior_art #174, residual_screen #172
- Runner finished (UTC): 2026-09-25T02:52:29Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 216 threshold entries forming **71 distinct event(s)**, **28 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

**Positive control not tested.** The catalogued transit epoch (BJD 2458346.575) is not covered by any
retrieved SPOC light curve: TIC 219332978 has 120-s SPOC data only in sectors 28, 68, 95, 102, 103 and 104
(2020 onward), so the 2018 catalogue epoch has no TESS data. Per the runbook this is recorded and the
target is skipped — it is not a positive-control failure. The injection–recovery completeness for this
target is also low (0–40 % at the reference box), so the screen is only weakly sensitive here.

All 28 persistent events are in sector 103, inside a single ~0.31 d window (BJD 2461174.205 – 2461174.513),
i.e. one episode, not 28 transits. The episode is a clean, flat-bottomed dip:

| Test | Result | State |
|---|---|---|
| Quality flags and gaps | all cadences within ±0.15 d have QUALITY = 0; largest gap 2.0 min | passed |
| SAP vs PDCSAP | flat-bottom profiles agree to ~150 ppm; centre ≈ −4.7 ppt in both | passed |
| Depth vs the catalogue | measured ≈ −4700 ppm against the TOI table's 5180 ppm | consistent |
| Duration vs the catalogue | ≈ 8 h below −2 ppt against the TOI table's 8.48 h | consistent |
| Flux-weighted centroid (MOM_CENTR1/2) | episode residual within the excursion scatter (−0.0005/−0.0014 px vs sd 0.0054/0.0064 px) | inconclusive (no help) |
| Repeat candidate | not set: the positive control did not run, so there is no reference depth to match against | not_tested |
| Difference-image centroids / blend audit | not done | not tested |
| TOI table / literature | TOI table (row updated 2021-10-29) lists no period; ADS and ExoFOP not searched | inconclusive |

The 28 persistent events, one line each — all `tess2026111101500-s0103-…-s_lc.fits`, PDCSAP+SAP at
baselines 1/2/3, BJD and deepest residual:

- 2461174.20504 (−0.00500), 2461174.21754 (−0.00599), 2461174.22448 (−0.00492), 2461174.25643 (−0.00486),
  2461174.26268 (−0.00584), 2461174.26824 (−0.00516), 2461174.27726 (−0.00471), 2461174.28282 (−0.00569),
  2461174.29254 (−0.00629), 2461174.30852 (−0.00556), 2461174.32310 (−0.00492), 2461174.33282 (−0.00578),
  2461174.34116 (−0.00530), 2461174.34602 (−0.00509), 2461174.35227 (−0.00461), 2461174.36199 (−0.00657),
  2461174.38005 (−0.00613), 2461174.38699 (−0.00626), 2461174.39116 (−0.00611), 2461174.39672 (−0.00454),
  2461174.40644 (−0.00483), 2461174.41686 (−0.00515), 2461174.43700 (−0.00465), 2461174.44255 (−0.00504),
  2461174.45783 (−0.00613), 2461174.46200 (−0.00568), 2461174.50089 (−0.00478), 2461174.51339 (−0.00477)
  — all one ~8 h dip.

What this supports: a single clean, transit-shaped ~0.5 % dip in sector 103 of TIC 219332978 (Tmag 10.8)
whose depth and duration match the TOI table's values. What it does not: that it *is* the catalogued
transit — the catalogue epoch is unobservable here, so the two cannot be tied together by this pipeline,
and a single dip gives no period. Next test: the TOI/ExoFOP record for the epoch and period, and a
difference-image check for the sector 103 dip.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2534.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 219332978 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 338.644613 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -57.570425 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458346.575296 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 5180.0 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 8.475 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.8209 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2020212050318-s0028-0000000219332978-0190-s_lc.fits` | 28 | False | `2aaf76777b884e92` | True |
| `tess2023209231226-s0068-0000000219332978-0262-s_lc.fits` | 68 | False | `ee78545d39cfd6ae` | True |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 95 | False | `294fe7a8d94bb5d6` | True |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | 102 | False | `8d1f21a88b612f2d` | True |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 103 | False | `a224c50c46d15a2f` | True |
| `tess2026137223500-s0104-0000000219332978-0306-s_lc.fits` | 104 | False | `dcd2e7e429c4ef9a` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000219332978-0190-s_lc.fits` | — | epoch not in this light curve | — | — | 5180 | — |
| `tess2023209231226-s0068-0000000219332978-0262-s_lc.fits` | — | epoch not in this light curve | — | — | 5180 | — |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | — | epoch not in this light curve | — | — | 5180 | — |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 5180 | — |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | — | epoch not in this light curve | — | — | 5180 | — |
| `tess2026137223500-s0104-0000000219332978-0306-s_lc.fits` | — | epoch not in this light curve | — | — | 5180 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020212050318-s0028-0000000219332978-0190-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023209231226-s0068-0000000219332978-0262-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026137223500-s0104-0000000219332978-0306-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.36199 | -0.00657 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.29254 | -0.00629 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.38699 | -0.00626 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.38005 | -0.00613 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.45783 | -0.00613 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.39116 | -0.00611 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.21754 | -0.00599 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.26268 | -0.00584 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.33282 | -0.00578 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.28282 | -0.00569 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.46200 | -0.00568 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.30852 | -0.00556 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.34116 | -0.00530 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.26824 | -0.00516 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.41686 | -0.00515 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.34602 | -0.00509 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.44255 | -0.00504 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.20504 | -0.00500 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.32310 | -0.00492 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.22448 | -0.00492 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.25643 | -0.00486 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.40644 | -0.00483 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.50089 | -0.00478 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.51339 | -0.00477 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.27726 | -0.00471 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.43700 | -0.00465 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.35227 | -0.00461 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.39672 | -0.00454 | 5 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.39623 | -0.01092 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.51290 | -0.01027 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.38373 | -0.00891 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.48512 | -0.00889 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.60179 | -0.00794 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.02679 | -0.00778 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.57123 | -0.00765 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.39207 | -0.00760 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.26846 | -0.00757 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.64067 | -0.00755 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.44345 | -0.00707 | 4 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.67817 | -0.00695 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.77956 | -0.00683 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460899.76151 | -0.00648 | 4 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.58095 | -0.00638 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.73373 | -0.00626 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.27609 | -0.00618 | 3 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.42123 | -0.00611 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.29484 | -0.00593 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.23373 | -0.00591 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.45526 | -0.00588 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000219332978-0306-s_lc.fits` | 2461197.39128 | -0.00568 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.05526 | -0.00566 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461171.23816 | -0.00543 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461170.62701 | -0.00537 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.36290 | -0.00536 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.30179 | -0.00532 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.65734 | -0.00520 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461170.72424 | -0.00510 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.74970 | -0.00510 | 3 | SAP | 3 | no |
| `tess2023209231226-s0068-0000000219332978-0262-s_lc.fits` | 2460174.81083 | -0.00510 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000219332978-0292-s_lc.fits` | 2460900.24484 | -0.00507 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.24671 | -0.00493 | 2 | PDCSAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000219332978-0306-s_lc.fits` | 2461193.85633 | -0.00478 | 2 | PDCSAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.33699 | -0.00461 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | 2461128.16864 | -0.00442 | 2 | PDCSAP+SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461164.28767 | -0.00439 | 2 | SAP | 1 | no |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | 2461137.50115 | -0.00438 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461170.78396 | -0.00425 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.35783 | -0.00422 | 2 | PDCSAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461170.92008 | -0.00421 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000219332978-0305-s_lc.fits` | 2461174.23837 | -0.00410 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000219332978-0304-s_lc.fits` | 2461137.59560 | -0.00407 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2534.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T02:52:10Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T02:52:12Z: TOI-2534.01 (TIC 219332978, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T02:52:16Z
- SIMBAD (error, 2026-09-25): inconclusive (SIMBAD query failed as of 2026-09-25T02:52:17Z: ProxyError: HTTPSConnectionPool(host='simbad.cds.unistra.fr', port=443): Max retries exceeded with url: /simbad/sim-tap/sync (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: )

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3, 3, ≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 40%, 20%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | inconclusive | 1 target(s) × 4 services, radius 30″; 3 answered, 1 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2534-01.yaml
python -m cygnus.campaign report campaigns/toi-2534-01.yaml
```
