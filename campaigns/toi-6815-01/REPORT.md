<!-- cygnus:generated-draft -->
# Known-object test, TOI-6815.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6815-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #677, calibrate_screen #663, event_census #667, fetch_products #662, known_signal_recovery #664, moving_objects #669, period_aliases #668, prior_art #679, residual_screen #666, stellar_context #665, variability_guard #678
- Runner finished (UTC): 2026-09-26T10:13:17Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 58 threshold entries forming **17 distinct event(s)**, **9 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6815.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 233964924 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 36.351144 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -65.055381 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460196.836562 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 44474.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.309 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.169 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-01-03 12:03:46 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | lightcurve | 95 | False | `f33b65fd795751c8` | True |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | lightcurve | 96 | False | `e573a280e2ea9857` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | — | epoch not in this light curve | — | — | 44474 | — |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 44474 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460931.62812 | -0.04608 | 97 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460913.70873 | -0.04400 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460931.69965 | -0.02728 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460909.22883 | -0.02539 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460931.55729 | -0.02288 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460906.71632 | -0.02044 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460906.46424 | -0.01800 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460889.30223 | -0.01792 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460906.71077 | -0.01698 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460909.29134 | -0.02187 | 2 | PDCSAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460909.25522 | -0.02177 | 2 | PDCSAP | 3 | no |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460913.63442 | -0.02168 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000233964924-0293-s_lc.fits` | 2460909.26911 | -0.02168 | 2 | PDCSAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460906.35243 | -0.01814 | 2 | PDCSAP+SAP | 3 | no |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460906.53091 | -0.01740 | 3 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460904.37881 | -0.01730 | 2 | SAP | 1 | no |
| `tess2025206162959-s0095-0000000233964924-0292-s_lc.fits` | 2460906.52118 | -0.01655 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6815.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:13:14Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:13:15Z: TOI-6815.01 (TIC 233964924, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:13:17Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:13:17Z: UCAC4 125-002278 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6815.01: Gaia DR3 4699689249783351552 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6815.01: Teff 5130 K, R* 0.78 ± 0.06, M* 0.81 ± 0.08, ρ* 1.73 ± 0.45 ρ☉ (dwarf sequence, M_G 5.91, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-6815.01: 3 Gaia neighbour(s) within 52.5", contamination 1.55%; depth 44474 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 9 persistent event(s), 5 clean; BJD 2460906.4642 suspect: POS_CORR2 z=-5.8, SAP_BKG z=+6.1; BJD 2460906.7108 suspect: manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), POS_CORR1 z=-7.8, POS_CORR2 z=-6.0; BJD 2460906.7163 suspect: manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), POS_CORR1 z=-7.7, POS_CORR2 z=-5.8; BJD 2460909.2288 suspect: scattered light 2 (in event), POS_CORR1 z=-6.2, POS_CORR2 z=-7.3, SAP_BKG z=+42.3 |
| Moving objects at screen-event epochs | passed | 9 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6815.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6815.01: UCAC4 125-002278 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6815-01.yaml
python -m cygnus.multi report campaigns/toi-6815-01.yaml
```
