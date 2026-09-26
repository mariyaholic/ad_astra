<!-- [private Drive store] -->
# Known-object test, TOI-668.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-668-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #342, calibrate_screen #222, event_census #234, fetch_products #218, known_signal_recovery #223, moving_objects #330, period_aliases #235, prior_art #344, residual_screen #230, stellar_context #225, variability_guard #343
- Runner finished (UTC): 2026-09-26T10:03:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-668.01 (BJD 2459283.0656: recovered, depth 27135 ± 333 ppm (catalogue 30199 ppm)).
Outside the catalogued epoch the screen left 735 threshold entries forming **179 distinct event(s)**, **37 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459287.4436 matches the catalogued transit's depth (26397 vs 27135 ppm), 4.379 d later; 0 of 4 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-668.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 102195674 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 154.191741 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -42.559071 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459283.065609 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 30199.2684097 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.827504 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.3425 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | lightcurve | 36 | True | `a922e6dd3fe5d6a7` | True |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | lightcurve | 9 | False | `c7e6122f61ebfe66` | True |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | lightcurve | 63 | False | `eead01e3e342935f` | True |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | lightcurve | 90 | False | `2c1933d68e3c42e4` | True |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | lightcurve | 99 | False | `0fd424609ecf7763` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459283.06561 | recovered | 115 | 27135 ± 333 | 30199 | -0.03 |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | — | epoch not in this light curve | — | — | 30199 | — |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 30199 | — |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 30199 | — |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 30199 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 4 | False | 1h: —, 2h: 20000, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.57227 | -0.03263 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458564.97585 | -0.03160 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.55213 | -0.03139 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459300.57830 | -0.03079 | 99 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460036.18555 | -0.03048 | 100 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461069.53472 | -0.02987 | 101 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.50769 | -0.02973 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.58130 | -0.02967 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460771.78950 | -0.02883 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.59519 | -0.02855 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461047.64388 | -0.02852 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459287.44360 | -0.02838 | 101 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460767.41250 | -0.02785 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460763.03062 | -0.02757 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459291.82486 | -0.02755 | 98 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.60005 | -0.02723 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460018.66896 | -0.02718 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458560.59807 | -0.02695 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460027.38077 | -0.02685 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458547.46115 | -0.02662 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460031.80643 | -0.02662 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459304.96019 | -0.02595 | 97 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460023.04953 | -0.02587 | 98 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459296.20332 | -0.02569 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460754.27650 | -0.02554 | 101 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460749.89733 | -0.02551 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458551.83969 | -0.02498 | 101 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461065.15464 | -0.02474 | 97 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461052.02124 | -0.02464 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.50352 | -0.02193 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460014.75713 | -0.02053 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461047.70986 | -0.01863 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.75993 | -0.01699 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460014.77866 | -0.01528 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.61167 | -0.01493 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.44808 | -0.01367 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460014.77171 | -0.01083 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.56741 | -0.02974 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.60491 | -0.02402 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.53130 | -0.02378 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.72933 | -0.01787 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.79104 | -0.01778 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.71131 | -0.01763 | 11 | PDCSAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.12437 | -0.01645 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461069.31527 | -0.01606 | 2 | PDCSAP | 2 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.70298 | -0.01580 | 4 | PDCSAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.95363 | -0.01544 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459303.60535 | -0.01521 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.62000 | -0.01504 | 5 | SAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458545.31110 | -0.01476 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.01057 | -0.01468 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.43042 | -0.01464 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.49708 | -0.01442 | 6 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.74673 | -0.01438 | 3 | PDCSAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.77516 | -0.01435 | 3 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459282.44146 | -0.01429 | 2 | PDCSAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.02168 | -0.01404 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.90363 | -0.01388 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.68002 | -0.01377 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.81058 | -0.01370 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.08131 | -0.01368 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.89808 | -0.01364 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.13193 | -0.01362 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.69658 | -0.01360 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.83141 | -0.01356 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.65958 | -0.01354 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.66882 | -0.01349 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.04999 | -0.01341 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.99669 | -0.01338 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.88835 | -0.01337 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.86335 | -0.01327 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.77854 | -0.01318 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.07307 | -0.01317 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.17360 | -0.01316 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.85502 | -0.01309 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.67019 | -0.01307 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459303.34146 | -0.01307 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.46327 | -0.01304 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.32486 | -0.01302 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458566.61265 | -0.01301 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.48458 | -0.01294 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.55819 | -0.01279 | 4 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.68284 | -0.01277 | 3 | PDCSAP | 1, 2 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.75819 | -0.01272 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.54222 | -0.01272 | 3 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.69673 | -0.01272 | 3 | PDCSAP | 1, 2 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.38250 | -0.01271 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.95919 | -0.01256 | 4 | SAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458553.83832 | -0.01254 | 3 | PDCSAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.43875 | -0.01254 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460027.36202 | -0.01252 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.81613 | -0.01250 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.03696 | -0.01234 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.40492 | -0.01232 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.62438 | -0.01225 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000102195674-0139-s_lc.fits` | 2458560.66682 | -0.01204 | 2 | PDCSAP | 1 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.13749 | -0.01200 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.67486 | -0.01199 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.72520 | -0.01196 | 2 | PDCSAP | 1 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459296.13596 | -0.01195 | 2 | PDCSAP | 1, 2 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.17846 | -0.01193 | 3 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.43458 | -0.01191 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.74014 | -0.01189 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.04113 | -0.01182 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.71880 | -0.01179 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.20770 | -0.01179 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.25542 | -0.01179 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.08888 | -0.01176 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.76326 | -0.01172 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460014.79463 | -0.01170 | 4 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.75632 | -0.01161 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460038.92022 | -0.01157 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.64986 | -0.01147 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.28270 | -0.01146 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.01543 | -0.01135 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.87863 | -0.01130 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460027.35785 | -0.01128 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.73076 | -0.01118 | 4 | PDCSAP | 1 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.64669 | -0.01089 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.76752 | -0.01087 | 4 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.49521 | -0.01082 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.31792 | -0.01081 | 6 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.60264 | -0.01076 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.97932 | -0.01076 | 4 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.08418 | -0.01074 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.74430 | -0.01071 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459299.83455 | -0.01064 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.09652 | -0.01060 | 5 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.19708 | -0.01057 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.03687 | -0.01052 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.76236 | -0.01039 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.04530 | -0.01033 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460014.92727 | -0.01033 | 2 | PDCSAP | 1, 2 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.12568 | -0.01031 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.66474 | -0.01023 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.19292 | -0.01016 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.91335 | -0.01011 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.21327 | -0.00999 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.83963 | -0.00993 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.84252 | -0.00992 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.82585 | -0.00983 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.42716 | -0.00968 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.86602 | -0.00967 | 2 | SAP | 1 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.69569 | -0.00961 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.59778 | -0.00960 | 3 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.11943 | -0.00958 | 4 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.06127 | -0.00957 | 7 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.14721 | -0.00954 | 7 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.80433 | -0.00952 | 3 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.58111 | -0.00952 | 3 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.64014 | -0.00950 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.36167 | -0.00947 | 3 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.45680 | -0.00945 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.41722 | -0.00941 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460040.46880 | -0.00938 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460033.87308 | -0.00935 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.65771 | -0.00931 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460034.05293 | -0.00924 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460021.90439 | -0.00921 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460021.76620 | -0.00921 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.37160 | -0.00921 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.37139 | -0.00915 | 3 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.47555 | -0.00895 | 3 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.73319 | -0.00892 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460039.90770 | -0.00891 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460021.77314 | -0.00890 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.15693 | -0.00887 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459298.94289 | -0.00875 | 2 | SAP | 1 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.85125 | -0.00872 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000102195674-0207-s_lc.fits` | 2459292.67903 | -0.00871 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460021.68564 | -0.00868 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460032.88836 | -0.00867 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460767.34861 | -0.00867 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.16596 | -0.00854 | 3 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460768.04583 | -0.00849 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000102195674-0287-s_lc.fits` | 2460754.11122 | -0.00845 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000102195674-0255-s_lc.fits` | 2460024.52314 | -0.00840 | 2 | SAP | 1, 2 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461052.96158 | -0.00592 | 2 | SAP | 2 | no |
| `tess2026005125623-s0099-0000000102195674-0300-s_lc.fits` | 2461073.46408 | -0.00522 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459287.44360 | 26397 | 27135 | 4.3792 | 0 / 4 |  |
| 2459291.82486 | 26915 | 27135 | 8.7605 | 0 / 8 |  |
| 2459296.20332 | 22944 | 27135 | 13.1389 | 0 / 13 |  |
| 2459300.57830 | 28790 | 27135 | 17.5139 | 2 / 17 | 17.5139, 8.757 |
| 2459304.96019 | 22632 | 27135 | 21.8958 | 0 / 21 |  |
| 2458547.46115 | 25242 | 27135 | 735.6032 | 24 / 735 | 735.603, 367.802, 245.201, 183.901, 122.6, 105.086, 91.9504, 81.7337, 66.873, 61.3003, 56.5849, 52.5431, 45.9752, 43.2708, 40.8668, 35.0287, 31.9827, 30.6501, 26.2715, 25.3656 |
| 2458551.83969 | 23246 | 27135 | 731.2247 | 17 / 731 | 731.225, 365.612, 243.742, 182.806, 146.245, 121.871, 104.461, 91.4031, 73.1225, 66.475, 56.2481, 52.2303, 48.7483, 36.5612, 34.8202, 33.2375, 29.249 |
| 2458560.59807 | 24557 | 27135 | 722.4663 | 17 / 722 | 722.466, 361.233, 240.822, 180.617, 144.493, 120.411, 103.21, 90.3083, 72.2466, 65.6788, 60.2055, 55.5743, 51.6047, 48.1644, 45.1541, 21.8929, 13.1358 |
| 2458564.97585 | 28290 | 27135 | 718.0885 | 15 / 718 | 718.088, 359.044, 239.363, 179.522, 143.618, 119.681, 102.584, 89.7611, 79.7876, 71.8089, 65.2808, 59.8407, 39.8938, 17.5144, 8.7572 |
| 2460018.66896 | 25929 | 27135 | 735.6046 | 24 / 735 | 735.605, 367.802, 245.202, 183.901, 122.601, 105.086, 91.9506, 81.7338, 66.8731, 61.3004, 56.585, 52.5432, 45.9753, 43.2709, 40.8669, 35.0288, 31.9828, 30.6502, 26.2716, 25.3657 |
| 2460023.04953 | 24412 | 27135 | 739.9851 | 20 / 739 | 739.985, 369.993, 246.662, 184.996, 147.997, 123.331, 105.712, 92.4981, 82.2206, 73.9985, 67.2714, 56.9219, 52.8561, 49.3323, 46.2491, 38.9466, 36.9993, 35.2374, 29.5994, 28.461 |
| 2460031.80643 | 25480 | 27135 | 748.7420 | 18 / 748 | 748.742, 374.371, 249.581, 187.185, 149.748, 124.79, 106.963, 93.5928, 83.1936, 74.8742, 68.0675, 62.3952, 49.9161, 46.7964, 44.0436, 39.4075, 37.4371, 13.1358 |
| 2460036.18555 | 27413 | 27135 | 753.1212 | 15 / 753 | 753.121, 376.561, 251.04, 188.28, 150.624, 125.52, 107.589, 83.6801, 75.3121, 62.7601, 57.9324, 53.7944, 50.2081, 17.5144, 8.7572 |
| 2460040.50352 | 16434 | 27135 | 757.4391 | 9 / 757 | 757.439, 378.72, 189.36, 151.488, 108.206, 94.6799, 75.7439, 68.8581, 58.2645 |
| 2460040.50769 | 17234 | 27135 | 757.4433 | 9 / 757 | 757.443, 378.722, 189.361, 151.489, 108.206, 94.6804, 75.7443, 68.8585, 58.2649 |
| 2460040.55213 | 24868 | 27135 | 757.4877 | 9 / 757 | 757.488, 378.744, 189.372, 151.498, 108.213, 94.686, 75.7488, 68.8625, 58.2683 |
| 2460040.57227 | 24146 | 27135 | 757.5079 | 9 / 757 | 757.508, 378.754, 189.377, 151.502, 108.215, 94.6885, 75.7508, 68.8644, 58.2698 |
| 2460040.58130 | 24860 | 27135 | 757.5169 | 10 / 757 | 757.517, 378.759, 189.379, 151.503, 108.217, 94.6896, 75.7517, 68.8652, 58.2705, 4.3787 |
| 2460040.59519 | 21200 | 27135 | 757.5308 | 9 / 757 | 757.531, 378.765, 189.383, 151.506, 108.219, 94.6914, 75.7531, 68.8664, 58.2716 |
| 2460040.60005 | 21160 | 27135 | 757.5357 | 9 / 757 | 757.536, 378.768, 189.384, 151.507, 108.219, 94.692, 75.7536, 68.8669, 58.272 |
| 2460749.89733 | 24448 | 27135 | 1466.8329 | 14 / 1466 | 1466.83, 488.944, 293.367, 209.548, 162.981, 133.348, 112.833, 97.7889, 86.2843, 77.2017, 69.8492, 58.6733, 54.3271, 21.893 |
| 2460754.27650 | 23495 | 27135 | 1471.2121 | 36 / 1471 | 1471.21, 735.606, 490.404, 367.803, 245.202, 210.173, 183.901, 163.468, 133.747, 122.601, 113.17, 105.087, 91.9508, 86.5419, 81.734, 70.0577, 66.8733, 63.9657, 61.3005, 56.5851 |
| 2460763.03062 | 25558 | 27135 | 1479.9662 | 35 / 1479 | 1479.97, 739.983, 493.322, 369.992, 295.993, 246.661, 211.424, 184.996, 164.441, 147.997, 134.542, 123.331, 113.844, 105.712, 98.6644, 92.4979, 87.0568, 82.2203, 77.893, 73.9983 |
| 2460767.41250 | 25129 | 27135 | 1484.3481 | 10 / 1484 | 1484.35, 494.783, 212.05, 164.928, 134.941, 114.181, 87.3146, 78.1236, 64.5369, 13.1358 |
| 2460771.78950 | 27070 | 27135 | 1488.7251 | 35 / 1488 | 1488.73, 744.363, 496.242, 372.181, 297.745, 248.121, 212.675, 186.091, 165.414, 148.873, 135.339, 124.06, 114.517, 106.338, 99.2483, 87.5721, 82.707, 78.354, 74.4363, 67.6693 |
| 2461047.64388 | 25832 | 27135 | 1764.5795 | 18 / 1764 | 1764.58, 882.29, 588.193, 441.145, 352.916, 220.572, 196.064, 176.458, 160.416, 135.737, 117.639, 110.286, 103.799, 88.229, 76.7208, 56.9219, 51.8994, 28.461 |
| 2461052.02124 | 23174 | 27135 | 1768.9569 | 21 / 1768 | 1768.96, 884.478, 589.652, 442.239, 353.791, 252.708, 221.12, 196.551, 176.896, 160.814, 136.074, 126.354, 117.93, 110.56, 88.4478, 84.236, 76.9112, 63.177, 45.3579, 17.5144 |
| 2461065.15464 | 22176 | 27135 | 1782.0903 | 22 / 1782 | 1782.09, 891.045, 594.03, 445.523, 356.418, 254.584, 222.761, 198.01, 178.209, 162.008, 137.084, 127.292, 118.806, 111.381, 89.1045, 84.8614, 71.2836, 66.0033, 63.6461, 50.9169 |
| 2461069.53472 | 26925 | 27135 | 1786.4703 | 28 / 1786 | 1786.47, 893.235, 595.49, 446.618, 297.745, 255.21, 223.309, 198.497, 162.406, 148.873, 137.421, 127.605, 111.654, 105.087, 99.2484, 85.07, 77.6726, 74.4363, 55.8272, 54.1355 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-668.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:03:20Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:03:22Z: TOI-668.01 (TIC 102195674, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:03:23Z: Gaia DR3 5416752491036144000 (type RS, P — d)
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:03:23Z: TYC 7716-2066-1 (*); TOI-668.01 (err); TOI-668 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459283.0656: recovered, depth 27135 ± 333 ppm (catalogue 30199 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10%, 10%, 10%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 29 repeat-candidate event(s); first at BJD 2459287.4436, ΔT = 4.379 d, 0 of 4 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-668.01: Gaia DR3 5416752486737577984 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-668.01: Teff 6004 K, R* 1.19 ± 0.10, M* 1.15 ± 0.11, ρ* 0.69 ± 0.18 ρ☉ (dwarf sequence, M_G 4.02, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-668.01: 37 Gaia neighbour(s) within 52.5", contamination 64.70%; depth 27135 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 5416752525397369600, 18.6", ΔG -0.59); a centroid test is needed |
| Pointing and quality census per event | failed | 37 persistent event(s), 4 clean; BJD 2459287.4436 suspect: MOM_CENTR1 z=+8.3; BJD 2459292.6117 suspect: MOM_CENTR1 z=-5.7, POS_CORR2 z=+8.5, SAP_BKG z=+10.2; BJD 2459296.2033 suspect: MOM_CENTR1 z=+7.7, SAP_BKG z=-10.9; BJD 2459300.5783 suspect: MOM_CENTR1 z=+8.5 |
| Moving objects at screen-event epochs | inconclusive | 37 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 5 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-668.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-668.01: TOI-668 otype SB* (multiple) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-668-01.yaml
python -m cygnus.multi report campaigns/toi-668-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit.** The joint period (4.3786 d) is the catalogued period (4.3787 d); the phase-0.5 dip at P 4.38 d is the catalogued EB's secondary eclipse. No new signal.

Source: `campaigns/toi-668-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
