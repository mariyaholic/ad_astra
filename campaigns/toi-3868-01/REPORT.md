<!-- cygnus:generated-draft -->
# Known-object test, TOI-3868.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3868-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4589, calibrate_screen #4575, event_census #4580, fetch_independent #4585, fetch_products #4570, known_signal_recovery #4576, moving_objects #4582, period_aliases #4581, prior_art #4592, residual_screen #4579, stellar_context #4578, variability_guard #4590
- Runner finished (UTC): 2026-09-30T22:03:03Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3868.01 (BJD 2459642.3366: gap (catalogue 9420 ppm); BJD 2459660.9024: recovered, depth 8684 ± 356 ppm (catalogue 9420 ppm); BJD 2459623.7708: gap (catalogue 9420 ppm); BJD 2460347.8375: recovered, depth 10001 ± 359 ppm (catalogue 9420 ppm); BJD 2460366.4033: recovered, depth 7854 ± 323 ppm (catalogue 9420 ppm); BJD 2460384.9691: recovered, depth 10964 ± 567 ppm (catalogue 9420 ppm)).
Outside the catalogued epoch the screen left 32 threshold entries forming **12 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460339.7909 matches the catalogued transit's depth (5981 vs 8684 ppm), 678.887 d later; 12 of 678 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3868.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 310994622 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 203.567211 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 65.128389 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459660.902382 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 18.565813 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 9420.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.82 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.3572 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-04-12 12:03:09 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022057073128-s0049-0000000310994622-0221-s_lc.fits` | lightcurve | 49 | True | `c48da33929ab35d8` | True |
| `tess2022027120115-s0048-0000000310994622-0219-s_lc.fits` | lightcurve | 48 | False | `63d3cdd36ca6491c` | True |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | lightcurve | 75 | False | `48e6d3ad1691a0a2` | True |
| `tess2024058030222-s0076-0000000310994622-0271-s_lc.fits` | lightcurve | 76 | False | `1dfef99bb5f2de88` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022057073128-s0049-0000000310994622-0221-s_lc.fits` | 2459642.33657 | gap | 0 | — | 9420 | — |
| `tess2022057073128-s0049-0000000310994622-0221-s_lc.fits` | 2459660.90238 | recovered | 114 | 8684 ± 356 | 9420 | 0.03 |
| `tess2022027120115-s0048-0000000310994622-0219-s_lc.fits` | 2459623.77076 | gap | 0 | — | 9420 | — |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460347.83746 | recovered | 115 | 10001 ± 359 | 9420 | -0.71 |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460366.40328 | recovered | 115 | 7854 ± 323 | 9420 | 0.21 |
| `tess2024058030222-s0076-0000000310994622-0271-s_lc.fits` | 2460384.96909 | recovered | 115 | 10964 ± 567 | 9420 | 1.06 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022057073128-s0049-0000000310994622-0221-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2022027120115-s0048-0000000310994622-0219-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024058030222-s0076-0000000310994622-0271-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460339.79091 | -0.01111 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460341.17148 | -0.01006 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.66182 | -0.01675 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.37431 | -0.01394 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.42779 | -0.01303 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.32292 | -0.01209 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.58404 | -0.01172 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.56737 | -0.01154 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.74654 | -0.01124 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.68960 | -0.01113 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460355.34524 | -0.01060 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000310994622-0270-s_lc.fits` | 2460345.34029 | -0.01056 | 3 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460339.79091 | 5981 | 8684 | 678.8873 | 12 / 678 | 678.887, 339.444, 226.296, 169.722, 135.778, 113.148, 96.9839, 84.8609, 75.4319, 67.8887, 61.717, 56.5739 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3868.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:02:50Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:02:53Z: TOI-3868.01 (TIC 310994622, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T22:02:57Z: Gaia DR3 1666196385974431104 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:03:00Z: TOI-3868.01 (Pl?); TOI-3868 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459642.3366: gap (catalogue 9420 ppm); BJD 2459660.9024: recovered, depth 8684 ± 356 ppm (catalogue 9420 ppm); BJD 2459623.7708: gap (catalogue 9420 ppm); BJD 2460347.8375: recovered, depth 10001 ± 359 ppm (catalogue 9420 ppm); BJD 2460366.4033: recovered, depth 7854 ± 323 ppm (catalogue 9420 ppm); BJD 2460384.9691: recovered, depth 10964 ± 567 ppm (catalogue 9420 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460339.7909, ΔT = 678.887 d, 12 of 678 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (678.887, 339.444, 226.296, 169.722, 135.778, 113.148, 96.9839, 84.8609, 75.4319, 67.8887, 61.717, 56.5739 d); duration likelihood under Gaia priors (circular orbits) peaks at 56.6 d (weight 0.16) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3868.01: Gaia DR3 1666196385974431104 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3868.01: Teff 4731 K, R* 0.74 ± 0.06, M* 0.76 ± 0.08, ρ* 1.88 ± 0.49 ρ☉ (dwarf sequence, M_G 6.32, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-3868.01: 0 Gaia neighbour(s) within 52.5", contamination 0.00%; depth 8684 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2460339.7909 suspect: earth point (in event), manual exclude (in event), momentum dump (in event), MOM_CENTR1 z=-8.3, MOM_CENTR2 z=+5.0, POS_CORR1 z=-9.8, POS_CORR2 z=+5.9; BJD 2460341.1715 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=-7.9, MOM_CENTR2 z=-6.0, POS_CORR1 z=-9.4, SAP_BKG z=+1447.5 |
| Moving objects at screen-event epochs | inconclusive | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 4 light curve × candidate pair(s); aliases supported: none; excluded: 96.9839; 47 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-3868.01: Gaia DR3 1666196385974431104   ROT                            P=None at 0.5" |
| Object-class guard (SIMBAD) | passed | TOI-3868.01: TOI-3868 otype * (star_or_other) at 0.7" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3868-01.yaml
python -m cygnus.multi report campaigns/toi-3868-01.yaml
```
