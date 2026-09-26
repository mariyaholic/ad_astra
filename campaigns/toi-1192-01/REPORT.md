<!-- cygnus:generated-draft -->
# Known-object test, TOI-1192.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1192-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #635, calibrate_screen #607, event_census #621, fetch_products #606, known_signal_recovery #608, moving_objects #631, period_aliases #622, prior_art #639, residual_screen #618, stellar_context #609, variability_guard #636
- Runner finished (UTC): 2026-09-26T10:12:16Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1192.01 (BJD 2460524.9058: recovered, depth 7542 ± 122 ppm (catalogue 14807 ppm)).
Outside the catalogued epoch the screen left 45 threshold entries forming **18 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459422.3379 matches the catalogued transit's depth (8292 vs 7542 ppm), 1102.619 d later; 14 of 1102 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1192.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 158276040 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 286.550056 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 44.0808 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460524.90576 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14807.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.768 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.4999 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-10-18 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000158276040-0276-s_lc.fits` | lightcurve | 81 | True | `bf6645606c7ee08d` | True |
| `tess2020160202036-s0026-0000000158276040-0188-s_lc.fits` | lightcurve | 26 | False | `e4e71f6679726bfc` | True |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | lightcurve | 40 | False | `4a8622ae692427bf` | True |
| `tess2021204101404-s0041-0000000158276040-0212-s_lc.fits` | lightcurve | 41 | False | `1f1cb439d025db12` | True |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | lightcurve | 53 | False | `b17fdae4c1e4cf96` | True |
| `tess2022217014003-s0055-0000000158276040-0242-s_lc.fits` | lightcurve | 55 | False | `3a6f13b933ffff17` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000158276040-0276-s_lc.fits` | 2460524.90576 | recovered | 113 | 7542 ± 122 | 14807 | 1.23 |
| `tess2020160202036-s0026-0000000158276040-0188-s_lc.fits` | — | epoch not in this light curve | — | — | 14807 | — |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | — | epoch not in this light curve | — | — | 14807 | — |
| `tess2021204101404-s0041-0000000158276040-0212-s_lc.fits` | — | epoch not in this light curve | — | — | 14807 | — |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | — | epoch not in this light curve | — | — | 14807 | — |
| `tess2022217014003-s0055-0000000158276040-0242-s_lc.fits` | — | epoch not in this light curve | — | — | 14807 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024196212429-s0081-0000000158276040-0276-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020160202036-s0026-0000000158276040-0188-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021204101404-s0041-0000000158276040-0212-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022217014003-s0055-0000000158276040-0242-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021204101404-s0041-0000000158276040-0212-s_lc.fits` | 2459422.33791 | -0.00973 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459758.03409 | -0.00433 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459390.74533 | -0.00428 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459403.78995 | -0.00550 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459396.91069 | -0.00512 | 2 | SAP | 1, 2, 3 | no |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459755.84656 | -0.00457 | 2 | SAP | 1, 2, 3 | no |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459744.05881 | -0.00453 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022217014003-s0055-0000000158276040-0242-s_lc.fits` | 2459822.67959 | -0.00443 | 2 | SAP | 3 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459391.03978 | -0.00441 | 2 | PDCSAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459390.96270 | -0.00437 | 3 | PDCSAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459390.99395 | -0.00413 | 2 | PDCSAP | 3 | no |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459757.83270 | -0.00408 | 2 | PDCSAP | 2 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459396.95236 | -0.00404 | 2 | SAP | 3 | no |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459749.94088 | -0.00396 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459397.31764 | -0.00393 | 2 | SAP | 2, 3 | no |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459744.07270 | -0.00386 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 2459403.75800 | -0.00375 | 2 | SAP | 2, 3 | no |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 2459747.94639 | -0.00357 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459422.33791 | 8292 | 7542 | 1102.6192 | 14 / 1102 | 1102.62, 551.31, 367.54, 275.655, 220.524, 183.77, 157.517, 137.827, 122.513, 91.8849, 73.5079, 61.2566, 52.5057, 45.9425 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1192.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:12:12Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:12:14Z: TOI-1192.01 (TIC 158276040, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:12:15Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:12:15Z: 2MASS J19061407+4404536 (*); TOI-1192.01 (Pl?); TOI-1192 (Em*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460524.9058: recovered, depth 7542 ± 122 ppm (catalogue 14807 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3.5, ≤2.5, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 30%, 0%, 40%, 20%, 60%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459422.3379, ΔT = 1102.619 d, 14 of 1102 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1102.62, 551.31, 367.54, 275.655, 220.524, 183.77, 157.517, 137.827, 122.513, 91.8849, 73.5079, 61.2566 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1192.01: Gaia DR3 2106084325094924800 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1192.01: dwarf priors not applied — RUWE 7.209528 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1192.01: 23 Gaia neighbour(s) within 52.5", contamination 8.75%; depth 7542 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 2106072677143620480, 22.3", ΔG 2.83); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 0 clean; BJD 2459390.7453 suspect: earth point (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+13.4, POS_CORR1 z=+14.6, POS_CORR2 z=-5.7, SAP_BKG z=-38.6; BJD 2459422.3379 suspect: SAP_BKG z=-14.9; BJD 2459758.0341 suspect: MOM_CENTR1 z=-8.8, MOM_CENTR2 z=+8.1, POS_CORR1 z=-8.7, POS_CORR2 z=+9.0, SAP_BKG z=+8.6 |
| Moving objects at screen-event epochs | inconclusive | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1192.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1192.01: TOI-1192 otype Em* (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1192-01.yaml
python -m cygnus.multi report campaigns/toi-1192-01.yaml
```
