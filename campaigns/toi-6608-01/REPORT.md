<!-- cygnus:generated-draft -->
# Known-object test, TOI-6608.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6608-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4166, calibrate_screen #4144, event_census #4152, fetch_independent #4159, fetch_products #4142, known_signal_recovery #4146, moving_objects #4155, period_aliases #4153, prior_art #4168, residual_screen #4150, stellar_context #4147, variability_guard #4167
- Runner finished (UTC): 2026-09-30T21:40:53Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6608.01 (BJD 2461132.2447: recovered, depth 10970 ± 1019 ppm (catalogue 19146 ppm); BJD 2461139.5592: gap (catalogue 19146 ppm); BJD 2461146.8737: recovered, depth 10132 ± 1039 ppm (catalogue 19146 ppm)).
Outside the catalogued epoch the screen left 9 threshold entries forming **4 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6608.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 366315051 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 218.944637 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -32.719293 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460093.589256 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 7.3144752 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 19146.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.481 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8314 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | lightcurve | 102 | False | `7f5830bcb4006b73` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461132.24473 | recovered | 44 | 10970 ± 1019 | 19146 | -0.09 |
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461139.55921 | gap | 0 | — | 19146 | — |
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461146.87368 | recovered | 44 | 10132 ± 1039 | 19146 | 0.05 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: —, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461127.32117 | -0.02249 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461129.58937 | -0.02227 | 2 | PDCSAP+SAP | 3 | no |
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461133.05693 | -0.01937 | 3 | PDCSAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000366315051-0304-s_lc.fits` | 2461136.18139 | -0.01451 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6608.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:40:44Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:40:46Z: TOI-6608.01 (TIC 366315051, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:40:49Z: ASASSN-V J143546.72-324309.5 (type ROT, P 1.1616 d)
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:40:51Z: UCAC4 287-074748 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2461132.2447: recovered, depth 10970 ± 1019 ppm (catalogue 19146 ppm); BJD 2461139.5592: gap (catalogue 19146 ppm); BJD 2461146.8737: recovered, depth 10132 ± 1039 ppm (catalogue 19146 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6608.01: Gaia DR3 6216291267710496128 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6608.01: Teff 5074 K, R* 0.83 ± 0.07, M* 0.89 ± 0.09, ρ* 1.54 ± 0.40 ρ☉ (dwarf sequence, M_G 5.44, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6608.01: 11 Gaia neighbour(s) within 52.5", contamination 66.14%; depth 10970 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 6216291267710489088, 44.7", ΔG -0.44); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2461127.3212 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+270.1 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6608.01: ASASSN-V J143546.72-324309.5   ROT                            P=1.1616 at 1.1" |
| Object-class guard (SIMBAD) | passed | TOI-6608.01: UCAC4 287-074748 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6608-01.yaml
python -m cygnus.multi report campaigns/toi-6608-01.yaml
```
