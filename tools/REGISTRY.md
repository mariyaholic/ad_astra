# Repository tools

| Tool | Purpose | Owner |
| --- | --- | --- |
| `register_colab_sync.ps1` | Register/update the canonical Windows task `\Cygnus-Colab-Sync`; `-VerifyOnly` inspects it. | Cygnus |
| `build_pages_bundle.py` | Assemble the explorer and curated repository pages; leak-scan the complete deployment bundle. | Cygnus |
| `push_site_branch.py` | Publish the built bundle through the existing `site` branch / Cloudflare workflow. | Cygnus |
| `build_pack_docs.py` | Generate baseline-pack documentation from its manifests. | Cygnus |
| `upload_verify_retire.py` | Upload, verify and retire eligible local pack copies; consult storage policy first. | Cygnus |
| `analyze_tess_residual.py` | Historical residual-screen pilot. Use the campaign runner for new known-object analyses. | Cygnus |

The Colab sync implementation is `src/cygnus/colab_sync.py`, not a second helper script.
