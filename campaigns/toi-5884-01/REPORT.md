<!-- cygnus:generated-draft -->
# Known-object test, TOI-5884.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5884-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4915, calibrate_screen #4906, event_census #4910, fetch_independent #4913, fetch_products #4900, known_signal_recovery #4907, moving_objects #4912, period_aliases #4911, prior_art #4918, residual_screen #4909, stellar_context #4908, variability_guard #4916
- Runner finished (UTC): 2026-09-30T22:39:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5884.01 (BJD 2460533.6915: recovered, depth 2185 ± 146 ppm (catalogue 4240 ppm); BJD 2460539.5226: recovered, depth 3421 ± 153 ppm (catalogue 4240 ppm); BJD 2460545.3537: recovered, depth 3895 ± 147 ppm (catalogue 4240 ppm); BJD 2460551.1848: recovered, depth 3769 ± 138 ppm (catalogue 4240 ppm); BJD 2460557.0159: recovered, depth 3621 ± 137 ppm (catalogue 4240 ppm)).
Outside the catalogued epoch the screen left 27 threshold entries forming **16 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5884.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 13574009 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 320.450532 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 23.926451 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459822.29685 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.8311038 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 4240.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.283 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.5002 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | lightcurve | 82 | False | `6cd32cd53df73ace` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460533.69151 | recovered | 98 | 2185 ± 146 | 4240 | -0.02 |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460539.52262 | recovered | 80 | 3421 ± 153 | 4240 | 0.33 |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.35372 | recovered | 98 | 3895 ± 147 | 4240 | -0.03 |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460551.18482 | recovered | 99 | 3769 ± 138 | 4240 | -0.23 |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460557.01593 | recovered | 98 | 3621 ± 137 | 4240 | -0.13 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.12323 | -0.00565 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.03990 | -0.00532 | 4 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.00309 | -0.00504 | 3 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.07323 | -0.00479 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460544.97879 | -0.00477 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.13990 | -0.00475 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.06698 | -0.00464 | 5 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460539.16487 | -0.00459 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460544.96767 | -0.00444 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.10101 | -0.00439 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460544.95240 | -0.00418 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460538.59680 | -0.00417 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460545.04754 | -0.00417 | 5 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460544.90934 | -0.00416 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460538.52944 | -0.00395 | 3 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000013574009-0278-s_lc.fits` | 2460538.40027 | -0.00383 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5884.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:38:59Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:39:05Z: TOI-5884.01 (TIC 13574009, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:39:10Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:39:18Z: TYC 2187-45-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460533.6915: recovered, depth 2185 ± 146 ppm (catalogue 4240 ppm); BJD 2460539.5226: recovered, depth 3421 ± 153 ppm (catalogue 4240 ppm); BJD 2460545.3537: recovered, depth 3895 ± 147 ppm (catalogue 4240 ppm); BJD 2460551.1848: recovered, depth 3769 ± 138 ppm (catalogue 4240 ppm); BJD 2460557.0159: recovered, depth 3621 ± 137 ppm (catalogue 4240 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 40% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5884.01: Gaia DR3 1792372835687091456 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-5884.01: dwarf priors not applied — 1.50 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5884.01: 17 Gaia neighbour(s) within 52.5", contamination 5.99%; depth 2185 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 1792373041844457856, 42.8", ΔG 3.87); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5884.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5884.01: TYC 2187-45-1 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5884-01.yaml
python -m cygnus.multi report campaigns/toi-5884-01.yaml
```
