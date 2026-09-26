<!-- cygnus:generated-draft -->
# Known-object test, TOI-760.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-760-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #613, calibrate_screen #456, event_census #474, fetch_products #455, known_signal_recovery #459, moving_objects #599, period_aliases #475, prior_art #615, residual_screen #466, stellar_context #460, variability_guard #614
- Runner finished (UTC): 2026-09-26T10:11:49Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-760.01 (BJD 2458578.6663: recovered, depth 11386 ± 107 ppm (catalogue 13386 ppm)).
Outside the catalogued epoch the screen left 209 threshold entries forming **65 distinct event(s)**, **14 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458591.0129 matches the catalogued transit's depth (12040 vs 11386 ppm), 12.251 d later; 0 of 12 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-760.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 162362398 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 169.414385 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -44.017088 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458578.666284 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13386.1311036 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.2659032 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.6171 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-01-24 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | lightcurve | 10 | True | `a974d59977e41e16` | True |
| `tess2021065132309-s0036-0000000162362398-0207-s_lc.fits` | lightcurve | 36 | False | `17f503f6d945f55d` | True |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | lightcurve | 37 | False | `9e52df3369853c87` | True |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | lightcurve | 63 | False | `04bdcae232974788` | True |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | lightcurve | 90 | False | `e5127ca0bd4397a0` | True |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | lightcurve | 99 | False | `d8ae2b44553f94c6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 2458578.66628 | recovered | 188 | 11386 ± 107 | 13386 | 2.29 |
| `tess2021065132309-s0036-0000000162362398-0207-s_lc.fits` | — | epoch not in this light curve | — | — | 13386 | — |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | — | epoch not in this light curve | — | — | 13386 | — |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 13386 | — |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 13386 | — |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 13386 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2021065132309-s0036-0000000162362398-0207-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460750.45792 | -0.01314 | 151 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461071.29391 | -0.01310 | 152 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 2458591.01289 | -0.01284 | 154 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460022.38794 | -0.01275 | 155 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460762.80393 | -0.01273 | 155 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 2459331.38736 | -0.01253 | 150 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461046.60608 | -0.01253 | 156 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.73599 | -0.01130 | 146 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 2459318.99318 | -0.00828 | 43 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 2459318.96402 | -0.00777 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461071.18487 | -0.00585 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461072.52454 | -0.00550 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460750.34889 | -0.00535 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460027.82066 | -0.00430 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.42061 | -0.00757 | 3 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.44700 | -0.00691 | 7 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461073.20792 | -0.00687 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461072.56899 | -0.00675 | 2 | SAP | 1, 2 | no |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 2459331.27834 | -0.00622 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.41159 | -0.00617 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.49631 | -0.00607 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.50047 | -0.00596 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.43520 | -0.00584 | 9 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000162362398-0207-s_lc.fits` | 2459305.20021 | -0.00575 | 2 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.46714 | -0.00570 | 13 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.55186 | -0.00563 | 2 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 2458580.68106 | -0.00561 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.34224 | -0.00560 | 4 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.51992 | -0.00553 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.51020 | -0.00551 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.45742 | -0.00550 | 6 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461046.49219 | -0.00532 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461072.72316 | -0.00525 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461071.40225 | -0.00520 | 2 | PDCSAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 2458595.39335 | -0.00515 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.49145 | -0.00514 | 3 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000162362398-0207-s_lc.fits` | 2459299.58906 | -0.00509 | 2 | SAP | 3 | no |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 2459308.56479 | -0.00509 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460750.56556 | -0.00508 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.33321 | -0.00507 | 5 | SAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000162362398-0140-s_lc.fits` | 2458590.89761 | -0.00503 | 2 | PDCSAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.50603 | -0.00502 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.63183 | -0.00494 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.36655 | -0.00484 | 4 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.37349 | -0.00482 | 4 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.53797 | -0.00478 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.57964 | -0.00474 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000162362398-0287-s_lc.fits` | 2460768.48520 | -0.00470 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.35127 | -0.00468 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.35683 | -0.00467 | 4 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461071.17723 | -0.00462 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.39849 | -0.00459 | 4 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461052.00509 | -0.00458 | 2 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.32071 | -0.00431 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.41933 | -0.00430 | 2 | SAP | 2, 3 | no |
| `tess2021091135823-s0037-0000000162362398-0208-s_lc.fits` | 2459313.77102 | -0.00422 | 2 | SAP | 1 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.84016 | -0.00421 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.37905 | -0.00420 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460027.78177 | -0.00419 | 2 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.62627 | -0.00419 | 4 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461067.44088 | -0.00412 | 2 | SAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.31655 | -0.00409 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000162362398-0300-s_lc.fits` | 2461067.42352 | -0.00402 | 3 | SAP | 1, 2 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.43183 | -0.00393 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000162362398-0255-s_lc.fits` | 2460034.84502 | -0.00374 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458591.01289 | 12040 | 11386 | 12.2513 | 0 / 12 |  |
| 2459331.38736 | 12028 | 11386 | 752.6257 | 8 / 752 | 752.626, 376.313, 250.875, 188.156, 150.525, 125.438, 94.0782, 62.7188 |
| 2460022.38794 | 12195 | 11386 | 1443.6263 | 9 / 1443 | 1443.63, 481.209, 288.725, 160.403, 111.048, 96.2418, 84.9192, 75.9803, 37.0161 |
| 2460034.73599 | 10070 | 11386 | 1455.9744 | 32 / 1455 | 1455.97, 727.987, 485.325, 363.994, 291.195, 242.662, 207.996, 181.997, 161.775, 132.361, 121.331, 111.998, 103.998, 97.065, 90.9984, 85.6456, 80.8875, 76.6302, 69.3321, 66.1807 |
| 2460750.45792 | 12101 | 11386 | 2171.6963 | 23 / 2171 | 2171.7, 1085.85, 542.924, 434.339, 310.242, 271.462, 217.17, 197.427, 167.054, 155.121, 135.731, 127.747, 114.3, 108.585, 98.7135, 94.4216, 86.8679, 77.5606, 70.0547, 57.1499 |
| 2460762.80393 | 11895 | 11386 | 2184.0423 | 38 / 2184 | 2184.04, 1092.02, 728.014, 546.011, 436.808, 364.007, 312.006, 273.005, 242.671, 218.404, 198.549, 182.004, 168.003, 156.003, 136.503, 128.473, 121.336, 114.95, 109.202, 104.002 |
| 2461046.60608 | 11379 | 11386 | 2467.8445 | 23 / 2467 | 2467.84, 1233.92, 822.615, 616.961, 493.569, 411.307, 308.481, 246.784, 224.35, 189.834, 164.523, 154.24, 129.887, 123.392, 98.7138, 82.2615, 77.1201, 64.9433, 63.2781, 61.6961 |
| 2461071.29391 | 12361 | 11386 | 2492.5323 | 16 / 2492 | 2492.53, 1246.27, 830.844, 623.133, 498.507, 415.422, 276.948, 226.594, 191.733, 166.169, 138.474, 113.297, 108.371, 67.3657, 24.6785, 12.3393 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-760.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:11:46Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:11:47Z: TOI-760.01 (TIC 162362398, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:11:48Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:11:48Z: TOI-760 (*); TOI-760.01 (err)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458578.6663: recovered, depth 11386 ± 107 ppm (catalogue 13386 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 10%, 30%, 0%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 8 repeat-candidate event(s); first at BJD 2458591.0129, ΔT = 12.251 d, 0 of 12 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-760.01: Gaia DR3 5377022012022524672 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-760.01: dwarf priors not applied — RUWE 1.7047967 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-760.01: 26 Gaia neighbour(s) within 52.5", contamination 17.52%; depth 11386 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 5377022016321410944, 28.1", ΔG 1.97); a centroid test is needed |
| Pointing and quality census per event | failed | 14 persistent event(s), 5 clean; BJD 2458591.0129 suspect: MOM_CENTR1 z=+6.0; BJD 2459318.9640 caution: manual exclude (within ±0.25 d); BJD 2459318.9932 suspect: manual exclude (within ±0.25 d), SAP_BKG z=-5.8; BJD 2459331.3874 suspect: MOM_CENTR1 z=+7.9 |
| Moving objects at screen-event epochs | inconclusive | 14 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-760.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-760.01: TOI-760.01 otype err (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-760-01.yaml
python -m cygnus.multi report campaigns/toi-760-01.yaml
```
