<!-- [private Drive store] -->
# Known-object test, TOI-890.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-890-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #148, calibrate_screen #72, event_census #86, fetch_products #71, known_signal_recovery #77, moving_objects #125, period_aliases #89, prior_art #151, residual_screen #82, stellar_context #78, variability_guard #149
- Runner finished (UTC): 2026-09-26T09:55:23Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-890.01 (BJD 2459226.7411: recovered, depth 30367 ± 566 ppm (catalogue 41820 ppm)).
Outside the catalogued epoch the screen left 79 threshold entries forming **14 distinct event(s)**, **13 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459204.3228 matches the catalogued transit's depth (38508 vs 30367 ppm), 22.424 d later; 0 of 22 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-890.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 333607525 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 100.36319 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -12.285043 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459226.741148 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 41820.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.51 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.936 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2022-07-11 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | lightcurve | 33 | True | `5f1086ae2aee3db1` | True |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | lightcurve | 87 | False | `11e2b633a92b935c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459226.74115 | recovered | 105 | 30367 ± 566 | 41820 | 0.14 |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | — | epoch not in this light curve | — | — | 41820 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459223.53403 | -0.04331 | 97 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459210.72709 | -0.04280 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460674.17523 | -0.04196 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459217.13406 | -0.04033 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459204.32283 | -0.04005 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460686.98352 | -0.03870 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459220.33406 | -0.03847 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460670.97520 | -0.03811 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460683.78146 | -0.03718 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460680.58217 | -0.03615 | 85 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460667.76682 | -0.03548 | 86 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459207.52914 | -0.03211 | 86 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000333607525-0284-s_lc.fits` | 2460674.23982 | -0.01583 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2020351194500-s0033-0000000333607525-0203-s_lc.fits` | 2459220.40211 | -0.01324 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459204.32283 | 38508 | 30367 | 22.4243 | 0 / 22 |  |
| 2459207.52914 | 30364 | 30367 | 19.2180 | 0 / 19 |  |
| 2459210.72709 | 40757 | 30367 | 16.0201 | 0 / 16 |  |
| 2459217.13406 | 39261 | 30367 | 9.6131 | 0 / 9 |  |
| 2459220.33406 | 36801 | 30367 | 6.4131 | 0 / 6 |  |
| 2459223.53403 | 42479 | 30367 | 3.2131 | 0 / 3 |  |
| 2460667.76682 | 33712 | 30367 | 1441.0196 | 66 / 1441 | 1441.02, 720.51, 480.34, 360.255, 288.204, 240.17, 205.86, 180.127, 160.113, 144.102, 131.002, 120.085, 110.848, 102.93, 96.068, 90.0637, 84.7659, 80.0566, 75.8431, 72.051 |
| 2460670.97520 | 36975 | 30367 | 1444.2280 | 68 / 1444 | 1444.23, 722.114, 481.409, 361.057, 288.846, 240.705, 206.318, 180.529, 160.47, 144.423, 131.293, 120.352, 111.094, 103.159, 96.2819, 90.2643, 84.9546, 80.2349, 76.012, 72.2114 |
| 2460674.17523 | 39865 | 30367 | 1447.4280 | 64 / 1447 | 1447.43, 723.714, 482.476, 361.857, 289.486, 241.238, 206.775, 180.929, 160.825, 144.743, 131.584, 120.619, 111.341, 103.388, 96.4952, 90.4643, 85.1428, 80.4127, 76.1804, 72.3714 |
| 2460680.58217 | 34096 | 30367 | 1453.8350 | 67 / 1453 | 1453.84, 726.918, 484.612, 363.459, 290.767, 242.306, 207.691, 181.729, 161.537, 145.383, 132.167, 121.153, 111.834, 103.845, 96.9223, 90.8647, 85.5197, 80.7686, 76.5176, 72.6917 |
| 2460683.78146 | 35101 | 30367 | 1457.0343 | 68 / 1457 | 1457.03, 728.517, 485.678, 364.259, 291.407, 242.839, 208.148, 182.129, 161.893, 145.703, 132.458, 121.419, 112.08, 104.074, 97.1356, 91.0646, 85.7079, 80.9463, 76.686, 72.8517 |
| 2460686.98352 | 37476 | 30367 | 1460.2363 | 67 / 1460 | 1460.24, 730.118, 486.745, 365.059, 292.047, 243.373, 208.605, 182.53, 162.249, 146.024, 132.749, 121.686, 112.326, 104.303, 97.3491, 91.2648, 85.8963, 81.1242, 76.8545, 73.0118 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-890.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:55:19Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:55:21Z: TOI-890.01 (TIC 333607525, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:55:22Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T09:55:22Z: TOI-890.01 (err); Gaia DR3 2953400695932187904 (*); TOI-890 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459226.7411: recovered, depth 30367 ± 566 ppm (catalogue 41820 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 12 repeat-candidate event(s); first at BJD 2459204.3228, ΔT = 22.424 d, 0 of 22 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | inconclusive | TOI-890.01: Gaia DR3 2953400695928635648 at 0.04" (propagated 2016.0 → J2015.5; 0.04" unpropagated; another source 0.41" away, ΔG 0.550001) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-890.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-890.01: 29 Gaia neighbour(s) within 52.5", contamination 46.50%; depth 30367 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 2953400695932187904, 0.4", ΔG 0.55); a centroid test is needed |
| Pointing and quality census per event | failed | 13 persistent event(s), 3 clean; BJD 2459204.3228 suspect: MOM_CENTR1 z=-6.0; BJD 2459207.5291 suspect: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-6.9; BJD 2459210.7271 suspect: MOM_CENTR1 z=-7.6; BJD 2459217.1341 suspect: MOM_CENTR1 z=-6.5 |
| Moving objects at screen-event epochs | passed | 13 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-890.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-890.01: TOI-890 otype * (star_or_other) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-890-01.yaml
python -m cygnus.multi report campaigns/toi-890-01.yaml
```
