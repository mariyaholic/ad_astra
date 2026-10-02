<!-- cygnus:generated-draft -->
# Known-object test, TOI-3787.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3787-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4352, calibrate_screen #4335, event_census #4340, fetch_independent #4343, fetch_products #4328, known_signal_recovery #4336, moving_objects #4342, period_aliases #4341, prior_art #4356, residual_screen #4339, stellar_context #4337, variability_guard #4353
- Runner finished (UTC): 2026-09-30T21:49:14Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3787.01 (BJD 2459580.2535: gap (catalogue 15809 ppm); BJD 2459585.0698: not recovered, depth 13357 ± 726 ppm (catalogue 15809 ppm); BJD 2459589.8861: recovered, depth 13538 ± 755 ppm (catalogue 15809 ppm); BJD 2459594.7024: gap (catalogue 15809 ppm); BJD 2459599.5187: not recovered, depth 13468 ± 757 ppm (catalogue 15809 ppm); BJD 2459604.3350: recovered, depth 12269 ± 757 ppm (catalogue 15809 ppm); BJD 2459941.4772: recovered, depth 11229 ± 722 ppm (catalogue 15809 ppm); BJD 2459946.2935: recovered, depth 12133 ± 705 ppm (catalogue 15809 ppm); BJD 2459951.1098: gap (catalogue 15809 ppm); BJD 2459955.9261: recovered, depth 9940 ± 710 ppm (catalogue 15809 ppm); BJD 2459960.7424: recovered, depth 14240 ± 693 ppm (catalogue 15809 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3787.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 457104362 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 133.072602 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 61.972124 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459604.335042 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.8163162 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15809.0676843 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.5830779 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.398 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-08 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | lightcurve | 47 | True | `f3810260af5ad93b` | True |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | lightcurve | 60 | False | `07b6bb5031182db8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 2459580.25346 | gap | 0 | — | 15809 | — |
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 2459585.06978 | not_recovered | 108 | 13357 ± 726 | 15809 | — |
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 2459589.88609 | recovered | 108 | 13538 ± 755 | 15809 | -0.40 |
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 2459594.70241 | gap | 0 | — | 15809 | — |
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 2459599.51873 | not_recovered | 107 | 13468 ± 757 | 15809 | — |
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 2459604.33504 | recovered | 108 | 12269 ± 757 | 15809 | 0.09 |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 2459941.47718 | recovered | 108 | 11229 ± 722 | 15809 | 0.64 |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 2459946.29349 | recovered | 107 | 12133 ± 705 | 15809 | 0.25 |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 2459951.10981 | gap | 0 | — | 15809 | — |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 2459955.92612 | recovered | 108 | 9940 ± 710 | 15809 | -0.41 |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 2459960.74244 | recovered | 107 | 14240 ± 693 | 15809 | 0.88 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000457104362-0218-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2022357055054-s0060-0000000457104362-0249-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-3787.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:49:06Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:49:08Z: TOI-3787.01 (TIC 457104362, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:49:11Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:49:12Z: TOI-3787 (*); TOI-3787.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459580.2535: gap (catalogue 15809 ppm); BJD 2459585.0698: not recovered, depth 13357 ± 726 ppm (catalogue 15809 ppm); BJD 2459589.8861: recovered, depth 13538 ± 755 ppm (catalogue 15809 ppm); BJD 2459594.7024: gap (catalogue 15809 ppm); BJD 2459599.5187: not recovered, depth 13468 ± 757 ppm (catalogue 15809 ppm); BJD 2459604.3350: recovered, depth 12269 ± 757 ppm (catalogue 15809 ppm); BJD 2459941.4772: recovered, depth 11229 ± 722 ppm (catalogue 15809 ppm); BJD 2459946.2935: recovered, depth 12133 ± 705 ppm (catalogue 15809 ppm); BJD 2459951.1098: gap (catalogue 15809 ppm); BJD 2459955.9261: recovered, depth 9940 ± 710 ppm (catalogue 15809 ppm); BJD 2459960.7424: recovered, depth 14240 ± 693 ppm (catalogue 15809 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3787.01: Gaia DR3 1042956705309349760 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3787.01: Teff 5111 K, R* 0.93 ± 0.07, M* 0.95 ± 0.10, ρ* 1.18 ± 0.31 ρ☉ (dwarf sequence, M_G 4.99, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-3787.01: 1 Gaia neighbour(s) within 52.5", contamination 0.17%; depth 13538 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3787.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3787.01: TOI-3787 otype * (star_or_other) at 0.3" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3787-01.yaml
python -m cygnus.multi report campaigns/toi-3787-01.yaml
```
