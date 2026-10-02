<!-- cygnus:generated-draft -->
# Known-object test, TOI-6562.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6562-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5026, calibrate_screen #5014, event_census #5018, fetch_independent #5022, fetch_products #5009, known_signal_recovery #5015, moving_objects #5020, period_aliases #5019, prior_art #5029, residual_screen #5017, stellar_context #5016, variability_guard #5027
- Runner finished (UTC): 2026-09-30T22:51:00Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6562.01 (BJD 2460071.6473: recovered, depth 4671 ± 220 ppm (catalogue 5981 ppm); BJD 2460075.7420: recovered, depth 4445 ± 237 ppm (catalogue 5981 ppm); BJD 2460079.8368: gap (catalogue 5981 ppm); BJD 2460083.9315: recovered, depth 5211 ± 227 ppm (catalogue 5981 ppm); BJD 2460088.0263: recovered, depth 4810 ± 224 ppm (catalogue 5981 ppm); BJD 2460092.1210: recovered, depth 4092 ± 269 ppm (catalogue 5981 ppm); BJD 2460096.2158: gap (catalogue 5981 ppm); BJD 2461128.0924: recovered, depth 104 ± 257 ppm (catalogue 5981 ppm); BJD 2461132.1871: not recovered, depth -325 ± 249 ppm (catalogue 5981 ppm); BJD 2461136.2819: not recovered, depth -383 ± 247 ppm (catalogue 5981 ppm); BJD 2461140.3766: not recovered, depth -1320 ± 215 ppm (catalogue 5981 ppm); BJD 2461144.4714: not recovered, depth -615 ± 246 ppm (catalogue 5981 ppm); BJD 2461148.5661: partial, depth -61 ± 237 ppm (catalogue 5981 ppm)).
Outside the catalogued epoch the screen left 28 threshold entries forming **15 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460092.8149 matches the catalogued transit's depth (3400 vs 4671 ppm), 21.112 d later; 1 of 21 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6562.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 368713985 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 220.299751 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -32.363352 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460071.647261 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.0947485 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5981.4894009 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.1910541 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.7584 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-07-21 12:03:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | lightcurve | 65 | True | `38c85857bf385318` | True |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | lightcurve | 102 | False | `2a38756b2be8f26f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460071.64726 | recovered | 156 | 4671 ± 220 | 5981 | 1.33 |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460075.74201 | recovered | 156 | 4445 ± 237 | 5981 | 0.02 |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460079.83676 | gap | 0 | — | 5981 | — |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460083.93151 | recovered | 156 | 5211 ± 227 | 5981 | 0.31 |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460088.02625 | recovered | 156 | 4810 ± 224 | 5981 | 0.81 |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460092.12100 | recovered | 155 | 4092 ± 269 | 5981 | -0.11 |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460096.21575 | gap | 0 | — | 5981 | — |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461128.09237 | recovered | 156 | 104 ± 257 | 5981 | -4.21 |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461132.18712 | not_recovered | 156 | -325 ± 249 | 5981 | — |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461136.28187 | not_recovered | 155 | -383 ± 247 | 5981 | — |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461140.37662 | not_recovered | 154 | -1320 ± 215 | 5981 | — |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461144.47137 | not_recovered | 155 | -615 ± 246 | 5981 | — |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461148.56612 | partial | 156 | -61 ± 237 | 5981 | -4.42 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460092.81489 | -0.00859 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461145.67902 | -0.01115 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460089.91566 | -0.01078 | 3 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461127.75171 | -0.01023 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460089.82886 | -0.00986 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460068.85127 | -0.00978 | 4 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000368713985-0304-s_lc.fits` | 2461135.95079 | -0.00978 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460090.00246 | -0.00958 | 4 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460090.05732 | -0.00952 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460089.98372 | -0.00928 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460089.81497 | -0.00925 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460068.79988 | -0.00907 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460089.66081 | -0.00874 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460089.95038 | -0.00821 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000368713985-0259-s_lc.fits` | 2460092.64545 | -0.00819 | 2 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460092.81489 | 3400 | 4671 | 21.1122 | 1 / 21 | 21.1122 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6562.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:50:48Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:50:51Z: TOI-6562.01 (TIC 368713985, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:50:54Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:50:56Z: UCAC4 289-074362 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460071.6473: recovered, depth 4671 ± 220 ppm (catalogue 5981 ppm); BJD 2460075.7420: recovered, depth 4445 ± 237 ppm (catalogue 5981 ppm); BJD 2460079.8368: gap (catalogue 5981 ppm); BJD 2460083.9315: recovered, depth 5211 ± 227 ppm (catalogue 5981 ppm); BJD 2460088.0263: recovered, depth 4810 ± 224 ppm (catalogue 5981 ppm); BJD 2460092.1210: recovered, depth 4092 ± 269 ppm (catalogue 5981 ppm); BJD 2460096.2158: gap (catalogue 5981 ppm); BJD 2461128.0924: recovered, depth 104 ± 257 ppm (catalogue 5981 ppm); BJD 2461132.1871: not recovered, depth -325 ± 249 ppm (catalogue 5981 ppm); BJD 2461136.2819: not recovered, depth -383 ± 247 ppm (catalogue 5981 ppm); BJD 2461140.3766: not recovered, depth -1320 ± 215 ppm (catalogue 5981 ppm); BJD 2461144.4714: not recovered, depth -615 ± 246 ppm (catalogue 5981 ppm); BJD 2461148.5661: partial, depth -61 ± 237 ppm (catalogue 5981 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460092.8149, ΔT = 21.112 d, 1 of 21 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (21.1122 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6562.01: Gaia DR3 6215933514123357440 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6562.01: dwarf priors not applied — 1.31 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6562.01: 10 Gaia neighbour(s) within 52.5", contamination 6.78%; depth 4671 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 6215933617202577664, 39.9", ΔG 3.38); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460092.8149 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=-7.4, POS_CORR2 z=-9.4, SAP_BKG z=+41.9 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-6562.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6562.01: UCAC4 289-074362 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-6562.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6562-01.yaml
python -m cygnus.multi report campaigns/toi-6562-01.yaml
```
