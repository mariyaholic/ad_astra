#!/usr/bin/env bash
# Run the experimental multi-archive pipeline from the repository root.
# Usage:  experimental/run.sh archives
#         experimental/run.sh run experimental/campaigns/<id>.yaml
# Sandbox root: $CYGNUS_MULTI_ROOT if set, else experimental/.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE/.."
export PYTHONPATH="$PWD/src:$PWD/experimental${PYTHONPATH:+:$PYTHONPATH}"
exec python -m experimental.cygnus_multi "$@"