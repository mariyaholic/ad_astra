<!-- [private Drive store] -->
# Known-object test, TOI-316.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-316-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #188, calibrate_screen #172, event_census #179, fetch_products #171, known_signal_recovery #173, moving_objects #181, period_aliases #180, prior_art #190, residual_screen #175, stellar_context #174, variability_guard #189
- Runner finished (UTC): 2026-09-26T09:56:32Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 73 threshold entries forming **14 distinct event(s)**, **9 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-316.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 8988289 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 354.759157 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -9.882022 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458365.98759 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 95718.1 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.561 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.1186 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2022-07-20 12:03:42 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | lightcurve | 29 | False | `f497e3ff06bc6217` | True |
| `tess2021232031932-s0042-0000000008988289-0213-s_lc.fits` | lightcurve | 42 | False | `833cc6aa783917d0` | True |
| `tess2023263165758-s0070-0000000008988289-0265-s_lc.fits` | lightcurve | 70 | False | `88f9e66a4fff456b` | True |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | lightcurve | 92 | False | `fa8716e3dc743cf8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | — | epoch not in this light curve | — | — | 95718 | — |
| `tess2021232031932-s0042-0000000008988289-0213-s_lc.fits` | — | epoch not in this light curve | — | — | 95718 | — |
| `tess2023263165758-s0070-0000000008988289-0265-s_lc.fits` | — | epoch not in this light curve | — | — | 95718 | — |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | — | epoch not in this light curve | — | — | 95718 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2021232031932-s0042-0000000008988289-0213-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2023263165758-s0070-0000000008988289-0265-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 2460821.68000 | -0.04700 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 2460821.70917 | -0.04257 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 2460808.34409 | -0.04237 | 25 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 2460821.67514 | -0.03951 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 2460821.71681 | -0.03571 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2459098.47120 | -0.02182 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2459098.59621 | -0.02106 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2459098.60871 | -0.02025 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023263165758-s0070-0000000008988289-0265-s_lc.fits` | 2460211.53316 | -0.01992 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025127075000-s0092-0000000008988289-0289-s_lc.fits` | 2460821.66958 | -0.03336 | 2 | PDCSAP | 1, 2 | no |
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2459102.49764 | -0.02091 | 2 | SAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2459098.51704 | -0.01936 | 2 | SAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000008988289-0193-s_lc.fits` | 2459098.39898 | -0.01910 | 2 | SAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000008988289-0265-s_lc.fits` | 2460208.93945 | -0.01854 | 3 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-316.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:56:27Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:56:28Z: TOI-316.01 (TIC 8988289, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T09:56:30Z: Gaia DR3 2435626548553370880 (type ROT, P — d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:56:30Z: TOI-316.01 (err); TOI-316 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-316.01: Gaia DR3 2435626548553370880 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-316.01: dwarf priors not applied — RUWE 2.8389704 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-316.01: 1 Gaia neighbour(s) within 52.5", contamination 2.01%; depth 95718 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 9 persistent event(s), 6 clean; BJD 2459098.4712 suspect: POS_CORR2 z=-8.4, SAP_BKG z=+21.5; BJD 2459098.5962 suspect: argabrightening (within ±0.25 d), MOM_CENTR2 z=-6.3, POS_CORR2 z=-8.5, SAP_BKG z=+25.2; BJD 2459098.6087 suspect: argabrightening (within ±0.25 d), MOM_CENTR2 z=-6.6, POS_CORR2 z=-8.3, SAP_BKG z=+25.9 |
| Moving objects at screen-event epochs | inconclusive | 9 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-316.01: Gaia DR3 2435626548553370880   ROT                            P=None at 0.6" |
| Object-class guard (SIMBAD) | passed | TOI-316.01: TOI-316 otype * (star_or_other) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-316-01.yaml
python -m cygnus.multi report campaigns/toi-316-01.yaml
```
