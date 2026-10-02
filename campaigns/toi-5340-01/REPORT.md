<!-- cygnus:generated-draft -->
# Known-object test, TOI-5340.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5340-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4103, calibrate_screen #4090, event_census #4094, fetch_independent #4097, fetch_products #4083, known_signal_recovery #4091, moving_objects #4096, period_aliases #4095, prior_art #4106, residual_screen #4093, stellar_context #4092, variability_guard #4104
- Runner finished (UTC): 2026-09-30T21:38:05Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5340.01 (BJD 2460236.1406: recovered, depth 5705 ± 234 ppm (catalogue 6420 ppm); BJD 2460241.0799: recovered, depth 5586 ± 235 ppm (catalogue 6420 ppm); BJD 2460246.0192: recovered, depth 4034 ± 233 ppm (catalogue 6420 ppm); BJD 2460250.9585: partial, depth 5352 ± 231 ppm (catalogue 6420 ppm); BJD 2460255.8978: recovered, depth 4772 ± 229 ppm (catalogue 6420 ppm)).
Outside the catalogued epoch the screen left 2 threshold entries forming **1 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5340.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 14156936 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 59.309482 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 22.378337 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459519.940368 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.9393117 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6420.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.696 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.7085 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | lightcurve | 71 | False | `e18d22325a64263f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 2460236.14056 | recovered | 141 | 5705 ± 234 | 6420 | 1.36 |
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 2460241.07988 | recovered | 141 | 5586 ± 235 | 6420 | 1.93 |
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 2460246.01919 | recovered | 141 | 4034 ± 233 | 6420 | 2.55 |
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 2460250.95850 | partial | 141 | 5352 ± 231 | 6420 | -0.25 |
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 2460255.89781 | recovered | 141 | 4772 ± 229 | 6420 | 0.04 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000014156936-0266-s_lc.fits` | 2460253.02870 | -0.01002 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5340.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:37:54Z: TOI-5340 b (host TOI-5340)
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:37:57Z: TOI-5340.01 (TIC 14156936, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:38:01Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:38:03Z: TOI-5340.01 (Pl); UCAC4 562-008479 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460236.1406: recovered, depth 5705 ± 234 ppm (catalogue 6420 ppm); BJD 2460241.0799: recovered, depth 5586 ± 235 ppm (catalogue 6420 ppm); BJD 2460246.0192: recovered, depth 4034 ± 233 ppm (catalogue 6420 ppm); BJD 2460250.9585: partial, depth 5352 ± 231 ppm (catalogue 6420 ppm); BJD 2460255.8978: recovered, depth 4772 ± 229 ppm (catalogue 6420 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5340.01: Gaia DR3 65315118156520320 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-5340.01: dwarf priors not applied — 1.75 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-5340.01: 5 Gaia neighbour(s) within 52.5", contamination 0.78%; depth 5705 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5340.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5340.01: TOI-5340.01 otype Pl (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5340-01.yaml
python -m cygnus.multi report campaigns/toi-5340-01.yaml
```
