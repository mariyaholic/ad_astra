<!-- cygnus:generated-draft -->
# Known-object test, TOI-5575.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5575-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #219, calibrate_screen #194, event_census #202, fetch_products #192, known_signal_recovery #196, moving_objects #204, period_aliases #203, prior_art #221, residual_screen #201, stellar_context #198, variability_guard #220
- Runner finished (UTC): 2026-09-26T09:57:10Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 72 threshold entries forming **16 distinct event(s)**, **11 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5575.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 160162137 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 241.248539 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 85.204724 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459747.65944 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 145640.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.347 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 14.0127 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | lightcurve | 59 | False | `6a1cc4575c9ad76e` | True |
| `tess2022357055054-s0060-0000000160162137-0249-s_lc.fits` | lightcurve | 60 | False | `ae25b9b830f43ea3` | True |
| `tess2023341045131-s0073-0000000160162137-0268-s_lc.fits` | lightcurve | 73 | False | `9230529cf63cfc1c` | True |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | lightcurve | 79 | False | `36506575eba856f4` | True |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | lightcurve | 86 | False | `9d391b7564be5150` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | — | epoch not in this light curve | — | — | 145640 | — |
| `tess2022357055054-s0060-0000000160162137-0249-s_lc.fits` | — | epoch not in this light curve | — | — | 145640 | — |
| `tess2023341045131-s0073-0000000160162137-0268-s_lc.fits` | — | epoch not in this light curve | — | — | 145640 | — |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | — | epoch not in this light curve | — | — | 145640 | — |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | — | epoch not in this light curve | — | — | 145640 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2022357055054-s0060-0000000160162137-0249-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023341045131-s0073-0000000160162137-0268-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000160162137-0249-s_lc.fits` | 2459940.08509 | -0.14461 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | 2460453.24343 | -0.13092 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000160162137-0268-s_lc.fits` | 2460292.88139 | -0.13045 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | 2460645.67922 | -0.12833 | 43 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | 2460645.64658 | -0.06057 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000160162137-0249-s_lc.fits` | 2459940.12398 | -0.05806 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | 2460645.71186 | -0.05402 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2459912.03901 | -0.04915 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2459911.99595 | -0.04775 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | 2460453.28510 | -0.04716 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2459931.52812 | -0.03466 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023341045131-s0073-0000000160162137-0268-s_lc.fits` | 2460299.32935 | -0.04729 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2459912.38346 | -0.04251 | 2 | PDCSAP+SAP | 3 | no |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | 2460474.76257 | -0.03701 | 2 | SAP | 1 | no |
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2459911.96123 | -0.03535 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 2459912.95708 | -0.03274 | 2 | PDCSAP+SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5575.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:57:06Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:57:08Z: TOI-5575.01 (TIC 160162137, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:57:09Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T09:57:09Z: TOI-5575 (PM*); TOI-5575.01 (Pl?); ** TOI 5575B (BD*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5575.01: Gaia DR3 1724291831608394624 at 0.00" (propagated 2016.0 → J2015.5; 0.07" unpropagated, proper-motion shift 0.07") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5575.01: Teff 3179 K, R* 0.25 ± 0.02, M* 0.21 ± 0.02, ρ* 13.81 ± 3.59 ρ☉ (dwarf sequence, M_G 11.60, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-5575.01: 0 Gaia neighbour(s) within 52.5", contamination 0.00%; depth 145640 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 11 persistent event(s), 2 clean; BJD 2459911.9960 suspect: scattered light 2 (within ±0.25 d), POS_CORR1 z=-8.2, SAP_BKG z=+27.2; BJD 2459912.0390 suspect: scattered light 2 (within ±0.25 d), POS_CORR1 z=-7.0, SAP_BKG z=+27.1; BJD 2459940.0851 suspect: SAP_BKG z=+11.9; BJD 2459940.1240 suspect: SAP_BKG z=+6.5 |
| Moving objects at screen-event epochs | passed | 11 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5575.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5575.01: TOI-5575 otype PM* (star_or_other) at 2.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5575-01.yaml
python -m cygnus.multi report campaigns/toi-5575-01.yaml
```
