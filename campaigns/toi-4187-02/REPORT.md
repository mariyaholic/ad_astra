# Known-object test, TOI-4187.02

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-4187-02.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #327, fetch_products #326, known_signal_recovery #328, period_aliases #330, prior_art #331, residual_screen #329
- Runner finished (UTC): 2026-09-25T04:35:33Z

## Bottom line

Positive control **failed**: BJD 2460939.1181: not recovered, depth 591 ± 23 ppm (catalogue 534 ppm).
Outside the catalogued epoch the screen left 185 threshold entries forming **82 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** with the epoch covered (sector 97, 381 usable in-transit cadences; 0 flagged cadences). Two readings, both from the runner's outputs:

- Sensitivity first: at sector 97's k* = 3.5 the calibrated 90 %-completeness depth is 2000 ppm for every duration — four times the catalogue depth (534 ppm over 12.70 h), so the gate could never clear even a present transit of catalogue depth; failure formal, not astrophysical evidence.
- The direct measurement is concordant: 591 ± 23 ppm at the epoch (ratio 1.10), i.e. a dip consistent with the catalogue depth exists at the catalogue epoch (like toi-1893-01 above, tied to a soft ≥4 h-depression-reading through the 12.7 h wrap).

Hand checks on the two persistent screen events:

| Event (BJD) | Shape | Quality/gaps | Centroid | Verdict |
|---|---|---|---|---|
| 2461222.38482 (S105, −0.31 %/3 cad) | ≥0.4 d continuous soft depression (−0.02…−0.15 ppt over ~60 bins, slightly deeper core near the event), SAP mirrors | 0 flags/216, max gap 2 min | col −0.0013 vs 0.0038 (≈0.3σ); row +0.0262 vs 0.0296 (≈0.9σ) | long-timescale trend wrapped by the merging windows; systematic class |
| 2459166.56206 (S31, −0.13 %/2 cad) | 20-min binned PDCSAP ±0.15 d: scatter ±~0.4 ppt round a mild soft trough (−0.02…−0.06 ppt), deepest bin −0.57 ppt, no sharp minimum | 0 flags/216, max gap 2 min | col −0.0067 vs 0.0040 (≈1.7σ); row +0.0071 vs 0.0064 (≈1.1σ) | shallow 2-cadence sweep layered on a soft trough; not transit-shaped; not vetted |

Prior art answered by all 4 services: TESS_TOI lists TOI-4187.01 PC and .02 PC on the same TIC (a multi-signal host, so mutual blends are live); SIMBAD HD 20143 (PM*) is the host. The deepest patch in S105 is ~3× deeper than the catalogue depth — a systematic signature, not a repeat candidate (no reference block: PC not recovered).

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4187.02 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 176780257 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 48.283944 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -34.375416 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2460939.118107 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 534.3464628 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 12.7019393 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 8.301 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2026-07-25 12:04:08 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 97 | True | `d83912fb0e28515b` | True |
| `tess2018292075959-s0004-0000000176780257-0124-s_lc.fits` | 4 | False | `f4e89ff85983cbd8` | True |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | 30 | False | `a4b8d0df425ff5cd` | True |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 31 | False | `9b05642a752ca73a` | True |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 105 | False | `702db0fe13f27a91` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460939.11811 | not_recovered | 381 | 591 ± 23 | 534 | — |
| `tess2018292075959-s0004-0000000176780257-0124-s_lc.fits` | — | epoch not in this light curve | — | — | 534 | — |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | — | epoch not in this light curve | — | — | 534 | — |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | — | epoch not in this light curve | — | — | 534 | — |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | — | epoch not in this light curve | — | — | 534 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2018292075959-s0004-0000000176780257-0124-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 1000, 8h: 1000 |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.38482 | -0.00305 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459166.56206 | -0.00132 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461230.85617 | -0.00444 | 4 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.57661 | -0.00390 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.84399 | -0.00367 | 3 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.69329 | -0.00354 | 3 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461225.16971 | -0.00349 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461231.28814 | -0.00347 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.32243 | -0.00346 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.23909 | -0.00323 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460981.15399 | -0.00322 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.82663 | -0.00321 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461231.15479 | -0.00312 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460967.47763 | -0.00297 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.04543 | -0.00295 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.02936 | -0.00294 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461225.49542 | -0.00292 | 3 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461225.25999 | -0.00289 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461230.64226 | -0.00280 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.66927 | -0.00279 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.36650 | -0.00275 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460981.37205 | -0.00274 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460940.93961 | -0.00274 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.53316 | -0.00274 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461224.62523 | -0.00272 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461230.53948 | -0.00267 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460967.40124 | -0.00259 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461218.59156 | -0.00257 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.24289 | -0.00253 | 3 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461230.78255 | -0.00250 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461230.86450 | -0.00248 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461231.91039 | -0.00240 | 2 | SAP | 2 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461231.99929 | -0.00238 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461221.79450 | -0.00232 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461225.64751 | -0.00230 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.70816 | -0.00229 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.61233 | -0.00221 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.09150 | -0.00221 | 2 | SAP | 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.20931 | -0.00214 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.02299 | -0.00212 | 3 | SAP | 2 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460981.54427 | -0.00208 | 2 | SAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459163.45379 | -0.00206 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459164.16489 | -0.00205 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.15261 | -0.00205 | 2 | SAP | 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461217.00258 | -0.00203 | 2 | SAP | 1 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459162.55937 | -0.00203 | 2 | SAP | 1, 2, 3 | no |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | 2459132.58163 | -0.00198 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460981.62760 | -0.00197 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460967.48944 | -0.00195 | 3 | SAP | 2, 3 | no |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | 2459139.86365 | -0.00191 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460967.38596 | -0.00189 | 2 | SAP | 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.17459 | -0.00187 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.01535 | -0.00184 | 2 | PDCSAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000176780257-0294-s_lc.fits` | 2460980.02622 | -0.00183 | 2 | SAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.14612 | -0.00182 | 3 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459164.99126 | -0.00181 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.10098 | -0.00180 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459164.98640 | -0.00171 | 3 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.32926 | -0.00170 | 2 | PDCSAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459164.90932 | -0.00167 | 2 | SAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459162.84131 | -0.00163 | 2 | SAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.19265 | -0.00163 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.31815 | -0.00161 | 2 | PDCSAP | 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.38570 | -0.00160 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.02785 | -0.00159 | 2 | PDCSAP | 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.33620 | -0.00159 | 2 | PDCSAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.01765 | -0.00153 | 2 | SAP | 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459150.90533 | -0.00153 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459162.60659 | -0.00152 | 2 | SAP | 1, 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461207.41734 | -0.00151 | 2 | PDCSAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459164.87321 | -0.00150 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461207.50763 | -0.00150 | 2 | PDCSAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.22925 | -0.00150 | 2 | PDCSAP | 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461222.05841 | -0.00149 | 2 | PDCSAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.37875 | -0.00148 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459165.11070 | -0.00145 | 2 | SAP | 2, 3 | no |
| `tess2026164183000-s0105-0000000176780257-0307-s_lc.fits` | 2461207.34651 | -0.00145 | 2 | PDCSAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459166.29123 | -0.00143 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459162.21354 | -0.00141 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459161.82743 | -0.00138 | 2 | SAP | 1, 2 | no |
| `tess2020266004630-s0030-0000000176780257-0195-s_lc.fits` | 2459135.43584 | -0.00137 | 2 | PDCSAP | 3 | no |
| `tess2020294194027-s0031-0000000176780257-0198-s_lc.fits` | 2459150.80811 | -0.00135 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4187.02**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:35:27Z
- TESS_TOI (done, 2026-09-25): 2 match(es) in TESS_TOI within 30" as of 2026-09-25T04:35:29Z: TOI-4187.01 (TIC 176780257, disposition PC); TOI-4187.02 (TIC 176780257, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:35:30Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T04:35:31Z: HD  20143 (PM*); TOI-4187.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2460939.1181: not recovered, depth 591 ± 23 ppm (catalogue 534 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 4, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 90%, 100%, 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-4187-02.yaml
python -m cygnus.campaign report campaigns/toi-4187-02.yaml
```
