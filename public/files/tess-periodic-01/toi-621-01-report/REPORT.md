<!-- [private Drive store] -->
# Known-object test, TOI-621.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-621-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #670, calibrate_screen #641, event_census #652, fetch_products #640, known_signal_recovery #644, moving_objects #654, period_aliases #653, prior_art #672, residual_screen #651, stellar_context #645, variability_guard #671
- Runner finished (UTC): 2026-09-26T10:13:06Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 141 threshold entries forming **28 distinct event(s)**, **16 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-621.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 30828562 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 134.718341 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -43.452796 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459304.418696 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6080.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.388 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.1327 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-10-10 10:08:04 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | lightcurve | 8 | False | `588517ccc35fd1ab` | True |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | lightcurve | 9 | False | `6c8775ecd3ef7bd8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | — | epoch not in this light curve | — | — | 6080 | — |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | — | epoch not in this light curve | — | — | 6080 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458541.89601 | -0.00573 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458560.55142 | -0.00569 | 33 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.68696 | -0.00568 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458554.34873 | -0.00562 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458545.01267 | -0.00558 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458557.45840 | -0.00553 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458563.68192 | -0.00550 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458538.78490 | -0.00542 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458526.33895 | -0.00539 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458560.59169 | -0.00534 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458551.23557 | -0.00533 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458523.22153 | -0.00531 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458548.12239 | -0.00527 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000030828562-0139-s_lc.fits` | 2458566.79644 | -0.00526 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458520.10896 | -0.00517 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.64460 | -0.00415 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.02029 | -0.00373 | 28 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.04876 | -0.00320 | 11 | SAP | 2, 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.05987 | -0.00279 | 3 | SAP | 2, 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458539.72865 | -0.00226 | 2 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.07029 | -0.00215 | 2 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.07446 | -0.00214 | 2 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.06543 | -0.00207 | 3 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.08140 | -0.00204 | 2 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458535.09112 | -0.00175 | 2 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458517.72418 | -0.00143 | 2 | PDCSAP | 2, 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458526.28964 | -0.00142 | 2 | PDCSAP | 2, 3 | no |
| `tess2019032160000-s0008-0000000030828562-0136-s_lc.fits` | 2458517.65196 | -0.00132 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-621.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:13:01Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:13:03Z: TOI-621.01 (TIC 30828562, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:13:05Z: KELT KS34C003047 (type EA, P 3.112338 d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:13:05Z: HD  77113 (SB*); TOI-621.01 (err)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-621.01: Gaia DR3 5332029175877608576 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-621.01: Teff 7771 K, R* 1.79 ± 0.14, M* 1.90 ± 0.19, ρ* 0.33 ± 0.09 ρ☉ (dwarf sequence, M_G 1.96, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-621.01: 1 Gaia neighbour(s) within 52.5", contamination 0.19%; depth 6080 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 16 persistent event(s), 9 clean; BJD 2458535.6446 suspect: manual exclude (in event), MOM_CENTR1 z=-9.3, MOM_CENTR2 z=-8.4, POS_CORR1 z=-9.1, POS_CORR2 z=-8.3, SAP_BKG z=-9.6; BJD 2458535.6870 suspect: manual exclude (within ±0.25 d), MOM_CENTR1 z=-9.5, MOM_CENTR2 z=-8.4, POS_CORR1 z=-10.0, POS_CORR2 z=-8.3, SAP_BKG z=-7.1; BJD 2458541.8960 suspect: MOM_CENTR1 z=-7.4, MOM_CENTR2 z=+9.0, POS_CORR1 z=-7.2, POS_CORR2 z=+9.3, SAP_BKG z=+5.8; BJD 2458545.0127 suspect: SAP_BKG z=+8.9 |
| Moving objects at screen-event epochs | inconclusive | 16 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | failed | TOI-621.01: KELT KS34C003047               EA                             P=3.112338 at 1.0" |
| Object-class guard (SIMBAD) | inconclusive | TOI-621.01: HD  77113 otype SB* (multiple) at 0.6" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-621-01.yaml
python -m cygnus.multi report campaigns/toi-621-01.yaml
```
