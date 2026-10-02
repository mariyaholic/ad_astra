<!-- cygnus:generated-draft -->
# Known-object test, TOI-3315.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3315-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4395, calibrate_screen #4380, event_census #4386, fetch_independent #4390, fetch_products #4378, known_signal_recovery #4381, moving_objects #4389, period_aliases #4388, prior_art #4398, residual_screen #4384, stellar_context #4382, variability_guard #4397
- Runner finished (UTC): 2026-09-30T21:51:12Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3315.01 (BJD 2460097.9159: recovered, depth 5688 ± 260 ppm (catalogue 6900 ppm); BJD 2460103.1490: not recovered, depth 6026 ± 253 ppm (catalogue 6900 ppm); BJD 2460108.3821: gap (catalogue 6900 ppm); BJD 2460113.6151: partial, depth 6966 ± 260 ppm (catalogue 6900 ppm); BJD 2460118.8482: recovered, depth 6932 ± 281 ppm (catalogue 6900 ppm); BJD 2460124.0813: gap (catalogue 6900 ppm); BJD 2460830.5471: not recovered, depth -0 ± 421 ppm (catalogue 6900 ppm); BJD 2460835.7802: recovered, depth 6329 ± 266 ppm (catalogue 6900 ppm); BJD 2460841.0133: not recovered, depth 3034 ± 305 ppm (catalogue 6900 ppm); BJD 2460846.2464: not recovered, depth 6671 ± 260 ppm (catalogue 6900 ppm); BJD 2460851.4795: not recovered, depth 6569 ± 274 ppm (catalogue 6900 ppm); BJD 2461076.5019: recovered, depth 6676 ± 270 ppm (catalogue 6900 ppm); BJD 2461081.7350: recovered, depth 7035 ± 248 ppm (catalogue 6900 ppm); BJD 2461086.9681: gap (catalogue 6900 ppm); BJD 2461092.2012: recovered, depth 7334 ± 268 ppm (catalogue 6900 ppm); BJD 2461097.4342: partial, depth 7350 ± 305 ppm (catalogue 6900 ppm); BJD 2461128.8327: recovered, depth 6700 ± 275 ppm (catalogue 6900 ppm); BJD 2461134.0658: recovered, depth 6545 ± 251 ppm (catalogue 6900 ppm); BJD 2461139.2989: gap (catalogue 6900 ppm); BJD 2461144.5320: recovered, depth 7442 ± 277 ppm (catalogue 6900 ppm); BJD 2461149.7650: recovered, depth 7135 ± 294 ppm (catalogue 6900 ppm); BJD 2461154.9981: recovered, depth 7227 ± 265 ppm (catalogue 6900 ppm); BJD 2461160.2312: recovered, depth 6280 ± 273 ppm (catalogue 6900 ppm); BJD 2461165.4643: gap (catalogue 6900 ppm); BJD 2461170.6974: recovered, depth 6497 ± 303 ppm (catalogue 6900 ppm); BJD 2461175.9304: recovered, depth 7286 ± 271 ppm (catalogue 6900 ppm)).
Outside the catalogued epoch the screen left 3 threshold entries forming **3 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3315.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 312030014 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 264.934249 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -73.37763 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459386.216984 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.2330803 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6900.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.617 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.8748 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | lightcurve | 66 | False | `f4ce481fac01a258` | True |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | lightcurve | 93 | False | `f4d808508791c208` | True |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | lightcurve | 100 | False | `743c7062f030d1c0` | True |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | lightcurve | 102 | False | `b5d600e4a06240bc` | True |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | lightcurve | 103 | False | `7efb990b2d642eeb` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 2460097.91590 | recovered | 138 | 5688 ± 260 | 6900 | -0.83 |
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 2460103.14899 | not_recovered | 139 | 6026 ± 253 | 6900 | — |
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 2460108.38207 | gap | 0 | — | 6900 | — |
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 2460113.61515 | partial | 139 | 6966 ± 260 | 6900 | 1.12 |
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 2460118.84823 | recovered | 133 | 6932 ± 281 | 6900 | -0.24 |
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 2460124.08131 | gap | 0 | — | 6900 | — |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 2460830.54715 | not_recovered | 47 | -0 ± 421 | 6900 | — |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 2460835.78023 | recovered | 138 | 6329 ± 266 | 6900 | 0.87 |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 2460841.01331 | not_recovered | 139 | 3034 ± 305 | 6900 | — |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 2460846.24639 | not_recovered | 139 | 6671 ± 260 | 6900 | — |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 2460851.47947 | not_recovered | 138 | 6569 ± 274 | 6900 | — |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 2461076.50192 | recovered | 138 | 6676 ± 270 | 6900 | -1.76 |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 2461081.73500 | recovered | 139 | 7035 ± 248 | 6900 | -0.50 |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 2461086.96808 | gap | 0 | — | 6900 | — |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 2461092.20116 | recovered | 138 | 7334 ± 268 | 6900 | -0.33 |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 2461097.43424 | partial | 139 | 7350 ± 305 | 6900 | -0.28 |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2461128.83272 | recovered | 138 | 6700 ± 275 | 6900 | 0.54 |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2461134.06580 | recovered | 139 | 6545 ± 251 | 6900 | -1.22 |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2461139.29888 | gap | 0 | — | 6900 | — |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2461144.53196 | recovered | 139 | 7442 ± 277 | 6900 | -0.17 |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2461149.76505 | recovered | 139 | 7135 ± 294 | 6900 | 0.34 |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461154.99813 | recovered | 138 | 7227 ± 265 | 6900 | 0.30 |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461160.23121 | recovered | 139 | 6280 ± 273 | 6900 | -0.95 |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461165.46429 | gap | 0 | — | 6900 | — |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461170.69737 | recovered | 129 | 6497 ± 303 | 6900 | 0.43 |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461175.93045 | recovered | 139 | 7286 ± 271 | 6900 | 0.12 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023153011303-s0066-0000000312030014-0260-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025154050500-s0093-0000000312030014-0290-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026033082000-s0100-0000000312030014-0302-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461171.18379 | -0.01005 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000312030014-0304-s_lc.fits` | 2461138.38626 | -0.00880 | 2 | PDCSAP | 1 | no |
| `tess2026111101500-s0103-0000000312030014-0305-s_lc.fits` | 2461171.21573 | -0.00868 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3315.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:51:00Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:51:02Z: TOI-3315.01 (TIC 312030014, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:51:05Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:51:08Z: TOI-3315.01 (Pl?); TOI-3315 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460097.9159: recovered, depth 5688 ± 260 ppm (catalogue 6900 ppm); BJD 2460103.1490: not recovered, depth 6026 ± 253 ppm (catalogue 6900 ppm); BJD 2460108.3821: gap (catalogue 6900 ppm); BJD 2460113.6151: partial, depth 6966 ± 260 ppm (catalogue 6900 ppm); BJD 2460118.8482: recovered, depth 6932 ± 281 ppm (catalogue 6900 ppm); BJD 2460124.0813: gap (catalogue 6900 ppm); BJD 2460830.5471: not recovered, depth -0 ± 421 ppm (catalogue 6900 ppm); BJD 2460835.7802: recovered, depth 6329 ± 266 ppm (catalogue 6900 ppm); BJD 2460841.0133: not recovered, depth 3034 ± 305 ppm (catalogue 6900 ppm); BJD 2460846.2464: not recovered, depth 6671 ± 260 ppm (catalogue 6900 ppm); BJD 2460851.4795: not recovered, depth 6569 ± 274 ppm (catalogue 6900 ppm); BJD 2461076.5019: recovered, depth 6676 ± 270 ppm (catalogue 6900 ppm); BJD 2461081.7350: recovered, depth 7035 ± 248 ppm (catalogue 6900 ppm); BJD 2461086.9681: gap (catalogue 6900 ppm); BJD 2461092.2012: recovered, depth 7334 ± 268 ppm (catalogue 6900 ppm); BJD 2461097.4342: partial, depth 7350 ± 305 ppm (catalogue 6900 ppm); BJD 2461128.8327: recovered, depth 6700 ± 275 ppm (catalogue 6900 ppm); BJD 2461134.0658: recovered, depth 6545 ± 251 ppm (catalogue 6900 ppm); BJD 2461139.2989: gap (catalogue 6900 ppm); BJD 2461144.5320: recovered, depth 7442 ± 277 ppm (catalogue 6900 ppm); BJD 2461149.7650: recovered, depth 7135 ± 294 ppm (catalogue 6900 ppm); BJD 2461154.9981: recovered, depth 7227 ± 265 ppm (catalogue 6900 ppm); BJD 2461160.2312: recovered, depth 6280 ± 273 ppm (catalogue 6900 ppm); BJD 2461165.4643: gap (catalogue 6900 ppm); BJD 2461170.6974: recovered, depth 6497 ± 303 ppm (catalogue 6900 ppm); BJD 2461175.9304: recovered, depth 7286 ± 271 ppm (catalogue 6900 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3.5, 3.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3315.01: Gaia DR3 5803338992653301120 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3315.01: Teff 6188 K, R* 1.41 ± 0.11, M* 1.29 ± 0.13, ρ* 0.46 ± 0.12 ρ☉ (dwarf sequence, M_G 3.42, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3315.01: 26 Gaia neighbour(s) within 52.5", contamination 20.19%; depth 5688 ppm (measured depth of the recovered catalogued transit); 7 could produce it if fully eclipsed (brightest 5803339022716373120, 48.7", ΔG 2.65); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3315.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3315.01: TOI-3315 otype * (star_or_other) at 0.3" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3315-01.yaml
python -m cygnus.multi report campaigns/toi-3315-01.yaml
```
