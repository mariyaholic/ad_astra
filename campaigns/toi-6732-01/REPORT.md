<!-- cygnus:generated-draft -->
# Known-object test, TOI-6732.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6732-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4391, calibrate_screen #4361, event_census #4373, fetch_independent #4379, fetch_products #4358, known_signal_recovery #4363, moving_objects #4377, period_aliases #4376, prior_art #4394, residual_screen #4367, stellar_context #4364, variability_guard #4392
- Runner finished (UTC): 2026-09-30T21:50:56Z

## Bottom line

Positive control **inconclusive**: BJD 2460830.1836: gap (catalogue 38320 ppm); BJD 2460831.4839: not recovered, depth 6589 ± 4840 ppm (catalogue 38320 ppm); BJD 2460832.7843: not recovered, depth 7232 ± 4468 ppm (catalogue 38320 ppm); BJD 2460834.0846: not recovered, depth -2256 ± 4726 ppm (catalogue 38320 ppm); BJD 2460835.3849: not recovered, depth -78 ± 4641 ppm (catalogue 38320 ppm); BJD 2460836.6853: partial, depth -9027 ± 4500 ppm (catalogue 38320 ppm); BJD 2460837.9856: not recovered, depth -7141 ± 4776 ppm (catalogue 38320 ppm); BJD 2460839.2860: not recovered, depth -3591 ± 4712 ppm (catalogue 38320 ppm); BJD 2460840.5863: not recovered, depth 565 ± 4840 ppm (catalogue 38320 ppm); BJD 2460841.8866: gap (catalogue 38320 ppm); BJD 2460843.1870: gap (catalogue 38320 ppm); BJD 2460844.4873: not recovered, depth 3273 ± 4808 ppm (catalogue 38320 ppm); BJD 2460845.7877: not recovered, depth -5209 ± 4628 ppm (catalogue 38320 ppm); BJD 2460847.0880: not recovered, depth 4900 ± 4562 ppm (catalogue 38320 ppm); BJD 2460848.3883: not recovered, depth -2512 ± 4817 ppm (catalogue 38320 ppm); BJD 2460849.6887: not recovered, depth 5355 ± 4781 ppm (catalogue 38320 ppm); BJD 2460850.9890: not recovered, depth 3454 ± 4553 ppm (catalogue 38320 ppm); BJD 2460852.2894: not recovered, depth -2048 ± 4506 ppm (catalogue 38320 ppm); BJD 2460853.5897: not recovered, depth -3516 ± 4804 ppm (catalogue 38320 ppm); BJD 2460854.8900: gap (catalogue 38320 ppm); BJD 2461152.6678: gap (catalogue 38320 ppm); BJD 2461153.9681: not recovered, depth 4065 ± 5938 ppm (catalogue 38320 ppm); BJD 2461155.2684: not recovered, depth 13919 ± 5215 ppm (catalogue 38320 ppm); BJD 2461156.5688: not recovered, depth 6589 ± 5193 ppm (catalogue 38320 ppm); BJD 2461157.8691: not recovered, depth 5336 ± 5249 ppm (catalogue 38320 ppm); BJD 2461159.1695: partial, depth 7770 ± 5396 ppm (catalogue 38320 ppm); BJD 2461160.4698: not recovered, depth -2234 ± 5239 ppm (catalogue 38320 ppm); BJD 2461161.7701: not recovered, depth -1086 ± 4954 ppm (catalogue 38320 ppm); BJD 2461163.0705: not recovered, depth 772 ± 5334 ppm (catalogue 38320 ppm); BJD 2461164.3708: not recovered, depth -45366 ± 5433 ppm (catalogue 38320 ppm); BJD 2461165.6711: gap (catalogue 38320 ppm); BJD 2461166.9715: not recovered, depth -9220 ± 5937 ppm (catalogue 38320 ppm); BJD 2461168.2718: not recovered, depth -3147 ± 5246 ppm (catalogue 38320 ppm); BJD 2461169.5722: not recovered, depth -8796 ± 5141 ppm (catalogue 38320 ppm); BJD 2461170.8725: not recovered, depth 1302 ± 6349 ppm (catalogue 38320 ppm); BJD 2461172.1728: partial, depth 11772 ± 5526 ppm (catalogue 38320 ppm); BJD 2461173.4732: not recovered, depth 2145 ± 5258 ppm (catalogue 38320 ppm); BJD 2461174.7735: not recovered, depth 1348 ± 5072 ppm (catalogue 38320 ppm); BJD 2461176.0739: not recovered, depth 10473 ± 5328 ppm (catalogue 38320 ppm); BJD 2461177.3742: partial, depth 1559 ± 5479 ppm (catalogue 38320 ppm); BJD 2461178.6745: gap (catalogue 38320 ppm); BJD 2461179.9749: not recovered, depth 15896 ± 4430 ppm (catalogue 38320 ppm); BJD 2461181.2752: not recovered, depth 10383 ± 3934 ppm (catalogue 38320 ppm); BJD 2461182.5756: not recovered, depth 3260 ± 3851 ppm (catalogue 38320 ppm); BJD 2461183.8759: not recovered, depth -1426 ± 3930 ppm (catalogue 38320 ppm); BJD 2461185.1762: not recovered, depth 752 ± 3868 ppm (catalogue 38320 ppm); BJD 2461186.4766: not recovered, depth -56 ± 3944 ppm (catalogue 38320 ppm); BJD 2461187.7769: not recovered, depth 4367 ± 3816 ppm (catalogue 38320 ppm); BJD 2461189.0773: not recovered, depth -4535 ± 3851 ppm (catalogue 38320 ppm); BJD 2461190.3776: not recovered, depth -18475 ± 4065 ppm (catalogue 38320 ppm); BJD 2461191.6779: gap (catalogue 38320 ppm); BJD 2461192.9783: gap (catalogue 38320 ppm); BJD 2461194.2786: not recovered, depth -3871 ± 4101 ppm (catalogue 38320 ppm); BJD 2461195.5790: not recovered, depth -1210 ± 3868 ppm (catalogue 38320 ppm); BJD 2461196.8793: not recovered, depth 5443 ± 4021 ppm (catalogue 38320 ppm); BJD 2461198.1796: gap (catalogue 38320 ppm); BJD 2461199.4800: not recovered, depth 7343 ± 3900 ppm (catalogue 38320 ppm); BJD 2461200.7803: partial, depth -5087 ± 3804 ppm (catalogue 38320 ppm); BJD 2461202.0807: not recovered, depth 582 ± 3656 ppm (catalogue 38320 ppm); BJD 2461203.3810: not recovered, depth -3680 ± 3826 ppm (catalogue 38320 ppm); BJD 2461204.6813: gap (catalogue 38320 ppm).
Outside the catalogued epoch the screen left 350 threshold entries forming **158 distinct event(s)**, **13 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6732.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 349891396 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 274.39888 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -53.01713 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460121.49861 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1.3003394 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 38320.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.341 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 14.2548 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-06-25 12:03:43 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | lightcurve | 93 | False | `ba7d009cac977a4e` | True |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | lightcurve | 103 | False | `2929df1202e6b41f` | True |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | lightcurve | 104 | False | `781465e2783af230` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460830.18358 | gap | 0 | — | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460831.48392 | not_recovered | 40 | 6589 ± 4840 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460832.78426 | not_recovered | 40 | 7232 ± 4468 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460834.08460 | not_recovered | 40 | -2256 ± 4726 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460835.38494 | not_recovered | 40 | -78 ± 4641 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.68528 | partial | 41 | -9027 ± 4500 | 38320 | -1.15 |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460837.98562 | not_recovered | 40 | -7141 ± 4776 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460839.28596 | not_recovered | 40 | -3591 ± 4712 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460840.58630 | not_recovered | 40 | 565 ± 4840 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460841.88664 | gap | 0 | — | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.18698 | gap | 0 | — | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460844.48732 | not_recovered | 40 | 3273 ± 4808 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460845.78766 | not_recovered | 40 | -5209 ± 4628 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460847.08800 | not_recovered | 41 | 4900 ± 4562 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460848.38833 | not_recovered | 40 | -2512 ± 4817 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460849.68867 | not_recovered | 40 | 5355 ± 4781 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.98901 | not_recovered | 40 | 3454 ± 4553 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460852.28935 | not_recovered | 40 | -2048 ± 4506 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460853.58969 | not_recovered | 41 | -3516 ± 4804 | 38320 | — |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460854.89003 | gap | 0 | — | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461152.66775 | gap | 0 | — | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.96809 | not_recovered | 40 | 4065 ± 5938 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461155.26843 | not_recovered | 40 | 13919 ± 5215 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461156.56877 | not_recovered | 40 | 6589 ± 5193 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461157.86911 | not_recovered | 41 | 5336 ± 5249 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.16945 | partial | 40 | 7770 ± 5396 | 38320 | -0.62 |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461160.46979 | not_recovered | 40 | -2234 ± 5239 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461161.77013 | not_recovered | 40 | -1086 ± 4954 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461163.07047 | not_recovered | 40 | 772 ± 5334 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461164.37081 | not_recovered | 41 | -45366 ± 5433 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461165.67115 | gap | 0 | — | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461166.97149 | not_recovered | 40 | -9220 ± 5937 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461168.27183 | not_recovered | 40 | -3147 ± 5246 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461169.57217 | not_recovered | 40 | -8796 ± 5141 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461170.87251 | not_recovered | 28 | 1302 ± 6349 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.17285 | partial | 41 | 11772 ± 5526 | 38320 | -0.45 |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461173.47318 | not_recovered | 40 | 2145 ± 5258 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461174.77352 | not_recovered | 40 | 1348 ± 5072 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461176.07386 | not_recovered | 40 | 10473 ± 5328 | 38320 | — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461177.37420 | partial | 39 | 1559 ± 5479 | 38320 | -0.98 |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461178.67454 | gap | 0 | — | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461179.97488 | not_recovered | 40 | 15896 ± 4430 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461181.27522 | not_recovered | 40 | 10383 ± 3934 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461182.57556 | not_recovered | 40 | 3260 ± 3851 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461183.87590 | not_recovered | 40 | -1426 ± 3930 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461185.17624 | not_recovered | 41 | 752 ± 3868 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461186.47658 | not_recovered | 40 | -56 ± 3944 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461187.77692 | not_recovered | 40 | 4367 ± 3816 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461189.07726 | not_recovered | 40 | -4535 ± 3851 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461190.37760 | not_recovered | 40 | -18475 ± 4065 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461191.67794 | gap | 0 | — | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461192.97828 | gap | 0 | — | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461194.27862 | not_recovered | 40 | -3871 ± 4101 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461195.57895 | not_recovered | 40 | -1210 ± 3868 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461196.87929 | not_recovered | 41 | 5443 ± 4021 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.17963 | gap | 0 | — | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461199.47997 | not_recovered | 40 | 7343 ± 3900 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461200.78031 | partial | 40 | -5087 ± 3804 | 38320 | 1.38 |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461202.08065 | not_recovered | 40 | 582 ± 3656 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461203.38099 | not_recovered | 41 | -3680 ± 3826 | 38320 | — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461204.68133 | gap | 0 | — | 38320 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461167.15232 | -0.10450 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461202.28229 | -0.09567 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.38846 | -0.09393 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461195.77449 | -0.09348 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461181.45588 | -0.08949 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461194.48139 | -0.08912 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460832.90667 | -0.08881 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.38012 | -0.08844 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.38429 | -0.08408 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.37387 | -0.08063 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461199.66071 | -0.08032 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461197.09536 | -0.07743 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.36762 | -0.07574 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461167.16205 | -0.12383 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.27566 | -0.11764 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.31942 | -0.11240 | 2 | PDCSAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.30553 | -0.10970 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.62179 | -0.10755 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.26663 | -0.10435 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.31455 | -0.10374 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.29997 | -0.10373 | 2 | PDCSAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460840.73738 | -0.09981 | 2 | PDCSAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461168.46352 | -0.09913 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461167.17038 | -0.09898 | 2 | PDCSAP | 1, 2 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.34372 | -0.09843 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461176.24314 | -0.09839 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461174.95557 | -0.09478 | 2 | PDCSAP | 1, 2 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461153.29233 | -0.09382 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460854.60966 | -0.09374 | 2 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460848.53468 | -0.09321 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461194.45570 | -0.09054 | 3 | PDCSAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461180.14957 | -0.08997 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460831.60247 | -0.08993 | 2 | PDCSAP | 1, 2 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460839.42069 | -0.08960 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461180.15721 | -0.08931 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460840.73043 | -0.08825 | 4 | PDCSAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460840.70682 | -0.08804 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461202.27743 | -0.08770 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461189.26871 | -0.08512 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460853.73189 | -0.08429 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461195.76060 | -0.08256 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460835.52479 | -0.08237 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461199.65376 | -0.08151 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460847.23745 | -0.08144 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460840.71863 | -0.08079 | 5 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460834.21921 | -0.08071 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460854.58189 | -0.07989 | 2 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460853.99022 | -0.07851 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461197.07314 | -0.07844 | 2 | PDCSAP | 2 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461195.78560 | -0.07840 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461182.74484 | -0.07786 | 2 | PDCSAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461182.76984 | -0.07625 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461184.05601 | -0.07598 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461181.47255 | -0.07528 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.65513 | -0.07519 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461185.36162 | -0.07515 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461202.25659 | -0.07416 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461181.46839 | -0.07387 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461180.17526 | -0.07379 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461202.26215 | -0.07348 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461203.57744 | -0.07315 | 2 | PDCSAP | 1 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461190.55417 | -0.07267 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461187.97561 | -0.07202 | 2 | PDCSAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461190.57709 | -0.07169 | 2 | PDCSAP | 1 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461203.55800 | -0.07110 | 2 | PDCSAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461179.54467 | -0.07048 | 2 | PDCSAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461182.79206 | -0.07037 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461179.62662 | -0.06979 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.39401 | -0.06760 | 2 | PDCSAP | 1 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461202.28923 | -0.06662 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461187.95895 | -0.06344 | 2 | PDCSAP | 1 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461200.88018 | -0.05514 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.63013 | -0.04813 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461203.04133 | -0.03729 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.55120 | -0.03712 | 4 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.36154 | -0.03386 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.34918 | -0.03318 | 9 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.37195 | -0.03276 | 7 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.26237 | -0.03257 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.35821 | -0.03114 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.82065 | -0.03063 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.67318 | -0.03027 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.34818 | -0.03026 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.63846 | -0.03015 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.59634 | -0.03006 | 3 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.38807 | -0.02990 | 3 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000349891396-0306-s_lc.fits` | 2461198.68568 | -0.02985 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.29848 | -0.02983 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.43599 | -0.02885 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.36376 | -0.02880 | 4 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.70686 | -0.02879 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.12219 | -0.02875 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.63325 | -0.02852 | 4 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.43654 | -0.02818 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.37959 | -0.02802 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.56370 | -0.02776 | 4 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.33862 | -0.02776 | 3 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.74158 | -0.02770 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.33237 | -0.02743 | 4 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.11594 | -0.02732 | 3 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.60408 | -0.02724 | 6 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.56850 | -0.02713 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.49627 | -0.02707 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.55676 | -0.02700 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.57343 | -0.02692 | 4 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.82690 | -0.02690 | 5 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461172.37626 | -0.02682 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.64019 | -0.02673 | 4 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.34765 | -0.02619 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.68464 | -0.02595 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.58949 | -0.02581 | 30 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.26941 | -0.02576 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.42682 | -0.02573 | 4 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.58037 | -0.02552 | 4 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.35529 | -0.02550 | 5 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.81301 | -0.02549 | 7 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.83524 | -0.02523 | 3 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.65130 | -0.02512 | 10 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.79704 | -0.02475 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.78871 | -0.02461 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.31153 | -0.02450 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.79287 | -0.02437 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.67838 | -0.02431 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.58662 | -0.02427 | 4 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000349891396-0305-s_lc.fits` | 2461159.52405 | -0.02422 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.14302 | -0.02403 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.12913 | -0.02399 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.68950 | -0.02388 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.62005 | -0.02375 | 13 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.13330 | -0.02371 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.21177 | -0.02367 | 3 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.34719 | -0.02359 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.70200 | -0.02342 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.18608 | -0.02340 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.81103 | -0.02323 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.14858 | -0.02311 | 4 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.80329 | -0.02289 | 5 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.37496 | -0.02272 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.66380 | -0.02251 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.74922 | -0.02248 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.13816 | -0.02247 | 3 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.20413 | -0.02240 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.44857 | -0.02230 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.76103 | -0.02215 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.16246 | -0.02206 | 4 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.72352 | -0.02163 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.84010 | -0.02157 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.67213 | -0.02129 | 4 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.90547 | -0.02113 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.32427 | -0.02086 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.75686 | -0.02079 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.79228 | -0.02010 | 3 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.23191 | -0.02005 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.39024 | -0.02001 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.22219 | -0.01996 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460850.17427 | -0.01931 | 7 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460836.95121 | -0.01928 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000349891396-0290-s_lc.fits` | 2460843.94714 | -0.01923 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6732.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:50:49Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:50:52Z: TOI-6732.01 (TIC 349891396, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:50:54Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:50:55Z: UCAC4 185-202831 (*); UCAC4 185-202833 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460830.1836: gap (catalogue 38320 ppm); BJD 2460831.4839: not recovered, depth 6589 ± 4840 ppm (catalogue 38320 ppm); BJD 2460832.7843: not recovered, depth 7232 ± 4468 ppm (catalogue 38320 ppm); BJD 2460834.0846: not recovered, depth -2256 ± 4726 ppm (catalogue 38320 ppm); BJD 2460835.3849: not recovered, depth -78 ± 4641 ppm (catalogue 38320 ppm); BJD 2460836.6853: partial, depth -9027 ± 4500 ppm (catalogue 38320 ppm); BJD 2460837.9856: not recovered, depth -7141 ± 4776 ppm (catalogue 38320 ppm); BJD 2460839.2860: not recovered, depth -3591 ± 4712 ppm (catalogue 38320 ppm); BJD 2460840.5863: not recovered, depth 565 ± 4840 ppm (catalogue 38320 ppm); BJD 2460841.8866: gap (catalogue 38320 ppm); BJD 2460843.1870: gap (catalogue 38320 ppm); BJD 2460844.4873: not recovered, depth 3273 ± 4808 ppm (catalogue 38320 ppm); BJD 2460845.7877: not recovered, depth -5209 ± 4628 ppm (catalogue 38320 ppm); BJD 2460847.0880: not recovered, depth 4900 ± 4562 ppm (catalogue 38320 ppm); BJD 2460848.3883: not recovered, depth -2512 ± 4817 ppm (catalogue 38320 ppm); BJD 2460849.6887: not recovered, depth 5355 ± 4781 ppm (catalogue 38320 ppm); BJD 2460850.9890: not recovered, depth 3454 ± 4553 ppm (catalogue 38320 ppm); BJD 2460852.2894: not recovered, depth -2048 ± 4506 ppm (catalogue 38320 ppm); BJD 2460853.5897: not recovered, depth -3516 ± 4804 ppm (catalogue 38320 ppm); BJD 2460854.8900: gap (catalogue 38320 ppm); BJD 2461152.6678: gap (catalogue 38320 ppm); BJD 2461153.9681: not recovered, depth 4065 ± 5938 ppm (catalogue 38320 ppm); BJD 2461155.2684: not recovered, depth 13919 ± 5215 ppm (catalogue 38320 ppm); BJD 2461156.5688: not recovered, depth 6589 ± 5193 ppm (catalogue 38320 ppm); BJD 2461157.8691: not recovered, depth 5336 ± 5249 ppm (catalogue 38320 ppm); BJD 2461159.1695: partial, depth 7770 ± 5396 ppm (catalogue 38320 ppm); BJD 2461160.4698: not recovered, depth -2234 ± 5239 ppm (catalogue 38320 ppm); BJD 2461161.7701: not recovered, depth -1086 ± 4954 ppm (catalogue 38320 ppm); BJD 2461163.0705: not recovered, depth 772 ± 5334 ppm (catalogue 38320 ppm); BJD 2461164.3708: not recovered, depth -45366 ± 5433 ppm (catalogue 38320 ppm); BJD 2461165.6711: gap (catalogue 38320 ppm); BJD 2461166.9715: not recovered, depth -9220 ± 5937 ppm (catalogue 38320 ppm); BJD 2461168.2718: not recovered, depth -3147 ± 5246 ppm (catalogue 38320 ppm); BJD 2461169.5722: not recovered, depth -8796 ± 5141 ppm (catalogue 38320 ppm); BJD 2461170.8725: not recovered, depth 1302 ± 6349 ppm (catalogue 38320 ppm); BJD 2461172.1728: partial, depth 11772 ± 5526 ppm (catalogue 38320 ppm); BJD 2461173.4732: not recovered, depth 2145 ± 5258 ppm (catalogue 38320 ppm); BJD 2461174.7735: not recovered, depth 1348 ± 5072 ppm (catalogue 38320 ppm); BJD 2461176.0739: not recovered, depth 10473 ± 5328 ppm (catalogue 38320 ppm); BJD 2461177.3742: partial, depth 1559 ± 5479 ppm (catalogue 38320 ppm); BJD 2461178.6745: gap (catalogue 38320 ppm); BJD 2461179.9749: not recovered, depth 15896 ± 4430 ppm (catalogue 38320 ppm); BJD 2461181.2752: not recovered, depth 10383 ± 3934 ppm (catalogue 38320 ppm); BJD 2461182.5756: not recovered, depth 3260 ± 3851 ppm (catalogue 38320 ppm); BJD 2461183.8759: not recovered, depth -1426 ± 3930 ppm (catalogue 38320 ppm); BJD 2461185.1762: not recovered, depth 752 ± 3868 ppm (catalogue 38320 ppm); BJD 2461186.4766: not recovered, depth -56 ± 3944 ppm (catalogue 38320 ppm); BJD 2461187.7769: not recovered, depth 4367 ± 3816 ppm (catalogue 38320 ppm); BJD 2461189.0773: not recovered, depth -4535 ± 3851 ppm (catalogue 38320 ppm); BJD 2461190.3776: not recovered, depth -18475 ± 4065 ppm (catalogue 38320 ppm); BJD 2461191.6779: gap (catalogue 38320 ppm); BJD 2461192.9783: gap (catalogue 38320 ppm); BJD 2461194.2786: not recovered, depth -3871 ± 4101 ppm (catalogue 38320 ppm); BJD 2461195.5790: not recovered, depth -1210 ± 3868 ppm (catalogue 38320 ppm); BJD 2461196.8793: not recovered, depth 5443 ± 4021 ppm (catalogue 38320 ppm); BJD 2461198.1796: gap (catalogue 38320 ppm); BJD 2461199.4800: not recovered, depth 7343 ± 3900 ppm (catalogue 38320 ppm); BJD 2461200.7803: partial, depth -5087 ± 3804 ppm (catalogue 38320 ppm); BJD 2461202.0807: not recovered, depth 582 ± 3656 ppm (catalogue 38320 ppm); BJD 2461203.3810: not recovered, depth -3680 ± 3826 ppm (catalogue 38320 ppm); BJD 2461204.6813: gap (catalogue 38320 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6732.01: Gaia DR3 6653816012742811136 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6732.01: Teff 3614 K, R* 0.54 ± 0.04, M* 0.54 ± 0.05, ρ* 3.38 ± 0.88 ρ☉ (dwarf sequence, M_G 8.46, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6732.01: 53 Gaia neighbour(s) within 52.5", contamination 93.99%; depth 38320 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 6653816012742809728, 18.4", ΔG -2.77); a centroid test is needed |
| Pointing and quality census per event | inconclusive | 13 persistent event(s), 8 clean; BJD 2461198.3676 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2461198.3739 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2461198.3801 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2461198.3843 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 13 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6732.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6732.01: UCAC4 185-202833 otype * (star_or_other) at 0.3" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6732-01.yaml
python -m cygnus.multi report campaigns/toi-6732-01.yaml
```
