<!-- [private Drive store] -->
# Known-object test, TOI-3157.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3157-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #580, calibrate_screen #513, event_census #538, fetch_products #509, known_signal_recovery #516, moving_objects #540, period_aliases #539, prior_art #582, residual_screen #525, stellar_context #518, variability_guard #581
- Runner finished (UTC): 2026-09-26T10:10:49Z

## Bottom line

Positive control **failed**: BJD 2460043.1381: not recovered, depth 45520 ± 4197 ppm (catalogue 66566 ppm).
Outside the catalogued epoch the screen left 330 threshold entries forming **83 distinct event(s)**, **45 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3157.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 456962262 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 201.47318 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -59.18126 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460043.13808 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 66566.1005931 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.6626984 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.6244 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-07-22 12:04:25 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | lightcurve | 64 | True | `e68d7a19e2f6c781` | True |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | lightcurve | 65 | False | `f7a344c449c513c8` | True |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | lightcurve | 99 | False | `b3c2765af12c2879` | True |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | lightcurve | 100 | False | `8bd2d43a7f18c0a0` | True |
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | lightcurve | 101 | False | `04cb07158607432e` | True |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | lightcurve | 102 | False | `36b65f63460f7f8f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 2460043.13808 | not_recovered | 110 | 45520 ± 4197 | 66566 | — |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | — | epoch not in this light curve | — | — | 66566 | — |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 66566 | — |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 66566 | — |
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 66566 | — |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 66566 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | 2461106.70365 | -0.19267 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461141.27683 | -0.18354 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | 2461115.33332 | -0.17286 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461138.40103 | -0.16534 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 2460048.88970 | -0.16523 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461144.15748 | -0.16265 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | 2461109.56077 | -0.16215 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 2460054.65235 | -0.15817 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 2460063.35040 | -0.15414 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461138.36631 | -0.14944 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461145.60683 | -0.14315 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | 2460077.73309 | -0.13773 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | 2460086.36356 | -0.12784 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | 2460077.70809 | -0.12246 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461086.50369 | -0.10269 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461089.38028 | -0.09861 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461074.99872 | -0.09728 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461086.51480 | -0.09555 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461086.52522 | -0.09394 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461074.95983 | -0.09311 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461095.14040 | -0.08658 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461098.03364 | -0.08518 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461051.96038 | -0.06749 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461051.91732 | -0.06441 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461063.45141 | -0.06125 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461049.03797 | -0.06067 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461063.43682 | -0.05985 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461063.46043 | -0.05891 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461069.22611 | -0.05875 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461054.78486 | -0.05814 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461069.20458 | -0.05681 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461051.89579 | -0.05642 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461066.35161 | -0.05597 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461066.34327 | -0.05596 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461054.80014 | -0.05569 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.10963 | -0.05555 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461049.08033 | -0.05392 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.08394 | -0.05313 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.11727 | -0.05265 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461066.35925 | -0.05259 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461066.36619 | -0.05247 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461049.05255 | -0.05189 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461063.42502 | -0.05087 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461063.47641 | -0.04980 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.13325 | -0.04912 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461149.91387 | -0.13874 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461144.12484 | -0.13711 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 2461141.30253 | -0.13688 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461086.54813 | -0.08121 | 2 | PDCSAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461092.30549 | -0.08119 | 2 | PDCSAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 2461089.40667 | -0.07857 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 2460048.89387 | -0.06740 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461049.02477 | -0.06054 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.20554 | -0.06018 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461051.90690 | -0.05934 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461054.83903 | -0.05819 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461051.93815 | -0.05759 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461051.92774 | -0.05474 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461054.80500 | -0.05399 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.46111 | -0.05347 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.08880 | -0.05330 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461069.25528 | -0.05316 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.92774 | -0.05311 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461066.32522 | -0.05273 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461054.82931 | -0.05192 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.10130 | -0.04999 | 2 | PDCSAP | 2 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.05824 | -0.04958 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.28610 | -0.04948 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461066.37383 | -0.04852 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461069.27750 | -0.04822 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.88468 | -0.04661 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461054.79597 | -0.04623 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.29721 | -0.04537 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.08192 | -0.04465 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.11248 | -0.04413 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.15276 | -0.04109 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.89857 | -0.04060 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.10137 | -0.03894 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.03469 | -0.03869 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.18193 | -0.03503 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.00553 | -0.03496 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461072.94163 | -0.03303 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 2461073.02080 | -0.03069 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3157.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:10:46Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:10:47Z: TOI-3157.01 (TIC 456962262, disposition PC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:10:48Z: Gaia DR3 5869860717491400320 (type E, P 2.08874 d)
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:10:49Z: Gaia DR3 5869860717491400320 (EB*); TOI-3157 (*); TOI-3157.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2460043.1381: not recovered, depth 45520 ± 4197 ppm (catalogue 66566 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5, 3, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 20%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3157.01: Gaia DR3 5869861091104400384 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3157.01: dwarf priors not applied — parallax/error 2.2 < 5; RUWE 17.894434 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3157.01: 244 Gaia neighbour(s) within 52.5", contamination 85.59%; depth 66566 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 5869860923670499456, 41.0", ΔG -0.17); a centroid test is needed |
| Pointing and quality census per event | failed | 45 persistent event(s), 33 clean; BJD 2460048.8897 suspect: MOM_CENTR1 z=-6.2, POS_CORR1 z=-15.4, POS_CORR2 z=+11.2; BJD 2460054.6523 suspect: manual exclude (within ±0.25 d), SAP_BKG z=-11.5; BJD 2461063.4250 suspect: POS_CORR1 z=+12.9, POS_CORR2 z=+15.7; BJD 2461063.4368 suspect: POS_CORR1 z=+12.9, POS_CORR2 z=+15.4 |
| Moving objects at screen-event epochs | inconclusive | 45 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 6 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | failed | TOI-3157.01: Gaia DR3 5869860717491400320   E                              P=2.08874 at 4.3" |
| Object-class guard (SIMBAD) | passed | TOI-3157.01: TOI-3157.01 otype Pl? (star_or_other) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3157-01.yaml
python -m cygnus.multi report campaigns/toi-3157-01.yaml
```
