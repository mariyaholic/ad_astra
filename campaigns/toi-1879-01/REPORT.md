<!-- cygnus:generated-draft -->
# Known-object test, TOI-1879.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1879-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4755, calibrate_screen #4726, event_census #4741, fetch_independent #4747, fetch_products #4707, known_signal_recovery #4735, moving_objects #4744, period_aliases #4742, prior_art #4758, residual_screen #4738, stellar_context #4736, variability_guard #4757
- Runner finished (UTC): 2026-09-30T22:17:03Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1879.01 (BJD 2459703.2899: not recovered, depth 5826 ± 462 ppm (catalogue 10116 ppm); BJD 2459716.9945: recovered, depth 7994 ± 466 ppm (catalogue 10116 ppm); BJD 2458963.2418: recovered, depth 7121 ± 501 ppm (catalogue 10116 ppm); BJD 2458976.9464: recovered, depth 6891 ± 514 ppm (catalogue 10116 ppm); BJD 2458990.6510: recovered, depth 6341 ± 587 ppm (catalogue 10116 ppm); BJD 2459004.3556: recovered, depth 6770 ± 557 ppm (catalogue 10116 ppm); BJD 2459018.0602: not recovered, depth 6254 ± 665 ppm (catalogue 10116 ppm); BJD 2459031.7648: not recovered, depth 7140 ± 662 ppm (catalogue 10116 ppm); BJD 2459401.7888: not recovered, depth 7456 ± 447 ppm (catalogue 10116 ppm); BJD 2459415.4934: not recovered, depth 6005 ± 491 ppm (catalogue 10116 ppm); BJD 2459429.1980: recovered, depth 6761 ± 602 ppm (catalogue 10116 ppm); BJD 2459442.9026: not recovered, depth 7954 ± 564 ppm (catalogue 10116 ppm)).
Outside the catalogued epoch the screen left 8 threshold entries forming **2 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1879.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 243335710 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 289.861603 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 59.670112 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459703.289921 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 13.7045951 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10116.0470111 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.8535412 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.9935 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-02-15 12:03:00 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022112184951-s0051-0000000243335710-0223-s_lc.fits` | lightcurve | 51 | True | `14f19dbe848e6903` | True |
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | lightcurve | 24 | False | `ef050ff10857dd3a` | True |
| `tess2020133194932-s0025-0000000243335710-0182-s_lc.fits` | lightcurve | 25 | False | `db34e4fcaf47b06f` | True |
| `tess2020160202036-s0026-0000000243335710-0188-s_lc.fits` | lightcurve | 26 | False | `ca3dd7a2685d7218` | True |
| `tess2021175071901-s0040-0000000243335710-0211-s_lc.fits` | lightcurve | 40 | False | `2e0962302c9bf798` | True |
| `tess2021204101404-s0041-0000000243335710-0212-s_lc.fits` | lightcurve | 41 | False | `6ab994ca5c9fc6d4` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022112184951-s0051-0000000243335710-0223-s_lc.fits` | 2459703.28992 | not_recovered | 176 | 5826 ± 462 | 10116 | — |
| `tess2022112184951-s0051-0000000243335710-0223-s_lc.fits` | 2459716.99452 | recovered | 176 | 7994 ± 466 | 10116 | 1.00 |
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | 2458963.24179 | recovered | 176 | 7121 ± 501 | 10116 | -0.59 |
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | 2458976.94638 | recovered | 171 | 6891 ± 514 | 10116 | -1.68 |
| `tess2020133194932-s0025-0000000243335710-0182-s_lc.fits` | 2458990.65098 | recovered | 174 | 6341 ± 587 | 10116 | 0.52 |
| `tess2020133194932-s0025-0000000243335710-0182-s_lc.fits` | 2459004.35557 | recovered | 175 | 6770 ± 557 | 10116 | -0.32 |
| `tess2020160202036-s0026-0000000243335710-0188-s_lc.fits` | 2459018.06017 | not_recovered | 176 | 6254 ± 665 | 10116 | — |
| `tess2020160202036-s0026-0000000243335710-0188-s_lc.fits` | 2459031.76476 | not_recovered | 176 | 7140 ± 662 | 10116 | — |
| `tess2021175071901-s0040-0000000243335710-0211-s_lc.fits` | 2459401.78883 | not_recovered | 175 | 7456 ± 447 | 10116 | — |
| `tess2021175071901-s0040-0000000243335710-0211-s_lc.fits` | 2459415.49342 | not_recovered | 175 | 6005 ± 491 | 10116 | — |
| `tess2021204101404-s0041-0000000243335710-0212-s_lc.fits` | 2459429.19802 | recovered | 176 | 6761 ± 602 | 10116 | 0.54 |
| `tess2021204101404-s0041-0000000243335710-0212-s_lc.fits` | 2459442.90261 | not_recovered | 176 | 7954 ± 564 | 10116 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022112184951-s0051-0000000243335710-0223-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2020133194932-s0025-0000000243335710-0182-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2020160202036-s0026-0000000243335710-0188-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2021175071901-s0040-0000000243335710-0211-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2021204101404-s0041-0000000243335710-0212-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | 2458975.82637 | -0.01845 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020106103520-s0024-0000000243335710-0180-s_lc.fits` | 2458962.59004 | -0.01795 | 2 | PDCSAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1879.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:16:41Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:16:48Z: TOI-1879.01 (TIC 243335710, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:16:52Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:16:56Z: TOI-1879 (*); TOI-1879.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459703.2899: not recovered, depth 5826 ± 462 ppm (catalogue 10116 ppm); BJD 2459716.9945: recovered, depth 7994 ± 466 ppm (catalogue 10116 ppm); BJD 2458963.2418: recovered, depth 7121 ± 501 ppm (catalogue 10116 ppm); BJD 2458976.9464: recovered, depth 6891 ± 514 ppm (catalogue 10116 ppm); BJD 2458990.6510: recovered, depth 6341 ± 587 ppm (catalogue 10116 ppm); BJD 2459004.3556: recovered, depth 6770 ± 557 ppm (catalogue 10116 ppm); BJD 2459018.0602: not recovered, depth 6254 ± 665 ppm (catalogue 10116 ppm); BJD 2459031.7648: not recovered, depth 7140 ± 662 ppm (catalogue 10116 ppm); BJD 2459401.7888: not recovered, depth 7456 ± 447 ppm (catalogue 10116 ppm); BJD 2459415.4934: not recovered, depth 6005 ± 491 ppm (catalogue 10116 ppm); BJD 2459429.1980: recovered, depth 6761 ± 602 ppm (catalogue 10116 ppm); BJD 2459442.9026: not recovered, depth 7954 ± 564 ppm (catalogue 10116 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1879.01: Gaia DR3 2239508514935155584 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-1879.01: Teff 6319 K, R* 1.47 ± 0.12, M* 1.32 ± 0.13, ρ* 0.42 ± 0.11 ρ☉ (dwarf sequence, M_G 3.28, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1879.01: 10 Gaia neighbour(s) within 52.5", contamination 6.81%; depth 7994 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 2239508549294896128, 38.7", ΔG 4.31); a centroid test is needed |
| Pointing and quality census per event | inconclusive | 1 persistent event(s), 0 clean; BJD 2458975.8264 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1879.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1879.01: TOI-1879 otype * (star_or_other) at 0.0" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1879-01.yaml
python -m cygnus.multi report campaigns/toi-1879-01.yaml
```
