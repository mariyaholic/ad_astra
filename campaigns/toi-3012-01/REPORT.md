<!-- cygnus:generated-draft -->
# Known-object test, TOI-3012.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3012-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #706, calibrate_screen #624, event_census #632, fetch_products #617, known_signal_recovery #627, moving_objects #634, period_aliases #633, prior_art #708, residual_screen #630, stellar_context #628, variability_guard #707
- Runner finished (UTC): 2026-09-26T10:14:07Z

## Bottom line

Positive control **inconclusive**: BJD 2459991.4597: partial, depth 38307 ± 2485 ppm (catalogue 63492 ppm).
Outside the catalogued epoch the screen left 423 threshold entries forming **90 distinct event(s)**, **69 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3012.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 437560683 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 141.416611 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -54.841235 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459991.459725 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 63491.9490893 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.0267639 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.7563 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-01-17 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | lightcurve | 62 | True | `2721d54c86075d9b` | True |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | lightcurve | 63 | False | `c96e15fd05aea53e` | True |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | lightcurve | 89 | False | `45c6e70a0c2bfcc2` | True |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | lightcurve | 90 | False | `45d23eee9523edb8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2459991.45972 | partial | 121 | 38307 ± 2485 | 63492 | -1.65 |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 63492 | — |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | — | epoch not in this light curve | — | — | 63492 | — |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 63492 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.35927 | -0.14668 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460764.45786 | -0.14042 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460773.71262 | -0.13751 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460000.71820 | -0.13277 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.38010 | -0.12684 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460773.73623 | -0.12514 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460770.57308 | -0.12258 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460758.25581 | -0.12215 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460752.03359 | -0.12208 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.32802 | -0.12158 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460764.43217 | -0.12066 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 2460028.52327 | -0.12055 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 2460031.70451 | -0.12032 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460755.15443 | -0.12028 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460758.21136 | -0.11892 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460770.61475 | -0.11781 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460748.99469 | -0.11770 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 2460034.71074 | -0.11707 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460000.72862 | -0.11658 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460770.66127 | -0.11493 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460752.08845 | -0.11492 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.32038 | -0.11381 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460748.96274 | -0.11339 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460755.13498 | -0.11289 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460767.52381 | -0.11186 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.36482 | -0.11114 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460752.12387 | -0.10861 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460767.57867 | -0.10789 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460752.06762 | -0.10706 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 2460016.17950 | -0.10586 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460773.72234 | -0.10480 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460770.63627 | -0.10447 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2459994.51322 | -0.10129 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2459994.54239 | -0.10115 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460003.84117 | -0.10058 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.38496 | -0.10024 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460003.77728 | -0.09931 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460736.64874 | -0.09386 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460006.92178 | -0.09295 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.92522 | -0.09134 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460727.33747 | -0.09093 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.88633 | -0.08916 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.40419 | -0.08554 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.91272 | -0.08504 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460733.54174 | -0.08349 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460736.61541 | -0.08193 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460736.66332 | -0.08113 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.38197 | -0.07925 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460733.46674 | -0.07901 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.47086 | -0.07887 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460742.76548 | -0.07820 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.91828 | -0.07745 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.93633 | -0.07745 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.84328 | -0.07705 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460736.64318 | -0.07632 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.41669 | -0.07545 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460733.53619 | -0.07509 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460733.48202 | -0.07473 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460745.85994 | -0.07441 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460721.13454 | -0.07284 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460727.29858 | -0.07152 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460724.22907 | -0.07129 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.48544 | -0.07094 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460736.57929 | -0.07000 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.39863 | -0.06904 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460721.17760 | -0.06840 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460721.18593 | -0.06598 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460724.26934 | -0.06531 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460730.47989 | -0.06419 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460764.47383 | -0.12813 | 2 | PDCSAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460773.68623 | -0.12054 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460755.19054 | -0.12044 | 2 | PDCSAP | 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460764.40022 | -0.11252 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460764.37939 | -0.10872 | 2 | PDCSAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460773.73067 | -0.10846 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460764.42245 | -0.10613 | 2 | PDCSAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460000.68834 | -0.10516 | 2 | PDCSAP | 3 | no |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460000.71334 | -0.10413 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460770.60155 | -0.10329 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460742.83631 | -0.07209 | 2 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460742.84187 | -0.06800 | 2 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460724.25545 | -0.06452 | 2 | PDCSAP+SAP | 2 | no |
| `tess2025042113628-s0089-0000000437560683-0286-s_lc.fits` | 2460721.11093 | -0.06370 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460775.00913 | -0.04901 | 3 | SAP | 1, 2, 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460768.17241 | -0.04729 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000437560683-0255-s_lc.fits` | 2460031.69271 | -0.04622 | 2 | SAP | 2 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460767.56686 | -0.04394 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000437560683-0287-s_lc.fits` | 2460761.29468 | -0.04222 | 2 | SAP | 1 | no |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460013.10934 | -0.03685 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000437560683-0254-s_lc.fits` | 2460013.06351 | -0.03527 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3012.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:14:04Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:14:05Z: TOI-3012.01 (TIC 437560683, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:14:07Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:14:07Z: ** TOI 3012B (*); ** TOI 3012A (*); TOI-3012 (**)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2459991.4597: partial, depth 38307 ± 2485 ppm (catalogue 63492 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3012.01: Gaia DR3 5310465760018011136 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3012.01: dwarf priors not applied — parallax/error 1.8 < 5; RUWE 39.819473 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3012.01: 184 Gaia neighbour(s) within 52.5", contamination 84.86%; depth 63492 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 5310465725658272512, 46.3", ΔG 0.47); a centroid test is needed |
| Pointing and quality census per event | failed | 69 persistent event(s), 46 clean; BJD 2459994.5132 suspect: MOM_CENTR1 z=-6.7; BJD 2460000.7182 suspect: POS_CORR1 z=+5.1, POS_CORR2 z=+10.9, SAP_BKG z=+232.1; BJD 2460000.7286 suspect: POS_CORR2 z=+11.0, SAP_BKG z=+254.6; BJD 2460006.9218 suspect: manual exclude (in event) |
| Moving objects at screen-event epochs | inconclusive | 69 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 12 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3012.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3012.01: ** TOI 3012A otype * (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3012-01.yaml
python -m cygnus.multi report campaigns/toi-3012-01.yaml
```
