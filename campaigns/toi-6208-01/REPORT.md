<!-- cygnus:generated-draft -->
# Known-object test, TOI-6208.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6208-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4547, calibrate_screen #4530, event_census #4536, fetch_independent #4540, fetch_products #4518, known_signal_recovery #4533, moving_objects #4539, period_aliases #4537, prior_art #4552, residual_screen #4535, stellar_context #4534, variability_guard #4549
- Runner finished (UTC): 2026-09-30T22:00:17Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6208.01 (BJD 2460368.6349: not recovered, depth 6872 ± 361 ppm (catalogue 6662 ppm); BJD 2460373.8615: not recovered, depth 7035 ± 396 ppm (catalogue 6662 ppm); BJD 2460379.0881: not recovered, depth 6814 ± 341 ppm (catalogue 6662 ppm); BJD 2460384.3147: not recovered, depth 5852 ± 391 ppm (catalogue 6662 ppm); BJD 2460389.5414: not recovered, depth 6885 ± 422 ppm (catalogue 6662 ppm); BJD 2460394.7680: not recovered, depth -159 ± 491 ppm (catalogue 6662 ppm); BJD 2460399.9946: not recovered, depth 4740 ± 452 ppm (catalogue 6662 ppm); BJD 2460405.2213: not recovered, depth 7111 ± 385 ppm (catalogue 6662 ppm); BJD 2460410.4479: gap (catalogue 6662 ppm); BJD 2460415.6745: gap (catalogue 6662 ppm); BJD 2460420.9011: not recovered, depth 4193 ± 371 ppm (catalogue 6662 ppm); BJD 2460562.0201: recovered, depth 6542 ± 412 ppm (catalogue 6662 ppm); BJD 2460567.2467: not recovered, depth 6906 ± 393 ppm (catalogue 6662 ppm); BJD 2460572.4734: not recovered, depth 5573 ± 401 ppm (catalogue 6662 ppm); BJD 2460577.7000: recovered, depth 5763 ± 388 ppm (catalogue 6662 ppm); BJD 2460582.9266: recovered, depth 6785 ± 410 ppm (catalogue 6662 ppm); BJD 2460588.1533: recovered, depth 6319 ± 386 ppm (catalogue 6662 ppm); BJD 2460593.3799: recovered, depth 5657 ± 397 ppm (catalogue 6662 ppm); BJD 2460598.6065: recovered, depth 6308 ± 385 ppm (catalogue 6662 ppm); BJD 2460603.8331: recovered, depth 6698 ± 383 ppm (catalogue 6662 ppm); BJD 2460609.0598: recovered, depth 6749 ± 400 ppm (catalogue 6662 ppm)).
Outside the catalogued epoch the screen left 28 threshold entries forming **15 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6208.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 326475995 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 331.838189 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 53.519585 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459872.105147 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.2266285 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6662.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.412 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.9806 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-10-02 12:02:55 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | lightcurve | 76 | False | `311a9dbdcc2e8125` | True |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | lightcurve | 77 | False | `b6ecc107ad94af33` | True |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | lightcurve | 83 | False | `40b722d64c3db4db` | True |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | lightcurve | 84 | False | `2dff6f4ad34c11a3` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 2460368.63485 | not_recovered | 162 | 6872 ± 361 | 6662 | — |
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 2460373.86148 | not_recovered | 160 | 7035 ± 396 | 6662 | — |
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 2460379.08811 | not_recovered | 162 | 6814 ± 341 | 6662 | — |
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 2460384.31474 | not_recovered | 162 | 5852 ± 391 | 6662 | — |
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 2460389.54137 | not_recovered | 162 | 6885 ± 422 | 6662 | — |
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 2460394.76800 | not_recovered | 86 | -159 ± 491 | 6662 | — |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460399.99463 | not_recovered | 163 | 4740 ± 452 | 6662 | — |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460405.22125 | not_recovered | 162 | 7111 ± 385 | 6662 | — |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460410.44788 | gap | 0 | — | 6662 | — |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460415.67451 | gap | 0 | — | 6662 | — |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460420.90114 | not_recovered | 163 | 4193 ± 371 | 6662 | — |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460562.02011 | recovered | 141 | 6542 ± 412 | 6662 | -1.74 |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460567.24674 | not_recovered | 161 | 6906 ± 393 | 6662 | — |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460572.47337 | not_recovered | 162 | 5573 ± 401 | 6662 | — |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460577.69999 | recovered | 163 | 5763 ± 388 | 6662 | 0.22 |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460582.92662 | recovered | 163 | 6785 ± 410 | 6662 | -0.45 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460588.15325 | recovered | 162 | 6319 ± 386 | 6662 | -0.06 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460593.37988 | recovered | 162 | 5657 ± 397 | 6662 | -1.00 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460598.60651 | recovered | 162 | 6308 ± 385 | 6662 | 1.23 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460603.83314 | recovered | 163 | 6698 ± 383 | 6662 | 1.03 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460609.05977 | recovered | 162 | 6749 ± 400 | 6662 | -0.19 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024058030222-s0076-0000000326475995-0271-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460585.24382 | -0.01420 | 2 | PDCSAP | 1 | no |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460395.50355 | -0.01336 | 2 | SAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460395.52300 | -0.01229 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460559.63527 | -0.01112 | 2 | SAP | 2, 3 | no |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460401.83550 | -0.01048 | 2 | SAP | 1, 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460559.70472 | -0.00998 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460570.82572 | -0.00980 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460564.02840 | -0.00971 | 2 | SAP | 2, 3 | no |
| `tess2024085201119-s0077-0000000326475995-0272-s_lc.fits` | 2460395.51258 | -0.00971 | 3 | SAP | 1, 2 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460577.22714 | -0.00914 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460570.37988 | -0.00894 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460570.85905 | -0.00894 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000326475995-0281-s_lc.fits` | 2460590.52990 | -0.00882 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460559.55749 | -0.00876 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000326475995-0280-s_lc.fits` | 2460571.68545 | -0.00819 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6208.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:00:04Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:00:07Z: TOI-6208.01 (TIC 326475995, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:00:10Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:00:12Z: UCAC4 718-091104 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460368.6349: not recovered, depth 6872 ± 361 ppm (catalogue 6662 ppm); BJD 2460373.8615: not recovered, depth 7035 ± 396 ppm (catalogue 6662 ppm); BJD 2460379.0881: not recovered, depth 6814 ± 341 ppm (catalogue 6662 ppm); BJD 2460384.3147: not recovered, depth 5852 ± 391 ppm (catalogue 6662 ppm); BJD 2460389.5414: not recovered, depth 6885 ± 422 ppm (catalogue 6662 ppm); BJD 2460394.7680: not recovered, depth -159 ± 491 ppm (catalogue 6662 ppm); BJD 2460399.9946: not recovered, depth 4740 ± 452 ppm (catalogue 6662 ppm); BJD 2460405.2213: not recovered, depth 7111 ± 385 ppm (catalogue 6662 ppm); BJD 2460410.4479: gap (catalogue 6662 ppm); BJD 2460415.6745: gap (catalogue 6662 ppm); BJD 2460420.9011: not recovered, depth 4193 ± 371 ppm (catalogue 6662 ppm); BJD 2460562.0201: recovered, depth 6542 ± 412 ppm (catalogue 6662 ppm); BJD 2460567.2467: not recovered, depth 6906 ± 393 ppm (catalogue 6662 ppm); BJD 2460572.4734: not recovered, depth 5573 ± 401 ppm (catalogue 6662 ppm); BJD 2460577.7000: recovered, depth 5763 ± 388 ppm (catalogue 6662 ppm); BJD 2460582.9266: recovered, depth 6785 ± 410 ppm (catalogue 6662 ppm); BJD 2460588.1533: recovered, depth 6319 ± 386 ppm (catalogue 6662 ppm); BJD 2460593.3799: recovered, depth 5657 ± 397 ppm (catalogue 6662 ppm); BJD 2460598.6065: recovered, depth 6308 ± 385 ppm (catalogue 6662 ppm); BJD 2460603.8331: recovered, depth 6698 ± 383 ppm (catalogue 6662 ppm); BJD 2460609.0598: recovered, depth 6749 ± 400 ppm (catalogue 6662 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6208.01: Gaia DR3 2005283023221079552 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6208.01: dwarf priors not applied — 1.65 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6208.01: 98 Gaia neighbour(s) within 52.5", contamination 61.14%; depth 6542 ppm (measured depth of the recovered catalogued transit); 11 could produce it if fully eclipsed (brightest 2005283023221075456, 31.0", ΔG 0.60); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6208.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6208.01: UCAC4 718-091104 otype * (star_or_other) at 0.3" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6208-01.yaml
python -m cygnus.multi report campaigns/toi-6208-01.yaml
```
