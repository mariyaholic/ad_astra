<!-- [private Drive store] -->
# Known-object test, TOI-5379.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5379-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #514, calibrate_screen #491, event_census #499, fetch_products #490, known_signal_recovery #493, moving_objects #502, period_aliases #500, prior_art #517, residual_screen #498, stellar_context #494, variability_guard #515
- Runner finished (UTC): 2026-09-26T10:09:25Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5379.01 (BJD 2459942.5443: recovered, depth 7798 ± 86 ppm (catalogue 10765 ppm)).
Outside the catalogued epoch the screen left 81 threshold entries forming **29 distinct event(s)**, **5 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459955.2889 matches the catalogued transit's depth (7411 vs 7798 ppm), 12.743 d later; 1 of 12 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5379.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 328325110 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 112.424109 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 50.6838 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459942.544324 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10765.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.633 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.59788 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-09 12:03:10 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | lightcurve | 60 | True | `710760d3bb5d3f23` | True |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | lightcurve | 47 | False | `3b911445ca513037` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459942.54432 | recovered | 109 | 7798 ± 86 | 10765 | 0.04 |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | — | epoch not in this light curve | — | — | 10765 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459955.28889 | -0.00872 | 87 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | 2459598.49521 | -0.00842 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | 2459585.74881 | -0.00835 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | 2459585.68423 | -0.00318 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000328325110-0218-s_lc.fits` | 2459598.42924 | -0.00287 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.49789 | -0.00478 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.20483 | -0.00437 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.38261 | -0.00351 | 4 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.13677 | -0.00340 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459939.00197 | -0.00315 | 2 | PDCSAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.16867 | -0.00309 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.24511 | -0.00307 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459939.03253 | -0.00293 | 2 | PDCSAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.24927 | -0.00292 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.22700 | -0.00288 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459943.54928 | -0.00276 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459939.27281 | -0.00275 | 2 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459939.25615 | -0.00273 | 2 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459939.05892 | -0.00272 | 2 | PDCSAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459938.98114 | -0.00270 | 2 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459938.95614 | -0.00269 | 2 | PDCSAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459955.35278 | -0.00257 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.37144 | -0.00255 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.34505 | -0.00255 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.36727 | -0.00244 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459939.08878 | -0.00243 | 3 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.20130 | -0.00237 | 3 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459962.30200 | -0.00235 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000328325110-0249-s_lc.fits` | 2459941.95759 | -0.00228 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459955.28889 | 7411 | 7798 | 12.7431 | 1 / 12 | 12.7431 |
| 2459585.74881 | 7418 | 7798 | 356.7970 | 17 / 356 | 356.797, 178.399, 118.932, 89.1992, 71.3594, 59.4662, 50.971, 44.5996, 39.6441, 35.6797, 32.4361, 29.7331, 27.4459, 25.4855, 23.7865, 22.2998, 12.7427 |
| 2459598.49521 | 7707 | 7798 | 344.0506 | 18 / 344 | 344.051, 172.025, 114.683, 86.0126, 68.8101, 57.3418, 49.1501, 43.0063, 38.2278, 34.4051, 31.2773, 28.6709, 26.4654, 24.575, 22.9367, 21.5032, 20.2383, 12.7426 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-5379.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:09:21Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:09:23Z: TOI-5379.01 (TIC 328325110, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:09:24Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:09:24Z: HD 233395 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459942.5443: recovered, depth 7798 ± 86 ppm (catalogue 10765 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 90%, 80% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2459955.2889, ΔT = 12.743 d, 1 of 12 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (12.7431 d); duration likelihood under Gaia priors (circular orbits) peaks at 12.7 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5379.01: Gaia DR3 983011056484954496 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5379.01: Teff 6319 K, R* 1.38 ± 0.11, M* 1.26 ± 0.13, ρ* 0.48 ± 0.13 ρ☉ (dwarf sequence, M_G 3.51, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5379.01: 5 Gaia neighbour(s) within 52.5", contamination 4.27%; depth 7798 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 983011090844692224, 33.8", ΔG 3.84); a centroid test is needed |
| Pointing and quality census per event | failed | 5 persistent event(s), 4 clean; BJD 2459955.2889 suspect: manual exclude (within ±0.25 d), MOM_CENTR1 z=-28.3, MOM_CENTR2 z=-40.6, POS_CORR1 z=-28.4, POS_CORR2 z=-41.7, SAP_BKG z=+33.6 |
| Moving objects at screen-event epochs | inconclusive | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-5379.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-5379.01: HD 233395 otype SB* (multiple) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5379-01.yaml
python -m cygnus.multi report campaigns/toi-5379-01.yaml
```
