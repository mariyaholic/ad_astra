<!-- [private Drive store] -->
# Known-object test, TOI-671.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-671-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #87, calibrate_screen #33, event_census #58, fetch_products #18, known_signal_recovery #43, moving_objects #60, period_aliases #59, prior_art #90, residual_screen #49, stellar_context #44, variability_guard #88
- Runner finished (UTC): 2026-09-26T09:54:19Z

## Bottom line

Positive control **inconclusive**: BJD 2460021.2902: gap (catalogue 16111 ppm).
Outside the catalogued epoch the screen left 387 threshold entries forming **166 distinct event(s)**, **24 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-671.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 151681127 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 166.888906 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -40.206918 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460021.290156 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16111.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.694 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.1379 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-05-11 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | lightcurve | 63 | True | `1cbf9b509290dada` | True |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | lightcurve | 9 | False | `711d13eb77f2e509` | True |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | lightcurve | 90 | False | `509c5f8ffc6e0ead` | True |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | lightcurve | 99 | False | `a50cea7fd8909152` | True |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | lightcurve | 100 | False | `1105870d0d4b68f7` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460021.29016 | gap | 0 | — | 16111 | — |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | — | epoch not in this light curve | — | — | 16111 | — |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 16111 | — |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 16111 | — |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 16111 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 2000, 8h: 5000 |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 5000, 4h: 2000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458563.12283 | -0.01464 | 124 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458552.91710 | -0.01440 | 136 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | 2460755.47558 | -0.01410 | 132 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461071.58459 | -0.01406 | 134 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461081.78104 | -0.01400 | 132 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461091.97877 | -0.01394 | 132 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460031.48754 | -0.01388 | 134 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461051.18944 | -0.01375 | 134 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | 2460765.67354 | -0.01374 | 133 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.90348 | -0.00448 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.82640 | -0.00428 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.07782 | -0.00350 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458563.02492 | -0.00347 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.46945 | -0.00323 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461046.13281 | -0.00278 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.21871 | -0.00272 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461055.61128 | -0.00267 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461054.83206 | -0.00234 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458544.53212 | -0.00218 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.45898 | -0.00215 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461055.71407 | -0.00212 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461046.28421 | -0.00210 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461046.15920 | -0.00200 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461046.27309 | -0.00197 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.19306 | -0.00543 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.68195 | -0.00476 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.60070 | -0.00454 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.14688 | -0.00411 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.09723 | -0.00410 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.73889 | -0.00404 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.57154 | -0.00402 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.95279 | -0.00401 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.94445 | -0.00397 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.97779 | -0.00397 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.77365 | -0.00383 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.81393 | -0.00378 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.65972 | -0.00375 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.39653 | -0.00372 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.77501 | -0.00366 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.86945 | -0.00359 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.01529 | -0.00346 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.15135 | -0.00345 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.52365 | -0.00345 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.51671 | -0.00342 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.08715 | -0.00341 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460038.99585 | -0.00338 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.73404 | -0.00338 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.97912 | -0.00336 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.03751 | -0.00335 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.70827 | -0.00335 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.59029 | -0.00335 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.28126 | -0.00334 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.07773 | -0.00334 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.20830 | -0.00328 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.62085 | -0.00328 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.11524 | -0.00327 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.39032 | -0.00320 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.48754 | -0.00319 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.86948 | -0.00318 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.46112 | -0.00317 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.51526 | -0.00316 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.85004 | -0.00316 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.17774 | -0.00314 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.79413 | -0.00313 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461092.82186 | -0.00311 | 2 | SAP | 1, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.03190 | -0.00311 | 2 | SAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458544.42517 | -0.00310 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.78754 | -0.00308 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.92640 | -0.00308 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.01106 | -0.00307 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.53476 | -0.00307 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.60837 | -0.00306 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.52990 | -0.00304 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.49862 | -0.00300 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.16385 | -0.00299 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.38268 | -0.00297 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.76254 | -0.00294 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.80559 | -0.00293 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.29997 | -0.00293 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.01532 | -0.00291 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.84855 | -0.00290 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.18368 | -0.00286 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.51254 | -0.00286 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.57917 | -0.00284 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.06390 | -0.00283 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.88744 | -0.00283 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.58578 | -0.00282 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.72355 | -0.00281 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.58543 | -0.00279 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.85663 | -0.00278 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.26671 | -0.00277 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.06801 | -0.00275 | 4 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.93612 | -0.00273 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.22921 | -0.00273 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.15104 | -0.00271 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460038.71808 | -0.00271 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.20274 | -0.00271 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458563.52562 | -0.00270 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.18469 | -0.00268 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.24792 | -0.00268 | 3 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460032.93893 | -0.00267 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.89726 | -0.00267 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.47226 | -0.00265 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.15552 | -0.00264 | 2 | SAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458553.07266 | -0.00263 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.72014 | -0.00262 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.65837 | -0.00260 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.57361 | -0.00259 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.02293 | -0.00259 | 5 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.52884 | -0.00258 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.61671 | -0.00257 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.86254 | -0.00256 | 2 | SAP | 2, 3 | no |
| `tess2025071122000-s0090-0000000151681127-0287-s_lc.fits` | 2460772.86584 | -0.00256 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461052.53467 | -0.00255 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.09865 | -0.00255 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.57076 | -0.00254 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.27258 | -0.00253 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.93606 | -0.00253 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.67815 | -0.00253 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.80140 | -0.00252 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.42776 | -0.00252 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.21809 | -0.00250 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.63754 | -0.00249 | 2 | SAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.18676 | -0.00249 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.81529 | -0.00249 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461092.88020 | -0.00248 | 2 | SAP | 1, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.70410 | -0.00247 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.77921 | -0.00246 | 4 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.10482 | -0.00245 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.93195 | -0.00240 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.67501 | -0.00237 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.48337 | -0.00236 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.40661 | -0.00236 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461093.29688 | -0.00236 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460040.12501 | -0.00235 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458546.72247 | -0.00235 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.30768 | -0.00235 | 3 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461092.97812 | -0.00234 | 3 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458566.63259 | -0.00234 | 2 | SAP | 2 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461081.68659 | -0.00234 | 2 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.21254 | -0.00231 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461055.70434 | -0.00226 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.88820 | -0.00224 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461067.42460 | -0.00223 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461073.23052 | -0.00222 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.44232 | -0.00221 | 2 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458546.73497 | -0.00221 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460039.76182 | -0.00219 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.45004 | -0.00218 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.83684 | -0.00217 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.02226 | -0.00216 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460038.92224 | -0.00215 | 2 | SAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.11315 | -0.00215 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.29865 | -0.00212 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000151681127-0302-s_lc.fits` | 2461099.37628 | -0.00212 | 2 | PDCSAP | 1 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.34024 | -0.00211 | 3 | PDCSAP | 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458545.57938 | -0.00209 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460025.47778 | -0.00208 | 2 | SAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.13815 | -0.00207 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461052.20687 | -0.00205 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460033.80004 | -0.00203 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000151681127-0255-s_lc.fits` | 2460032.02087 | -0.00203 | 2 | SAP | 1 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.26176 | -0.00203 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461072.48811 | -0.00202 | 3 | SAP | 1 | no |
| `tess2019058134432-s0009-0000000151681127-0139-s_lc.fits` | 2458568.46593 | -0.00192 | 2 | PDCSAP | 2 | no |
| `tess2026005125623-s0099-0000000151681127-0300-s_lc.fits` | 2461052.61246 | -0.00182 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-671.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:54:16Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:54:17Z: TOI-671.01 (TIC 151681127, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:54:19Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:54:19Z: TOI-671.01 (err); HD  96645 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460021.2902: gap (catalogue 16111 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 100%, 100%, 90% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-671.01: Gaia DR3 5390443239364017024 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-671.01: Teff 7818 K, R* 1.78 ± 0.14, M* 1.85 ± 0.19, ρ* 0.33 ± 0.09 ρ☉ (dwarf sequence, M_G 2.04, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-671.01: 17 Gaia neighbour(s) within 52.5", contamination 0.86%; depth 16111 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 24 persistent event(s), 6 clean; BJD 2460033.0778 caution: manual exclude (within ±0.25 d); BJD 2460039.8264 suspect: manual exclude (in event), SAP_BKG z=+6.0; BJD 2460039.9035 suspect: manual exclude (in event), SAP_BKG z=+5.5; BJD 2460040.4694 suspect: manual exclude (in event), SAP_BKG z=+7.7 |
| Moving objects at screen-event epochs | inconclusive | 24 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-671.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-671.01: HD  96645 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-671-01.yaml
python -m cygnus.multi report campaigns/toi-671-01.yaml
```
