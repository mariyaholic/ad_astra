# Search log: position-epoch-audit-01

| Item | Value |
|---|---|
| Question | At which epoch are the TOI-table target positions in `campaigns/*.yaml` valid? |
| Input | All 81 `campaigns/*.yaml` (state 2026-09-25). 78 targets with `ra_deg`/`dec_deg` form 76 unique positions. |
| Service | ESA Gaia TAP, `https://gea.esac.esa.int/tap-server/tap`, sync, CSV, anonymous |
| Tables | `gaiadr3.gaia_source` (all positions); `gaiadr2.gaia_source`, `gaiadr1.gaia_source` (3 unresolved + 2 controls) |
| Query window (UTC) | DR3: 2026-09-25T21:18:52Z – 21:36:23Z; DR2/DR1: 2026-09-25, after 21:39Z (per-query times in `gaia_dr2_check.json`) |
| Cone radius | 10″ |
| Columns | source_id, ra, dec, pmra, pmdec, parallax, phot_g_mean_mag (DR1: no PM or parallax) |
| Thresholds | epoch fit ≤ 5 mas and ≥ 5 mas better than the other epoch; discriminating only if 16 yr × PM ≥ 10 mas; direct DR2/DR1 match ≤ 2.5 mas |
| Pacing | serial, 1.5 s between queries; retries in `TapDirect` (none needed) |

## Totals

- Screened: 78 targets / 76 unique positions. Queries: 76 DR3 + 10 DR2/DR1, all HTTP 200.
- Excluded: none. Every cone had ≥ 1 source, and the nearest match was also the brightest in 78/78.
- DR3 stage: 75 J2015.5, 3 inconsistent, 0 J2000.0, 0 undetermined.
- Final: 77 J2015.5, 1 J2015.0 (TOI-6663.01, Gaia DR1 position), 0 J2000.0, 0 undetermined.

## Not searched / limitations

- Specs without explicit positions (`tess-mono-01`, `tess-wasp12-residual-01`,
  `wasp12-sector20-recovery`) and `docs/tier1_pack/NAME_RESOLUTIONS.json` positions (CDS Sesame)
  were not audited.
- The queue targets in the existing `campaigns/tess-mono-01/sky_record.json` (label
  `J2000.0 (TIC)` from the old runner fallback) were not individually audited. They come from the
  same TOI-table columns, and the record is regenerated on the next run.
- pscomppars (`--planet`) and `--manual` positions were not audited. The scaffolds label them
  `unverified`.
- Propagation is linear; parallax and perspective acceleration are neglected (≪ 1 mas here).
- The NASA Exoplanet Archive's documentation of the TOI-table epoch was not consulted. The result
  is empirical, from Gaia positions.
