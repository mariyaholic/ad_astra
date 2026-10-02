<!-- cygnus:generated-draft -->
# Known-object test, TOI-746.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-746-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4368, calibrate_screen #4344, event_census #4348, fetch_independent #4351, fetch_products #4323, known_signal_recovery #4345, moving_objects #4350, period_aliases #4349, prior_art #4370, residual_screen #4347, stellar_context #4346, variability_guard #4369
- Runner finished (UTC): 2026-09-30T21:49:55Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-746.01 (BJD 2458599.2987: gap (catalogue 8276 ppm); BJD 2458610.2791: gap (catalogue 8276 ppm); BJD 2458621.2594: recovered, depth 5588 ± 322 ppm (catalogue 8276 ppm); BJD 2458632.2397: recovered, depth 5519 ± 456 ppm (catalogue 8276 ppm); BJD 2458643.2200: recovered, depth 8361 ± 512 ppm (catalogue 8276 ppm); BJD 2458654.2003: gap (catalogue 8276 ppm); BJD 2458665.1806: recovered, depth 4346 ± 427 ppm (catalogue 8276 ppm); BJD 2458676.1609: partial, depth 4973 ± 418 ppm (catalogue 8276 ppm); BJD 2459071.4521: gap (catalogue 8276 ppm); BJD 2459082.4324: recovered, depth 6405 ± 297 ppm (catalogue 8276 ppm); BJD 2459093.4128: partial, depth 5370 ± 454 ppm (catalogue 8276 ppm); BJD 2459104.3931: partial, depth 5130 ± 392 ppm (catalogue 8276 ppm); BJD 2459126.3537: not recovered, depth 2911 ± 540 ppm (catalogue 8276 ppm); BJD 2459137.3340: not recovered, depth 5692 ± 502 ppm (catalogue 8276 ppm)).
Outside the catalogued epoch the screen left 65 threshold entries forming **27 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-746.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 167418903 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 99.620795 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -67.64895 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458599.298747 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 10.9803114 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8276.212333 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.0361453 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.3786 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-19 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | lightcurve | 11 | True | `b66671ea624f23d4` | True |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | lightcurve | 12 | False | `1a38462748970bb5` | True |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | lightcurve | 13 | False | `bc25c426843ead6a` | True |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | lightcurve | 28 | False | `7a7dc43125bb5338` | True |
| `tess2020238165205-s0029-0000000167418903-0193-s_lc.fits` | lightcurve | 29 | False | `20533902ae665871` | True |
| `tess2020266004630-s0030-0000000167418903-0195-s_lc.fits` | lightcurve | 30 | False | `6b90b67b5eeb623e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458599.29875 | gap | 0 | — | 8276 | — |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458610.27906 | gap | 0 | — | 8276 | — |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458621.25937 | recovered | 61 | 5588 ± 322 | 8276 | -0.01 |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458632.23968 | recovered | 56 | 5519 ± 456 | 8276 | -0.13 |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458643.21999 | recovered | 45 | 8361 ± 512 | 8276 | 0.00 |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458654.20030 | gap | 0 | — | 8276 | — |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458665.18062 | recovered | 61 | 4346 ± 427 | 8276 | 0.11 |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458676.16093 | partial | 61 | 4973 ± 418 | 8276 | 0.06 |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | 2459071.45214 | gap | 0 | — | 8276 | — |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | 2459082.43245 | recovered | 61 | 6405 ± 297 | 8276 | 0.02 |
| `tess2020238165205-s0029-0000000167418903-0193-s_lc.fits` | 2459093.41276 | partial | 61 | 5370 ± 454 | 8276 | -0.02 |
| `tess2020238165205-s0029-0000000167418903-0193-s_lc.fits` | 2459104.39307 | partial | 61 | 5130 ± 392 | 8276 | -0.01 |
| `tess2020266004630-s0030-0000000167418903-0195-s_lc.fits` | 2459126.35369 | not_recovered | 61 | 2911 ± 540 | 8276 | — |
| `tess2020266004630-s0030-0000000167418903-0195-s_lc.fits` | 2459137.33401 | not_recovered | 61 | 5692 ± 502 | 8276 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020238165205-s0029-0000000167418903-0193-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2020266004630-s0030-0000000167418903-0195-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458657.76864 | -0.02388 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458661.47557 | -0.01840 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458664.89915 | -0.01750 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458628.62159 | -0.01638 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458658.38114 | -0.01576 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458628.88131 | -0.01483 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458629.44937 | -0.01480 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458661.14362 | -0.01369 | 2 | SAP | 1, 2 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458629.51881 | -0.01328 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458638.62848 | -0.01263 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458658.35892 | -0.01234 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458658.69919 | -0.01193 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458661.03807 | -0.01109 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458638.67015 | -0.01098 | 2 | SAP | 1, 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458638.45071 | -0.01004 | 2 | SAP | 3 | no |
| `tess2019169103026-s0013-0000000167418903-0146-s_lc.fits` | 2458657.67003 | -0.00936 | 2 | PDCSAP | 2, 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458643.48401 | -0.00924 | 2 | PDCSAP | 3 | no |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | 2459075.39729 | -0.00917 | 2 | SAP | 3 | no |
| `tess2020212050318-s0028-0000000167418903-0190-s_lc.fits` | 2459075.15840 | -0.00911 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458629.32298 | -0.00899 | 2 | PDCSAP | 1 | no |
| `tess2019140104343-s0012-0000000167418903-0144-s_lc.fits` | 2458652.50896 | -0.00895 | 2 | PDCSAP | 3 | no |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458609.51611 | -0.00823 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458609.59250 | -0.00810 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458603.46613 | -0.00797 | 2 | SAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458609.60639 | -0.00797 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458603.18280 | -0.00723 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000167418903-0143-s_lc.fits` | 2458615.89526 | -0.00694 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-746.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:49:48Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:49:51Z: TOI-746.01 (TIC 167418903, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:49:53Z: Gaia DR3 5280334193589882496 (type RRAB, P 0.61218 d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:49:54Z: TOI-746b (Pl); OGLE LMC-RRLYR-40864 (RR*); TOI-746 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458599.2987: gap (catalogue 8276 ppm); BJD 2458610.2791: gap (catalogue 8276 ppm); BJD 2458621.2594: recovered, depth 5588 ± 322 ppm (catalogue 8276 ppm); BJD 2458632.2397: recovered, depth 5519 ± 456 ppm (catalogue 8276 ppm); BJD 2458643.2200: recovered, depth 8361 ± 512 ppm (catalogue 8276 ppm); BJD 2458654.2003: gap (catalogue 8276 ppm); BJD 2458665.1806: recovered, depth 4346 ± 427 ppm (catalogue 8276 ppm); BJD 2458676.1609: partial, depth 4973 ± 418 ppm (catalogue 8276 ppm); BJD 2459071.4521: gap (catalogue 8276 ppm); BJD 2459082.4324: recovered, depth 6405 ± 297 ppm (catalogue 8276 ppm); BJD 2459093.4128: partial, depth 5370 ± 454 ppm (catalogue 8276 ppm); BJD 2459104.3931: partial, depth 5130 ± 392 ppm (catalogue 8276 ppm); BJD 2459126.3537: not recovered, depth 2911 ± 540 ppm (catalogue 8276 ppm); BJD 2459137.3340: not recovered, depth 5692 ± 502 ppm (catalogue 8276 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-746.01: Gaia DR3 5280337144228825472 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-746.01: Teff 5611 K, R* 0.94 ± 0.08, M* 0.97 ± 0.10, ρ* 1.15 ± 0.30 ρ☉ (dwarf sequence, M_G 4.93, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-746.01: 13 Gaia neighbour(s) within 52.5", contamination 73.96%; depth 5588 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 5280337148528151808, 30.9", ΔG -1.12); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-746.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-746.01: TOI-746b otype Pl (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-746-01.yaml
python -m cygnus.multi report campaigns/toi-746-01.yaml
```
