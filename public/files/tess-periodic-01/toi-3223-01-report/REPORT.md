<!-- [private Drive store] -->
# Known-object test, TOI-3223.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3223-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #462, calibrate_screen #390, event_census #403, fetch_products #389, known_signal_recovery #392, moving_objects #405, period_aliases #404, prior_art #464, residual_screen #398, stellar_context #393, variability_guard #463
- Runner finished (UTC): 2026-09-26T10:08:44Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 851 threshold entries forming **189 distinct event(s)**, **110 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3223.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 297668572 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 180.606425 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -66.529163 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459358.775725 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 48110.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.755 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.2272 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | lightcurve | 64 | False | `71c46bb7de6cff28` | True |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | lightcurve | 65 | False | `e19937143fa4919a` | True |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | lightcurve | 99 | False | `e07220c12fe118cd` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 48110 | — |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | — | epoch not in this light curve | — | — | 48110 | — |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 48110 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.36966 | -0.09495 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.62097 | -0.09276 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.59588 | -0.08971 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.68417 | -0.08838 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461054.72570 | -0.08659 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461054.68681 | -0.08659 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.38355 | -0.08495 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.09908 | -0.08491 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.65986 | -0.08353 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.59996 | -0.08270 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.44188 | -0.08236 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.20772 | -0.08219 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.37799 | -0.08176 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.39258 | -0.08173 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460077.00019 | -0.08131 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.17782 | -0.08092 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.41128 | -0.07875 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.59573 | -0.07725 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.56403 | -0.07722 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.27230 | -0.07720 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460077.06130 | -0.07680 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.62158 | -0.07651 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460076.93908 | -0.07648 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460076.96824 | -0.07638 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.12659 | -0.07556 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.70084 | -0.07533 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.84942 | -0.07519 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.29049 | -0.07482 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.24453 | -0.07477 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.53537 | -0.07425 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.05298 | -0.07418 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.25425 | -0.07401 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.69181 | -0.07394 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.67653 | -0.07360 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.14118 | -0.07313 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.57357 | -0.07304 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.75428 | -0.07279 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.55434 | -0.07272 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.15838 | -0.07239 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.48490 | -0.07178 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.54857 | -0.07121 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460076.99046 | -0.07112 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.44740 | -0.07110 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.19241 | -0.07026 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.18685 | -0.06983 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.25769 | -0.06967 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.41545 | -0.06896 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.54162 | -0.06891 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.49809 | -0.06862 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.50920 | -0.06849 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.83901 | -0.06785 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.12104 | -0.06779 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.81748 | -0.06776 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.07659 | -0.06725 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.16741 | -0.06712 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.22435 | -0.06692 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.20074 | -0.06586 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.58329 | -0.06583 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.23199 | -0.06582 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.03493 | -0.06552 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.02034 | -0.06461 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.53420 | -0.06459 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.76609 | -0.06372 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.24032 | -0.06348 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.77234 | -0.06239 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.13423 | -0.06215 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.21741 | -0.06187 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.00576 | -0.06180 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.90290 | -0.06173 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.09326 | -0.06160 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.40156 | -0.06157 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.52635 | -0.06091 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.85984 | -0.06087 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.88762 | -0.06083 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.14604 | -0.06067 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.50968 | -0.06063 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.88345 | -0.06053 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.51732 | -0.06040 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.62288 | -0.06038 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.80151 | -0.06031 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.04326 | -0.06030 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.72313 | -0.06028 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.54184 | -0.06019 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.16618 | -0.05984 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.06201 | -0.05966 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.64649 | -0.05929 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.56823 | -0.05921 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.24935 | -0.05913 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.49162 | -0.05912 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.40712 | -0.05896 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.48051 | -0.05862 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.55017 | -0.05838 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.86817 | -0.05829 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.11532 | -0.05790 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.39601 | -0.05749 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.56176 | -0.05746 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.77928 | -0.05711 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.27366 | -0.05704 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.42587 | -0.05680 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.17520 | -0.05677 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.46962 | -0.05669 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.46198 | -0.05668 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.59301 | -0.05484 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.79317 | -0.05482 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.67383 | -0.05434 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.90706 | -0.05408 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.69397 | -0.05306 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.71063 | -0.05093 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.63676 | -0.05022 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.60621 | -0.04935 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.12061 | -0.08452 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.07547 | -0.08330 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.11019 | -0.08277 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461054.73195 | -0.08191 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.05047 | -0.08149 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.08936 | -0.08137 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461054.73890 | -0.08112 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.14353 | -0.08101 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.10325 | -0.07963 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.38772 | -0.07901 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.58199 | -0.07848 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.03172 | -0.07823 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.58755 | -0.07812 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461063.94424 | -0.07799 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.06713 | -0.07749 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.63477 | -0.07718 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461054.66181 | -0.07645 | 2 | PDCSAP | 2 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.61394 | -0.07635 | 2 | PDCSAP | 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.57505 | -0.07628 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.55213 | -0.07625 | 3 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.64727 | -0.07614 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.67236 | -0.07581 | 2 | PDCSAP+SAP | 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461068.60630 | -0.07570 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461063.98591 | -0.07568 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461050.15047 | -0.07540 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.41549 | -0.07433 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.33341 | -0.07414 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.52351 | -0.07413 | 2 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.43077 | -0.07348 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461054.63125 | -0.07331 | 2 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.23758 | -0.07326 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461063.91993 | -0.07269 | 3 | PDCSAP | 1, 2 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461063.91368 | -0.07268 | 2 | PDCSAP | 1, 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.21953 | -0.07247 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.29105 | -0.07228 | 3 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.37383 | -0.07115 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.56378 | -0.07036 | 2 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.58209 | -0.07021 | 2 | PDCSAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461064.02619 | -0.07004 | 2 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.20286 | -0.06983 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460072.30160 | -0.06928 | 2 | PDCSAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460076.95227 | -0.06888 | 3 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460086.32369 | -0.06832 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460077.02727 | -0.06820 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460076.97380 | -0.06641 | 2 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.51934 | -0.06403 | 2 | PDCSAP | 2 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.04743 | -0.06225 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.71827 | -0.06155 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.19465 | -0.06071 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.77105 | -0.05869 | 2 | PDCSAP | 1, 2 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.65994 | -0.05810 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.52587 | -0.05741 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.51823 | -0.05732 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.37795 | -0.05718 | 2 | PDCSAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.28407 | -0.05672 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460063.11062 | -0.05504 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460044.61246 | -0.05302 | 2 | PDCSAP | 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460058.38837 | -0.05109 | 3 | PDCSAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.79188 | -0.05085 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460049.13893 | -0.05003 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460062.99326 | -0.04905 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461073.20584 | -0.02886 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461063.07614 | -0.02201 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 2461073.16417 | -0.01990 | 2 | SAP | 1 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.56101 | -0.01836 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.49365 | -0.01696 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460095.50128 | -0.01680 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 2460081.61125 | -0.01526 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.67791 | -0.01523 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.60638 | -0.01504 | 3 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460061.52797 | -0.01441 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.74744 | -0.01421 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.71541 | -0.01416 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.86124 | -0.01330 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.74458 | -0.01326 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460067.73772 | -0.01262 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460053.78414 | -0.01168 | 3 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.81194 | -0.01167 | 3 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 2460054.42929 | -0.01151 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3223.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:08:41Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:08:42Z: TOI-3223.01 (TIC 297668572, disposition PC)
- VSX (done, 2026-09-26): 2 match(es) in VSX within 30" as of 2026-09-26T10:08:43Z: Gaia DR3 5860668319251706368 (type DSCT|GDOR|SXPHE, P — d); Gaia DR3 5860668383620853376 (type RS, P — d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:08:44Z: TOI-3223 (*); TOI-3223.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 30%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3223.01: Gaia DR3 5860668319251708928 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3223.01: dwarf priors not applied — 1.51 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3223.01: 292 Gaia neighbour(s) within 52.5", contamination 84.86%; depth 48110 ppm (catalogue depth); 4 could produce it if fully eclipsed (brightest 5860668319251706368, 20.3", ΔG -0.34); a centroid test is needed |
| Pointing and quality census per event | failed | 110 persistent event(s), 11 clean; BJD 2460044.4805 suspect: MOM_CENTR1 z=-8.2; BJD 2460044.4916 suspect: MOM_CENTR1 z=-8.3; BJD 2460044.5097 suspect: MOM_CENTR1 z=-9.4; BJD 2460044.5173 suspect: MOM_CENTR1 z=-10.0 |
| Moving objects at screen-event epochs | inconclusive | 110 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 7 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3223.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3223.01: TOI-3223 otype * (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3223-01.yaml
python -m cygnus.multi report campaigns/toi-3223-01.yaml
```
