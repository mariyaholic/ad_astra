<!-- cygnus:generated-draft -->
# Known-object test, TOI-1149.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1149-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #747, calibrate_screen #740, event_census #744, fetch_products #739, known_signal_recovery #741, moving_objects #746, period_aliases #745, prior_art #749, residual_screen #743, stellar_context #742, variability_guard #748
- Runner finished (UTC): 2026-09-26T10:17:40Z

## Bottom line

Positive control **failed**: BJD 2459770.3308: not recovered, depth 12056 ± 613 ppm (catalogue 5083 ppm).
Outside the catalogued epoch the screen left 110 threshold entries forming **55 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1149.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 117789567 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 300.774016 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 26.892025 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459770.330784 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5082.9417064 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.3817612 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 7.9172 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2022-10-17 12:03:06 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | lightcurve | 54 | True | `a6e53e2a0de13676` | True |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | lightcurve | 41 | False | `b6acc9537ce7e615` | True |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | lightcurve | 55 | False | `defd21e2334e82d7` | True |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | lightcurve | 81 | False | `36d304575c8c84a5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459770.33078 | not_recovered | 71 | 12056 ± 613 | 5083 | — |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | — | epoch not in this light curve | — | — | 5083 | — |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | — | epoch not in this light curve | — | — | 5083 | — |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | — | epoch not in this light curve | — | — | 5083 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459786.57201 | -0.02662 | 150 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459781.93585 | -0.01916 | 44 | PDCSAP+SAP | 1, 3 | yes |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460517.42610 | -0.01846 | 25 | PDCSAP+SAP | 1, 3 | yes |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.13643 | -0.01936 | 3 | PDCSAP+SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.16213 | -0.01934 | 2 | PDCSAP+SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.21838 | -0.01932 | 3 | PDCSAP+SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.24685 | -0.01927 | 2 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.22324 | -0.01925 | 2 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.19199 | -0.01918 | 11 | PDCSAP+SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.14199 | -0.01912 | 3 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.20796 | -0.01912 | 10 | PDCSAP+SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.22879 | -0.01909 | 4 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.26005 | -0.01903 | 3 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.17046 | -0.01899 | 8 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.26491 | -0.01890 | 2 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.15240 | -0.01889 | 10 | PDCSAP+SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.26907 | -0.01884 | 2 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.24129 | -0.01869 | 4 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.27949 | -0.01865 | 3 | PDCSAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.05518 | -0.01849 | 2 | SAP | 3 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459776.06629 | -0.01827 | 2 | SAP | 3 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460524.38725 | -0.01622 | 49 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459821.37649 | -0.01565 | 43 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459812.09548 | -0.01513 | 43 | PDCSAP+SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460510.46213 | -0.01467 | 35 | PDCSAP+SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460529.02474 | -0.01466 | 33 | PDCSAP+SAP | 1 | no |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 2459438.54713 | -0.01454 | 30 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459819.05433 | -0.01452 | 29 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459816.73703 | -0.01432 | 24 | PDCSAP+SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460522.06781 | -0.01427 | 23 | PDCSAP+SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460512.79203 | -0.01410 | 2 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459802.81644 | -0.01408 | 31 | PDCSAP+SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460531.34417 | -0.01381 | 11 | PDCSAP+SAP | 1 | no |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 2459440.87765 | -0.01377 | 16 | PDCSAP+SAP | 1 | no |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 2459440.86307 | -0.01377 | 3 | PDCSAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460531.35875 | -0.01373 | 8 | PDCSAP+SAP | 1 | no |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 2459438.52005 | -0.01368 | 7 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459819.03003 | -0.01347 | 3 | PDCSAP+SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459795.85399 | -0.01343 | 36 | PDCSAP+SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460524.42545 | -0.01343 | 2 | PDCSAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460522.08864 | -0.01340 | 3 | PDCSAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460510.48922 | -0.01330 | 2 | PDCSAP+SAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459816.71690 | -0.01325 | 3 | SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460512.78092 | -0.01322 | 5 | PDCSAP+SAP | 1 | no |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 2459440.85543 | -0.01307 | 2 | PDCSAP | 1 | no |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 2459813.31629 | -0.01287 | 2 | SAP | 1 | no |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 2460529.05043 | -0.01281 | 2 | SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459772.65164 | -0.01221 | 28 | PDCSAP+SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459793.53385 | -0.01212 | 23 | PDCSAP+SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459795.82483 | -0.01205 | 4 | PDCSAP+SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459786.67965 | -0.01181 | 3 | PDCSAP+SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459795.88177 | -0.01158 | 2 | SAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459786.46437 | -0.01152 | 3 | PDCSAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459786.45534 | -0.01152 | 2 | PDCSAP | 1 | no |
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 2459793.51371 | -0.01150 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1149.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:17:37Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:17:38Z: TOI-1149.01 (TIC 117789567, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:17:39Z: HIP 98726 (type VAR, P 0.88632 d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:17:40Z: TOI-1149.01 (Pl?); HD 190257 (Pu*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459770.3308: not recovered, depth 12056 ± 613 ppm (catalogue 5083 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1149.01: Gaia DR3 1835201042675810688 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1149.01: dwarf priors not applied — 1.90 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1149.01: 209 Gaia neighbour(s) within 52.5", contamination 1.14%; depth 5083 ppm (catalogue depth); none bright enough to produce it alone; 1 neighbour(s) without G not assessed |
| Pointing and quality census per event | failed | 3 persistent event(s), 2 clean; BJD 2459781.9358 suspect: SAP_BKG z=-10.2 |
| Moving objects at screen-event epochs | inconclusive | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1149.01: HIP 98726                      VAR                            P=0.88632 at 0.1" |
| Object-class guard (SIMBAD) | passed | TOI-1149.01: TOI-1149.01 otype Pl? (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1149-01.yaml
python -m cygnus.multi report campaigns/toi-1149-01.yaml
```
