<!-- cygnus:generated-draft -->
# Known-object test, TOI-3445.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3445-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4558, calibrate_screen #4538, event_census #4544, fetch_independent #4554, fetch_products #4531, known_signal_recovery #4541, moving_objects #4550, period_aliases #4545, prior_art #4563, residual_screen #4543, stellar_context #4542, variability_guard #4559
- Runner finished (UTC): 2026-09-30T22:00:53Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3445.01 (BJD 2460069.3149: recovered, depth 19876 ± 891 ppm (catalogue 14000 ppm); BJD 2460072.3016: recovered, depth 15054 ± 762 ppm (catalogue 14000 ppm); BJD 2460075.2883: recovered, depth 14989 ± 804 ppm (catalogue 14000 ppm); BJD 2460078.2749: recovered, depth 15476 ± 816 ppm (catalogue 14000 ppm); BJD 2460081.2616: recovered, depth 16220 ± 822 ppm (catalogue 14000 ppm); BJD 2460084.2483: recovered, depth 14590 ± 790 ppm (catalogue 14000 ppm); BJD 2460087.2350: recovered, depth 13958 ± 785 ppm (catalogue 14000 ppm); BJD 2460090.2217: recovered, depth 10485 ± 928 ppm (catalogue 14000 ppm); BJD 2460093.2084: recovered, depth 14995 ± 904 ppm (catalogue 14000 ppm); BJD 2460096.1950: gap (catalogue 14000 ppm); BJD 2461153.4810: recovered, depth 24187 ± 1034 ppm (catalogue 14000 ppm); BJD 2461156.4677: recovered, depth 20190 ± 929 ppm (catalogue 14000 ppm); BJD 2461159.4544: recovered, depth 20539 ± 925 ppm (catalogue 14000 ppm); BJD 2461162.4411: recovered, depth 16607 ± 925 ppm (catalogue 14000 ppm); BJD 2461165.4278: gap (catalogue 14000 ppm); BJD 2461168.4145: recovered, depth 16567 ± 983 ppm (catalogue 14000 ppm); BJD 2461171.4011: partial, depth 12882 ± 1522 ppm (catalogue 14000 ppm); BJD 2461174.3878: recovered, depth 19474 ± 950 ppm (catalogue 14000 ppm); BJD 2461177.3745: partial, depth 11870 ± 999 ppm (catalogue 14000 ppm)).
Outside the catalogued epoch the screen left 25 threshold entries forming **14 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461153.0491 matches the catalogued transit's depth (17225 vs 19876 ppm), 1083.748 d later; 42 of 1083 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3445.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 364431259 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 244.138351 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -41.073966 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459382.37766 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.9866836 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14000.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.681 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8311 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | lightcurve | 65 | False | `1b0fb6880da6195c` | True |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | lightcurve | 103 | False | `cf0b2310ea68e9af` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460069.31489 | recovered | 80 | 19876 ± 891 | 14000 | -0.34 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460072.30157 | recovered | 81 | 15054 ± 762 | 14000 | -0.25 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460075.28826 | recovered | 80 | 14989 ± 804 | 14000 | 0.40 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460078.27494 | recovered | 81 | 15476 ± 816 | 14000 | -0.23 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460081.26162 | recovered | 81 | 16220 ± 822 | 14000 | -0.01 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460084.24831 | recovered | 80 | 14590 ± 790 | 14000 | 0.62 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460087.23499 | recovered | 81 | 13958 ± 785 | 14000 | 0.32 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460090.22167 | recovered | 67 | 10485 ± 928 | 14000 | -0.58 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460093.20836 | recovered | 80 | 14995 ± 904 | 14000 | -0.31 |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460096.19504 | gap | 0 | — | 14000 | — |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461153.48103 | recovered | 80 | 24187 ± 1034 | 14000 | -0.10 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461156.46772 | recovered | 81 | 20190 ± 929 | 14000 | -0.28 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461159.45440 | recovered | 81 | 20539 ± 925 | 14000 | 0.61 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461162.44109 | recovered | 80 | 16607 ± 925 | 14000 | 0.57 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461165.42777 | gap | 0 | — | 14000 | — |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461168.41445 | recovered | 81 | 16567 ± 983 | 14000 | -0.72 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461171.40114 | partial | 36 | 12882 ± 1522 | 14000 | -0.38 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461174.38782 | recovered | 80 | 19474 ± 950 | 14000 | -0.09 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461177.37450 | partial | 78 | 11870 ± 999 | 14000 | 0.22 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461153.04905 | -0.03821 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461153.06017 | -0.02902 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461170.96655 | -0.02925 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460089.79141 | -0.02696 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461171.16794 | -0.02548 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461171.06655 | -0.02476 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461170.98877 | -0.02355 | 4 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461171.07350 | -0.02303 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000364431259-0305-s_lc.fits` | 2461170.95335 | -0.02295 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460089.44696 | -0.02159 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460083.71216 | -0.02129 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460089.83030 | -0.02123 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460083.04409 | -0.02073 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000364431259-0259-s_lc.fits` | 2460089.41085 | -0.02018 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461153.04905 | 17225 | 19876 | 1083.7484 | 42 / 1083 | 1083.75, 541.874, 361.25, 270.937, 216.75, 180.625, 154.821, 135.469, 120.416, 108.375, 98.5226, 90.3124, 83.3653, 77.4106, 72.2499, 67.7343, 63.7499, 60.2082, 57.0394, 54.1874 |
| 2461153.06017 | 12376 | 19876 | 1083.7596 | 42 / 1083 | 1083.76, 541.88, 361.253, 270.94, 216.752, 180.627, 154.823, 135.47, 120.418, 108.376, 98.5236, 90.3133, 83.3661, 77.4114, 72.2506, 67.735, 63.7506, 60.2089, 57.04, 54.188 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3445.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:00:41Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:00:45Z: TOI-3445.01 (TIC 364431259, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:00:47Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:00:49Z: TOI-3445 (*); TOI-3445.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460069.3149: recovered, depth 19876 ± 891 ppm (catalogue 14000 ppm); BJD 2460072.3016: recovered, depth 15054 ± 762 ppm (catalogue 14000 ppm); BJD 2460075.2883: recovered, depth 14989 ± 804 ppm (catalogue 14000 ppm); BJD 2460078.2749: recovered, depth 15476 ± 816 ppm (catalogue 14000 ppm); BJD 2460081.2616: recovered, depth 16220 ± 822 ppm (catalogue 14000 ppm); BJD 2460084.2483: recovered, depth 14590 ± 790 ppm (catalogue 14000 ppm); BJD 2460087.2350: recovered, depth 13958 ± 785 ppm (catalogue 14000 ppm); BJD 2460090.2217: recovered, depth 10485 ± 928 ppm (catalogue 14000 ppm); BJD 2460093.2084: recovered, depth 14995 ± 904 ppm (catalogue 14000 ppm); BJD 2460096.1950: gap (catalogue 14000 ppm); BJD 2461153.4810: recovered, depth 24187 ± 1034 ppm (catalogue 14000 ppm); BJD 2461156.4677: recovered, depth 20190 ± 929 ppm (catalogue 14000 ppm); BJD 2461159.4544: recovered, depth 20539 ± 925 ppm (catalogue 14000 ppm); BJD 2461162.4411: recovered, depth 16607 ± 925 ppm (catalogue 14000 ppm); BJD 2461165.4278: gap (catalogue 14000 ppm); BJD 2461168.4145: recovered, depth 16567 ± 983 ppm (catalogue 14000 ppm); BJD 2461171.4011: partial, depth 12882 ± 1522 ppm (catalogue 14000 ppm); BJD 2461174.3878: recovered, depth 19474 ± 950 ppm (catalogue 14000 ppm); BJD 2461177.3745: partial, depth 11870 ± 999 ppm (catalogue 14000 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 2 repeat-candidate event(s); first at BJD 2461153.0491, ΔT = 1083.748 d, 42 of 1083 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1083.75, 541.874, 361.25, 270.937, 216.75, 180.625, 154.821, 135.469, 120.416, 108.375, 98.5226, 90.3124 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3445.01: Gaia DR3 5993818043474139392 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3445.01: dwarf priors not applied — 1.14 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3445.01: 117 Gaia neighbour(s) within 52.5", contamination 51.91%; depth 19876 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 5993818112193633280, 50.2", ΔG 1.48); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2461153.0491 suspect: scattered light 2 (in event), POS_CORR1 z=-9.2, POS_CORR2 z=-6.4, SAP_BKG z=+20.0; BJD 2461153.0602 suspect: scattered light 2 (in event), MOM_CENTR1 z=-5.3, POS_CORR1 z=-11.0, POS_CORR2 z=-8.0, SAP_BKG z=+23.3 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3445.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3445.01: TOI-3445 otype * (star_or_other) at 0.3" |
| Event-time prior art | inconclusive | 2 possible published-ephemeris overlap(s) within 1 d (TOI-3445.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3445-01.yaml
python -m cygnus.multi report campaigns/toi-3445-01.yaml
```
