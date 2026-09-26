<!-- [private Drive store] -->
# Known-object test, TOI-447.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-447-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #316, calibrate_screen #80, event_census #106, fetch_products #75, known_signal_recovery #83, moving_objects #306, period_aliases #107, prior_art #318, residual_screen #93, stellar_context #84, variability_guard #317
- Runner finished (UTC): 2026-09-26T10:01:15Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-447.01 (BJD 2459176.3193: recovered, depth 9895 ± 278 ppm (catalogue 17914 ppm)).
Outside the catalogued epoch the screen left 309 threshold entries forming **115 distinct event(s)**, **35 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459181.8469 matches the catalogued transit's depth (9675 vs 9895 ppm), 5.528 d later; 0 of 5 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-447.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 14091633 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 77.260156 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -36.464478 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459176.31925 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 17914.4576673 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.542935 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.8695 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | lightcurve | 32 | True | `2175b3b0c189b832` | True |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | lightcurve | 5 | False | `1190308dec7618b7` | True |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | lightcurve | 6 | False | `c8ff5d12facd87de` | True |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | lightcurve | 98 | False | `a95f198012042a8e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459176.31925 | recovered | 77 | 9895 ± 278 | 17914 | -0.02 |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | — | epoch not in this light curve | — | — | 17914 | — |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | — | epoch not in this light curve | — | — | 17914 | — |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | — | epoch not in this light curve | — | — | 17914 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461045.17492 | -0.01907 | 34 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458452.00834 | -0.01842 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458457.52154 | -0.01653 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461045.22006 | -0.01623 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461028.60586 | -0.01622 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459192.90661 | -0.01603 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458446.46250 | -0.01600 | 65 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2460995.43090 | -0.01588 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461023.07676 | -0.01581 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461017.55042 | -0.01530 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459187.37538 | -0.01515 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461012.01851 | -0.01491 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459198.43849 | -0.01473 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458463.05206 | -0.01471 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458485.16626 | -0.01399 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.10886 | -0.01388 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458451.96598 | -0.01384 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459181.84691 | -0.01380 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458468.58048 | -0.01377 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461000.96222 | -0.01372 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458440.93397 | -0.01353 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458479.63861 | -0.01333 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000014091633-0298-s_lc.fits` | 2461039.66605 | -0.01318 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.77829 | -0.00630 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458476.18521 | -0.00611 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.40663 | -0.00603 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.76996 | -0.00600 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.33372 | -0.00573 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.73941 | -0.00556 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.79079 | -0.00553 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458479.04626 | -0.00536 | 4 | PDCSAP+SAP | 1, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.36705 | -0.00532 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.75816 | -0.00531 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458439.18672 | -0.00530 | 2 | PDCSAP+SAP | 1, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.41844 | -0.00512 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459200.03985 | -0.00764 | 11 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.95860 | -0.00728 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.99124 | -0.00726 | 7 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.94194 | -0.00713 | 2 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459200.05305 | -0.00698 | 2 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.99888 | -0.00684 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459200.02805 | -0.00672 | 2 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.98291 | -0.00666 | 3 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459200.05999 | -0.00666 | 2 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459200.02388 | -0.00661 | 2 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.89541 | -0.00657 | 3 | PDCSAP | 1, 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.32266 | -0.00650 | 2 | SAP | 1, 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.22752 | -0.00640 | 5 | SAP | 1, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459200.00513 | -0.00640 | 3 | PDCSAP | 1, 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.06149 | -0.00639 | 4 | PDCSAP+SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.07955 | -0.00634 | 6 | PDCSAP+SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.13372 | -0.00629 | 4 | PDCSAP+SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459199.88846 | -0.00625 | 3 | PDCSAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458479.08654 | -0.00625 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.35177 | -0.00607 | 2 | SAP | 1, 2, 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.24419 | -0.00582 | 3 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.25391 | -0.00580 | 3 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.26155 | -0.00573 | 4 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.96293 | -0.00567 | 2 | PDCSAP | 1, 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.24905 | -0.00552 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.03649 | -0.00548 | 2 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.80885 | -0.00545 | 2 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458479.00876 | -0.00543 | 2 | PDCSAP | 1, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.30733 | -0.00541 | 2 | SAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.16983 | -0.00540 | 2 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.21711 | -0.00536 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.26983 | -0.00533 | 2 | SAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.47816 | -0.00532 | 2 | SAP | 2, 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.23516 | -0.00531 | 2 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.79635 | -0.00531 | 2 | PDCSAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.38719 | -0.00530 | 3 | SAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.01705 | -0.00529 | 2 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458474.78524 | -0.00519 | 4 | PDCSAP+SAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.46288 | -0.00519 | 2 | SAP | 2, 3 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458479.05598 | -0.00518 | 2 | PDCSAP | 1, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.10733 | -0.00517 | 4 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458479.03654 | -0.00514 | 2 | PDCSAP | 1, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.10038 | -0.00513 | 4 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.26711 | -0.00513 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.45733 | -0.00509 | 2 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.12816 | -0.00505 | 2 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.41149 | -0.00504 | 2 | SAP | 2, 3 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458439.15200 | -0.00504 | 2 | PDCSAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459179.95455 | -0.00502 | 2 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.22122 | -0.00501 | 2 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.31849 | -0.00500 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.18858 | -0.00499 | 3 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.07052 | -0.00497 | 3 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458478.28794 | -0.00496 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.01011 | -0.00493 | 2 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.14205 | -0.00491 | 6 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.37608 | -0.00490 | 3 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.18094 | -0.00490 | 2 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.16566 | -0.00485 | 2 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.15941 | -0.00484 | 5 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459184.32955 | -0.00483 | 2 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.09413 | -0.00481 | 3 | SAP | 2 | no |
| `tess2020324010417-s0032-0000000014091633-0200-s_lc.fits` | 2459180.11566 | -0.00480 | 2 | SAP | 2 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458468.35340 | -0.00414 | 2 | PDCSAP | 1 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458476.21021 | -0.00409 | 2 | PDCSAP | 1 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458476.23035 | -0.00387 | 3 | PDCSAP | 1 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458476.17549 | -0.00381 | 2 | PDCSAP | 1 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458487.61966 | -0.00376 | 2 | PDCSAP | 1 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458480.41012 | -0.00367 | 2 | SAP | 1 | no |
| `tess2018349182500-s0006-0000000014091633-0126-s_lc.fits` | 2458480.55317 | -0.00362 | 2 | SAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458449.10695 | -0.00361 | 3 | PDCSAP+SAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458447.81042 | -0.00358 | 2 | PDCSAP+SAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458456.28682 | -0.00353 | 2 | PDCSAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458463.30761 | -0.00349 | 2 | PDCSAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458449.15070 | -0.00336 | 2 | PDCSAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458449.07848 | -0.00325 | 2 | PDCSAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458449.12014 | -0.00319 | 2 | PDCSAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458447.76111 | -0.00318 | 3 | PDCSAP+SAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458447.82014 | -0.00315 | 2 | PDCSAP | 1 | no |
| `tess2018319095959-s0005-0000000014091633-0125-s_lc.fits` | 2458449.18959 | -0.00291 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459181.84691 | 9675 | 9895 | 5.5285 | 0 / 5 |  |
| 2459184.36705 | 5137 | 9895 | 8.0486 | 0 / 8 |  |
| 2459187.37538 | 11536 | 9895 | 11.0570 | 0 / 11 |  |
| 2459192.90661 | 12424 | 9895 | 16.5882 | 0 / 16 |  |
| 2459198.43849 | 11124 | 9895 | 22.1201 | 0 / 22 |  |
| 2458440.93397 | 9521 | 9895 | 735.3844 | 8 / 735 | 735.384, 245.128, 147.077, 105.055, 81.7094, 66.8531, 38.7044, 5.5292 |
| 2458446.46250 | 13310 | 9895 | 729.8559 | 18 / 729 | 729.856, 364.928, 243.285, 182.464, 145.971, 121.643, 104.265, 91.232, 72.9856, 66.3505, 60.8213, 52.1326, 45.616, 33.1753, 22.1168, 16.5876, 11.0584, 5.5292 |
| 2458451.96598 | 13841 | 9895 | 724.3524 | 13 / 724 | 724.352, 362.176, 241.451, 181.088, 144.87, 120.725, 90.5441, 72.4352, 65.8502, 60.3627, 45.272, 42.609, 31.4936 |
| 2458452.00834 | 13972 | 9895 | 724.3101 | 15 / 724 | 724.31, 362.155, 241.437, 181.077, 144.862, 120.718, 103.473, 90.5388, 72.431, 65.8464, 60.3592, 51.7364, 45.2694, 42.6065, 31.4917 |
| 2458457.52154 | 13099 | 9895 | 718.7969 | 16 / 718 | 718.797, 359.398, 239.599, 179.699, 143.759, 119.799, 89.8496, 71.8797, 65.3452, 59.8997, 55.2921, 44.9248, 32.6726, 27.646, 11.0584, 5.5292 |
| 2458463.05206 | 10919 | 9895 | 713.2664 | 13 / 713 | 713.266, 356.633, 237.756, 178.317, 118.878, 89.1583, 64.8424, 59.4389, 44.5791, 32.4212, 29.7194, 16.5876, 5.5292 |
| 2458468.58048 | 9870 | 9895 | 707.7379 | 14 / 707 | 707.738, 353.869, 235.913, 176.935, 117.956, 88.4672, 78.6375, 58.9782, 44.2336, 39.3188, 29.4891, 22.1168, 11.0584, 5.5292 |
| 2458474.10886 | 10198 | 9895 | 702.2096 | 13 / 702 | 702.21, 351.105, 234.07, 175.552, 117.035, 100.316, 87.7762, 78.0233, 58.5175, 43.8881, 39.0116, 36.9584, 5.5292 |
| 2458474.73941 | 5024 | 9895 | 701.5790 | 10 / 701 | 701.579, 350.789, 233.86, 175.395, 116.93, 100.226, 87.6974, 77.9532, 43.8487, 41.2694 |
| 2458474.75816 | 5025 | 9895 | 701.5603 | 10 / 701 | 701.56, 350.78, 233.853, 175.39, 116.927, 100.223, 87.695, 77.9511, 43.8475, 41.2683 |
| 2458474.76996 | 5025 | 9895 | 701.5485 | 10 / 701 | 701.548, 350.774, 233.85, 175.387, 116.925, 100.221, 87.6936, 77.9498, 43.8468, 41.2676 |
| 2458474.77829 | 5015 | 9895 | 701.5401 | 10 / 701 | 701.54, 350.77, 233.847, 175.385, 116.923, 100.22, 87.6925, 77.9489, 43.8463, 41.2671 |
| 2458474.79079 | 4978 | 9895 | 701.5276 | 10 / 701 | 701.528, 350.764, 233.843, 175.382, 116.921, 100.218, 87.691, 77.9475, 43.8455, 41.2663 |
| 2458479.04626 | 4961 | 9895 | 697.2722 | 10 / 697 | 697.272, 348.636, 174.318, 139.454, 99.6103, 87.159, 69.7272, 53.6363, 49.8052, 43.5795 |
| 2458479.63861 | 8346 | 9895 | 696.6798 | 21 / 696 | 696.68, 348.34, 232.227, 174.17, 139.336, 116.113, 99.5257, 87.085, 77.4089, 69.668, 58.0567, 53.5908, 49.7628, 46.4453, 43.5425, 38.7044, 33.1752, 29.0283, 16.5876, 11.0584 |
| 2458485.16626 | 11328 | 9895 | 691.1522 | 15 / 691 | 691.152, 345.576, 230.384, 172.788, 138.23, 115.192, 98.736, 86.394, 76.7947, 62.832, 57.596, 49.368, 46.0768, 27.6461, 5.5292 |
| 2460995.43090 | 13383 | 9895 | 1819.1125 | 23 / 1819 | 1819.11, 909.556, 606.371, 454.778, 303.185, 259.873, 227.389, 202.124, 165.374, 151.593, 129.937, 113.695, 107.007, 95.7428, 86.6244, 82.6869, 79.0918, 75.7964, 67.3745, 56.8473 |
| 2461000.96222 | 9609 | 9895 | 1824.6438 | 35 / 1824 | 1824.64, 912.322, 608.215, 456.161, 364.929, 304.107, 260.663, 228.081, 202.738, 182.464, 165.877, 152.054, 130.332, 121.643, 114.04, 107.332, 101.369, 96.0339, 91.2322, 82.9384 |
| 2461012.01851 | 10658 | 9895 | 1835.7001 | 21 / 1835 | 1835.7, 917.85, 611.9, 458.925, 305.95, 262.243, 203.967, 166.882, 152.975, 131.121, 107.982, 96.6158, 83.4409, 67.9889, 59.2161, 42.6907, 41.7205, 37.4633, 22.1169, 11.0584 |
| 2461017.55042 | 11795 | 9895 | 1841.2320 | 27 / 1841 | 1841.23, 920.616, 613.744, 460.308, 306.872, 263.033, 204.581, 167.385, 153.436, 141.633, 131.517, 108.308, 96.9069, 87.6777, 83.6924, 70.8166, 68.1938, 63.4908, 55.7949, 49.763 |
| 2461023.07676 | 12372 | 9895 | 1846.7583 | 29 / 1846 | 1846.76, 923.379, 615.586, 461.69, 369.352, 307.793, 263.823, 205.195, 184.676, 167.887, 153.897, 142.058, 131.911, 123.117, 108.633, 97.1978, 92.3379, 83.9436, 73.8703, 71.0292 |
| 2461028.60586 | 13547 | 9895 | 1852.2874 | 30 / 1852 | 1852.29, 926.144, 617.429, 463.072, 370.457, 308.715, 264.613, 205.81, 185.229, 168.39, 154.357, 142.484, 132.306, 123.486, 108.958, 97.4888, 92.6144, 84.1949, 80.5342, 74.0915 |
| 2461039.66605 | 8423 | 9895 | 1863.3476 | 27 / 1863 | 1863.35, 931.674, 621.116, 465.837, 372.67, 310.558, 266.192, 232.918, 207.039, 186.335, 169.395, 155.279, 133.096, 124.223, 116.459, 109.609, 93.1674, 88.7308, 84.6976, 77.6395 |
| 2461045.17492 | 14791 | 9895 | 1868.8565 | 24 / 1868 | 1868.86, 934.428, 622.952, 467.214, 373.771, 311.476, 266.979, 207.651, 186.886, 169.896, 155.738, 143.758, 133.49, 124.59, 109.933, 93.4428, 88.9932, 84.948, 74.7543, 71.8791 |
| 2461045.22006 | 14504 | 9895 | 1868.9016 | 25 / 1868 | 1868.9, 934.451, 622.967, 467.225, 373.78, 311.484, 266.986, 207.656, 186.89, 169.9, 155.742, 143.762, 133.493, 124.593, 109.935, 93.4451, 88.9953, 84.9501, 74.7561, 71.8808 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-447.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:01:11Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:01:13Z: TOI-447.01 (TIC 14091633, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:01:14Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:01:14Z: TOI-447.01 (err); HD  33512 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459176.3193: recovered, depth 9895 ± 278 ppm (catalogue 17914 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 30%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 30 repeat-candidate event(s); first at BJD 2459181.8469, ΔT = 5.528 d, 0 of 5 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-447.01: Gaia DR3 4823999931341640832 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-447.01: Teff 6413 K, R* 1.30 ± 0.10, M* 1.20 ± 0.12, ρ* 0.55 ± 0.14 ρ☉ (dwarf sequence, M_G 3.73, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-447.01: 6 Gaia neighbour(s) within 52.5", contamination 15.57%; depth 9895 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4823999931341641600, 30.4", ΔG 1.84); a centroid test is needed |
| Pointing and quality census per event | failed | 35 persistent event(s), 14 clean; BJD 2459187.3754 suspect: MOM_CENTR1 z=+28.5, MOM_CENTR2 z=-24.6, POS_CORR1 z=+25.8, POS_CORR2 z=-25.4, SAP_BKG z=+14.3; BJD 2458439.1867 suspect: manual exclude (in event); BJD 2458440.9340 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2458451.9660 suspect: manual exclude (in event), MOM_CENTR2 z=-7.3, POS_CORR2 z=-7.0 |
| Moving objects at screen-event epochs | inconclusive | 35 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 7 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-447.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-447.01: HD  33512 otype SB* (multiple) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-447-01.yaml
python -m cygnus.multi report campaigns/toi-447-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit.** No new signal.

Source: `campaigns/toi-447-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
