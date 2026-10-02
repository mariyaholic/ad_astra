<!-- cygnus:generated-draft -->
# Known-object test, TOI-4028.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4028-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5046, calibrate_screen #5038, event_census #5042, fetch_independent #5045, fetch_products #5033, known_signal_recovery #5039, moving_objects #5044, period_aliases #5043, prior_art #5048, residual_screen #5041, stellar_context #5040, variability_guard #5047
- Runner finished (UTC): 2026-09-30T22:54:43Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4028.01 (BJD 2459884.2859: recovered, depth 13592 ± 953 ppm (catalogue 16160 ppm); BJD 2459888.2448: recovered, depth 15390 ± 982 ppm (catalogue 16160 ppm); BJD 2459892.2037: recovered, depth 13321 ± 915 ppm (catalogue 16160 ppm); BJD 2459896.1626: gap (catalogue 16160 ppm); BJD 2459900.1216: not recovered, depth 11225 ± 918 ppm (catalogue 16160 ppm); BJD 2459904.0805: recovered, depth 13330 ± 947 ppm (catalogue 16160 ppm); BJD 2459908.0394: partial, depth 11900 ± 923 ppm (catalogue 16160 ppm); BJD 2459721.9704: recovered, depth 13644 ± 963 ppm (catalogue 16160 ppm); BJD 2459725.9293: recovered, depth 12779 ± 919 ppm (catalogue 16160 ppm); BJD 2459729.8882: recovered, depth 10242 ± 908 ppm (catalogue 16160 ppm); BJD 2459733.8472: recovered, depth 12816 ± 1023 ppm (catalogue 16160 ppm); BJD 2459737.8061: recovered, depth 13134 ± 966 ppm (catalogue 16160 ppm); BJD 2459741.7650: recovered, depth 14331 ± 914 ppm (catalogue 16160 ppm); BJD 2460434.5750: not recovered, depth 4033 ± 954 ppm (catalogue 16160 ppm); BJD 2460438.5339: recovered, depth 10866 ± 881 ppm (catalogue 16160 ppm); BJD 2460442.4928: partial, depth 13291 ± 904 ppm (catalogue 16160 ppm); BJD 2460446.4517: partial, depth 12536 ± 938 ppm (catalogue 16160 ppm); BJD 2460450.4106: recovered, depth 10518 ± 891 ppm (catalogue 16160 ppm)).
Outside the catalogued epoch the screen left 26 threshold entries forming **11 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460445.5158 matches the catalogued transit's depth (7191 vs 13592 ppm), 561.221 d later; 15 of 561 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4028.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 406634633 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 355.230606 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 69.974452 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459884.285896 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.9589142 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16160.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.42 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.0911 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-09 12:03:38 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | lightcurve | 58 | True | `51348044efe09b32` | True |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | lightcurve | 52 | False | `a768c06d788acbbf` | True |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | lightcurve | 78 | False | `ed3bf6a8dc6c1d0b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459884.28590 | recovered | 72 | 13592 ± 953 | 16160 | 0.20 |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459888.24481 | recovered | 73 | 15390 ± 982 | 16160 | -0.24 |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459892.20372 | recovered | 73 | 13321 ± 915 | 16160 | -0.08 |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459896.16264 | gap | 0 | — | 16160 | — |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459900.12155 | not_recovered | 73 | 11225 ± 918 | 16160 | — |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459904.08047 | recovered | 72 | 13330 ± 947 | 16160 | 0.23 |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459908.03938 | partial | 73 | 11900 ± 923 | 16160 | 0.72 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2459721.97041 | recovered | 73 | 13644 ± 963 | 16160 | -0.16 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2459725.92933 | recovered | 72 | 12779 ± 919 | 16160 | -0.54 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2459729.88824 | recovered | 73 | 10242 ± 908 | 16160 | -0.08 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2459733.84716 | recovered | 72 | 12816 ± 1023 | 16160 | -0.16 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2459737.80607 | recovered | 72 | 13134 ± 966 | 16160 | 0.29 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2459741.76498 | recovered | 73 | 14331 ± 914 | 16160 | 0.23 |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2460434.57497 | not_recovered | 73 | 4033 ± 954 | 16160 | — |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2460438.53388 | recovered | 72 | 10866 ± 881 | 16160 | 0.50 |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2460442.49280 | partial | 73 | 13291 ± 904 | 16160 | 0.32 |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2460446.45171 | partial | 72 | 12536 ± 938 | 16160 | -0.76 |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2460450.41063 | recovered | 73 | 10518 ± 891 | 16160 | -0.30 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2022138205153-s0052-0000000406634633-0224-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024114025118-s0078-0000000406634633-0273-s_lc.fits` | 2460445.51580 | -0.02509 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.64292 | -0.02113 | 2 | SAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.49986 | -0.01980 | 2 | SAP | 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.58875 | -0.01920 | 2 | SAP | 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.46792 | -0.01804 | 2 | SAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.47486 | -0.01754 | 2 | SAP | 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.39709 | -0.01751 | 2 | SAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.37070 | -0.01742 | 2 | SAP | 1, 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.44848 | -0.01699 | 2 | SAP | 2, 3 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459882.62487 | -0.01562 | 2 | SAP | 2 | no |
| `tess2022302161335-s0058-0000000406634633-0247-s_lc.fits` | 2459897.11793 | -0.01546 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460445.51580 | 7191 | 13592 | 561.2215 | 15 / 561 | 561.221, 280.611, 187.074, 140.305, 112.244, 93.5369, 70.1527, 62.3579, 56.1221, 51.0201, 46.7685, 43.1709, 35.0763, 33.013, 28.0611 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4028.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:54:34Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:54:37Z: TOI-4028.01 (TIC 406634633, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:54:39Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:54:41Z: TOI-4028 (*); TOI-4028.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459884.2859: recovered, depth 13592 ± 953 ppm (catalogue 16160 ppm); BJD 2459888.2448: recovered, depth 15390 ± 982 ppm (catalogue 16160 ppm); BJD 2459892.2037: recovered, depth 13321 ± 915 ppm (catalogue 16160 ppm); BJD 2459896.1626: gap (catalogue 16160 ppm); BJD 2459900.1216: not recovered, depth 11225 ± 918 ppm (catalogue 16160 ppm); BJD 2459904.0805: recovered, depth 13330 ± 947 ppm (catalogue 16160 ppm); BJD 2459908.0394: partial, depth 11900 ± 923 ppm (catalogue 16160 ppm); BJD 2459721.9704: recovered, depth 13644 ± 963 ppm (catalogue 16160 ppm); BJD 2459725.9293: recovered, depth 12779 ± 919 ppm (catalogue 16160 ppm); BJD 2459729.8882: recovered, depth 10242 ± 908 ppm (catalogue 16160 ppm); BJD 2459733.8472: recovered, depth 12816 ± 1023 ppm (catalogue 16160 ppm); BJD 2459737.8061: recovered, depth 13134 ± 966 ppm (catalogue 16160 ppm); BJD 2459741.7650: recovered, depth 14331 ± 914 ppm (catalogue 16160 ppm); BJD 2460434.5750: not recovered, depth 4033 ± 954 ppm (catalogue 16160 ppm); BJD 2460438.5339: recovered, depth 10866 ± 881 ppm (catalogue 16160 ppm); BJD 2460442.4928: partial, depth 13291 ± 904 ppm (catalogue 16160 ppm); BJD 2460446.4517: partial, depth 12536 ± 938 ppm (catalogue 16160 ppm); BJD 2460450.4106: recovered, depth 10518 ± 891 ppm (catalogue 16160 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460445.5158, ΔT = 561.221 d, 15 of 561 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (561.221, 280.611, 187.074, 140.305, 112.244, 93.5369, 70.1527, 62.3579, 56.1221, 51.0201, 46.7685, 43.1709 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4028.01: Gaia DR3 2215248924742863872 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-4028.01: dwarf priors not applied — 1.01 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4028.01: 33 Gaia neighbour(s) within 52.5", contamination 48.03%; depth 13592 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 2215248168829362944, 15.7", ΔG 0.69); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460445.5158 suspect: argabrightening (in event), coarse point (in event), manual exclude (in event), momentum dump (within ±0.25 d), MOM_CENTR2 z=-6.3, POS_CORR1 z=-6.8, POS_CORR2 z=-5.3, SAP_BKG z=-6.7 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 4 light curve × candidate pair(s); aliases supported: none; excluded: none; 60 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-4028.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4028.01: TOI-4028 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-4028.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4028-01.yaml
python -m cygnus.multi report campaigns/toi-4028-01.yaml
```
