<!-- cygnus:generated-draft -->
# Known-object test, TOI-2558.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2558-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4673, calibrate_screen #4650, event_census #4662, fetch_independent #4668, fetch_products #4639, known_signal_recovery #4658, moving_objects #4664, period_aliases #4663, prior_art #4675, residual_screen #4661, stellar_context #4660, variability_guard #4674
- Runner finished (UTC): 2026-09-30T22:09:56Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2558.01 (BJD 2459233.1276: recovered, depth 4881 ± 271 ppm (catalogue 6536 ppm); BJD 2459250.9135: recovered, depth 5443 ± 258 ppm (catalogue 6536 ppm); BJD 2459268.6994: gap (catalogue 6536 ppm); BJD 2459980.1360: recovered, depth 4846 ± 257 ppm (catalogue 6536 ppm); BJD 2460691.5727: gap (catalogue 6536 ppm); BJD 2460709.3586: not recovered, depth 5030 ± 258 ppm (catalogue 6536 ppm)).
Outside the catalogued epoch the screen left 40 threshold entries forming **16 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2558.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 283307274 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 128.24579 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -25.256245 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459233.127609 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 17.7859152 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6535.8664276 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.2520718 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6919 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-07-09 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | lightcurve | 34 | True | `3dd190681e465e1f` | True |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | lightcurve | 35 | False | `a1bcee952282de24` | True |
| `tess2023018032328-s0061-0000000283307274-0250-s_lc.fits` | lightcurve | 61 | False | `70256042b299a079` | True |
| `tess2025014115807-s0088-0000000283307274-0285-s_lc.fits` | lightcurve | 88 | False | `48f5fa9f61507a9a` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459233.12761 | recovered | 128 | 4881 ± 271 | 6536 | 0.71 |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459250.91352 | recovered | 127 | 5443 ± 258 | 6536 | -0.35 |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459268.69944 | gap | 0 | — | 6536 | — |
| `tess2023018032328-s0061-0000000283307274-0250-s_lc.fits` | 2459980.13605 | recovered | 128 | 4846 ± 257 | 6536 | -0.23 |
| `tess2025014115807-s0088-0000000283307274-0285-s_lc.fits` | 2460691.57266 | gap | 0 | — | 6536 | — |
| `tess2025014115807-s0088-0000000283307274-0285-s_lc.fits` | 2460709.35857 | not_recovered | 128 | 5030 ± 258 | 6536 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023018032328-s0061-0000000283307274-0250-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025014115807-s0088-0000000283307274-0285-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459278.44157 | -0.01020 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459279.75263 | -0.00869 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459247.38915 | -0.00982 | 2 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000283307274-0285-s_lc.fits` | 2460711.62133 | -0.00955 | 2 | SAP | 2 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459247.44887 | -0.00948 | 2 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459247.53776 | -0.00897 | 2 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459265.99186 | -0.00893 | 2 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459279.65541 | -0.00843 | 2 | PDCSAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459273.86948 | -0.00839 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000283307274-0205-s_lc.fits` | 2459265.92936 | -0.00828 | 2 | SAP | 2 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459252.64473 | -0.00825 | 2 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000283307274-0250-s_lc.fits` | 2459980.97910 | -0.00784 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459246.08497 | -0.00761 | 2 | PDCSAP | 1, 2 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459252.55167 | -0.00756 | 2 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459253.57250 | -0.00749 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000283307274-0204-s_lc.fits` | 2459240.80156 | -0.00739 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2558.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:09:44Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:09:47Z: TOI-2558.01 (TIC 283307274, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:09:49Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:09:52Z: UCAC4 324-049925 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459233.1276: recovered, depth 4881 ± 271 ppm (catalogue 6536 ppm); BJD 2459250.9135: recovered, depth 5443 ± 258 ppm (catalogue 6536 ppm); BJD 2459268.6994: gap (catalogue 6536 ppm); BJD 2459980.1360: recovered, depth 4846 ± 257 ppm (catalogue 6536 ppm); BJD 2460691.5727: gap (catalogue 6536 ppm); BJD 2460709.3586: not recovered, depth 5030 ± 258 ppm (catalogue 6536 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2558.01: Gaia DR3 5695421342277587840 at 0.02" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2558.01: dwarf priors not applied — RUWE 30.400345 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2558.01: 35 Gaia neighbour(s) within 52.5", contamination 39.08%; depth 4881 ppm (measured depth of the recovered catalogued transit); 6 could produce it if fully eclipsed (brightest 5695420586360916352, 51.1", ΔG 1.75); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 1 clean; BJD 2459279.7526 suspect: MOM_CENTR1 z=-7.4, POS_CORR1 z=-8.8 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2558.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2558.01: UCAC4 324-049925 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2558-01.yaml
python -m cygnus.multi report campaigns/toi-2558-01.yaml
```
