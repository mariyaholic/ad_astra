<!-- [private Drive store] -->
# Known-object test, TOI-1709.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1709-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #986, calibrate_screen #972, event_census #976, fetch_products #971, known_signal_recovery #973, moving_objects #979, period_aliases #977, prior_art #988, residual_screen #975, stellar_context #974, variability_guard #987
- Runner finished (UTC): 2026-09-26T10:27:45Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1709.01 (BJD 2459597.1983: recovered, depth 8467 ± 116 ppm (catalogue 10850 ppm)).
Outside the catalogued epoch the screen left 79 threshold entries forming **25 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459581.9385 matches the catalogued transit's depth (8346 vs 8467 ppm), 15.258 d later; 2 of 15 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1709.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 29119552 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 118.629831 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 45.807841 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459597.198308 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10850.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.311 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.2061 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-02-27 10:10:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | lightcurve | 47 | True | `bdd2eca30fe6b6d3` | True |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | lightcurve | 60 | False | `3784cdca0d382da0` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2459597.19831 | recovered | 100 | 8467 ± 116 | 10850 | -0.05 |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | — | epoch not in this light curve | — | — | 10850 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459955.74880 | -0.00935 | 85 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459940.49026 | -0.00892 | 83 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2459604.82732 | -0.00892 | 82 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459948.12097 | -0.00890 | 85 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2459581.93849 | -0.00889 | 80 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2459589.56913 | -0.00878 | 82 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2459606.34395 | -0.00337 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459960.17171 | -0.00312 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.28616 | -0.00475 | 3 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.07435 | -0.00468 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.20352 | -0.00409 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.49867 | -0.00408 | 3 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.54381 | -0.00375 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459942.60767 | -0.00372 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.48547 | -0.00359 | 2 | SAP | 1, 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459942.97296 | -0.00355 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.45214 | -0.00354 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459942.95074 | -0.00351 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459939.47148 | -0.00348 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459955.46616 | -0.00339 | 2 | SAP | 2, 3 | no |
| `tess2021364111932-s0047-0000000029119552-0218-s_lc.fits` | 2459585.65660 | -0.00332 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459942.66740 | -0.00322 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459955.40019 | -0.00319 | 3 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459941.52292 | -0.00316 | 2 | SAP | 1 | no |
| `tess2022357055054-s0060-0000000029119552-0249-s_lc.fits` | 2459943.19380 | -0.00316 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459581.93849 | 8346 | 8467 | 15.2577 | 2 / 15 | 15.2577, 7.6288 |
| 2459589.56913 | 8236 | 8467 | 7.6271 | 0 / 7 |  |
| 2459604.82732 | 8651 | 8467 | 7.6311 | 0 / 7 |  |
| 2459940.49026 | 8333 | 8467 | 343.2941 | 16 / 343 | 343.294, 171.647, 114.431, 85.8235, 68.6588, 57.2157, 49.042, 42.9118, 38.1438, 34.3294, 31.2086, 28.6078, 26.4072, 24.521, 22.8863, 7.6288 |
| 2459948.12097 | 8494 | 8467 | 350.9248 | 22 / 350 | 350.925, 175.462, 116.975, 87.7312, 70.185, 58.4875, 50.1321, 43.8656, 38.9916, 35.0925, 31.9023, 29.2437, 26.9942, 25.0661, 23.395, 21.9328, 20.6426, 19.4958, 18.4697, 17.5462 |
| 2459955.74880 | 8470 | 8467 | 358.5526 | 22 / 358 | 358.553, 179.276, 119.517, 89.6382, 71.7105, 59.7588, 51.2218, 44.8191, 39.8392, 35.8553, 32.5957, 29.8794, 27.581, 25.6109, 23.9035, 22.4095, 21.0913, 19.9196, 18.8712, 17.9276 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1709.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:27:41Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:27:43Z: TOI-1709.01 (TIC 29119552, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:27:44Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:27:45Z: TOI-1709 (*); TOI-1709.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459597.1983: recovered, depth 8467 ± 116 ppm (catalogue 10850 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 80%, 50% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 6 repeat-candidate event(s); first at BJD 2459581.9385, ΔT = 15.258 d, 2 of 15 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (15.2577, 7.6288 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1709.01: Gaia DR3 926524844902727296 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1709.01: dwarf priors not applied — RUWE 4.386462 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1709.01: 6 Gaia neighbour(s) within 52.5", contamination 1.34%; depth 8467 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 926524844905419008, 5.8", ΔG 4.84); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 5 clean; BJD 2459604.8273 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+5.9; BJD 2459606.3439 suspect: MOM_CENTR1 z=+5.6, MOM_CENTR2 z=+5.9, POS_CORR1 z=+6.2, POS_CORR2 z=+6.0; BJD 2459955.7488 suspect: MOM_CENTR1 z=-6.1, MOM_CENTR2 z=-5.5, POS_CORR1 z=-6.6, POS_CORR2 z=-5.7 |
| Moving objects at screen-event epochs | passed | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1709.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1709.01: TOI-1709 otype * (star_or_other) at 0.6" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1709-01.yaml
python -m cygnus.multi report campaigns/toi-1709-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** Both events are the catalogued signal's adjacent transits (one and two periods before the reference). No new signal.

Source: `campaigns/toi-1709-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
