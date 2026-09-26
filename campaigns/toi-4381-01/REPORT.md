<!-- cygnus:generated-draft -->
# Known-object test, TOI-4381.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4381-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1101, calibrate_screen #751, event_census #756, fetch_products #750, known_signal_recovery #752, moving_objects #1097, period_aliases #981, prior_art #1103, residual_screen #754, stellar_context #753, variability_guard #1102
- Runner finished (UTC): 2026-09-26T10:36:29Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4381.01 (BJD 2459362.9262: recovered, depth 59978 ± 3842 ppm (catalogue 39325 ppm)).
Outside the catalogued epoch the screen left 530 threshold entries forming **92 distinct event(s)**, **40 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461074.4717 matches the catalogued transit's depth (39105 vs 59978 ppm), 1711.533 d later; 22 of 1711 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4381.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 305767364 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 263.167427 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -64.352997 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459362.92619 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 39324.5082012 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.2238426 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2907 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2022-08-19 12:02:36 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | lightcurve | 39 | True | `78cee9bd3b8f0cc3` | True |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | lightcurve | 100 | False | `112695369b55d3ae` | True |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | lightcurve | 101 | False | `5fdfb13df9c6c6db` | True |
| `tess2026086090000-s0102-0000000305767364-0304-s_lc.fits` | lightcurve | 102 | False | `d52cd52739c9ec95` | True |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | lightcurve | 103 | False | `7eb9f57808bed0a9` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459362.92619 | recovered | 67 | 59978 ± 3842 | 39325 | 0.31 |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 39325 | — |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 39325 | — |
| `tess2026086090000-s0102-0000000305767364-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 39325 | — |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | — | epoch not in this light curve | — | — | 39325 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026086090000-s0102-0000000305767364-0304-s_lc.fits` | 8 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461108.92334 | -0.06079 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461110.42206 | -0.05818 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461122.40004 | -0.05714 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461162.81730 | -0.05710 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461176.32070 | -0.05663 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461093.94518 | -0.05565 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461164.34237 | -0.05528 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461095.44737 | -0.05375 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461107.42670 | -0.05353 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461174.80536 | -0.05220 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461081.97009 | -0.05175 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461120.90271 | -0.05115 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461167.30780 | -0.05104 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461096.94261 | -0.04958 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461125.39539 | -0.04913 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461080.47209 | -0.04872 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461161.32417 | -0.04857 | 46 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461083.46949 | -0.04834 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461119.37829 | -0.04804 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461074.47172 | -0.04781 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461093.96671 | -0.04730 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461119.41371 | -0.04720 | 34 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461153.85707 | -0.04708 | 48 | PDCSAP+SAP | 1, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461123.89806 | -0.04690 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461105.90576 | -0.04550 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461078.94283 | -0.04532 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461111.93397 | -0.04466 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461117.93790 | -0.04405 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461098.44271 | -0.04333 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461092.45203 | -0.04331 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461116.41487 | -0.04286 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461077.48302 | -0.04160 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461084.96541 | -0.04056 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461089.44001 | -0.03891 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461102.93123 | -0.03887 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461104.44315 | -0.03835 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461101.42833 | -0.03828 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461087.96490 | -0.03816 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461090.94567 | -0.03759 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461075.98015 | -0.03729 | 57 | PDCSAP+SAP | 1, 3 | yes |
| `tess2026086090000-s0102-0000000305767364-0304-s_lc.fits` | 2461149.35956 | -0.06754 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459376.40452 | -0.05483 | 54 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461159.83520 | -0.04155 | 52 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459377.91981 | -0.04077 | 14 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459373.38782 | -0.03970 | 8 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459377.90453 | -0.03784 | 8 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461158.33859 | -0.03778 | 49 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459365.92520 | -0.03733 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459377.89273 | -0.03702 | 5 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459377.93231 | -0.03686 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459382.41010 | -0.03665 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459388.35869 | -0.03613 | 2 | PDCSAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459377.88370 | -0.03604 | 6 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461155.34050 | -0.03593 | 46 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461114.90850 | -0.03578 | 46 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459367.43217 | -0.03523 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459377.87398 | -0.03510 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459388.36425 | -0.03498 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461156.84059 | -0.03476 | 50 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459373.40518 | -0.03436 | 3 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459388.38091 | -0.03425 | 2 | PDCSAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459382.39621 | -0.03416 | 2 | SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459365.91270 | -0.03411 | 4 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461168.81968 | -0.03390 | 47 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459382.38787 | -0.03357 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461173.31156 | -0.03341 | 47 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459365.90159 | -0.03327 | 2 | PDCSAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459365.91825 | -0.03295 | 2 | PDCSAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461155.37592 | -0.03287 | 3 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459373.39199 | -0.03215 | 2 | SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461170.32045 | -0.03193 | 2 | PDCSAP+SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459388.39758 | -0.03089 | 2 | SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459386.87536 | -0.03081 | 2 | SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459382.38093 | -0.03052 | 2 | SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459368.20441 | -0.02973 | 2 | SAP | 1 | no |
| `tess2021146024351-s0039-0000000305767364-0210-s_lc.fits` | 2459364.44045 | -0.02968 | 2 | SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461161.30056 | -0.02951 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461158.37540 | -0.02823 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461170.33504 | -0.02793 | 7 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461174.84842 | -0.02771 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461170.30587 | -0.02635 | 5 | PDCSAP+SAP | 1 | no |
| `tess2026111101500-s0103-0000000305767364-0305-s_lc.fits` | 2461170.29962 | -0.02562 | 2 | PDCSAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461114.94530 | -0.02551 | 5 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461115.69606 | -0.02137 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461108.98168 | -0.01959 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461123.85917 | -0.01949 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461110.73736 | -0.01933 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461115.66342 | -0.01924 | 3 | PDCSAP+SAP | 1 | no |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461075.25649 | -0.01902 | 3 | PDCSAP+SAP | 1 | no |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461075.21691 | -0.01798 | 2 | PDCSAP | 1 | no |
| `tess2026033082000-s0100-0000000305767364-0302-s_lc.fits` | 2461075.29191 | -0.01764 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026060005000-s0101-0000000305767364-0303-s_lc.fits` | 2461107.27739 | -0.01656 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461074.47172 | 39105 | 59978 | 1711.5327 | 22 / 1711 | 1711.53, 855.766, 570.511, 427.883, 342.307, 285.255, 244.505, 213.942, 190.17, 171.153, 155.594, 142.628, 131.656, 122.252, 114.102, 106.971, 90.0807, 77.7969, 65.8282, 51.8646 |
| 2461077.48302 | 33695 | 59978 | 1714.5440 | 20 / 1714 | 1714.54, 857.272, 571.515, 428.636, 342.909, 285.757, 244.935, 214.318, 190.505, 171.454, 155.868, 142.879, 131.888, 122.467, 114.303, 107.159, 100.856, 74.5454, 63.5016, 61.2337 |
| 2461078.94283 | 36731 | 59978 | 1716.0038 | 25 / 1716 | 1716, 858.002, 572.001, 429.001, 343.201, 286.001, 245.143, 214.5, 190.667, 171.6, 156, 143, 132, 122.572, 114.4, 107.25, 100.941, 85.8002, 68.6402, 63.5557 |
| 2461080.47209 | 45897 | 59978 | 1717.5331 | 28 / 1717 | 1717.53, 858.766, 572.511, 429.383, 343.507, 286.255, 245.362, 214.692, 190.837, 171.753, 156.139, 143.128, 132.118, 122.681, 114.502, 107.346, 101.031, 71.5639, 68.7013, 63.6123 |
| 2461081.97009 | 49377 | 59978 | 1719.0311 | 24 / 1719 | 1719.03, 859.515, 573.01, 429.758, 343.806, 286.505, 245.576, 214.879, 191.004, 171.903, 156.276, 143.253, 132.233, 122.788, 114.602, 107.439, 101.12, 95.5017, 61.394, 57.301 |
| 2461083.46949 | 46170 | 59978 | 1720.5305 | 24 / 1720 | 1720.53, 860.265, 573.51, 430.133, 344.106, 286.755, 245.79, 215.066, 191.17, 172.053, 156.412, 143.377, 132.349, 122.895, 114.702, 107.533, 101.208, 95.585, 81.93, 68.8212 |
| 2461084.96541 | 36316 | 59978 | 1722.0264 | 26 / 1722 | 1722.03, 861.013, 574.009, 430.507, 344.405, 287.004, 246.004, 215.253, 191.336, 172.203, 156.548, 143.502, 132.464, 123.002, 114.802, 107.627, 101.296, 95.6681, 74.8707, 68.8811 |
| 2461090.94567 | 30816 | 59978 | 1728.0066 | 24 / 1728 | 1728.01, 864.003, 576.002, 432.002, 345.601, 288.001, 246.858, 216.001, 192.001, 172.801, 157.091, 144.001, 132.924, 123.429, 115.2, 108, 101.647, 96.0004, 90.9477, 75.1307 |
| 2461092.45203 | 41515 | 59978 | 1729.5130 | 30 / 1729 | 1729.51, 864.756, 576.504, 432.378, 345.903, 288.252, 247.073, 216.189, 192.168, 172.951, 157.228, 144.126, 133.04, 123.537, 115.301, 108.095, 101.736, 96.0841, 91.027, 86.4757 |
| 2461093.94518 | 46842 | 59978 | 1731.0062 | 26 / 1731 | 1731.01, 865.503, 577.002, 432.752, 346.201, 288.501, 247.287, 216.376, 192.334, 173.101, 157.364, 144.25, 133.154, 123.643, 115.4, 108.188, 101.824, 96.167, 91.1056, 86.5503 |
| 2461093.96671 | 43176 | 59978 | 1731.0277 | 25 / 1731 | 1731.03, 865.514, 577.009, 432.757, 346.205, 288.505, 247.29, 216.379, 192.336, 173.103, 157.366, 144.252, 133.156, 123.645, 115.402, 108.189, 101.825, 96.1682, 91.1067, 86.5514 |
| 2461095.44737 | 52236 | 59978 | 1732.5083 | 27 / 1732 | 1732.51, 866.254, 577.503, 433.127, 346.502, 288.751, 247.501, 216.564, 192.501, 173.251, 157.501, 144.376, 133.27, 123.751, 115.501, 108.282, 101.912, 96.2505, 91.1846, 86.6254 |
| 2461096.94261 | 47232 | 59978 | 1734.0036 | 25 / 1734 | 1734, 867.002, 578.001, 433.501, 346.801, 289.001, 247.715, 216.75, 192.667, 173.4, 157.637, 144.5, 133.385, 123.857, 115.6, 108.375, 102, 96.3335, 91.2633, 86.7002 |
| 2461098.44271 | 40501 | 59978 | 1735.5037 | 28 / 1735 | 1735.5, 867.752, 578.501, 433.876, 347.101, 289.251, 247.929, 216.938, 192.834, 173.55, 157.773, 144.625, 133.5, 123.965, 115.7, 108.469, 102.088, 96.4169, 91.3423, 86.7752 |
| 2461101.42833 | 31178 | 59978 | 1738.4893 | 30 / 1738 | 1738.49, 869.245, 579.496, 434.622, 347.698, 289.748, 248.356, 217.311, 193.166, 173.849, 158.044, 144.874, 133.73, 124.178, 115.899, 108.656, 102.264, 96.5827, 91.4994, 86.9245 |
| 2461105.90576 | 38750 | 59978 | 1742.9667 | 28 / 1742 | 1742.97, 871.483, 580.989, 435.742, 348.593, 290.495, 248.995, 217.871, 193.663, 174.297, 158.452, 145.247, 134.074, 124.498, 116.198, 108.935, 102.528, 96.8315, 91.7351, 87.1483 |
| 2461107.42670 | 51770 | 59978 | 1744.4877 | 28 / 1744 | 1744.49, 872.244, 581.496, 436.122, 348.897, 290.748, 249.213, 218.061, 193.832, 174.449, 158.59, 145.374, 134.191, 124.606, 116.299, 109.031, 102.617, 96.916, 91.8151, 87.2244 |
| 2461108.92334 | 58934 | 59978 | 1745.9843 | 31 / 1745 | 1745.98, 872.992, 581.995, 436.496, 349.197, 290.997, 249.426, 218.248, 193.998, 174.598, 158.726, 145.499, 134.306, 124.713, 116.399, 109.124, 102.705, 96.9991, 91.8939, 87.2992 |
| 2461110.42206 | 56107 | 59978 | 1747.4830 | 32 / 1747 | 1747.48, 873.741, 582.494, 436.871, 349.497, 291.247, 249.64, 218.435, 194.165, 174.748, 158.862, 145.624, 134.422, 124.82, 116.499, 109.218, 102.793, 97.0824, 91.9728, 87.3742 |
| 2461111.93397 | 35995 | 59978 | 1748.9949 | 29 / 1748 | 1748.99, 874.497, 582.998, 437.249, 349.799, 291.499, 249.856, 218.624, 194.333, 174.899, 159, 145.75, 134.538, 124.928, 116.6, 109.312, 102.882, 97.1664, 92.0524, 87.4497 |
| 2461117.93790 | 35850 | 59978 | 1754.9989 | 31 / 1754 | 1755, 877.499, 585, 438.75, 351, 292.5, 250.714, 219.375, 195, 175.5, 159.545, 146.25, 135, 125.357, 117, 109.687, 103.235, 97.4999, 92.3684, 87.7499 |
| 2461119.37829 | 39132 | 59978 | 1756.4393 | 35 / 1756 | 1756.44, 878.22, 585.48, 439.11, 351.288, 292.74, 250.92, 219.555, 195.16, 175.644, 159.676, 146.37, 135.111, 125.46, 117.096, 109.778, 103.32, 97.58, 92.4442, 87.822 |
| 2461119.41371 | 43625 | 59978 | 1756.4747 | 34 / 1756 | 1756.47, 878.237, 585.492, 439.119, 351.295, 292.746, 250.925, 219.559, 195.164, 175.648, 159.679, 146.373, 135.113, 125.463, 117.098, 109.78, 103.322, 97.5819, 92.446, 87.8237 |
| 2461120.90271 | 49836 | 59978 | 1757.9637 | 35 / 1757 | 1757.96, 878.982, 585.988, 439.491, 351.593, 292.994, 251.138, 219.745, 195.329, 175.796, 159.815, 146.497, 135.228, 125.569, 117.198, 109.873, 103.41, 97.6646, 92.5244, 87.8982 |
| 2461122.40004 | 55283 | 59978 | 1759.4610 | 38 / 1759 | 1759.46, 879.731, 586.487, 439.865, 351.892, 293.243, 251.352, 219.933, 195.496, 175.946, 159.951, 146.622, 135.343, 125.676, 117.297, 109.966, 103.498, 97.7478, 92.6032, 87.9731 |
| 2461123.89806 | 44432 | 59978 | 1760.9590 | 37 / 1760 | 1760.96, 880.48, 586.986, 440.24, 352.192, 293.493, 251.566, 220.12, 195.662, 176.096, 160.087, 146.747, 135.458, 125.783, 117.397, 110.06, 103.586, 97.8311, 92.6821, 88.048 |
| 2461125.39539 | 44496 | 59978 | 1762.4564 | 39 / 1762 | 1762.46, 881.228, 587.486, 440.614, 352.491, 293.743, 251.78, 220.307, 195.828, 176.246, 160.223, 146.871, 135.574, 125.89, 117.497, 110.153, 103.674, 97.9142, 92.7609, 88.1228 |
| 2461153.85707 | 38461 | 59978 | 1790.9180 | 35 / 1790 | 1790.92, 895.459, 596.973, 447.729, 358.184, 298.486, 255.845, 223.865, 198.991, 179.092, 162.811, 149.243, 137.763, 127.923, 119.394, 111.932, 105.348, 99.4954, 94.2588, 89.5459 |
| 2461161.32417 | 41057 | 59978 | 1798.3851 | 24 / 1798 | 1798.39, 899.193, 599.462, 449.596, 359.677, 299.731, 256.912, 224.798, 199.821, 179.839, 163.49, 149.865, 138.337, 128.456, 119.892, 112.399, 105.787, 99.9103, 94.6518, 89.9193 |
| 2461162.81730 | 47897 | 59978 | 1799.8783 | 23 / 1799 | 1799.88, 899.939, 599.959, 449.97, 359.976, 299.98, 257.125, 224.985, 199.987, 179.988, 163.625, 149.99, 138.452, 128.563, 119.992, 112.492, 105.875, 99.9932, 94.7304, 89.9939 |
| 2461164.34237 | 44230 | 59978 | 1801.4033 | 25 / 1801 | 1801.4, 900.702, 600.468, 450.351, 360.281, 300.234, 257.343, 225.175, 200.156, 180.14, 163.764, 150.117, 138.57, 128.672, 120.094, 112.588, 105.965, 100.078, 94.8107, 90.0702 |
| 2461167.30780 | 39212 | 59978 | 1804.3688 | 26 / 1804 | 1804.37, 902.184, 601.456, 451.092, 360.874, 300.728, 257.767, 225.546, 200.485, 180.437, 164.034, 150.364, 138.798, 128.883, 120.291, 112.773, 106.139, 100.243, 94.9668, 66.8285 |
| 2461174.80536 | 39571 | 59978 | 1811.8663 | 22 / 1811 | 1811.87, 905.933, 603.955, 452.967, 362.373, 301.978, 258.838, 226.483, 201.319, 181.187, 164.715, 150.989, 139.374, 129.419, 120.791, 113.242, 106.58, 100.659, 82.3576, 32.943 |
| 2461176.32070 | 46266 | 59978 | 1813.3817 | 21 / 1813 | 1813.38, 906.691, 604.461, 453.345, 362.676, 302.23, 259.055, 226.673, 201.487, 181.338, 164.853, 151.115, 139.491, 129.527, 120.892, 113.336, 106.669, 82.4264, 75.5576, 62.5304 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4381.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:36:25Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:36:26Z: TOI-4381.01 (TIC 305767364, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:36:28Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:36:28Z: TOI-4381 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459362.9262: recovered, depth 59978 ± 3842 ppm (catalogue 39325 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 8, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 20%, 20%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 34 repeat-candidate event(s); first at BJD 2461074.4717, ΔT = 1711.533 d, 22 of 1711 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1711.53, 855.766, 570.511, 427.883, 342.307, 285.255, 244.505, 213.942, 190.17, 171.153, 155.594, 142.628 … d); duration likelihood under Gaia priors (circular orbits) peaks at 13.5 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4381.01: Gaia DR3 5909925679911156608 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4381.01: Teff 5255 K, R* 0.83 ± 0.07, M* 0.89 ± 0.09, ρ* 1.56 ± 0.41 ρ☉ (dwarf sequence, M_G 5.47, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4381.01: 55 Gaia neighbour(s) within 52.5", contamination 34.33%; depth 59978 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 5909925684214320256, 18.8", ΔG 2.53); a centroid test is needed |
| Pointing and quality census per event | failed | 40 persistent event(s), 23 clean; BJD 2461074.4717 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+18.0, MOM_CENTR2 z=+13.1, POS_CORR1 z=+17.4, POS_CORR2 z=+12.5, SAP_BKG z=+451.8; BJD 2461083.4695 caution: manual exclude (within ±0.25 d); BJD 2461084.9654 suspect: SAP_BKG z=+70.5; BJD 2461087.9649 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+16.6, MOM_CENTR2 z=+12.9, POS_CORR1 z=+17.8, POS_CORR2 z=+10.9, SAP_BKG z=+230.6 |
| Moving objects at screen-event epochs | inconclusive | 40 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 7 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-4381.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4381.01: TOI-4381 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4381-01.yaml
python -m cygnus.multi report campaigns/toi-4381-01.yaml
```
