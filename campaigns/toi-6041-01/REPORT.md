<!-- cygnus:generated-draft -->
# Known-object test, TOI-6041.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6041-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5212, calibrate_screen #5204, event_census #5208, fetch_independent #5211, fetch_products #5203, known_signal_recovery #5205, moving_objects #5210, period_aliases #5209, prior_art #5214, residual_screen #5207, stellar_context #5206, variability_guard #5213
- Runner finished (UTC): 2026-10-02T06:13:58Z

## Bottom line

Positive control **failed**: BJD 2459890.0882: not recovered, depth 2178 ± 70 ppm (catalogue 2352 ppm); BJD 2458796.0260: not recovered, depth 2286 ± 69 ppm (catalogue 2352 ppm).
Outside the catalogued epoch the screen left 56 threshold entries forming **14 distinct event(s)**, **9 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6041.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 192415680 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 46.061033 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 43.557667 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459890.088192 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1094.062167 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 2352.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.534 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.2063 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-01-13 12:03:09 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000192415680-0247-s_lc.fits` | lightcurve | 58 | True | `a813e425c527758e` | False |
| `tess2019306063752-s0018-0000000192415680-0162-s_lc.fits` | lightcurve | 18 | False | `5577a9336672ae1c` | False |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | lightcurve | 85 | False | `f837cba813559d1e` | False |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000192415680-0247-s_lc.fits` | 2459890.08819 | not_recovered | 106 | 2178 ± 70 | 2352 | — |
| `tess2019306063752-s0018-0000000192415680-0162-s_lc.fits` | 2458796.02603 | not_recovered | 106 | 2286 ± 69 | 2352 | — |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | — | epoch not in this light curve | — | — | 2352 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000192415680-0247-s_lc.fits` | — | False |  |  |
| `tess2019306063752-s0018-0000000192415680-0162-s_lc.fits` | — | False |  |  |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.51800 | -0.00333 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.48744 | -0.00274 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.46452 | -0.00272 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.47216 | -0.00270 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.44716 | -0.00268 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.45688 | -0.00255 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.52772 | -0.00253 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.53883 | -0.00250 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.50619 | -0.00243 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460622.69444 | -0.00274 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460622.91944 | -0.00271 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460622.76527 | -0.00245 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460616.70474 | -0.00235 | 3 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000192415680-0282-s_lc.fits` | 2460619.51105 | -0.00230 | 2 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6041.01**

- NASA_Exoplanet_Archive (done, 2026-10-02): 2 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-10-02T06:13:53Z: TOI-6041 c (host TOI-6041); TOI-6041 b (host TOI-6041)
- TESS_TOI (done, 2026-10-02): 1 match(es) in TESS_TOI within 30" as of 2026-10-02T06:13:55Z: TOI-6041.01 (TIC 192415680, disposition PC)
- VSX (done, 2026-10-02): 1 match(es) in VSX within 30" as of 2026-10-02T06:13:56Z: Gaia DR3 432549871529588608 (type ROT, P — d)
- SIMBAD (done, 2026-10-02): 4 match(es) in SIMBAD within 30" as of 2026-10-02T06:13:57Z: TOI-6041b (Pl); TYC 2859-682-1 (Em*); TOI-6041c (Pl); NVSS J030415+433340 (Rad)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459890.0882: not recovered, depth 2178 ± 70 ppm (catalogue 2352 ppm); BJD 2458796.0260: not recovered, depth 2286 ± 69 ppm (catalogue 2352 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | inconclusive | screen run at each light curve's own k* (none, none, 3; ≤ 0 persistent null events outside the veto); 2 light curve(s) have no usable cadence outside the veto (the veto window covers all of the data; no k* exists there) |
| Synthetic signal injection–recovery | inconclusive | completeness for 2000 ppm, 4.0 h boxes at the declared threshold: 0% per light curve (pass mark 90%) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6041.01: Gaia DR3 432549871529588608 at 0.00" (propagated 2016.0 → J2015.5; 0.05" unpropagated, proper-motion shift 0.05") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6041.01: Teff 5332 K, R* 0.84 ± 0.07, M* 0.89 ± 0.09, ρ* 1.51 ± 0.39 ρ☉ (dwarf sequence, M_G 5.41, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6041.01: 16 Gaia neighbour(s) within 52.5", contamination 0.86%; depth 2352 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 432549493572472448, 45.4", ΔG 6.33); a centroid test is needed |
| Pointing and quality census per event | passed | 9 persistent event(s), 9 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | inconclusive | 9 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6041.01: Gaia DR3 432549871529588608    ROT                            P=None at 1.4" |
| Object-class guard (SIMBAD) | passed | TOI-6041.01: TYC 2859-682-1 otype Em* (star_or_other) at 1.5" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6041-01.yaml
python -m cygnus.multi report campaigns/toi-6041-01.yaml
```
