<!-- cygnus:generated-draft -->
# Known-object test, TOI-1379.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1379-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #277, calibrate_screen #256, event_census #264, fetch_products #254, known_signal_recovery #259, moving_objects #266, period_aliases #265, prior_art #279, residual_screen #262, stellar_context #260, variability_guard #278
- Runner finished (UTC): 2026-09-26T09:59:33Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1379.01 (BJD 2459871.4386: recovered, depth 13032 ± 140 ppm (catalogue 18121 ppm)).
Outside the catalogued epoch the screen left 56 threshold entries forming **11 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1379.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 252490659 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 344.35978 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 53.140835 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459871.438619 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 18121.2 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.119 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.3842 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-01-30 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000252490659-0245-s_lc.fits` | lightcurve | 57 | True | `963ad842715c744a` | True |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | lightcurve | 77 | False | `d9bff85b7a528230` | True |
| `tess2024274222008-s0084-0000000252490659-0281-s_lc.fits` | lightcurve | 84 | False | `d1198003b9b7827f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000252490659-0245-s_lc.fits` | 2459871.43862 | recovered | 123 | 13032 ± 140 | 18121 | 0.02 |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | — | epoch not in this light curve | — | — | 18121 | — |
| `tess2024274222008-s0084-0000000252490659-0281-s_lc.fits` | — | epoch not in this light curve | — | — | 18121 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022273165103-s0057-0000000252490659-0245-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024274222008-s0084-0000000252490659-0281-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460397.97329 | -0.00881 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460398.00523 | -0.00823 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460398.01218 | -0.00742 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460398.01912 | -0.00705 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460397.92537 | -0.00653 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460397.93926 | -0.00635 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460398.02815 | -0.00553 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000252490659-0281-s_lc.fits` | 2460584.59839 | -0.00386 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460395.52054 | -0.00703 | 3 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000252490659-0272-s_lc.fits` | 2460395.50457 | -0.00559 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000252490659-0281-s_lc.fits` | 2460590.58452 | -0.00406 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1379.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:59:29Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:59:30Z: TOI-1379.01 (TIC 252490659, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:59:32Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:59:32Z: TOI-1379 (*); TOI-1379.01 (err)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459871.4386: recovered, depth 13032 ± 140 ppm (catalogue 18121 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1379.01: Gaia DR3 1990461640828054400 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1379.01: dwarf priors not applied — 1.18 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1379.01: 47 Gaia neighbour(s) within 52.5", contamination 8.51%; depth 13032 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 1990461606468319488, 29.4", ΔG 4.31); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 7 clean; BJD 2460584.5984 suspect: earth point (in event), manual exclude (in event), momentum dump (in event), MOM_CENTR1 z=+10.2, MOM_CENTR2 z=-42.5, POS_CORR1 z=+6.9, POS_CORR2 z=-43.7 |
| Moving objects at screen-event epochs | passed | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1379.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1379.01: TOI-1379 otype * (star_or_other) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1379-01.yaml
python -m cygnus.multi report campaigns/toi-1379-01.yaml
```
