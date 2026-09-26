<!-- cygnus:generated-draft -->
# Known-object test, TOI-340.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-340-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #205, calibrate_screen #156, event_census #176, fetch_products #150, known_signal_recovery #159, moving_objects #178, period_aliases #177, prior_art #207, residual_screen #169, stellar_context #160, variability_guard #206
- Runner finished (UTC): 2026-09-26T09:56:57Z

## Bottom line

Positive control **failed**: BJD 2459088.6955: not recovered, depth 6414 ± 1930 ppm (catalogue 53559 ppm).
Outside the catalogued epoch the screen left 433 threshold entries forming **164 distinct event(s)**, **32 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-340.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 80439101 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 11.747329 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -44.369951 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459088.695472 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 53558.5635109 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.9888165 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.6435 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-03-14 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | lightcurve | 29 | True | `26e20f11c98f9cb9` | True |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | lightcurve | 69 | False | `f473029f64c10f52` | True |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | lightcurve | 96 | False | `623074fb7a3dbfa1` | True |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | lightcurve | 104 | False | `9a0364c4379a4d0c` | True |
| `tess2026164183000-s0105-0000000080439101-0307-s_lc.fits` | lightcurve | 105 | False | `62f38dde313d35d8` | True |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | lightcurve | 106 | False | `09c64a2ea1dc3839` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459088.69547 | not_recovered | 178 | 6414 ± 1930 | 53559 | — |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | — | epoch not in this light curve | — | — | 53559 | — |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 53559 | — |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | — | epoch not in this light curve | — | — | 53559 | — |
| `tess2026164183000-s0105-0000000080439101-0307-s_lc.fits` | — | epoch not in this light curve | — | — | 53559 | — |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | — | epoch not in this light curve | — | — | 53559 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026164183000-s0105-0000000080439101-0307-s_lc.fits` | 7 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.47194 | -0.08813 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.45944 | -0.08616 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.41639 | -0.08125 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460187.57745 | -0.07716 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460200.64140 | -0.07371 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460930.08507 | -0.06156 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.55591 | -0.05834 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460915.22247 | -0.05719 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.40345 | -0.05659 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.49479 | -0.05524 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461198.62506 | -0.05499 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.58369 | -0.05484 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.54271 | -0.05461 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.52257 | -0.05457 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.57535 | -0.05445 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.50104 | -0.05389 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.59271 | -0.05302 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.50799 | -0.05204 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.59896 | -0.05195 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.39234 | -0.05194 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.56702 | -0.05043 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.42776 | -0.05023 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.52951 | -0.05010 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.37636 | -0.04973 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.42220 | -0.04970 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.36386 | -0.04826 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.47673 | -0.04615 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461200.85717 | -0.04562 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.43539 | -0.04473 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.38261 | -0.04463 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.33469 | -0.04421 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.34580 | -0.04420 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.57100 | -0.10447 | 2 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.24973 | -0.09585 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.52655 | -0.09384 | 2 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.64322 | -0.09347 | 2 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.68211 | -0.09330 | 2 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.26084 | -0.09276 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.69183 | -0.09137 | 2 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.84482 | -0.09098 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.55989 | -0.09092 | 2 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459103.54884 | -0.08962 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.70433 | -0.08742 | 6 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.62239 | -0.08658 | 2 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.58350 | -0.08530 | 4 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.02890 | -0.08368 | 2 | PDCSAP | 1, 2 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.99877 | -0.08348 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.81080 | -0.08285 | 2 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.64274 | -0.08154 | 2 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.94738 | -0.08124 | 2 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.14417 | -0.07988 | 2 | PDCSAP | 1 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.76683 | -0.07944 | 2 | PDCSAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.67308 | -0.07824 | 3 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460187.60245 | -0.07705 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.60385 | -0.07661 | 2 | PDCSAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459111.73419 | -0.07644 | 3 | PDCSAP | 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461241.94592 | -0.07259 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461256.76190 | -0.07257 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.62746 | -0.07204 | 2 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.83302 | -0.07145 | 2 | PDCSAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.70663 | -0.07060 | 2 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.87538 | -0.06978 | 3 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.86982 | -0.06937 | 3 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460205.91357 | -0.06935 | 2 | PDCSAP | 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461241.91119 | -0.06819 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461241.97370 | -0.06721 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461256.80079 | -0.06502 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461235.55943 | -0.06471 | 2 | PDCSAP | 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461241.95425 | -0.06424 | 2 | PDCSAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460930.09896 | -0.06314 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026192185000-s0106-0000000080439101-0308-s_lc.fits` | 2461256.78690 | -0.05697 | 2 | PDCSAP | 1, 2 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460930.12813 | -0.05658 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460915.31136 | -0.05327 | 2 | PDCSAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.51493 | -0.05026 | 3 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.48646 | -0.04573 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.60313 | -0.04241 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461182.47257 | -0.04214 | 2 | PDCSAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.35900 | -0.03752 | 5 | SAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.36689 | -0.03698 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.41109 | -0.03348 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.46635 | -0.03297 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.35136 | -0.03238 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.31664 | -0.02908 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000080439101-0306-s_lc.fits` | 2461197.33886 | -0.02860 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.37731 | -0.02793 | 3 | SAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.41134 | -0.02779 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.74972 | -0.02767 | 4 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.74139 | -0.02740 | 4 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460927.15035 | -0.02726 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.46218 | -0.02709 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.41773 | -0.02680 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460927.11007 | -0.02664 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.45524 | -0.02650 | 6 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.75945 | -0.02640 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.73445 | -0.02626 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.49551 | -0.02575 | 38 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.41287 | -0.02566 | 3 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.42333 | -0.02547 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.38356 | -0.02535 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.54065 | -0.02531 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.77959 | -0.02524 | 3 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.75528 | -0.02520 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.38722 | -0.02499 | 4 | SAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.34051 | -0.02487 | 14 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.79903 | -0.02444 | 23 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.42815 | -0.02444 | 9 | SAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.39467 | -0.02441 | 2 | SAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.37106 | -0.02433 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.43305 | -0.02414 | 6 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.53579 | -0.02412 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.94695 | -0.02376 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.52815 | -0.02368 | 7 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.82125 | -0.02357 | 7 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.99833 | -0.02353 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.54760 | -0.02338 | 5 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.62329 | -0.02335 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.44065 | -0.02332 | 3 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.90875 | -0.02326 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460182.52875 | -0.02322 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460927.09479 | -0.02314 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460182.55792 | -0.02305 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.58371 | -0.02304 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.44000 | -0.02295 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.57607 | -0.02290 | 4 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.50111 | -0.02279 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.38166 | -0.02268 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.86083 | -0.02265 | 24 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.90181 | -0.02252 | 5 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460182.39958 | -0.02249 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460182.67598 | -0.02229 | 2 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460182.61209 | -0.02214 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000080439101-0293-s_lc.fits` | 2460930.05590 | -0.02211 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.91917 | -0.02211 | 4 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.77472 | -0.02192 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.70107 | -0.02180 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.51222 | -0.02174 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.56565 | -0.02168 | 9 | SAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.96083 | -0.02158 | 4 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.55385 | -0.02157 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.63926 | -0.02149 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.76500 | -0.02130 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.62954 | -0.02124 | 5 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.09972 | -0.02116 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.00875 | -0.02116 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460182.63570 | -0.02103 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.68510 | -0.02100 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.44416 | -0.02092 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.99417 | -0.02072 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.42106 | -0.02070 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.95181 | -0.02049 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.61565 | -0.02035 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.93792 | -0.02034 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.83167 | -0.02021 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.98444 | -0.02014 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460201.96847 | -0.02014 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.50805 | -0.02004 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460188.60524 | -0.02000 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.40458 | -0.01993 | 5 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.47819 | -0.01961 | 5 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.44902 | -0.01951 | 3 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000080439101-0264-s_lc.fits` | 2460202.24417 | -0.01931 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.47384 | -0.01759 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.45301 | -0.01724 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000080439101-0193-s_lc.fits` | 2459102.38773 | -0.01641 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-340.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:56:53Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:56:54Z: TOI-340.01 (TIC 80439101, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:56:55Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T09:56:56Z: TOI-340 (*); TOI-340.01 (Pl?); TYC 7538-319-1 (Pe*); Gaia DR3 4979568766402993152 (WD?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459088.6955: not recovered, depth 6414 ± 1930 ppm (catalogue 53559 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 4, 3.5, 7, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-340.01: Gaia DR3 4979568766404541696 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-340.01: dwarf priors not applied — parallax/error 3.9 < 5; RUWE 16.729807 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-340.01: 4 Gaia neighbour(s) within 52.5", contamination 88.55%; depth 53559 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 4979569144361074560, 21.5", ΔG -2.22); a centroid test is needed |
| Pointing and quality census per event | failed | 32 persistent event(s), 3 clean; BJD 2460187.5774 suspect: MOM_CENTR2 z=-8.1; BJD 2460200.6414 suspect: manual exclude (within ±0.25 d), MOM_CENTR1 z=+5.6; BJD 2460202.4164 suspect: MOM_CENTR2 z=-10.8; BJD 2460202.4594 suspect: MOM_CENTR2 z=-10.0 |
| Moving objects at screen-event epochs | inconclusive | 32 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 7 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-340.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-340.01: TOI-340 otype * (star_or_other) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-340-01.yaml
python -m cygnus.multi report campaigns/toi-340-01.yaml
```
