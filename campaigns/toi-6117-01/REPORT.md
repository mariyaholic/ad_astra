<!-- cygnus:generated-draft -->
# Known-object test, TOI-6117.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6117-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4231, calibrate_screen #4207, event_census #4214, fetch_independent #4223, fetch_products #4202, known_signal_recovery #4208, moving_objects #4216, period_aliases #4215, prior_art #4233, residual_screen #4213, stellar_context #4209, variability_guard #4232
- Runner finished (UTC): 2026-09-30T21:43:04Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6117.01 (BJD 2460560.6317: recovered, depth -201 ± 229 ppm (catalogue 5737 ppm); BJD 2460570.4980: recovered, depth -642 ± 199 ppm (catalogue 5737 ppm); BJD 2460580.3644: recovered, depth -177 ± 197 ppm (catalogue 5737 ppm)).
Outside the catalogued epoch the screen left 36 threshold entries forming **10 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6117.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 436508469 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 348.099929 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 22.34547 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459850.257269 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 9.866312 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5737.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.285 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.5989 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | lightcurve | 83 | False | `f643deadb5dd406c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460560.63173 | recovered | 130 | -201 ± 229 | 5737 | -4.06 |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460570.49805 | recovered | 158 | -642 ± 199 | 5737 | -3.78 |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460580.36436 | recovered | 159 | -177 ± 197 | 5737 | -4.22 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460584.27231 | -0.00936 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460584.17578 | -0.00815 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460583.55287 | -0.00759 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460584.36119 | -0.00750 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460570.94322 | -0.00811 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460571.00294 | -0.00773 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460571.21406 | -0.00740 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460564.45289 | -0.00733 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460571.50850 | -0.00710 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000436508469-0280-s_lc.fits` | 2460559.48613 | -0.00623 | 2 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6117.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:42:57Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:42:59Z: TOI-6117.01 (TIC 436508469, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:43:01Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:43:03Z: TYC 1718-2182-1 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460560.6317: recovered, depth -201 ± 229 ppm (catalogue 5737 ppm); BJD 2460570.4980: recovered, depth -642 ± 199 ppm (catalogue 5737 ppm); BJD 2460580.3644: recovered, depth -177 ± 197 ppm (catalogue 5737 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6117.01: Gaia DR3 2838654459861938944 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6117.01: dwarf priors not applied — 1.24 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6117.01: 6 Gaia neighbour(s) within 52.5", contamination 7.36%; depth -201 ppm (measured depth of the recovered catalogued transit); 6 could produce it if fully eclipsed (brightest 2838654391142462976, 40.0", ΔG 2.83); a centroid test is needed |
| Pointing and quality census per event | failed | 4 persistent event(s), 1 clean; BJD 2460584.1758 suspect: MOM_CENTR1 z=+14.2, MOM_CENTR2 z=+9.3, POS_CORR1 z=+15.6, POS_CORR2 z=+11.0; BJD 2460584.2723 suspect: MOM_CENTR1 z=+12.5, MOM_CENTR2 z=+11.6, POS_CORR1 z=+15.8, POS_CORR2 z=+13.7; BJD 2460584.3612 suspect: MOM_CENTR1 z=+11.1, MOM_CENTR2 z=+11.3, POS_CORR1 z=+13.7, POS_CORR2 z=+12.8 |
| Moving objects at screen-event epochs | inconclusive | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6117.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-6117.01: TYC 1718-2182-1 otype SB* (multiple) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6117-01.yaml
python -m cygnus.multi report campaigns/toi-6117-01.yaml
```
