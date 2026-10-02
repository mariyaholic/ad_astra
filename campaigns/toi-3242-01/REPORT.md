<!-- cygnus:generated-draft -->
# Known-object test, TOI-3242.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3242-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5056, calibrate_screen #5031, event_census #5036, fetch_independent #5052, fetch_products #5013, known_signal_recovery #5032, moving_objects #5050, period_aliases #5037, prior_art #5061, residual_screen #5035, stellar_context #5034, variability_guard #5057
- Runner finished (UTC): 2026-09-30T22:56:00Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3242.01 (BJD 2460070.2692: recovered, depth 14853 ± 629 ppm (catalogue 10600 ppm); BJD 2460073.2694: recovered, depth 12947 ± 561 ppm (catalogue 10600 ppm); BJD 2460076.2695: recovered, depth 14056 ± 655 ppm (catalogue 10600 ppm); BJD 2460079.2697: recovered, depth 15489 ± 625 ppm (catalogue 10600 ppm); BJD 2460082.2699: recovered, depth 17870 ± 631 ppm (catalogue 10600 ppm); BJD 2460085.2700: recovered, depth 14253 ± 608 ppm (catalogue 10600 ppm); BJD 2460088.2702: recovered, depth 10815 ± 632 ppm (catalogue 10600 ppm); BJD 2460091.2703: recovered, depth 13330 ± 649 ppm (catalogue 10600 ppm); BJD 2460094.2705: recovered, depth 9400 ± 644 ppm (catalogue 10600 ppm); BJD 2461048.3222: recovered, depth 14057 ± 717 ppm (catalogue 10600 ppm); BJD 2461051.3224: not recovered, depth 12115 ± 699 ppm (catalogue 10600 ppm); BJD 2461054.3226: recovered, depth 14157 ± 632 ppm (catalogue 10600 ppm); BJD 2461057.3227: gap (catalogue 10600 ppm); BJD 2461060.3229: gap (catalogue 10600 ppm); BJD 2461063.3231: recovered, depth 9417 ± 666 ppm (catalogue 10600 ppm); BJD 2461066.3232: recovered, depth 15982 ± 720 ppm (catalogue 10600 ppm); BJD 2461069.3234: recovered, depth 15804 ± 665 ppm (catalogue 10600 ppm); BJD 2461072.3235: partial, depth 13794 ± 746 ppm (catalogue 10600 ppm); BJD 2461075.3237: partial, depth 14585 ± 692 ppm (catalogue 10600 ppm); BJD 2461078.3239: recovered, depth 13131 ± 693 ppm (catalogue 10600 ppm); BJD 2461081.3240: recovered, depth 16056 ± 717 ppm (catalogue 10600 ppm); BJD 2461084.3242: recovered, depth 14941 ± 692 ppm (catalogue 10600 ppm); BJD 2461087.3244: gap (catalogue 10600 ppm); BJD 2461090.3245: partial, depth 15582 ± 722 ppm (catalogue 10600 ppm); BJD 2461093.3247: partial, depth 13558 ± 879 ppm (catalogue 10600 ppm); BJD 2461096.3248: recovered, depth 14330 ± 667 ppm (catalogue 10600 ppm); BJD 2461099.3250: recovered, depth 17357 ± 732 ppm (catalogue 10600 ppm); BJD 2461102.3252: recovered, depth 14623 ± 823 ppm (catalogue 10600 ppm); BJD 2461105.3253: recovered, depth 17702 ± 746 ppm (catalogue 10600 ppm); BJD 2461108.3255: recovered, depth 14960 ± 804 ppm (catalogue 10600 ppm); BJD 2461111.3257: recovered, depth 13662 ± 787 ppm (catalogue 10600 ppm); BJD 2461114.3258: recovered, depth 17299 ± 849 ppm (catalogue 10600 ppm); BJD 2461117.3260: recovered, depth 16063 ± 831 ppm (catalogue 10600 ppm); BJD 2461120.3261: recovered, depth 15491 ± 735 ppm (catalogue 10600 ppm); BJD 2461123.3263: recovered, depth 13606 ± 779 ppm (catalogue 10600 ppm); BJD 2461126.3265: gap (catalogue 10600 ppm); BJD 2461129.3266: recovered, depth 14645 ± 662 ppm (catalogue 10600 ppm); BJD 2461132.3268: recovered, depth 16066 ± 653 ppm (catalogue 10600 ppm); BJD 2461135.3270: recovered, depth 17022 ± 634 ppm (catalogue 10600 ppm); BJD 2461138.3271: recovered, depth 12877 ± 669 ppm (catalogue 10600 ppm); BJD 2461141.3273: recovered, depth 15788 ± 728 ppm (catalogue 10600 ppm); BJD 2461144.3274: recovered, depth 17015 ± 697 ppm (catalogue 10600 ppm); BJD 2461147.3276: recovered, depth 15388 ± 727 ppm (catalogue 10600 ppm); BJD 2461150.3278: recovered, depth 15135 ± 708 ppm (catalogue 10600 ppm)).
Outside the catalogued epoch the screen left 56 threshold entries forming **18 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461125.3714 matches the catalogued transit's depth (8346 vs 14853 ppm), 1055.107 d later; 16 of 1055 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3242.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 209923610 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 211.181028 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -55.447698 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459356.230477 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.0001627 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10600.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.892 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.3666 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | lightcurve | 65 | False | `5c01a34866149666` | True |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | lightcurve | 99 | False | `24c3aab785456818` | True |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | lightcurve | 100 | False | `4cccbec4e433ac84` | True |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | lightcurve | 101 | False | `2c1525f16b9053e1` | True |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | lightcurve | 102 | False | `0862684b6ba58e1b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460070.26920 | recovered | 87 | 14853 ± 629 | 10600 | -0.12 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460073.26936 | recovered | 87 | 12947 ± 561 | 10600 | -0.26 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460076.26952 | recovered | 86 | 14056 ± 655 | 10600 | -0.13 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460079.26969 | recovered | 86 | 15489 ± 625 | 10600 | 0.20 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460082.26985 | recovered | 87 | 17870 ± 631 | 10600 | 0.03 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460085.27001 | recovered | 87 | 14253 ± 608 | 10600 | 0.28 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460088.27018 | recovered | 87 | 10815 ± 632 | 10600 | -1.07 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460091.27034 | recovered | 87 | 13330 ± 649 | 10600 | -0.04 |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460094.27050 | recovered | 87 | 9400 ± 644 | 10600 | -0.03 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461048.32224 | recovered | 87 | 14057 ± 717 | 10600 | -0.52 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461051.32240 | not_recovered | 87 | 12115 ± 699 | 10600 | — |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461054.32257 | recovered | 87 | 14157 ± 632 | 10600 | 0.55 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461057.32273 | gap | 0 | — | 10600 | — |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461060.32289 | gap | 0 | — | 10600 | — |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461063.32305 | recovered | 87 | 9417 ± 666 | 10600 | -0.58 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461066.32322 | recovered | 87 | 15982 ± 720 | 10600 | -0.41 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461069.32338 | recovered | 87 | 15804 ± 665 | 10600 | -0.28 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 2461072.32354 | partial | 87 | 13794 ± 746 | 10600 | 0.29 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461075.32370 | partial | 87 | 14585 ± 692 | 10600 | -0.07 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461078.32387 | recovered | 87 | 13131 ± 693 | 10600 | 0.73 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461081.32403 | recovered | 86 | 16056 ± 717 | 10600 | -0.10 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461084.32419 | recovered | 86 | 14941 ± 692 | 10600 | 0.10 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461087.32435 | gap | 0 | — | 10600 | — |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461090.32452 | partial | 86 | 15582 ± 722 | 10600 | -0.46 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461093.32468 | partial | 55 | 13558 ± 879 | 10600 | -0.50 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461096.32484 | recovered | 87 | 14330 ± 667 | 10600 | 0.24 |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461099.32501 | recovered | 87 | 17357 ± 732 | 10600 | 0.04 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461102.32517 | recovered | 87 | 14623 ± 823 | 10600 | 0.24 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461105.32533 | recovered | 87 | 17702 ± 746 | 10600 | 0.03 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461108.32549 | recovered | 87 | 14960 ± 804 | 10600 | -0.19 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461111.32566 | recovered | 87 | 13662 ± 787 | 10600 | -0.44 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461114.32582 | recovered | 87 | 17299 ± 849 | 10600 | 0.08 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461117.32598 | recovered | 87 | 16063 ± 831 | 10600 | -0.39 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461120.32614 | recovered | 87 | 15491 ± 735 | 10600 | -0.59 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461123.32631 | recovered | 87 | 13606 ± 779 | 10600 | 0.36 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461126.32647 | gap | 0 | — | 10600 | — |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461129.32663 | recovered | 87 | 14645 ± 662 | 10600 | -0.02 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461132.32680 | recovered | 87 | 16066 ± 653 | 10600 | -0.50 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461135.32696 | recovered | 87 | 17022 ± 634 | 10600 | -0.22 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461138.32712 | recovered | 87 | 12877 ± 669 | 10600 | -0.15 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461141.32728 | recovered | 87 | 15788 ± 728 | 10600 | -0.26 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461144.32745 | recovered | 87 | 17015 ± 697 | 10600 | -0.35 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461147.32761 | recovered | 87 | 15388 ± 727 | 10600 | 0.38 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461150.32777 | recovered | 87 | 15135 ± 708 | 10600 | -0.26 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026005125623-s0099-0000000209923610-0300-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.49365 | -0.02930 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.50060 | -0.02801 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.43809 | -0.02679 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.48949 | -0.02641 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461124.07830 | -0.02510 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.48254 | -0.02407 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.37142 | -0.02152 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.36170 | -0.02501 | 2 | PDCSAP+SAP | 3 | no |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461145.67930 | -0.00993 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460083.25848 | -0.00951 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000209923610-0303-s_lc.fits` | 2461125.46865 | -0.00930 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460082.94321 | -0.00900 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461146.01403 | -0.00885 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000209923610-0302-s_lc.fits` | 2461093.61930 | -0.00877 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000209923610-0259-s_lc.fits` | 2460082.99460 | -0.00872 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461145.91959 | -0.00863 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461144.94594 | -0.00853 | 2 | SAP | 1, 3 | no |
| `tess2026086090000-s0102-0000000209923610-0304-s_lc.fits` | 2461132.97600 | -0.00841 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461125.37142 | 8346 | 14853 | 1055.1074 | 16 / 1055 | 1055.11, 527.554, 351.702, 263.777, 211.022, 175.851, 150.73, 131.888, 117.234, 105.511, 95.9189, 87.9256, 81.1621, 65.9442, 62.0651, 43.9628 |
| 2461125.43809 | 13251 | 14853 | 1055.1741 | 14 / 1055 | 1055.17, 527.587, 351.725, 263.793, 211.035, 175.862, 150.739, 131.897, 117.242, 105.517, 95.9249, 87.9312, 81.1672, 65.9484 |
| 2461125.48254 | 16293 | 14853 | 1055.2185 | 15 / 1055 | 1055.22, 527.609, 351.74, 263.805, 211.044, 175.87, 150.745, 131.902, 117.246, 105.522, 95.929, 87.9349, 81.1707, 65.9512, 31.9763 |
| 2461125.48949 | 16652 | 14853 | 1055.2255 | 15 / 1055 | 1055.23, 527.613, 351.742, 263.806, 211.045, 175.871, 150.746, 131.903, 117.247, 105.522, 95.9296, 87.9355, 81.1712, 65.9516, 31.9765 |
| 2461125.49365 | 16695 | 14853 | 1055.2296 | 15 / 1055 | 1055.23, 527.615, 351.743, 263.807, 211.046, 175.872, 150.747, 131.904, 117.248, 105.523, 95.93, 87.9358, 81.1715, 65.9519, 31.9767 |
| 2461125.50060 | 16652 | 14853 | 1055.2366 | 16 / 1055 | 1055.24, 527.618, 351.745, 263.809, 211.047, 175.873, 150.748, 131.905, 117.249, 105.524, 95.9306, 87.9364, 81.172, 65.9523, 50.2494, 31.9769 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3242.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:55:45Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:55:48Z: TOI-3242.01 (TIC 209923610, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:55:52Z: Gaia DR3 5896362349318312832 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T22:55:54Z: TOI-3242.01 (Pl?); TOI-3242 (*); Gaia DR3 5896362349288353920 (RR?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460070.2692: recovered, depth 14853 ± 629 ppm (catalogue 10600 ppm); BJD 2460073.2694: recovered, depth 12947 ± 561 ppm (catalogue 10600 ppm); BJD 2460076.2695: recovered, depth 14056 ± 655 ppm (catalogue 10600 ppm); BJD 2460079.2697: recovered, depth 15489 ± 625 ppm (catalogue 10600 ppm); BJD 2460082.2699: recovered, depth 17870 ± 631 ppm (catalogue 10600 ppm); BJD 2460085.2700: recovered, depth 14253 ± 608 ppm (catalogue 10600 ppm); BJD 2460088.2702: recovered, depth 10815 ± 632 ppm (catalogue 10600 ppm); BJD 2460091.2703: recovered, depth 13330 ± 649 ppm (catalogue 10600 ppm); BJD 2460094.2705: recovered, depth 9400 ± 644 ppm (catalogue 10600 ppm); BJD 2461048.3222: recovered, depth 14057 ± 717 ppm (catalogue 10600 ppm); BJD 2461051.3224: not recovered, depth 12115 ± 699 ppm (catalogue 10600 ppm); BJD 2461054.3226: recovered, depth 14157 ± 632 ppm (catalogue 10600 ppm); BJD 2461057.3227: gap (catalogue 10600 ppm); BJD 2461060.3229: gap (catalogue 10600 ppm); BJD 2461063.3231: recovered, depth 9417 ± 666 ppm (catalogue 10600 ppm); BJD 2461066.3232: recovered, depth 15982 ± 720 ppm (catalogue 10600 ppm); BJD 2461069.3234: recovered, depth 15804 ± 665 ppm (catalogue 10600 ppm); BJD 2461072.3235: partial, depth 13794 ± 746 ppm (catalogue 10600 ppm); BJD 2461075.3237: partial, depth 14585 ± 692 ppm (catalogue 10600 ppm); BJD 2461078.3239: recovered, depth 13131 ± 693 ppm (catalogue 10600 ppm); BJD 2461081.3240: recovered, depth 16056 ± 717 ppm (catalogue 10600 ppm); BJD 2461084.3242: recovered, depth 14941 ± 692 ppm (catalogue 10600 ppm); BJD 2461087.3244: gap (catalogue 10600 ppm); BJD 2461090.3245: partial, depth 15582 ± 722 ppm (catalogue 10600 ppm); BJD 2461093.3247: partial, depth 13558 ± 879 ppm (catalogue 10600 ppm); BJD 2461096.3248: recovered, depth 14330 ± 667 ppm (catalogue 10600 ppm); BJD 2461099.3250: recovered, depth 17357 ± 732 ppm (catalogue 10600 ppm); BJD 2461102.3252: recovered, depth 14623 ± 823 ppm (catalogue 10600 ppm); BJD 2461105.3253: recovered, depth 17702 ± 746 ppm (catalogue 10600 ppm); BJD 2461108.3255: recovered, depth 14960 ± 804 ppm (catalogue 10600 ppm); BJD 2461111.3257: recovered, depth 13662 ± 787 ppm (catalogue 10600 ppm); BJD 2461114.3258: recovered, depth 17299 ± 849 ppm (catalogue 10600 ppm); BJD 2461117.3260: recovered, depth 16063 ± 831 ppm (catalogue 10600 ppm); BJD 2461120.3261: recovered, depth 15491 ± 735 ppm (catalogue 10600 ppm); BJD 2461123.3263: recovered, depth 13606 ± 779 ppm (catalogue 10600 ppm); BJD 2461126.3265: gap (catalogue 10600 ppm); BJD 2461129.3266: recovered, depth 14645 ± 662 ppm (catalogue 10600 ppm); BJD 2461132.3268: recovered, depth 16066 ± 653 ppm (catalogue 10600 ppm); BJD 2461135.3270: recovered, depth 17022 ± 634 ppm (catalogue 10600 ppm); BJD 2461138.3271: recovered, depth 12877 ± 669 ppm (catalogue 10600 ppm); BJD 2461141.3273: recovered, depth 15788 ± 728 ppm (catalogue 10600 ppm); BJD 2461144.3274: recovered, depth 17015 ± 697 ppm (catalogue 10600 ppm); BJD 2461147.3276: recovered, depth 15388 ± 727 ppm (catalogue 10600 ppm); BJD 2461150.3278: recovered, depth 15135 ± 708 ppm (catalogue 10600 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 6 repeat-candidate event(s); first at BJD 2461125.3714, ΔT = 1055.107 d, 16 of 1055 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1055.11, 527.554, 351.702, 263.777, 211.022, 175.851, 150.73, 131.888, 117.234, 105.511, 95.9189, 87.9256 … d); duration likelihood under Gaia priors (circular orbits) peaks at 44 d (weight 0.98) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3242.01: Gaia DR3 5896362344993281024 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3242.01: Teff 6036 K, R* 1.39 ± 0.11, M* 1.27 ± 0.13, ρ* 0.48 ± 0.12 ρ☉ (dwarf sequence, M_G 3.49, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3242.01: 185 Gaia neighbour(s) within 52.5", contamination 86.27%; depth 14853 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 5896362383648132480, 50.7", ΔG -1.57); a centroid test is needed |
| Pointing and quality census per event | failed | 7 persistent event(s), 1 clean; BJD 2461125.3714 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+951.7; BJD 2461125.4381 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+828.2; BJD 2461125.4825 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+722.0; BJD 2461125.4895 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+712.7 |
| Moving objects at screen-event epochs | inconclusive | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3242.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3242.01: TOI-3242.01 otype Pl? (star_or_other) at 0.0" |
| Event-time prior art | inconclusive | 6 possible published-ephemeris overlap(s) within 1 d (TOI-3242.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3242-01.yaml
python -m cygnus.multi report campaigns/toi-3242-01.yaml
```
