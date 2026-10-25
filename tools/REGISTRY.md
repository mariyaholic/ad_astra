# Repository tools

| Tool | Purpose | Owner |
| --- | --- | --- |
| `setup_cloud.py` | Create/reuse the cloud venv with CI extras; `--check` records offline readiness and package versions. | codex.impl |
| `register_colab_sync.ps1` | Register/update the canonical Windows task `\Cygnus-Colab-Sync`; `-VerifyOnly` inspects it. | Cygnus |
| `build_pages_bundle.py` | Assemble the explorer and curated repository pages; leak-scan the complete deployment bundle. | Cygnus |
| `push_site_branch.py` | Publish the built bundle through the existing `site` branch / Cloudflare workflow. | Cygnus |
| `build_pack_docs.py` | Generate baseline-pack documentation from its manifests. | Cygnus |
| `upload_verify_retire.py` | Upload, verify and retire eligible local pack copies; consult storage policy first. | Cygnus |
| `analyze_tess_residual.py` | Historical residual-screen pilot. Use the campaign runner for new known-object analyses. | Cygnus |

The Colab sync implementation is `src/cygnus/colab_sync.py`, not a second helper script.

The gated cloud entry point is `python -m cygnus.cloud {plan,run,status,report}`
(`src/cygnus/cloud.py`, owner `codex.impl`), not another batch/helper script.
Its `sources/scout/acquire` commands use `src/cygnus/cloud_scout.py` for finite
archive scouting, bounded retrieval and provenance-bound transit inputs.
