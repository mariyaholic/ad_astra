<!-- cygnus:generated-draft -->
# Known-object test, TOI-6111.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6111-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4524, calibrate_screen #4504, event_census #4511, fetch_independent #4517, fetch_products #4500, known_signal_recovery #4505, moving_objects #4514, period_aliases #4512, prior_art #4526, residual_screen #4507, stellar_context #4506, variability_guard #4525
- Runner finished (UTC): 2026-09-30T21:58:32Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6111.01 (BJD 2460368.0092: recovered, depth 12605 ± 843 ppm (catalogue 11944 ppm); BJD 2460373.8433: recovered, depth 5638 ± 998 ppm (catalogue 11944 ppm); BJD 2460379.6773: recovered, depth 11532 ± 769 ppm (catalogue 11944 ppm); BJD 2460385.5113: recovered, depth 8203 ± 900 ppm (catalogue 11944 ppm); BJD 2460391.3454: recovered, depth 12119 ± 762 ppm (catalogue 11944 ppm); BJD 2460537.1961: recovered, depth 9791 ± 687 ppm (catalogue 11944 ppm); BJD 2460543.0301: partial, depth 9509 ± 632 ppm (catalogue 11944 ppm); BJD 2460548.8641: partial, depth 10803 ± 550 ppm (catalogue 11944 ppm); BJD 2460554.6982: partial, depth 11853 ± 585 ppm (catalogue 11944 ppm); BJD 2460560.5322: partial, depth 8484 ± 616 ppm (catalogue 11944 ppm); BJD 2460566.3662: recovered, depth 7581 ± 587 ppm (catalogue 11944 ppm); BJD 2460572.2003: recovered, depth 13071 ± 753 ppm (catalogue 11944 ppm); BJD 2460578.0343: not recovered, depth 7443 ± 891 ppm (catalogue 11944 ppm); BJD 2460583.8683: recovered, depth 7282 ± 608 ppm (catalogue 11944 ppm)).
Outside the catalogued epoch the screen left 75 threshold entries forming **37 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460543.7757 matches the catalogued transit's depth (9187 vs 12605 ppm), 175.771 d later; 4 of 175 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6111.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 189322727 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 309.708254 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 44.791967 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459848.780642 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.8340292 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11944.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.289 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6894 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | lightcurve | 76 | False | `7f4ff5764f5d8f38` | True |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | lightcurve | 82 | False | `560b521444261c58` | True |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | lightcurve | 83 | False | `a8a1ef731b4a89b5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460368.00924 | recovered | 38 | 12605 ± 843 | 11944 | -0.10 |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.84327 | recovered | 36 | 5638 ± 998 | 11944 | -0.01 |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460379.67730 | recovered | 38 | 11532 ± 769 | 11944 | 0.04 |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460385.51133 | recovered | 39 | 8203 ± 900 | 11944 | -0.18 |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460391.34536 | recovered | 39 | 12119 ± 762 | 11944 | -0.21 |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460537.19609 | recovered | 39 | 9791 ± 687 | 11944 | 0.11 |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460543.03012 | partial | 39 | 9509 ± 632 | 11944 | 0.14 |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460548.86415 | partial | 39 | 10803 ± 550 | 11944 | -0.09 |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460554.69818 | partial | 39 | 11853 ± 585 | 11944 | -0.01 |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460560.53220 | partial | 39 | 8484 ± 616 | 11944 | -0.29 |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460566.36623 | recovered | 39 | 7581 ± 587 | 11944 | -0.24 |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460572.20026 | recovered | 38 | 13071 ± 753 | 11944 | 0.07 |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460578.03429 | not_recovered | 20 | 7443 ± 891 | 11944 | — |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460583.86832 | recovered | 38 | 7282 ± 608 | 11944 | -0.17 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 4 | False | 1h: —, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460543.77567 | -0.03292 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460543.70345 | -0.02476 | 8 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460544.31595 | -0.01853 | 2 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460544.30206 | -0.01631 | 6 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460544.06109 | -0.01572 | 6 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460563.43808 | -0.01559 | 2 | PDCSAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460562.00755 | -0.01550 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460367.77041 | -0.01531 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460545.68124 | -0.01473 | 2 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460370.42458 | -0.01454 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.30793 | -0.01397 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.09352 | -0.01299 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.72459 | -0.01282 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460545.38679 | -0.01276 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.48240 | -0.01244 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.56851 | -0.01240 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.41296 | -0.01229 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.39959 | -0.01223 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.63518 | -0.01204 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.53518 | -0.01194 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000189322727-0278-s_lc.fits` | 2460545.41040 | -0.01182 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.67459 | -0.01174 | 2 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460372.93292 | -0.01166 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.62823 | -0.01161 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460374.03849 | -0.01157 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460570.87130 | -0.01153 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.14352 | -0.01129 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.45879 | -0.01129 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.99543 | -0.01094 | 2 | SAP | 1, 2 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.48848 | -0.01093 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.14542 | -0.01070 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.09959 | -0.01056 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460388.17896 | -0.01041 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.17269 | -0.01041 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460561.97005 | -0.01031 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000189322727-0280-s_lc.fits` | 2460571.07269 | -0.01025 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000189322727-0271-s_lc.fits` | 2460373.32459 | -0.01008 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460543.77567 | 9187 | 12605 | 175.7705 | 4 / 175 | 175.77, 87.8853, 58.5902, 43.9426 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6111.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:58:21Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:58:25Z: TOI-6111.01 (TIC 189322727, disposition APC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:58:28Z: Gaia DR3 2070280099026014336 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:58:30Z: TYC 3165-991-1 (SB*); TYC 3165-441-1 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460368.0092: recovered, depth 12605 ± 843 ppm (catalogue 11944 ppm); BJD 2460373.8433: recovered, depth 5638 ± 998 ppm (catalogue 11944 ppm); BJD 2460379.6773: recovered, depth 11532 ± 769 ppm (catalogue 11944 ppm); BJD 2460385.5113: recovered, depth 8203 ± 900 ppm (catalogue 11944 ppm); BJD 2460391.3454: recovered, depth 12119 ± 762 ppm (catalogue 11944 ppm); BJD 2460537.1961: recovered, depth 9791 ± 687 ppm (catalogue 11944 ppm); BJD 2460543.0301: partial, depth 9509 ± 632 ppm (catalogue 11944 ppm); BJD 2460548.8641: partial, depth 10803 ± 550 ppm (catalogue 11944 ppm); BJD 2460554.6982: partial, depth 11853 ± 585 ppm (catalogue 11944 ppm); BJD 2460560.5322: partial, depth 8484 ± 616 ppm (catalogue 11944 ppm); BJD 2460566.3662: recovered, depth 7581 ± 587 ppm (catalogue 11944 ppm); BJD 2460572.2003: recovered, depth 13071 ± 753 ppm (catalogue 11944 ppm); BJD 2460578.0343: not recovered, depth 7443 ± 891 ppm (catalogue 11944 ppm); BJD 2460583.8683: recovered, depth 7282 ± 608 ppm (catalogue 11944 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460543.7757, ΔT = 175.771 d, 4 of 175 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (175.77, 87.8853, 58.5902, 43.9426 d); duration likelihood under Gaia priors (circular orbits) peaks at 43.9 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6111.01: Gaia DR3 2070280099026014336 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6111.01: Teff 5481 K, R* 1.00 ± 0.08, M* 0.99 ± 0.10, ρ* 1.00 ± 0.26 ρ☉ (dwarf sequence, M_G 4.74, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6111.01: 35 Gaia neighbour(s) within 52.5", contamination 82.29%; depth 12605 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 2070280137691639552, 29.6", ΔG -1.64); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460543.7757 suspect: MOM_CENTR1 z=-26.1, MOM_CENTR2 z=-18.9, POS_CORR1 z=-39.1, POS_CORR2 z=-14.1 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 1 light curve × candidate pair(s); aliases supported: none; excluded: none; 4 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-6111.01: Gaia DR3 2070280099026014336   ROT                            P=None at 0.7" |
| Object-class guard (SIMBAD) | inconclusive | TOI-6111.01: TYC 3165-441-1 otype SB* (multiple) at 0.1" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-6111.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6111-01.yaml
python -m cygnus.multi report campaigns/toi-6111-01.yaml
```
