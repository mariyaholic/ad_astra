<!-- [private Drive store] -->
# Known-object test, TOI-3098.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3098-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1090, calibrate_screen #1066, event_census #1071, fetch_products #1065, known_signal_recovery #1067, moving_objects #1073, period_aliases #1072, prior_art #1092, residual_screen #1069, stellar_context #1068, variability_guard #1091
- Runner finished (UTC): 2026-09-26T10:34:01Z

## Bottom line

Positive control **inconclusive**: BJD 2460015.1037: gap (catalogue 15682 ppm).
Outside the catalogued epoch the screen left 281 threshold entries forming **50 distinct event(s)**, **34 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3098.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 163260812 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 173.137772 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -46.315267 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460015.103725 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15681.823373 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.1038025 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.315 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-10 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | lightcurve | 63 | True | `3fe99f6aa109f81f` | True |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | lightcurve | 64 | False | `0d74ac64fd4c7b5c` | True |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | lightcurve | 90 | False | `213ac52d718f1016` | True |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | lightcurve | 99 | False | `2ddc9d6bab57d3a3` | True |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | lightcurve | 100 | False | `a16bc557c1622e17` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460015.10372 | gap | 0 | — | 15682 | — |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 15682 | — |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 15682 | — |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 15682 | — |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 15682 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461070.36992 | -0.01751 | 110 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460034.02898 | -0.01682 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461098.76113 | -0.01681 | 111 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460767.51362 | -0.01628 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460762.78441 | -0.01628 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460029.29628 | -0.01590 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461046.70922 | -0.01566 | 110 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460748.58411 | -0.01565 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460753.31896 | -0.01549 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461075.09871 | -0.01548 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460038.76513 | -0.01526 | 102 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460043.48527 | -0.01500 | 85 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461065.63349 | -0.01498 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461089.29678 | -0.01485 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460024.57119 | -0.01474 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461084.56665 | -0.01470 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460057.69208 | -0.01434 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461079.83443 | -0.01430 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461051.44013 | -0.01428 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460019.83704 | -0.01407 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460067.22380 | -0.01400 | 37 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460758.06488 | -0.01381 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460772.24349 | -0.01374 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461094.03522 | -0.01361 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460062.45031 | -0.01331 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460043.55680 | -0.01329 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460052.94840 | -0.01319 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460757.99335 | -0.01248 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460033.96023 | -0.01215 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460029.37197 | -0.01190 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461093.96438 | -0.01096 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000163260812-0287-s_lc.fits` | 2460753.24326 | -0.00916 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461081.29701 | -0.00885 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000163260812-0255-s_lc.fits` | 2460038.69151 | -0.00883 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460062.49545 | -0.01028 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460054.45255 | -0.00998 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460054.80394 | -0.00960 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460054.28172 | -0.00945 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000163260812-0257-s_lc.fits` | 2460054.23033 | -0.00919 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.72284 | -0.00888 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461093.27824 | -0.00854 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.70687 | -0.00837 | 3 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461093.52825 | -0.00811 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.84716 | -0.00719 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.66034 | -0.00713 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000163260812-0302-s_lc.fits` | 2461075.17580 | -0.00696 | 2 | PDCSAP | 1, 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461046.78631 | -0.00678 | 2 | SAP | 1, 2 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.77146 | -0.00660 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.59506 | -0.00651 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000163260812-0300-s_lc.fits` | 2461072.79924 | -0.00622 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3098.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:33:57Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:33:59Z: TOI-3098.01 (TIC 163260812, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:34:00Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:34:00Z: TOI-3098 (*); TOI-3098.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460015.1037: gap (catalogue 15682 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 20%, 30%, 20%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3098.01: Gaia DR3 5375256166289838976 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3098.01: dwarf priors not applied — RUWE 1.4872453 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-3098.01: 24 Gaia neighbour(s) within 52.5", contamination 4.85%; depth 15682 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 34 persistent event(s), 19 clean; BJD 2460029.2963 suspect: POS_CORR2 z=-7.9, SAP_BKG z=+322.1; BJD 2460029.3720 suspect: SAP_BKG z=+104.6; BJD 2460033.9602 caution: manual exclude (within ±0.25 d); BJD 2460034.0290 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+5.1, MOM_CENTR2 z=+9.3, POS_CORR2 z=+9.4, SAP_BKG z=-5.3 |
| Moving objects at screen-event epochs | inconclusive | 34 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 6 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3098.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3098.01: TOI-3098 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3098-01.yaml
python -m cygnus.multi report campaigns/toi-3098-01.yaml
```
