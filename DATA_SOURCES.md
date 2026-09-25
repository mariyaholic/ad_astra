# CYGNUS DATA SOURCES — Data-Gathering Reference

Maintained: 2026-09-24 (UTC).
Verification tags: **[V]** = service live-fetched and read during the Tier-1 pack build (2026-09-23/24); **[K]** = knowledge-based (re-verify before relying on it for a consequential claim or dossier entry). Tag every reuse of these entries in dossiers likewise.

Scope: free access to telescope/satellite **data** and to **steerable observing time**, under the relaxed bar agreed with the user (fully anonymous where possible; simple free account acceptable).

## 0. Tier-1 baseline pack (built 2026-09-23/24)

A provenance-logged sample of every §1 archive was built by
`cygnus.ingest.tier1` (see `ANALYSIS_STACK.md`, `tools/build_pack_docs.py`)
and lives at **`cygnus:Cygnus/data/tier1/`** with per-service manifests
(sha256+md5, exact endpoints, verbatim queries) and `MASTER_MANIFEST.csv`.
**Retention (user instruction, 2026-09-24): bulky data is Drive-hosted only;
staged local copies are deleted after rclone MD5 verification.** Worktree
keeps code, ledger (`state/ledger.sqlite`), and manifests
(`docs/tier1_pack/`). Re-download any product from the recorded URLs; never
run `rclone sync` from an emptied staging dir (it would mirror the emptiness
and delete the Drive copy — use `rclone copy`).

The optional `cygnus.analysis` suite (`docs/ANALYSIS_SUITE.md`) offers bounded,
read-only reanalysis pilots for selected pack products. Its Colab notebook first
checks the manifest and SHA-256; it does not establish that Drive is mounted,
that a catalog is complete, or that an anomaly is a new object. Existing pack
fields/epochs are targeted samples, not a blind or unsurveyed sky census.

Service quirks verified live (use these; re-verify dates if claims become consequential):
- **MAST** [V 2026-09-23]: CAOM `target_name` is the TIC id (`261136679` for Pi Mensae) — cone search + nearest-target group works; exact-name probes return zero. Kepler LC subgroup is `LLC` (TESS SPOC LC is `LC`). JWST/HST cone + `obs_collection` works (`provenance_name='JWST'` is actually `CALJWST`). File API: `https://mast.stsci.edu/api/v0.1/Download/file?uri=<dataURI>`.
- **MAST re-verified 2026-09-25** [V]: TESS SPOC timeseries queries need the **bare TIC number** as `target_name` (`'197807043'` → 8 obs; `'TIC 197807043'` / `'TIC197807043'` → 0). Genuine absorption-distinct absence verified: TIC 44161614 (TOI-7176.01) returns 0 SPOC timeseries rows at every filter strictness — a 0.02° cone shows only SPOC **FFI** observations (sectors 56, 83) and no 'TESS' target_name rows; absence is target-level, not query-level. A portal that answers famous-target queries (HD 209458 → 26 734 obs) is healthy: judge "service down" only from control queries failing on the same path.
- **Gaia** [V 2026-09-23/24]: use TAP `FORMAT=csv` — astropy's VOTable *binary* reader decodes var-char fields with a hardcoded ascii codec and raises on non-ASCII bytes; pyvo fails similarly on tap_schema descriptions. Live table names: `nss_acceleration_astro` (not `nss_acceleration`), `vari_eclipsing_binary` (not `vari_eb`); `xp_sampled_mean_spectrum` absent from the live gaiadr3 schema dump (`xp_summary` present).
- **CDS** [V 2026-09-23/24]: TAPVizieR `tap_schema.tables.table_name` values arrive already quote-wrapped (`"'B/vsx/vsx'"`); VSX's real id is `B/vsx/vsx` (`B/vsx` alone 400s "table not found"). Sync row caps apply; async queue can idle long.
- **ESO** [V 2026-09-24]: `ivoa.ObsCore` has no `dataRights` column (400); `access_url` is a DATALINK pointer (`/datalink/links?ID=...`) whose VOTable rows hold the actual `.fits` URLs (resolve smallest science product).
- **IRSA** [V 2026-09-23/24]: TAP works with `CONTAINS(POINT('J2000',...))=1`; AllWISE catalog table is `allwise_p3as_psd` and a 20-column list is rejected server-side (6-column subset works); `tap_schema.tables` rows come back as unnamed `col_0/col_1` columns; 2MASS point-source catalog is **not** served via TAP (image tables only). ZTF CGI (`/cgi-bin/ZTF/nph_light_curves`) accepts only `POS`+`FORMAT` (`MERGE`/`BAD_DATA` → 400 UsageFault).
- **Legacy Survey** [V 2026-09-23/24]: the old `/api/region/tractor` and `/api/brick` are retired (nginx 404s); live routes are `/viewer/bricks/?ralo=..&rahi=..&declo=..&dechi=..&layer=...` (JSON `polys[].name` = brick names) and tractor files at `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr{9,10}/{north|south}/tractor/{AAA}/tractor-{brick}.fits` (documented in `dr9/files`). LS/unWISE layers: **CC BY 4.0** with required credit "Legacy Surveys / D. Lang (Perimeter Institute)" (acknowledgment page fetched 2026-09-24).
- **SkyView** [V 2026-09-23]: survey names verified against `SkyView.survey_dict` (`DSS2 Blue`, `2MASS-K`, `WISE 12`, `GALEX Near UV`, `SDSSg`); WISE requests returned HTTP 404 on 2026-09-23/24 (service unavailable).
- **NED** [V 2026-09-23]: `astroquery.ned` works but is deprecated (moved to `astroquery.ipac.ned`).

---

## 1. Deep-sky astronomy archives (anonymous — no account)

| Service | URL | Script access | What you get |
| --- | --- | --- | --- |
| MAST (STScI) — HST, JWST, TESS, Kepler/K2, Pan-STARRS, GALEX, HLSPs | https://mast.stsci.edu/ [V] | `astroquery.mast` (portal API, TAP) | FITS/level-3 products, light curves, HLSPs; anonymous downloads for public data |
| Gaia Archive (ESA) | https://gea.esac.esa.int/archive/ [K] | ADQL via `astroquery.gaia` / TAP+ | astrometry, photometry, RV, NSS tables (DR3) |
| SkyView (NASA GSFC/HEASARC) | https://skyview.gsfc.nasa.gov/ [V] | `astroquery.skyview` | multi-survey cutouts: DSS, 2MASS, SDSS, GALEX, WISE, UKIDSS, FIRST, AKARI, TESS FFI |
| CDS Strasbourg (VizieR / SIMBAD / Aladin) | https://vizier.cds.unistra.fr/ · https://simbad.cds.unistra.fr/ [K] | `astroquery.vizier`, `astroquery.simbad`, TAP | tens of thousands of catalogs; object cross-IDs; TAP anonymous |
| NED (NASA/IPAC) | https://ned.ipac.caltech.edu/ [K] | `astroquery.ned` | extragalactic identifications, references |
| ESA Sky | https://esasky.esa.int/ [K] | browser | integrated viewer for ESA (JWST/HST? Euclid, Gaia, XMM) + missions |
| ESO Science Archive | https://archive.eso.org/ [K] | `astroquery.eso`, TAP | VLT/ALMA/large programs; public products anonymous |
| IRSA (NASA/IPAC) — WISE, 2MASS, ZTF | https://irsa.ipac.caltech.edu/ [K] | `astroquery.irsa`, IRSA TAP | all-WISE catalogs, ZTF light curves (main ZTF IRSA mirror) |
| Legacy Survey viewer / unWISE coadds | https://www.legacysurvey.org/viewer [K] | REST z-cutout API | deep optical N-S imaging + unWISE IR, anonymous cutouts |

## 2. Earth-observation archives (satellite imagery)

| Service | URL | Access tier | Notes |
| --- | --- | --- | --- |
| NASA Earthdata (Earthdata Search, DAACs) | https://www.earthdata.nasa.gov/ [V] | free Earthdata Login for downloads [V] | MODIS, VIIRS, GPM, Landsat (LP DAAC), ICESat-2, HLS; operational banner: **Suomi NPP delivery ends 2026-11-01 → migrate to NOAA-20/21 products** [V] |
| Worldview / GIBS | https://worldview.earthdata.nasa.gov/ [K] | anonymous browsing [K] | near-real-time map imagery |
| FIRMS (fires) | https://firms.modaps.eosdis.nasa.gov/ [K] | browse anonymous, download needs Earthdata Login [K] | |
| ASF Vertex (Alaska Satellite Facility DAAC) | https://search.asf.alaska.edu/ [K] | free Earthdata Login [K] | SAR: Sentinel-1, ALOS, RCM, SMAP |
| Copernicus Data Space Ecosystem (CDSE) | https://dataspace.copernicus.eu/ [V] | Copernicus Browser viewing anonymous [V: homepage wording]; downloads/API/openEO/STAC/JupyterLab need free account [V/K] | Sentinel-1/2/3/5P full archive; openEO server-side processing |
| Sentinel-2 / Landsat COGs on AWS open buckets | [K] | anonymous S3 reads | best scripted route for EO without any login |
| USGS EarthExplorer | https://earthexplorer.usgs.gov/ [K] | free USGS account [K] | full Landsat history incl. oldest MSS |
| space-track.org | https://www.space-track.org/ [K] | free account [K] | TLEs for satellite tracking sifsa (tangent to imaging but useful) |

Caveat retained from audit: CDSE replaced SciHub (Oct 2023) — anonymous bulk download claims seen in older guides are stale. Anonymous fallback = AWS open buckets.

## 3. Steerable telescope time

| Route | URL | Access tier | Capabilities / limits |
| --- | --- | --- | --- |
| MicroObservatory / Observing With NASA (CfA) | https://mo-www.cfa.harvard.edu/OWN/ · control: https://mo-www.cfa.harvard.edu/cgi-bin/OWN/Own.pl [V both] | free, **no account** | fixed curated target list (incl. Cyg X-1, Algol, SS Cyg, T CrB, Mira, Delta Cep, planets, Moon, Sun); flow = target → settings → email → submit; image (JPEG+FITS) typically next day; no custom RA/Dec |
| Skynet Robotic Telescope Network (UNC) | https://skynet.unc.edu/ [V] | free simple sign-up [V/K: login required] | custom RA/Dec, filters, integrations, scheduling queue; professional scopes (PROMPT @ CTIO, Yerkes, …) + radio (Green Bank); efficiencies table published; next-gen "Skynet Global Observatory" in preview @ https://skynetgo.org [V] |
| Competitive proposal time (free ≠ queue-free) | JDox: https://jwst-docs.stsci.edu/ [V — Cycle 6 call open, dual-anonymous review] · Gemini/NRAO/ESO [K] | registration + TAC proposal | JWST/HST/GBT/VLBA/ESO/VLT; institutional-affiliation expectations; not "drop-in" time |

## 4. JWST free-data specifics

- **Primary and canonical: MAST** — https://mast.stsci.edu/ [V]; via `astroquery.mast`. Anonymous downloads for public data.
- **ESA mirror: ESA JWST Science Archive** — https://jwst.esac.esa.int/archive/ [V].
- Access rule [K, confirm on policy page]: products become public when each program's exclusive-access period ends — default **12 months**; commissioning/early-release data were public essentially immediately; by 2026 the large majority of Cycle 1–3 (2022–2025) observations are public. Policy page: NASA-SMD Policy 2 "Data Rights and Data Dissemination" in JDox [V-fetched; body app-gated, nav only — open in a browser to read the full text].

## 5. Supplementary solar-system services (agent addition, beyond user's list)

| Service | URL | Access | Use |
| --- | --- | --- | --- |
| JPL Horizons | https://ssd.jpl.nasa.gov/horizons/ [K] | anonymous | ephemerides for asteroids, small bodies, SSO prospects |
| JPL Small-Body Database API | https://ssd-api.jpl.nasa.gov/sbdb.api [K] | anonymous | orbital elements, fit parameter lookups |
| MPC (Minor Planet Center) | https://minorplanetcenter.net/ [K] | mostly anonymous | IHB/NECP candidate checks before "uncataloged" claims |
| AstDyS / NEODyS | https://newton.spacedys.com/astdys/ [K] | anonymous | independent orbit solutions |

---

## 6. Worktree access mechanics & hygiene

- **Scripting stack:** `astroquery`, `pyvo` (TAP/VO), `astropy`, `lightkurve`; EO side via STAC API / openEO / direct S3 bucket reads. Tier-1 retrieval uses the byte-safe `TapDirect` client (`src/cygnus/ingest/tap.py`, CSV-first) with `astroquery` for MAST/SkyView/SIMBAD/NED search stages.
- **Downloads land in** `D:\AO_Artifacts\cygnus_scratch\` (nonsynced, disposable). Curated outputs and reports go to the connected Google Drive at `cygnus:Cygnus/` (rclone remote; scope `drive.file` — see AGENTS.md). **Retention (2026-09-24): bulk data is Drive-hosted only; staged files are deleted after rclone MD5 verification; worktree retains code + ledger + manifests.**
- **Credentials:** kept out of the repo and out of logs/transcripts: never pasted into code, dossiers, or search logs. Centralize auth in uncommitted environment files. One free account each (Earthdata, CDSE) covers all Tier-2 services; note which tokens were configured and when without logging the secrets themselves.
- **Query discipline for every retrieval:** record endpoint, exact query/selection text, UTC retrieval date, catalog/release identifier, product IDs (and checksums when served), plus package versions. This is the provenance trail dossier sections point at.
- **Rate limits:** honor each service's published concurrency policies; back off on HTTP 429/503; prefer resumable chunked downloads over restart-from-scratch.
- **Verification tags traveled with the data:** any [K] entry used in a dossier or magnitude/mass estimate must first be re-verified live (or replaced by an authoritative citation) when the claim becomes consequential.
