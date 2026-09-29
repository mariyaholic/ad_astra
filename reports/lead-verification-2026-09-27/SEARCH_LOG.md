# Search log — four-lead verification, 2026-09-27

This finite screen covers four named TOI targets; it is not an all-archive or full-sky search. No light-curve or TPF product was downloaded in this pass; cached vetting measurements were reclassified under the corrected rule.

## MAST SPOC timeseries metadata

Endpoint `https://mast.stsci.edu/api/v0/invoke`; services `Mast.Caom.Filtered` and `Mast.Caom.Products`; filters: `obs_collection=TESS`, `dataproduct_type=timeseries`, `target_name=<bare TIC>`, `provenance_name=SPOC`, product subgroup `LC`, excluding fast cadence files; limit 200 products per target. Retrieval began 2026-09-27T04:57:36.101355+00:00. `mast_metadata.json` stores product IDs, sectors, sizes, URLs, target TICs and any errors. This query does not cover FFI, HLSP, ground photometry or unreleased sectors.

| Target | TIC | Product ID | Sector | Bytes |
|---|---:|---|---:|---:|
| toi-224-01 | 70797900 | `tess2020238165205-s0029-0000000070797900-0193-s_lc.fits` | 29 | 1915200 |
| toi-224-01 | 70797900 | `tess2018234235059-s0002-0000000070797900-0121-s_lc.fits` | 2 | 2004480 |
| toi-224-01 | 70797900 | `tess2023237165326-s0069-0000000070797900-0264-s_lc.fits` | 69 | 1886400 |
| toi-224-01 | 70797900 | `tess2025232030459-s0096-0000000070797900-0293-s_lc.fits` | 96 | 1877760 |
| toi-224-01 | 70797900 | `tess2026192185000-s0106-0000000070797900-0308-s_lc.fits` | 106 | 2079360 |
| toi-2666-01 | 170889511 | `tess2021039152502-s0035-0000000170889511-0205-s_lc.fits` | 35 | 1828800 |
| toi-2666-01 | 170889511 | `tess2023018032328-s0061-0000000170889511-0250-s_lc.fits` | 61 | 1860480 |
| toi-2666-01 | 170889511 | `tess2026005125623-s0099-0000000170889511-0300-s_lc.fits` | 99 | 2021760 |
| toi-7610-01 | 121341000 | `tess2025014115807-s0088-0000000121341000-0285-s_lc.fits` | 88 | 2030400 |
| toi-7610-01 | 121341000 | `tess2026005125623-s0099-0000000121341000-0300-s_lc.fits` | 99 | 2021760 |
| toi-3500-02 | 443666343 | `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 37 | 1854720 |
| toi-3500-02 | 443666343 | `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 64 | 1969920 |
| toi-3500-02 | 443666343 | `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 90 | 2041920 |
| toi-3500-02 | 443666343 | `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 101 | 1912320 |

Four targets returned metadata successfully, zero archive errors. Their product counts are 5, 3, 4 and 2 for TOI-224, 2666, 3500 and 7610 respectively. No new SPOC sector beyond the existing campaign sectors was returned; absence here is not an astrophysical nondetection.

## NASA Exoplanet Archive event-time screen

Endpoint `https://exoplanetarchive.ipac.caltech.edu/TAP/sync`; `pscomppars` and `toi` 30-arcsec position queries are recorded verbatim with rows and retrieval UTC in `prior_art.json` (screen run 2026-09-27T04:58:22.736381+00:00). Event times were compared with all returned non-null periods and mid-times using nearest integer cycle and a broad ±1-d screening tolerance. No overlap was found for these four events. A missing period, publication-specific TTV or different source identity is *not* cleared.

| Target | Confirmed table rows | TOI rows | One-day linear overlap |
|---|---:|---:|---|
| toi-224-01 | 0 | 1 | 0 |
| toi-2666-01 | 0 | 1 | 0 |
| toi-7610-01 | 0 | 1 | 0 |
| toi-3500-02 | 0 | 2 | 0 |

## Exclusions and untested work

Screened 4 targets, 14 SPOC LC metadata records, no archive errors, no newly released SPOC sectors in these results. No products were downloaded and no new event was accepted or rejected by new photometry. Excluded from this pass: FFI/HLSP, later unreleased sectors, independent photometry, spectra/RV, PRF two-source fits, target-specific TESS pointing confirmation, and full literature/ADS search for the four. Local TPF measurements were inherited from the earlier campaign products and reclassified; see their vetting files.

