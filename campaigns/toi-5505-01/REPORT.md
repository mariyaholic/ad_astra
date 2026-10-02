<!-- cygnus:generated-draft -->
# Known-object test, TOI-5505.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5505-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4892, calibrate_screen #4869, event_census #4875, fetch_independent #4886, fetch_products #4865, known_signal_recovery #4870, moving_objects #4877, period_aliases #4876, prior_art #4899, residual_screen #4873, stellar_context #4871, variability_guard #4894
- Runner finished (UTC): 2026-09-30T22:35:55Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5505.01 (BJD 2460262.4682: gap (catalogue 15290 ppm); BJD 2460273.5746: gap (catalogue 15290 ppm); BJD 2460284.6811: recovered, depth 3632 ± 789 ppm (catalogue 15290 ppm)).
Outside the catalogued epoch the screen left 71 threshold entries forming **17 distinct event(s)**, **13 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460263.1923 matches the catalogued transit's depth (6607 vs 3632 ppm), 21.535 d later; 3 of 21 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5505.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 374350678 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 160.866036 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 3.9587 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459573.870053 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 11.1064221 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15290.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.12 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8078 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | lightcurve | 72 | False | `6a819c9326c8445f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460262.46822 | gap | 0 | — | 15290 | — |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460273.57465 | gap | 0 | — | 15290 | — |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460284.68107 | recovered | 63 | 3632 ± 789 | 15290 | 1.12 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460262.93607 | -0.02478 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.06247 | -0.02262 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.08261 | -0.02245 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.01871 | -0.02234 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.00205 | -0.02178 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460276.04915 | -0.02138 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460262.96732 | -0.02066 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460276.07137 | -0.01917 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460267.08994 | -0.01905 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.19234 | -0.01898 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.26596 | -0.01865 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460262.97982 | -0.01855 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460262.95482 | -0.01840 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.09928 | -0.02064 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.06733 | -0.01962 | 2 | PDCSAP | 3 | no |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460272.88079 | -0.01910 | 2 | SAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000374350678-0267-s_lc.fits` | 2460263.02288 | -0.01737 | 2 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460263.19234 | 6607 | 3632 | 21.5355 | 3 / 21 | 21.5355, 10.7677, 5.3839 |
| 2460263.26596 | 4363 | 3632 | 21.4618 | 2 / 21 | 21.4618, 10.7309 |
| 2460267.08994 | 1960 | 3632 | 17.6379 | 2 / 17 | 17.6379, 8.8189 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-5505.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:35:26Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:35:35Z: TOI-5505.01 (TIC 374350678, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:35:45Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:35:49Z: UCAC4 470-044472 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460262.4682: gap (catalogue 15290 ppm); BJD 2460273.5746: gap (catalogue 15290 ppm); BJD 2460284.6811: recovered, depth 3632 ± 789 ppm (catalogue 15290 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460263.1923, ΔT = 21.535 d, 3 of 21 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (21.5355, 10.7677, 5.3839 d); duration likelihood under Gaia priors (circular orbits) peaks at 5.38 d (weight 0.62) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5505.01: Gaia DR3 3857604423992185600 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5505.01: Teff 5110 K, R* 0.79 ± 0.06, M* 0.83 ± 0.08, ρ* 1.71 ± 0.44 ρ☉ (dwarf sequence, M_G 5.77, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5505.01: 3 Gaia neighbour(s) within 52.5", contamination 29.07%; depth 3632 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 3857604385337525376, 23.5", ΔG 1.00); a centroid test is needed |
| Pointing and quality census per event | failed | 13 persistent event(s), 1 clean; BJD 2460262.9361 suspect: scattered light 2 (in event), POS_CORR2 z=-5.0, SAP_BKG z=+12.1; BJD 2460262.9548 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-5.4, SAP_BKG z=+15.7; BJD 2460262.9673 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-6.0, SAP_BKG z=+16.0; BJD 2460262.9798 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-6.0, SAP_BKG z=+16.6 |
| Moving objects at screen-event epochs | inconclusive | 13 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 12 light curve × candidate pair(s); aliases supported: none; excluded: none; 26 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-5505.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5505.01: UCAC4 470-044472 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 2 possible published-ephemeris overlap(s) within 1 d (TOI-5505.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5505-01.yaml
python -m cygnus.multi report campaigns/toi-5505-01.yaml
```
