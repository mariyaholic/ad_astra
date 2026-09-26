<!-- cygnus:generated-draft -->
# Known-object test, TOI-162.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-162-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #789, calibrate_screen #782, event_census #786, fetch_products #781, known_signal_recovery #783, moving_objects #788, period_aliases #787, prior_art #791, residual_screen #785, stellar_context #784, variability_guard #790
- Runner finished (UTC): 2026-09-26T10:19:21Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 33 threshold entries forming **11 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-162.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 99493790 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 317.639908 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -23.305817 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459078.393053 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 24530.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.185 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6834 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2022-03-29 16:02:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | lightcurve | 92 | False | `3ac14459318495b4` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | — | epoch not in this light curve | — | — | 24530 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460809.91744 | -0.02364 | 84 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460817.68483 | -0.02212 | 77 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460825.44596 | -0.01995 | 80 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460817.62718 | -0.01115 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460814.30048 | -0.01279 | 2 | PDCSAP | 2, 3 | no |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460814.21020 | -0.01095 | 2 | PDCSAP | 3 | no |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460814.43105 | -0.01092 | 2 | PDCSAP | 3 | no |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460814.26437 | -0.01059 | 2 | PDCSAP | 3 | no |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460817.74108 | -0.01024 | 2 | PDCSAP | 2 | no |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460823.19020 | -0.00909 | 2 | SAP | 1, 2 | no |
| `tess2025127075000-s0092-0000000099493790-0289-s_lc.fits` | 2460825.50499 | -0.00900 | 3 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-162.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:19:18Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:19:19Z: TOI-162.01 (TIC 99493790, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:19:21Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:19:21Z: TOI-162.01 (err); TOI-162 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-162.01: Gaia DR3 6804708139515008640 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.03") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-162.01: Teff 5426 K, R* 0.93 ± 0.07, M* 0.96 ± 0.10, ρ* 1.17 ± 0.30 ρ☉ (dwarf sequence, M_G 4.97, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-162.01: 5 Gaia neighbour(s) within 52.5", contamination 3.36%; depth 24530 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 4 persistent event(s), 3 clean; BJD 2460809.9174 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR2 z=+10.5 |
| Moving objects at screen-event epochs | inconclusive | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-162.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-162.01: TOI-162.01 otype err (star_or_other) at 0.8" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-162-01.yaml
python -m cygnus.multi report campaigns/toi-162-01.yaml
```
