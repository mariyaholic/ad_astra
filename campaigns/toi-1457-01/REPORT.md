<!-- cygnus:generated-draft -->
# Known-object test, TOI-1457.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1457-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1098, calibrate_screen #1078, event_census #1082, fetch_products #1077, known_signal_recovery #1079, moving_objects #1096, period_aliases #1083, prior_art #1100, residual_screen #1081, stellar_context #1080, variability_guard #1099
- Runner finished (UTC): 2026-09-26T10:36:14Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1457.01 (BJD 2460602.8860: recovered, depth 1753 ± 54 ppm (catalogue 2760 ppm)).
Outside the catalogued epoch the screen left 613 threshold entries forming **205 distinct event(s)**, **38 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460590.0929 matches the catalogued transit's depth (1255 vs 1753 ppm), 12.795 d later; 0 of 12 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1457.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 176860064 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 354.836651 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 45.719851 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460602.885963 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 2760.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.752 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 7.1145 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-05-02 16:23:22 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | lightcurve | 84 | True | `f962156ed2b6361f` | True |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | lightcurve | 17 | False | `675409b1e599d37c` | True |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | lightcurve | 57 | False | `0b9b2f7d9e181172` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460602.88596 | recovered | 83 | 1753 ± 54 | 2760 | 0.05 |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | — | epoch not in this light curve | — | — | 2760 | — |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | — | epoch not in this light curve | — | — | 2760 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.10053 | -0.00412 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.16303 | -0.00395 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.43526 | -0.00354 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.15678 | -0.00325 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.17762 | -0.00317 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.09289 | -0.00300 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458779.11218 | -0.00289 | 45 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.74418 | -0.00281 | 45 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.41928 | -0.00279 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.88446 | -0.00275 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459863.17424 | -0.00267 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460609.26497 | -0.00264 | 37 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.34144 | -0.00257 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458779.14135 | -0.00252 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.36644 | -0.00251 | 33 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459869.54783 | -0.00247 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459856.79853 | -0.00244 | 46 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.28109 | -0.00242 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.25470 | -0.00233 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460609.23650 | -0.00233 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.48219 | -0.00230 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460609.29413 | -0.00229 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.91293 | -0.00226 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.70599 | -0.00225 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459875.92969 | -0.00224 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.16798 | -0.00216 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.88357 | -0.00215 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.24020 | -0.00196 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459866.99576 | -0.00188 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458779.06843 | -0.00187 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.18465 | -0.00179 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.77960 | -0.00178 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.11520 | -0.00159 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.16243 | -0.00154 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459856.84020 | -0.00150 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.17493 | -0.00147 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459875.97067 | -0.00128 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459866.70965 | -0.00126 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.87345 | -0.00394 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458783.10585 | -0.00388 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.88380 | -0.00368 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.55678 | -0.00348 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.65031 | -0.00338 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458781.81421 | -0.00337 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458781.86421 | -0.00329 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458781.88644 | -0.00324 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.95462 | -0.00322 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.58039 | -0.00321 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.36851 | -0.00320 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.53456 | -0.00315 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.45331 | -0.00305 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.52970 | -0.00304 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.31990 | -0.00302 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.12956 | -0.00295 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.98109 | -0.00294 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.67947 | -0.00294 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.40323 | -0.00291 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.02477 | -0.00290 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.12198 | -0.00288 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.91095 | -0.00283 | 5 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.31303 | -0.00280 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.96234 | -0.00278 | 3 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.98942 | -0.00276 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.98032 | -0.00274 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.62206 | -0.00274 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.10039 | -0.00273 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.01998 | -0.00271 | 4 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.82755 | -0.00268 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.56164 | -0.00267 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.44914 | -0.00265 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.51651 | -0.00265 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.97553 | -0.00265 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.84769 | -0.00262 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.92662 | -0.00260 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.78387 | -0.00260 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.62963 | -0.00259 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.85539 | -0.00258 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.89081 | -0.00258 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.46991 | -0.00256 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.97199 | -0.00256 | 3 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.39212 | -0.00255 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.46720 | -0.00251 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.19914 | -0.00250 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.74915 | -0.00249 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.58595 | -0.00248 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.60609 | -0.00248 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.54637 | -0.00248 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.76442 | -0.00247 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.54267 | -0.00247 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.45324 | -0.00246 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.55309 | -0.00243 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.81413 | -0.00243 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.23039 | -0.00242 | 7 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.18233 | -0.00241 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.73364 | -0.00239 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.37553 | -0.00239 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.73873 | -0.00237 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.71303 | -0.00236 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.99428 | -0.00236 | 3 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.60046 | -0.00235 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.95053 | -0.00232 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.98357 | -0.00230 | 2 | SAP | 2 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.34220 | -0.00229 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.05886 | -0.00229 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.55053 | -0.00229 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.37261 | -0.00229 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.41164 | -0.00229 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458767.98935 | -0.00228 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.54845 | -0.00228 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.05463 | -0.00227 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.38039 | -0.00227 | 3 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460603.74075 | -0.00226 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.01581 | -0.00225 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.61574 | -0.00224 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.87824 | -0.00223 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.04483 | -0.00222 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.66211 | -0.00222 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.05261 | -0.00221 | 3 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.76419 | -0.00220 | 4 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.55391 | -0.00218 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.93317 | -0.00218 | 7 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.69498 | -0.00217 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458771.26294 | -0.00214 | 2 | SAP | 1 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.48365 | -0.00214 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.83079 | -0.00214 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.46559 | -0.00213 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.64352 | -0.00213 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458784.12389 | -0.00212 | 2 | SAP | 1 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.53169 | -0.00212 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.04636 | -0.00211 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.36427 | -0.00210 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.47970 | -0.00209 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.21157 | -0.00207 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.86852 | -0.00207 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.94907 | -0.00207 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458780.02953 | -0.00206 | 2 | SAP | 1 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.94490 | -0.00206 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.56571 | -0.00205 | 6 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.07553 | -0.00205 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.47400 | -0.00203 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.61512 | -0.00202 | 3 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.21567 | -0.00202 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458779.46842 | -0.00202 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.48664 | -0.00202 | 4 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.85043 | -0.00200 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.47276 | -0.00199 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.46234 | -0.00198 | 3 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460588.72761 | -0.00197 | 3 | SAP | 1, 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.40809 | -0.00197 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.18595 | -0.00197 | 3 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.11983 | -0.00196 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.68781 | -0.00196 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.02407 | -0.00194 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.26164 | -0.00194 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.08109 | -0.00194 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.87821 | -0.00191 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.19220 | -0.00190 | 4 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.34775 | -0.00190 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.67137 | -0.00189 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.11713 | -0.00188 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.01019 | -0.00188 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.46142 | -0.00188 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.44151 | -0.00188 | 3 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458767.97685 | -0.00186 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.84907 | -0.00184 | 2 | SAP | 1, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.61142 | -0.00183 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458786.02523 | -0.00183 | 2 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.03525 | -0.00183 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.14907 | -0.00182 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.61983 | -0.00182 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.32477 | -0.00179 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458782.36420 | -0.00178 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.66643 | -0.00177 | 3 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.98654 | -0.00176 | 25 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.03102 | -0.00176 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458781.91213 | -0.00175 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458765.50741 | -0.00174 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460589.83942 | -0.00173 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.06852 | -0.00173 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458770.20253 | -0.00172 | 3 | SAP | 1 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458769.01157 | -0.00171 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458768.33240 | -0.00170 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460590.54012 | -0.00169 | 3 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.29483 | -0.00169 | 2 | SAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458778.12539 | -0.00162 | 2 | SAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458766.20463 | -0.00162 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.05965 | -0.00147 | 2 | PDCSAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459866.74854 | -0.00145 | 2 | PDCSAP | 2 | no |
| `tess2024274222008-s0084-0000000176860064-0281-s_lc.fits` | 2460609.30455 | -0.00144 | 2 | PDCSAP | 1 | no |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459866.84993 | -0.00140 | 2 | PDCSAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.86432 | -0.00139 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.94627 | -0.00133 | 8 | PDCSAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000176860064-0245-s_lc.fits` | 2459867.20548 | -0.00131 | 2 | PDCSAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458779.15385 | -0.00131 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458779.06426 | -0.00124 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.93654 | -0.00122 | 2 | PDCSAP | 1, 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.84557 | -0.00120 | 3 | PDCSAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.92265 | -0.00120 | 2 | PDCSAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.52247 | -0.00120 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458785.44261 | -0.00114 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.84071 | -0.00111 | 2 | PDCSAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.82404 | -0.00105 | 2 | PDCSAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.90252 | -0.00104 | 3 | PDCSAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458772.78516 | -0.00103 | 2 | PDCSAP | 2 | no |
| `tess2019279210107-s0017-0000000176860064-0161-s_lc.fits` | 2458787.06132 | -0.00088 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460590.09289 | 1255 | 1753 | 12.7951 | 0 / 12 |  |
| 2460590.10053 | 1742 | 1753 | 12.7875 | 0 / 12 |  |
| 2460590.15678 | 1825 | 1753 | 12.7312 | 0 / 12 |  |
| 2460590.16303 | 1729 | 1753 | 12.7250 | 0 / 12 |  |
| 2460590.17762 | 1337 | 1753 | 12.7104 | 0 / 12 |  |
| 2460609.23650 | 1498 | 1753 | 6.3485 | 0 / 6 |  |
| 2460609.26497 | 1791 | 1753 | 6.3770 | 1 / 6 | 6.377 |
| 2460609.29413 | 1650 | 1753 | 6.4062 | 0 / 6 |  |
| 2458766.34144 | 1940 | 1753 | 1836.5465 | 40 / 1836 | 1836.55, 918.273, 612.182, 459.137, 306.091, 262.364, 229.568, 204.061, 166.959, 153.046, 141.273, 131.182, 114.784, 108.032, 102.03, 96.6603, 87.4546, 83.4794, 79.8498, 76.5228 |
| 2458766.36644 | 1929 | 1753 | 1836.5215 | 41 / 1836 | 1836.52, 918.261, 612.174, 459.13, 306.087, 262.36, 229.565, 204.058, 166.957, 153.043, 141.271, 131.18, 114.783, 108.031, 102.029, 96.659, 87.4534, 83.4783, 79.8488, 76.5217 |
| 2458772.70599 | 2048 | 1753 | 1830.1820 | 40 / 1830 | 1830.18, 915.091, 610.061, 457.546, 305.03, 261.455, 228.773, 203.354, 166.38, 152.515, 140.783, 130.727, 114.386, 107.658, 101.677, 96.3254, 87.1515, 79.5731, 76.2576, 70.3916 |
| 2458772.74418 | 2294 | 1753 | 1830.1438 | 40 / 1830 | 1830.14, 915.072, 610.048, 457.536, 305.024, 261.449, 228.768, 203.349, 166.377, 152.512, 140.78, 130.725, 114.384, 107.656, 101.675, 96.3234, 87.1497, 79.5715, 76.256, 70.3901 |
| 2458772.77960 | 1272 | 1753 | 1830.1084 | 39 / 1830 | 1830.11, 915.054, 610.036, 457.527, 305.018, 261.444, 228.763, 203.345, 166.374, 152.509, 140.778, 130.722, 114.382, 107.653, 101.673, 96.3215, 87.148, 79.5699, 76.2545, 70.3888 |
| 2458772.91293 | 1003 | 1753 | 1829.9750 | 40 / 1829 | 1829.97, 914.987, 609.992, 457.494, 304.996, 261.425, 228.747, 203.331, 166.361, 152.498, 140.767, 130.713, 114.373, 107.646, 101.665, 96.3145, 87.1417, 79.5641, 76.249, 70.3837 |
| 2458779.06843 | 1131 | 1753 | 1823.8196 | 47 / 1823 | 1823.82, 911.91, 607.94, 455.955, 303.97, 260.546, 227.977, 202.647, 165.802, 151.985, 140.294, 130.273, 113.989, 107.284, 101.323, 95.9905, 86.8486, 82.9009, 79.2965, 75.9925 |
| 2458779.11218 | 2082 | 1753 | 1823.7758 | 46 / 1823 | 1823.78, 911.888, 607.925, 455.944, 303.963, 260.539, 227.972, 202.642, 165.798, 151.981, 140.29, 130.27, 113.986, 107.281, 101.321, 95.9882, 86.8465, 82.8989, 79.2946, 75.9907 |
| 2458779.14135 | 2056 | 1753 | 1823.7466 | 46 / 1823 | 1823.75, 911.873, 607.915, 455.937, 303.958, 260.535, 227.968, 202.638, 165.795, 151.979, 140.288, 130.268, 113.984, 107.279, 101.319, 95.9867, 86.8451, 82.8976, 79.2933, 75.9894 |
| 2458785.48219 | 1826 | 1753 | 1817.4058 | 59 / 1817 | 1817.41, 908.703, 605.802, 454.351, 363.481, 302.901, 259.629, 227.176, 201.934, 181.741, 165.219, 151.451, 139.8, 129.815, 121.16, 113.588, 100.967, 95.6529, 90.8703, 86.5431 |
| 2459856.79853 | 1789 | 1753 | 746.0895 | 25 / 746 | 746.09, 373.045, 248.696, 186.522, 149.218, 124.348, 106.584, 93.2612, 82.8988, 74.6089, 62.1741, 57.3915, 53.2921, 49.7393, 43.8876, 41.4494, 39.2679, 37.3045, 35.5281, 28.6957 |
| 2459856.84020 | 1091 | 1753 | 746.0478 | 18 / 746 | 746.048, 373.024, 248.683, 186.512, 149.21, 124.341, 106.578, 93.256, 74.6048, 62.1706, 53.2891, 49.7365, 43.8852, 39.2657, 37.3024, 35.5261, 26.6446, 25.7258 |
| 2459863.17424 | 2064 | 1753 | 739.7137 | 24 / 739 | 739.714, 369.857, 246.571, 184.928, 147.943, 123.286, 105.673, 92.4642, 82.1904, 73.9714, 61.6428, 52.8367, 46.2321, 43.5126, 41.0952, 38.9323, 36.9857, 25.5074, 23.1161, 21.7563 |
| 2459869.54783 | 1828 | 1753 | 733.3402 | 12 / 733 | 733.34, 244.447, 146.668, 104.763, 81.4822, 66.6673, 56.4108, 48.8893, 43.1377, 38.5969, 31.8844, 6.3769 |
| 2459875.92969 | 1738 | 1753 | 726.9583 | 31 / 726 | 726.958, 363.479, 242.319, 181.74, 145.392, 121.16, 103.851, 90.8698, 80.7731, 72.6958, 66.0871, 60.5799, 55.9199, 51.9256, 48.4639, 45.4349, 42.7623, 40.3866, 38.261, 36.3479 |
| 2459875.97067 | 1061 | 1753 | 726.9173 | 11 / 726 | 726.917, 242.306, 145.383, 103.845, 80.7686, 66.0834, 55.9167, 48.4612, 42.7598, 25.0661, 23.4489 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1457.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:36:10Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:36:12Z: TOI-1457.01 (TIC 176860064, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:36:13Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:36:13Z: HD 222326 (**)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460602.8860: recovered, depth 1753 ± 54 ppm (catalogue 2760 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 24 repeat-candidate event(s); first at BJD 2460590.0929, ΔT = 12.795 d, 0 of 12 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1457.01: Gaia DR3 1938853485592250752 at 0.02" (propagated 2016.0 → J2015.5; 0.02" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1457.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1457.01: 13 Gaia neighbour(s) within 52.5", contamination 0.29%; depth 1753 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 38 persistent event(s), 7 clean; BJD 2460590.0929 caution: manual exclude (within ±0.25 d); BJD 2460590.1005 caution: manual exclude (within ±0.25 d); BJD 2460590.1568 caution: manual exclude (within ±0.25 d); BJD 2460590.1630 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 38 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 9 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1457.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-1457.01: HD 222326 otype ** (multiple) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1457-01.yaml
python -m cygnus.multi report campaigns/toi-1457-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** No new signal.

Source: `campaigns/toi-1457-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
