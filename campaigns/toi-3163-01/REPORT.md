<!-- cygnus:generated-draft -->
# Known-object test, TOI-3163.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3163-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5162, calibrate_screen #5142, event_census #5154, fetch_independent #5159, fetch_products #5129, known_signal_recovery #5146, moving_objects #5156, period_aliases #5155, prior_art #5164, residual_screen #5153, stellar_context #5147, variability_guard #5163
- Runner finished (UTC): 2026-09-30T23:05:03Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3163.01 (BJD 2460043.6013: recovered, depth 7322 ± 352 ppm (catalogue 8540 ppm); BJD 2460046.6762: recovered, depth 6923 ± 348 ppm (catalogue 8540 ppm); BJD 2460049.7512: recovered, depth 7980 ± 350 ppm (catalogue 8540 ppm); BJD 2460052.8261: recovered, depth 8586 ± 354 ppm (catalogue 8540 ppm); BJD 2460055.9010: recovered, depth 8324 ± 342 ppm (catalogue 8540 ppm); BJD 2460058.9759: recovered, depth 8904 ± 366 ppm (catalogue 8540 ppm); BJD 2460062.0508: recovered, depth 9499 ± 361 ppm (catalogue 8540 ppm); BJD 2460065.1257: recovered, depth 8010 ± 371 ppm (catalogue 8540 ppm); BJD 2461049.0991: recovered, depth 8317 ± 326 ppm (catalogue 8540 ppm); BJD 2461052.1740: recovered, depth 7101 ± 343 ppm (catalogue 8540 ppm); BJD 2461055.2490: recovered, depth 9455 ± 354 ppm (catalogue 8540 ppm); BJD 2461058.3239: gap (catalogue 8540 ppm); BJD 2461061.3988: gap (catalogue 8540 ppm); BJD 2461064.4737: recovered, depth 8898 ± 337 ppm (catalogue 8540 ppm); BJD 2461067.5486: recovered, depth 7753 ± 326 ppm (catalogue 8540 ppm); BJD 2461070.6235: recovered, depth 7901 ± 333 ppm (catalogue 8540 ppm); BJD 2461073.6985: gap (catalogue 8540 ppm); BJD 2461076.7734: recovered, depth 7656 ± 385 ppm (catalogue 8540 ppm); BJD 2461079.8483: recovered, depth 9024 ± 368 ppm (catalogue 8540 ppm); BJD 2461082.9232: recovered, depth 7688 ± 383 ppm (catalogue 8540 ppm); BJD 2461085.9981: partial, depth 8189 ± 428 ppm (catalogue 8540 ppm); BJD 2461089.0730: recovered, depth 8177 ± 366 ppm (catalogue 8540 ppm); BJD 2461092.1480: recovered, depth 6496 ± 395 ppm (catalogue 8540 ppm); BJD 2461095.2229: recovered, depth 7755 ± 392 ppm (catalogue 8540 ppm); BJD 2461098.2978: recovered, depth 7915 ± 413 ppm (catalogue 8540 ppm); BJD 2461101.3727: recovered, depth 9239 ± 391 ppm (catalogue 8540 ppm); BJD 2461104.4476: recovered, depth 8457 ± 370 ppm (catalogue 8540 ppm); BJD 2461107.5225: recovered, depth 6885 ± 379 ppm (catalogue 8540 ppm); BJD 2461110.5975: recovered, depth 7293 ± 340 ppm (catalogue 8540 ppm); BJD 2461113.6724: gap (catalogue 8540 ppm); BJD 2461116.7473: recovered, depth 7697 ± 361 ppm (catalogue 8540 ppm); BJD 2461119.8222: recovered, depth 7416 ± 378 ppm (catalogue 8540 ppm); BJD 2461122.8971: recovered, depth 7854 ± 351 ppm (catalogue 8540 ppm); BJD 2461125.9720: gap (catalogue 8540 ppm)).
Outside the catalogued epoch the screen left 19 threshold entries forming **8 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3163.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 425316308 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 191.088792 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -55.013313 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459357.894877 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.0749168 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8540.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.67 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.8232 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | lightcurve | 64 | False | `2c2beed0cb2ccf81` | True |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | lightcurve | 99 | False | `f3e50b3b965a3c28` | True |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | lightcurve | 100 | False | `6a0c5eeb47ee5339` | True |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | lightcurve | 101 | False | `493939fb9a774070` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460043.60132 | recovered | 80 | 7322 ± 352 | 8540 | 0.09 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460046.67624 | recovered | 80 | 6923 ± 348 | 8540 | 0.96 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460049.75116 | recovered | 80 | 7980 ± 350 | 8540 | -0.05 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460052.82607 | recovered | 80 | 8586 ± 354 | 8540 | 0.25 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460055.90099 | recovered | 80 | 8324 ± 342 | 8540 | 0.24 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460058.97591 | recovered | 80 | 8904 ± 366 | 8540 | -0.36 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460062.05082 | recovered | 80 | 9499 ± 361 | 8540 | -0.11 |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460065.12574 | recovered | 80 | 8010 ± 371 | 8540 | -0.57 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461049.09912 | recovered | 80 | 8317 ± 326 | 8540 | 0.53 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461052.17403 | recovered | 80 | 7101 ± 343 | 8540 | -0.35 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461055.24895 | recovered | 80 | 9455 ± 354 | 8540 | 0.14 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461058.32387 | gap | 0 | — | 8540 | — |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461061.39878 | gap | 0 | — | 8540 | — |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461064.47370 | recovered | 80 | 8898 ± 337 | 8540 | -0.07 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461067.54862 | recovered | 80 | 7753 ± 326 | 8540 | -0.13 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461070.62353 | recovered | 80 | 7901 ± 333 | 8540 | -0.07 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 2461073.69845 | gap | 0 | — | 8540 | — |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461076.77337 | recovered | 80 | 7656 ± 385 | 8540 | -0.20 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461079.84828 | recovered | 80 | 9024 ± 368 | 8540 | 0.09 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461082.92320 | recovered | 80 | 7688 ± 383 | 8540 | 0.31 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461085.99812 | partial | 81 | 8189 ± 428 | 8540 | 0.72 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461089.07304 | recovered | 80 | 8177 ± 366 | 8540 | 0.54 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461092.14795 | recovered | 80 | 6496 ± 395 | 8540 | -0.25 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461095.22287 | recovered | 80 | 7755 ± 392 | 8540 | 0.14 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461098.29779 | recovered | 80 | 7915 ± 413 | 8540 | -0.22 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461101.37270 | recovered | 81 | 9239 ± 391 | 8540 | -0.12 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461104.44762 | recovered | 80 | 8457 ± 370 | 8540 | -0.21 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461107.52254 | recovered | 80 | 6885 ± 379 | 8540 | -0.04 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461110.59745 | recovered | 80 | 7293 ± 340 | 8540 | 0.19 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461113.67237 | gap | 0 | — | 8540 | — |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461116.74729 | recovered | 80 | 7697 ± 361 | 8540 | -0.20 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461119.82220 | recovered | 77 | 7416 ± 378 | 8540 | 0.19 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461122.89712 | recovered | 80 | 7854 ± 351 | 8540 | -0.14 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461125.97204 | gap | 0 | — | 8540 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026005125623-s0099-0000000425316308-0300-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461102.93875 | -0.00906 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461112.23370 | -0.01330 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461125.25511 | -0.01249 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000425316308-0302-s_lc.fits` | 2461086.35297 | -0.01115 | 2 | PDCSAP | 1 | no |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461125.31900 | -0.01088 | 2 | PDCSAP | 3 | no |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460054.84976 | -0.00993 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000425316308-0303-s_lc.fits` | 2461101.92341 | -0.00956 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023096110322-s0064-0000000425316308-0257-s_lc.fits` | 2460054.78170 | -0.00859 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3163.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:04:52Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:04:55Z: TOI-3163.01 (TIC 425316308, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T23:04:58Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T23:05:00Z: TOI-3163 (*); TOI-3163.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460043.6013: recovered, depth 7322 ± 352 ppm (catalogue 8540 ppm); BJD 2460046.6762: recovered, depth 6923 ± 348 ppm (catalogue 8540 ppm); BJD 2460049.7512: recovered, depth 7980 ± 350 ppm (catalogue 8540 ppm); BJD 2460052.8261: recovered, depth 8586 ± 354 ppm (catalogue 8540 ppm); BJD 2460055.9010: recovered, depth 8324 ± 342 ppm (catalogue 8540 ppm); BJD 2460058.9759: recovered, depth 8904 ± 366 ppm (catalogue 8540 ppm); BJD 2460062.0508: recovered, depth 9499 ± 361 ppm (catalogue 8540 ppm); BJD 2460065.1257: recovered, depth 8010 ± 371 ppm (catalogue 8540 ppm); BJD 2461049.0991: recovered, depth 8317 ± 326 ppm (catalogue 8540 ppm); BJD 2461052.1740: recovered, depth 7101 ± 343 ppm (catalogue 8540 ppm); BJD 2461055.2490: recovered, depth 9455 ± 354 ppm (catalogue 8540 ppm); BJD 2461058.3239: gap (catalogue 8540 ppm); BJD 2461061.3988: gap (catalogue 8540 ppm); BJD 2461064.4737: recovered, depth 8898 ± 337 ppm (catalogue 8540 ppm); BJD 2461067.5486: recovered, depth 7753 ± 326 ppm (catalogue 8540 ppm); BJD 2461070.6235: recovered, depth 7901 ± 333 ppm (catalogue 8540 ppm); BJD 2461073.6985: gap (catalogue 8540 ppm); BJD 2461076.7734: recovered, depth 7656 ± 385 ppm (catalogue 8540 ppm); BJD 2461079.8483: recovered, depth 9024 ± 368 ppm (catalogue 8540 ppm); BJD 2461082.9232: recovered, depth 7688 ± 383 ppm (catalogue 8540 ppm); BJD 2461085.9981: partial, depth 8189 ± 428 ppm (catalogue 8540 ppm); BJD 2461089.0730: recovered, depth 8177 ± 366 ppm (catalogue 8540 ppm); BJD 2461092.1480: recovered, depth 6496 ± 395 ppm (catalogue 8540 ppm); BJD 2461095.2229: recovered, depth 7755 ± 392 ppm (catalogue 8540 ppm); BJD 2461098.2978: recovered, depth 7915 ± 413 ppm (catalogue 8540 ppm); BJD 2461101.3727: recovered, depth 9239 ± 391 ppm (catalogue 8540 ppm); BJD 2461104.4476: recovered, depth 8457 ± 370 ppm (catalogue 8540 ppm); BJD 2461107.5225: recovered, depth 6885 ± 379 ppm (catalogue 8540 ppm); BJD 2461110.5975: recovered, depth 7293 ± 340 ppm (catalogue 8540 ppm); BJD 2461113.6724: gap (catalogue 8540 ppm); BJD 2461116.7473: recovered, depth 7697 ± 361 ppm (catalogue 8540 ppm); BJD 2461119.8222: recovered, depth 7416 ± 378 ppm (catalogue 8540 ppm); BJD 2461122.8971: recovered, depth 7854 ± 351 ppm (catalogue 8540 ppm); BJD 2461125.9720: gap (catalogue 8540 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3163.01: Gaia DR3 6073589158249558400 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3163.01: Teff 6008 K, R* 1.39 ± 0.11, M* 1.27 ± 0.13, ρ* 0.48 ± 0.12 ρ☉ (dwarf sequence, M_G 3.49, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3163.01: 83 Gaia neighbour(s) within 52.5", contamination 38.35%; depth 7322 ppm (measured depth of the recovered catalogued transit); 10 could produce it if fully eclipsed (brightest 6073589123889816704, 42.9", ΔG 1.71); a centroid test is needed |
| Pointing and quality census per event | passed | 1 persistent event(s), 1 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3163.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3163.01: TOI-3163 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3163-01.yaml
python -m cygnus.multi report campaigns/toi-3163-01.yaml
```
