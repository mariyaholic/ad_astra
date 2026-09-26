# Gaia NSS vetting, TOI-2666.01

> Drafted by `python -m cygnus.multi report` from the runner's outputs; reviewed 2026-09-25.
> The reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-2666-01-nss.yaml`
- Parent queue: `toi-2666-01`
- Ledger runs: astrometric_vetting #639, context_products #637, fetch_products #636, source_checks #638
- Runner finished (UTC): 2026-09-25T13:28:58Z

## Bottom line

No light curve was screened in this campaign (steps run: fetch_products, context_products, source_checks, astrometric_vetting); see *Checks* for what was tested.
Gaia DR3 NSS, TOI-2666.01: **inconclusive** — no Gaia DR3 NSS two-body solution for source 3837451574150437120 (0.03" away); Gaia sensitivity is incomplete, so this is not proof of a single star.

This is a pipeline check on a known object, not a discovery claim.

## Reviewer notes (2026-09-25)

**Identification.** From `gaia_cone_TOI-2666.01_r30as.csv` on disk: the matched source
3837451574150437120 (G 7.544, parallax 30.980 mas ≈ 32 pc, proper motion 23.3, −63.9 mas/yr) is
0.034″ from the TOI-table position and 6.16 mag brighter in G than the only other source in the 5″
radius, so the identification is unique. That 0.034″ is itself proper motion: the TOI-table
position is at epoch J2015.5 (Gaia DR2), and 0.5 yr × PM = 0.034″
(`reports/position-epoch-audit-01`). The other source, Gaia DR3 3837451578445470464 (G 13.704,
1.33″ from the host, two-parameter solution: no parallax or proper motion), is a fainter
neighbour (no parallax); its distance is not measured, so "background" is not established.
SIMBAD lists the host as `HD 80133` (otype `PM*`, high proper-motion star) with the TOI-2666.01
candidate record at the same coordinates; that row sits 1.05″ from the TOI-table coordinates
entirely because of proper motion, not a mismatch: SIMBAD's coordinates are at epoch 2000, and
Gaia DR3 (2016.0) minus SIMBAD is (+0.372″, −1.022″) in (RA·cos δ, Dec), equal to 16 yr × PM to
within 1 mas (the SIMBAD-to-TOI offset is 15.5 yr × PM).

**Neighbour inside the TESS aperture (not excluded as the event source).** The neighbour lies
well inside one TESS pixel (21″) of the host, so TESS photometry does not separate them. With
ΔG = 6.16 mag, a neighbour eclipsed completely would dilute to at most 10^(−0.4 × 6.16) ≈ 0.34 %
in G. The TOI-2666.01 events are deeper: catalogue depth 22040 ppm, and 12466 ± 43 ppm
(catalogued transit, BJD 2459259.1414) and 14437 ppm (sector-99 repeat, BJD 2461049.1644)
measured by the screen (`campaigns/toi-2666-01/REPORT.md`; centre depth −18.9 ppt), i.e. ≥ 3.6×
the G-band cap. The neighbour's TESS-band contrast is not measured (no BP−RP), and a red
neighbour would be relatively brighter in the TESS band, so the neighbour is disfavoured, not
excluded, as the source of the events.

**RUWE > 1.4 (check state `inconclusive`, not a pass).** The matched host has Gaia DR3 RUWE
1.464 (from the cone product), so the single-star astrometric model does not fit well. In the
framework here this is recorded as inconclusive; it is weak astrometric evidence *consistent
with* an unseen companion (the eclipsing-binary alternative for the sector-99 repeat-event lead),
but RUWE alone is not an NSS detection and has instrumental causes (e.g. excess single-source
noise), so it is not claimed as support.

**No NSS solution.** Gaia DR3 publishes no two-body solution for this source
(`nss.json`: 0 rows queried at significance ≥ 5): inconclusive, never a pass — Gaia's NSS
sensitivity is incomplete at these orbital parameters. `non_single_star` = 0 for both cone
sources.

What this supports: the astrometric-companion channel neither supports nor excludes the
companion alternative for the TOI-2666.01 repeat-event lead (`campaigns/tess-mono-01/LEAD_VETTING_LOG.md`).
What it does not: anything about the sector-99 events themselves (no photometry used here). Next
test, unchanged from the vetting log: ExoFOP/SPOC DV check and difference-image centroids for the
repeat events; radial velocities would constrain any companion directly.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2666.01 | NASA Exoplanet Archive TOI table (via campaigns/toi-2666-01.yaml) (copied in the spec) |
| tic | 170889511 | NASA Exoplanet Archive TOI table (via campaigns/toi-2666-01.yaml) (copied in the spec) |
| ra_deg | 139.480865 | NASA Exoplanet Archive TOI table (via campaigns/toi-2666-01.yaml) (copied in the spec) |
| dec_deg | -3.387525 | NASA Exoplanet Archive TOI table (via campaigns/toi-2666-01.yaml) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `gaia_cone_TOI-2666.01_r30as.csv` | table | — | — | `e74fc63f7b4154d5` | True |
| `simbad_TOI-2666.01.csv` | table | — | — | `19935a08665e0d7d` | True |

## Gaia DR3 astrometric vetting

| Target | Gaia DR3 source | Sep (") | G | Parallax (mas) | Sources in radius | Identification | NSS solutions | State |
|---|---|---|---|---|---|---|---|---|
| TOI-2666.01 | 3837451574150437120 | 0.034 | 7.544 | 30.980 | 2 | unique | 0 | inconclusive |

An NSS solution at or above the significance threshold means the companion is already known to Gaia; no solution is *inconclusive* (Gaia's NSS sensitivity is incomplete), never a pass. Full rows: `nss.json`.

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from gaia, simbad checksummed at first retrieval |
| Target-to-Gaia source identification | passed | TOI-2666.01: Gaia DR3 3837451574150437120 at 0.03", G 7.5441976; 2 source(s) within 5", nearest other ΔG 6.16 |
| Gaia NSS astrometric vetting | inconclusive | TOI-2666.01: no Gaia DR3 NSS two-body solution for source 3837451574150437120 (0.03" away); Gaia sensitivity is incomplete, so this is not proof of a single star |
| Proper-motion propagation to the Gaia epoch | passed | the runner matches positions as given; `reports/position-epoch-audit-01` (Gaia DR3 TAP, 2026-09-25) shows the TOI-table position is at epoch J2015.5, not J2000.0: TOI − Gaia DR3 = (−11.2, +31.7) mas = −0.5 yr × PM (−11.6, +31.9) mas; residual after propagation 0.5 mas. The 0.5-yr offset (0.034″) is far below the 5″ match radius |
| Radial-velocity / literature companion search (ADS) | not_tested |  |
| Context products read | passed | 2 non-light-curve product(s) (table) recorded in context.json |
| Source checks (gaia) | inconclusive | 4/5 passed; non-passing: gaia_cone_TOI-2666.01_r30as.csv:Gaia RUWE |
| Source checks (simbad) | passed | 2/2 passed |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2666-01-nss.yaml
python -m cygnus.multi report campaigns/toi-2666-01-nss.yaml
```
