<!-- cygnus:generated-draft -->
# Known-object test, TOI-3476.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3476-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4810, calibrate_screen #4774, event_census #4785, fetch_independent #4807, fetch_products #4760, known_signal_recovery #4780, moving_objects #4801, period_aliases #4786, prior_art #4813, residual_screen #4783, stellar_context #4782, variability_guard #4811
- Runner finished (UTC): 2026-09-30T22:25:44Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3476.01 (BJD 2460072.8576: partial, depth 14140 ± 910 ppm (catalogue 13290 ppm); BJD 2460077.1781: recovered, depth 16077 ± 867 ppm (catalogue 13290 ppm); BJD 2460081.4986: recovered, depth 16394 ± 995 ppm (catalogue 13290 ppm); BJD 2460085.8191: recovered, depth 15965 ± 959 ppm (catalogue 13290 ppm); BJD 2460090.1396: partial, depth 13859 ± 937 ppm (catalogue 13290 ppm); BJD 2460094.4601: not recovered, depth -7706 ± 1523 ppm (catalogue 13290 ppm); BJD 2461127.0616: gap (catalogue 13290 ppm); BJD 2461131.3821: recovered, depth 18278 ± 1133 ppm (catalogue 13290 ppm); BJD 2461135.7026: partial, depth 16697 ± 1175 ppm (catalogue 13290 ppm); BJD 2461140.0231: not recovered, depth 5225 ± 4807 ppm (catalogue 13290 ppm); BJD 2461144.3436: recovered, depth 22370 ± 1207 ppm (catalogue 13290 ppm); BJD 2461148.6641: partial, depth 18230 ± 1173 ppm (catalogue 13290 ppm); BJD 2461152.9846: recovered, depth 28209 ± 1052 ppm (catalogue 13290 ppm); BJD 2461157.3051: recovered, depth 21359 ± 977 ppm (catalogue 13290 ppm); BJD 2461161.6256: recovered, depth 17565 ± 914 ppm (catalogue 13290 ppm); BJD 2461165.9461: not recovered, depth -4228 ± 1283 ppm (catalogue 13290 ppm); BJD 2461170.2667: partial, depth 15954 ± 994 ppm (catalogue 13290 ppm); BJD 2461174.5872: partial, depth 17569 ± 993 ppm (catalogue 13290 ppm)).
Outside the catalogued epoch the screen left 92 threshold entries forming **35 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461138.4737 matches the catalogued transit's depth (13705 vs 16077 ppm), 1061.301 d later; 32 of 1061 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3476.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 272983172 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 237.008308 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -50.692487 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459385.89681 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.3205081 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13290.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.51 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.6718 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | lightcurve | 65 | False | `a33d8f953e584257` | True |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | lightcurve | 102 | False | `83ab7d720196ad47` | True |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | lightcurve | 103 | False | `12e4a95e9f476e9e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460072.85760 | partial | 75 | 14140 ± 910 | 13290 | 0.69 |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460077.17811 | recovered | 76 | 16077 ± 867 | 13290 | -0.13 |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460081.49861 | recovered | 75 | 16394 ± 995 | 13290 | -0.02 |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460085.81912 | recovered | 75 | 15965 ± 959 | 13290 | -0.24 |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460090.13963 | partial | 76 | 13859 ± 937 | 13290 | 0.40 |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460094.46014 | not_recovered | 38 | -7706 ± 1523 | 13290 | — |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461127.06157 | gap | 0 | — | 13290 | — |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461131.38208 | recovered | 75 | 18278 ± 1133 | 13290 | 0.07 |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461135.70259 | partial | 75 | 16697 ± 1175 | 13290 | -0.65 |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.02310 | not_recovered | 8 | 5225 ± 4807 | 13290 | — |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461144.34361 | recovered | 75 | 22370 ± 1207 | 13290 | -0.05 |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461148.66411 | partial | 76 | 18230 ± 1173 | 13290 | -0.25 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461152.98462 | recovered | 75 | 28209 ± 1052 | 13290 | -0.09 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461157.30513 | recovered | 75 | 21359 ± 977 | 13290 | 0.89 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461161.62564 | recovered | 76 | 17565 ± 914 | 13290 | -0.20 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461165.94615 | not_recovered | 52 | -4228 ± 1283 | 13290 | — |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461170.26666 | partial | 75 | 15954 ± 994 | 13290 | -0.51 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461174.58716 | partial | 76 | 17569 ± 993 | 13290 | 0.50 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: 20000, 8h: 20000 |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.49122 | -0.04465 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.47373 | -0.03840 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.43080 | -0.03719 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.45372 | -0.03629 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.39261 | -0.03495 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.49943 | -0.03407 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.46900 | -0.03398 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.48359 | -0.03371 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.52387 | -0.03978 | 3 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.49817 | -0.03577 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.50928 | -0.03261 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.44678 | -0.03211 | 2 | PDCSAP | 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.42316 | -0.03210 | 2 | PDCSAP | 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.51345 | -0.02819 | 2 | PDCSAP | 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461140.45928 | -0.02801 | 2 | PDCSAP | 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460080.32977 | -0.02272 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460074.18657 | -0.02098 | 2 | PDCSAP | 1 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460083.25344 | -0.01925 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460083.25899 | -0.01815 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461177.44411 | -0.01717 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461176.95938 | -0.01693 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461177.43300 | -0.01688 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000272983172-0305-s_lc.fits` | 2461177.47606 | -0.01585 | 2 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.31886 | -0.01545 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460083.11316 | -0.01358 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461151.41268 | -0.01312 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.28414 | -0.01282 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.40637 | -0.01256 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460089.69793 | -0.01255 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460083.19788 | -0.01246 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460082.92982 | -0.01183 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.41609 | -0.01179 | 2 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000272983172-0304-s_lc.fits` | 2461138.29525 | -0.01170 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460083.29094 | -0.01101 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000272983172-0259-s_lc.fits` | 2460083.06316 | -0.01090 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461138.47373 | 13705 | 16077 | 1061.3010 | 32 / 1061 | 1061.3, 530.65, 353.767, 265.325, 212.26, 176.883, 151.614, 132.663, 117.922, 106.13, 96.4819, 88.4417, 81.6385, 75.8072, 70.7534, 66.3313, 62.4295, 58.9612, 55.8579, 53.065 |
| 2461138.49943 | 12914 | 16077 | 1061.3267 | 34 / 1061 | 1061.33, 530.663, 353.776, 265.332, 212.265, 176.888, 151.618, 132.666, 117.925, 106.133, 96.4842, 88.4439, 81.6405, 75.809, 70.7551, 66.3329, 62.431, 58.9626, 55.8593, 53.0663 |
| 2461140.39261 | 20837 | 16077 | 1063.2199 | 34 / 1063 | 1063.22, 531.61, 354.407, 265.805, 212.644, 177.203, 151.889, 132.903, 118.135, 106.322, 96.6564, 88.6017, 81.7861, 75.9443, 70.8813, 66.4512, 62.5423, 59.0678, 55.9589, 53.161 |
| 2461140.43080 | 22859 | 16077 | 1063.2580 | 33 / 1063 | 1063.26, 531.629, 354.419, 265.815, 212.652, 177.21, 151.894, 132.907, 118.14, 106.326, 96.6598, 88.6048, 81.7891, 75.947, 70.8839, 66.4536, 62.5446, 59.0699, 55.9609, 53.1629 |
| 2461140.45372 | 23095 | 16077 | 1063.2810 | 33 / 1063 | 1063.28, 531.64, 354.427, 265.82, 212.656, 177.214, 151.897, 132.91, 118.142, 106.328, 96.6619, 88.6067, 81.7908, 75.9486, 70.8854, 66.4551, 62.5459, 59.0712, 55.9622, 53.164 |
| 2461140.46900 | 23783 | 16077 | 1063.2962 | 32 / 1063 | 1063.3, 531.648, 354.432, 265.824, 212.659, 177.216, 151.899, 132.912, 118.144, 106.33, 96.6633, 88.608, 81.792, 75.9497, 70.8864, 66.456, 62.5468, 59.072, 55.963, 53.1648 |
| 2461140.48359 | 23356 | 16077 | 1063.3108 | 32 / 1063 | 1063.31, 531.655, 354.437, 265.828, 212.662, 177.219, 151.901, 132.914, 118.146, 106.331, 96.6646, 88.6092, 81.7931, 75.9508, 70.8874, 66.4569, 62.5477, 59.0728, 55.9637, 53.1655 |
| 2461140.49122 | 22529 | 16077 | 1063.3185 | 32 / 1063 | 1063.32, 531.659, 354.44, 265.83, 212.664, 177.22, 151.903, 132.915, 118.147, 106.332, 96.6653, 88.6099, 81.7937, 75.9513, 70.8879, 66.4574, 62.5481, 59.0732, 55.9641, 53.1659 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3476.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:25:31Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:25:35Z: TOI-3476.01 (TIC 272983172, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:25:38Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:25:40Z: TOI-3476.01 (Pl?); TOI-3476 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460072.8576: partial, depth 14140 ± 910 ppm (catalogue 13290 ppm); BJD 2460077.1781: recovered, depth 16077 ± 867 ppm (catalogue 13290 ppm); BJD 2460081.4986: recovered, depth 16394 ± 995 ppm (catalogue 13290 ppm); BJD 2460085.8191: recovered, depth 15965 ± 959 ppm (catalogue 13290 ppm); BJD 2460090.1396: partial, depth 13859 ± 937 ppm (catalogue 13290 ppm); BJD 2460094.4601: not recovered, depth -7706 ± 1523 ppm (catalogue 13290 ppm); BJD 2461127.0616: gap (catalogue 13290 ppm); BJD 2461131.3821: recovered, depth 18278 ± 1133 ppm (catalogue 13290 ppm); BJD 2461135.7026: partial, depth 16697 ± 1175 ppm (catalogue 13290 ppm); BJD 2461140.0231: not recovered, depth 5225 ± 4807 ppm (catalogue 13290 ppm); BJD 2461144.3436: recovered, depth 22370 ± 1207 ppm (catalogue 13290 ppm); BJD 2461148.6641: partial, depth 18230 ± 1173 ppm (catalogue 13290 ppm); BJD 2461152.9846: recovered, depth 28209 ± 1052 ppm (catalogue 13290 ppm); BJD 2461157.3051: recovered, depth 21359 ± 977 ppm (catalogue 13290 ppm); BJD 2461161.6256: recovered, depth 17565 ± 914 ppm (catalogue 13290 ppm); BJD 2461165.9461: not recovered, depth -4228 ± 1283 ppm (catalogue 13290 ppm); BJD 2461170.2667: partial, depth 15954 ± 994 ppm (catalogue 13290 ppm); BJD 2461174.5872: partial, depth 17569 ± 993 ppm (catalogue 13290 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 8 repeat-candidate event(s); first at BJD 2461138.4737, ΔT = 1061.301 d, 32 of 1061 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1061.3, 530.65, 353.767, 265.325, 212.26, 176.883, 151.614, 132.663, 117.922, 106.13, 96.4819, 88.4417 … d); duration likelihood under Gaia priors (circular orbits) peaks at 13.1 d (weight 0.46) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3476.01: Gaia DR3 5982358211745957632 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3476.01: Teff 5890 K, R* 1.20 ± 0.10, M* 1.16 ± 0.12, ρ* 0.67 ± 0.18 ρ☉ (dwarf sequence, M_G 3.99, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3476.01: 199 Gaia neighbour(s) within 52.5", contamination 67.29%; depth 16077 ppm (measured depth of the recovered catalogued transit); 8 could produce it if fully eclipsed (brightest 5982358211745958784, 19.6", ΔG 0.94); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 0 clean; BJD 2461138.4737 suspect: scattered light 2 (within ±0.25 d), POS_CORR1 z=-5.4, POS_CORR2 z=-6.6, SAP_BKG z=+1451.5; BJD 2461138.4994 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+1448.2; BJD 2461140.3926 suspect: manual exclude (within ±0.25 d), MOM_CENTR2 z=-8.3, POS_CORR1 z=+5.9, POS_CORR2 z=-8.0, SAP_BKG z=+417.3; BJD 2461140.4308 suspect: manual exclude (within ±0.25 d), POS_CORR2 z=-8.0, SAP_BKG z=+352.9 |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3476.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3476.01: TOI-3476 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 6 possible published-ephemeris overlap(s) within 1 d (TOI-3476.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3476-01.yaml
python -m cygnus.multi report campaigns/toi-3476-01.yaml
```
