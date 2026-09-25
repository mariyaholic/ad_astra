# Known-object test, TOI-1772.02

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-1772-02.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #225, fetch_products #224, known_signal_recovery #226, period_aliases #228, prior_art #229, residual_screen #227
- Runner finished (UTC): 2026-09-25T03:57:14Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1772.02 (BJD 2459618.7076: recovered, depth 3322 ± 60 ppm (catalogue 2163 ppm)).
Outside the catalogued epoch the screen left 270 threshold entries forming **127 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **passed**: the sector-48 profile (`sector48/normalized_series.csv`) shows a dip
centred on the catalogued epoch (BJD 2459618.7076), recovered at 3322 ± 60 ppm against a catalogue
depth of 2163 ppm — the usual dilution-style excess. No repeat candidate was raised
(`period_aliases` `not_tested`).

The four persistent events were checked by hand and none is transit-like:

- **2459620.84280 (sector 48)** — the PDCSAP binned profile oscillates around zero with no coherent
  dip; only SAP shows structure, and the two disagree. Nearest-excursion centroid residual
  MOM_CENTR2 +0.0154 px against sd 0.0191 (≈ 0.8σ).
- **2459615.00107 (sector 48)** — SAP shows a broad ~1500–2500 ppm depression while PDCSAP stays flat,
  i.e. a SAP/PDCSAP disagreement, the signature of a reduction/instrument systematic rather than a
  transit. Centroid residual ≤ 1σ.
- **2459621.39697 (sector 48)** and **2458888.09727 (sector 21)** — same pattern (broad, non-flat,
  SAP-dominated); at 2458888.09727 the MOM_CENTR2 residual is −0.0376 px against sd 0.0143 (≈ 2.6σ),
  a pointing excursion accompanying the dip rather than a flat-bottomed transit.

Read as systematics; nothing is advanced and each event remains at most an unverified lead. Catalogue
cross-match answered by all four services.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1772.02 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 85293053 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 156.837704 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 34.39095 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459618.707643 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 2162.8449313 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 5.3489749 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 9.3523 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2022-03-25 12:02:08 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 48 | True | `4fcf934ba269cf0e` | True |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 21 | False | `a408636ddac0816e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459618.70764 | recovered | 161 | 3322 ± 60 | 2163 | 0.03 |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | — | epoch not in this light curve | — | — | 2163 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 2000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458888.09727 | -0.00332 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.84280 | -0.00324 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.39697 | -0.00239 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459615.00107 | -0.00215 | 2 | PDCSAP+SAP | 1, 3 | yes |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.61356 | -0.00532 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.21633 | -0.00525 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.38439 | -0.00523 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.94719 | -0.00510 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458891.23341 | -0.00481 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.16077 | -0.00459 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.74967 | -0.00451 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.96247 | -0.00450 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.50661 | -0.00449 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.81247 | -0.00440 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458887.91393 | -0.00437 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.35808 | -0.00427 | 3 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.53161 | -0.00421 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.38994 | -0.00403 | 4 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.36217 | -0.00397 | 4 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.48995 | -0.00393 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.66773 | -0.00390 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.29975 | -0.00388 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.34703 | -0.00388 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.78995 | -0.00386 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.03313 | -0.00383 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.56787 | -0.00373 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.10461 | -0.00371 | 3 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.28994 | -0.00370 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.76495 | -0.00370 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.46926 | -0.00366 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.10397 | -0.00362 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.88191 | -0.00351 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.24425 | -0.00350 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.37328 | -0.00349 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.25814 | -0.00347 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.18341 | -0.00346 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.27647 | -0.00344 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.53717 | -0.00339 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.15531 | -0.00338 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.49996 | -0.00338 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.78301 | -0.00337 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.04966 | -0.00336 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.10869 | -0.00335 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458896.92369 | -0.00333 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.77884 | -0.00331 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.32397 | -0.00331 | 3 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459613.43992 | -0.00329 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.21216 | -0.00329 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.29981 | -0.00328 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.74273 | -0.00327 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.24003 | -0.00326 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.35244 | -0.00326 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459613.58854 | -0.00325 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458896.70008 | -0.00325 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458887.84587 | -0.00319 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.71364 | -0.00319 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.08202 | -0.00318 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.27883 | -0.00317 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.25424 | -0.00316 | 6 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.70691 | -0.00315 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.39703 | -0.00314 | 4 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.50691 | -0.00314 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458891.37299 | -0.00313 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.23897 | -0.00313 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.86455 | -0.00313 | 3 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.09688 | -0.00313 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.57614 | -0.00312 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.14286 | -0.00312 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.71802 | -0.00312 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.58717 | -0.00310 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.33300 | -0.00310 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.45537 | -0.00309 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.05660 | -0.00309 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458896.99730 | -0.00307 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.24842 | -0.00305 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.14003 | -0.00305 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.04036 | -0.00300 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.50120 | -0.00299 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.58523 | -0.00299 | 3 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.87636 | -0.00298 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.54411 | -0.00296 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.05563 | -0.00293 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458875.96646 | -0.00293 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.73586 | -0.00291 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.03619 | -0.00291 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.14419 | -0.00290 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.63454 | -0.00288 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.25808 | -0.00287 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.52614 | -0.00286 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.95830 | -0.00285 | 2 | SAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.59550 | -0.00285 | 3 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.53870 | -0.00284 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.41494 | -0.00282 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.34697 | -0.00282 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.14036 | -0.00280 | 4 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.57482 | -0.00280 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.72884 | -0.00278 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459613.38576 | -0.00278 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458896.88897 | -0.00276 | 4 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.14550 | -0.00276 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.27230 | -0.00276 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.46217 | -0.00271 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.66217 | -0.00270 | 3 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.07369 | -0.00269 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.47467 | -0.00269 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458896.65355 | -0.00268 | 3 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.55661 | -0.00267 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458897.16675 | -0.00265 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.75523 | -0.00264 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.25105 | -0.00262 | 4 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458875.94285 | -0.00262 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.79003 | -0.00258 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.39281 | -0.00253 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.49287 | -0.00250 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.39718 | -0.00248 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.04272 | -0.00248 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.71009 | -0.00245 | 3 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459614.29966 | -0.00243 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458876.17828 | -0.00243 | 3 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458882.88747 | -0.00238 | 2 | SAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459620.05530 | -0.00237 | 2 | SAP | 1, 2 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458890.30007 | -0.00235 | 2 | SAP | 1 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.31294 | -0.00233 | 3 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459621.27058 | -0.00226 | 2 | PDCSAP | 2 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459610.17179 | -0.00220 | 2 | PDCSAP | 3 | no |
| `tess2022027120115-s0048-0000000085293053-0219-s_lc.fits` | 2459632.59278 | -0.00209 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000085293053-0167-s_lc.fits` | 2458887.90004 | -0.00200 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1772.02**

- NASA_Exoplanet_Archive (done, 2026-09-25): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-25T03:57:03Z: TOI-1772.01 (host TOI-1772)
- TESS_TOI (done, 2026-09-25): 2 match(es) in TESS_TOI within 30" as of 2026-09-25T03:57:08Z: TOI-1772.01 (TIC 85293053, disposition CP); TOI-1772.02 (TIC 85293053, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T03:57:11Z
- SIMBAD (done, 2026-09-25): 4 match(es) in SIMBAD within 30" as of 2026-09-25T03:57:12Z: BD+35  2144B (*); TOI-1772.02 (Pl?); BD+35  2144 (Em*); TOI-1772.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459618.7076: recovered, depth 3322 ± 60 ppm (catalogue 2163 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 80%, 90% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-1772-02.yaml
python -m cygnus.campaign report campaigns/toi-1772-02.yaml
```
