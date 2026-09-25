# Known-object test, TOI-4309.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The covered control formally failed at BJD 2458564.6105 (65 usable cadences), with measured depth 207 ± 95 ppm vs catalogue 661 ppm. At k* = 3 the 90%-completeness floor is 5000 ppm across the tabulated duration grid, so a 2.16-h, 661-ppm transit is below sensitivity. This is a sensitivity-limited gate failure, not evidence against the epoch; thresholds were not tuned. Next: compare the epoch with SPOC DV/TOI records and an independent reduction sensitive to sub-1000-ppm dips.


- Campaign spec: `campaigns/toi-4309-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #532, fetch_products #531, known_signal_recovery #533, period_aliases #535, prior_art #536, residual_screen #534
- Runner finished (UTC): 2026-09-25T05:58:50Z

## Bottom line

Positive control **failed**: BJD 2458564.6105: not recovered, depth 207 ± 95 ppm (catalogue 661 ppm).
Outside the catalogued epoch the screen left 138 threshold entries forming **78 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** at the covered sector-9 epoch (65 usable cadences; QUALITY=0, max gap 2 min): measured 207 ± 95 ppm vs catalogue 661 ppm (ratio 0.31). The 90%-completeness depth at k* = 3 is 5000 ppm for the tabulated 1–8-h durations, far above this 2.16-h signal; the gate is under-sensitive here. Do not infer a wrong epoch from the failure.

The single persistent entry is BJD 2459992.18013 in sector 62 (2 cadences, −0.23%); its binned SAP/PDCSAP profile is scatter-level with no local transit shape. QUALITY=0, max gap 2 min, and centroid residuals (col −0.0051 vs 0.0043 px scatter; row −0.0025 vs 0.0038 px) show no compelling shift. It is not a repeat candidate. Other entries are short single-flux events; no VSX variable match. Difference images, pointing and alternate detrending remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4309.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 56662591 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 158.578516 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -9.162846 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458564.610546 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 661.1667085 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 2.1563739 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 9.456101 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2025-09-04 16:00:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 9 | True | `66a6dd7abaf22ddf` | True |
| `tess2021039152502-s0035-0000000056662591-0205-s_lc.fits` | 35 | False | `922dca73392858bf` | True |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 62 | False | `ac144e898373dfde` | True |
| `tess2025042113628-s0089-0000000056662591-0286-s_lc.fits` | 89 | False | `ba0020ec86165f1e` | True |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 100 | False | `bdc3fe7c8f3bcd39` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 2458564.61055 | not_recovered | 65 | 207 ± 95 | 661 | — |
| `tess2021039152502-s0035-0000000056662591-0205-s_lc.fits` | — | epoch not in this light curve | — | — | 661 | — |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 661 | — |
| `tess2025042113628-s0089-0000000056662591-0286-s_lc.fits` | — | epoch not in this light curve | — | — | 661 | — |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 661 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021039152502-s0035-0000000056662591-0205-s_lc.fits` | 3 | False | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2025042113628-s0089-0000000056662591-0286-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 2000, 8h: 5000 |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2459992.18013 | -0.00226 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.53064 | -0.00523 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.40911 | -0.00497 | 3 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.85843 | -0.00489 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.15008 | -0.00476 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.79593 | -0.00472 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.18411 | -0.00421 | 5 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.85009 | -0.00417 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.81954 | -0.00415 | 4 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.83690 | -0.00411 | 3 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.19981 | -0.00408 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.74454 | -0.00402 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.11300 | -0.00395 | 5 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.43897 | -0.00393 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.11258 | -0.00392 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.27508 | -0.00390 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.14453 | -0.00388 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.29800 | -0.00388 | 3 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.24592 | -0.00372 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.97133 | -0.00372 | 3 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.30884 | -0.00365 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.38342 | -0.00363 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.34495 | -0.00354 | 3 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.93731 | -0.00353 | 4 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.82342 | -0.00349 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.76786 | -0.00346 | 2 | SAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 2458560.30726 | -0.00344 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.20953 | -0.00336 | 9 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.18314 | -0.00334 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.13870 | -0.00328 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.19564 | -0.00321 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.90397 | -0.00320 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.36953 | -0.00320 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461092.78063 | -0.00319 | 2 | SAP | 3 | no |
| `tess2026033082000-s0100-0000000056662591-0302-s_lc.fits` | 2461093.08827 | -0.00313 | 3 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.01647 | -0.00312 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.15189 | -0.00312 | 3 | SAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 2458558.50451 | -0.00311 | 2 | SAP | 2 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.87342 | -0.00308 | 3 | SAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 2458558.52395 | -0.00308 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.02203 | -0.00304 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.01231 | -0.00302 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000056662591-0205-s_lc.fits` | 2459266.10697 | -0.00296 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.86231 | -0.00295 | 4 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.27481 | -0.00289 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.25953 | -0.00283 | 6 | SAP | 1, 2, 3 | no |
| `tess2025042113628-s0089-0000000056662591-0286-s_lc.fits` | 2460725.51132 | -0.00283 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.03592 | -0.00279 | 4 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.05814 | -0.00276 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.05258 | -0.00274 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.32620 | -0.00274 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.88036 | -0.00270 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460013.36091 | -0.00269 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000056662591-0205-s_lc.fits` | 2459255.85805 | -0.00268 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.89703 | -0.00266 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.35120 | -0.00266 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.85328 | -0.00266 | 3 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.23731 | -0.00265 | 4 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.94842 | -0.00264 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000056662591-0139-s_lc.fits` | 2458558.27257 | -0.00263 | 2 | PDCSAP | 1 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.66786 | -0.00257 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460013.35466 | -0.00256 | 5 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.06786 | -0.00254 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.16231 | -0.00253 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.10536 | -0.00252 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.29425 | -0.00246 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.17620 | -0.00245 | 4 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.32134 | -0.00244 | 3 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460013.32202 | -0.00243 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.12897 | -0.00242 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.98314 | -0.00241 | 3 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.07620 | -0.00237 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.74842 | -0.00236 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460006.53730 | -0.00231 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.31439 | -0.00226 | 3 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.00536 | -0.00225 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2460007.26856 | -0.00212 | 3 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000056662591-0254-s_lc.fits` | 2459989.76061 | -0.00200 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4309.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:58:45Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:58:46Z: TOI-4309.01 (TIC 56662591, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:58:48Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:58:49Z: BD-08  2955 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2458564.6105: not recovered, depth 207 ± 95 ppm (catalogue 661 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 50%, 100%, 90%, 40% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-4309-01.yaml
python -m cygnus.campaign report campaigns/toi-4309-01.yaml
```
