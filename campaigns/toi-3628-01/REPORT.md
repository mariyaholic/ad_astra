<!-- cygnus:generated-draft -->
# Known-object test, TOI-3628.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3628-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4383, calibrate_screen #4360, event_census #4371, fetch_independent #4375, fetch_products #4359, known_signal_recovery #4362, moving_objects #4374, period_aliases #4372, prior_art #4387, residual_screen #4366, stellar_context #4365, variability_guard #4385
- Runner finished (UTC): 2026-09-30T21:50:47Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3628.01 (BJD 2459854.7700: recovered, depth 7347 ± 328 ppm (catalogue 8254 ppm); BJD 2459858.2645: recovered, depth 7340 ± 362 ppm (catalogue 8254 ppm); BJD 2459861.7590: recovered, depth 7241 ± 307 ppm (catalogue 8254 ppm); BJD 2459865.2535: gap (catalogue 8254 ppm); BJD 2459868.7480: recovered, depth 6848 ± 338 ppm (catalogue 8254 ppm); BJD 2459872.2425: recovered, depth 6782 ± 344 ppm (catalogue 8254 ppm); BJD 2459875.7370: recovered, depth 7291 ± 316 ppm (catalogue 8254 ppm); BJD 2459879.2316: recovered, depth 6745 ± 337 ppm (catalogue 8254 ppm); BJD 2460585.1236: recovered, depth 8221 ± 466 ppm (catalogue 8254 ppm); BJD 2460588.6181: recovered, depth 7466 ± 358 ppm (catalogue 8254 ppm); BJD 2460592.1126: recovered, depth 7335 ± 316 ppm (catalogue 8254 ppm); BJD 2460595.6071: gap (catalogue 8254 ppm); BJD 2460599.1016: gap (catalogue 8254 ppm); BJD 2460602.5961: recovered, depth 7158 ± 365 ppm (catalogue 8254 ppm); BJD 2460606.0906: recovered, depth 7250 ± 331 ppm (catalogue 8254 ppm); BJD 2460609.5852: recovered, depth 7257 ± 330 ppm (catalogue 8254 ppm); BJD 2460613.0797: gap (catalogue 8254 ppm); BJD 2460616.5742: recovered, depth 6715 ± 489 ppm (catalogue 8254 ppm); BJD 2460620.0687: partial, depth 7575 ± 370 ppm (catalogue 8254 ppm); BJD 2460623.5632: partial, depth 10047 ± 427 ppm (catalogue 8254 ppm); BJD 2460627.0577: gap (catalogue 8254 ppm); BJD 2460630.5522: recovered, depth 4463 ± 390 ppm (catalogue 8254 ppm); BJD 2460634.0468: recovered, depth 9012 ± 363 ppm (catalogue 8254 ppm)).
Outside the catalogued epoch the screen left 153 threshold entries forming **112 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3628.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 238624131 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 12.866044 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 47.662806 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459879.231564 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.4945148 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8254.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.555 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6203 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-09-19 12:04:41 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | lightcurve | 57 | True | `7de3541c4f61fcae` | True |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | lightcurve | 84 | False | `bdb25141077152d3` | True |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | lightcurve | 85 | False | `47e5819c9436961c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459854.76996 | recovered | 77 | 7347 ± 328 | 8254 | -0.03 |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459858.26448 | recovered | 77 | 7340 ± 362 | 8254 | -0.31 |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459861.75899 | recovered | 77 | 7241 ± 307 | 8254 | -0.05 |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459865.25350 | gap | 0 | — | 8254 | — |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459868.74802 | recovered | 77 | 6848 ± 338 | 8254 | -0.12 |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459872.24253 | recovered | 77 | 6782 ± 344 | 8254 | 0.22 |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459875.73705 | recovered | 77 | 7291 ± 316 | 8254 | 0.20 |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459879.23156 | recovered | 77 | 6745 ± 337 | 8254 | 0.01 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460585.12355 | recovered | 77 | 8221 ± 466 | 8254 | 0.34 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460588.61807 | recovered | 77 | 7466 ± 358 | 8254 | 0.23 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460592.11258 | recovered | 77 | 7335 ± 316 | 8254 | 0.15 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460595.60710 | gap | 0 | — | 8254 | — |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460599.10161 | gap | 0 | — | 8254 | — |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460602.59613 | recovered | 77 | 7158 ± 365 | 8254 | -0.02 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460606.09064 | recovered | 77 | 7250 ± 331 | 8254 | 0.01 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460609.58516 | recovered | 77 | 7257 ± 330 | 8254 | 0.36 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460613.07967 | gap | 0 | — | 8254 | — |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460616.57419 | recovered | 55 | 6715 ± 489 | 8254 | -0.56 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460620.06870 | partial | 76 | 7575 ± 370 | 8254 | 0.19 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.56322 | partial | 76 | 10047 ± 427 | 8254 | -0.57 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460627.05773 | gap | 0 | — | 8254 | — |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460630.55225 | recovered | 77 | 4463 ± 390 | 8254 | 0.06 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460634.04676 | recovered | 77 | 9012 ± 363 | 8254 | -0.68 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.04096 | -0.01516 | 2 | SAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.20624 | -0.01324 | 4 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.01597 | -0.01276 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.17707 | -0.01179 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.11041 | -0.01172 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460610.63693 | -0.01161 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.00347 | -0.01153 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.92152 | -0.01147 | 4 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.98055 | -0.01142 | 3 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.23402 | -0.01140 | 4 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.05624 | -0.01138 | 6 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.18541 | -0.01136 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.19721 | -0.01132 | 3 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.22707 | -0.01121 | 4 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.18957 | -0.01120 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.16457 | -0.01097 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.18124 | -0.01092 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.86180 | -0.01082 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.15138 | -0.01081 | 3 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.11874 | -0.01068 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.57376 | -0.01047 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.94374 | -0.01044 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.96388 | -0.01041 | 3 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.17013 | -0.01028 | 4 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459860.15140 | -0.01016 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.02916 | -0.01014 | 5 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.02222 | -0.01014 | 3 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.99583 | -0.00984 | 3 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.13680 | -0.00978 | 4 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.92916 | -0.00972 | 5 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.09374 | -0.00941 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459866.97167 | -0.00938 | 3 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.89236 | -0.00936 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.22152 | -0.00920 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.62708 | -0.00920 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460622.84791 | -0.00917 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.48765 | -0.00877 | 4 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.63695 | -0.00877 | 3 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.06874 | -0.00876 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.47654 | -0.00871 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000238624131-0282-s_lc.fits` | 2460623.01180 | -0.00863 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460590.11447 | -0.00862 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.77654 | -0.00854 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.06958 | -0.00849 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.54945 | -0.00845 | 5 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.48209 | -0.00824 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.59320 | -0.00819 | 8 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.85849 | -0.00818 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.77098 | -0.00805 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.52515 | -0.00805 | 4 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.17653 | -0.00805 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460585.30601 | -0.00802 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.84876 | -0.00795 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.53487 | -0.00794 | 6 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.54251 | -0.00791 | 3 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460590.58671 | -0.00790 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.58487 | -0.00789 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.79598 | -0.00777 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.20570 | -0.00772 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.68279 | -0.00769 | 13 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459866.93764 | -0.00767 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.78210 | -0.00751 | 4 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.12931 | -0.00749 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.72029 | -0.00747 | 3 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.57931 | -0.00744 | 4 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.76196 | -0.00741 | 5 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.19320 | -0.00740 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.20153 | -0.00740 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.73209 | -0.00735 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.64529 | -0.00732 | 5 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460589.97975 | -0.00727 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.65154 | -0.00723 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.13625 | -0.00723 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.55779 | -0.00720 | 3 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460585.40254 | -0.00720 | 3 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.61473 | -0.00718 | 5 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.73973 | -0.00717 | 7 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460590.67838 | -0.00716 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.84043 | -0.00716 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.66890 | -0.00716 | 5 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.49806 | -0.00704 | 5 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.62723 | -0.00704 | 9 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.51473 | -0.00702 | 3 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.80571 | -0.00694 | 4 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.72793 | -0.00687 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.65918 | -0.00685 | 7 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460590.02419 | -0.00684 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.60501 | -0.00684 | 7 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.50848 | -0.00683 | 4 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460595.27292 | -0.00681 | 2 | SAP | 1 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.86265 | -0.00674 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460590.75060 | -0.00672 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.11195 | -0.00656 | 3 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460598.18685 | -0.00656 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.07931 | -0.00655 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.96265 | -0.00649 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.79182 | -0.00648 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.81404 | -0.00647 | 4 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460590.60060 | -0.00647 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.69807 | -0.00647 | 5 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.75154 | -0.00646 | 4 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459853.56510 | -0.00645 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.56543 | -0.00643 | 6 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.83557 | -0.00643 | 3 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.90640 | -0.00639 | 3 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460599.83826 | -0.00636 | 2 | SAP | 1 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459853.67205 | -0.00636 | 2 | SAP | 2 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459866.90430 | -0.00629 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459853.57343 | -0.00627 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000238624131-0281-s_lc.fits` | 2460589.54918 | -0.00626 | 2 | SAP | 1 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459866.55569 | -0.00619 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000238624131-0245-s_lc.fits` | 2459867.78765 | -0.00617 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3628.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:50:40Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:50:42Z: TOI-3628.01 (TIC 238624131, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:50:44Z
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:50:46Z: 2MASS J00512655+4739277 (*); TOI-3628.01 (Pl?); Pul -3   70152 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459854.7700: recovered, depth 7347 ± 328 ppm (catalogue 8254 ppm); BJD 2459858.2645: recovered, depth 7340 ± 362 ppm (catalogue 8254 ppm); BJD 2459861.7590: recovered, depth 7241 ± 307 ppm (catalogue 8254 ppm); BJD 2459865.2535: gap (catalogue 8254 ppm); BJD 2459868.7480: recovered, depth 6848 ± 338 ppm (catalogue 8254 ppm); BJD 2459872.2425: recovered, depth 6782 ± 344 ppm (catalogue 8254 ppm); BJD 2459875.7370: recovered, depth 7291 ± 316 ppm (catalogue 8254 ppm); BJD 2459879.2316: recovered, depth 6745 ± 337 ppm (catalogue 8254 ppm); BJD 2460585.1236: recovered, depth 8221 ± 466 ppm (catalogue 8254 ppm); BJD 2460588.6181: recovered, depth 7466 ± 358 ppm (catalogue 8254 ppm); BJD 2460592.1126: recovered, depth 7335 ± 316 ppm (catalogue 8254 ppm); BJD 2460595.6071: gap (catalogue 8254 ppm); BJD 2460599.1016: gap (catalogue 8254 ppm); BJD 2460602.5961: recovered, depth 7158 ± 365 ppm (catalogue 8254 ppm); BJD 2460606.0906: recovered, depth 7250 ± 331 ppm (catalogue 8254 ppm); BJD 2460609.5852: recovered, depth 7257 ± 330 ppm (catalogue 8254 ppm); BJD 2460613.0797: gap (catalogue 8254 ppm); BJD 2460616.5742: recovered, depth 6715 ± 489 ppm (catalogue 8254 ppm); BJD 2460620.0687: partial, depth 7575 ± 370 ppm (catalogue 8254 ppm); BJD 2460623.5632: partial, depth 10047 ± 427 ppm (catalogue 8254 ppm); BJD 2460627.0577: gap (catalogue 8254 ppm); BJD 2460630.5522: recovered, depth 4463 ± 390 ppm (catalogue 8254 ppm); BJD 2460634.0468: recovered, depth 9012 ± 363 ppm (catalogue 8254 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3628.01: Gaia DR3 378265951674712448 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3628.01: Teff 5497 K, R* 1.06 ± 0.08, M* 1.03 ± 0.10, ρ* 0.87 ± 0.23 ρ☉ (dwarf sequence, M_G 4.47, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3628.01: 9 Gaia neighbour(s) within 52.5", contamination 48.66%; depth 7347 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 378265947376465024, 22.3", ΔG 0.13); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3628.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3628.01: Pul -3   70152 otype * (star_or_other) at 0.6" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3628-01.yaml
python -m cygnus.multi report campaigns/toi-3628-01.yaml
```
