<!-- [private Drive store] -->
# Known-object test, TOI-764.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-764-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #937, calibrate_screen #713, event_census #720, fetch_products #711, known_signal_recovery #714, moving_objects #904, period_aliases #721, prior_art #939, residual_screen #719, stellar_context #715, variability_guard #938
- Runner finished (UTC): 2026-09-26T10:23:55Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-764.01 (BJD 2458574.5840: recovered, depth 13021 ± 135 ppm (catalogue 13883 ppm)).
Outside the catalogued epoch the screen left 321 threshold entries forming **60 distinct event(s)**, **36 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458580.2155 matches the catalogued transit's depth (12276 vs 13021 ppm), 5.749 d later; 0 of 5 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-764.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 181159386 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 174.302837 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -38.307191 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458574.583993 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13883.4017678 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.5350826 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.1689 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-01-24 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | lightcurve | 10 | True | `32ac6489752631b9` | True |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | lightcurve | 36 | False | `cf954222b83a6bf1` | True |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | lightcurve | 37 | False | `d588d12c16d607d9` | True |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | lightcurve | 63 | False | `9b0d6febb1452cce` | True |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | lightcurve | 90 | False | `b1c71881489dbc3e` | True |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | lightcurve | 99 | False | `db85f2154c0d01a6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458574.58399 | recovered | 196 | 13021 ± 135 | 13883 | -2.83 |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | — | epoch not in this light curve | — | — | 13883 | — |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | — | epoch not in this light curve | — | — | 13883 | — |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 13883 | — |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 13883 | — |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 13883 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2 | True | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461063.77341 | -0.01510 | 171 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460033.22879 | -0.01481 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459295.43874 | -0.01478 | 173 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458580.21553 | -0.01470 | 171 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459289.80669 | -0.01460 | 173 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461046.88597 | -0.01451 | 175 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460021.92168 | -0.01436 | 179 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460748.40481 | -0.01434 | 176 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 2459329.22257 | -0.01434 | 160 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459284.17528 | -0.01430 | 176 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460033.10379 | -0.01418 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460759.66961 | -0.01414 | 173 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461069.40507 | -0.01408 | 178 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460038.80659 | -0.01406 | 173 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460770.93077 | -0.01406 | 169 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459301.07077 | -0.01391 | 175 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460016.29168 | -0.01384 | 172 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460765.30161 | -0.01379 | 173 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458591.47790 | -0.01371 | 173 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 2459312.33120 | -0.01357 | 172 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461052.55657 | -0.01354 | 174 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 2459323.59492 | -0.01339 | 168 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 2459317.96378 | -0.01332 | 170 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460754.02924 | -0.01327 | 157 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458585.82658 | -0.01280 | 139 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458585.94186 | -0.01189 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460754.14452 | -0.01116 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 2459329.33993 | -0.01112 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458585.95575 | -0.01072 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460771.05230 | -0.00872 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458585.72728 | -0.00821 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461063.89912 | -0.00805 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461069.53147 | -0.00763 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461063.90329 | -0.00683 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460016.16806 | -0.00675 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460025.91412 | -0.00554 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460759.54669 | -0.00842 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458579.70512 | -0.00827 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000181159386-0287-s_lc.fits` | 2460754.16050 | -0.00781 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458580.33706 | -0.00769 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461046.75888 | -0.00763 | 2 | PDCSAP+SAP | 3 | no |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459295.31513 | -0.00760 | 3 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458580.08706 | -0.00754 | 2 | SAP | 2, 3 | no |
| `tess2021091135823-s0037-0000000181159386-0208-s_lc.fits` | 2459317.84087 | -0.00736 | 2 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460033.39476 | -0.00731 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460040.66005 | -0.00730 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461073.00810 | -0.00698 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459289.67822 | -0.00693 | 2 | PDCSAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458580.04262 | -0.00673 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461052.93299 | -0.00671 | 2 | PDCSAP | 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458579.97456 | -0.00666 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459295.56583 | -0.00666 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460021.79043 | -0.00642 | 2 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458580.03428 | -0.00639 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000181159386-0300-s_lc.fits` | 2461073.51508 | -0.00633 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000181159386-0207-s_lc.fits` | 2459295.18318 | -0.00619 | 3 | SAP | 1 | no |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460033.33504 | -0.00589 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460033.81004 | -0.00573 | 2 | SAP | 1, 3 | no |
| `tess2023069172124-s0063-0000000181159386-0255-s_lc.fits` | 2460016.41807 | -0.00568 | 2 | SAP | 3 | no |
| `tess2019085135100-s0010-0000000181159386-0140-s_lc.fits` | 2458591.35429 | -0.00560 | 3 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458580.21553 | 12276 | 13021 | 5.7493 | 0 / 5 |  |
| 2458585.82658 | 11671 | 13021 | 11.3604 | 0 / 11 |  |
| 2458585.94186 | 8646 | 13021 | 11.4756 | 0 / 11 |  |
| 2458585.95575 | 7501 | 13021 | 11.4895 | 0 / 11 |  |
| 2458591.47790 | 12875 | 13021 | 17.0117 | 0 / 17 |  |
| 2459284.17528 | 13552 | 13021 | 709.7091 | 11 / 709 | 709.709, 354.854, 236.57, 177.427, 141.942, 118.285, 101.387, 88.7136, 78.8566, 70.9709, 39.4283 |
| 2459289.80669 | 13689 | 13021 | 715.3405 | 13 / 715 | 715.341, 357.67, 238.447, 178.835, 143.068, 119.223, 102.192, 89.4176, 79.4823, 71.534, 65.031, 59.6117, 44.7088 |
| 2459295.43874 | 12301 | 13021 | 720.9725 | 15 / 720 | 720.972, 360.486, 240.324, 180.243, 144.195, 120.162, 90.1216, 80.1081, 72.0973, 60.081, 48.0648, 45.0608, 42.4101, 40.054, 37.9459 |
| 2459301.07077 | 13366 | 13021 | 726.6045 | 0 / 726 |  |
| 2459312.33120 | 12728 | 13021 | 737.8650 | 13 / 737 | 737.865, 368.933, 245.955, 184.466, 147.573, 122.978, 105.409, 81.985, 73.7865, 67.0786, 61.4887, 49.191, 40.9925 |
| 2459317.96378 | 12682 | 13021 | 743.4976 | 12 / 743 | 743.498, 371.749, 247.833, 185.874, 148.7, 123.916, 106.214, 92.9372, 82.6108, 74.3498, 67.5907, 61.9581 |
| 2459323.59492 | 12922 | 13021 | 749.1287 | 8 / 749 | 749.129, 374.564, 187.282, 149.826, 107.018, 93.6411, 68.1026, 39.4278 |
| 2459329.22257 | 13356 | 13021 | 754.7563 | 7 / 754 | 754.756, 377.378, 251.585, 188.689, 150.951, 125.793, 94.3445 |
| 2459329.33993 | 8435 | 13021 | 754.8737 | 8 / 754 | 754.874, 377.437, 251.625, 188.718, 150.975, 125.812, 94.3592, 62.9061 |
| 2460016.29168 | 13319 | 13021 | 1441.8255 | 24 / 1441 | 1441.83, 720.913, 480.608, 360.456, 288.365, 240.304, 180.228, 160.203, 144.183, 120.152, 110.91, 90.1141, 84.8133, 80.1014, 75.8856, 72.0913, 60.0761, 45.057, 42.4066, 40.0507 |
| 2460021.92168 | 12603 | 13021 | 1447.4555 | 12 / 1447 | 1447.46, 482.485, 289.491, 206.779, 160.828, 131.587, 111.343, 96.497, 85.1444, 76.1819, 68.9265, 5.6321 |
| 2460033.10379 | 11635 | 13021 | 1458.6376 | 14 / 1458 | 1458.64, 486.212, 291.728, 208.377, 162.071, 132.603, 112.203, 97.2425, 85.8022, 76.7704, 69.4589, 58.3455, 39.4226, 5.6318 |
| 2460033.22879 | 12837 | 13021 | 1458.7626 | 13 / 1458 | 1458.76, 486.254, 291.752, 208.395, 162.085, 132.615, 112.213, 97.2508, 85.8096, 76.777, 69.4649, 58.3505, 39.426 |
| 2460038.80659 | 12979 | 13021 | 1464.3404 | 38 / 1464 | 1464.34, 732.17, 488.113, 366.085, 292.868, 244.057, 209.191, 183.042, 162.704, 146.434, 133.122, 122.028, 112.642, 104.596, 97.6227, 91.5213, 81.3522, 77.0705, 73.217, 69.7305 |
| 2460748.40481 | 13225 | 13021 | 2173.9386 | 23 / 2173 | 2173.94, 1086.97, 543.485, 434.788, 310.563, 271.742, 217.394, 197.631, 167.226, 155.281, 135.871, 127.879, 114.418, 108.697, 98.8154, 86.9575, 77.6407, 70.1271, 62.1125, 58.7551 |
| 2460754.02924 | 12018 | 13021 | 2179.5630 | 36 / 2179 | 2179.56, 1089.78, 726.521, 544.891, 435.913, 363.26, 272.445, 242.174, 217.956, 198.142, 181.63, 167.659, 145.304, 136.223, 128.21, 121.087, 114.714, 108.978, 90.8151, 87.1825 |
| 2460754.14452 | 8961 | 13021 | 2179.6783 | 35 / 2179 | 2179.68, 1089.84, 726.559, 544.92, 435.936, 363.28, 272.46, 242.186, 217.968, 198.153, 181.64, 167.668, 145.312, 136.23, 128.216, 121.093, 114.72, 108.984, 94.7686, 90.8199 |
| 2460759.66961 | 12766 | 13021 | 2185.2034 | 22 / 2185 | 2185.2, 1092.6, 546.301, 437.041, 273.15, 218.52, 198.655, 168.093, 136.575, 128.541, 115.011, 109.26, 99.3274, 95.0088, 87.4081, 70.4904, 64.2707, 53.2976, 49.6637, 22.5279 |
| 2460765.30161 | 12897 | 13021 | 2190.8354 | 19 / 2190 | 2190.84, 1095.42, 547.709, 438.167, 312.976, 273.854, 219.083, 199.167, 168.526, 156.488, 136.927, 128.873, 115.307, 109.542, 87.6334, 84.2629, 78.2441, 44.7109, 5.632 |
| 2460770.93077 | 12875 | 13021 | 2196.4646 | 45 / 2196 | 2196.46, 1098.23, 732.155, 549.116, 439.293, 366.077, 313.781, 274.558, 244.052, 219.647, 199.679, 183.039, 168.959, 156.89, 146.431, 137.279, 129.204, 122.026, 115.603, 109.823 |
| 2460771.05230 | 7201 | 13021 | 2196.5861 | 40 / 2196 | 2196.59, 1098.29, 732.195, 549.146, 439.317, 366.098, 313.798, 274.573, 244.065, 219.659, 199.69, 183.049, 168.968, 156.899, 137.287, 129.211, 122.033, 115.61, 109.829, 104.599 |
| 2461046.88597 | 13334 | 13021 | 2472.4198 | 19 / 2472 | 2472.42, 1236.21, 824.14, 618.105, 494.484, 412.07, 353.203, 309.053, 224.765, 190.186, 176.601, 164.828, 154.526, 130.127, 117.734, 88.3007, 77.2631, 44.9531, 5.6319 |
| 2461052.55657 | 11875 | 13021 | 2478.0903 | 27 / 2478 | 2478.09, 1239.05, 826.03, 619.523, 495.618, 413.015, 309.761, 275.343, 247.809, 225.281, 190.622, 165.206, 154.881, 137.672, 130.426, 123.904, 112.641, 82.603, 79.9384, 77.4403 |
| 2461063.77341 | 14071 | 13021 | 2489.3072 | 25 / 2489 | 2489.31, 1244.65, 829.769, 622.327, 497.861, 414.885, 276.59, 248.931, 226.301, 191.485, 165.954, 146.43, 138.295, 124.465, 113.15, 95.7426, 82.9769, 73.2149, 63.8284, 55.3179 |
| 2461069.40507 | 13621 | 13021 | 2494.9389 | 23 / 2494 | 2494.94, 1247.47, 831.646, 623.735, 498.988, 415.823, 277.215, 226.813, 191.918, 166.329, 146.761, 138.608, 113.406, 108.476, 95.9592, 73.3806, 54.2378, 48.9204, 47.9796, 36.6903 |
| 2461069.53147 | 6742 | 13021 | 2495.0653 | 21 / 2495 | 2495.07, 1247.53, 831.688, 623.766, 499.013, 415.844, 277.229, 226.824, 191.928, 166.338, 146.768, 138.615, 113.412, 108.481, 95.964, 73.3843, 48.9228, 47.982, 36.6921, 29.3537 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-764.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:23:52Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:23:53Z: TOI-764.01 (TIC 181159386, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:23:54Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:23:55Z: TOI-764.01 (err); TOI-764b (Pl); TOI-764 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458574.5840: recovered, depth 13021 ± 135 ppm (catalogue 13883 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 20%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 31 repeat-candidate event(s); first at BJD 2458580.2155, ΔT = 5.749 d, 0 of 5 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-764.01: Gaia DR3 5385762893242980992 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-764.01: dwarf priors not applied — 1.61 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-764.01: 15 Gaia neighbour(s) within 52.5", contamination 2.61%; depth 13021 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 36 persistent event(s), 15 clean; BJD 2458585.7273 suspect: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), SAP_BKG z=+12.2; BJD 2458585.8266 suspect: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), SAP_BKG z=+43.6; BJD 2458585.9419 suspect: coarse point (in event), manual exclude (in event), momentum dump (in event), SAP_BKG z=+11.2; BJD 2458585.9558 suspect: manual exclude (in event), coarse point (within ±0.25 d), momentum dump (within ±0.25 d), SAP_BKG z=+12.7 |
| Moving objects at screen-event epochs | inconclusive | 36 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 10 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-764.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-764.01: TOI-764 otype SB* (multiple) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-764-01.yaml
python -m cygnus.multi report campaigns/toi-764-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** No new signal.

Source: `campaigns/toi-764-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
