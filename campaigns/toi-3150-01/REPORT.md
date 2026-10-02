<!-- cygnus:generated-draft -->
# Known-object test, TOI-3150.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3150-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4283, calibrate_screen #4260, event_census #4267, fetch_independent #4273, fetch_products #4247, known_signal_recovery #4261, moving_objects #4270, period_aliases #4268, prior_art #4285, residual_screen #4266, stellar_context #4264, variability_guard #4284
- Runner finished (UTC): 2026-09-30T21:45:41Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3150.01 (BJD 2460073.8022: recovered, depth 8126 ± 371 ppm (catalogue 7220 ppm); BJD 2460079.1453: partial, depth 7661 ± 393 ppm (catalogue 7220 ppm); BJD 2460084.4883: recovered, depth 7574 ± 344 ppm (catalogue 7220 ppm); BJD 2460089.8314: recovered, depth 8059 ± 380 ppm (catalogue 7220 ppm); BJD 2460095.1745: partial, depth 8508 ± 410 ppm (catalogue 7220 ppm); BJD 2461046.2403: not recovered, depth 6067 ± 499 ppm (catalogue 7220 ppm); BJD 2461051.5833: recovered, depth 7904 ± 470 ppm (catalogue 7220 ppm); BJD 2461056.9264: gap (catalogue 7220 ppm); BJD 2461062.2695: gap (catalogue 7220 ppm); BJD 2461067.6125: not recovered, depth 7395 ± 432 ppm (catalogue 7220 ppm); BJD 2461072.9556: recovered, depth 7571 ± 554 ppm (catalogue 7220 ppm); BJD 2461078.2987: recovered, depth 7862 ± 414 ppm (catalogue 7220 ppm); BJD 2461083.6417: recovered, depth 7855 ± 437 ppm (catalogue 7220 ppm); BJD 2461088.9848: recovered, depth 7695 ± 465 ppm (catalogue 7220 ppm); BJD 2461094.3279: not recovered, depth 5080 ± 627 ppm (catalogue 7220 ppm); BJD 2461099.6709: partial, depth 418 ± 483 ppm (catalogue 7220 ppm); BJD 2461105.0140: recovered, depth 7636 ± 437 ppm (catalogue 7220 ppm); BJD 2461110.3571: recovered, depth 6575 ± 458 ppm (catalogue 7220 ppm); BJD 2461115.7001: recovered, depth 8751 ± 451 ppm (catalogue 7220 ppm); BJD 2461121.0432: recovered, depth 7107 ± 446 ppm (catalogue 7220 ppm); BJD 2461126.3863: gap (catalogue 7220 ppm); BJD 2461131.7293: partial, depth 7581 ± 401 ppm (catalogue 7220 ppm); BJD 2461137.0724: recovered, depth 6521 ± 419 ppm (catalogue 7220 ppm); BJD 2461142.4155: partial, depth 6373 ± 421 ppm (catalogue 7220 ppm); BJD 2461147.7585: partial, depth 7357 ± 404 ppm (catalogue 7220 ppm)).
Outside the catalogued epoch the screen left 99 threshold entries forming **48 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461125.2890 matches the catalogued transit's depth (4908 vs 8126 ppm), 1051.454 d later; 15 of 1051 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3150.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 195256633 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 222.683091 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -57.761231 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459357.83131 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.3430663 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 7220.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.101 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.0697 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | lightcurve | 65 | False | `f824d313d689fad8` | True |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | lightcurve | 99 | False | `4af1e3064896f4bb` | True |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | lightcurve | 100 | False | `351f7a094eff72bf` | True |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | lightcurve | 101 | False | `b7c86e395f4811f3` | True |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | lightcurve | 102 | False | `be7b22eb04d5614e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460073.80219 | recovered | 153 | 8126 ± 371 | 7220 | 0.78 |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460079.14526 | partial | 153 | 7661 ± 393 | 7220 | -1.03 |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460084.48833 | recovered | 153 | 7574 ± 344 | 7220 | 0.25 |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460089.83139 | recovered | 145 | 8059 ± 380 | 7220 | 0.09 |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460095.17446 | partial | 153 | 8508 ± 410 | 7220 | 1.05 |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461046.24026 | not_recovered | 153 | 6067 ± 499 | 7220 | — |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461051.58333 | recovered | 153 | 7904 ± 470 | 7220 | 0.21 |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461056.92639 | gap | 0 | — | 7220 | — |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461062.26946 | gap | 0 | — | 7220 | — |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461067.61253 | not_recovered | 153 | 7395 ± 432 | 7220 | — |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461072.95559 | recovered | 136 | 7571 ± 554 | 7220 | 0.71 |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461078.29866 | recovered | 153 | 7862 ± 414 | 7220 | -0.65 |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461083.64172 | recovered | 153 | 7855 ± 437 | 7220 | 1.23 |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461088.98479 | recovered | 153 | 7695 ± 465 | 7220 | -0.06 |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461094.32786 | not_recovered | 80 | 5080 ± 627 | 7220 | — |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461099.67092 | partial | 153 | 418 ± 483 | 7220 | 1.86 |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461105.01399 | recovered | 153 | 7636 ± 437 | 7220 | 0.30 |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461110.35706 | recovered | 153 | 6575 ± 458 | 7220 | 0.46 |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461115.70012 | recovered | 153 | 8751 ± 451 | 7220 | 0.97 |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461121.04319 | recovered | 153 | 7107 ± 446 | 7220 | 0.73 |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461126.38626 | gap | 0 | — | 7220 | — |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461131.72932 | partial | 153 | 7581 ± 401 | 7220 | 0.02 |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461137.07239 | recovered | 153 | 6521 ± 419 | 7220 | 0.58 |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461142.41545 | partial | 153 | 6373 ± 421 | 7220 | 0.69 |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461147.75852 | partial | 153 | 7357 ± 404 | 7220 | 1.03 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461125.28896 | -0.01840 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461125.32091 | -0.01816 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461106.79325 | -0.01624 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461129.21423 | -0.01454 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461125.12507 | -0.02025 | 2 | PDCSAP | 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461125.64732 | -0.01859 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461146.23873 | -0.01840 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461125.27230 | -0.01697 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460083.25298 | -0.01662 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461133.74088 | -0.01533 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461140.41345 | -0.01471 | 2 | PDCSAP | 2 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461151.31670 | -0.01467 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461151.35004 | -0.01438 | 3 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461144.92895 | -0.01429 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461146.29151 | -0.01426 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461133.42975 | -0.01415 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461140.65791 | -0.01412 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461140.21899 | -0.01406 | 2 | PDCSAP | 1 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461145.67760 | -0.01330 | 2 | SAP | 1 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461133.26308 | -0.01325 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461114.60908 | -0.01288 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461093.52558 | -0.01244 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461151.09170 | -0.01244 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461146.24429 | -0.01217 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461133.21585 | -0.01195 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460096.18486 | -0.01194 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460083.15159 | -0.01185 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461146.23457 | -0.01160 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461151.40004 | -0.01156 | 2 | SAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461133.34503 | -0.01151 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461146.41235 | -0.01124 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460083.06409 | -0.01124 | 2 | SAP | 2 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461133.12696 | -0.01116 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461119.86223 | -0.01113 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460083.20715 | -0.01104 | 2 | SAP | 2 | no |
| `tess2023124020739-s0065-0000000195256633-0259-s_lc.fits` | 2460096.23764 | -0.01098 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461101.52826 | -0.01080 | 3 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461144.86228 | -0.01079 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461119.82056 | -0.01070 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461145.34564 | -0.01068 | 2 | SAP | 1, 2 | no |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461087.55427 | -0.01065 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461101.72272 | -0.01058 | 3 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000195256633-0304-s_lc.fits` | 2461145.68176 | -0.01049 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000195256633-0300-s_lc.fits` | 2461073.72822 | -0.01035 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461111.84777 | -0.01020 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461101.57201 | -0.01007 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000195256633-0303-s_lc.fits` | 2461114.88688 | -0.01005 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000195256633-0302-s_lc.fits` | 2461087.50148 | -0.00951 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461125.28896 | 4908 | 8126 | 1051.4541 | 15 / 1051 | 1051.45, 525.727, 350.485, 262.863, 210.291, 175.242, 150.208, 131.432, 116.828, 105.145, 95.5867, 87.6212, 80.8811, 65.7159, 36.257 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3150.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:45:33Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:45:36Z: TOI-3150.01 (TIC 195256633, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:45:38Z: Gaia DR3 5880704955815832960 (type VAR, P 0.015501 d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:45:40Z: Gaia DR3 5880704955815832960 (*); TOI-3150 (*); TOI-3150.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460073.8022: recovered, depth 8126 ± 371 ppm (catalogue 7220 ppm); BJD 2460079.1453: partial, depth 7661 ± 393 ppm (catalogue 7220 ppm); BJD 2460084.4883: recovered, depth 7574 ± 344 ppm (catalogue 7220 ppm); BJD 2460089.8314: recovered, depth 8059 ± 380 ppm (catalogue 7220 ppm); BJD 2460095.1745: partial, depth 8508 ± 410 ppm (catalogue 7220 ppm); BJD 2461046.2403: not recovered, depth 6067 ± 499 ppm (catalogue 7220 ppm); BJD 2461051.5833: recovered, depth 7904 ± 470 ppm (catalogue 7220 ppm); BJD 2461056.9264: gap (catalogue 7220 ppm); BJD 2461062.2695: gap (catalogue 7220 ppm); BJD 2461067.6125: not recovered, depth 7395 ± 432 ppm (catalogue 7220 ppm); BJD 2461072.9556: recovered, depth 7571 ± 554 ppm (catalogue 7220 ppm); BJD 2461078.2987: recovered, depth 7862 ± 414 ppm (catalogue 7220 ppm); BJD 2461083.6417: recovered, depth 7855 ± 437 ppm (catalogue 7220 ppm); BJD 2461088.9848: recovered, depth 7695 ± 465 ppm (catalogue 7220 ppm); BJD 2461094.3279: not recovered, depth 5080 ± 627 ppm (catalogue 7220 ppm); BJD 2461099.6709: partial, depth 418 ± 483 ppm (catalogue 7220 ppm); BJD 2461105.0140: recovered, depth 7636 ± 437 ppm (catalogue 7220 ppm); BJD 2461110.3571: recovered, depth 6575 ± 458 ppm (catalogue 7220 ppm); BJD 2461115.7001: recovered, depth 8751 ± 451 ppm (catalogue 7220 ppm); BJD 2461121.0432: recovered, depth 7107 ± 446 ppm (catalogue 7220 ppm); BJD 2461126.3863: gap (catalogue 7220 ppm); BJD 2461131.7293: partial, depth 7581 ± 401 ppm (catalogue 7220 ppm); BJD 2461137.0724: recovered, depth 6521 ± 419 ppm (catalogue 7220 ppm); BJD 2461142.4155: partial, depth 6373 ± 421 ppm (catalogue 7220 ppm); BJD 2461147.7585: partial, depth 7357 ± 404 ppm (catalogue 7220 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 20%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2461125.2890, ΔT = 1051.454 d, 15 of 1051 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1051.45, 525.727, 350.485, 262.863, 210.291, 175.242, 150.208, 131.432, 116.828, 105.145, 95.5867, 87.6212 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3150.01: Gaia DR3 5880704990174696704 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3150.01: dwarf priors not applied — RUWE 1.4868411 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3150.01: 184 Gaia neighbour(s) within 52.5", contamination 43.39%; depth 8126 ppm (measured depth of the recovered catalogued transit); 8 could produce it if fully eclipsed (brightest 5880704960142890112, 20.4", ΔG 1.89); a centroid test is needed |
| Pointing and quality census per event | failed | 4 persistent event(s), 2 clean; BJD 2461125.2890 suspect: SAP_BKG z=+312.7; BJD 2461125.3209 suspect: SAP_BKG z=+332.3 |
| Moving objects at screen-event epochs | inconclusive | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3150.01: Gaia DR3 5880704955815832960   VAR                            P=0.015501 at 8.8" |
| Object-class guard (SIMBAD) | passed | TOI-3150.01: TOI-3150 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3150-01.yaml
python -m cygnus.multi report campaigns/toi-3150-01.yaml
```
