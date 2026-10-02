<!-- cygnus:generated-draft -->
# Known-object test, TOI-3820.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3820-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4098, calibrate_screen #4063, event_census #4073, fetch_independent #4087, fetch_products #4053, known_signal_recovery #4065, moving_objects #4078, period_aliases #4074, prior_art #4100, residual_screen #4069, stellar_context #4066, variability_guard #4099
- Runner finished (UTC): 2026-09-30T21:37:40Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3820.01 (BJD 2459503.0924: recovered, depth 4154 ± 315 ppm (catalogue 7392 ppm); BJD 2459508.5214: recovered, depth 4620 ± 308 ppm (catalogue 7392 ppm); BJD 2459513.9505: gap (catalogue 7392 ppm); BJD 2459519.3796: recovered, depth 4780 ± 325 ppm (catalogue 7392 ppm); BJD 2459530.2377: not recovered, depth 4190 ± 321 ppm (catalogue 7392 ppm); BJD 2459535.6668: recovered, depth 4217 ± 319 ppm (catalogue 7392 ppm); BJD 2459541.0959: recovered, depth 2093 ± 331 ppm (catalogue 7392 ppm); BJD 2459546.5250: recovered, depth 4350 ± 306 ppm (catalogue 7392 ppm); BJD 2459551.9541: gap (catalogue 7392 ppm); BJD 2459557.3831: not recovered, depth 3991 ± 298 ppm (catalogue 7392 ppm); BJD 2459562.8122: not recovered, depth 4425 ± 289 ppm (catalogue 7392 ppm); BJD 2459568.2413: not recovered, depth 4535 ± 314 ppm (catalogue 7392 ppm); BJD 2459573.6704: partial, depth 3811 ± 312 ppm (catalogue 7392 ppm); BJD 2459584.5285: recovered, depth 4219 ± 323 ppm (catalogue 7392 ppm); BJD 2459589.9576: recovered, depth 4275 ± 320 ppm (catalogue 7392 ppm); BJD 2459595.3867: gap (catalogue 7392 ppm); BJD 2459600.8158: recovered, depth 4136 ± 324 ppm (catalogue 7392 ppm); BJD 2459606.2448: recovered, depth 4498 ± 305 ppm (catalogue 7392 ppm); BJD 2460236.0179: recovered, depth 8297 ± 328 ppm (catalogue 7392 ppm); BJD 2460241.4470: recovered, depth 4478 ± 291 ppm (catalogue 7392 ppm); BJD 2460246.8761: gap (catalogue 7392 ppm); BJD 2460252.3051: recovered, depth 4120 ± 294 ppm (catalogue 7392 ppm); BJD 2460257.7342: recovered, depth 3773 ± 276 ppm (catalogue 7392 ppm); BJD 2460263.1633: recovered, depth 3650 ± 341 ppm (catalogue 7392 ppm); BJD 2460268.5924: recovered, depth 3971 ± 304 ppm (catalogue 7392 ppm); BJD 2460274.0214: gap (catalogue 7392 ppm); BJD 2460279.4505: gap (catalogue 7392 ppm); BJD 2460284.8796: recovered, depth 3682 ± 294 ppm (catalogue 7392 ppm)).
Outside the catalogued epoch the screen left 75 threshold entries forming **27 distinct event(s)**, **5 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460235.7624 matches the catalogued transit's depth (5016 vs 4154 ppm), 732.671 d later; 9 of 732 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3820.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 95234976 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 115.641632 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 28.807132 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459503.092356 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.4290781 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 7391.6084773 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.1018506 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.5562 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-15 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | lightcurve | 44 | True | `4ca67863c1f9274b` | True |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | lightcurve | 45 | False | `9051ae01388ffe0e` | True |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | lightcurve | 46 | False | `b3da587be8295b46` | True |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | lightcurve | 47 | False | `b44b31ef2bb5bcca` | True |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | lightcurve | 71 | False | `0d180e9f907f8edc` | True |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | lightcurve | 72 | False | `5e08d94c0ea28aac` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 2459503.09236 | recovered | 93 | 4154 ± 315 | 7392 | -0.01 |
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 2459508.52143 | recovered | 94 | 4620 ± 308 | 7392 | 0.27 |
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 2459513.95051 | gap | 0 | — | 7392 | — |
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 2459519.37959 | recovered | 90 | 4780 ± 325 | 7392 | 0.31 |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 2459530.23775 | not_recovered | 93 | 4190 ± 321 | 7392 | — |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 2459535.66682 | recovered | 93 | 4217 ± 319 | 7392 | -0.63 |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 2459541.09590 | recovered | 93 | 2093 ± 331 | 7392 | -0.13 |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 2459546.52498 | recovered | 93 | 4350 ± 306 | 7392 | -0.17 |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 2459551.95406 | gap | 0 | — | 7392 | — |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 2459557.38314 | not_recovered | 93 | 3991 ± 298 | 7392 | — |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 2459562.81222 | not_recovered | 92 | 4425 ± 289 | 7392 | — |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 2459568.24129 | not_recovered | 94 | 4535 ± 314 | 7392 | — |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 2459573.67037 | partial | 93 | 3811 ± 312 | 7392 | -0.43 |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459584.52853 | recovered | 93 | 4219 ± 323 | 7392 | 0.00 |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459589.95761 | recovered | 93 | 4275 ± 320 | 7392 | 0.14 |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459595.38668 | gap | 0 | — | 7392 | — |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459600.81576 | recovered | 93 | 4136 ± 324 | 7392 | -0.04 |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459606.24484 | recovered | 93 | 4498 ± 305 | 7392 | -0.21 |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460236.01790 | recovered | 93 | 8297 ± 328 | 7392 | -0.48 |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460241.44698 | recovered | 93 | 4478 ± 291 | 7392 | -0.13 |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460246.87606 | gap | 0 | — | 7392 | — |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460252.30513 | recovered | 93 | 4120 ± 294 | 7392 | 0.35 |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460257.73421 | recovered | 93 | 3773 ± 276 | 7392 | 0.96 |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460263.16329 | recovered | 93 | 3650 ± 341 | 7392 | -0.03 |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460268.59237 | recovered | 92 | 3971 ± 304 | 7392 | -0.11 |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460274.02145 | gap | 0 | — | 7392 | — |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460279.45052 | gap | 0 | — | 7392 | — |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460284.87960 | recovered | 93 | 3682 ± 294 | 7392 | -0.08 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2021336043614-s0046-0000000095234976-0217-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459580.86253 | -0.03011 | 119 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.80618 | -0.01250 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.76242 | -0.01129 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.82007 | -0.01100 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021310001228-s0045-0000000095234976-0216-s_lc.fits` | 2459536.54627 | -0.01076 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.79021 | -0.00978 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.79715 | -0.00949 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460253.01548 | -0.00849 | 2 | SAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460262.68024 | -0.00838 | 2 | PDCSAP | 3 | no |
| `tess2021284114741-s0044-0000000095234976-0215-s_lc.fits` | 2459508.72287 | -0.00836 | 2 | PDCSAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460262.33368 | -0.00832 | 3 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.81243 | -0.00813 | 4 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460246.16623 | -0.00737 | 2 | SAP | 2, 3 | no |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459586.33901 | -0.00724 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460235.73742 | -0.00669 | 2 | SAP | 1, 2, 3 | no |
| `tess2021364111932-s0047-0000000095234976-0218-s_lc.fits` | 2459580.77572 | -0.00660 | 3 | SAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460266.02775 | -0.00654 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460279.18987 | -0.00642 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460253.08216 | -0.00634 | 2 | SAP | 1, 2 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460266.03192 | -0.00624 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460240.74209 | -0.00616 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460266.14304 | -0.00609 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460266.27500 | -0.00605 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460266.09582 | -0.00602 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000095234976-0266-s_lc.fits` | 2460253.09188 | -0.00589 | 2 | SAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460265.82635 | -0.00558 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000095234976-0267-s_lc.fits` | 2460265.50549 | -0.00545 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460235.76242 | 5016 | 4154 | 732.6707 | 9 / 732 | 732.671, 366.335, 244.224, 183.168, 146.534, 122.112, 104.667, 91.5838, 81.4079 |
| 2460235.80618 | 5016 | 4154 | 732.7144 | 9 / 732 | 732.714, 366.357, 244.238, 183.179, 146.543, 122.119, 104.674, 91.5893, 81.4127 |
| 2460235.82007 | 5367 | 4154 | 732.7283 | 9 / 732 | 732.728, 366.364, 244.243, 183.182, 146.546, 122.121, 104.675, 91.591, 81.4143 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3820.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:37:33Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:37:35Z: TOI-3820.01 (TIC 95234976, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:37:37Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:37:38Z: TOI-3820 (*); TOI-3820.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459503.0924: recovered, depth 4154 ± 315 ppm (catalogue 7392 ppm); BJD 2459508.5214: recovered, depth 4620 ± 308 ppm (catalogue 7392 ppm); BJD 2459513.9505: gap (catalogue 7392 ppm); BJD 2459519.3796: recovered, depth 4780 ± 325 ppm (catalogue 7392 ppm); BJD 2459530.2377: not recovered, depth 4190 ± 321 ppm (catalogue 7392 ppm); BJD 2459535.6668: recovered, depth 4217 ± 319 ppm (catalogue 7392 ppm); BJD 2459541.0959: recovered, depth 2093 ± 331 ppm (catalogue 7392 ppm); BJD 2459546.5250: recovered, depth 4350 ± 306 ppm (catalogue 7392 ppm); BJD 2459551.9541: gap (catalogue 7392 ppm); BJD 2459557.3831: not recovered, depth 3991 ± 298 ppm (catalogue 7392 ppm); BJD 2459562.8122: not recovered, depth 4425 ± 289 ppm (catalogue 7392 ppm); BJD 2459568.2413: not recovered, depth 4535 ± 314 ppm (catalogue 7392 ppm); BJD 2459573.6704: partial, depth 3811 ± 312 ppm (catalogue 7392 ppm); BJD 2459584.5285: recovered, depth 4219 ± 323 ppm (catalogue 7392 ppm); BJD 2459589.9576: recovered, depth 4275 ± 320 ppm (catalogue 7392 ppm); BJD 2459595.3867: gap (catalogue 7392 ppm); BJD 2459600.8158: recovered, depth 4136 ± 324 ppm (catalogue 7392 ppm); BJD 2459606.2448: recovered, depth 4498 ± 305 ppm (catalogue 7392 ppm); BJD 2460236.0179: recovered, depth 8297 ± 328 ppm (catalogue 7392 ppm); BJD 2460241.4470: recovered, depth 4478 ± 291 ppm (catalogue 7392 ppm); BJD 2460246.8761: gap (catalogue 7392 ppm); BJD 2460252.3051: recovered, depth 4120 ± 294 ppm (catalogue 7392 ppm); BJD 2460257.7342: recovered, depth 3773 ± 276 ppm (catalogue 7392 ppm); BJD 2460263.1633: recovered, depth 3650 ± 341 ppm (catalogue 7392 ppm); BJD 2460268.5924: recovered, depth 3971 ± 304 ppm (catalogue 7392 ppm); BJD 2460274.0214: gap (catalogue 7392 ppm); BJD 2460279.4505: gap (catalogue 7392 ppm); BJD 2460284.8796: recovered, depth 3682 ± 294 ppm (catalogue 7392 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 4, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 30%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460235.7624, ΔT = 732.671 d, 9 of 732 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (732.671, 366.335, 244.224, 183.168, 146.534, 122.112, 104.667, 91.5838, 81.4079 d); duration likelihood under Gaia priors (circular orbits) peaks at 81.4 d (weight 0.92) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3820.01: Gaia DR3 878444610169482880 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3820.01: Teff 6298 K, R* 1.65 ± 0.13, M* 1.48 ± 0.15, ρ* 0.33 ± 0.09 ρ☉ (dwarf sequence, M_G 2.78, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3820.01: 6 Gaia neighbour(s) within 52.5", contamination 28.57%; depth 4154 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 878444614466071936, 11.6", ΔG 1.89); a centroid test is needed |
| Pointing and quality census per event | failed | 5 persistent event(s), 0 clean; BJD 2459536.5463 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+15.8; BJD 2459580.8625 suspect: MOM_CENTR1 z=-6.0, POS_CORR1 z=-18.7, SAP_BKG z=+116.1; BJD 2460235.7624 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=-10.8, MOM_CENTR2 z=-9.6, POS_CORR1 z=-12.5, POS_CORR2 z=-10.1, SAP_BKG z=+39.8; BJD 2460235.8062 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=-11.0, MOM_CENTR2 z=-10.5, POS_CORR1 z=-11.9, POS_CORR2 z=-10.9, SAP_BKG z=+44.6 |
| Moving objects at screen-event epochs | passed | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 3 light curve × candidate pair(s); aliases supported: none; excluded: none; 27 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-3820.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3820.01: TOI-3820 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 3 possible published-ephemeris overlap(s) within 1 d (TOI-3820.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3820-01.yaml
python -m cygnus.multi report campaigns/toi-3820-01.yaml
```
