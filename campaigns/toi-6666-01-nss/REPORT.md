# Gaia NSS vetting, TOI-6666.01

> Drafted by `python -m cygnus.multi report` from the runner's outputs; reviewed 2026-09-25.
> The reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-6666-01-nss.yaml`
- Parent queue: `toi-6666-01`
- Ledger runs: astrometric_vetting #635, context_products #633, fetch_products #632, source_checks #634
- Runner finished (UTC): 2026-09-25T13:28:35Z

## Bottom line

No light curve was screened in this campaign (steps run: fetch_products, context_products, source_checks, astrometric_vetting); see *Checks* for what was tested.
Gaia DR3 NSS, TOI-6666.01: **inconclusive** — no Gaia DR3 NSS two-body solution for source 2223770483452673408 (0.02" away); Gaia sensitivity is incomplete, so this is not proof of a single star.

This is a pipeline check on a known object, not a discovery claim.

## Reviewer notes (2026-09-25)

**Astrometry of the matched host is clean.** From `gaia_cone_TOI-6666.01_r30as.csv` and
`source_checks.json` on disk: the matched source 2223770483452673408 has RUWE 0.827 (single-star
model fits), no `non_single_star` flag, and it is the only Gaia DR3 source within 5″ — the
identification is unique. (The 0.02″ to Gaia is itself 0.5 yr of proper motion, since the
TOI-table position is at epoch J2015.5, `reports/position-epoch-audit-01`; the single SIMBAD row,
`HD 206617`, is 0.57″ from the TOI position for the same reason: SIMBAD is at epoch 2000, and
Gaia DR3 minus SIMBAD equals 16 yr × PM to within 1 mas.) No NSS two-body solution is published for it, which is *inconclusive*:
Gaia's NSS catalogue is not complete at these orbital parameters, so absence is not evidence for
or against the eclipsing-binary / companion alternative for the TOI-6666.01 repeat-event lead.

**Earlier ad-hoc SB2 attribution withdrawn** (check row marked `failed` — the test ran and
refuted the attribution). An earlier ad-hoc check in this worktree attributed an SB2 NSS solution
(P = 4.8124683 d, e = 0.053, K1 = 85.77 km/s, significance 1199.6, f(M) = 0.31 M☉) to this
target. That solution belongs to Gaia source `4513527912472807936` at ICRS 287.16737, +16.85086 —
57.276° from TOI-6666.01 (re-verified arithmetically from the two ICRS positions on 2026-09-25)
— and is not related to this campaign; the full query audit is in the sandbox record this
campaign was promoted from. Nothing in this campaign depends on it.

What this supports: the astrometric-companion channel neither supports nor excludes the
companion alternative for the repeat-event lead. What it does not: any statement about the
sector-18 event itself (no photometry was used here). Next test, unchanged from the vetting log:
independent epochs; radial velocities would constrain any companion directly.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6666.01 | NASA Exoplanet Archive TOI table (via campaigns/toi-6666-01.yaml) (copied in the spec) |
| tic | 256429408 | NASA Exoplanet Archive TOI table (via campaigns/toi-6666-01.yaml) (copied in the spec) |
| ra_deg | 325.003248 | NASA Exoplanet Archive TOI table (via campaigns/toi-6666-01.yaml) (copied in the spec) |
| dec_deg | 69.086612 | NASA Exoplanet Archive TOI table (via campaigns/toi-6666-01.yaml) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `gaia_cone_TOI-6666.01_r30as.csv` | table | — | — | `a0006c4ca461fbfe` | True |
| `simbad_TOI-6666.01.csv` | table | — | — | `b442c5a8d6fa2804` | True |

## Gaia DR3 astrometric vetting

| Target | Gaia DR3 source | Sep (") | G | Parallax (mas) | Sources in radius | Identification | NSS solutions | State |
|---|---|---|---|---|---|---|---|---|
| TOI-6666.01 | 2223770483452673408 | 0.019 | 8.779 | 7.866 | 1 | unique | 0 | inconclusive |

An NSS solution at or above the significance threshold means the companion is already known to Gaia; no solution is *inconclusive* (Gaia's NSS sensitivity is incomplete), never a pass. Full rows: `nss.json`.

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from gaia, simbad checksummed at first retrieval |
| Target-to-Gaia source identification | passed | TOI-6666.01: Gaia DR3 2223770483452673408 at 0.02", G 8.779094; 1 source(s) within 5" |
| Gaia NSS astrometric vetting | inconclusive | TOI-6666.01: no Gaia DR3 NSS two-body solution for source 2223770483452673408 (0.02" away); Gaia sensitivity is incomplete, so this is not proof of a single star |
| Proper-motion propagation to the Gaia epoch | passed | the runner matches positions as given; `reports/position-epoch-audit-01` (Gaia DR3 TAP, 2026-09-25) shows the TOI-table position is at epoch J2015.5, not J2000.0: TOI − Gaia DR3 = (+0.8, −19.1) mas = −0.5 yr × PM (+0.8, −18.5) mas; residual after propagation 0.6 mas. The 0.5-yr offset (0.019″) is far below the 5″ match radius |
| Radial-velocity / literature companion search (ADS) | not_tested |  |
| Earlier ad-hoc SB2 attribution | failed | cited source 4513527912472807936 (ICRS 287.16737, +16.85086) is 57.276 deg from the target; attribution withdrawn |
| Context products read | passed | 2 non-light-curve product(s) (table) recorded in context.json |
| Source checks (gaia) | passed | 5/5 passed |
| Source checks (simbad) | passed | 2/2 passed |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6666-01-nss.yaml
python -m cygnus.multi report campaigns/toi-6666-01-nss.yaml
```
