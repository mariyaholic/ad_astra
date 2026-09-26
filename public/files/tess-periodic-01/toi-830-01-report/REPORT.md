<!-- [private Drive store] -->
# Known-object test, TOI-830.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-830-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1027, calibrate_screen #1008, event_census #1016, fetch_products #1003, known_signal_recovery #1013, moving_objects #1018, period_aliases #1017, prior_art #1029, residual_screen #1015, stellar_context #1014, variability_guard #1028
- Runner finished (UTC): 2026-09-26T10:28:47Z

## Bottom line

Positive control **inconclusive**: BJD 2458584.4536: gap (catalogue 17982 ppm).
Outside the catalogued epoch the screen left 264 threshold entries forming **110 distinct event(s)**, **15 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-830.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 281924357 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 129.756861 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -74.763114 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458584.453568 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 17981.6903217 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.2981691 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.9303 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-06-03 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | lightcurve | 10 | True | `ad630a538d2590f8` | True |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | lightcurve | 11 | False | `66a6d42fe5606890` | True |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | lightcurve | 12 | False | `8326784dbdec6508` | True |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | lightcurve | 33 | False | `60ca25ab8246d614` | True |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | lightcurve | 36 | False | `46dc9a608b7cbe89` | True |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | lightcurve | 37 | False | `703da0c3a3f4e182` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458584.45357 | gap | 0 | — | 17982 | — |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | — | epoch not in this light curve | — | — | 17982 | — |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | — | epoch not in this light curve | — | — | 17982 | — |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | — | epoch not in this light curve | — | — | 17982 | — |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | — | epoch not in this light curve | — | — | 17982 | — |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | — | epoch not in this light curve | — | — | 17982 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2 | True | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458629.58734 | -0.01642 | 31 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458644.61498 | -0.01520 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459291.35803 | -0.01443 | 44 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459216.15415 | -0.01295 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458629.55470 | -0.01200 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.36305 | -0.00874 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.48389 | -0.00826 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.42902 | -0.00802 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458616.41725 | -0.00789 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.41305 | -0.00771 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458623.86585 | -0.00765 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.46586 | -0.00739 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458648.36007 | -0.00630 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458644.65872 | -0.00615 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458571.10853 | -0.00610 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | 2459314.41397 | -0.01211 | 2 | PDCSAP | 3 | no |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | 2459314.49036 | -0.01100 | 2 | PDCSAP+SAP | 3 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459301.61934 | -0.01048 | 2 | PDCSAP | 3 | no |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459221.55774 | -0.00799 | 2 | PDCSAP | 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.36725 | -0.00757 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459291.32469 | -0.00756 | 2 | PDCSAP | 1 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459292.61916 | -0.00751 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459292.65667 | -0.00734 | 2 | SAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.56586 | -0.00727 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2021091135823-s0037-0000000281924357-0208-s_lc.fits` | 2459332.43080 | -0.00725 | 2 | PDCSAP | 1 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459292.65250 | -0.00725 | 2 | SAP | 1, 2 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.67420 | -0.00724 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.62697 | -0.00721 | 2 | PDCSAP | 1, 2 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458616.07281 | -0.00710 | 2 | PDCSAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458616.24225 | -0.00706 | 2 | PDCSAP+SAP | 3 | no |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459225.71894 | -0.00698 | 2 | PDCSAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.63244 | -0.00678 | 2 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.71145 | -0.00675 | 2 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.62003 | -0.00651 | 2 | PDCSAP | 1, 2 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458629.54220 | -0.00644 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458644.65317 | -0.00637 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.60743 | -0.00632 | 2 | SAP | 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.37416 | -0.00632 | 2 | PDCSAP | 1 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.46299 | -0.00632 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458575.47527 | -0.00603 | 2 | PDCSAP | 3 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459292.64694 | -0.00602 | 2 | SAP | 1, 2 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.80312 | -0.00599 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.55257 | -0.00599 | 3 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.46993 | -0.00593 | 2 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.54077 | -0.00590 | 2 | SAP | 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.39361 | -0.00581 | 2 | PDCSAP+SAP | 1 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.89340 | -0.00580 | 2 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.36722 | -0.00578 | 2 | PDCSAP | 1 | no |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459216.19651 | -0.00577 | 2 | PDCSAP | 1 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.78244 | -0.00570 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.73298 | -0.00558 | 3 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.78799 | -0.00557 | 2 | SAP | 2, 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458629.53804 | -0.00550 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.54632 | -0.00550 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458588.19766 | -0.00546 | 2 | PDCSAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.49493 | -0.00545 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000281924357-0207-s_lc.fits` | 2459292.41499 | -0.00545 | 2 | SAP | 2 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.74964 | -0.00534 | 5 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.68923 | -0.00521 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.71646 | -0.00520 | 3 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.62827 | -0.00514 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.76091 | -0.00513 | 3 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.74131 | -0.00506 | 5 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.36993 | -0.00506 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458580.01006 | -0.00501 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.71021 | -0.00494 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458589.44768 | -0.00489 | 2 | SAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.58250 | -0.00484 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.63799 | -0.00483 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.59216 | -0.00476 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.73660 | -0.00475 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.48313 | -0.00475 | 3 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.56855 | -0.00475 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.68799 | -0.00474 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.77133 | -0.00473 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.69756 | -0.00463 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.60049 | -0.00462 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.50327 | -0.00461 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.65311 | -0.00459 | 2 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458603.85751 | -0.00458 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458635.32133 | -0.00455 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458589.60810 | -0.00449 | 3 | SAP | 1, 2 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458615.94086 | -0.00446 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.49007 | -0.00446 | 3 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.75258 | -0.00444 | 3 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.55743 | -0.00440 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.65257 | -0.00438 | 3 | SAP | 2, 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458631.80191 | -0.00435 | 2 | SAP | 1, 2, 3 | no |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459216.91736 | -0.00424 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.77048 | -0.00424 | 3 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.34777 | -0.00423 | 2 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.10866 | -0.00421 | 2 | SAP | 1 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458589.35879 | -0.00419 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458633.58107 | -0.00419 | 2 | SAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458620.75753 | -0.00418 | 2 | SAP | 2 | no |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459216.73680 | -0.00417 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458652.86486 | -0.00415 | 3 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.78228 | -0.00410 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458635.25327 | -0.00409 | 2 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458601.51027 | -0.00406 | 2 | SAP | 2 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458652.81972 | -0.00404 | 4 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458592.84355 | -0.00400 | 2 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458603.69918 | -0.00395 | 2 | SAP | 2 | no |
| `tess2019112060037-s0011-0000000281924357-0143-s_lc.fits` | 2458609.49503 | -0.00393 | 2 | SAP | 2 | no |
| `tess2020351194500-s0033-0000000281924357-0203-s_lc.fits` | 2459205.08242 | -0.00392 | 2 | SAP | 2 | no |
| `tess2019085135100-s0010-0000000281924357-0140-s_lc.fits` | 2458579.12672 | -0.00382 | 2 | SAP | 1 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458652.76139 | -0.00379 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458643.16430 | -0.00364 | 2 | SAP | 1 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458652.78639 | -0.00361 | 2 | SAP | 1 | no |
| `tess2019140104343-s0012-0000000281924357-0144-s_lc.fits` | 2458631.90191 | -0.00360 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-830.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:28:44Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:28:46Z: TOI-830.01 (TIC 281924357, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:28:47Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T10:28:47Z: TOI-830.01 (Pl?); TOI-830 (**); ** TOI  830A (*); ** TOI  830B (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2458584.4536: gap (catalogue 17982 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 30%, 20%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-830.01: Gaia DR3 5216790594823376640 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-830.01: Teff 5669 K, R* 1.01 ± 0.08, M* 1.00 ± 0.10, ρ* 0.97 ± 0.25 ρ☉ (dwarf sequence, M_G 4.65, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-830.01: 12 Gaia neighbour(s) within 52.5", contamination 31.20%; depth 17982 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 5216790594823376512, 10.8", ΔG 1.19); a centroid test is needed |
| Pointing and quality census per event | failed | 15 persistent event(s), 5 clean; BJD 2458571.1085 suspect: attitude tweak (within ±0.25 d), manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), MOM_CENTR2 z=-8.8, POS_CORR2 z=-8.7, SAP_BKG z=+28.0; BJD 2458601.3631 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+9.7; BJD 2458601.4131 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+10.1; BJD 2458601.4290 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+9.9 |
| Moving objects at screen-event epochs | passed | 15 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-830.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-830.01: ** TOI  830A otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-830-01.yaml
python -m cygnus.multi report campaigns/toi-830-01.yaml
```
