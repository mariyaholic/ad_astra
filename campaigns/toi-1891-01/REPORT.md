<!-- cygnus:generated-draft -->
# Known-object test, TOI-1891.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1891-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5130, calibrate_screen #5101, event_census #5109, fetch_independent #5127, fetch_products #5090, known_signal_recovery #5103, moving_objects #5124, period_aliases #5110, prior_art #5132, residual_screen #5106, stellar_context #5104, variability_guard #5131
- Runner finished (UTC): 2026-09-30T23:03:31Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1891.01 (BJD 2460161.1424: recovered, depth 3238 ± 96 ppm (catalogue 3321 ppm); BJD 2460176.5042: recovered, depth 3066 ± 93 ppm (catalogue 3321 ppm); BJD 2458333.0914: recovered, depth 2646 ± 102 ppm (catalogue 3321 ppm); BJD 2458348.4532: partial, depth 1697 ± 200 ppm (catalogue 3321 ppm); BJD 2459070.4565: recovered, depth 2648 ± 95 ppm (catalogue 3321 ppm); BJD 2459085.8183: gap (catalogue 3321 ppm); BJD 2460883.1457: recovered, depth 2087 ± 97 ppm (catalogue 3321 ppm); BJD 2460898.5075: recovered, depth 3073 ± 97 ppm (catalogue 3321 ppm); BJD 2460913.8693: recovered, depth 3108 ± 98 ppm (catalogue 3321 ppm); BJD 2460929.2311: recovered, depth 3186 ± 91 ppm (catalogue 3321 ppm); BJD 2461205.7430: gap (catalogue 3321 ppm); BJD 2461221.1047: recovered, depth 2885 ± 108 ppm (catalogue 3321 ppm)).
Outside the catalogued epoch the screen left 181 threshold entries forming **82 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459072.0514 matches the catalogued transit's depth (2255 vs 3238 ppm), 1089.080 d later; 9 of 1089 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1891.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 139198430 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 345.630986 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -46.085195 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460176.504188 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 15.3617729 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 3321.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.745 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.3059 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-11-15 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000139198430-0262-s_lc.fits` | lightcurve | 68 | True | `3771dc6e47acd53e` | True |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | lightcurve | 1 | False | `8db3a87a3404194f` | True |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | lightcurve | 28 | False | `c27fd3c15243e71c` | True |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | lightcurve | 95 | False | `c6b30c58fab0213d` | True |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | lightcurve | 96 | False | `ac6078edd51ad322` | True |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | lightcurve | 105 | False | `a96acff776adf0b6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000139198430-0262-s_lc.fits` | 2460161.14242 | recovered | 53 | 3238 ± 96 | 3321 | -0.27 |
| `tess2023209231226-s0068-0000000139198430-0262-s_lc.fits` | 2460176.50419 | recovered | 52 | 3066 ± 93 | 3321 | 0.01 |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458333.09144 | recovered | 52 | 2646 ± 102 | 3321 | -0.04 |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458348.45321 | partial | 15 | 1697 ± 200 | 3321 | -0.42 |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 2459070.45654 | recovered | 52 | 2648 ± 95 | 3321 | 0.26 |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 2459085.81831 | gap | 0 | — | 3321 | — |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460883.14574 | recovered | 53 | 2087 ± 97 | 3321 | 0.02 |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460898.50751 | recovered | 52 | 3073 ± 97 | 3321 | -0.02 |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460913.86929 | recovered | 52 | 3108 ± 98 | 3321 | 0.07 |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460929.23106 | recovered | 52 | 3186 ± 91 | 3321 | -0.01 |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 2461205.74297 | gap | 0 | — | 3321 | — |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 2461221.10475 | recovered | 52 | 2885 ± 108 | 3321 | -0.00 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023209231226-s0068-0000000139198430-0262-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 2459072.05142 | -0.00365 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 2459071.97295 | -0.00302 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.91038 | -0.00612 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.14927 | -0.00575 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.96246 | -0.00562 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.75761 | -0.00511 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.51340 | -0.00484 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.81872 | -0.00480 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460899.84117 | -0.00470 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.42035 | -0.00453 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.58261 | -0.00449 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.03121 | -0.00444 | 4 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.26896 | -0.00444 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.52937 | -0.00434 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.73424 | -0.00425 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.07008 | -0.00423 | 4 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.90483 | -0.00411 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.00899 | -0.00411 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.53537 | -0.00408 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.38354 | -0.00405 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.13815 | -0.00394 | 4 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.74372 | -0.00388 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.39673 | -0.00384 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 2461224.52715 | -0.00381 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.11201 | -0.00377 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460933.28306 | -0.00376 | 5 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.03952 | -0.00376 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.85341 | -0.00374 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.80622 | -0.00372 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.11313 | -0.00371 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.13260 | -0.00366 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.09438 | -0.00366 | 3 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 2461231.16361 | -0.00363 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.14368 | -0.00361 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.44187 | -0.00360 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.57243 | -0.00357 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.97633 | -0.00355 | 4 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458349.10388 | -0.00355 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.42868 | -0.00355 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.63539 | -0.00354 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460932.79072 | -0.00354 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 2461224.33547 | -0.00353 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.99302 | -0.00351 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.48562 | -0.00349 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.10480 | -0.00348 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.15507 | -0.00344 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.47312 | -0.00344 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.85899 | -0.00343 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.96244 | -0.00339 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.12704 | -0.00331 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.59674 | -0.00323 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.46479 | -0.00321 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.55898 | -0.00320 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.45507 | -0.00317 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.44674 | -0.00315 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.76316 | -0.00314 | 2 | SAP | 2, 3 | no |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 2459072.06045 | -0.00312 | 2 | PDCSAP | 1 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460933.10320 | -0.00309 | 2 | SAP | 1, 2 | no |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458347.49208 | -0.00309 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460927.05549 | -0.00308 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460920.19244 | -0.00307 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000139198430-0307-s_lc.fits` | 2461230.28718 | -0.00305 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460899.92173 | -0.00293 | 2 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458339.73855 | -0.00292 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460920.25494 | -0.00290 | 2 | SAP | 1, 2 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.86175 | -0.00290 | 4 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.06340 | -0.00290 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.92983 | -0.00286 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.58146 | -0.00281 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460932.58100 | -0.00280 | 2 | SAP | 2 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.50203 | -0.00279 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.61870 | -0.00277 | 2 | SAP | 3 | no |
| `tess2020212050318-s0028-0000000139198430-0190-s_lc.fits` | 2459072.04309 | -0.00276 | 3 | PDCSAP | 1, 2 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.91872 | -0.00269 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458347.45388 | -0.00268 | 2 | SAP | 1 | no |
| `tess2018206045859-s0001-0000000139198430-0120-s_lc.fits` | 2458347.46083 | -0.00264 | 2 | SAP | 1, 2 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.30229 | -0.00263 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460925.97010 | -0.00262 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.67868 | -0.00260 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460920.09106 | -0.00253 | 2 | SAP | 2 | no |
| `tess2025206162959-s0095-0000000139198430-0292-s_lc.fits` | 2460900.21687 | -0.00253 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000139198430-0293-s_lc.fits` | 2460926.82841 | -0.00249 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459072.05142 | 2255 | 3238 | 1089.0796 | 9 / 1089 | 1089.08, 544.54, 272.27, 217.816, 155.583, 136.135, 99.0072, 77.7914, 31.1166 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1891.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:03:19Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:03:22Z: TOI-1891.01 (TIC 139198430, disposition APC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T23:03:26Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T23:03:28Z: HD 217596 (**); TOI-1891.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460161.1424: recovered, depth 3238 ± 96 ppm (catalogue 3321 ppm); BJD 2460176.5042: recovered, depth 3066 ± 93 ppm (catalogue 3321 ppm); BJD 2458333.0914: recovered, depth 2646 ± 102 ppm (catalogue 3321 ppm); BJD 2458348.4532: partial, depth 1697 ± 200 ppm (catalogue 3321 ppm); BJD 2459070.4565: recovered, depth 2648 ± 95 ppm (catalogue 3321 ppm); BJD 2459085.8183: gap (catalogue 3321 ppm); BJD 2460883.1457: recovered, depth 2087 ± 97 ppm (catalogue 3321 ppm); BJD 2460898.5075: recovered, depth 3073 ± 97 ppm (catalogue 3321 ppm); BJD 2460913.8693: recovered, depth 3108 ± 98 ppm (catalogue 3321 ppm); BJD 2460929.2311: recovered, depth 3186 ± 91 ppm (catalogue 3321 ppm); BJD 2461205.7430: gap (catalogue 3321 ppm); BJD 2461221.1047: recovered, depth 2885 ± 108 ppm (catalogue 3321 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3, 3.5, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 90%, 40%, 100%, 60%, 50% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459072.0514, ΔT = 1089.080 d, 9 of 1089 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1089.08, 544.54, 272.27, 217.816, 155.583, 136.135, 99.0072, 77.7914, 31.1166 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1891.01: Gaia DR3 6539676638373111552 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1891.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1891.01: 3 Gaia neighbour(s) within 52.5", contamination 0.19%; depth 3238 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2459071.9730 suspect: SAP_BKG z=+50.1; BJD 2459072.0514 suspect: SAP_BKG z=+39.0 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-1891.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-1891.01: HD 217596 otype ** (multiple) at 0.5" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1891-01.yaml
python -m cygnus.multi report campaigns/toi-1891-01.yaml
```
