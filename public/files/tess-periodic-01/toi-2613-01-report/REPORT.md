<!-- [private Drive store] -->
# Known-object test, TOI-2613.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2613-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #681, calibrate_screen #527, event_census #555, fetch_products #523, known_signal_recovery #536, moving_objects #620, period_aliases #557, prior_art #684, residual_screen #550, stellar_context #537, variability_guard #682
- Runner finished (UTC): 2026-09-26T10:13:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2613.01 (BJD 2460155.2182: recovered, depth 30286 ± 417 ppm (catalogue 35221 ppm)).
Outside the catalogued epoch the screen left 374 threshold entries forming **52 distinct event(s)**, **46 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460170.2953 matches the catalogued transit's depth (16674 vs 30286 ppm), 15.030 d later; 0 of 15 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2613.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 52315301 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 22.910564 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -67.609909 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460155.218217 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 35221.1348039 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 8.2467072 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.1488 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-17 12:03:25 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | lightcurve | 68 | True | `a3d920f4679672d2` | True |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | lightcurve | 69 | False | `f1f96a5a93f7cc44` | True |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | lightcurve | 95 | False | `c30dbba039f1966c` | True |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | lightcurve | 96 | False | `4c660fe8e8ce3b65` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460155.21822 | recovered | 247 | 30286 ± 417 | 35221 | 1.13 |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | — | epoch not in this light curve | — | — | 35221 | — |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | — | epoch not in this light curve | — | — | 35221 | — |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 35221 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.77630 | -0.03802 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460900.13198 | -0.03568 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.58204 | -0.03490 | 129 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460170.50985 | -0.03399 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.73672 | -0.03357 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.51164 | -0.03319 | 153 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460884.87420 | -0.03267 | 75 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.84019 | -0.03248 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460900.05768 | -0.03243 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460915.29377 | -0.03237 | 175 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460884.96656 | -0.03221 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460170.45290 | -0.03217 | 80 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460170.36818 | -0.03211 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460900.17018 | -0.03129 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.52857 | -0.03102 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.51190 | -0.03031 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460884.77697 | -0.03023 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.89435 | -0.02997 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.39776 | -0.02907 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460884.80475 | -0.02897 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.92491 | -0.02884 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.69783 | -0.02829 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460170.29526 | -0.02748 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460900.21045 | -0.02722 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460900.19170 | -0.02674 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460170.52860 | -0.02632 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.37067 | -0.02619 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.37762 | -0.02566 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.72649 | -0.02511 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000052315301-0262-s_lc.fits` | 2460170.54040 | -0.02510 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.74801 | -0.02497 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.50427 | -0.02428 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460915.44030 | -0.02414 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.73204 | -0.02410 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.73829 | -0.02382 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460915.42085 | -0.02378 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460885.01100 | -0.02345 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.93879 | -0.02303 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.38526 | -0.02276 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460899.97504 | -0.02158 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.71033 | -0.02152 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.63039 | -0.02114 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000052315301-0292-s_lc.fits` | 2460884.76517 | -0.02081 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460930.62275 | -0.02072 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460915.43057 | -0.01814 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460925.77630 | -0.01765 | 2 | PDCSAP+SAP | 1, 3 | yes |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.94921 | -0.02347 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.94366 | -0.02309 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460185.49246 | -0.02126 | 2 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.69366 | -0.02014 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000052315301-0264-s_lc.fits` | 2460200.70477 | -0.01976 | 3 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000052315301-0293-s_lc.fits` | 2460927.07073 | -0.01479 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460170.29526 | 16674 | 30286 | 15.0300 | 0 / 15 |  |
| 2460170.36818 | 28466 | 30286 | 15.1029 | 0 / 15 |  |
| 2460170.45290 | 28466 | 30286 | 15.1876 | 0 / 15 |  |
| 2460170.50985 | 26202 | 30286 | 15.2446 | 0 / 15 |  |
| 2460170.52860 | 22355 | 30286 | 15.2633 | 0 / 15 |  |
| 2460170.54040 | 18659 | 30286 | 15.2751 | 0 / 15 |  |
| 2460185.50427 | 21993 | 30286 | 30.2390 | 0 / 30 |  |
| 2460185.51190 | 22710 | 30286 | 30.2466 | 0 / 30 |  |
| 2460185.52857 | 26019 | 30286 | 30.2633 | 0 / 30 |  |
| 2460185.58204 | 27883 | 30286 | 30.3168 | 0 / 30 |  |
| 2460185.72649 | 22690 | 30286 | 30.4612 | 0 / 30 |  |
| 2460185.73204 | 22007 | 30286 | 30.4668 | 0 / 30 |  |
| 2460185.73829 | 19838 | 30286 | 30.4730 | 0 / 30 |  |
| 2460200.69783 | 15768 | 30286 | 45.4326 | 0 / 45 |  |
| 2460200.71033 | 19117 | 30286 | 45.4451 | 0 / 45 |  |
| 2460200.73672 | 23101 | 30286 | 45.4715 | 0 / 45 |  |
| 2460200.77630 | 24901 | 30286 | 45.5110 | 0 / 45 |  |
| 2460200.84019 | 24945 | 30286 | 45.5749 | 0 / 45 |  |
| 2460200.89435 | 24236 | 30286 | 45.6291 | 0 / 45 |  |
| 2460200.92491 | 21834 | 30286 | 45.6596 | 0 / 45 |  |
| 2460200.93879 | 19362 | 30286 | 45.6735 | 0 / 45 |  |
| 2460884.76517 | 15984 | 30286 | 729.4999 | 17 / 729 | 729.5, 364.75, 243.167, 182.375, 145.9, 121.583, 104.214, 91.1875, 81.0555, 72.95, 66.3182, 60.7917, 56.1154, 52.1071, 45.5937, 30.3958, 15.1979 |
| 2460884.77697 | 20954 | 30286 | 729.5117 | 17 / 729 | 729.512, 364.756, 243.171, 182.378, 145.902, 121.585, 104.216, 91.189, 81.0569, 72.9512, 66.3192, 60.7926, 56.1163, 52.108, 45.5945, 30.3963, 15.1982 |
| 2460884.80475 | 26161 | 30286 | 729.5395 | 17 / 729 | 729.539, 364.77, 243.18, 182.385, 145.908, 121.59, 104.22, 91.1924, 81.0599, 72.9539, 66.3218, 60.795, 56.1184, 52.11, 45.5962, 30.3975, 15.1987 |
| 2460884.87420 | 27258 | 30286 | 729.6089 | 17 / 729 | 729.609, 364.805, 243.203, 182.402, 145.922, 121.602, 104.23, 91.2011, 81.0677, 72.9609, 66.3281, 60.8007, 56.1238, 52.1149, 45.6006, 30.4004, 15.2002 |
| 2460884.96656 | 26239 | 30286 | 729.7013 | 17 / 729 | 729.701, 364.851, 243.234, 182.425, 145.94, 121.617, 104.243, 91.2127, 81.0779, 72.9701, 66.3365, 60.8084, 56.1309, 52.1215, 45.6063, 30.4042, 15.2021 |
| 2460885.01100 | 21393 | 30286 | 729.7457 | 17 / 729 | 729.746, 364.873, 243.249, 182.436, 145.949, 121.624, 104.249, 91.2182, 81.0829, 72.9746, 66.3405, 60.8121, 56.1343, 52.1247, 45.6091, 30.4061, 15.203 |
| 2460899.97504 | 19125 | 30286 | 744.7098 | 16 / 744 | 744.71, 372.355, 248.237, 186.177, 148.942, 124.118, 106.387, 93.0887, 82.7455, 74.471, 67.7009, 62.0591, 57.2854, 53.1936, 39.1953, 15.1982 |
| 2460900.05768 | 26143 | 30286 | 744.7924 | 16 / 744 | 744.792, 372.396, 248.264, 186.198, 148.958, 124.132, 106.399, 93.0991, 82.7547, 74.4792, 67.7084, 62.066, 57.2917, 53.1995, 39.1996, 15.1998 |
| 2460900.13198 | 26895 | 30286 | 744.8667 | 16 / 744 | 744.867, 372.433, 248.289, 186.217, 148.973, 124.144, 106.409, 93.1083, 82.763, 74.4867, 67.7152, 62.0722, 57.2974, 53.2048, 39.2035, 15.2014 |
| 2460900.17018 | 26143 | 30286 | 744.9049 | 16 / 744 | 744.905, 372.452, 248.302, 186.226, 148.981, 124.151, 106.415, 93.1131, 82.7672, 74.4905, 67.7186, 62.0754, 57.3004, 53.2075, 39.2055, 15.2021 |
| 2460900.19170 | 25280 | 30286 | 744.9264 | 16 / 744 | 744.926, 372.463, 248.309, 186.232, 148.985, 124.154, 106.418, 93.1158, 82.7696, 74.4926, 67.7206, 62.0772, 57.302, 53.209, 39.2067, 15.2026 |
| 2460900.21045 | 22237 | 30286 | 744.9452 | 16 / 744 | 744.945, 372.473, 248.315, 186.236, 148.989, 124.157, 106.421, 93.1181, 82.7717, 74.4945, 67.7223, 62.0788, 57.3035, 53.2104, 39.2076, 15.203 |
| 2460915.29377 | 27846 | 30286 | 760.0285 | 19 / 760 | 760.029, 380.014, 253.343, 190.007, 152.006, 126.671, 108.576, 95.0036, 84.4476, 76.0029, 69.0935, 63.3357, 58.4637, 54.2878, 40.0015, 38.0014, 33.0447, 30.4011, 15.2006 |
| 2460915.42085 | 19578 | 30286 | 760.1556 | 20 / 760 | 760.156, 380.078, 253.385, 190.039, 152.031, 126.693, 108.594, 95.0194, 84.4617, 76.0156, 69.1051, 63.3463, 58.4735, 54.2968, 40.0082, 38.0078, 33.0502, 30.4062, 27.1484, 15.2031 |
| 2460915.43057 | 16936 | 30286 | 760.1653 | 20 / 760 | 760.165, 380.083, 253.388, 190.041, 152.033, 126.694, 108.595, 95.0207, 84.4628, 76.0165, 69.1059, 63.3471, 58.4743, 54.2975, 40.0087, 38.0083, 33.0507, 30.4066, 27.1488, 15.2033 |
| 2460930.37762 | 18375 | 30286 | 775.1124 | 17 / 775 | 775.112, 387.556, 258.371, 193.778, 155.023, 129.185, 110.73, 96.889, 86.1236, 77.5112, 70.4648, 64.5927, 59.624, 55.3652, 51.6742, 45.5948, 15.1983 |
| 2460930.38526 | 20260 | 30286 | 775.1200 | 17 / 775 | 775.12, 387.56, 258.373, 193.78, 155.024, 129.187, 110.731, 96.89, 86.1244, 77.512, 70.4655, 64.5933, 59.6246, 55.3657, 51.6747, 45.5953, 15.1984 |
| 2460930.39776 | 23366 | 30286 | 775.1325 | 17 / 775 | 775.133, 387.566, 258.377, 193.783, 155.026, 129.189, 110.733, 96.8916, 86.1258, 77.5132, 70.4666, 64.5944, 59.6256, 55.3666, 51.6755, 45.596, 15.1987 |
| 2460930.51164 | 28455 | 30286 | 775.2464 | 17 / 775 | 775.246, 387.623, 258.416, 193.812, 155.049, 129.208, 110.749, 96.9058, 86.1385, 77.5246, 70.4769, 64.6039, 59.6343, 55.3747, 51.6831, 45.6027, 15.2009 |
| 2460930.62275 | 19610 | 30286 | 775.3575 | 17 / 775 | 775.357, 387.679, 258.452, 193.839, 155.071, 129.226, 110.765, 96.9197, 86.1508, 77.5357, 70.487, 64.6131, 59.6429, 55.3827, 51.6905, 45.6093, 15.2031 |
| 2460930.63039 | 17118 | 30286 | 775.3651 | 17 / 775 | 775.365, 387.683, 258.455, 193.841, 155.073, 129.227, 110.766, 96.9206, 86.1517, 77.5365, 70.4877, 64.6138, 59.6435, 55.3832, 51.691, 45.6097, 15.2032 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2613.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:13:21Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:13:22Z: TOI-2613.01 (TIC 52315301, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:13:23Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:13:23Z: TOI-2613 (*); TOI-2613.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460155.2182: recovered, depth 30286 ± 417 ppm (catalogue 35221 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 42 repeat-candidate event(s); first at BJD 2460170.2953, ΔT = 15.030 d, 0 of 15 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2613.01: Gaia DR3 4692442574804865152 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2613.01: Teff 5998 K, R* 1.10 ± 0.09, M* 1.06 ± 0.11, ρ* 0.80 ± 0.21 ρ☉ (dwarf sequence, M_G 4.33, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2613.01: 1 Gaia neighbour(s) within 52.5", contamination 18.04%; depth 30286 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4692441818890647168, 17.7", ΔG 1.64); a centroid test is needed |
| Pointing and quality census per event | failed | 46 persistent event(s), 25 clean; BJD 2460170.3682 suspect: MOM_CENTR1 z=+6.0; BJD 2460185.5820 suspect: MOM_CENTR2 z=+5.6; BJD 2460200.6978 suspect: manual exclude (in event); BJD 2460200.7103 suspect: manual exclude (in event) |
| Moving objects at screen-event epochs | inconclusive | 46 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-2613.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2613.01: TOI-2613 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2613-01.yaml
python -m cygnus.multi report campaigns/toi-2613-01.yaml
```
