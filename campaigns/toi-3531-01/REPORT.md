<!-- cygnus:generated-draft -->
# Known-object test, TOI-3531.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3531-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #895, calibrate_screen #841, event_census #854, fetch_products #834, known_signal_recovery #843, moving_objects #856, period_aliases #855, prior_art #897, residual_screen #847, stellar_context #844, variability_guard #896
- Runner finished (UTC): 2026-09-26T10:22:22Z

## Bottom line

Positive control **inconclusive**: BJD 2459825.3327: partial, depth 2975 ± 167 ppm (catalogue 13074 ppm).
Outside the catalogued epoch the screen left 280 threshold entries forming **53 distinct event(s)**, **38 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3531.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 316038054 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 321.377492 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 55.722936 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459825.332652 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13073.8770598 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.3118658 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.711 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-08 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | lightcurve | 56 | True | `2660e54873a8d608` | True |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | lightcurve | 57 | False | `ef79410ed72b5e14` | True |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | lightcurve | 76 | False | `a392aad3b9700519` | True |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | lightcurve | 77 | False | `340e50dde9233f1b` | True |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | lightcurve | 83 | False | `7e7e7ef5897c168e` | True |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | lightcurve | 84 | False | `1fa7ac4c3bc0b4ca` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459825.33265 | partial | 118 | 2975 ± 167 | 13074 | 0.09 |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | — | epoch not in this light curve | — | — | 13074 | — |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | — | epoch not in this light curve | — | — | 13074 | — |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | — | epoch not in this light curve | — | — | 13074 | — |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | — | epoch not in this light curve | — | — | 13074 | — |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | — | epoch not in this light curve | — | — | 13074 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 2459859.62250 | -0.01323 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460373.96461 | -0.01312 | 118 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460560.63422 | -0.01301 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 2460610.18039 | -0.01301 | 114 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460389.20476 | -0.01300 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460396.82421 | -0.01286 | 111 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460404.44370 | -0.01284 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460419.68583 | -0.01283 | 114 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 2460602.56180 | -0.01273 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 2459871.05011 | -0.01267 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 2460606.37353 | -0.01267 | 112 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 2459878.67217 | -0.01265 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460377.77567 | -0.01259 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460400.63464 | -0.01251 | 114 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 2460591.12934 | -0.01249 | 110 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460393.01448 | -0.01246 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459848.19411 | -0.01245 | 118 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460385.39644 | -0.01238 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 2459855.81074 | -0.01238 | 112 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459844.38300 | -0.01236 | 116 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 2460594.94249 | -0.01235 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459832.95169 | -0.01230 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460370.15703 | -0.01219 | 110 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460575.89124 | -0.01217 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460564.46133 | -0.01216 | 118 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459840.57258 | -0.01203 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460583.51067 | -0.01201 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460579.70235 | -0.01193 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459829.14263 | -0.01192 | 116 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459836.76353 | -0.01190 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460568.27247 | -0.01184 | 114 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460572.08152 | -0.01179 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460381.63119 | -0.01166 | 47 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 2459874.87989 | -0.01152 | 86 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459852.00382 | -0.01143 | 118 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 2459867.20643 | -0.01103 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459836.84548 | -0.00544 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459839.16771 | -0.00500 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.44286 | -0.00770 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.45952 | -0.00732 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.46508 | -0.00705 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 2460595.02374 | -0.00683 | 2 | PDCSAP+SAP | 1 | no |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.47341 | -0.00668 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.48244 | -0.00660 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.43314 | -0.00652 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460570.90304 | -0.00644 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 2460423.48730 | -0.00622 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 2460370.07717 | -0.00570 | 3 | PDCSAP | 2 | no |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460564.61411 | -0.00525 | 2 | SAP | 2, 3 | no |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459838.22882 | -0.00492 | 2 | PDCSAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460571.11138 | -0.00474 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 2460571.09888 | -0.00427 | 2 | SAP | 3 | no |
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 2459838.46215 | -0.00398 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3531.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:22:19Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:22:20Z: TOI-3531.01 (TIC 316038054, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:22:21Z: Gaia DR3 2177849036734191744 (type EP, P 3.80952 d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:22:21Z: TOI-3531.01 (Pl?); TOI-3531 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2459825.3327: partial, depth 2975 ± 167 ppm (catalogue 13074 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 0%, 10%, 20%, 30%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3531.01: Gaia DR3 2177849036734191744 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3531.01: Teff 6260 K, R* 1.47 ± 0.12, M* 1.33 ± 0.13, ρ* 0.42 ± 0.11 ρ☉ (dwarf sequence, M_G 3.28, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3531.01: 107 Gaia neighbour(s) within 52.5", contamination 17.44%; depth 13074 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 2177849002374450560, 44.1", ΔG 3.19); a centroid test is needed |
| Pointing and quality census per event | failed | 38 persistent event(s), 17 clean; BJD 2459832.9517 suspect: SAP_BKG z=+9.0; BJD 2459836.7635 suspect: SAP_BKG z=+29.5; BJD 2459836.8455 suspect: SAP_BKG z=+17.9; BJD 2459839.1677 suspect: MOM_CENTR2 z=-8.4, POS_CORR2 z=-9.7 |
| Moving objects at screen-event epochs | inconclusive | 38 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3531.01: Gaia DR3 2177849036734191744   EP                             P=3.80952 at 1.1" |
| Object-class guard (SIMBAD) | passed | TOI-3531.01: TOI-3531 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3531-01.yaml
python -m cygnus.multi report campaigns/toi-3531-01.yaml
```
