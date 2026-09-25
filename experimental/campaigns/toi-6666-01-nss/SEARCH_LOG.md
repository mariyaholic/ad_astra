# Search log: toi-6666-01-nss

## Service and release

| Item | Value |
|---|---|
| Service | ESA Gaia archive, TAP sync endpoint |
| Endpoint | https://gea.esac.esa.int/tap-server/tap/sync |
| Release | Gaia DR3 |
| Tables | `gaiadr3.gaia_source`, `gaiadr3.nss_two_body_orbit` |
| Query date | 2026-09-25 (UTC) |
| Authentication | anonymous |
| Products downloaded | none |

## Queries

1. Host match, radius 5" (0.0013889 deg):

```sql
SELECT TOP 20 source_id, ra, dec, phot_g_mean_mag, parallax
FROM gaiadr3.gaia_source
WHERE 1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', 325.0032480, 69.0866120, 0.0013889))
```

Result: 1 row — `2223770483452673408` at 0.019" (G 8.779, parallax 7.866 mas).

2. NSS two-body solutions for the matched source (up to 10 rows):

```sql
SELECT TOP 10 source_id, nss_solution_type, ra, dec, parallax, period, period_error,
       eccentricity, eccentricity_error, semi_amplitude_primary, semi_amplitude_primary_error,
       mass_ratio, inclination, inclination_error, significance, goodness_of_fit, flags,
       astrometric_jitter
FROM gaiadr3.nss_two_body_orbit
WHERE source_id = 2223770483452673408
```

Result: 0 rows.

3. Discrepancy audit of the withdrawn ad-hoc attribution — the same two queries
   with `source_id = 4513527912472807936`:

- `gaia_source`: ICRS 287.1673666435155, +16.850855038571932; G 6.539; parallax 13.390 mas.
- `nss_two_body_orbit`: SB2; P 4.8124682601437705 d; e 0.05299656496184946;
  K1 85.76665645084256 km/s; significance 1199.6366.
- Separation from TOI-2666.01: 57.276 deg. Not the host; attribution withdrawn.

## Selection

- `radius_arcsec = 5.0` (nearest source only)
- `significance_min = 5.0`
- `max_solutions = 10`

## Not searched / not tested

- Companions outside Gaia NSS sensitivity (period, mass ratio, contrast).
- Radial-velocity or eclipse ephemerides; difference imaging; neighbour astrometry.
- The production lead's other artifact checks (difference-image centroids,
  pointing, ADS literature) remain as stated in
  `campaigns/toi-6666-01/sky_record.json`.
