<!-- cygnus:generated-draft -->
# Known-object test, TOI-2223.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2223-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4826, calibrate_screen #4792, event_census #4797, fetch_independent #4817, fetch_products #4787, known_signal_recovery #4793, moving_objects #4816, period_aliases #4798, prior_art #4829, residual_screen #4795, stellar_context #4794, variability_guard #4827
- Runner finished (UTC): 2026-09-30T22:27:26Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2223.01 (BJD 2459365.1469: recovered, depth 5497 ± 249 ppm (catalogue 6887 ppm); BJD 2459372.0778: recovered, depth 5268 ± 247 ppm (catalogue 6887 ppm); BJD 2459379.0088: not recovered, depth 5390 ± 259 ppm (catalogue 6887 ppm); BJD 2459385.9398: recovered, depth 6320 ± 251 ppm (catalogue 6887 ppm); BJD 2459039.3915: recovered, depth 5524 ± 251 ppm (catalogue 6887 ppm); BJD 2459046.3225: recovered, depth 5520 ± 270 ppm (catalogue 6887 ppm); BJD 2459053.2534: recovered, depth 5616 ± 251 ppm (catalogue 6887 ppm); BJD 2459060.1844: gap (catalogue 6887 ppm); BJD 2459067.1154: not recovered, depth 5400 ± 285 ppm (catalogue 6887 ppm); BJD 2459074.0463: gap (catalogue 6887 ppm); BJD 2459080.9773: partial, depth 4583 ± 268 ppm (catalogue 6887 ppm); BJD 2460099.8292: recovered, depth 5465 ± 242 ppm (catalogue 6887 ppm); BJD 2460106.7602: recovered, depth 6423 ± 260 ppm (catalogue 6887 ppm); BJD 2460113.6912: not recovered, depth 5268 ± 232 ppm (catalogue 6887 ppm); BJD 2460120.6221: recovered, depth 4452 ± 257 ppm (catalogue 6887 ppm); BJD 2460155.2770: recovered, depth 7450 ± 276 ppm (catalogue 6887 ppm); BJD 2460162.2079: recovered, depth 5003 ± 274 ppm (catalogue 6887 ppm); BJD 2460169.1389: recovered, depth 6234 ± 288 ppm (catalogue 6887 ppm); BJD 2460176.0699: recovered, depth 6235 ± 263 ppm (catalogue 6887 ppm); BJD 2460834.5116: recovered, depth 5657 ± 245 ppm (catalogue 6887 ppm); BJD 2460841.4426: not recovered, depth 968 ± 505 ppm (catalogue 6887 ppm); BJD 2460848.3735: partial, depth 5571 ± 237 ppm (catalogue 6887 ppm); BJD 2460855.3045: gap (catalogue 6887 ppm)).
Outside the catalogued epoch the screen left 34 threshold entries forming **12 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460165.5094 matches the catalogued transit's depth (4240 vs 5497 ppm), 800.390 d later; 7 of 800 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2223.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 273695332 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 18.689893 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -81.982165 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459365.146877 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 6.9309657 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6887.4200394 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.2921448 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.0599 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-01 12:02:56 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | lightcurve | 39 | True | `7473b9ea8fe2607d` | True |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | lightcurve | 27 | False | `d5f9ff567e5688bf` | True |
| `tess2020212050318-s0028-0000000273695332-0190-s_lc.fits` | lightcurve | 28 | False | `d06d1a9ace629fdb` | True |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | lightcurve | 66 | False | `160ec88c7030491d` | True |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | lightcurve | 68 | False | `b5b2abff2b175e94` | True |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | lightcurve | 93 | False | `04b5e9f26e7536ab` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | 2459365.14688 | recovered | 159 | 5497 ± 249 | 6887 | -0.65 |
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | 2459372.07784 | recovered | 159 | 5268 ± 247 | 6887 | -0.09 |
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | 2459379.00881 | not_recovered | 159 | 5390 ± 259 | 6887 | — |
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | 2459385.93977 | recovered | 158 | 6320 ± 251 | 6887 | -0.34 |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | 2459039.39149 | recovered | 158 | 5524 ± 251 | 6887 | -0.07 |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | 2459046.32245 | recovered | 159 | 5520 ± 270 | 6887 | -0.08 |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | 2459053.25342 | recovered | 159 | 5616 ± 251 | 6887 | 0.28 |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | 2459060.18439 | gap | 0 | — | 6887 | — |
| `tess2020212050318-s0028-0000000273695332-0190-s_lc.fits` | 2459067.11535 | not_recovered | 159 | 5400 ± 285 | 6887 | — |
| `tess2020212050318-s0028-0000000273695332-0190-s_lc.fits` | 2459074.04632 | gap | 0 | — | 6887 | — |
| `tess2020212050318-s0028-0000000273695332-0190-s_lc.fits` | 2459080.97728 | partial | 158 | 4583 ± 268 | 6887 | 1.67 |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | 2460099.82924 | recovered | 157 | 5465 ± 242 | 6887 | -1.63 |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | 2460106.76021 | recovered | 158 | 6423 ± 260 | 6887 | -0.34 |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | 2460113.69117 | not_recovered | 159 | 5268 ± 232 | 6887 | — |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | 2460120.62214 | recovered | 159 | 4452 ± 257 | 6887 | 0.70 |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460155.27697 | recovered | 158 | 7450 ± 276 | 6887 | 0.02 |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460162.20793 | recovered | 159 | 5003 ± 274 | 6887 | -1.01 |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460169.13890 | recovered | 159 | 6234 ± 288 | 6887 | -0.49 |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460176.06986 | recovered | 159 | 6235 ± 263 | 6887 | -0.81 |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | 2460834.51161 | recovered | 159 | 5657 ± 245 | 6887 | 0.08 |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | 2460841.44257 | not_recovered | 40 | 968 ± 505 | 6887 | — |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | 2460848.37354 | partial | 159 | 5571 ± 237 | 6887 | 0.83 |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | 2460855.30450 | gap | 0 | — | 6887 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021146024351-s0039-0000000273695332-0210-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020186164531-s0027-0000000273695332-0189-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020212050318-s0028-0000000273695332-0190-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2023153011303-s0066-0000000273695332-0260-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025154050500-s0093-0000000273695332-0290-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460165.50940 | -0.01090 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460179.42509 | -0.01080 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460179.44592 | -0.01061 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460165.46704 | -0.01092 | 2 | SAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460174.37521 | -0.01051 | 2 | SAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460179.36814 | -0.01020 | 2 | PDCSAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460174.19466 | -0.01014 | 2 | SAP | 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460179.47509 | -0.00998 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460179.22370 | -0.00900 | 2 | SAP | 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460179.43203 | -0.00898 | 2 | SAP | 1, 2, 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460174.45854 | -0.00879 | 2 | SAP | 3 | no |
| `tess2023209231226-s0068-0000000273695332-0262-s_lc.fits` | 2460165.57120 | -0.00863 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460165.50940 | 4240 | 5497 | 800.3896 | 7 / 800 | 800.39, 400.195, 266.796, 200.097, 88.9322, 72.7627, 27.5996 |
| 2460179.42509 | 5602 | 5497 | 814.3053 | 8 / 814 | 814.305, 407.153, 271.435, 203.576, 135.718, 116.329, 90.4784, 45.2392 |
| 2460179.44592 | 5836 | 5497 | 814.3261 | 8 / 814 | 814.326, 407.163, 271.442, 203.582, 135.721, 116.332, 90.4807, 45.2403 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2223.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:27:07Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:27:10Z: TOI-2223.01 (TIC 273695332, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:27:12Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:27:14Z: TOI-2223 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459365.1469: recovered, depth 5497 ± 249 ppm (catalogue 6887 ppm); BJD 2459372.0778: recovered, depth 5268 ± 247 ppm (catalogue 6887 ppm); BJD 2459379.0088: not recovered, depth 5390 ± 259 ppm (catalogue 6887 ppm); BJD 2459385.9398: recovered, depth 6320 ± 251 ppm (catalogue 6887 ppm); BJD 2459039.3915: recovered, depth 5524 ± 251 ppm (catalogue 6887 ppm); BJD 2459046.3225: recovered, depth 5520 ± 270 ppm (catalogue 6887 ppm); BJD 2459053.2534: recovered, depth 5616 ± 251 ppm (catalogue 6887 ppm); BJD 2459060.1844: gap (catalogue 6887 ppm); BJD 2459067.1154: not recovered, depth 5400 ± 285 ppm (catalogue 6887 ppm); BJD 2459074.0463: gap (catalogue 6887 ppm); BJD 2459080.9773: partial, depth 4583 ± 268 ppm (catalogue 6887 ppm); BJD 2460099.8292: recovered, depth 5465 ± 242 ppm (catalogue 6887 ppm); BJD 2460106.7602: recovered, depth 6423 ± 260 ppm (catalogue 6887 ppm); BJD 2460113.6912: not recovered, depth 5268 ± 232 ppm (catalogue 6887 ppm); BJD 2460120.6221: recovered, depth 4452 ± 257 ppm (catalogue 6887 ppm); BJD 2460155.2770: recovered, depth 7450 ± 276 ppm (catalogue 6887 ppm); BJD 2460162.2079: recovered, depth 5003 ± 274 ppm (catalogue 6887 ppm); BJD 2460169.1389: recovered, depth 6234 ± 288 ppm (catalogue 6887 ppm); BJD 2460176.0699: recovered, depth 6235 ± 263 ppm (catalogue 6887 ppm); BJD 2460834.5116: recovered, depth 5657 ± 245 ppm (catalogue 6887 ppm); BJD 2460841.4426: not recovered, depth 968 ± 505 ppm (catalogue 6887 ppm); BJD 2460848.3735: partial, depth 5571 ± 237 ppm (catalogue 6887 ppm); BJD 2460855.3045: gap (catalogue 6887 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, 3, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460165.5094, ΔT = 800.390 d, 7 of 800 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (800.39, 400.195, 266.796, 200.097, 88.9322, 72.7627, 27.5996 d); duration likelihood under Gaia priors (circular orbits) peaks at 27.6 d (weight 0.54) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2223.01: Gaia DR3 4630347312027956480 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2223.01: Teff 5873 K, R* 1.37 ± 0.11, M* 1.26 ± 0.13, ρ* 0.49 ± 0.13 ρ☉ (dwarf sequence, M_G 3.52, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2223.01: 7 Gaia neighbour(s) within 52.5", contamination 15.63%; depth 5497 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4630347312027959296, 37.0", ΔG 1.89); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 0 clean; BJD 2460165.5094 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+18.9; BJD 2460179.4251 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+15.2; BJD 2460179.4459 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+16.7 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2223.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2223.01: TOI-2223 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2223-01.yaml
python -m cygnus.multi report campaigns/toi-2223-01.yaml
```
