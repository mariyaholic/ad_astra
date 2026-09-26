<!-- [private Drive store] -->
# Known-object test, TOI-3586.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3586-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #934, calibrate_screen #915, event_census #930, fetch_products #914, known_signal_recovery #917, moving_objects #932, period_aliases #931, prior_art #936, residual_screen #926, stellar_context #918, variability_guard #935
- Runner finished (UTC): 2026-09-26T10:23:54Z

## Bottom line

Positive control **inconclusive**: BJD 2459810.5215: gap (catalogue 31070 ppm).
Outside the catalogued epoch the screen left 216 threshold entries forming **48 distinct event(s)**, **24 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3586.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 286080865 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 310.219074 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 50.922722 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459810.521522 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 31070.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.276 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.3944 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-20 12:02:42 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | lightcurve | 55 | True | `6bf83da9fca23f33` | True |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | lightcurve | 56 | False | `338c1d70f4405442` | True |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | lightcurve | 75 | False | `b3212f5e557c2401` | True |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | lightcurve | 76 | False | `a6e0d34982831d11` | True |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | lightcurve | 82 | False | `4ee2ea2099898f37` | True |
| `tess2024249191853-s0083-0000000286080865-0280-s_lc.fits` | lightcurve | 83 | False | `8accb1c4f8b54eb8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | 2459810.52152 | gap | 0 | — | 31070 | — |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | — | epoch not in this light curve | — | — | 31070 | — |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | — | epoch not in this light curve | — | — | 31070 | — |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | — | epoch not in this light curve | — | — | 31070 | — |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | — | epoch not in this light curve | — | — | 31070 | — |
| `tess2024249191853-s0083-0000000286080865-0280-s_lc.fits` | — | epoch not in this light curve | — | — | 31070 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 10000 |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024249191853-s0083-0000000286080865-0280-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 2460353.89250 | -0.03056 | 75 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460387.83410 | -0.02948 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | 2459833.16001 | -0.02901 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460376.52638 | -0.02882 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 2460365.20627 | -0.02864 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | 2459821.84128 | -0.02830 | 74 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 2460342.57048 | -0.02796 | 75 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | 2459799.20215 | -0.02751 | 70 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | 2459844.48074 | -0.02750 | 84 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000286080865-0280-s_lc.fits` | 2460568.96753 | -0.02741 | 77 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000286080865-0280-s_lc.fits` | 2460580.28891 | -0.02698 | 73 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460546.31478 | -0.02682 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460535.01257 | -0.02604 | 74 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460557.64814 | -0.02589 | 81 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460546.36269 | -0.02530 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460387.88896 | -0.02497 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 2460342.61978 | -0.02280 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 2460353.83347 | -0.02036 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 2460357.16259 | -0.01863 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | 2459799.15076 | -0.01820 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460546.38006 | -0.01734 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460372.59027 | -0.01515 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460534.95007 | -0.01389 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460534.95701 | -0.01353 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460543.78281 | -0.01688 | 9 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.44463 | -0.01624 | 2 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460544.99324 | -0.01579 | 2 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460388.63341 | -0.01545 | 2 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.20019 | -0.01523 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460376.47083 | -0.01441 | 2 | PDCSAP | 1, 2 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460543.77239 | -0.01432 | 4 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460387.78896 | -0.01429 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460386.83339 | -0.01398 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.40297 | -0.01351 | 2 | SAP | 2, 3 | no |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | 2459838.91067 | -0.01348 | 2 | PDCSAP | 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.13213 | -0.01316 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460538.44872 | -0.01282 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460543.70156 | -0.01268 | 2 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.16130 | -0.01167 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460538.29594 | -0.01138 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460538.16261 | -0.01128 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.02102 | -0.01127 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.32935 | -0.01121 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.44880 | -0.01115 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460538.49872 | -0.01103 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460543.70573 | -0.01101 | 2 | SAP | 1, 2 | no |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 2460545.30435 | -0.01052 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 2460394.73489 | -0.01044 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3586.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:23:50Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:23:51Z: TOI-3586.01 (TIC 286080865, disposition PC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:23:53Z: Gaia DR3 2180517379653155072 (type ROT, P — d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:23:53Z: TOI-3586 (*); TOI-3586.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2459810.5215: gap (catalogue 31070 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, ≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3586.01: Gaia DR3 2180517379653155072 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3586.01: dwarf priors not applied — RUWE 1.9690187 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3586.01: 62 Gaia neighbour(s) within 52.5", contamination 64.01%; depth 31070 ppm (catalogue depth); 4 could produce it if fully eclipsed (brightest 2180423611927056384, 43.7", ΔG -0.12); a centroid test is needed |
| Pointing and quality census per event | failed | 24 persistent event(s), 10 clean; BJD 2459821.8413 suspect: SAP_BKG z=+9.9; BJD 2460353.8335 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2460353.8925 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+5.5, POS_CORR1 z=+6.1; BJD 2460357.1626 suspect: SAP_BKG z=+8.2 |
| Moving objects at screen-event epochs | inconclusive | 24 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3586.01: Gaia DR3 2180517379653155072   ROT                            P=None at 0.2" |
| Object-class guard (SIMBAD) | passed | TOI-3586.01: TOI-3586 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3586-01.yaml
python -m cygnus.multi report campaigns/toi-3586-01.yaml
```
