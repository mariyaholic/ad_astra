# CYGNUS Tier-1 Data Pack — Search Log

Generated: 2026-09-24 (UTC). Pack contents live on Drive at `cygnus:Cygnus/data/tier1/` and are hosted there only (local staging copies deleted after MD5 verification per the user retention instruction).

Aggregate: 82 data products, 1112.1 MB, 132 manifest rows (including probes/exclusions), across 8 archives. Every product carries sha256+md5 checksums, the exact endpoint, and the verbatim query used to retrieve it.

## Service summary

| Pack dir | Archive | Products (state counts) |
| --- | --- | --- |
| 01_mast | MAST (STScI) |  |
| 02_gaia | Gaia DR3 (ESA TAP+) |  |
| 03_skyview | SkyView (NASA GSFC) |  |
| 04_cds | CDS Strasbourg |  |
| 05_ned | NED (IPAC) |  |
| 06_eso | ESO Science Archive |  |
| 07_irsa | IRSA (IPAC) |  |
| 08_legacy_survey | Legacy Survey (LS DR9/DR10) |  |

## What each directory contains

- **01_mast** — MAST (STScI): TESS SPOC 2-min light curves; TESS FFI cutouts; Kepler LCs; JWST + HST samples.
- **02_gaia** — Gaia DR3 (ESA TAP+): gaia_source cones; NSS two-body orbits + acceleration; vari_rrlyrae / eclipsing binaries / summary; xp_summary.
- **03_skyview** — SkyView (NASA GSFC): DSS2 Blue + 2MASS-K cutouts of three test fields; GALEX NUV (M44, Omega Cen).
- **04_cds** — CDS Strasbourg: TAPVizieR watchlist extracts (VSX, GCVS, Byurakan, ...); SIMBAD benchmark objects.
- **05_ned** — NED (IPAC): Object queries for the benchmark target list.
- **06_eso** — ESO Science Archive: HARPS ObsCore metadata + two reduced spectra via DATALINK.
- **07_irsa** — IRSA (IPAC): AllWISE source-catalog cones; ZTF light curves at four anchors.
- **08_legacy_survey** — Legacy Survey (LS DR9/DR10): Brick listings + DR9 tractor catalogs; DR9/DR10 cutouts; unWISE cutout.

## Volume vs. request (as-built, 2026-09-24)

The as-built verified pack is **1112.1 MB across 82 checksummed data products**, below the 5–10 GB size range chosen at scope time. The shortfall is a property of the queried products, not of missing coverage: every service is represented. Scaling notes for a later round (recorded so they are not rediscovered): TESS SPOC LC files are ~2 MB each (a 5 GB TESS-only pack needs ~2500 files); the NGC 6819 Kepler cluster stars have ~0.2–0.5 MB quarter LCs (cluster targets are faint); the TAP row caps (Gaia sync, TAPVizieR, IRSA) bound single-query extracts; and the largest single lever remains larger TESScut cubes (30 px cubes already yield 23–198 MB each — 60 px cubes would give ~1 GB per sector but must be guarded against memory limits).

## Verified data gaps and limitations (recorded, not hidden)

- **MAST** — 'GJ 1214' has no SPOC 2-min series in the searched cone (probe recorded); several `_a_fast` observations hold no LC subgroup. JWST/HST samples are single-observation picks, not survey coverage.
- **MAST (earlier staging run)** — the `mast` pack's 2026-09-23 SPOC name probes recorded 12 targets (WASP-12, HD 209458, Pi Mensae, TRAPPIST-1, 51 Peg, KIC 8462852, T Tau, AU Mic, WASP-126, DS Tuc, Iota Horologii, GJ 1214) as "zero SPOC timeseries observations matched". For eleven of them that was a transient MAST condition: the corrected `01_mast` cone run (2026-09-24) found them, and a live re-check on 2026-09-25 returned 11 SPOC rows for WASP-12 with the same query. GJ 1214's zero is genuine (no TESS data even in a 1° cone, re-checked 2026-09-25). The earlier manifest is kept for provenance but is now **listed as restricted, not published**.
- **SkyView** — 'WISE 12' returned HTTP 404 for all three fields (SkyView's WISE service unavailable on 2026-09-23/24); GALEX NUV and SDSS g have no coverage for Pleiades in the served footprint. Recorded per-field as failed/excluded rows.
- **Gaia** — `xp_sampled_mean_spectrum` is absent from the live `tap_schema` dump (2026-09-24); `xp_summary` was retrieved instead. `nss_acceleration` and `vari_eb` do not exist by those names; the live schema names `nss_acceleration_astro` and `vari_eclipsing_binary` were used.
- **CDS** — VSX table id is `B/vsx/vsx` (live-verified); the probe fallback name `B/vsx` does not resolve in TAPVizieR. Extracts are TOP 20000 row samples of watchlist catalogs, not full catalogs.
- **ESO** — `ivoa.ObsCore` has no `dataRights` column (400 observed); HARPS products were resolved through the DATALINK service. Two reduced spectra retrieved (smallest by access_estsize among the TOP 100 metadata rows).
- **IRSA** — the 20-column AllWISE query is rejected server-side (async phase=ERROR); the six-column list was used. 2MASS point-source catalog is not served via IRSA TAP (image-metadata tables only) — recorded as an exclusion.
- **Legacy Survey** — the old `/api/region/tractor` service is retired (nginx 404s); access now goes through `/viewer/bricks/` + the NERSC portal DR9 layout. Omega Centauri (NGC 5139) has no DR9 bricks listed and only a near-empty DR9 cutout (out of footprint); DR9 fits-cutouts for NGC 5139 and Pleiades failed while DR10 worked for Omega Cen. These gaps are recorded, not worked around.

## Machine log (collector stdout, chronological)

```
# CYGNUS Tier-1 pack — search log (machine-written)

## gaia

    [2026-09-24T01:14:40Z] [gaia] >>> service start (pack_dir=02_gaia)
    [2026-09-24T01:14:48Z] [gaia] OK: tap_schema_gaiadr3_tables (65842 bytes)
    [2026-09-24T01:15:00Z] [gaia] OK: gaia_source_cone_Pleiades_r0d5 (1978732 bytes)
    [2026-09-24T01:15:10Z] [gaia] OK: gaia_source_cone_M44_r0d5 (1395768 bytes)
    [2026-09-24T01:16:15Z] [gaia] OK: gaia_source_cone_NGC_5139_r0d5 (29576053 bytes)
    [2026-09-24T01:16:38Z] [gaia] OK: gaia_source_cone_Pleiades_r1d0 (8254154 bytes)
    [2026-09-24T01:16:51Z] [gaia] OK: gaia_source_cone_M44_r1d0 (5476208 bytes)
    [2026-09-24T01:18:34Z] [gaia] OK: gaia_source_cone_NGC_5139_r1d0 (58046990 bytes)
    [2026-09-24T01:20:36Z] [gaia] OK: nss_two_body_orbit_top100k (68560723 bytes)
    [2026-09-24T01:22:40Z] [gaia] OK: nss_acceleration_astro_top100k (64885382 bytes)
    [2026-09-24T01:24:38Z] [gaia] OK: vari_rrlyrae_top50k (69586876 bytes)
    [2026-09-24T01:25:18Z] [gaia] OK: vari_eclipsing_binary_top50k (21240074 bytes)
    [2026-09-24T01:25:34Z] [gaia] OK: vari_summary_top10k (6671445 bytes)
    [2026-09-24T01:25:42Z] [gaia] OK: xp_summary_top5000 (679423 bytes)
    [2026-09-24T01:25:42Z] [gaia] <<< service end; bytes_used=336417670

## irsa

    [2026-09-24T01:46:37Z] [irsa] >>> service start (pack_dir=07_irsa)
    [2026-09-24T01:46:39Z] [irsa] OK: tap_schema_probe (2477 bytes)
    [2026-09-24T01:46:54Z] [irsa] OK: allwise_Pleiades_r0d5 (495790 bytes)
    [2026-09-24T01:47:12Z] [irsa] OK: allwise_M44_r0d5 (600707 bytes)
    [2026-09-24T01:47:35Z] [irsa] OK: allwise_NGC_5139_r0d5 (1226565 bytes)
    [2026-09-24T01:47:35Z] [irsa] SKIP (drive_only): ztf_lc_Pleiades_16as
    [2026-09-24T01:47:58Z] [irsa] OK: ztf_lc_Pleiades_72as (837033 bytes)
    [2026-09-24T01:47:58Z] [irsa] SKIP (drive_only): ztf_lc_M44_16as
    [2026-09-24T01:48:51Z] [irsa] OK: ztf_lc_M44_72as (4112439 bytes)
    [2026-09-24T01:48:51Z] [irsa] SKIP (drive_only): ztf_lc_NGC_5139_16as
    [2026-09-24T01:49:04Z] [irsa] OK: ztf_lc_NGC_5139_72as (162 bytes)
    [2026-09-24T01:49:04Z] [irsa] SKIP (drive_only): ztf_lc_NGC_6819_16as
    [2026-09-24T01:58:16Z] [irsa] FAIL: ztf_lc_NGC_6819_72as: ReadTimeout
    [2026-09-24T01:58:16Z] [irsa] <<< service end; bytes_used=7275173

## legacysurvey

    [2026-09-24T01:25:42Z] [legacysurvey] >>> service start (pack_dir=08_legacy_survey)
    [2026-09-24T01:25:44Z] [legacysurvey] OK: bricks_listing_M44_dr9 (3635 bytes)
    [2026-09-24T01:25:44Z] [legacysurvey] bricks in box 'M44' (ls-dr9): 24; first: 1294p190, 1294p197, 1294p200, 1295p195
    [2026-09-24T01:27:21Z] [legacysurvey] FAIL: tractor_dr9_north_1294p190: HTTPError
    [2026-09-24T01:27:25Z] [legacysurvey] OK: tractor_dr9_south_1294p190 (12283200 bytes)
    [2026-09-24T01:29:05Z] [legacysurvey] FAIL: tractor_dr9_north_1294p197: HTTPError
    [2026-09-24T01:29:30Z] [legacysurvey] OK: tractor_dr9_south_1294p197 (12672000 bytes)
    [2026-09-24T01:29:32Z] [legacysurvey] OK: bricks_listing_Pleiades_dr9 (13 bytes)
    [2026-09-24T01:29:32Z] [legacysurvey] no bricks listed for 'Pleiades' (ls-dr9)
    [2026-09-24T01:29:34Z] [legacysurvey] OK: bricks_listing_NGC_5139_dr10 (2815 bytes)
    [2026-09-24T01:29:34Z] [legacysurvey] bricks in box 'NGC 5139' (ls-dr10): 18; first: 2010m480, 2011m472, 2012m475, 2012m477
    [2026-09-24T01:31:13Z] [legacysurvey] FAIL: tractor_dr10_north_2010m480: HTTPError
    [2026-09-24T01:35:53Z] [legacysurvey] OK: tractor_dr10_south_2010m480 (16104960 bytes)
    [2026-09-24T01:37:31Z] [legacysurvey] FAIL: tractor_dr10_north_2011m472: HTTPError
    [2026-09-24T01:37:42Z] [legacysurvey] OK: tractor_dr10_south_2011m472 (45132480 bytes)
    [2026-09-24T01:37:42Z] [legacysurvey] SKIP (drive_only): cutout_M44_r_ls-dr9
    [2026-09-24T01:37:49Z] [legacysurvey] OK: cutout_M44_r_ls-dr10 (362880 bytes)
    [2026-09-24T01:37:49Z] [legacysurvey] SKIP (drive_only): cutout_M44_grz_jpeg_ls-dr9
    [2026-09-24T01:40:41Z] [legacysurvey] FAIL: cutout_NGC_5139_r_ls-dr9: RequestException
    [2026-09-24T01:40:41Z] [legacysurvey] SKIP (drive_only): cutout_NGC_5139_r_ls-dr10
    [2026-09-24T01:40:41Z] [legacysurvey] SKIP (drive_only): cutout_NGC_5139_grz_jpeg_ls-dr9
    [2026-09-24T01:43:41Z] [legacysurvey] FAIL: cutout_Pleiades_r_ls-dr9: RequestException
    [2026-09-24T01:46:35Z] [legacysurvey] FAIL: cutout_Pleiades_r_ls-dr10: RequestException
    [2026-09-24T01:46:35Z] [legacysurvey] SKIP (drive_only): cutout_Pleiades_grz_jpeg_ls-dr9
    [2026-09-24T01:46:35Z] [legacysurvey] SKIP (drive_only): unwise_cutout_M44_unwise-neo7
    [2026-09-24T01:46:37Z] [legacysurvey] OK: unwise_cutout_M44_unwise-neo6 (43200 bytes)
    [2026-09-24T01:46:37Z] [legacysurvey] <<< service end; bytes_used=86605183

## mast

    [2026-09-24T00:50:18Z] [mast] >>> service start (pack_dir=01_mast)
    [2026-09-24T00:51:41Z] [mast] SKIP (drive_only): tess2018206045859-s0001-0000000261136679-0120-s_lc.fits
    [2026-09-24T00:51:52Z] [mast] OK: tess2019032160000-s0008-0000000261136679-0136-s_lc.fits (1805760 bytes)
    [2026-09-24T00:51:59Z] [mast] no TESS LC product for obs tess2021014023720-s0034-0000000261136679-0204-a_fast
    [2026-09-24T00:52:05Z] [mast] no TESS LC product for obs tess2023096110322-s0064-0000000261136679-0257-a_fast
    [2026-09-24T00:52:11Z] [mast] no TESS LC product for obs tess2025014115807-s0088-0000000261136679-0285-a_fast
    [2026-09-24T00:52:18Z] [mast] SKIP (drive_only): tess2025206162959-s0095-0000000261136679-0292-s_lc.fits
    [2026-09-24T00:52:36Z] [mast] no TESS LC product for obs tess2019199201929-s0014-s0086-0000000420814525
    [2026-09-24T00:52:39Z] [mast] no TESS LC product for obs tess2022244194134-s0056-0000000420814525-0243-a_fast
    [2026-09-24T00:52:46Z] [mast] SKIP (drive_only): tess2022244194134-s0056-0000000420814525-0243-s_lc.fits
    [2026-09-24T00:52:54Z] [mast] no TESS LC product for obs tess2024223182411-s0082-0000000420814525-0278-a_fast
    [2026-09-24T00:53:01Z] [mast] SKIP (drive_only): tess2024223182411-s0082-0000000420814525-0278-s_lc.fits
    [2026-09-24T00:53:17Z] [mast] no TESS LC product for obs tess2018206190142-s0001-s0046-0000000086396382
    [2026-09-24T00:53:28Z] [mast] OK: tess2019357164649-s0020-0000000086396382-0165-s_lc.fits (1926720 bytes)
    [2026-09-24T00:53:43Z] [mast] OK: tess2021258175143-s0043-0000000086396382-0214-s_lc.fits (1811520 bytes)
    [2026-09-24T00:53:58Z] [mast] OK: tess2021310001228-s0045-0000000086396382-0216-s_lc.fits (1840320 bytes)
    [2026-09-24T00:54:15Z] [mast] OK: tess2023289093419-s0071-0000000086396382-0266-s_lc.fits (1897920 bytes)
    [2026-09-24T00:54:21Z] [mast] SKIP (drive_only): tess2023315124025-s0072-0000000086396382-0267-s_lc.fits
    [2026-09-24T00:54:35Z] [mast] no TESS LC product for obs tess2023263165758-s0070-0000000278892590-0265-a_fast
    [2026-09-24T00:54:39Z] [mast] SKIP (drive_only): tess2023263165758-s0070-0000000278892590-0265-s_lc.fits
    [2026-09-24T00:54:41Z] [mast] no SPOC timeseries obs within 0.05 deg of 'GJ 1214'; probe recorded
    [2026-09-24T00:54:49Z] [mast] no TESS LC product for obs tess2022244194134-s0056-0000000139298196-0243-a_fast
    [2026-09-24T00:55:02Z] [mast] OK: tess2022244194134-s0056-0000000139298196-0243-s_lc.fits (2039040 bytes)
    [2026-09-24T00:55:09Z] [mast] no TESS LC product for obs tess2024249191853-s0083-0000000139298196-0280-a_fast
    [2026-09-24T00:55:16Z] [mast] SKIP (drive_only): tess2024249191853-s0083-0000000139298196-0280-s_lc.fits
    [2026-09-24T00:55:39Z] [mast] SKIP (drive_only): tess2019198215352-s0014-0000000185336364-0150-s_lc.fits
    [2026-09-24T00:55:48Z] [mast] no TESS LC product for obs tess2019199201929-s0014-s0055-0000000185336364
    [2026-09-24T00:55:55Z] [mast] no TESS LC product for obs tess2021204101404-s0041-0000000185336364-0212-a_fast
    [2026-09-24T00:55:56Z] [mast] no TESS LC product for obs tess2022190063128-s0054-0000000185336364-0227-a_fast
    [2026-09-24T00:56:03Z] [mast] no TESS LC product for obs tess2022217014003-s0055-0000000185336364-0242-a_fast
    [2026-09-24T00:56:06Z] [mast] SKIP (drive_only): tess2022217014003-s0055-0000000185336364-0242-s_lc.fits
    [2026-09-24T00:56:25Z] [mast] no TESS LC product for obs tess2021233042500-s0042-s0046-0000000017308640
    [2026-09-24T00:56:32Z] [mast] SKIP (drive_only): tess2021258175143-s0043-0000000017308640-0214-s_lc.fits
    [2026-09-24T00:56:38Z] [mast] SKIP (drive_only): tess2021284114741-s0044-0000000017308640-0215-s_lc.fits
    [2026-09-24T00:56:56Z] [mast] SKIP (drive_only): tess2018206045859-s0001-0000000441420236-0120-s_lc.fits
    [2026-09-24T00:56:58Z] [mast] no TESS LC product for obs tess2018206190142-s0001-s0036-0000000441420236
    [2026-09-24T00:57:00Z] [mast] no TESS LC product for obs tess2018206190142-s0001-s0096-0000000441420236
    [2026-09-24T00:57:12Z] [mast] OK: tess2020186164531-s0027-0000000441420236-0189-s_lc.fits (1785600 bytes)
    [2026-09-24T00:57:19Z] [mast] no TESS LC product for obs tess2025206162959-s0095-0000000441420236-0292-a_fast
    [2026-09-24T00:57:25Z] [mast] SKIP (drive_only): tess2025206162959-s0095-0000000441420236-0292-s_lc.fits
    [2026-09-24T00:58:51Z] [mast] SKIP (drive_only): tess2018206045859-s0001-0000000025155310-0120-s_lc.fits
    [2026-09-24T00:59:06Z] [mast] OK: tess2018292075959-s0004-0000000025155310-0124-s_lc.fits (1897920 bytes)
    [2026-09-24T00:59:21Z] [mast] OK: tess2020212050318-s0028-0000000025155310-0190-s_lc.fits (1848960 bytes)
    [2026-09-24T00:59:26Z] [mast] no TESS LC product for obs tess2021065132309-s0036-0000000025155310-0207-a_fast
    [2026-09-24T00:59:38Z] [mast] OK: tess2023181235917-s0067-0000000025155310-0261-s_lc.fits (2027520 bytes)
    [2026-09-24T00:59:44Z] [mast] SKIP (drive_only): tess2025312202959-s0098-0000000025155310-0298-s_lc.fits
    [2026-09-24T01:00:01Z] [mast] SKIP (drive_only): tess2018206045859-s0001-0000000410214986-0120-s_lc.fits
    [2026-09-24T01:00:06Z] [mast] no TESS LC product for obs tess2020186164531-s0027-0000000410214986-0189-a_fast
    [2026-09-24T01:00:10Z] [mast] no TESS LC product for obs tess2023181235917-s0067-0000000410214986-0261-a_fast
    [2026-09-24T01:00:22Z] [mast] OK: tess2025180145000-s0094-0000000410214986-0291-s_lc.fits (1892160 bytes)
    [2026-09-24T01:00:34Z] [mast] OK: tess2026086090000-s0102-0000000410214986-0304-s_lc.fits (1808640 bytes)
    [2026-09-24T01:00:47Z] [mast] SKIP (drive_only): tess2026137223500-s0104-0000000410214986-0306-s_lc.fits
    [2026-09-24T01:01:30Z] [mast] SKIP (drive_only): tess2018234235059-s0002-0000000166853853-0121-s_lc.fits
    [2026-09-24T01:01:43Z] [mast] no TESS LC product for obs tess2020238165205-s0029-0000000166853853-0193-a_fast
    [2026-09-24T01:01:45Z] [mast] no TESS LC product for obs tess2020266004630-s0030-0000000166853853-0195-a_fast
    [2026-09-24T01:01:53Z] [mast] OK: tess2023237165326-s0069-0000000166853853-0264-s_lc.fits (1886400 bytes)
    [2026-09-24T01:02:13Z] [mast] OK: tess2025258001959-s0097-0000000166853853-0294-s_lc.fits (3962880 bytes)
    [2026-09-24T01:02:22Z] [mast] SKIP (drive_only): tess2026164183000-s0105-0000000166853853-0307-s_lc.fits
    [2026-09-24T01:06:15Z] [mast] OK: kplr005023822-2009166043257_llc.fits (192960 bytes)
    [2026-09-24T01:06:18Z] [mast] no Kepler LC product for obs kplr005023822_sc_Q001003033303330332
    [2026-09-24T01:06:34Z] [mast] OK: kplr005023849-2009350155506_llc.fits (466560 bytes)
    [2026-09-24T01:06:43Z] [mast] no Kepler LC product for obs kplr005023849_sc_Q000103000300000000
    [2026-09-24T01:06:50Z] [mast] OK: kplr005023890-2009259160929_llc.fits (466560 bytes)
    [2026-09-24T01:06:56Z] [mast] no Kepler LC product for obs kplr005023890_sc_Q001003003300000000
    [2026-09-24T01:07:03Z] [mast] OK: kplr005023948-2010355172524_llc.fits (466560 bytes)
    [2026-09-24T01:07:07Z] [mast] no Kepler LC product for obs kplr005023948_sc_Q000000000000100000
    [2026-09-24T01:07:19Z] [mast] OK: kplr005023956-2009166043257_llc.fits (192960 bytes)
    [2026-09-24T01:07:27Z] [mast] no Kepler LC product for obs kplr005023956_sc_Q010000000000000000
    [2026-09-24T01:07:34Z] [mast] OK: kplr005024084-2009166043257_llc.fits (192960 bytes)
    [2026-09-24T01:07:37Z] [mast] no Kepler LC product for obs kplr005024084_sc_Q000010000000000000
    [2026-09-24T01:07:45Z] [mast] OK: kplr005024149-2010355172524_llc.fits (466560 bytes)
    [2026-09-24T01:07:50Z] [mast] no Kepler LC product for obs kplr005024149_sc_Q000000033300000000
    [2026-09-24T01:07:55Z] [mast] OK: kplr005024150-2009166043257_llc.fits (192960 bytes)
    [2026-09-24T01:08:02Z] [mast] no Kepler LC product for obs kplr005024150_sc_Q010000000300000000
    [2026-09-24T01:08:28Z] [mast] OK: tesscut-Pleiades-sec42-30px (63889920 bytes)
    [2026-09-24T01:10:12Z] [mast] OK: tesscut-Pleiades-sec71-30px (197542080 bytes)
    [2026-09-24T01:10:37Z] [mast] OK: tesscut-M44-sec44-30px (59264640 bytes)
    [2026-09-24T01:10:52Z] [mast] OK: tesscut-M44-sec1751-30px (33194880 bytes)
    [2026-09-24T01:11:04Z] [mast] OK: tesscut-NGC_5139-sec11-30px (22590720 bytes)
    [2026-09-24T01:12:02Z] [mast] OK: tesscut-NGC_5139-sec102-30px (188582400 bytes)
    [2026-09-24T01:13:52Z] [mast] SKIP (drive_only): jw02736-o003_t001_niriss_f115w-gr150c_c1d.fits
    [2026-09-24T01:13:52Z] [mast] SKIP (drive_only): jw02736003001_02104_00001_nis_x1d.fits
    [2026-09-24T01:13:52Z] [mast] JWST sample complete (spectrum)
    [2026-09-24T01:14:40Z] [mast] SKIP (drive_only): oc2k45010_asn.fits
    [2026-09-24T01:14:40Z] [mast] SKIP (drive_only): oc2k45gpj_epc.fits
    [2026-09-24T01:14:40Z] [mast] HST sample complete (spectrum)
    [2026-09-24T01:14:40Z] [mast] <<< service end; bytes_used=596134080

## run

    [2026-09-24T00:50:18Z] [run] run_id=29 config_hash=7dbe8179b2a213c2e4a04ec2b442de482c98ee2f

```