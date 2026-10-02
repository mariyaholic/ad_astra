<!-- cygnus:generated-draft -->
# Known-object test, TOI-3706.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3706-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5157, calibrate_screen #5133, event_census #5138, fetch_independent #5141, fetch_products #5123, known_signal_recovery #5134, moving_objects #5140, period_aliases #5139, prior_art #5160, residual_screen #5137, stellar_context #5135, variability_guard #5158
- Runner finished (UTC): 2026-09-30T23:04:37Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3706.01 (BJD 2460286.7700: gap (catalogue 15001 ppm); BJD 2460291.1402: recovered, depth 14021 ± 945 ppm (catalogue 15001 ppm); BJD 2460295.5104: not recovered, depth 9504 ± 818 ppm (catalogue 15001 ppm); BJD 2460299.8805: gap (catalogue 15001 ppm); BJD 2460304.2507: gap (catalogue 15001 ppm); BJD 2460308.6209: recovered, depth 9758 ± 840 ppm (catalogue 15001 ppm); BJD 2459910.9346: gap (catalogue 15001 ppm); BJD 2459915.3047: recovered, depth 8112 ± 844 ppm (catalogue 15001 ppm); BJD 2459919.6749: recovered, depth 7358 ± 859 ppm (catalogue 15001 ppm); BJD 2459924.0451: gap (catalogue 15001 ppm); BJD 2459928.4153: recovered, depth 8063 ± 897 ppm (catalogue 15001 ppm); BJD 2459932.7855: recovered, depth 7448 ± 875 ppm (catalogue 15001 ppm); BJD 2460636.3844: not recovered, depth 13373 ± 764 ppm (catalogue 15001 ppm); BJD 2460640.7545: not recovered, depth 16843 ± 1120 ppm (catalogue 15001 ppm); BJD 2460645.1247: not recovered, depth 7916 ± 799 ppm (catalogue 15001 ppm); BJD 2460649.4949: not recovered, depth 5903 ± 1104 ppm (catalogue 15001 ppm); BJD 2460653.8651: gap (catalogue 15001 ppm); BJD 2460658.2353: gap (catalogue 15001 ppm); BJD 2460662.6054: not recovered, depth 8364 ± 794 ppm (catalogue 15001 ppm)).
Outside the catalogued epoch the screen left 28 threshold entries forming **14 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460299.4869 matches the catalogued transit's depth (12874 vs 14021 ppm), 8.392 d later; 0 of 8 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3706.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 252430813 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 76.825224 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 59.729551 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460286.769995 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.3701795 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15001.3632154 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.7808822 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.4223 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-10 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | lightcurve | 73 | True | `4144810d5881e1da` | True |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | lightcurve | 59 | False | `acfa3a7eb2649167` | True |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | lightcurve | 86 | False | `4b6a5b1b636cc8b9` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460286.77000 | gap | 0 | — | 15001 | — |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460291.14017 | recovered | 114 | 14021 ± 945 | 15001 | -1.10 |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460295.51035 | not_recovered | 113 | 9504 ± 818 | 15001 | — |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.88053 | gap | 0 | — | 15001 | — |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460304.25071 | gap | 0 | — | 15001 | — |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460308.62089 | recovered | 114 | 9758 ± 840 | 15001 | -0.24 |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459910.93456 | gap | 0 | — | 15001 | — |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459915.30474 | recovered | 113 | 8112 ± 844 | 15001 | -1.54 |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459919.67492 | recovered | 113 | 7358 ± 859 | 15001 | -1.23 |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459924.04510 | gap | 0 | — | 15001 | — |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459928.41528 | recovered | 114 | 8063 ± 897 | 15001 | -0.39 |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459932.78546 | recovered | 113 | 7448 ± 875 | 15001 | -0.41 |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460636.38436 | not_recovered | 113 | 13373 ± 764 | 15001 | — |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460640.75453 | not_recovered | 114 | 16843 ± 1120 | 15001 | — |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460645.12471 | not_recovered | 113 | 7916 ± 799 | 15001 | — |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460649.49489 | not_recovered | 111 | 5903 ± 1104 | 15001 | — |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460653.86507 | gap | 0 | — | 15001 | — |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460658.23525 | gap | 0 | — | 15001 | — |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 2460662.60543 | not_recovered | 113 | 8364 ± 794 | 15001 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024326142117-s0086-0000000252430813-0283-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.48687 | -0.03778 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459911.65289 | -0.02787 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459912.12929 | -0.02780 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.28757 | -0.02735 | 4 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.27368 | -0.02725 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.35562 | -0.02683 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460285.97368 | -0.02594 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.45423 | -0.02576 | 2 | PDCSAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.24868 | -0.02548 | 2 | PDCSAP | 3 | no |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459912.01401 | -0.02534 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.23340 | -0.02508 | 2 | PDCSAP | 3 | no |
| `tess2022330142927-s0059-0000000252430813-0248-s_lc.fits` | 2459930.22667 | -0.02507 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460299.26673 | -0.02460 | 2 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000252430813-0268-s_lc.fits` | 2460311.30541 | -0.02321 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460299.48687 | 12874 | 14021 | 8.3923 | 0 / 8 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3706.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:04:27Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:04:30Z: TOI-3706.01 (TIC 252430813, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T23:04:32Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T23:04:34Z: TOI-3706.01 (Pl?); TOI-3706 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460286.7700: gap (catalogue 15001 ppm); BJD 2460291.1402: recovered, depth 14021 ± 945 ppm (catalogue 15001 ppm); BJD 2460295.5104: not recovered, depth 9504 ± 818 ppm (catalogue 15001 ppm); BJD 2460299.8805: gap (catalogue 15001 ppm); BJD 2460304.2507: gap (catalogue 15001 ppm); BJD 2460308.6209: recovered, depth 9758 ± 840 ppm (catalogue 15001 ppm); BJD 2459910.9346: gap (catalogue 15001 ppm); BJD 2459915.3047: recovered, depth 8112 ± 844 ppm (catalogue 15001 ppm); BJD 2459919.6749: recovered, depth 7358 ± 859 ppm (catalogue 15001 ppm); BJD 2459924.0451: gap (catalogue 15001 ppm); BJD 2459928.4153: recovered, depth 8063 ± 897 ppm (catalogue 15001 ppm); BJD 2459932.7855: recovered, depth 7448 ± 875 ppm (catalogue 15001 ppm); BJD 2460636.3844: not recovered, depth 13373 ± 764 ppm (catalogue 15001 ppm); BJD 2460640.7545: not recovered, depth 16843 ± 1120 ppm (catalogue 15001 ppm); BJD 2460645.1247: not recovered, depth 7916 ± 799 ppm (catalogue 15001 ppm); BJD 2460649.4949: not recovered, depth 5903 ± 1104 ppm (catalogue 15001 ppm); BJD 2460653.8651: gap (catalogue 15001 ppm); BJD 2460658.2353: gap (catalogue 15001 ppm); BJD 2460662.6054: not recovered, depth 8364 ± 794 ppm (catalogue 15001 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460299.4869, ΔT = 8.392 d, 0 of 8 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3706.01: Gaia DR3 284571549348793728 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3706.01: dwarf priors not applied — 1.95 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3706.01: 13 Gaia neighbour(s) within 52.5", contamination 12.78%; depth 14021 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 284572305263037696, 31.6", ΔG 2.94); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2460299.4869 suspect: manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), MOM_CENTR2 z=+18.1, POS_CORR1 z=-7.9, POS_CORR2 z=+29.8, SAP_BKG z=+343.1; BJD 2459911.6529 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=-6.2, POS_CORR1 z=-6.2, POS_CORR2 z=-12.8, SAP_BKG z=+19.5 |
| Moving objects at screen-event epochs | inconclusive | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3706.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3706.01: TOI-3706 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-3706.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3706-01.yaml
python -m cygnus.multi report campaigns/toi-3706-01.yaml
```
