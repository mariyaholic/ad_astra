<!-- [private Drive store] -->
# Known-object test, TOI-3312.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3312-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1074, calibrate_screen #1023, event_census #1031, fetch_products #1022, known_signal_recovery #1024, moving_objects #1033, period_aliases #1032, prior_art #1076, residual_screen #1026, stellar_context #1025, variability_guard #1075
- Runner finished (UTC): 2026-09-26T10:32:53Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 658 threshold entries forming **144 distinct event(s)**, **66 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3312.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 332314607 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 272.905634 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -36.782023 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458672.498932 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 29490.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.794 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.5578 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | lightcurve | 66 | False | `adc89c53058e7bdc` | True |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | lightcurve | 93 | False | `14cfe2fec06ee2a4` | True |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | lightcurve | 104 | False | `8bd6de3111fb4141` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 29490 | — |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | — | epoch not in this light curve | — | — | 29490 | — |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | — | epoch not in this light curve | — | — | 29490 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.83898 | -0.05748 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.18565 | -0.05653 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.42558 | -0.05554 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.64591 | -0.05341 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.80842 | -0.05299 | 30 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.85079 | -0.05283 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.66536 | -0.05264 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.21412 | -0.05172 | 30 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.18010 | -0.05054 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.63410 | -0.04999 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.59660 | -0.04997 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.65494 | -0.04962 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.83204 | -0.04890 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.16899 | -0.04855 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.68272 | -0.04794 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.37836 | -0.04746 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.61605 | -0.04730 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.35822 | -0.04667 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.85843 | -0.04491 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.78342 | -0.04462 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.69363 | -0.04370 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460106.73174 | -0.04314 | 21 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.25093 | -0.04278 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.23843 | -0.04243 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461179.60216 | -0.04148 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.77280 | -0.04132 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.16412 | -0.04108 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.33180 | -0.04058 | 15 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.53996 | -0.03952 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.75127 | -0.03932 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.30819 | -0.03922 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.94631 | -0.03905 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.70057 | -0.03878 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460106.68035 | -0.03859 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.31583 | -0.03854 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.29342 | -0.03802 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.72766 | -0.03766 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.27953 | -0.03765 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460117.51869 | -0.03724 | 45 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.93103 | -0.03691 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.30333 | -0.03662 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.97062 | -0.03662 | 21 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.27120 | -0.03658 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.36305 | -0.03610 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460117.43466 | -0.03604 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.91298 | -0.03593 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.58440 | -0.03590 | 15 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.54829 | -0.03536 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.32398 | -0.03513 | 33 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.35176 | -0.03477 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.56982 | -0.03461 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.77974 | -0.03400 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.70682 | -0.03387 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.91992 | -0.03379 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.55940 | -0.03359 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.39014 | -0.03343 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460850.76516 | -0.03317 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.51635 | -0.03274 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460106.64424 | -0.03267 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.59760 | -0.03240 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.53024 | -0.03184 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460106.73799 | -0.03021 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460106.75119 | -0.02971 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.90187 | -0.02917 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.41166 | -0.02774 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460834.50037 | -0.02693 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.19051 | -0.05430 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461201.17454 | -0.04385 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461185.08300 | -0.04019 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461185.09134 | -0.03791 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460117.53466 | -0.03193 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.26634 | -0.03073 | 2 | PDCSAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460106.64980 | -0.03068 | 2 | PDCSAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460117.52355 | -0.03039 | 2 | PDCSAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460840.00603 | -0.03023 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.89076 | -0.03017 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460839.98937 | -0.02995 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460101.36217 | -0.02837 | 2 | PDCSAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460845.29708 | -0.02721 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460840.00048 | -0.02705 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.04991 | -0.01784 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460849.73391 | -0.01780 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460849.77558 | -0.01759 | 4 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.51934 | -0.01590 | 5 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.04019 | -0.01573 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.38461 | -0.01567 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.99435 | -0.01509 | 4 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.84851 | -0.01499 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.00130 | -0.01483 | 4 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.76101 | -0.01480 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.07352 | -0.01460 | 4 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.11658 | -0.01447 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.28322 | -0.01417 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.92004 | -0.01402 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.57420 | -0.01374 | 3 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.77768 | -0.01368 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460849.84224 | -0.01362 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.48392 | -0.01351 | 5 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.83879 | -0.01345 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.60128 | -0.01343 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.79712 | -0.01334 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.98741 | -0.01329 | 4 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.57906 | -0.01328 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.79712 | -0.01326 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.10408 | -0.01302 | 4 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.74017 | -0.01291 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.63323 | -0.01279 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.94018 | -0.01279 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.74504 | -0.01265 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.86796 | -0.01244 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.49503 | -0.01239 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.79156 | -0.01235 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460836.56848 | -0.01235 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.36725 | -0.01228 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.06102 | -0.01224 | 8 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.86310 | -0.01219 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.49017 | -0.01218 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.63045 | -0.01212 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.70268 | -0.01211 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.71587 | -0.01202 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.09019 | -0.01202 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.66240 | -0.01200 | 4 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.88601 | -0.01188 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.73184 | -0.01183 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.49989 | -0.01164 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460118.79161 | -0.01160 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461191.03394 | -0.01157 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.80407 | -0.01154 | 4 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.77004 | -0.01149 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.60962 | -0.01143 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460836.57264 | -0.01143 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.95546 | -0.01133 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.92629 | -0.01128 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.70823 | -0.01126 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460836.54973 | -0.01123 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461190.60545 | -0.01123 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460118.49716 | -0.01110 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.68601 | -0.01062 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.64364 | -0.01047 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460117.75827 | -0.01024 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000332314607-0290-s_lc.fits` | 2460849.73946 | -0.01024 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000332314607-0260-s_lc.fits` | 2460111.72351 | -0.01014 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461195.77370 | -0.01001 | 2 | SAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000332314607-0306-s_lc.fits` | 2461203.06138 | -0.00986 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3312.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:32:50Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:32:51Z: TOI-3312.01 (TIC 332314607, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:32:52Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T10:32:53Z: Gaia DR3 4037914121810087552 (*); TOI-3312 (**); TOI-3312.01 (Pl?); Gaia DR3 4037914126188971008 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | not_tested | TOI-3312.01: gaia unavailable: Gaia TAP failed: HTTPError: 400 Client Error: 400 for url: https://gea.esac.esa.int/tap-server/tap/sync |
| Stellar priors (Gaia colour and parallax) | not_tested | TOI-3312.01: gaia unavailable: Gaia TAP failed: HTTPError: 400 Client Error: 400 for url: https://gea.esac.esa.int/tap-server/tap/sync |
| Blend and dilution census (Gaia DR3 cone) | not_tested | TOI-3312.01: gaia unavailable: Gaia TAP failed: HTTPError: 400 Client Error: 400 for url: https://gea.esac.esa.int/tap-server/tap/sync |
| Pointing and quality census per event | failed | 66 persistent event(s), 42 clean; BJD 2460101.3240 suspect: MOM_CENTR1 z=+5.3; BJD 2460101.3518 suspect: MOM_CENTR1 z=+6.5; BJD 2460106.6442 caution: manual exclude (within ±0.25 d); BJD 2460106.6804 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 66 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 10 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3312.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3312.01: TOI-3312.01 otype Pl? (star_or_other) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3312-01.yaml
python -m cygnus.multi report campaigns/toi-3312-01.yaml
```
