"""Assemble the reusable second-stage notebook from reviewable Python cell files."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / 'notebooks/higher_tiers'
OUTPUT = ROOT / 'notebooks/cygnus_higher_tiers_colab.ipynb'


def build():
    sections = [
        ('Configuration', '01_config.py',
         'Set SOURCE_RUN (latest by default), a reviewed code pin and the frozen null-draw settings.',
         'Run the same notebook on every first-stage batch with no manual target list or run-id edits.',
         'Configuration globals only; no file writes.',
         'An invalid source identifier or non-full commit SHA must stop immediately.'),
        ('Pinned CPU setup', '02_setup.py',
         'Mount Drive, clone the pinned tools and run their targeted offline gate; expect a few minutes.',
         'Separate code provenance from the source-data commit and keep all computation/scratch on the CPU VM.',
         'A VM checkout/environment and scratch directory; no first-stage or reviewed-record modifications.',
         'A wrong checkout, GPU/TPU, missing Cygnus folder or failed software gate must stop.'),
        ('Workflow helpers', 'workflow.py',
         'Load the shared orchestration; scientific calculations remain in the pinned campaign tools.',
         'Centralize discovery and checks so subsequent batches need no agent-written target lists.',
         'In-kernel workflow helpers; no archive queries or Drive writes.',
         'A bad packet or unearned target must be refused, never repaired or silently promoted.'),
        ('Discover first-stage results', '04_discover.py',
         'Choose the newest finalized first-stage lead export, verify its metadata and derive every earned T2 target; normally seconds to minutes.',
         'Read actual post-run records, not the old starting board. Retain T0/T1/missing/excluded rows in the audit.',
         'A source-keyed contract, exact source specs from their own commit and a printed LC volume estimate.',
         'Corrupt newest input must stop instead of silently falling back; follow-up exports cannot become their own inputs.'),
        ('Run and checkpoint T2', '05_run.py',
         'Rehydrate exact first-stage products by SHA-256, then run native pixel/neighbour vetting and event-null/injection tests; duration is archive/event dependent.',
         'Carry the original event/alias selection forward without T0/T1 rescreening or changing reviewed records.',
         'Per-target reports, sky records, raw vet/null outputs, product hashes, companion ledger and byte-checked checkpoints under Cygnus only.',
         'No fitted events or missing exact products must not produce a completed checkpoint. Failed/unavailable tests cannot become passed.'),
        ('Verified readout and export', '06_readout.py',
         'Read saved checkpoints, re-hash the export and audit it using the same metadata path as workstation sync; normally seconds to minutes.',
         'A completed loop or DONE flag is not evidence that all targets succeeded. Make every missing/failed target explicit.',
         'READOUT, SOURCE_AUDIT, LINEAGE, tier_board, done, MANIFEST.sha256 and LOCATION.json.',
         'Any byte mismatch must stop. Zero eligible targets is a valid accounted no-op; T3/T4 and evidence promotion remain unexecuted.')]
    revision_payload = b''.join((PARTS / section[1]).read_bytes().replace(b'\r\n', b'\n') for section in sections)
    revision = 't2-v1-' + hashlib.sha256(revision_payload).hexdigest()[:12]
    cells = [{'cell_type': 'markdown', 'id': 'intro', 'metadata': {}, 'source': (
        '# Cygnus — seamless higher-tier follow-up\n\n'
        f'**Build revision:** `{revision}`.\n\n'
        '**Reusable stage two.** Finish the first notebook and its export, then Run all here on a CPU runtime. '
        'The newest finalized first-stage packet is discovered automatically; name SOURCE_RUN to choose an older batch. '
        'Earned targets are derived again from manifest-verified records, never the starting board or a manual target list.\n\n'
        '**Scope:** T2 vetting, event-epoch empirical nulls and event-depth injection recovery. '
        'No T0/T1 rescreen, no spectra/RV/PRF placeholder presented as T3 execution, no T4 or evidence promotion. '
        'The old specialist leads remain excluded from routine reruns. Sources and reviewed records stay immutable.\n'
    ).splitlines(keepends=True)}]
    for number, (title, filename, tests, why, outputs, falsifier) in enumerate(sections, 1):
        payload = (PARTS / filename).read_bytes().decode('utf-8').replace('\r\n', '\n')
        payload = payload.replace('T2_WORKFLOW_REVISION', revision)
        compile(payload, filename, 'exec')
        definition = (f'### Cell {number} — {title}\n\n**What it tests:** {tests}\n\n'
                      f'**Why it exists:** {why}\n\n**What it writes:** {outputs}\n\n'
                      f'**How to read it:** States are workflow/test outcomes, not scientific confirmation.\n\n'
                      f'**How to falsify it:** {falsifier}\n')
        identifier = f'cell-{number}'
        cells.extend([
            {'cell_type': 'markdown', 'id': identifier + '-definition', 'metadata': {},
             'source': definition.splitlines(keepends=True)},
            {'cell_type': 'code', 'id': identifier, 'execution_count': None,
             'metadata': {'title': title}, 'outputs': [], 'source': payload.splitlines(keepends=True)}])
    titles = [c['metadata']['title'] for c in cells if c['cell_type'] == 'code']
    assert len(titles) == len(set(titles)) == len(sections)
    notebook = {'nbformat': 4, 'nbformat_minor': 5, 'cells': cells,
                'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
                             'language_info': {'name': 'python'},
                             'colab': {'name': OUTPUT.name, 'provenance': []}}}
    OUTPUT.write_bytes((json.dumps(notebook, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
    print(f'{OUTPUT.name}: {len(titles)} code cells; SHA256 {hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}')


if __name__ == '__main__':
    build()
