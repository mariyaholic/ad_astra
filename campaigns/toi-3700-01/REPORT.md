<!-- cygnus:generated-draft -->
# Known-object test, TOI-3700.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3700-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5001, calibrate_screen #4984, event_census #4995, fetch_independent #4999, fetch_products #4982, known_signal_recovery #4988, moving_objects #4997, period_aliases #4996, prior_art #5004, residual_screen #4991, stellar_context #4989, variability_guard #5002
- Runner finished (UTC): 2026-09-30T22:48:34Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3700.01 (BJD 2460286.3535: gap (catalogue 12333 ppm); BJD 2460290.7720: recovered, depth 10029 ± 573 ppm (catalogue 12333 ppm); BJD 2460295.1904: not recovered, depth 9604 ± 480 ppm (catalogue 12333 ppm); BJD 2460299.6089: not recovered, depth -26 ± 3638 ppm (catalogue 12333 ppm); BJD 2460304.0273: gap (catalogue 12333 ppm); BJD 2460308.4458: not recovered, depth 10307 ± 520 ppm (catalogue 12333 ppm); BJD 2459910.7859: gap (catalogue 12333 ppm); BJD 2459915.2043: not recovered, depth 8179 ± 550 ppm (catalogue 12333 ppm); BJD 2459919.6228: recovered, depth 10227 ± 541 ppm (catalogue 12333 ppm); BJD 2459924.0412: gap (catalogue 12333 ppm); BJD 2459928.4597: not recovered, depth 8970 ± 585 ppm (catalogue 12333 ppm); BJD 2459932.8781: recovered, depth 8572 ± 582 ppm (catalogue 12333 ppm); BJD 2460639.8290: gap (catalogue 12333 ppm); BJD 2460644.2474: recovered, depth 8027 ± 634 ppm (catalogue 12333 ppm); BJD 2460648.6659: recovered, depth 10782 ± 668 ppm (catalogue 12333 ppm); BJD 2460653.0843: gap (catalogue 12333 ppm); BJD 2460657.5028: gap (catalogue 12333 ppm); BJD 2460661.9212: recovered, depth 10703 ± 683 ppm (catalogue 12333 ppm)).
Outside the catalogued epoch the screen left 42 threshold entries forming **23 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460649.5252 matches the catalogued transit's depth (6334 vs 10029 ppm), 358.758 d later; 0 of 358 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3700.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 417676091 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 82.250858 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 68.481405 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460286.353547 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.4184429 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12333.3914621 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.2423132 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8166 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-10 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | lightcurve | 73 | True | `b3ef403bc41c778e` | True |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | lightcurve | 59 | False | `e5fb8e54ef4f9fe3` | True |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | lightcurve | 86 | False | `044e12cf9e2dcd64` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460286.35355 | gap | 0 | — | 12333 | — |
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460290.77199 | recovered | 97 | 10029 ± 573 | 12333 | -0.11 |
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460295.19043 | not_recovered | 97 | 9604 ± 480 | 12333 | — |
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460299.60888 | not_recovered | 2 | -26 ± 3638 | 12333 | — |
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460304.02732 | gap | 0 | — | 12333 | — |
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460308.44576 | not_recovered | 97 | 10307 ± 520 | 12333 | — |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 2459910.78590 | gap | 0 | — | 12333 | — |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 2459915.20434 | not_recovered | 97 | 8179 ± 550 | 12333 | — |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 2459919.62279 | recovered | 97 | 10227 ± 541 | 12333 | 0.08 |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 2459924.04123 | gap | 0 | — | 12333 | — |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 2459928.45967 | not_recovered | 97 | 8970 ± 585 | 12333 | — |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 2459932.87811 | recovered | 97 | 8572 ± 582 | 12333 | -0.25 |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460639.82898 | gap | 0 | — | 12333 | — |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460644.24742 | recovered | 98 | 8027 ± 634 | 12333 | -0.38 |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460648.66586 | recovered | 97 | 10782 ± 668 | 12333 | 0.64 |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460653.08431 | gap | 0 | — | 12333 | — |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460657.50275 | gap | 0 | — | 12333 | — |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460661.92119 | recovered | 98 | 10703 ± 683 | 12333 | 1.09 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2022330142927-s0059-0000000417676091-0248-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460641.79728 | -0.02223 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.52522 | -0.01875 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460641.55283 | -0.02573 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.16827 | -0.02419 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.02244 | -0.02289 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.53911 | -0.02207 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.35577 | -0.02169 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.60439 | -0.02151 | 2 | SAP | 1, 2, 3 | no |
| `tess2023341045131-s0073-0000000417676091-0268-s_lc.fits` | 2460298.92316 | -0.02080 | 2 | PDCSAP+SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.41411 | -0.02065 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.41827 | -0.01992 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.55994 | -0.01990 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.25438 | -0.01978 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.50161 | -0.01969 | 4 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.36411 | -0.01962 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460662.50725 | -0.01961 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.27522 | -0.01956 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.37105 | -0.01862 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.37938 | -0.01652 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.42800 | -0.01639 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.12244 | -0.01612 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460649.34119 | -0.01611 | 3 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000417676091-0283-s_lc.fits` | 2460641.42227 | -0.01599 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460649.52522 | 6334 | 10029 | 358.7576 | 0 / 358 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3700.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:48:20Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:48:23Z: TOI-3700.01 (TIC 417676091, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:48:27Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:48:30Z: TOI-3700.01 (Pl?); TOI-3700 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460286.3535: gap (catalogue 12333 ppm); BJD 2460290.7720: recovered, depth 10029 ± 573 ppm (catalogue 12333 ppm); BJD 2460295.1904: not recovered, depth 9604 ± 480 ppm (catalogue 12333 ppm); BJD 2460299.6089: not recovered, depth -26 ± 3638 ppm (catalogue 12333 ppm); BJD 2460304.0273: gap (catalogue 12333 ppm); BJD 2460308.4458: not recovered, depth 10307 ± 520 ppm (catalogue 12333 ppm); BJD 2459910.7859: gap (catalogue 12333 ppm); BJD 2459915.2043: not recovered, depth 8179 ± 550 ppm (catalogue 12333 ppm); BJD 2459919.6228: recovered, depth 10227 ± 541 ppm (catalogue 12333 ppm); BJD 2459924.0412: gap (catalogue 12333 ppm); BJD 2459928.4597: not recovered, depth 8970 ± 585 ppm (catalogue 12333 ppm); BJD 2459932.8781: recovered, depth 8572 ± 582 ppm (catalogue 12333 ppm); BJD 2460639.8290: gap (catalogue 12333 ppm); BJD 2460644.2474: recovered, depth 8027 ± 634 ppm (catalogue 12333 ppm); BJD 2460648.6659: recovered, depth 10782 ± 668 ppm (catalogue 12333 ppm); BJD 2460653.0843: gap (catalogue 12333 ppm); BJD 2460657.5028: gap (catalogue 12333 ppm); BJD 2460661.9212: recovered, depth 10703 ± 683 ppm (catalogue 12333 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 11% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460649.5252, ΔT = 358.758 d, 0 of 358 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3700.01: Gaia DR3 484588446904510720 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3700.01: Teff 5864 K, R* 1.09 ± 0.09, M* 1.06 ± 0.11, ρ* 0.81 ± 0.21 ρ☉ (dwarf sequence, M_G 4.35, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3700.01: 17 Gaia neighbour(s) within 52.5", contamination 38.34%; depth 10029 ppm (measured depth of the recovered catalogued transit); 7 could produce it if fully eclipsed (brightest 484576700173070720, 24.0", ΔG 1.60); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2460641.7973 suspect: manual exclude (in event); BJD 2460649.5252 suspect: manual exclude (within ±0.25 d), POS_CORR2 z=+5.3 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3700.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3700.01: TOI-3700 otype * (star_or_other) at 0.0" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-3700.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3700-01.yaml
python -m cygnus.multi report campaigns/toi-3700-01.yaml
```
