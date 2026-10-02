<!-- cygnus:generated-draft -->
# Known-object test, TOI-5851.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5851-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5003, calibrate_screen #4985, event_census #4992, fetch_independent #4998, fetch_products #4983, known_signal_recovery #4986, moving_objects #4994, period_aliases #4993, prior_art #5006, residual_screen #4990, stellar_context #4987, variability_guard #5005
- Runner finished (UTC): 2026-09-30T22:48:39Z

## Bottom line

Positive control **inconclusive**: BJD 2460507.2344: not recovered, depth -6134 ± 1447 ppm (catalogue 14400 ppm); BJD 2460511.7393: partial, depth -772 ± 1467 ppm (catalogue 14400 ppm); BJD 2460516.2443: gap (catalogue 14400 ppm); BJD 2460520.7492: not recovered, depth -1278 ± 1363 ppm (catalogue 14400 ppm); BJD 2460525.2542: not recovered, depth -3432 ± 1479 ppm (catalogue 14400 ppm); BJD 2460529.7591: not recovered, depth -248 ± 1418 ppm (catalogue 14400 ppm).
Outside the catalogued epoch the screen left 92 threshold entries forming **30 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5851.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 277329402 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 292.681077 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 12.393071 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459790.948702 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.5049415 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14400.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.372 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8137 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-30 12:03:44 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | lightcurve | 81 | False | `fe55c738f235a2ab` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460507.23440 | not_recovered | 71 | -6134 ± 1447 | 14400 | — |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460511.73934 | partial | 69 | -772 ± 1467 | 14400 | -1.71 |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460516.24428 | gap | 0 | — | 14400 | — |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460520.74922 | not_recovered | 71 | -1278 ± 1363 | 14400 | — |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460525.25417 | not_recovered | 71 | -3432 ± 1479 | 14400 | — |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460529.75911 | not_recovered | 71 | -248 ± 1418 | 14400 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460525.06085 | -0.04349 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460529.52602 | -0.04276 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460525.00530 | -0.04004 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460529.53505 | -0.03877 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460525.02891 | -0.03770 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460516.69291 | -0.03404 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460516.59291 | -0.03265 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460511.51239 | -0.03232 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460529.56352 | -0.04098 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460507.04155 | -0.03806 | 2 | PDCSAP | 1 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460531.92318 | -0.03775 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460529.51769 | -0.03726 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460525.01155 | -0.03703 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460529.50102 | -0.03700 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460511.47628 | -0.03670 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460517.53040 | -0.03517 | 2 | PDCSAP | 1, 2 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460506.98738 | -0.03486 | 4 | PDCSAP | 1 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460525.02474 | -0.03431 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460511.53183 | -0.03193 | 2 | PDCSAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460520.54565 | -0.03138 | 2 | PDCSAP | 1, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.27766 | -0.01159 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.25821 | -0.01147 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460516.82763 | -0.01144 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.30682 | -0.01129 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.21516 | -0.01074 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.35127 | -0.01051 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460512.84710 | -0.01044 | 2 | SAP | 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.34016 | -0.01007 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460513.34571 | -0.00973 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000277329402-0276-s_lc.fits` | 2460520.51371 | -0.00938 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5851.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:48:26Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:48:30Z: TOI-5851.01 (TIC 277329402, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:48:34Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:48:36Z: UCAC4 512-096768 (SB*); UCAC4 512-096764 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460507.2344: not recovered, depth -6134 ± 1447 ppm (catalogue 14400 ppm); BJD 2460511.7393: partial, depth -772 ± 1467 ppm (catalogue 14400 ppm); BJD 2460516.2443: gap (catalogue 14400 ppm); BJD 2460520.7492: not recovered, depth -1278 ± 1363 ppm (catalogue 14400 ppm); BJD 2460525.2542: not recovered, depth -3432 ± 1479 ppm (catalogue 14400 ppm); BJD 2460529.7591: not recovered, depth -248 ± 1418 ppm (catalogue 14400 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5851.01: Gaia DR3 4316153205796932480 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5851.01: Teff 5162 K, R* 0.90 ± 0.07, M* 0.93 ± 0.09, ρ* 1.27 ± 0.33 ρ☉ (dwarf sequence, M_G 5.15, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5851.01: 364 Gaia neighbour(s) within 52.5", contamination 88.86%; depth 14400 ppm (catalogue depth); 11 could produce it if fully eclipsed (brightest 4316153132727698560, 43.5", ΔG -1.06); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 5 clean; BJD 2460511.5124 caution: manual exclude (within ±0.25 d); BJD 2460516.5929 suspect: scattered light 2 (within ±0.25 d), POS_CORR1 z=+7.9, SAP_BKG z=+102.9; BJD 2460516.6929 suspect: scattered light 2 (within ±0.25 d), POS_CORR1 z=+7.0, SAP_BKG z=+75.8 |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5851.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5851.01: UCAC4 512-096764 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5851-01.yaml
python -m cygnus.multi report campaigns/toi-5851-01.yaml
```
