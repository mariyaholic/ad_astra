<!-- cygnus:generated-draft -->
# Known-object test, TOI-7610.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-7610-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #911, calibrate_screen #884, event_census #892, fetch_products #883, known_signal_recovery #887, moving_objects #900, period_aliases #893, prior_art #913, residual_screen #890, stellar_context #888, variability_guard #912
- Runner finished (UTC): 2026-09-26T10:22:46Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-7610.01 (BJD 2460700.9708: recovered, depth 17261 ± 290 ppm (catalogue 20134 ppm)).
Outside the catalogued epoch the screen left 39 threshold entries forming **9 distinct event(s)**, **6 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461066.2847 matches the catalogued transit's depth (10431 vs 17261 ppm), 365.313 d later; 21 of 365 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7610.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 121341000 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 129.250045 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -3.530909 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460700.970803 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 20133.8745178 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.7045956 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.7985 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-11-21 12:03:40 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | lightcurve | 88 | True | `e6a87fa9c798599b` | True |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | lightcurve | 99 | False | `d5d4d0f7552f7ad8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | 2460700.97080 | recovered | 141 | 17261 ± 290 | 20134 | 0.02 |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 20134 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.35066 | -0.01740 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.30968 | -0.01713 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.38816 | -0.01640 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.41663 | -0.01254 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.40830 | -0.01209 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.28468 | -0.01188 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 2461066.27913 | -0.01070 | 2 | SAP | 1, 2 | no |
| `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | 2460710.59324 | -0.01065 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | 2460709.85296 | -0.00959 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461066.28468 | 10431 | 17261 | 365.3130 | 21 / 365 | 365.313, 182.656, 121.771, 91.3283, 73.0626, 60.8855, 52.1876, 45.6641, 40.5903, 36.5313, 33.2103, 30.4428, 28.101, 26.0938, 24.3542, 22.8321, 21.489, 20.2952, 19.227, 18.2657 |
| 2461066.30968 | 14270 | 17261 | 365.3380 | 21 / 365 | 365.338, 182.669, 121.779, 91.3345, 73.0676, 60.8897, 52.1911, 45.6673, 40.5931, 36.5338, 33.2125, 30.4448, 28.1029, 26.0956, 24.3559, 22.8336, 21.4905, 20.2966, 19.2283, 18.2669 |
| 2461066.35066 | 14332 | 17261 | 365.3790 | 21 / 365 | 365.379, 182.69, 121.793, 91.3447, 73.0758, 60.8965, 52.197, 45.6724, 40.5977, 36.5379, 33.2163, 30.4482, 28.1061, 26.0985, 24.3586, 22.8362, 21.4929, 20.2988, 19.2305, 18.2689 |
| 2461066.38816 | 14209 | 17261 | 365.4165 | 21 / 365 | 365.416, 182.708, 121.805, 91.3541, 73.0833, 60.9027, 52.2024, 45.6771, 40.6018, 36.5416, 33.2197, 30.4514, 28.109, 26.1012, 24.3611, 22.8385, 21.4951, 20.3009, 19.2324, 18.2708 |
| 2461066.40830 | 11478 | 17261 | 365.4366 | 21 / 365 | 365.437, 182.718, 121.812, 91.3592, 73.0873, 60.9061, 52.2052, 45.6796, 40.6041, 36.5437, 33.2215, 30.4531, 28.1105, 26.1026, 24.3624, 22.8398, 21.4963, 20.302, 19.2335, 18.2718 |
| 2461066.41663 | 8882 | 17261 | 365.4450 | 21 / 365 | 365.445, 182.722, 121.815, 91.3612, 73.089, 60.9075, 52.2064, 45.6806, 40.605, 36.5445, 33.2223, 30.4537, 28.1112, 26.1032, 24.363, 22.8403, 21.4968, 20.3025, 19.2339, 18.2722 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-7610.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:22:38Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:22:44Z: TOI-7610.01 (TIC 121341000, disposition PC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:22:45Z: Gaia DR3 3071787586789910144 (type ROT, P — d)
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:22:46Z: UCAC4 433-048726 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460700.9708: recovered, depth 17261 ± 290 ppm (catalogue 20134 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 6 repeat-candidate event(s); first at BJD 2461066.2847, ΔT = 365.313 d, 21 of 365 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (365.313, 182.656, 121.771, 91.3283, 73.0626, 60.8855, 52.1876, 45.6641, 40.5903, 36.5313, 33.2103, 30.4428 … d); duration likelihood under Gaia priors (circular orbits) peaks at 28.1 d (weight 0.07) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-7610.01: Gaia DR3 3071787586789910144 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-7610.01: Teff 4768 K, R* 0.72 ± 0.06, M* 0.74 ± 0.07, ρ* 1.96 ± 0.51 ρ☉ (dwarf sequence, M_G 6.45, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-7610.01: 7 Gaia neighbour(s) within 52.5", contamination 0.69%; depth 17261 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | passed | 6 persistent event(s), 6 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | inconclusive | 6 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-7610.01: Gaia DR3 3071787586789910144   ROT                            P=None at 0.2" |
| Object-class guard (SIMBAD) | inconclusive | TOI-7610.01: UCAC4 433-048726 otype SB* (multiple) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-7610-01.yaml
python -m cygnus.multi report campaigns/toi-7610-01.yaml
```
