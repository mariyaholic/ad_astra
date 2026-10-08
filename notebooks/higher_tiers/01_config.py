# Reusable defaults: no target list and no batch-specific run id.
SOURCE_RUN = 'latest'  # Or the exact stage-one RUN_ID when several batches are being run.
PINNED_COMMIT = '05ba4f4ee6e2053c256240ab04f7fbb527e32afe'
NOTEBOOK_REVISION = 'T2_WORKFLOW_REVISION'  # Replaced by the builder's source digest.
NULL_PARAMS = {'n_null': 300, 'n_inject': 100, 'min_n': 100}
# T3 spectra/PRF/RV and T4 are deliberately not enabled. The native runner lacks their full adapters.
# Run in one CPU runtime per source packet; do not connect two writers to the same output directory.
import re
if SOURCE_RUN != 'latest' and not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', SOURCE_RUN):
    raise ValueError('SOURCE_RUN must be latest or an exact first-stage RUN_ID')
if not re.fullmatch(r'[0-9a-f]{40}', PINNED_COMMIT):
    raise ValueError('Code pin must be a full pushed commit SHA')
print('Stage two:', NOTEBOOK_REVISION, '| source:', SOURCE_RUN, '| CPU, T2 only')
