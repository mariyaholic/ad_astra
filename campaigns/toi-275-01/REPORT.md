<!-- cygnus:generated-draft -->
# Known-object test, TOI-275.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-275-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5086, calibrate_screen #5068, event_census #5074, fetch_independent #5077, fetch_products #5063, known_signal_recovery #5069, moving_objects #5076, period_aliases #5075, prior_art #5089, residual_screen #5072, stellar_context #5071, variability_guard #5087
- Runner finished (UTC): 2026-09-30T22:59:51Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-275.01 (BJD 2460041.9647: recovered, depth 7491 ± 325 ppm (catalogue 9180 ppm); BJD 2460042.8842: recovered, depth 7492 ± 345 ppm (catalogue 9180 ppm); BJD 2460043.8038: recovered, depth 7659 ± 323 ppm (catalogue 9180 ppm); BJD 2460044.7233: recovered, depth 7791 ± 327 ppm (catalogue 9180 ppm); BJD 2460045.6429: recovered, depth 6576 ± 329 ppm (catalogue 9180 ppm); BJD 2460046.5625: recovered, depth 7676 ± 327 ppm (catalogue 9180 ppm); BJD 2460047.4820: recovered, depth 6989 ± 333 ppm (catalogue 9180 ppm); BJD 2460048.4016: recovered, depth 7046 ± 323 ppm (catalogue 9180 ppm); BJD 2460049.3212: recovered, depth 6671 ± 330 ppm (catalogue 9180 ppm); BJD 2460050.2407: recovered, depth 8540 ± 336 ppm (catalogue 9180 ppm); BJD 2460051.1603: recovered, depth 6532 ± 350 ppm (catalogue 9180 ppm); BJD 2460052.0798: recovered, depth 7501 ± 328 ppm (catalogue 9180 ppm); BJD 2460052.9994: recovered, depth 7117 ± 348 ppm (catalogue 9180 ppm); BJD 2460053.9190: recovered, depth 7696 ± 340 ppm (catalogue 9180 ppm); BJD 2460054.8385: recovered, depth 8044 ± 352 ppm (catalogue 9180 ppm); BJD 2460055.7581: recovered, depth 8164 ± 338 ppm (catalogue 9180 ppm); BJD 2460056.6776: recovered, depth 6894 ± 331 ppm (catalogue 9180 ppm); BJD 2460057.5972: recovered, depth 6807 ± 327 ppm (catalogue 9180 ppm); BJD 2460058.5168: recovered, depth 7627 ± 336 ppm (catalogue 9180 ppm); BJD 2460059.4363: recovered, depth 7587 ± 328 ppm (catalogue 9180 ppm); BJD 2460060.3559: recovered, depth 7218 ± 331 ppm (catalogue 9180 ppm); BJD 2460061.2755: recovered, depth 6952 ± 349 ppm (catalogue 9180 ppm); BJD 2460062.1950: recovered, depth 5104 ± 348 ppm (catalogue 9180 ppm); BJD 2460063.1146: recovered, depth 7236 ± 317 ppm (catalogue 9180 ppm); BJD 2460064.0341: recovered, depth 7961 ± 340 ppm (catalogue 9180 ppm); BJD 2460064.9537: recovered, depth 7869 ± 350 ppm (catalogue 9180 ppm); BJD 2460065.8733: recovered, depth 7436 ± 360 ppm (catalogue 9180 ppm); BJD 2460066.7928: recovered, depth 7275 ± 371 ppm (catalogue 9180 ppm); BJD 2460067.7124: recovered, depth 8315 ± 395 ppm (catalogue 9180 ppm); BJD 2458326.0625: recovered, depth 7457 ± 383 ppm (catalogue 9180 ppm); BJD 2458326.9821: recovered, depth 6514 ± 368 ppm (catalogue 9180 ppm); BJD 2458327.9017: recovered, depth 7722 ± 349 ppm (catalogue 9180 ppm); BJD 2458328.8212: partial, depth 6201 ± 369 ppm (catalogue 9180 ppm); BJD 2458329.7408: recovered, depth 8010 ± 378 ppm (catalogue 9180 ppm); BJD 2458330.6603: recovered, depth 6099 ± 381 ppm (catalogue 9180 ppm); BJD 2458331.5799: recovered, depth 7587 ± 378 ppm (catalogue 9180 ppm); BJD 2458332.4995: recovered, depth 6369 ± 389 ppm (catalogue 9180 ppm); BJD 2458333.4190: recovered, depth 8314 ± 388 ppm (catalogue 9180 ppm); BJD 2458334.3386: recovered, depth 6518 ± 394 ppm (catalogue 9180 ppm); BJD 2458335.2581: recovered, depth 7911 ± 401 ppm (catalogue 9180 ppm); BJD 2458336.1777: partial, depth 6396 ± 377 ppm (catalogue 9180 ppm); BJD 2458337.0973: recovered, depth 7223 ± 371 ppm (catalogue 9180 ppm); BJD 2458338.0168: recovered, depth 6120 ± 351 ppm (catalogue 9180 ppm); BJD 2458338.9364: gap (catalogue 9180 ppm); BJD 2458339.8560: recovered, depth 6347 ± 329 ppm (catalogue 9180 ppm); BJD 2458340.7755: recovered, depth 7714 ± 332 ppm (catalogue 9180 ppm); BJD 2458341.6951: recovered, depth 6788 ± 390 ppm (catalogue 9180 ppm); BJD 2458342.6146: recovered, depth 7887 ± 390 ppm (catalogue 9180 ppm); BJD 2458343.5342: recovered, depth 7180 ± 423 ppm (catalogue 9180 ppm); BJD 2458344.4538: recovered, depth 7067 ± 377 ppm (catalogue 9180 ppm); BJD 2458345.3733: recovered, depth 6227 ± 358 ppm (catalogue 9180 ppm); BJD 2458346.2929: recovered, depth 7762 ± 343 ppm (catalogue 9180 ppm); BJD 2458347.2124: recovered, depth 5954 ± 387 ppm (catalogue 9180 ppm); BJD 2458348.1320: recovered, depth 7636 ± 447 ppm (catalogue 9180 ppm); BJD 2458349.0516: partial, depth 5897 ± 604 ppm (catalogue 9180 ppm); BJD 2458349.9711: recovered, depth 8107 ± 373 ppm (catalogue 9180 ppm); BJD 2458350.8907: partial, depth 5269 ± 372 ppm (catalogue 9180 ppm); BJD 2458351.8103: recovered, depth 8221 ± 375 ppm (catalogue 9180 ppm); BJD 2458352.7298: recovered, depth 6220 ± 370 ppm (catalogue 9180 ppm); BJD 2458382.1558: gap (catalogue 9180 ppm); BJD 2458383.0754: gap (catalogue 9180 ppm); BJD 2458383.9949: gap (catalogue 9180 ppm); BJD 2458384.9145: gap (catalogue 9180 ppm); BJD 2458385.8340: gap (catalogue 9180 ppm); BJD 2458386.7536: not recovered, depth 8021 ± 408 ppm (catalogue 9180 ppm); BJD 2458387.6732: not recovered, depth 6920 ± 362 ppm (catalogue 9180 ppm); BJD 2458388.5927: recovered, depth 7761 ± 356 ppm (catalogue 9180 ppm); BJD 2458389.5123: not recovered, depth 5812 ± 377 ppm (catalogue 9180 ppm); BJD 2458390.4318: not recovered, depth 7687 ± 336 ppm (catalogue 9180 ppm); BJD 2458391.3514: recovered, depth 5827 ± 331 ppm (catalogue 9180 ppm); BJD 2458392.2710: not recovered, depth 6498 ± 434 ppm (catalogue 9180 ppm); BJD 2458393.1905: not recovered, depth 5181 ± 397 ppm (catalogue 9180 ppm); BJD 2458394.1101: recovered, depth 2599 ± 384 ppm (catalogue 9180 ppm); BJD 2458395.0297: gap (catalogue 9180 ppm); BJD 2458395.9492: gap (catalogue 9180 ppm); BJD 2458396.8688: recovered, depth 5404 ± 374 ppm (catalogue 9180 ppm); BJD 2458397.7883: recovered, depth 7425 ± 373 ppm (catalogue 9180 ppm); BJD 2458398.7079: not recovered, depth 4360 ± 434 ppm (catalogue 9180 ppm); BJD 2458399.6275: recovered, depth 7864 ± 356 ppm (catalogue 9180 ppm); BJD 2458400.5470: not recovered, depth 5425 ± 359 ppm (catalogue 9180 ppm); BJD 2458401.4666: recovered, depth 7462 ± 353 ppm (catalogue 9180 ppm); BJD 2458402.3861: recovered, depth 5382 ± 362 ppm (catalogue 9180 ppm); BJD 2458403.3057: recovered, depth 8203 ± 369 ppm (catalogue 9180 ppm); BJD 2458404.2253: recovered, depth 5531 ± 382 ppm (catalogue 9180 ppm); BJD 2458405.1448: recovered, depth 7249 ± 372 ppm (catalogue 9180 ppm); BJD 2458406.0644: not recovered, depth 5418 ± 376 ppm (catalogue 9180 ppm); BJD 2458406.9840: gap (catalogue 9180 ppm); BJD 2458407.9035: gap (catalogue 9180 ppm); BJD 2458408.8231: gap (catalogue 9180 ppm); BJD 2458411.5818: recovered, depth 6133 ± 362 ppm (catalogue 9180 ppm); BJD 2458412.5013: recovered, depth 8376 ± 366 ppm (catalogue 9180 ppm); BJD 2458413.4209: recovered, depth 6709 ± 348 ppm (catalogue 9180 ppm); BJD 2458414.3405: recovered, depth 7287 ± 336 ppm (catalogue 9180 ppm); BJD 2458415.2600: recovered, depth 4520 ± 367 ppm (catalogue 9180 ppm); BJD 2458416.1796: recovered, depth 8135 ± 354 ppm (catalogue 9180 ppm); BJD 2458417.0991: recovered, depth 5307 ± 504 ppm (catalogue 9180 ppm); BJD 2458418.0187: recovered, depth 6647 ± 337 ppm (catalogue 9180 ppm); BJD 2458418.9383: gap (catalogue 9180 ppm); BJD 2458419.8578: gap (catalogue 9180 ppm); BJD 2458420.7774: gap (catalogue 9180 ppm); BJD 2458421.6969: recovered, depth 8705 ± 320 ppm (catalogue 9180 ppm); BJD 2458422.6165: gap (catalogue 9180 ppm); BJD 2458423.5361: gap (catalogue 9180 ppm); BJD 2458424.4556: gap (catalogue 9180 ppm); BJD 2458425.3752: recovered, depth 7870 ± 358 ppm (catalogue 9180 ppm); BJD 2458426.2948: recovered, depth 4863 ± 369 ppm (catalogue 9180 ppm); BJD 2458427.2143: recovered, depth 7186 ± 367 ppm (catalogue 9180 ppm); BJD 2458428.1339: recovered, depth 6412 ± 373 ppm (catalogue 9180 ppm); BJD 2458429.0534: recovered, depth 7770 ± 358 ppm (catalogue 9180 ppm); BJD 2458429.9730: recovered, depth 7107 ± 353 ppm (catalogue 9180 ppm); BJD 2458430.8926: recovered, depth 8306 ± 334 ppm (catalogue 9180 ppm); BJD 2458431.8121: recovered, depth 6724 ± 332 ppm (catalogue 9180 ppm); BJD 2458432.7317: recovered, depth 7390 ± 344 ppm (catalogue 9180 ppm); BJD 2458433.6512: recovered, depth 4969 ± 376 ppm (catalogue 9180 ppm); BJD 2458434.5708: recovered, depth 7603 ± 348 ppm (catalogue 9180 ppm); BJD 2458435.4904: recovered, depth 5781 ± 447 ppm (catalogue 9180 ppm); BJD 2458436.4099: recovered, depth 9677 ± 474 ppm (catalogue 9180 ppm); BJD 2458438.2491: not recovered, depth -4520 ± 489 ppm (catalogue 9180 ppm); BJD 2458439.1686: recovered, depth 6544 ± 394 ppm (catalogue 9180 ppm); BJD 2458440.0882: recovered, depth 6651 ± 367 ppm (catalogue 9180 ppm); BJD 2458441.0077: recovered, depth 6955 ± 390 ppm (catalogue 9180 ppm); BJD 2458441.9273: recovered, depth 6936 ± 355 ppm (catalogue 9180 ppm); BJD 2458442.8469: recovered, depth 6108 ± 348 ppm (catalogue 9180 ppm); BJD 2458443.7664: recovered, depth 7358 ± 359 ppm (catalogue 9180 ppm); BJD 2458444.6860: recovered, depth 5321 ± 371 ppm (catalogue 9180 ppm); BJD 2458445.6055: recovered, depth 8469 ± 369 ppm (catalogue 9180 ppm); BJD 2458446.5251: recovered, depth 5284 ± 376 ppm (catalogue 9180 ppm); BJD 2458447.4447: recovered, depth 7831 ± 357 ppm (catalogue 9180 ppm); BJD 2458448.3642: recovered, depth 6524 ± 378 ppm (catalogue 9180 ppm); BJD 2458449.2838: recovered, depth 8176 ± 378 ppm (catalogue 9180 ppm); BJD 2458450.2034: gap (catalogue 9180 ppm); BJD 2458451.1229: gap (catalogue 9180 ppm); BJD 2458452.0425: recovered, depth 6231 ± 380 ppm (catalogue 9180 ppm); BJD 2458452.9620: recovered, depth 7200 ± 359 ppm (catalogue 9180 ppm); BJD 2458453.8816: recovered, depth 5794 ± 366 ppm (catalogue 9180 ppm); BJD 2458454.8012: recovered, depth 7578 ± 353 ppm (catalogue 9180 ppm); BJD 2458455.7207: recovered, depth 6338 ± 366 ppm (catalogue 9180 ppm); BJD 2458456.6403: recovered, depth 6741 ± 358 ppm (catalogue 9180 ppm); BJD 2458457.5599: recovered, depth 5657 ± 362 ppm (catalogue 9180 ppm); BJD 2458458.4794: recovered, depth 7577 ± 352 ppm (catalogue 9180 ppm); BJD 2458459.3990: recovered, depth 6661 ± 378 ppm (catalogue 9180 ppm); BJD 2458460.3185: recovered, depth 7734 ± 372 ppm (catalogue 9180 ppm); BJD 2458461.2381: recovered, depth 6550 ± 370 ppm (catalogue 9180 ppm); BJD 2458462.1577: recovered, depth 8571 ± 362 ppm (catalogue 9180 ppm); BJD 2458463.0772: recovered, depth 5299 ± 414 ppm (catalogue 9180 ppm); BJD 2458463.9968: gap (catalogue 9180 ppm); BJD 2458468.5946: not recovered, depth 5362 ± 395 ppm (catalogue 9180 ppm); BJD 2458469.5142: not recovered, depth 6762 ± 383 ppm (catalogue 9180 ppm); BJD 2458470.4337: not recovered, depth 5640 ± 359 ppm (catalogue 9180 ppm); BJD 2458471.3533: not recovered, depth 8239 ± 340 ppm (catalogue 9180 ppm); BJD 2458472.2728: not recovered, depth 5764 ± 353 ppm (catalogue 9180 ppm); BJD 2458473.1924: not recovered, depth 8159 ± 342 ppm (catalogue 9180 ppm); BJD 2458474.1120: not recovered, depth 6175 ± 359 ppm (catalogue 9180 ppm); BJD 2458475.0315: not recovered, depth 8489 ± 356 ppm (catalogue 9180 ppm); BJD 2458475.9511: not recovered, depth 5960 ± 378 ppm (catalogue 9180 ppm); BJD 2458476.8706: not recovered, depth 5973 ± 339 ppm (catalogue 9180 ppm); BJD 2458477.7902: gap (catalogue 9180 ppm); BJD 2458478.7098: not recovered, depth 6124 ± 352 ppm (catalogue 9180 ppm); BJD 2458479.6293: not recovered, depth 6120 ± 349 ppm (catalogue 9180 ppm); BJD 2458480.5489: not recovered, depth 7810 ± 347 ppm (catalogue 9180 ppm); BJD 2458481.4685: not recovered, depth 6655 ± 344 ppm (catalogue 9180 ppm); BJD 2458482.3880: not recovered, depth 6902 ± 343 ppm (catalogue 9180 ppm); BJD 2458483.3076: not recovered, depth 6524 ± 350 ppm (catalogue 9180 ppm); BJD 2458484.2271: not recovered, depth 8406 ± 349 ppm (catalogue 9180 ppm); BJD 2458485.1467: not recovered, depth 5538 ± 356 ppm (catalogue 9180 ppm); BJD 2458486.0663: not recovered, depth 7284 ± 367 ppm (catalogue 9180 ppm); BJD 2458486.9858: not recovered, depth 6597 ± 393 ppm (catalogue 9180 ppm); BJD 2458487.9054: not recovered, depth 9487 ± 372 ppm (catalogue 9180 ppm); BJD 2458488.8249: not recovered, depth 6759 ± 361 ppm (catalogue 9180 ppm); BJD 2458489.7445: not recovered, depth 8619 ± 341 ppm (catalogue 9180 ppm)).
Outside the catalogued epoch the screen left 8 threshold entries forming **4 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-275.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 373844472 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 81.516646 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -67.232772 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460041.96466 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 0.9195617 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 9180.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.153 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.0611 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-08-10 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | lightcurve | 64 | True | `f2ede16be459818e` | True |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | lightcurve | 1 | False | `ec9574c7d72304a2` | True |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | lightcurve | 3 | False | `d010686c2c413b49` | True |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | lightcurve | 4 | False | `0b410d2e9317a08f` | True |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | lightcurve | 5 | False | `823f27ff009a35a7` | True |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | lightcurve | 6 | False | `e23321ccf1c590a9` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460041.96466 | recovered | 34 | 7491 ± 325 | 9180 | -0.03 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460042.88422 | recovered | 34 | 7492 ± 345 | 9180 | -0.19 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460043.80378 | recovered | 34 | 7659 ± 323 | 9180 | 0.02 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460044.72335 | recovered | 34 | 7791 ± 327 | 9180 | -0.02 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460045.64291 | recovered | 35 | 6576 ± 329 | 9180 | -0.01 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460046.56247 | recovered | 35 | 7676 ± 327 | 9180 | 0.02 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460047.48203 | recovered | 35 | 6989 ± 333 | 9180 | 0.00 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460048.40159 | recovered | 35 | 7046 ± 323 | 9180 | 0.00 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460049.32115 | recovered | 35 | 6671 ± 330 | 9180 | -0.03 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460050.24072 | recovered | 35 | 8540 ± 336 | 9180 | 0.03 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460051.16028 | recovered | 35 | 6532 ± 350 | 9180 | 0.08 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460052.07984 | recovered | 35 | 7501 ± 328 | 9180 | -0.01 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460052.99940 | recovered | 34 | 7117 ± 348 | 9180 | 0.02 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460053.91896 | recovered | 34 | 7696 ± 340 | 9180 | -0.02 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460054.83852 | recovered | 34 | 8044 ± 352 | 9180 | 0.03 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460055.75809 | recovered | 34 | 8164 ± 338 | 9180 | 0.04 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460056.67765 | recovered | 34 | 6894 ± 331 | 9180 | -0.01 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460057.59721 | recovered | 35 | 6807 ± 327 | 9180 | 0.01 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460058.51677 | recovered | 35 | 7627 ± 336 | 9180 | -0.01 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460059.43633 | recovered | 35 | 7587 ± 328 | 9180 | 0.00 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460060.35589 | recovered | 35 | 7218 ± 331 | 9180 | 0.07 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460061.27546 | recovered | 35 | 6952 ± 349 | 9180 | 0.23 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460062.19502 | recovered | 35 | 5104 ± 348 | 9180 | 0.14 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460063.11458 | recovered | 35 | 7236 ± 317 | 9180 | -0.13 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460064.03414 | recovered | 34 | 7961 ± 340 | 9180 | 0.05 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460064.95370 | recovered | 34 | 7869 ± 350 | 9180 | -0.23 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460065.87326 | recovered | 34 | 7436 ± 360 | 9180 | 0.03 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460066.79283 | recovered | 34 | 7275 ± 371 | 9180 | 0.03 |
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2460067.71239 | recovered | 32 | 8315 ± 395 | 9180 | 0.21 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458326.06253 | recovered | 35 | 7457 ± 383 | 9180 | -0.13 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458326.98209 | recovered | 35 | 6514 ± 368 | 9180 | -0.02 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458327.90165 | recovered | 35 | 7722 ± 349 | 9180 | 0.01 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458328.82121 | partial | 35 | 6201 ± 369 | 9180 | 0.11 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458329.74077 | recovered | 34 | 8010 ± 378 | 9180 | -0.02 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458330.66034 | recovered | 34 | 6099 ± 381 | 9180 | -0.01 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458331.57990 | recovered | 33 | 7587 ± 378 | 9180 | -0.08 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458332.49946 | recovered | 33 | 6369 ± 389 | 9180 | 0.17 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458333.41902 | recovered | 33 | 8314 ± 388 | 9180 | -0.12 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458334.33858 | recovered | 34 | 6518 ± 394 | 9180 | -0.07 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458335.25814 | recovered | 35 | 7911 ± 401 | 9180 | 0.03 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458336.17771 | partial | 35 | 6396 ± 377 | 9180 | -0.28 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458337.09727 | recovered | 35 | 7223 ± 371 | 9180 | 0.00 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458338.01683 | recovered | 35 | 6120 ± 351 | 9180 | -0.02 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458338.93639 | gap | 0 | — | 9180 | — |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458339.85595 | recovered | 35 | 6347 ± 329 | 9180 | -0.12 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458340.77551 | recovered | 35 | 7714 ± 332 | 9180 | 0.08 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458341.69508 | recovered | 27 | 6788 ± 390 | 9180 | -0.13 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458342.61464 | recovered | 34 | 7887 ± 390 | 9180 | 0.04 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458343.53420 | recovered | 31 | 7180 ± 423 | 9180 | -0.18 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458344.45376 | recovered | 33 | 7067 ± 377 | 9180 | -0.01 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458345.37332 | recovered | 34 | 6227 ± 358 | 9180 | -0.17 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458346.29289 | recovered | 35 | 7762 ± 343 | 9180 | -0.14 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458347.21245 | recovered | 34 | 5954 ± 387 | 9180 | -0.11 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458348.13201 | recovered | 24 | 7636 ± 447 | 9180 | -0.03 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458349.05157 | partial | 13 | 5897 ± 604 | 9180 | -0.05 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458349.97113 | recovered | 35 | 8107 ± 373 | 9180 | -0.05 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458350.89069 | partial | 35 | 5269 ± 372 | 9180 | -0.15 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458351.81026 | recovered | 33 | 8221 ± 375 | 9180 | -0.10 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 2458352.72982 | recovered | 34 | 6220 ± 370 | 9180 | 0.01 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458382.15579 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458383.07535 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458383.99491 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458384.91448 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458385.83404 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458386.75360 | not_recovered | 33 | 8021 ± 408 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458387.67316 | not_recovered | 34 | 6920 ± 362 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458388.59272 | recovered | 34 | 7761 ± 356 | 9180 | -0.24 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458389.51229 | not_recovered | 33 | 5812 ± 377 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458390.43185 | not_recovered | 35 | 7687 ± 336 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458391.35141 | recovered | 35 | 5827 ± 331 | 9180 | -0.21 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458392.27097 | not_recovered | 24 | 6498 ± 434 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458393.19053 | not_recovered | 35 | 5181 ± 397 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458394.11009 | recovered | 35 | 2599 ± 384 | 9180 | -0.25 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458395.02966 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458395.94922 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458396.86878 | recovered | 34 | 5404 ± 374 | 9180 | -0.30 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458397.78834 | recovered | 34 | 7425 ± 373 | 9180 | -0.22 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458398.70790 | not_recovered | 27 | 4360 ± 434 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458399.62746 | recovered | 34 | 7864 ± 356 | 9180 | -0.31 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458400.54703 | not_recovered | 35 | 5425 ± 359 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458401.46659 | recovered | 35 | 7462 ± 353 | 9180 | -0.23 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458402.38615 | recovered | 34 | 5382 ± 362 | 9180 | -0.21 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458403.30571 | recovered | 35 | 8203 ± 369 | 9180 | -0.18 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458404.22527 | recovered | 34 | 5531 ± 382 | 9180 | -0.16 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458405.14483 | recovered | 34 | 7249 ± 372 | 9180 | -0.24 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458406.06440 | not_recovered | 34 | 5418 ± 376 | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458406.98396 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458407.90352 | gap | 0 | — | 9180 | — |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 2458408.82308 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458411.58177 | recovered | 35 | 6133 ± 362 | 9180 | -0.01 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458412.50133 | recovered | 35 | 8376 ± 366 | 9180 | -0.25 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458413.42089 | recovered | 35 | 6709 ± 348 | 9180 | -0.42 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458414.34045 | recovered | 35 | 7287 ± 336 | 9180 | -0.23 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458415.26001 | recovered | 35 | 4520 ± 367 | 9180 | -0.14 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458416.17957 | recovered | 35 | 8135 ± 354 | 9180 | -0.29 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458417.09914 | recovered | 18 | 5307 ± 504 | 9180 | 0.01 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458418.01870 | recovered | 34 | 6647 ± 337 | 9180 | -0.23 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458418.93826 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458419.85782 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458420.77738 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458421.69694 | recovered | 35 | 8705 ± 320 | 9180 | -0.20 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458422.61651 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458423.53607 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458424.45563 | gap | 0 | — | 9180 | — |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458425.37519 | recovered | 35 | 7870 ± 358 | 9180 | -0.27 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458426.29475 | recovered | 35 | 4863 ± 369 | 9180 | -0.11 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458427.21431 | recovered | 35 | 7186 ± 367 | 9180 | -0.18 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458428.13388 | recovered | 33 | 6412 ± 373 | 9180 | -0.24 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458429.05344 | recovered | 34 | 7770 ± 358 | 9180 | -0.29 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458429.97300 | recovered | 34 | 7107 ± 353 | 9180 | -0.18 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458430.89256 | recovered | 34 | 8306 ± 334 | 9180 | -0.22 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458431.81212 | recovered | 35 | 6724 ± 332 | 9180 | -0.11 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458432.73169 | recovered | 35 | 7390 ± 344 | 9180 | -0.21 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458433.65125 | recovered | 35 | 4969 ± 376 | 9180 | -0.13 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458434.57081 | recovered | 35 | 7603 ± 348 | 9180 | -0.20 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458435.49037 | recovered | 34 | 5781 ± 447 | 9180 | -0.32 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458436.40993 | recovered | 35 | 9677 ± 474 | 9180 | -0.24 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458438.24906 | not_recovered | 18 | -4520 ± 489 | 9180 | — |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458439.16862 | recovered | 33 | 6544 ± 394 | 9180 | -0.22 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458440.08818 | recovered | 34 | 6651 ± 367 | 9180 | -0.38 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458441.00774 | recovered | 28 | 6955 ± 390 | 9180 | -0.20 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458441.92730 | recovered | 32 | 6936 ± 355 | 9180 | -0.32 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458442.84686 | recovered | 35 | 6108 ± 348 | 9180 | -0.03 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458443.76643 | recovered | 35 | 7358 ± 359 | 9180 | -0.21 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458444.68599 | recovered | 35 | 5321 ± 371 | 9180 | -0.14 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458445.60555 | recovered | 35 | 8469 ± 369 | 9180 | -0.14 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458446.52511 | recovered | 35 | 5284 ± 376 | 9180 | -0.14 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458447.44467 | recovered | 35 | 7831 ± 357 | 9180 | -0.23 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458448.36423 | recovered | 34 | 6524 ± 378 | 9180 | -0.17 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458449.28380 | recovered | 34 | 8176 ± 378 | 9180 | -0.23 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458450.20336 | gap | 0 | — | 9180 | — |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458451.12292 | gap | 0 | — | 9180 | — |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458452.04248 | recovered | 31 | 6231 ± 380 | 9180 | -0.16 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458452.96204 | recovered | 35 | 7200 ± 359 | 9180 | -0.14 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458453.88160 | recovered | 35 | 5794 ± 366 | 9180 | -0.09 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458454.80117 | recovered | 35 | 7578 ± 353 | 9180 | 0.02 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458455.72073 | recovered | 35 | 6338 ± 366 | 9180 | -0.16 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458456.64029 | recovered | 35 | 6741 ± 358 | 9180 | 0.06 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458457.55985 | recovered | 35 | 5657 ± 362 | 9180 | -0.05 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458458.47941 | recovered | 35 | 7577 ± 352 | 9180 | -0.13 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458459.39897 | recovered | 34 | 6661 ± 378 | 9180 | 0.07 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458460.31854 | recovered | 34 | 7734 ± 372 | 9180 | -0.05 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458461.23810 | recovered | 34 | 6550 ± 370 | 9180 | -0.07 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458462.15766 | recovered | 34 | 8571 ± 362 | 9180 | -0.02 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458463.07722 | recovered | 35 | 5299 ± 414 | 9180 | -0.07 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 2458463.99678 | gap | 0 | — | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458468.59459 | not_recovered | 35 | 5362 ± 395 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458469.51415 | not_recovered | 34 | 6762 ± 383 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458470.43371 | not_recovered | 34 | 5640 ± 359 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458471.35328 | not_recovered | 34 | 8239 ± 340 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458472.27284 | not_recovered | 34 | 5764 ± 353 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458473.19240 | not_recovered | 34 | 8159 ± 342 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458474.11196 | not_recovered | 35 | 6175 ± 359 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458475.03152 | not_recovered | 35 | 8489 ± 356 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458475.95108 | not_recovered | 35 | 5960 ± 378 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458476.87065 | not_recovered | 35 | 5973 ± 339 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458477.79021 | gap | 0 | — | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458478.70977 | not_recovered | 33 | 6124 ± 352 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458479.62933 | not_recovered | 34 | 6120 ± 349 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458480.54889 | not_recovered | 34 | 7810 ± 347 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458481.46846 | not_recovered | 34 | 6655 ± 344 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458482.38802 | not_recovered | 34 | 6902 ± 343 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458483.30758 | not_recovered | 34 | 6524 ± 350 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458484.22714 | not_recovered | 35 | 8406 ± 349 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458485.14670 | not_recovered | 35 | 5538 ± 356 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458486.06626 | not_recovered | 35 | 7284 ± 367 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458486.98583 | not_recovered | 35 | 6597 ± 393 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458487.90539 | not_recovered | 35 | 9487 ± 372 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458488.82495 | not_recovered | 35 | 6759 ± 361 | 9180 | — |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 2458489.74451 | not_recovered | 35 | 8619 ± 341 | 9180 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000373844472-0257-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2018206045859-s0001-0000000373844472-0120-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2018263035959-s0003-0000000373844472-0123-s_lc.fits` | 5 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018319095959-s0005-0000000373844472-0125-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018349182500-s0006-0000000373844472-0126-s_lc.fits` | 12 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458425.12019 | -0.00975 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458417.80912 | -0.00936 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458414.49108 | -0.00851 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000373844472-0124-s_lc.fits` | 2458425.49518 | -0.00732 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-275.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:59:39Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:59:43Z: TOI-275.01 (TIC 373844472, disposition APC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:59:46Z: Gaia DR3 4660192490061661056 (type SR|M, P 501.2 d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T22:59:48Z: TOI-275.01 (err); 2MASS J05260296-6713289 (LP*); 1RXS J052605.5-671404 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460041.9647: recovered, depth 7491 ± 325 ppm (catalogue 9180 ppm); BJD 2460042.8842: recovered, depth 7492 ± 345 ppm (catalogue 9180 ppm); BJD 2460043.8038: recovered, depth 7659 ± 323 ppm (catalogue 9180 ppm); BJD 2460044.7233: recovered, depth 7791 ± 327 ppm (catalogue 9180 ppm); BJD 2460045.6429: recovered, depth 6576 ± 329 ppm (catalogue 9180 ppm); BJD 2460046.5625: recovered, depth 7676 ± 327 ppm (catalogue 9180 ppm); BJD 2460047.4820: recovered, depth 6989 ± 333 ppm (catalogue 9180 ppm); BJD 2460048.4016: recovered, depth 7046 ± 323 ppm (catalogue 9180 ppm); BJD 2460049.3212: recovered, depth 6671 ± 330 ppm (catalogue 9180 ppm); BJD 2460050.2407: recovered, depth 8540 ± 336 ppm (catalogue 9180 ppm); BJD 2460051.1603: recovered, depth 6532 ± 350 ppm (catalogue 9180 ppm); BJD 2460052.0798: recovered, depth 7501 ± 328 ppm (catalogue 9180 ppm); BJD 2460052.9994: recovered, depth 7117 ± 348 ppm (catalogue 9180 ppm); BJD 2460053.9190: recovered, depth 7696 ± 340 ppm (catalogue 9180 ppm); BJD 2460054.8385: recovered, depth 8044 ± 352 ppm (catalogue 9180 ppm); BJD 2460055.7581: recovered, depth 8164 ± 338 ppm (catalogue 9180 ppm); BJD 2460056.6776: recovered, depth 6894 ± 331 ppm (catalogue 9180 ppm); BJD 2460057.5972: recovered, depth 6807 ± 327 ppm (catalogue 9180 ppm); BJD 2460058.5168: recovered, depth 7627 ± 336 ppm (catalogue 9180 ppm); BJD 2460059.4363: recovered, depth 7587 ± 328 ppm (catalogue 9180 ppm); BJD 2460060.3559: recovered, depth 7218 ± 331 ppm (catalogue 9180 ppm); BJD 2460061.2755: recovered, depth 6952 ± 349 ppm (catalogue 9180 ppm); BJD 2460062.1950: recovered, depth 5104 ± 348 ppm (catalogue 9180 ppm); BJD 2460063.1146: recovered, depth 7236 ± 317 ppm (catalogue 9180 ppm); BJD 2460064.0341: recovered, depth 7961 ± 340 ppm (catalogue 9180 ppm); BJD 2460064.9537: recovered, depth 7869 ± 350 ppm (catalogue 9180 ppm); BJD 2460065.8733: recovered, depth 7436 ± 360 ppm (catalogue 9180 ppm); BJD 2460066.7928: recovered, depth 7275 ± 371 ppm (catalogue 9180 ppm); BJD 2460067.7124: recovered, depth 8315 ± 395 ppm (catalogue 9180 ppm); BJD 2458326.0625: recovered, depth 7457 ± 383 ppm (catalogue 9180 ppm); BJD 2458326.9821: recovered, depth 6514 ± 368 ppm (catalogue 9180 ppm); BJD 2458327.9017: recovered, depth 7722 ± 349 ppm (catalogue 9180 ppm); BJD 2458328.8212: partial, depth 6201 ± 369 ppm (catalogue 9180 ppm); BJD 2458329.7408: recovered, depth 8010 ± 378 ppm (catalogue 9180 ppm); BJD 2458330.6603: recovered, depth 6099 ± 381 ppm (catalogue 9180 ppm); BJD 2458331.5799: recovered, depth 7587 ± 378 ppm (catalogue 9180 ppm); BJD 2458332.4995: recovered, depth 6369 ± 389 ppm (catalogue 9180 ppm); BJD 2458333.4190: recovered, depth 8314 ± 388 ppm (catalogue 9180 ppm); BJD 2458334.3386: recovered, depth 6518 ± 394 ppm (catalogue 9180 ppm); BJD 2458335.2581: recovered, depth 7911 ± 401 ppm (catalogue 9180 ppm); BJD 2458336.1777: partial, depth 6396 ± 377 ppm (catalogue 9180 ppm); BJD 2458337.0973: recovered, depth 7223 ± 371 ppm (catalogue 9180 ppm); BJD 2458338.0168: recovered, depth 6120 ± 351 ppm (catalogue 9180 ppm); BJD 2458338.9364: gap (catalogue 9180 ppm); BJD 2458339.8560: recovered, depth 6347 ± 329 ppm (catalogue 9180 ppm); BJD 2458340.7755: recovered, depth 7714 ± 332 ppm (catalogue 9180 ppm); BJD 2458341.6951: recovered, depth 6788 ± 390 ppm (catalogue 9180 ppm); BJD 2458342.6146: recovered, depth 7887 ± 390 ppm (catalogue 9180 ppm); BJD 2458343.5342: recovered, depth 7180 ± 423 ppm (catalogue 9180 ppm); BJD 2458344.4538: recovered, depth 7067 ± 377 ppm (catalogue 9180 ppm); BJD 2458345.3733: recovered, depth 6227 ± 358 ppm (catalogue 9180 ppm); BJD 2458346.2929: recovered, depth 7762 ± 343 ppm (catalogue 9180 ppm); BJD 2458347.2124: recovered, depth 5954 ± 387 ppm (catalogue 9180 ppm); BJD 2458348.1320: recovered, depth 7636 ± 447 ppm (catalogue 9180 ppm); BJD 2458349.0516: partial, depth 5897 ± 604 ppm (catalogue 9180 ppm); BJD 2458349.9711: recovered, depth 8107 ± 373 ppm (catalogue 9180 ppm); BJD 2458350.8907: partial, depth 5269 ± 372 ppm (catalogue 9180 ppm); BJD 2458351.8103: recovered, depth 8221 ± 375 ppm (catalogue 9180 ppm); BJD 2458352.7298: recovered, depth 6220 ± 370 ppm (catalogue 9180 ppm); BJD 2458382.1558: gap (catalogue 9180 ppm); BJD 2458383.0754: gap (catalogue 9180 ppm); BJD 2458383.9949: gap (catalogue 9180 ppm); BJD 2458384.9145: gap (catalogue 9180 ppm); BJD 2458385.8340: gap (catalogue 9180 ppm); BJD 2458386.7536: not recovered, depth 8021 ± 408 ppm (catalogue 9180 ppm); BJD 2458387.6732: not recovered, depth 6920 ± 362 ppm (catalogue 9180 ppm); BJD 2458388.5927: recovered, depth 7761 ± 356 ppm (catalogue 9180 ppm); BJD 2458389.5123: not recovered, depth 5812 ± 377 ppm (catalogue 9180 ppm); BJD 2458390.4318: not recovered, depth 7687 ± 336 ppm (catalogue 9180 ppm); BJD 2458391.3514: recovered, depth 5827 ± 331 ppm (catalogue 9180 ppm); BJD 2458392.2710: not recovered, depth 6498 ± 434 ppm (catalogue 9180 ppm); BJD 2458393.1905: not recovered, depth 5181 ± 397 ppm (catalogue 9180 ppm); BJD 2458394.1101: recovered, depth 2599 ± 384 ppm (catalogue 9180 ppm); BJD 2458395.0297: gap (catalogue 9180 ppm); BJD 2458395.9492: gap (catalogue 9180 ppm); BJD 2458396.8688: recovered, depth 5404 ± 374 ppm (catalogue 9180 ppm); BJD 2458397.7883: recovered, depth 7425 ± 373 ppm (catalogue 9180 ppm); BJD 2458398.7079: not recovered, depth 4360 ± 434 ppm (catalogue 9180 ppm); BJD 2458399.6275: recovered, depth 7864 ± 356 ppm (catalogue 9180 ppm); BJD 2458400.5470: not recovered, depth 5425 ± 359 ppm (catalogue 9180 ppm); BJD 2458401.4666: recovered, depth 7462 ± 353 ppm (catalogue 9180 ppm); BJD 2458402.3861: recovered, depth 5382 ± 362 ppm (catalogue 9180 ppm); BJD 2458403.3057: recovered, depth 8203 ± 369 ppm (catalogue 9180 ppm); BJD 2458404.2253: recovered, depth 5531 ± 382 ppm (catalogue 9180 ppm); BJD 2458405.1448: recovered, depth 7249 ± 372 ppm (catalogue 9180 ppm); BJD 2458406.0644: not recovered, depth 5418 ± 376 ppm (catalogue 9180 ppm); BJD 2458406.9840: gap (catalogue 9180 ppm); BJD 2458407.9035: gap (catalogue 9180 ppm); BJD 2458408.8231: gap (catalogue 9180 ppm); BJD 2458411.5818: recovered, depth 6133 ± 362 ppm (catalogue 9180 ppm); BJD 2458412.5013: recovered, depth 8376 ± 366 ppm (catalogue 9180 ppm); BJD 2458413.4209: recovered, depth 6709 ± 348 ppm (catalogue 9180 ppm); BJD 2458414.3405: recovered, depth 7287 ± 336 ppm (catalogue 9180 ppm); BJD 2458415.2600: recovered, depth 4520 ± 367 ppm (catalogue 9180 ppm); BJD 2458416.1796: recovered, depth 8135 ± 354 ppm (catalogue 9180 ppm); BJD 2458417.0991: recovered, depth 5307 ± 504 ppm (catalogue 9180 ppm); BJD 2458418.0187: recovered, depth 6647 ± 337 ppm (catalogue 9180 ppm); BJD 2458418.9383: gap (catalogue 9180 ppm); BJD 2458419.8578: gap (catalogue 9180 ppm); BJD 2458420.7774: gap (catalogue 9180 ppm); BJD 2458421.6969: recovered, depth 8705 ± 320 ppm (catalogue 9180 ppm); BJD 2458422.6165: gap (catalogue 9180 ppm); BJD 2458423.5361: gap (catalogue 9180 ppm); BJD 2458424.4556: gap (catalogue 9180 ppm); BJD 2458425.3752: recovered, depth 7870 ± 358 ppm (catalogue 9180 ppm); BJD 2458426.2948: recovered, depth 4863 ± 369 ppm (catalogue 9180 ppm); BJD 2458427.2143: recovered, depth 7186 ± 367 ppm (catalogue 9180 ppm); BJD 2458428.1339: recovered, depth 6412 ± 373 ppm (catalogue 9180 ppm); BJD 2458429.0534: recovered, depth 7770 ± 358 ppm (catalogue 9180 ppm); BJD 2458429.9730: recovered, depth 7107 ± 353 ppm (catalogue 9180 ppm); BJD 2458430.8926: recovered, depth 8306 ± 334 ppm (catalogue 9180 ppm); BJD 2458431.8121: recovered, depth 6724 ± 332 ppm (catalogue 9180 ppm); BJD 2458432.7317: recovered, depth 7390 ± 344 ppm (catalogue 9180 ppm); BJD 2458433.6512: recovered, depth 4969 ± 376 ppm (catalogue 9180 ppm); BJD 2458434.5708: recovered, depth 7603 ± 348 ppm (catalogue 9180 ppm); BJD 2458435.4904: recovered, depth 5781 ± 447 ppm (catalogue 9180 ppm); BJD 2458436.4099: recovered, depth 9677 ± 474 ppm (catalogue 9180 ppm); BJD 2458438.2491: not recovered, depth -4520 ± 489 ppm (catalogue 9180 ppm); BJD 2458439.1686: recovered, depth 6544 ± 394 ppm (catalogue 9180 ppm); BJD 2458440.0882: recovered, depth 6651 ± 367 ppm (catalogue 9180 ppm); BJD 2458441.0077: recovered, depth 6955 ± 390 ppm (catalogue 9180 ppm); BJD 2458441.9273: recovered, depth 6936 ± 355 ppm (catalogue 9180 ppm); BJD 2458442.8469: recovered, depth 6108 ± 348 ppm (catalogue 9180 ppm); BJD 2458443.7664: recovered, depth 7358 ± 359 ppm (catalogue 9180 ppm); BJD 2458444.6860: recovered, depth 5321 ± 371 ppm (catalogue 9180 ppm); BJD 2458445.6055: recovered, depth 8469 ± 369 ppm (catalogue 9180 ppm); BJD 2458446.5251: recovered, depth 5284 ± 376 ppm (catalogue 9180 ppm); BJD 2458447.4447: recovered, depth 7831 ± 357 ppm (catalogue 9180 ppm); BJD 2458448.3642: recovered, depth 6524 ± 378 ppm (catalogue 9180 ppm); BJD 2458449.2838: recovered, depth 8176 ± 378 ppm (catalogue 9180 ppm); BJD 2458450.2034: gap (catalogue 9180 ppm); BJD 2458451.1229: gap (catalogue 9180 ppm); BJD 2458452.0425: recovered, depth 6231 ± 380 ppm (catalogue 9180 ppm); BJD 2458452.9620: recovered, depth 7200 ± 359 ppm (catalogue 9180 ppm); BJD 2458453.8816: recovered, depth 5794 ± 366 ppm (catalogue 9180 ppm); BJD 2458454.8012: recovered, depth 7578 ± 353 ppm (catalogue 9180 ppm); BJD 2458455.7207: recovered, depth 6338 ± 366 ppm (catalogue 9180 ppm); BJD 2458456.6403: recovered, depth 6741 ± 358 ppm (catalogue 9180 ppm); BJD 2458457.5599: recovered, depth 5657 ± 362 ppm (catalogue 9180 ppm); BJD 2458458.4794: recovered, depth 7577 ± 352 ppm (catalogue 9180 ppm); BJD 2458459.3990: recovered, depth 6661 ± 378 ppm (catalogue 9180 ppm); BJD 2458460.3185: recovered, depth 7734 ± 372 ppm (catalogue 9180 ppm); BJD 2458461.2381: recovered, depth 6550 ± 370 ppm (catalogue 9180 ppm); BJD 2458462.1577: recovered, depth 8571 ± 362 ppm (catalogue 9180 ppm); BJD 2458463.0772: recovered, depth 5299 ± 414 ppm (catalogue 9180 ppm); BJD 2458463.9968: gap (catalogue 9180 ppm); BJD 2458468.5946: not recovered, depth 5362 ± 395 ppm (catalogue 9180 ppm); BJD 2458469.5142: not recovered, depth 6762 ± 383 ppm (catalogue 9180 ppm); BJD 2458470.4337: not recovered, depth 5640 ± 359 ppm (catalogue 9180 ppm); BJD 2458471.3533: not recovered, depth 8239 ± 340 ppm (catalogue 9180 ppm); BJD 2458472.2728: not recovered, depth 5764 ± 353 ppm (catalogue 9180 ppm); BJD 2458473.1924: not recovered, depth 8159 ± 342 ppm (catalogue 9180 ppm); BJD 2458474.1120: not recovered, depth 6175 ± 359 ppm (catalogue 9180 ppm); BJD 2458475.0315: not recovered, depth 8489 ± 356 ppm (catalogue 9180 ppm); BJD 2458475.9511: not recovered, depth 5960 ± 378 ppm (catalogue 9180 ppm); BJD 2458476.8706: not recovered, depth 5973 ± 339 ppm (catalogue 9180 ppm); BJD 2458477.7902: gap (catalogue 9180 ppm); BJD 2458478.7098: not recovered, depth 6124 ± 352 ppm (catalogue 9180 ppm); BJD 2458479.6293: not recovered, depth 6120 ± 349 ppm (catalogue 9180 ppm); BJD 2458480.5489: not recovered, depth 7810 ± 347 ppm (catalogue 9180 ppm); BJD 2458481.4685: not recovered, depth 6655 ± 344 ppm (catalogue 9180 ppm); BJD 2458482.3880: not recovered, depth 6902 ± 343 ppm (catalogue 9180 ppm); BJD 2458483.3076: not recovered, depth 6524 ± 350 ppm (catalogue 9180 ppm); BJD 2458484.2271: not recovered, depth 8406 ± 349 ppm (catalogue 9180 ppm); BJD 2458485.1467: not recovered, depth 5538 ± 356 ppm (catalogue 9180 ppm); BJD 2458486.0663: not recovered, depth 7284 ± 367 ppm (catalogue 9180 ppm); BJD 2458486.9858: not recovered, depth 6597 ± 393 ppm (catalogue 9180 ppm); BJD 2458487.9054: not recovered, depth 9487 ± 372 ppm (catalogue 9180 ppm); BJD 2458488.8249: not recovered, depth 6759 ± 361 ppm (catalogue 9180 ppm); BJD 2458489.7445: not recovered, depth 8619 ± 341 ppm (catalogue 9180 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 4.5, 5, 3, 3.5, 12; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-275.01: Gaia DR3 4660192386982447232 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.03") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-275.01: dwarf priors not applied — RUWE 5.5791526 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-275.01: 190 Gaia neighbour(s) within 52.5", contamination 16.49%; depth 7491 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 4660192490061661056, 29.7", ΔG 3.99); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-275.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-275.01: TOI-275.01 otype err (star_or_other) at 0.8" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-275-01.yaml
python -m cygnus.multi report campaigns/toi-275-01.yaml
```
