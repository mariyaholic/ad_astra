<!-- [private Drive store] -->
# Known-object test, TOI-5861.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5861-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1019, calibrate_screen #1005, event_census #1010, fetch_products #1004, known_signal_recovery #1006, moving_objects #1012, period_aliases #1011, prior_art #1021, residual_screen #1009, stellar_context #1007, variability_guard #1020
- Runner finished (UTC): 2026-09-26T10:28:28Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 70 threshold entries forming **13 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5861.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 11034516 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 297.980126 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 24.038241 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459771.875591 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 26130.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.769 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.5375 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-08 12:04:59 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | lightcurve | 81 | False | `0ca2c97639b62bce` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | — | epoch not in this light curve | — | — | 26130 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.89985 | -0.03281 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.87207 | -0.03047 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.96235 | -0.02792 | 81 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.87971 | -0.02775 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.86026 | -0.02472 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460519.07977 | -0.02033 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.89221 | -0.01982 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460511.36167 | -0.02221 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460530.02554 | -0.02132 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460519.18949 | -0.01440 | 3 | SAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460512.83668 | -0.01382 | 2 | SAP | 1, 2 | no |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460529.86443 | -0.01232 | 2 | SAP | 1, 2, 3 | no |
| `tess2024196212429-s0081-0000000011034516-0276-s_lc.fits` | 2460513.61516 | -0.01215 | 3 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5861.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:28:25Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:28:26Z: TOI-5861.01 (TIC 11034516, disposition PC)
- VSX (done, 2026-09-26): 3 match(es) in VSX within 30" as of 2026-09-26T10:28:27Z: Gaia DR3 1828407095924871808 (type L, P — d); ZTF J195156.78+240233.8 (type SR, P 84.2102748 d); ZTF J195154.23+240222.5 (type SR, P 67.4015505 d)
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T10:28:28Z: ZTF J195154.23+240222.5 (LP*); 2MASS J19515596+2402024 (LP?); UCAC4 571-097318 (*); ZTF J195156.78+240233.8 (LP*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5861.01: Gaia DR3 1828407095924880128 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5861.01: Teff 5376 K, R* 0.96 ± 0.08, M* 0.98 ± 0.10, ρ* 1.09 ± 0.28 ρ☉ (dwarf sequence, M_G 4.86, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5861.01: 117 Gaia neighbour(s) within 52.5", contamination 57.70%; depth 26130 ppm (catalogue depth); 4 could produce it if fully eclipsed (brightest 1828407125967628416, 26.7", ΔG 0.34); a centroid test is needed |
| Pointing and quality census per event | failed | 7 persistent event(s), 6 clean; BJD 2460519.0798 suspect: manual exclude (in event), argabrightening (within ±0.25 d), coarse point (within ±0.25 d), MOM_CENTR1 z=-11.1, MOM_CENTR2 z=-13.5, POS_CORR1 z=-16.9, POS_CORR2 z=-51.5, SAP_BKG z=+734.1 |
| Moving objects at screen-event epochs | inconclusive | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5861.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5861.01: UCAC4 571-097318 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5861-01.yaml
python -m cygnus.multi report campaigns/toi-5861-01.yaml
```
