<!-- cygnus:generated-draft -->
# Known-object test, TOI-6564.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6564-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #736, calibrate_screen #623, event_census #637, fetch_products #616, known_signal_recovery #625, moving_objects #722, period_aliases #638, prior_art #738, residual_screen #629, stellar_context #626, variability_guard #737
- Runner finished (UTC): 2026-09-26T10:17:11Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6564.01 (BJD 2460071.3702: recovered, depth 8070 ± 74 ppm (catalogue 8801 ppm)).
Outside the catalogued epoch the screen left 389 threshold entries forming **137 distinct event(s)**, **34 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460075.3542 matches the catalogued transit's depth (7750 vs 8070 ppm), 4.026 d later; 0 of 4 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6564.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 453668803 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 205.817879 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -56.156449 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460071.370156 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8800.6144816 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.5181131 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.5687 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-05-24 12:03:10 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | lightcurve | 65 | True | `0894ecb91d3f6929` | True |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | lightcurve | 99 | False | `f56159fee0a89ff1` | True |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | lightcurve | 100 | False | `8f3e7c5ccf99e125` | True |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | lightcurve | 101 | False | `b984e340ceaf037d` | True |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | lightcurve | 102 | False | `2c2de65e3e897b12` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460071.37016 | recovered | 135 | 8070 ± 74 | 8801 | -1.01 |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 8801 | — |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 8801 | — |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 8801 | — |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 8801 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 3 | False | 1h: 5000, 2h: 10000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460083.24999 | -0.00908 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461123.51515 | -0.00867 | 119 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461103.59172 | -0.00857 | 119 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461131.49124 | -0.00854 | 120 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461119.53230 | -0.00848 | 128 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461111.56307 | -0.00845 | 123 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461051.78312 | -0.00836 | 124 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460087.31104 | -0.00830 | 120 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461079.67957 | -0.00830 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461143.44448 | -0.00823 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461135.47613 | -0.00821 | 118 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460083.33262 | -0.00821 | 111 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461147.43210 | -0.00816 | 124 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461115.54804 | -0.00811 | 121 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461095.61963 | -0.00807 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460091.29637 | -0.00806 | 121 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461091.63324 | -0.00805 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460075.35420 | -0.00804 | 120 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461083.66389 | -0.00800 | 121 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461063.73743 | -0.00796 | 123 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461075.69177 | -0.00796 | 124 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461087.64821 | -0.00796 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461071.70675 | -0.00785 | 124 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461047.79744 | -0.00781 | 121 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460079.33960 | -0.00777 | 121 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461067.72313 | -0.00767 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461127.50424 | -0.00764 | 120 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461107.57671 | -0.00753 | 123 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461123.60057 | -0.00502 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461103.67715 | -0.00466 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461135.39141 | -0.00465 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461091.72074 | -0.00454 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.64092 | -0.00410 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461103.50630 | -0.00404 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.20547 | -0.00663 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.29714 | -0.00640 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.27214 | -0.00640 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.17491 | -0.00637 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.92767 | -0.00619 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.88484 | -0.00586 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.00546 | -0.00585 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.90823 | -0.00573 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.69594 | -0.00573 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461144.94592 | -0.00571 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.90150 | -0.00564 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.28603 | -0.00561 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.46105 | -0.00558 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.75428 | -0.00556 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461119.87121 | -0.00552 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461151.40024 | -0.00537 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.14585 | -0.00532 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.31798 | -0.00531 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.11241 | -0.00529 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.10269 | -0.00525 | 4 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.83484 | -0.00524 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.82928 | -0.00523 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.52643 | -0.00523 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.11796 | -0.00522 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.74033 | -0.00521 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.18741 | -0.00510 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.14783 | -0.00504 | 3 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.67928 | -0.00500 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.03463 | -0.00499 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.32086 | -0.00499 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.65566 | -0.00498 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.06657 | -0.00493 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.85423 | -0.00493 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.24176 | -0.00492 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.70983 | -0.00470 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460089.87071 | -0.00469 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.26381 | -0.00469 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.76933 | -0.00468 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.82511 | -0.00466 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.42424 | -0.00463 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460090.06932 | -0.00461 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.09018 | -0.00457 | 4 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.74664 | -0.00456 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460090.06098 | -0.00456 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.05495 | -0.00454 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.16241 | -0.00453 | 4 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.74450 | -0.00444 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.80961 | -0.00444 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.51244 | -0.00439 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.06240 | -0.00434 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461138.35679 | -0.00431 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.08473 | -0.00431 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.04157 | -0.00430 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461145.08065 | -0.00427 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461146.01401 | -0.00419 | 2 | SAP | 2 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460083.20415 | -0.00415 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.83201 | -0.00414 | 4 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.54726 | -0.00410 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.27641 | -0.00404 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461119.81704 | -0.00398 | 3 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 2461131.40513 | -0.00397 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.30419 | -0.00397 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.27770 | -0.00397 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.70613 | -0.00395 | 3 | SAP | 1, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.61654 | -0.00393 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.18186 | -0.00392 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461092.81943 | -0.00391 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.19991 | -0.00390 | 4 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460089.44711 | -0.00389 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460083.15554 | -0.00385 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.81256 | -0.00379 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.62713 | -0.00373 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460083.18193 | -0.00371 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.36531 | -0.00369 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.08185 | -0.00368 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.95406 | -0.00367 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.62147 | -0.00365 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.73113 | -0.00365 | 5 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 2460089.40822 | -0.00364 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.21668 | -0.00362 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.56792 | -0.00361 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.02907 | -0.00358 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.66106 | -0.00355 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461074.00830 | -0.00355 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461074.13609 | -0.00348 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.93601 | -0.00348 | 4 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.18126 | -0.00348 | 3 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.81673 | -0.00347 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.29447 | -0.00346 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.89850 | -0.00346 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.94990 | -0.00341 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.21658 | -0.00338 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.83895 | -0.00335 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461072.83322 | -0.00332 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461119.24270 | -0.00328 | 3 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 2461119.86357 | -0.00327 | 3 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.31669 | -0.00326 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461080.91855 | -0.00325 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.20696 | -0.00320 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.84520 | -0.00312 | 3 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461074.06664 | -0.00312 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 2461093.87437 | -0.00304 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 2461073.12838 | -0.00303 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460075.35420 | 7750 | 8070 | 4.0260 | 0 / 4 |  |
| 2460079.33960 | 7219 | 8070 | 8.0114 | 0 / 8 |  |
| 2460083.24999 | 6180 | 8070 | 11.9218 | 0 / 11 |  |
| 2460083.33262 | 7804 | 8070 | 12.0045 | 0 / 12 |  |
| 2460087.31104 | 8042 | 8070 | 15.9829 | 0 / 15 |  |
| 2460091.29637 | 7742 | 8070 | 19.9682 | 0 / 19 |  |
| 2461047.79744 | 7692 | 8070 | 976.4693 | 13 / 976 | 976.469, 488.235, 325.49, 244.117, 195.294, 162.745, 139.496, 122.059, 108.497, 65.098, 39.0588, 27.8991, 19.9279 |
| 2461051.78312 | 8102 | 8070 | 980.4550 | 15 / 980 | 980.455, 490.228, 326.818, 245.114, 196.091, 163.409, 140.065, 122.557, 108.939, 75.4196, 61.2784, 23.9135, 11.9568, 7.9712, 3.9856 |
| 2461063.73743 | 7765 | 8070 | 992.4093 | 15 / 992 | 992.409, 496.205, 330.803, 248.102, 198.482, 165.401, 141.773, 124.051, 110.268, 99.2409, 90.219, 76.3392, 62.0256, 49.6205, 11.9567 |
| 2461067.72313 | 7223 | 8070 | 996.3950 | 18 / 996 | 996.395, 498.197, 332.132, 249.099, 199.279, 166.066, 142.342, 124.549, 110.711, 99.6395, 90.5814, 71.1711, 58.6115, 52.4418, 45.2907, 39.8558, 19.9279, 7.9712 |
| 2461071.70675 | 7782 | 8070 | 1000.3786 | 13 / 1000 | 1000.38, 500.189, 333.459, 250.095, 200.076, 166.73, 142.911, 125.047, 111.153, 100.038, 90.9435, 83.3649, 41.6824 |
| 2461075.69177 | 7807 | 8070 | 1004.3636 | 23 / 1004 | 1004.36, 502.182, 334.788, 251.091, 200.873, 167.394, 143.481, 125.546, 111.596, 100.436, 91.3058, 83.697, 77.2587, 71.7403, 55.798, 50.2182, 47.8268, 35.8701, 27.899, 23.9134 |
| 2461079.67957 | 8141 | 8070 | 1008.3514 | 17 / 1008 | 1008.35, 504.176, 336.117, 252.088, 201.67, 168.059, 144.05, 126.044, 112.039, 100.835, 91.6683, 84.0293, 77.5655, 72.0251, 59.3148, 45.8342, 43.8414 |
| 2461083.66389 | 7798 | 8070 | 1012.3357 | 17 / 1012 | 1012.34, 506.168, 337.445, 253.084, 202.467, 168.723, 144.619, 126.542, 112.482, 101.234, 92.0305, 84.3613, 77.872, 72.3097, 56.2409, 42.1807, 7.9711 |
| 2461087.64821 | 7589 | 8070 | 1016.3200 | 19 / 1016 | 1016.32, 508.16, 338.773, 254.08, 203.264, 169.387, 145.189, 127.04, 112.924, 101.632, 92.3927, 84.6933, 78.1785, 72.5943, 67.7547, 59.7835, 26.0595, 19.9278, 11.9567 |
| 2461091.63324 | 7899 | 8070 | 1020.3051 | 22 / 1020 | 1020.31, 510.152, 340.102, 255.076, 204.061, 170.051, 145.758, 127.538, 113.367, 102.031, 92.755, 85.0254, 78.485, 72.8789, 68.0203, 63.7691, 60.0179, 35.1829, 34.0102, 31.8845 |
| 2461095.61963 | 7823 | 8070 | 1024.2915 | 18 / 1024 | 1024.29, 512.146, 341.43, 256.073, 204.858, 170.715, 146.327, 128.036, 113.81, 102.429, 93.1174, 85.3576, 78.7917, 73.1637, 68.2861, 64.0182, 60.2524, 56.9051 |
| 2461103.59172 | 8252 | 8070 | 1032.2636 | 18 / 1032 | 1032.26, 516.132, 344.088, 258.066, 206.453, 172.044, 147.466, 129.033, 114.696, 103.226, 93.8421, 86.022, 79.4049, 73.7331, 68.8176, 64.5165, 60.7214, 27.899 |
| 2461107.57671 | 7220 | 8070 | 1036.2486 | 24 / 1036 | 1036.25, 518.124, 345.416, 259.062, 207.25, 172.708, 148.036, 129.531, 115.139, 103.625, 94.2044, 86.354, 79.7114, 74.0178, 69.0832, 64.7655, 51.8124, 49.3452, 47.1022, 45.0543 |
| 2461111.56307 | 8169 | 8070 | 1040.2349 | 20 / 1040 | 1040.23, 520.117, 346.745, 260.059, 208.047, 173.373, 148.605, 130.029, 115.582, 104.023, 94.5668, 86.6862, 80.0181, 74.3025, 69.349, 54.7492, 52.0117, 49.535, 35.8702, 11.9567 |
| 2461115.54804 | 7979 | 8070 | 1044.2199 | 19 / 1044 | 1044.22, 522.11, 348.073, 261.055, 208.844, 174.037, 149.174, 130.528, 116.024, 104.422, 94.9291, 87.0183, 80.3246, 74.5871, 69.6147, 58.0122, 54.9589, 41.7688, 7.9711 |
| 2461119.53230 | 7602 | 8070 | 1048.2041 | 17 / 1048 | 1048.2, 524.102, 349.401, 262.051, 209.641, 174.701, 149.743, 131.025, 116.467, 104.82, 95.2913, 87.3503, 80.6311, 74.8717, 61.6591, 58.2336, 45.5741 |
| 2461123.51515 | 8275 | 8070 | 1052.1870 | 23 / 1052 | 1052.19, 526.093, 350.729, 263.047, 210.437, 175.364, 150.312, 131.523, 116.91, 105.219, 95.6534, 87.6822, 80.9375, 65.7617, 61.8934, 50.1041, 47.8267, 43.8411, 31.8845, 23.9133 |
| 2461127.50424 | 5997 | 8070 | 1056.1761 | 15 / 1056 | 1056.18, 528.088, 352.059, 264.044, 211.235, 176.029, 150.882, 132.022, 117.353, 105.618, 96.016, 88.0147, 70.4117, 66.011, 19.9279 |
| 2461131.49124 | 8267 | 8070 | 1060.1631 | 19 / 1060 | 1060.16, 530.082, 353.388, 265.041, 212.033, 176.694, 151.452, 132.52, 117.796, 106.016, 96.3785, 88.3469, 75.7259, 70.6775, 55.7981, 44.1735, 37.863, 27.899, 7.9712 |
| 2461135.47613 | 8006 | 8070 | 1064.1480 | 14 / 1064 | 1064.15, 532.074, 354.716, 266.037, 212.83, 177.358, 152.021, 133.018, 118.239, 106.415, 96.7407, 76.0106, 48.3704, 11.9567 |
| 2461143.44448 | 7925 | 8070 | 1072.1163 | 14 / 1072 | 1072.12, 536.058, 357.372, 268.029, 214.423, 178.686, 153.16, 134.014, 119.124, 107.212, 97.4651, 82.4705, 56.4272, 42.8847 |
| 2461147.43210 | 7941 | 8070 | 1076.1039 | 20 / 1076 | 1076.1, 538.052, 358.701, 269.026, 215.221, 179.351, 153.729, 134.513, 119.567, 107.61, 89.6753, 71.7403, 59.7836, 53.8052, 39.8557, 35.8701, 23.9134, 19.9279, 11.9567, 7.9711 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6564.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:17:08Z: TOI-6564 b (host TOI-6564)
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:17:09Z: TOI-6564.01 (TIC 453668803, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:17:10Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:17:11Z: TYC 8667-818-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460071.3702: recovered, depth 8070 ± 74 ppm (catalogue 8801 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 40%, 10%, 50%, 40%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 28 repeat-candidate event(s); first at BJD 2460075.3542, ΔT = 4.026 d, 0 of 4 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6564.01: Gaia DR3 6064308867810722560 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6564.01: dwarf priors not applied — 1.37 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6564.01: 123 Gaia neighbour(s) within 52.5", contamination 6.08%; depth 8070 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 6064308970889937408, 17.4", ΔG 4.84); a centroid test is needed |
| Pointing and quality census per event | failed | 34 persistent event(s), 15 clean; BJD 2460075.3542 suspect: SAP_BKG z=+60.7; BJD 2460079.3396 suspect: SAP_BKG z=+12.7; BJD 2460083.2500 suspect: manual exclude (in event), MOM_CENTR1 z=-5.3, POS_CORR1 z=-6.3; BJD 2460083.3326 suspect: manual exclude (within ±0.25 d), MOM_CENTR1 z=-9.9, POS_CORR1 z=-8.6 |
| Moving objects at screen-event epochs | inconclusive | 34 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-6564.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6564.01: TYC 8667-818-1 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6564-01.yaml
python -m cygnus.multi report campaigns/toi-6564-01.yaml
```
