<!-- cygnus:generated-draft -->
# Known-object test, TOI-4882.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4882-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4808, calibrate_screen #4796, event_census #4803, fetch_independent #4806, fetch_products #4791, known_signal_recovery #4799, moving_objects #4805, period_aliases #4804, prior_art #4812, residual_screen #4802, stellar_context #4800, variability_guard #4809
- Runner finished (UTC): 2026-09-30T22:25:41Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4882.01 (BJD 2460017.1806: not recovered, depth 4228 ± 677 ppm (catalogue 7040 ppm); BJD 2460021.6166: not recovered, depth 7004 ± 792 ppm (catalogue 7040 ppm); BJD 2460026.0527: not recovered, depth 5982 ± 735 ppm (catalogue 7040 ppm); BJD 2460030.4887: not recovered, depth 8312 ± 667 ppm (catalogue 7040 ppm); BJD 2460034.9247: not recovered, depth 5946 ± 829 ppm (catalogue 7040 ppm); BJD 2460039.3608: not recovered, depth 7031 ± 884 ppm (catalogue 7040 ppm); BJD 2460043.7968: partial, depth 5088 ± 621 ppm (catalogue 7040 ppm); BJD 2460048.2329: gap (catalogue 7040 ppm); BJD 2460052.6689: partial, depth 8380 ± 596 ppm (catalogue 7040 ppm); BJD 2460057.1050: partial, depth 10666 ± 600 ppm (catalogue 7040 ppm); BJD 2460061.5410: recovered, depth 9288 ± 697 ppm (catalogue 7040 ppm); BJD 2460065.9770: not recovered, depth 5371 ± 650 ppm (catalogue 7040 ppm)).
Outside the catalogued epoch the screen left 206 threshold entries forming **83 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460067.7236 matches the catalogued transit's depth (6304 vs 9288 ppm), 6.173 d later; 0 of 6 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4882.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 458331312 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 159.546802 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -54.579059 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459329.594358 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.4360402 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 7040.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.438 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.2673 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | lightcurve | 63 | False | `f62308eae0bf2605` | True |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | lightcurve | 64 | False | `839d90f172a22d7d` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460017.18059 | not_recovered | 74 | 4228 ± 677 | 7040 | — |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460021.61663 | not_recovered | 73 | 7004 ± 792 | 7040 | — |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460026.05267 | not_recovered | 73 | 5982 ± 735 | 7040 | — |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460030.48871 | not_recovered | 73 | 8312 ± 667 | 7040 | — |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460034.92475 | not_recovered | 73 | 5946 ± 829 | 7040 | — |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460039.36079 | not_recovered | 71 | 7031 ± 884 | 7040 | — |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460043.79683 | partial | 73 | 5088 ± 621 | 7040 | -0.28 |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.23287 | gap | 0 | — | 7040 | — |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460052.66891 | partial | 73 | 8380 ± 596 | 7040 | -0.58 |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460057.10495 | partial | 73 | 10666 ± 600 | 7040 | -0.05 |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.54099 | recovered | 70 | 9288 ± 697 | 7040 | 0.22 |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460065.97703 | not_recovered | 73 | 5371 ± 650 | 7040 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: —, 4h: —, 8h: — |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.72356 | -0.02029 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460014.75627 | -0.02654 | 5 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460014.76391 | -0.02316 | 2 | SAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460014.79377 | -0.02212 | 5 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.93189 | -0.01930 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460014.77849 | -0.01744 | 7 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.89994 | -0.01662 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.12393 | -0.01586 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.87356 | -0.01538 | 2 | PDCSAP | 1, 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.94451 | -0.01481 | 2 | PDCSAP | 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.61106 | -0.01479 | 2 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.15448 | -0.01345 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.71837 | -0.01342 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.66976 | -0.01320 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.81687 | -0.01303 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460034.07252 | -0.01285 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460034.03641 | -0.01210 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460033.81002 | -0.01207 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.28087 | -0.01180 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.33365 | -0.01164 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.71549 | -0.01135 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460034.05169 | -0.01132 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.81271 | -0.01132 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460033.95308 | -0.01126 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.03897 | -0.01077 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.25690 | -0.01073 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.40690 | -0.01070 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.95286 | -0.01067 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.96675 | -0.01049 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.08066 | -0.01015 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.84812 | -0.00996 | 3 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.95689 | -0.00986 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000458331312-0255-s_lc.fits` | 2460040.83920 | -0.00971 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.44743 | -0.00969 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.67521 | -0.00945 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.92786 | -0.00932 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.07230 | -0.00932 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.17924 | -0.00915 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.00980 | -0.00910 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.40653 | -0.00907 | 29 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.11952 | -0.00906 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.87659 | -0.00904 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.70576 | -0.00897 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460066.75553 | -0.00886 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.09857 | -0.00878 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460062.05355 | -0.00873 | 3 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460066.80136 | -0.00863 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.53292 | -0.00862 | 39 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.38917 | -0.00860 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460066.98608 | -0.00859 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460066.81664 | -0.00855 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.39472 | -0.00845 | 4 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.49681 | -0.00844 | 46 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460066.82775 | -0.00842 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.66069 | -0.00833 | 3 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.71965 | -0.00810 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.65028 | -0.00806 | 7 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.01108 | -0.00799 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.59750 | -0.00783 | 52 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.76694 | -0.00755 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.67458 | -0.00755 | 7 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.64056 | -0.00755 | 8 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.71278 | -0.00735 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.68500 | -0.00733 | 6 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.29718 | -0.00731 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.12232 | -0.00723 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.69472 | -0.00708 | 6 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460066.66803 | -0.00694 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.64326 | -0.00685 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.72458 | -0.00685 | 3 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.74889 | -0.00680 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.78222 | -0.00678 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.80722 | -0.00673 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.65438 | -0.00672 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460067.51940 | -0.00671 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.70375 | -0.00668 | 5 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.86062 | -0.00660 | 4 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460048.73222 | -0.00625 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.78354 | -0.00619 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.89326 | -0.00610 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460061.02094 | -0.00603 | 2 | SAP | 1, 2 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460060.87927 | -0.00600 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000458331312-0257-s_lc.fits` | 2460054.56688 | -0.00597 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460067.72356 | 6304 | 9288 | 6.1735 | 0 / 6 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4882.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:25:28Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:25:31Z: TOI-4882.01 (TIC 458331312, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:25:34Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:25:37Z: TYC 8605-2322-1 (*); TYC 8605-509-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460017.1806: not recovered, depth 4228 ± 677 ppm (catalogue 7040 ppm); BJD 2460021.6166: not recovered, depth 7004 ± 792 ppm (catalogue 7040 ppm); BJD 2460026.0527: not recovered, depth 5982 ± 735 ppm (catalogue 7040 ppm); BJD 2460030.4887: not recovered, depth 8312 ± 667 ppm (catalogue 7040 ppm); BJD 2460034.9247: not recovered, depth 5946 ± 829 ppm (catalogue 7040 ppm); BJD 2460039.3608: not recovered, depth 7031 ± 884 ppm (catalogue 7040 ppm); BJD 2460043.7968: partial, depth 5088 ± 621 ppm (catalogue 7040 ppm); BJD 2460048.2329: gap (catalogue 7040 ppm); BJD 2460052.6689: partial, depth 8380 ± 596 ppm (catalogue 7040 ppm); BJD 2460057.1050: partial, depth 10666 ± 600 ppm (catalogue 7040 ppm); BJD 2460061.5410: recovered, depth 9288 ± 697 ppm (catalogue 7040 ppm); BJD 2460065.9770: not recovered, depth 5371 ± 650 ppm (catalogue 7040 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460067.7236, ΔT = 6.173 d, 0 of 6 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4882.01: Gaia DR3 5353787858173613056 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4882.01: Teff 6280 K, R* 1.36 ± 0.11, M* 1.25 ± 0.12, ρ* 0.50 ± 0.13 ρ☉ (dwarf sequence, M_G 3.56, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4882.01: 130 Gaia neighbour(s) within 52.5", contamination 73.36%; depth 9288 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 5353787858185932800, 13.1", ΔG -0.91); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460067.7236 suspect: manual exclude (in event), SAP_BKG z=+15.4 |
| Moving objects at screen-event epochs | not_tested | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-4882.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4882.01: TYC 8605-2322-1 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4882-01.yaml
python -m cygnus.multi report campaigns/toi-4882-01.yaml
```
