<!-- cygnus:generated-draft -->
# Known-object test, TOI-3501.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3501-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #255, calibrate_screen #227, event_census #232, fetch_products #226, known_signal_recovery #228, moving_objects #250, period_aliases #233, prior_art #258, residual_screen #231, stellar_context #229, variability_guard #257
- Runner finished (UTC): 2026-09-26T09:59:08Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3501.01 (BJD 2459313.4714: recovered, depth 16092 ± 161 ppm (catalogue 26220 ppm)).
Outside the catalogued epoch the screen left 125 threshold entries forming **44 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459328.8217 matches the catalogued transit's depth (15818 vs 16092 ppm), 15.326 d later; 0 of 15 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3501.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 98957720 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 181.000805 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -28.325347 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459313.471423 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 26220.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.87 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.7413 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-01-25 10:10:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | lightcurve | 37 | True | `dcb1089104691bc0` | True |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | lightcurve | 63 | False | `4f1fecfc3a6a7add` | True |
| `tess2025071122000-s0090-0000000098957720-0287-s_lc.fits` | lightcurve | 90 | False | `680c5f6c690a8c5b` | True |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | lightcurve | 101 | False | `8a9947fe86e2361f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459313.47142 | recovered | 86 | 16092 ± 161 | 26220 | 0.57 |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 26220 | — |
| `tess2025071122000-s0090-0000000098957720-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 26220 | — |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 26220 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025071122000-s0090-0000000098957720-0287-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025071122000-s0090-0000000098957720-0287-s_lc.fits` | 2460756.39443 | -0.01878 | 72 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461109.45640 | -0.01867 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461124.80263 | -0.01855 | 68 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000098957720-0287-s_lc.fits` | 2460771.74593 | -0.01845 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460019.58258 | -0.01836 | 72 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460034.93702 | -0.01790 | 73 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459328.82174 | -0.01786 | 74 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.81922 | -0.00874 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.70255 | -0.00785 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.87269 | -0.00769 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.86505 | -0.00724 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.64838 | -0.00686 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.31895 | -0.00639 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.48353 | -0.00628 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.73449 | -0.00623 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.31226 | -0.00621 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.59117 | -0.00618 | 2 | SAP | 3 | no |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459332.42857 | -0.00612 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.78449 | -0.00603 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.40645 | -0.00592 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.36087 | -0.00587 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.85949 | -0.00581 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.75090 | -0.00551 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.33006 | -0.00537 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.71201 | -0.00534 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000098957720-0303-s_lc.fits` | 2461119.72755 | -0.00525 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.76340 | -0.00521 | 2 | SAP | 2, 3 | no |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459330.25364 | -0.00519 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.81479 | -0.00502 | 2 | SAP | 1, 2, 3 | no |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459326.09543 | -0.00482 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.28145 | -0.00473 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.39534 | -0.00469 | 2 | SAP | 2, 3 | no |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459325.12670 | -0.00465 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.26686 | -0.00459 | 3 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.68145 | -0.00458 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.55645 | -0.00457 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.84673 | -0.00436 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.51756 | -0.00427 | 2 | SAP | 3 | no |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459326.01279 | -0.00425 | 3 | SAP | 1, 2, 3 | no |
| `tess2021091135823-s0037-0000000098957720-0208-s_lc.fits` | 2459324.90657 | -0.00422 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460028.10084 | -0.00408 | 2 | PDCSAP | 1, 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.23006 | -0.00406 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.77590 | -0.00406 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000098957720-0255-s_lc.fits` | 2460033.55089 | -0.00391 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459328.82174 | 15818 | 16092 | 15.3264 | 0 / 15 |  |
| 2460019.58258 | 16821 | 16092 | 706.0873 | 13 / 706 | 706.087, 353.044, 235.362, 176.522, 141.218, 117.681, 100.87, 88.2609, 70.6087, 58.8406, 50.4348, 30.6994, 15.3497 |
| 2460034.93702 | 16266 | 16092 | 721.4417 | 12 / 721 | 721.442, 240.481, 144.288, 103.063, 80.1602, 65.5856, 55.4955, 48.0961, 42.4377, 37.9706, 34.3544, 15.3498 |
| 2460756.39443 | 16297 | 16092 | 1442.8991 | 28 / 1442 | 1442.9, 721.45, 480.966, 288.58, 240.483, 206.128, 160.322, 144.29, 131.173, 110.992, 103.064, 96.1933, 84.8764, 80.1611, 75.9421, 68.7095, 65.5863, 62.7347, 55.4961, 53.4407 |
| 2460771.74593 | 15237 | 16092 | 1458.2506 | 25 / 1458 | 1458.25, 729.125, 486.084, 364.563, 291.65, 243.042, 208.321, 182.281, 162.028, 145.825, 132.568, 121.521, 104.161, 97.2167, 91.1407, 81.0139, 76.75, 72.9125, 63.4022, 60.7604 |
| 2461109.45640 | 15280 | 16092 | 1795.9611 | 27 / 1795 | 1795.96, 897.981, 598.654, 448.99, 299.327, 256.566, 224.495, 199.551, 163.269, 149.663, 138.151, 128.283, 105.645, 99.7756, 94.5243, 81.6346, 74.8317, 66.5171, 61.9297, 52.8224 |
| 2461124.80263 | 14589 | 16092 | 1811.3073 | 30 / 1811 | 1811.31, 905.654, 603.769, 452.827, 301.885, 258.758, 226.413, 201.256, 164.664, 150.942, 139.331, 129.379, 113.207, 106.547, 95.332, 86.2527, 82.3322, 69.6657, 67.0855, 58.4293 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3501.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:59:04Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:59:06Z: TOI-3501.01 (TIC 98957720, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:59:07Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T09:59:07Z: TYC 6679-861-1 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459313.4714: recovered, depth 16092 ± 161 ppm (catalogue 26220 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 60%, 0%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 7 repeat-candidate event(s); first at BJD 2459328.8217, ΔT = 15.326 d, 0 of 15 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3501.01: Gaia DR3 3486043573401367168 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3501.01: dwarf priors not applied — RUWE 1.6394621 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-3501.01: 5 Gaia neighbour(s) within 52.5", contamination 0.85%; depth 16092 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 7 persistent event(s), 5 clean; BJD 2460034.9370 suspect: MOM_CENTR2 z=-8.4, POS_CORR2 z=-8.7, SAP_BKG z=-5.1; BJD 2460756.3944 suspect: SAP_BKG z=+7.5 |
| Moving objects at screen-event epochs | inconclusive | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-3501.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-3501.01: TYC 6679-861-1 otype SB* (multiple) at 0.7" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3501-01.yaml
python -m cygnus.multi report campaigns/toi-3501-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** No new signal.

Source: `campaigns/toi-3501-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
