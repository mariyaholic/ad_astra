<!-- cygnus:generated-draft -->
# Known-object test, TOI-3958.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3958-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5010, calibrate_screen #4941, event_census #4954, fetch_independent #5007, fetch_products #4925, known_signal_recovery #4945, moving_objects #5000, period_aliases #4955, prior_art #5012, residual_screen #4953, stellar_context #4949, variability_guard #5011
- Runner finished (UTC): 2026-09-30T22:49:22Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3958.01 (BJD 2459864.0714: gap (catalogue 5497 ppm); BJD 2459876.0746: recovered, depth 4359 ± 264 ppm (catalogue 5497 ppm); BJD 2459888.0777: partial, depth 4077 ± 264 ppm (catalogue 5497 ppm); BJD 2459900.0809: partial, depth 4570 ± 253 ppm (catalogue 5497 ppm); BJD 2460404.2138: not recovered, depth -675 ± 269 ppm (catalogue 5497 ppm); BJD 2460416.2170: gap (catalogue 5497 ppm); BJD 2460440.2233: not recovered, depth -144 ± 268 ppm (catalogue 5497 ppm); BJD 2460452.2265: partial, depth 2798 ± 245 ppm (catalogue 5497 ppm); BJD 2460596.2644: gap (catalogue 5497 ppm); BJD 2460608.2676: not recovered, depth -298 ± 279 ppm (catalogue 5497 ppm); BJD 2460620.2708: not recovered, depth 353 ± 268 ppm (catalogue 5497 ppm); BJD 2460632.2739: not recovered, depth 263 ± 262 ppm (catalogue 5497 ppm)).
Outside the catalogued epoch the screen left 171 threshold entries forming **69 distinct event(s)**, **14 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459853.4735 matches the catalogued transit's depth (4217 vs 4359 ppm), 22.653 d later; 0 of 22 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3958.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 279383896 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 349.685957 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 63.250498 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459864.071397 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 12.0031646 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5497.3001958 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.2145528 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.5687 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-22 12:04:07 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | lightcurve | 57 | True | `cae89b0ae0d4301f` | True |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | lightcurve | 58 | False | `3c9becdf850f1408` | True |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | lightcurve | 77 | False | `9353dcbc5507ce02` | True |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | lightcurve | 78 | False | `3ffff8293b58cff9` | True |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | lightcurve | 84 | False | `b3febefcd5432edd` | True |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | lightcurve | 85 | False | `d1bb6eff45121641` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459864.07140 | gap | 0 | — | 5497 | — |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459876.07456 | recovered | 157 | 4359 ± 264 | 5497 | 1.25 |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | 2459888.07773 | partial | 156 | 4077 ± 264 | 5497 | 1.47 |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | 2459900.08089 | partial | 157 | 4570 ± 253 | 5497 | -0.78 |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460404.21380 | not_recovered | 156 | -675 ± 269 | 5497 | — |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460416.21697 | gap | 0 | — | 5497 | — |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460440.22330 | not_recovered | 157 | -144 ± 268 | 5497 | — |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460452.22646 | partial | 146 | 2798 ± 245 | 5497 | -0.45 |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460596.26444 | gap | 0 | — | 5497 | — |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460608.26760 | not_recovered | 156 | -298 ± 279 | 5497 | — |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460620.27077 | not_recovered | 157 | 353 ± 268 | 5497 | — |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460632.27393 | not_recovered | 156 | 263 ± 262 | 5497 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.34646 | -0.01181 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.31313 | -0.01161 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460405.10786 | -0.01160 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.34204 | -0.01142 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459853.47348 | -0.01059 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.31730 | -0.01052 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460633.28792 | -0.00992 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460610.72571 | -0.00985 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460609.32016 | -0.00967 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460633.27403 | -0.00965 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460610.66460 | -0.00965 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.26035 | -0.00962 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.37077 | -0.00942 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460624.18948 | -0.00857 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.47784 | -0.01314 | 90 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460417.21421 | -0.01206 | 2 | SAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | 2459882.55010 | -0.01128 | 2 | PDCSAP | 2, 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460441.13236 | -0.01108 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459853.44917 | -0.01045 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.57020 | -0.01041 | 13 | SAP | 2, 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.65177 | -0.01034 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.55562 | -0.01016 | 6 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.60979 | -0.01003 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459853.42764 | -0.00979 | 2 | PDCSAP | 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460418.37948 | -0.00967 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460422.54892 | -0.00948 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459853.46237 | -0.00926 | 2 | PDCSAP | 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460633.31709 | -0.00920 | 2 | PDCSAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460610.99098 | -0.00920 | 2 | PDCSAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.60215 | -0.00918 | 7 | SAP | 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460405.14606 | -0.00916 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.40480 | -0.00900 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460405.04953 | -0.00899 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460405.20370 | -0.00899 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.63271 | -0.00885 | 3 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.62229 | -0.00878 | 10 | SAP | 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.60038 | -0.00871 | 2 | SAP | 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.50732 | -0.00871 | 4 | SAP | 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460405.15786 | -0.00870 | 3 | PDCSAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.54451 | -0.00862 | 4 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459853.36792 | -0.00857 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.20871 | -0.00851 | 2 | SAP | 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.58093 | -0.00846 | 2 | SAP | 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.54621 | -0.00839 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460599.52290 | -0.00825 | 2 | SAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460616.90345 | -0.00823 | 2 | SAP | 2, 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.34899 | -0.00822 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.59034 | -0.00819 | 8 | SAP | 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460421.38364 | -0.00808 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460418.51143 | -0.00805 | 2 | SAP | 2 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.56635 | -0.00802 | 3 | SAP | 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460441.25598 | -0.00801 | 2 | SAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460629.66855 | -0.00798 | 2 | SAP | 2, 3 | no |
| `tess2024114025118-s0078-0000000279383896-0273-s_lc.fits` | 2460437.26635 | -0.00794 | 3 | SAP | 3 | no |
| `tess2022302161335-s0058-0000000279383896-0247-s_lc.fits` | 2459910.01631 | -0.00790 | 2 | SAP | 1 | no |
| `tess2024085201119-s0077-0000000279383896-0272-s_lc.fits` | 2460421.40309 | -0.00788 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.71257 | -0.00779 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.64312 | -0.00778 | 8 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460609.33405 | -0.00764 | 2 | SAP | 1, 2 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460621.38535 | -0.00760 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460629.20883 | -0.00732 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.68201 | -0.00731 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.70423 | -0.00731 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.66673 | -0.00730 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459866.68896 | -0.00721 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000279383896-0282-s_lc.fits` | 2460629.41855 | -0.00712 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000279383896-0245-s_lc.fits` | 2459860.33054 | -0.00698 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460587.89498 | -0.00630 | 2 | SAP | 1 | no |
| `tess2024274222008-s0084-0000000279383896-0281-s_lc.fits` | 2460603.92292 | -0.00622 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459853.47348 | 4217 | 4359 | 22.6530 | 0 / 22 |  |
| 2460405.10786 | 3884 | 4359 | 528.9814 | 7 / 528 | 528.981, 264.491, 176.327, 132.245, 88.1636, 58.7757, 48.0892 |
| 2460609.32016 | 4592 | 4359 | 733.1937 | 14 / 733 | 733.194, 366.597, 244.398, 183.298, 146.639, 122.199, 91.6492, 73.3194, 66.654, 61.0995, 48.8796, 45.8246, 38.5891, 36.6597 |
| 2460610.66460 | 2312 | 4359 | 734.5381 | 15 / 734 | 734.538, 367.269, 244.846, 183.635, 146.908, 122.423, 91.8173, 73.4538, 66.7762, 61.2115, 56.5029, 48.9692, 45.9086, 43.2081, 36.7269 |
| 2460610.72571 | 2728 | 4359 | 734.5992 | 14 / 734 | 734.599, 367.3, 244.866, 183.65, 146.92, 122.433, 91.8249, 73.4599, 66.7817, 61.2166, 56.5076, 48.9733, 45.9125, 36.73 |
| 2460621.26035 | 2461 | 4359 | 745.1338 | 10 / 745 | 745.134, 372.567, 248.378, 149.027, 124.189, 106.448, 82.7926, 53.2238, 41.3963, 39.2176 |
| 2460621.31313 | 3608 | 4359 | 745.1866 | 10 / 745 | 745.187, 372.593, 248.395, 149.037, 124.198, 106.455, 82.7985, 53.2276, 41.3993, 39.2203 |
| 2460621.31730 | 3672 | 4359 | 745.1908 | 10 / 745 | 745.191, 372.595, 248.397, 149.038, 124.198, 106.456, 82.799, 53.2279, 41.3995, 39.2206 |
| 2460621.34646 | 3727 | 4359 | 745.2200 | 10 / 745 | 745.22, 372.61, 248.407, 149.044, 124.203, 106.46, 82.8022, 53.23, 41.4011, 39.2221 |
| 2460621.37077 | 3489 | 4359 | 745.2443 | 10 / 745 | 745.244, 372.622, 248.415, 149.049, 124.207, 106.463, 82.8049, 53.2317, 41.4025, 39.2234 |
| 2460633.27403 | 3044 | 4359 | 757.1475 | 11 / 757 | 757.148, 378.574, 252.382, 151.429, 126.191, 108.164, 84.1275, 68.8316, 54.082, 50.4765, 36.0546 |
| 2460633.28792 | 3378 | 4359 | 757.1614 | 11 / 757 | 757.161, 378.581, 252.387, 151.432, 126.194, 108.166, 84.129, 68.8329, 54.083, 50.4774, 36.0553 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3958.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:49:08Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:49:11Z: TOI-3958.01 (TIC 279383896, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:49:14Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:49:17Z: TOI-3958 (*); TOI-3958.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459864.0714: gap (catalogue 5497 ppm); BJD 2459876.0746: recovered, depth 4359 ± 264 ppm (catalogue 5497 ppm); BJD 2459888.0777: partial, depth 4077 ± 264 ppm (catalogue 5497 ppm); BJD 2459900.0809: partial, depth 4570 ± 253 ppm (catalogue 5497 ppm); BJD 2460404.2138: not recovered, depth -675 ± 269 ppm (catalogue 5497 ppm); BJD 2460416.2170: gap (catalogue 5497 ppm); BJD 2460440.2233: not recovered, depth -144 ± 268 ppm (catalogue 5497 ppm); BJD 2460452.2265: partial, depth 2798 ± 245 ppm (catalogue 5497 ppm); BJD 2460596.2644: gap (catalogue 5497 ppm); BJD 2460608.2676: not recovered, depth -298 ± 279 ppm (catalogue 5497 ppm); BJD 2460620.2708: not recovered, depth 353 ± 268 ppm (catalogue 5497 ppm); BJD 2460632.2739: not recovered, depth 263 ± 262 ppm (catalogue 5497 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 12 repeat-candidate event(s); first at BJD 2459853.4735, ΔT = 22.653 d, 0 of 22 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3958.01: Gaia DR3 2015357191117217920 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3958.01: Teff 5977 K, R* 1.28 ± 0.10, M* 1.20 ± 0.12, ρ* 0.57 ± 0.15 ρ☉ (dwarf sequence, M_G 3.76, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3958.01: 69 Gaia neighbour(s) within 52.5", contamination 48.20%; depth 4359 ppm (measured depth of the recovered catalogued transit); 6 could produce it if fully eclipsed (brightest 2015357191117217664, 44.6", ΔG 0.54); a centroid test is needed |
| Pointing and quality census per event | failed | 14 persistent event(s), 9 clean; BJD 2459853.4735 suspect: earth point (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+9.8, MOM_CENTR2 z=-15.8, POS_CORR1 z=+13.8, POS_CORR2 z=-16.6; BJD 2460405.1079 suspect: SAP_BKG z=+7.0; BJD 2460437.3420 suspect: POS_CORR2 z=-5.3; BJD 2460610.6646 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-10.5, MOM_CENTR2 z=-15.3, POS_CORR1 z=-11.8, POS_CORR2 z=-21.2, SAP_BKG z=-40.2 |
| Moving objects at screen-event epochs | inconclusive | 14 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 11 light curve × candidate pair(s); aliases supported: none; excluded: none; 122 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-3958.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3958.01: TOI-3958.01 otype Pl? (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 2 possible published-ephemeris overlap(s) within 1 d (TOI-3958.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3958-01.yaml
python -m cygnus.multi report campaigns/toi-3958-01.yaml
```
