<!-- cygnus:generated-draft -->
# Known-object test, TOI-5571.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5571-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4638, calibrate_screen #4618, event_census #4630, fetch_independent #4635, fetch_products #4613, known_signal_recovery #4623, moving_objects #4632, period_aliases #4631, prior_art #4642, residual_screen #4628, stellar_context #4624, variability_guard #4641
- Runner finished (UTC): 2026-09-30T22:08:04Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5571.01 (BJD 2459585.7067: recovered, depth 4548 ± 236 ppm (catalogue 5900 ppm)).
Outside the catalogued epoch the screen left 109 threshold entries forming **57 distinct event(s)**, **5 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459959.5585 matches the catalogued transit's depth (2340 vs 4548 ppm), 373.856 d later; 12 of 373 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5571.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 88565745 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 106.990414 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 60.01161 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458854.228883 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 731.4778512 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5900.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.41 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.2245 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-03-26 12:03:43 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000088565745-0218-s_lc.fits` | lightcurve | 47 | False | `4ace7ffeabb9d509` | True |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | lightcurve | 60 | False | `5e1fc3345e1c39a4` | True |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | lightcurve | 73 | False | `6be53743ed205b59` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000088565745-0218-s_lc.fits` | 2459585.70673 | recovered | 103 | 4548 ± 236 | 5900 | -0.09 |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | — | epoch not in this light curve | — | — | 5900 | — |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | — | epoch not in this light curve | — | — | 5900 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000088565745-0218-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.91247 | -0.01258 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.94094 | -0.01155 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.92150 | -0.01037 | 9 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2459961.11953 | -0.00649 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2459959.55846 | -0.00640 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.00260 | -0.01226 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.66247 | -0.01094 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.71247 | -0.01041 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.69511 | -0.01011 | 5 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.93191 | -0.00998 | 4 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.70136 | -0.00963 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.74163 | -0.00957 | 4 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.74858 | -0.00956 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.75691 | -0.00955 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.90066 | -0.00947 | 3 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.07204 | -0.00938 | 2 | SAP | 1, 2 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.59441 | -0.00938 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.78052 | -0.00918 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.89580 | -0.00916 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.86594 | -0.00914 | 5 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.83330 | -0.00897 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.72358 | -0.00894 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.63191 | -0.00890 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.73261 | -0.00889 | 5 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.87358 | -0.00882 | 4 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.82497 | -0.00880 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.81802 | -0.00880 | 6 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.84580 | -0.00870 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.90691 | -0.00869 | 4 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.84997 | -0.00868 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.88608 | -0.00867 | 4 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.80552 | -0.00865 | 4 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.01926 | -0.00857 | 2 | SAP | 1, 2 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460296.29715 | -0.00844 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.57358 | -0.00843 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.67913 | -0.00840 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.70830 | -0.00836 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460290.76298 | -0.00823 | 3 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.85483 | -0.00798 | 3 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.61247 | -0.00791 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460290.81576 | -0.00777 | 3 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.84094 | -0.00774 | 3 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460296.51521 | -0.00768 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.88052 | -0.00766 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460298.79927 | -0.00758 | 3 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460296.36173 | -0.00753 | 3 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460290.79423 | -0.00751 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.00815 | -0.00723 | 2 | SAP | 1, 2 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.06788 | -0.00721 | 2 | SAP | 1 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.03871 | -0.00708 | 2 | SAP | 1, 2 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460293.41236 | -0.00707 | 2 | PDCSAP | 2 | no |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2459942.66691 | -0.00706 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2459944.36831 | -0.00694 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460291.99287 | -0.00643 | 2 | PDCSAP | 1 | no |
| `tess2023341045131-s0073-0000000088565745-0268-s_lc.fits` | 2460292.05399 | -0.00625 | 2 | SAP | 1 | no |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2459939.82245 | -0.00604 | 2 | SAP | 1 | no |
| `tess2022357055054-s0060-0000000088565745-0249-s_lc.fits` | 2459939.62522 | -0.00559 | 2 | PDCSAP+SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459959.55846 | 2340 | 4548 | 373.8556 | 12 / 373 | 373.856, 186.928, 124.618, 93.4639, 74.7711, 62.3093, 53.4079, 46.732, 37.3856, 31.1546, 28.7581, 23.366 |
| 2460298.91247 | 4383 | 4548 | 713.2096 | 14 / 713 | 713.21, 237.737, 142.642, 101.887, 79.2455, 64.8372, 54.8623, 47.5473, 41.9535, 37.5373, 24.5934, 23.0068, 21.6124, 20.3774 |
| 2460298.92150 | 4516 | 4548 | 713.2186 | 14 / 713 | 713.219, 237.739, 142.644, 101.888, 79.2465, 64.8381, 54.863, 47.5479, 41.954, 37.5378, 24.5937, 23.0071, 21.6127, 20.3777 |
| 2460298.94094 | 4435 | 4548 | 713.2381 | 14 / 713 | 713.238, 237.746, 142.648, 101.891, 79.2487, 64.8398, 54.8645, 47.5492, 41.9552, 37.5388, 24.5944, 23.0077, 21.6133, 20.3782 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-5571.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:07:32Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:07:35Z: TOI-5571.01 (TIC 88565745, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:07:38Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:07:40Z: TYC 4110-260-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459585.7067: recovered, depth 4548 ± 236 ppm (catalogue 5900 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 30%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2459959.5585, ΔT = 373.856 d, 12 of 373 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (373.856, 186.928, 124.618, 93.4639, 74.7711, 62.3093, 53.4079, 46.732, 37.3856, 31.1546, 28.7581, 23.366 d); duration likelihood under Gaia priors (circular orbits) peaks at 23.4 d (weight 0.21) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5571.01: Gaia DR3 1002774052143638784 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5571.01: Teff 6066 K, R* 1.16 ± 0.09, M* 1.11 ± 0.11, ρ* 0.72 ± 0.19 ρ☉ (dwarf sequence, M_G 4.13, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-5571.01: 6 Gaia neighbour(s) within 52.5", contamination 0.82%; depth 4548 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 5 persistent event(s), 2 clean; BJD 2460298.9125 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), POS_CORR2 z=-5.4; BJD 2460298.9215 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2460298.9409 caution: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-5571.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5571.01: TYC 4110-260-1 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5571-01.yaml
python -m cygnus.multi report campaigns/toi-5571-01.yaml
```
