# Known-object test, TOI-2087.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-2087-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #406, fetch_products #405, known_signal_recovery #407, period_aliases #409, prior_art #410, residual_screen #408
- Runner finished (UTC): 2026-09-25T05:35:58Z

## Bottom line

Positive control **inconclusive**: BJD 2458709.1291: partial, depth 536 ± 51 ppm (catalogue 548 ppm).
Outside the catalogued epoch the screen left 160 threshold entries forming **64 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control is **inconclusive/partial** at BJD 2458709.1291 (sector 14): measured 536 ± 51 ppm vs catalogue 548 ppm, but the runner marks the 16.10-h event partial (483 usable cadences; nearest entry offset +6.63 h). QUALITY=0 and max gap is 2 min in the local window, but the reported state remains partial. At k* = 2, the 90%-completeness floor is 5000 ppm for every tabulated duration (up to 8 h); a 548-ppm signal cannot be excluded or robustly recovered by this screen.

The one persistent event (BJD 2458889.43707, sector 21, 2 cadences, −0.41%) is a short SAP/PDCSAP excursion. Its ±0.15-d bins show scatter without a distinct transit profile; quality is 0, max gap 2 min, and centroid residuals are small relative to scatter (col −0.0026 vs 0.0024 px; row −0.0031 vs 0.0129 px). Treat as a noise/systematics feature, not a repeat candidate. Other screen events are non-persistent and mostly two-cadence SAP entries. All four catalogue services answered; no VSX variable match. Pixel, pointing and alternate-reduction checks remain not tested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2087.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 219462190 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 208.052955 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 75.165261 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458709.129054 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 548.082765 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 16.0960466 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.0537 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2026-07-17 12:03:25 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 14 | True | `0351b82dea182e82` | True |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 15 | False | `92a60d0ad681e237` | True |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 20 | False | `1c1072fe4ad24827` | True |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 21 | False | `62f438fa4788962e` | True |
| `tess2020049080258-s0022-0000000219462190-0174-s_lc.fits` | 22 | False | `74c660031bc89596` | True |
| `tess2021175071901-s0040-0000000219462190-0211-s_lc.fits` | 40 | False | `7aab7ce6c124d185` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458709.12905 | partial | 483 | 536 ± 51 | 548 | 6.63 |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | — | epoch not in this light curve | — | — | 548 | — |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | — | epoch not in this light curve | — | — | 548 | — |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | — | epoch not in this light curve | — | — | 548 | — |
| `tess2020049080258-s0022-0000000219462190-0174-s_lc.fits` | — | epoch not in this light curve | — | — | 548 | — |
| `tess2021175071901-s0040-0000000219462190-0211-s_lc.fits` | — | epoch not in this light curve | — | — | 548 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 2000, 8h: 5000 |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020049080258-s0022-0000000219462190-0174-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021175071901-s0040-0000000219462190-0211-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458889.43707 | -0.00405 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458856.43557 | -0.00587 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458894.49398 | -0.00567 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458697.52059 | -0.00554 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458687.85118 | -0.00531 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458887.57458 | -0.00522 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458856.77169 | -0.00510 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458888.24125 | -0.00503 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458862.48564 | -0.00494 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458887.91069 | -0.00493 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458737.17797 | -0.00486 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458897.23561 | -0.00466 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458891.36970 | -0.00465 | 3 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458697.75809 | -0.00463 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458683.47065 | -0.00449 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458895.43980 | -0.00436 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458894.52036 | -0.00432 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458684.87342 | -0.00426 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458862.27870 | -0.00426 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458696.34698 | -0.00417 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458866.25651 | -0.00405 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458897.49672 | -0.00403 | 2 | SAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458712.73037 | -0.00403 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458691.75532 | -0.00399 | 2 | SAP | 1, 2, 3 | no |
| `tess2020049080258-s0022-0000000219462190-0174-s_lc.fits` | 2458915.89780 | -0.00393 | 2 | SAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458695.73726 | -0.00387 | 2 | SAP | 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458856.65780 | -0.00385 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458857.10086 | -0.00385 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458887.17598 | -0.00383 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458683.62621 | -0.00382 | 2 | SAP | 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458737.22102 | -0.00380 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458737.15852 | -0.00379 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458887.53153 | -0.00373 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458896.76062 | -0.00369 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458688.88173 | -0.00364 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458736.94185 | -0.00361 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458693.44004 | -0.00359 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458856.47377 | -0.00357 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458887.47389 | -0.00357 | 3 | SAP | 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458856.48696 | -0.00356 | 4 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458876.55933 | -0.00354 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000219462190-0167-s_lc.fits` | 2458896.96687 | -0.00354 | 3 | SAP | 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458859.80645 | -0.00352 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458697.96087 | -0.00348 | 2 | SAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458728.29029 | -0.00345 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458736.91963 | -0.00342 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458737.24186 | -0.00338 | 4 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458684.11648 | -0.00337 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458683.61510 | -0.00336 | 2 | SAP | 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458721.34158 | -0.00333 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458719.63739 | -0.00330 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458697.51365 | -0.00329 | 2 | SAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458728.34446 | -0.00324 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458711.51786 | -0.00320 | 2 | SAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458737.40019 | -0.00316 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458737.34186 | -0.00314 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458736.96129 | -0.00314 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458736.93629 | -0.00312 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458734.86958 | -0.00310 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458683.46649 | -0.00310 | 2 | PDCSAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000219462190-0151-s_lc.fits` | 2458736.95296 | -0.00297 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458856.72724 | -0.00283 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000219462190-0150-s_lc.fits` | 2458683.52065 | -0.00274 | 2 | PDCSAP | 3 | no |
| `tess2019357164649-s0020-0000000219462190-0165-s_lc.fits` | 2458848.17850 | -0.00260 | 2 | PDCSAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2087.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:35:53Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:35:55Z: TOI-2087.01 (TIC 219462190, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:35:56Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T05:35:57Z: TOI-2087.01 (Pl?); BD+75   522 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2458709.1291: partial, depth 536 ± 51 ppm (catalogue 548 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 80%, 90%, 40%, 30%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2087-01.yaml
python -m cygnus.campaign report campaigns/toi-2087-01.yaml
```
