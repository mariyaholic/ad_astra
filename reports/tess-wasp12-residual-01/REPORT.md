# Cygnus bounded discovery campaign: TESS residuals around WASP-12

**Run date:** 2026-09-24 UTC  
**Bottom line:** **Bounded null. No candidate and no dossier.**  
**Evidence level:** No unverified lead retained. The expected WASP-12 b transit signature is known and excluded from any novelty interpretation.

## Ranked search outcomes

| Rank | Target / products | Result and statistic | Evidence | Main concern / next test |
|---:|---|---|---|---|
| 1 | TIC 86396382 = WASP-12; MAST TESS SPOC S20 `tess2019357164649-s0020-0000000086396382-0165-s_lc.fits`; S43 `tess2021258175143-s0043-0000000086396382-0214-s_lc.fits` | Screened 16,551 and 15,577 usable cadences, respectively. With 1/2/3-day running medians on SAP and PDCSAP, there were 0 ≥5 robust-MAD, ≥2-cadence negative excursion entries outside the broad ±0.08-cycle known-transit phase window. The in-window screening entries (835 across S20 recipes/reductions; 464 across S43) are overlapping snippets, not unique events, and fall within the catalog-ephemeris transit-phase veto; they were not retained as new events. | Bounded null; no candidate | Threshold is uncalibrated; no pixel-level, centroid-correlation, injection/recovery, ADS/ExoFOP, or independent-instrument vetting. Next: only pursue any specific out-of-window feature if reanalysis identifies one; otherwise a broader campaign must prespecify targets and controls rather than extrapolating this one-target null. |

Coordinates are copied from TESS headers: RA 97.6366528°, Dec +29.6722962°; coordinate frame/epoch not independently checked. This table is the complete ranked outcome for this finite campaign, not a survey-wide ranking.

## Hypothesis and falsification

**Hypothesis:** at least one isolated negative excursion in either of two specified 120-s TESS SPOC light curves is both ≥5 robust-MAD below a centered local median, spans ≥2 consecutive cadences, and falls outside ±0.08 orbital phase of the known WASP-12 b transit. Persistence under both SAP and PDCSAP and all three baseline windows would motivate a lead, not establish one.

**Observed:** no detected screen entry outside the broad phase veto in any product/reduction/window combination. This falsifies this narrowly defined screen outcome for the two files; it does not rule out smaller, shorter, in-transit, other-band, other-sector, or non-photometric phenomena.

NASA Exoplanet Archive `pscomppars` query on 2026-09-24 returned WASP-12 b, period 1.09141890100 d, transit midpoint 2457607.51930500, duration 3.001 h, and discovery reference Hebb et al. 2009. The phase window is intentionally broad and provisional: updated timing/period evolution was not fit. Archive query URL and literal ADQL are in `SEARCH_LOG.md`.

## Provenance, footprint, and selection

The two public MAST TESS SPOC files were transferred one-at-a-time from the existing `cygnus:Cygnus/data/tier1/01_mast/` Drive tree to nonsynced scratch. TESS pipeline headers give S20 `PROCVER=spoc-5.0.96-20230729`/`DATA_REL=73` and S43 `PROCVER=spoc-5.0.45-20211006`/`DATA_REL=62`. Both byte sizes and SHA-256 hashes exactly match `docs/tier1_pack/MASTER_MANIFEST.csv` after retrieval. No original was changed. The underlying archive URL, stored product IDs, and manifest provenance are documented in the search log. S20 spans header dates 2019-12-25–2020-01-20; S43 spans 2021-09-16–2021-10-11. FITS table time is TDB with BJD reference 2457000; code preserves stored TIME and separately records BJD-like values.

Finite footprint: one target, one sector-20 light curve and one temporally independent sector-43 light curve, single optical TESS passband, 120-s cadence. The latter is a second epoch from the same mission/instrument/pipeline, not independent instrumentation. All 18,954 and 17,804 rows were screened; 2,403 and 2,227 rows respectively were excluded by combined quality/nonfinite/nonzero-flux rules (per-reason counts not generated). All exclusions and limitations are in `SEARCH_LOG.md`.

## Analysis and caveats

The checksum-gated script uses only local FITS products, Astropy FITS I/O, NumPy and SciPy. It compares SAP and PDCSAP and centered running-median windows of 1, 2, and 3 days. It requires `QUALITY == 0`, finite TIME/flux, and nonzero flux. A robust scale is estimated as 1.4826×MAD of fractional residuals. Because cadence noise is time-correlated and the search scans thousands of samples and multiple recipes, the -5 scale threshold is **not a p-value, sigma-calibrated detection, or false-alarm probability**. Repeated transit-phase snippets and non-independent recipes are not counted as independent evidence.

Off-transit phase controls supply same-product descriptive robust scatter only (SAP/PDCSAP: S20 0.002145/0.001957; S43 0.001935/0.001911 fractional). No synthetic signal injection was run. Centroid measurements exist in the light curves but were not correlated with event residuals. There was no pixel-level background/blend inspection, cosmic-ray/hot-pixel audit, or independent reduction. These checks remain **not tested**, not passed.

## Catalog/literature status

The NASA Exoplanet Archive live `pscomppars` snapshot queried 2026-09-24 establishes the already-known WASP-12 b context; no separately versioned release identifier was exposed by that query. Generic web searches for current literature were attempted but the configured search service returned HTTP 402 (insufficient balance); ADS, ExoFOP, additional variable-star catalogs, and publication searches were not completed. Accordingly no claim about absence of prior reports is made. There is no candidate for a novelty claim.

## Reproduction and artifacts

- Configuration: [`campaigns/tess-wasp12-residual-01.yaml`](../../campaigns/tess-wasp12-residual-01.yaml)
- Code: [`tools/analyze_tess_residual.py`](../../tools/analyze_tess_residual.py)
- Full search log and exact queries/checksums: [`SEARCH_LOG.md`](SEARCH_LOG.md)
- Machine-readable output: `sector20/screen.json`, `sector20/normalized_series.csv`, `sector43/screen.json`, `sector43/normalized_series.csv` (derived outputs; not source data)
- Environment: Python 3.13.3, NumPy 2.5.3, SciPy 1.18.1, Astropy 8.0.1.
- Reproduction commands, manifest gates, package/test context: see `SEARCH_LOG.md`.

The general Cygnus analysis suite is a triage utility collection validated on synthetic inputs; this run used a purpose-written, checksum-pinned screen rather than treating an uncalibrated utility score as a detection. The prior-art gate is incomplete. No data or report was sent externally.
