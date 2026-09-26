<!-- cygnus:generated-draft -->
# Known-object test, TOI-3048.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3048-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #799, calibrate_screen #762, event_census #775, fetch_products #760, known_signal_recovery #765, moving_objects #777, period_aliases #776, prior_art #801, residual_screen #768, stellar_context #766, variability_guard #800
- Runner finished (UTC): 2026-09-26T10:19:41Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 811 threshold entries forming **152 distinct event(s)**, **54 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3048.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 304426002 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 177.796145 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -65.316829 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459358.750411 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 29540.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.173 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.3662 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | lightcurve | 64 | False | `024a15b458128c81` | True |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | lightcurve | 65 | False | `dd4e7810cd2305c2` | True |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | lightcurve | 99 | False | `d14f99d6fa9cfe49` | True |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | lightcurve | 100 | False | `559c340b6b00f830` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 29540 | — |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | — | epoch not in this light curve | — | — | 29540 | — |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 29540 | — |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 29540 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461094.65991 | -0.04592 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461083.15863 | -0.04238 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.95198 | -0.04196 | 37 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.90614 | -0.03951 | 27 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461077.36665 | -0.03853 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461065.86743 | -0.03794 | 80 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461077.40693 | -0.03755 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.80914 | -0.03720 | 37 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.45560 | -0.03707 | 21 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.83901 | -0.03674 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461077.35068 | -0.03649 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460079.62235 | -0.03633 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460045.05350 | -0.03574 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461083.10932 | -0.03520 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460045.10628 | -0.03512 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460056.58213 | -0.03490 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.88114 | -0.03473 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.77442 | -0.03456 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460073.84533 | -0.03371 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461065.80978 | -0.03366 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.14159 | -0.03333 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461054.32306 | -0.03318 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461048.54707 | -0.03309 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.87350 | -0.03299 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461071.62884 | -0.03237 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.41254 | -0.03228 | 34 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460056.62866 | -0.03205 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461083.22460 | -0.03189 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.43963 | -0.03137 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460073.90783 | -0.03136 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460073.94880 | -0.03023 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.37713 | -0.03023 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460073.88838 | -0.02996 | 36 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.98393 | -0.02991 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461048.60471 | -0.02973 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.86956 | -0.02968 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461083.21349 | -0.02958 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.48615 | -0.02818 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460044.99725 | -0.02785 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460045.11878 | -0.02754 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460056.52865 | -0.02718 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460079.60915 | -0.02716 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461098.99067 | -0.02711 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461065.79451 | -0.02695 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.88415 | -0.02690 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460056.64324 | -0.02598 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460056.65504 | -0.02540 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461048.49498 | -0.02492 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461065.80006 | -0.02470 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.12909 | -0.02344 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460079.72512 | -0.02314 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.36532 | -0.02248 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460061.95577 | -0.02236 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461048.62971 | -0.02150 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461094.76478 | -0.03099 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461085.88168 | -0.03057 | 2 | PDCSAP | 1 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461094.64325 | -0.03057 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461094.75853 | -0.03043 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.49171 | -0.02875 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460044.99169 | -0.02834 | 2 | PDCSAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.86934 | -0.02775 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461083.09682 | -0.02756 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461094.09600 | -0.02740 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460079.71054 | -0.02723 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461077.33401 | -0.02714 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461085.67889 | -0.02676 | 2 | PDCSAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461077.45485 | -0.02674 | 4 | PDCSAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461085.44694 | -0.02613 | 2 | PDCSAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.99157 | -0.02604 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461065.93062 | -0.02583 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461071.56426 | -0.02577 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460079.60290 | -0.02572 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.75567 | -0.02570 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460073.83491 | -0.02568 | 2 | PDCSAP | 1, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460082.17926 | -0.02559 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.15686 | -0.02551 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461085.68514 | -0.02545 | 5 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.13603 | -0.02524 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460089.76245 | -0.02502 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460096.19633 | -0.02482 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.08186 | -0.02472 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460096.31785 | -0.02442 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460096.03661 | -0.02426 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461071.70871 | -0.02412 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460050.76331 | -0.02285 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.09852 | -0.02282 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.05616 | -0.02250 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.02074 | -0.02074 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.03046 | -0.02016 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461071.75732 | -0.02006 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461054.38904 | -0.01978 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.09297 | -0.01960 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.03741 | -0.01946 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461063.10825 | -0.01943 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461071.85455 | -0.01869 | 2 | PDCSAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461093.13901 | -0.01811 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461099.31499 | -0.01733 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.12076 | -0.01674 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461099.35180 | -0.01636 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460083.20563 | -0.01621 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.12492 | -0.01563 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.66024 | -0.01540 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.54010 | -0.01494 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460054.84739 | -0.01484 | 4 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.69566 | -0.01480 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461093.89599 | -0.01479 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460054.86683 | -0.01446 | 2 | SAP | 1, 2 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460083.25285 | -0.01441 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461092.87649 | -0.01385 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.26381 | -0.01381 | 4 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.81104 | -0.01380 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461093.74042 | -0.01372 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.65121 | -0.01371 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.88465 | -0.01355 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.83525 | -0.01332 | 3 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.88456 | -0.01326 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.49982 | -0.01306 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000304426002-0257-s_lc.fits` | 2460056.52379 | -0.01289 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461093.79043 | -0.01271 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.98048 | -0.01265 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461092.77649 | -0.01264 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.98604 | -0.01262 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.76372 | -0.01262 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.72424 | -0.01245 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461052.90493 | -0.01243 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.51093 | -0.01237 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.64566 | -0.01237 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460085.36949 | -0.01235 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.83039 | -0.01232 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.97354 | -0.01224 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.05826 | -0.01224 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.79854 | -0.01211 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.89715 | -0.01197 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460089.81523 | -0.01191 | 2 | SAP | 1 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460091.04715 | -0.01184 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.84984 | -0.01182 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.87215 | -0.01182 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.62691 | -0.01178 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460090.92285 | -0.01165 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461052.89104 | -0.01141 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.92831 | -0.01140 | 3 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461088.06929 | -0.01140 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.89289 | -0.01140 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461099.34208 | -0.01131 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460089.82773 | -0.01125 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461052.88132 | -0.01124 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.86650 | -0.01120 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461052.86326 | -0.01116 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460089.03747 | -0.01115 | 2 | SAP | 1 | no |
| `tess2026033082000-s0100-0000000304426002-0302-s_lc.fits` | 2461087.77622 | -0.01092 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000304426002-0300-s_lc.fits` | 2461072.57542 | -0.01056 | 2 | SAP | 1 | no |
| `tess2023124020739-s0065-0000000304426002-0259-s_lc.fits` | 2460094.92622 | -0.01033 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3048.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:19:37Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:19:39Z: TOI-3048.01 (TIC 304426002, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:19:40Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:19:40Z: TOI-3048.01 (Pl?); TOI-3048 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3048.01: Gaia DR3 5332388574447939328 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3048.01: dwarf priors not applied — 3.72 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3048.01: 253 Gaia neighbour(s) within 52.5", contamination 88.75%; depth 29540 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 5332388647516589312, 39.8", ΔG -1.90); a centroid test is needed |
| Pointing and quality census per event | failed | 54 persistent event(s), 31 clean; BJD 2460045.0535 suspect: MOM_CENTR1 z=+5.7; BJD 2460061.9558 suspect: manual exclude (in event); BJD 2460073.8453 suspect: MOM_CENTR2 z=+7.8; BJD 2460073.8884 suspect: MOM_CENTR1 z=+5.6, MOM_CENTR2 z=+9.9 |
| Moving objects at screen-event epochs | inconclusive | 54 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3048.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3048.01: TOI-3048.01 otype Pl? (star_or_other) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3048-01.yaml
python -m cygnus.multi report campaigns/toi-3048-01.yaml
```
