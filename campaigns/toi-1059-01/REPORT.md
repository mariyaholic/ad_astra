<!-- cygnus:generated-draft -->
# Known-object test, TOI-1059.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1059-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #267, calibrate_screen #130, event_census #139, fetch_products #127, known_signal_recovery #133, moving_objects #247, period_aliases #140, prior_art #271, residual_screen #137, stellar_context #134, variability_guard #268
- Runner finished (UTC): 2026-09-26T09:59:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1059.01 (BJD 2460852.8607: recovered, depth 14424 ± 170 ppm (catalogue 25388 ppm)).
Outside the catalogued epoch the screen left 318 threshold entries forming **128 distinct event(s)**, **23 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460833.9619 matches the catalogued transit's depth (13788 vs 14424 ppm), 18.899 d later; 2 of 18 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1059.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 380783252 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 269.714503 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -60.922727 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460852.860658 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 25387.7438512 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.2611055 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.7825 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-08-13 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | lightcurve | 93 | True | `3b23c0ed26f2eb36` | True |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | lightcurve | 13 | False | `3f782ee268dc0aed` | True |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | lightcurve | 39 | False | `e1d50e0d083f04dc` | True |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | lightcurve | 66 | False | `f0c6ee502cc24a34` | True |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | lightcurve | 100 | False | `8d74d8a6dbf8a84f` | True |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | lightcurve | 102 | False | `9583e4c47c719e57` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460852.86066 | recovered | 68 | 14424 ± 170 | 25388 | 0.01 |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | — | epoch not in this light curve | — | — | 25388 | — |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | — | epoch not in this light curve | — | — | 25388 | — |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 25388 | — |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 25388 | — |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 25388 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 3 | False | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 6 | False | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461145.80641 | -0.02176 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461136.34945 | -0.02110 | 47 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458679.44015 | -0.02002 | 44 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461089.10212 | -0.01968 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461098.55210 | -0.01959 | 49 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461079.65223 | -0.01942 | 45 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459388.15824 | -0.01928 | 41 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458669.98759 | -0.01894 | 48 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458660.54187 | -0.01894 | 41 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460106.33702 | -0.01839 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460833.96191 | -0.01834 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460115.78711 | -0.01808 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459378.71445 | -0.01804 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459369.26637 | -0.01766 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461145.77654 | -0.01249 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461145.82724 | -0.01076 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459388.19296 | -0.00999 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458682.09909 | -0.00806 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.74612 | -0.00804 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460849.77453 | -0.00746 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459388.20060 | -0.00693 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.77598 | -0.00682 | 3 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.76973 | -0.00587 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461132.94503 | -0.01193 | 9 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461132.97073 | -0.01179 | 19 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461132.92698 | -0.01063 | 9 | PDCSAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.02452 | -0.01056 | 2 | PDCSAP+SAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458669.04664 | -0.00981 | 2 | PDCSAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458668.91192 | -0.00940 | 2 | PDCSAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458668.96470 | -0.00877 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461093.89274 | -0.00870 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461140.38238 | -0.00867 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.11340 | -0.00858 | 2 | PDCSAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458668.92303 | -0.00847 | 2 | PDCSAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458668.90359 | -0.00844 | 2 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.73005 | -0.00834 | 102 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458668.87720 | -0.00830 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461093.85107 | -0.00811 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 2461136.31542 | -0.00807 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458668.78831 | -0.00788 | 2 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.58353 | -0.00784 | 9 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458682.11993 | -0.00767 | 2 | PDCSAP+SAP | 1 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.54464 | -0.00764 | 3 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458660.57312 | -0.00732 | 2 | PDCSAP | 1, 2 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460849.73287 | -0.00727 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.03702 | -0.00718 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.78778 | -0.00715 | 2 | PDCSAP | 1, 2 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.36757 | -0.00710 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.57380 | -0.00701 | 3 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.19813 | -0.00695 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461079.68626 | -0.00689 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.26340 | -0.00681 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.56616 | -0.00680 | 6 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.51894 | -0.00678 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.41269 | -0.00658 | 3 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.55783 | -0.00656 | 4 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460836.54668 | -0.00648 | 2 | PDCSAP | 1, 2 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.73675 | -0.00639 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.34535 | -0.00637 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.55089 | -0.00636 | 4 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.25090 | -0.00636 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.68536 | -0.00636 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.49464 | -0.00629 | 7 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.45505 | -0.00624 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.05507 | -0.00618 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.53144 | -0.00618 | 14 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.50852 | -0.00618 | 11 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460836.57168 | -0.00617 | 2 | PDCSAP | 1, 2 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458658.55507 | -0.00616 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.21061 | -0.00615 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 2458657.85507 | -0.00613 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.34811 | -0.00609 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.72008 | -0.00609 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.90759 | -0.00606 | 4 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461093.87469 | -0.00605 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.42172 | -0.00603 | 6 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461079.61820 | -0.00602 | 2 | PDCSAP | 1 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.99371 | -0.00602 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.44811 | -0.00601 | 6 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.98538 | -0.00600 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.35644 | -0.00600 | 4 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.84370 | -0.00596 | 4 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461093.67328 | -0.00595 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461088.04649 | -0.00587 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.48700 | -0.00586 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.47102 | -0.00586 | 19 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460836.55501 | -0.00585 | 2 | PDCSAP | 1 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.86454 | -0.00576 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.86870 | -0.00575 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.88259 | -0.00574 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.79161 | -0.00573 | 5 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.43144 | -0.00565 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.08838 | -0.00564 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.39602 | -0.00559 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.33561 | -0.00556 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461093.82885 | -0.00553 | 4 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.74369 | -0.00550 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461087.89093 | -0.00549 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460836.56196 | -0.00547 | 2 | PDCSAP | 1 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.37658 | -0.00546 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.26061 | -0.00543 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 2461088.05622 | -0.00538 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460852.16202 | -0.00535 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.27033 | -0.00521 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.43908 | -0.00521 | 5 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.40158 | -0.00515 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.38630 | -0.00510 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.20575 | -0.00505 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460843.70229 | -0.00501 | 2 | PDCSAP | 1 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.26616 | -0.00495 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.32311 | -0.00493 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.38144 | -0.00488 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.36339 | -0.00475 | 2 | SAP | 3 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459374.61718 | -0.00472 | 2 | SAP | 3 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459374.58801 | -0.00456 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460836.56751 | -0.00455 | 2 | PDCSAP | 1 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460841.28144 | -0.00454 | 2 | SAP | 3 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459380.24085 | -0.00453 | 2 | SAP | 1, 2 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459374.64357 | -0.00452 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.72389 | -0.00441 | 2 | SAP | 1, 2 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459365.83087 | -0.00440 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460843.55854 | -0.00431 | 3 | PDCSAP | 1 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459374.81301 | -0.00425 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.68500 | -0.00418 | 2 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 2460111.74195 | -0.00414 | 2 | SAP | 1, 2 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460854.60366 | -0.00408 | 2 | SAP | 1 | no |
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 2460854.58699 | -0.00394 | 2 | SAP | 1 | no |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 2459386.84504 | -0.00372 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460833.96191 | 13788 | 14424 | 18.8991 | 2 / 18 | 18.8991, 9.4495 |
| 2458660.54187 | 12395 | 14424 | 2192.3191 | 20 / 2192 | 2192.32, 1096.16, 548.08, 438.464, 313.188, 274.04, 219.232, 199.302, 168.64, 156.594, 137.02, 128.96, 109.616, 99.6509, 95.3182, 84.32, 75.5972, 37.7986, 18.8993, 9.4497 |
| 2458669.98759 | 12454 | 14424 | 2182.8734 | 24 / 2182 | 2182.87, 1091.44, 727.625, 545.718, 436.575, 363.812, 311.839, 272.859, 218.287, 198.443, 181.906, 167.913, 155.919, 136.43, 128.404, 109.144, 103.946, 90.9531, 83.9567, 66.1477 |
| 2458679.44015 | 13045 | 14424 | 2173.4208 | 25 / 2173 | 2173.42, 1086.71, 724.474, 543.355, 434.684, 362.237, 310.489, 271.678, 217.342, 197.584, 181.118, 167.186, 155.244, 135.839, 127.848, 108.671, 103.496, 94.4966, 90.5592, 86.9368 |
| 2459369.26637 | 14368 | 14424 | 1483.5946 | 16 / 1483 | 1483.59, 741.797, 494.531, 370.899, 247.266, 211.942, 185.449, 164.844, 134.872, 123.633, 105.971, 82.4219, 67.4361, 61.8164, 51.1584, 9.4496 |
| 2459378.71445 | 13501 | 14424 | 1474.1465 | 24 / 1474 | 1474.15, 737.073, 491.382, 368.537, 245.691, 210.592, 184.268, 163.794, 134.013, 122.846, 113.396, 105.296, 86.7145, 81.897, 67.0067, 61.4228, 56.6979, 52.6481, 43.3573, 40.9485 |
| 2459388.15824 | 15689 | 14424 | 1464.7027 | 13 / 1464 | 1464.7, 488.234, 292.94, 209.243, 162.745, 133.155, 97.6468, 86.159, 63.6827, 58.5881, 54.2482, 47.2485, 9.4497 |
| 2459388.19296 | 9776 | 14424 | 1464.6680 | 11 / 1464 | 1464.67, 488.223, 292.934, 209.238, 162.741, 133.152, 97.6445, 86.1569, 63.6812, 58.5867, 54.247 |
| 2460106.33702 | 14070 | 14424 | 746.5239 | 10 / 746 | 746.524, 373.262, 248.841, 186.631, 149.305, 124.421, 106.646, 93.3155, 82.9471, 9.4497 |
| 2460115.78711 | 13908 | 14424 | 737.0739 | 16 / 737 | 737.074, 368.537, 245.691, 184.268, 122.846, 105.296, 81.8971, 67.0067, 61.4228, 56.698, 52.6481, 43.3573, 40.9485, 28.349, 18.8993, 9.4497 |
| 2461079.65223 | 15187 | 14424 | 226.7913 | 8 / 226 | 226.791, 113.396, 75.5971, 56.6978, 37.7985, 28.3489, 18.8993, 9.4496 |
| 2461089.10212 | 14382 | 14424 | 236.2412 | 5 / 236 | 236.241, 118.121, 78.7471, 47.2482, 9.4496 |
| 2461098.55210 | 14833 | 14424 | 245.6911 | 7 / 245 | 245.691, 122.846, 81.897, 61.4228, 40.9485, 18.8993, 9.4497 |
| 2461136.34945 | 14963 | 14424 | 283.4885 | 8 / 283 | 283.488, 141.744, 94.4962, 56.6977, 47.2481, 28.3488, 18.8992, 9.4496 |
| 2461145.77654 | 13401 | 14424 | 292.9156 | 0 / 292 |  |
| 2461145.80641 | 14307 | 14424 | 292.9454 | 3 / 292 | 292.945, 97.6485, 58.5891 |
| 2461145.82724 | 14307 | 14424 | 292.9663 | 0 / 292 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1059.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:59:19Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:59:20Z: TOI-1059.01 (TIC 380783252, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:59:21Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T09:59:21Z: CD-60  6822 (SB*); TOI-1059.01 (Pl?); TYC 9054-2113-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460852.8607: recovered, depth 14424 ± 170 ppm (catalogue 25388 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, 3, 4.5, 5.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 30%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 17 repeat-candidate event(s); first at BJD 2460833.9619, ΔT = 18.899 d, 2 of 18 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (18.8991, 9.4495 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1059.01: Gaia DR3 5911682531996474624 at 0.00" (propagated 2016.0 → J2015.5; 0.11" unpropagated, proper-motion shift 0.10") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1059.01: dwarf priors not applied — RUWE 1.419898 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1059.01: 49 Gaia neighbour(s) within 52.5", contamination 41.12%; depth 14424 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 5911685486933977728, 26.2", ΔG 0.82); a centroid test is needed |
| Pointing and quality census per event | failed | 23 persistent event(s), 4 clean; BJD 2460833.9619 suspect: MOM_CENTR1 z=+8.1; BJD 2460849.7745 suspect: manual exclude (in event), SAP_BKG z=+8.9; BJD 2458660.5419 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2458669.9876 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 23 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1059.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1059.01: TOI-1059.01 otype Pl? (star_or_other) at 3.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1059-01.yaml
python -m cygnus.multi report campaigns/toi-1059-01.yaml
```
