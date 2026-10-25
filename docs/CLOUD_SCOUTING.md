# Public archive scouting and acquisition

Updated 2026-10-17 (Asia/Manila). This stage runs before scientific T0.
Its outputs establish selections, access and input integrity, never a detection,
scientific tier, on-target event or discovery. Read `AGENTS.md`, `STATUS.md`
and `CODEX_CLOUD.md` first.

## Run the finite pilot

From the repository root in the prepared cloud environment:

```bash
.venv/bin/python -m cygnus.cloud sources
.venv/bin/python -m cygnus.cloud scout cloud/scout.yaml
```

The second command prints `reports/cloud-scout/<id>/SCOUT.json`. Read its
source states, query/selection history, exclusions, target rows and product
references. Then use the actual printed path:

```bash
.venv/bin/python -m cygnus.cloud acquire reports/cloud-scout/<id>/SCOUT.json
```

This prints the corresponding `ACQUISITION.json`. Read the report, failed and
unavailable inputs, per-file source checks and all queues. If an acquired SPOC
input passes the exact TIC, declared TDB and native input-quality checks, it can
feed the existing transit controller:

```bash
.venv/bin/python -m cygnus.cloud plan cloud/workflow.yaml --acquisition reports/cloud-scout/<id>/ACQUISITION.json
# Use the cloud plan path printed by that command:
.venv/bin/python -m cygnus.cloud run state/cloud_runs/<cloud-id>/PLAN.json
```

The cloud plan independently refreshes the exact current TOI/TIC and ephemeris.
The parent verifies acquired bytes, copies them into the separate worker cache,
and pins their SHA-256/size in the native generated spec. The initial fetch step
reuses those files instead of rediscovering/downloading a different selection.
Other native steps may still retrieve new context or follow-up data.
No eligible transit input means stop that route and return the review queues;
do not invent a TIC or transit epoch for an unrelated catalogue source.

The earlier existing-queue route, `plan cloud/workflow.yaml` without
`--acquisition`, remains available when that is the requested campaign.

## Selection and source coverage

The pilot queries at most 100 current TOI rows ordered by TESS magnitude and
TOI, then applies the existing transparent ranking within that sample. Frozen,
retracted, already claimed and unusable rows are excluded. This is a declared
brightness-biased finite sample, not an all-sky census. The underlying query
uses the archive's documented [TAP/ADQL interface](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html).

One selected field then supplies bounded Gaia, VizieR/VSX, SIMBAD, NED and
AllWISE samples. Catalogue rows retain source IDs, coordinates, raw returned
rows, field association and position epoch. Unverified epochs remain explicit.
Equal positions do not merge cross-catalogue identities. Same-source duplicate
IDs are deduplicated; conflicting positions move that identity to review.

Retrieval targets are selected round-robin across source catalogues, up to
three targets. This ordering gives source diversity; it is not a scientific
anomaly score. Product discovery uses the native adapters and explicit limits:

| Source | Automatic route | Limits and interpretation |
| --- | --- | --- |
| MAST | TESS, Kepler/K2 light curves; HST/JWST science images | Exact TIC for known TESS targets; position searches elsewhere. Image products stay images. Metadata is not source-identity clearance. |
| Gaia, VizieR/VSX, SIMBAD, NED, NASA Exoplanet Archive | Catalogue queries and retained tables | Release/selection-bounded rows, not full catalogues. Proper-motion matching remains a separate review. |
| IRSA | AllWISE tables and small-radius ZTF time series | Sparse/irregular light curves remain time-series review inputs. |
| SkyView | Small multi-survey image cutouts | Resolve URLs with the documented `astroquery.skyview.get_image_list` path, then stream selected FITS bytes. A generated request is `planned` until a service answers. |
| Legacy Survey | Small optical/unWISE image cutouts | Survey/layer and selection retained; required survey credit preserved in native descriptions. |
| ESO | ObsCore discovery, Datalink science `#this` resolution and bounded public downloads | Auxiliary links are not substituted for science. HTTP 401/outages remain unavailable; a spectrum is not an extracted/calibrated RV. |
| KOA | HIRES metadata table | Raw/calibration acquisition remains a specialist route, not an automatic validated RV series. |
| Horizons, SBDB, MPC | Named-object context/observation records | Requires explicit object designations in `solar_objects`; no guessed coordinates. |
| SkyBoT | Known moving-object search for a field and observation epoch | Requires `epoch_utc` with UTC offset and an IAU/MPC observer code. No guessed epoch or spacecraft location. |

MAST discovery follows its [observation/product query interface](https://astroquery.readthedocs.io/en/latest/mast/mast_obsquery.html).
SkyView URL resolution follows its [documented image-list interface](https://astroquery.readthedocs.io/en/latest/skyview/skyview.html).
KOA's [TAP guide](https://koa.ipac.caltech.edu/UserGuide/PyKOA/TAPClients.html)
supports metadata access; a metadata answer never certifies raw-file rights.

`sources` inventories every registered adapter plus linked viewer/mirror routes.
Account-based Earth-observation/AOI services are outside this astronomical
campaign; viewer and telescope-request routes remain manual. ESA JWST products
use the canonical MAST route rather than downloading the same data from a
second mirror. Historical source-list verification tags are not live health
checks. No TLS checks or access restrictions are bypassed.

## Budgets, checkpoints and outputs

The pilot has one serial worker, 512 MiB retained acquisition scratch, 32 MiB
per product, at least 1 GiB free, three minutes per job, 30 minutes per
`scout`/`acquire` invocation and 100 new jobs per invocation. These are caps,
not quotas. Metadata-declared oversized files are excluded before download.
Direct science-file downloads use the existing resumable streaming retriever.
A truncated, empty or mismatched product cannot become a transit input.
Generated cutouts are deliberately small; some native adapters buffer their
bounded responses. Supervisor sampling can overshoot within one response.
Scratch occupancy is not a cumulative network-byte meter or a hard memory limit.

The parent records an attempt log and commits a per-job checkpoint only after
the worker exits and resource checks pass. Source requests record endpoints,
queries/selections and retrieval UTC without headers, credentials or session
state. Returned rows/references, native integrity checks, file hashes and byte
counts remain attributable to their jobs. Failed and unavailable attempts are
retained without a completed checkpoint.

To resume the same scout, pass its ignored state plan instead of the YAML:

```bash
.venv/bin/python -m cygnus.cloud scout state/cloud_scout/<id>/PLAN.json
.venv/bin/python -m cygnus.cloud acquire reports/cloud-scout/<id>/SCOUT.json
```

Verified jobs skip; failed jobs receive one new bounded attempt on an explicit
resume. Do not wrap either command in an unbounded retry loop. Changed source,
runtime, checkpoint, summary, queue or acquired bytes fail closed. Budget caps
apply per invocation; changing them requires a new plan. Preserve the same
cloud task and scratch. Automatic cross-task import/Drive retention is not added.

Small outputs live under `reports/cloud-scout/<id>/`:

- `SCOUT.json`, `LINEAGE.json`, per-job JSON and source/checkpoint receipts.
- `TARGET_QUEUE.csv`: all normalized target candidates with sample/rank rationale.
- `REVIEW_QUEUE.csv`: catalogue identities requiring scientific review.
- `TRANSIT_QUEUE.csv`: only targets with acquired, checked SPOC inputs.
- `ACQUISITION.json`: every download state, route, native quality check, checksum,
  byte count and portable scratch location; image/spectral review routes are here.
- `REPORT.md`, `SEARCH_LOG.md`, valid `sky_record.json` and `MANIFEST.sha256`.

Bulk bytes stay under `scratch:cloud_scout/<id>/products/`; resumability state,
locks and logs stay under ignored `state/cloud_scout/<id>/`. Each product route
is explicit. Only the compatible transit route is connected to the existing
T0–T3 tests; image, spectral, solar-system and other time-series routes remain
review queues with no fabricated tier completion or automatic publication.
