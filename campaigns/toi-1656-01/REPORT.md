<!-- cygnus:generated-draft -->
# Known-object test, TOI-1656.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1656-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #166, calibrate_screen #152, event_census #162, fetch_products #147, known_signal_recovery #153, moving_objects #165, period_aliases #163, prior_art #168, residual_screen #158, stellar_context #154, variability_guard #167
- Runner finished (UTC): 2026-09-26T09:55:35Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1656.01 (BJD 2459935.3134: recovered, depth 3737 ± 30 ppm (catalogue 6669 ppm)).
Outside the catalogued epoch the screen left 118 threshold entries forming **60 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1656.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 267694283 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 63.230018 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 53.68705 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459935.313412 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6669.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 9.386 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.54941 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-02-03 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | lightcurve | 59 | True | `331b9be015ef36ae` | True |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | lightcurve | 86 | False | `739feb156ea98940` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459935.31341 | recovered | 281 | 3737 ± 30 | 6669 | 3.32 |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | — | epoch not in this light curve | — | — | 6669 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.15248 | -0.00577 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.36502 | -0.00411 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.25529 | -0.00342 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.59557 | -0.00319 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.51293 | -0.00317 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.54001 | -0.00314 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460642.31360 | -0.00311 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.03859 | -0.00300 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.16918 | -0.00295 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.38029 | -0.00292 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.12335 | -0.00288 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.08377 | -0.00285 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.60668 | -0.00279 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.02335 | -0.00275 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.27613 | -0.00271 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.41849 | -0.00270 | 9 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.55248 | -0.00256 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460642.55805 | -0.00246 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.47613 | -0.00245 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.04418 | -0.00241 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.32613 | -0.00240 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.01502 | -0.00237 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.70249 | -0.00235 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.01776 | -0.00234 | 2 | SAP | 1 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.07123 | -0.00232 | 4 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.21085 | -0.00231 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.42960 | -0.00225 | 3 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.38945 | -0.00224 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.47972 | -0.00224 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.39415 | -0.00223 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.31918 | -0.00218 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.21502 | -0.00217 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.50195 | -0.00215 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.12609 | -0.00214 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.05803 | -0.00212 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.07474 | -0.00210 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.16502 | -0.00209 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.21918 | -0.00209 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.12752 | -0.00208 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460649.34140 | -0.00206 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.05109 | -0.00200 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.27054 | -0.00199 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459922.25609 | -0.00198 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.41498 | -0.00194 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.53111 | -0.00193 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000267694283-0283-s_lc.fits` | 2460641.08303 | -0.00188 | 2 | SAP | 1 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.53875 | -0.00188 | 3 | SAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.49778 | -0.00181 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.44361 | -0.00176 | 4 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.51722 | -0.00173 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459915.94778 | -0.00171 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.11167 | -0.00168 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.39778 | -0.00168 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459914.87416 | -0.00166 | 2 | SAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.50889 | -0.00156 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.69222 | -0.00155 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459911.97553 | -0.00155 | 2 | SAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459915.48111 | -0.00146 | 2 | SAP | 1, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459930.53375 | -0.00137 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000267694283-0248-s_lc.fits` | 2459916.96861 | -0.00131 | 2 | PDCSAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1656.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:55:32Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:55:33Z: TOI-1656.01 (TIC 267694283, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:55:35Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:55:35Z: TOI-1656.01 (err); HD 232911 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459935.3134: recovered, depth 3737 ± 30 ppm (catalogue 6669 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1656.01: Gaia DR3 275228582433787904 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1656.01: dwarf priors not applied — RUWE 3.0448787 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1656.01: 44 Gaia neighbour(s) within 52.5", contamination 1.34%; depth 3737 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 275228518018748288, 46.6", ΔG 5.44); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1656.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-1656.01: HD 232911 otype SB* (multiple) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1656-01.yaml
python -m cygnus.multi report campaigns/toi-1656-01.yaml
```
