# Known-object test, TOI-6675.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-6675-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #333, fetch_products #332, known_signal_recovery #334, period_aliases #336, prior_art #337, residual_screen #335
- Runner finished (UTC): 2026-09-25T04:36:51Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6675.01 (BJD 2459410.6163: recovered, depth 1249 ± 59 ppm (catalogue 1323 ppm)).
Outside the catalogued epoch the screen left 64 threshold entries forming **30 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **passed** cleanly: the catalogued transit was recovered at its epoch (sector 40, offset −0.09 h) with depth 1249 ± 59 ppm vs catalogue 1323 ppm (ratio 0.94) — the cleanest control of the batch.

Hand checks: **0 persistent screen events** (64 threshold entries → 30 distinct events, every one non-persistent, i.e. single-baseline slice-outs of the running median; deepest −0.38 % SAP-only at BJD 2459397.55932). A bounded null for the repeat-dip question, conditioned on sector-40's own sensitivity: 90 %-complete depths at k* = 2 are 2000 ppm (1–4 h) and 5000 ppm (8 h) — dips shallower than that per duration are not excluded by this light curve.

Prior art answered by all 4 services; TESS_TOI TOI-6675.01 PC only, no period anywhere. No candidate raised; no dossier.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6675.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 141522677 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 101.546921 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 78.50475 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459410.616258 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 1323.0928698 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 5.4653921 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 9.40853 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-01-26 12:02:43 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 40 | True | `449644592632cdc9` | True |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 19 | False | `7ab8d6e842d04235` | True |
| `tess2019357164649-s0020-0000000141522677-0165-s_lc.fits` | 20 | False | `942b121aed177c89` | True |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 26 | False | `f0e1b4f208ef5d05` | True |
| `tess2021364111932-s0047-0000000141522677-0218-s_lc.fits` | 47 | False | `16c52e9a6e8db2d4` | True |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 59 | False | `7534205b981c9611` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459410.61626 | recovered | 164 | 1249 ± 59 | 1323 | -0.09 |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | — | epoch not in this light curve | — | — | 1323 | — |
| `tess2019357164649-s0020-0000000141522677-0165-s_lc.fits` | — | epoch not in this light curve | — | — | 1323 | — |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | — | epoch not in this light curve | — | — | 1323 | — |
| `tess2021364111932-s0047-0000000141522677-0218-s_lc.fits` | — | epoch not in this light curve | — | — | 1323 | — |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | — | epoch not in this light curve | — | — | 1323 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019357164649-s0020-0000000141522677-0165-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 2000, 8h: 5000 |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021364111932-s0047-0000000141522677-0218-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 2459012.06929 | -0.00481 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 2459021.19559 | -0.00425 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 2459010.43042 | -0.00398 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 2459010.41862 | -0.00383 | 3 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459397.55932 | -0.00381 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000141522677-0188-s_lc.fits` | 2459019.79977 | -0.00352 | 2 | SAP | 1, 2, 3 | no |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2458828.99658 | -0.00335 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459397.18987 | -0.00331 | 3 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000141522677-0165-s_lc.fits` | 2458856.43549 | -0.00314 | 4 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459395.68570 | -0.00310 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459396.85932 | -0.00282 | 2 | SAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459396.96348 | -0.00282 | 2 | SAP | 2, 3 | no |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2458820.51310 | -0.00266 | 2 | SAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459396.87182 | -0.00252 | 2 | SAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459390.71416 | -0.00244 | 3 | SAP | 1 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459407.35247 | -0.00243 | 2 | SAP | 1 | no |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2458836.25639 | -0.00242 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459404.30382 | -0.00241 | 2 | SAP | 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459407.27469 | -0.00240 | 2 | PDCSAP | 1, 2 | no |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2459911.73747 | -0.00239 | 2 | SAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459397.47737 | -0.00239 | 2 | SAP | 1, 3 | no |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2458829.23964 | -0.00237 | 2 | SAP | 2, 3 | no |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2458829.07714 | -0.00234 | 2 | SAP | 3 | no |
| `tess2019331140908-s0019-0000000141522677-0164-s_lc.fits` | 2458839.20918 | -0.00233 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2459925.30719 | -0.00228 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2459936.58784 | -0.00218 | 2 | SAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2459922.62660 | -0.00211 | 2 | SAP | 1 | no |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2459936.31840 | -0.00211 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000141522677-0248-s_lc.fits` | 2459911.57774 | -0.00205 | 2 | SAP | 1 | no |
| `tess2021175071901-s0040-0000000141522677-0211-s_lc.fits` | 2459407.31913 | -0.00201 | 2 | PDCSAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6675.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:36:44Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T04:36:46Z: TOI-6675.01 (TIC 141522677, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:36:48Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T04:36:49Z: TYC 4530-25-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459410.6163: recovered, depth 1249 ± 59 ppm (catalogue 1323 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 90%, 0%, 80%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-6675-01.yaml
python -m cygnus.campaign report campaigns/toi-6675-01.yaml
```
