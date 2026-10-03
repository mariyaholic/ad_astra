"""Verify saved Colab tier metadata and mark post-run tiers in repository notes."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys

from .colab import read_manifest, sha256_file
from .campaign.tiers import decide, unmapped_checks
from .config import WORKTREE, scratch_dir
from . import storage


def _background_run(args, **kwargs):
    """Keep rclone child processes windowless when launched by pythonw on Windows."""
    if os.name == 'nt':
        kwargs['creationflags'] = kwargs.get('creationflags', 0) | subprocess.CREATE_NO_WINDOW
    return subprocess.run(args, **kwargs)


def _safe_id(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', value) or value in ('.', '..'):
        raise ValueError(f'invalid run/target id: {value!r}')
    return value


def checkpoint_entry(root: Path, cid: str, *, run_at: str) -> dict:
    """Notebook checkpoint from the just-written record; retain actual executed tier."""
    cid = _safe_id(cid)
    directory = Path(root) / 'campaigns' / cid
    path = directory / 'sky_record.json'
    rec = json.loads(path.read_text(encoding='utf-8'))
    d = decide(rec, spec={}, rejection_note=(directory / 'REJECTION.md').is_file())
    return {'earned': d.tier, 'run_at': run_at, 'record_exists': True,
            'status': rec.get('status'), 'decision': d.as_dict()}


def _manifest(source):
    entries = read_manifest(source / 'MANIFEST.sha256')
    for rel in entries:
        p = PurePosixPath(rel)
        if p.is_absolute() or '..' in p.parts or '\\' in rel or ':' in rel:
            raise ValueError(f'unsafe manifest path: {rel}')
    loc = json.loads((source / 'LOCATION.json').read_text(encoding='utf-8'))
    if sha256_file(source / 'MANIFEST.sha256') != loc['manifest_sha256']:
        raise ValueError('manifest checksum differs from LOCATION.json')
    return entries, loc


def audit(source: Path) -> dict:
    """Recompute tiers from hash-verified records; retain missing/incomplete targets explicitly.

    This verifies only metadata used for tiering, not all products or the scientific interpretation.
    LOCATION is the source's integrity assertion, not an independently signed identity certificate.
    No campaign record, measurement, evidence level or companion ledger is modified.
    """
    source = Path(source)
    entries, loc = _manifest(source)
    verified = {}

    def read(rel):
        if rel not in entries or not (source / rel).is_file():
            raise ValueError(f'missing manifest-listed tier input: {rel}')
        actual = sha256_file(source / rel)
        if actual != entries[rel]:
            raise ValueError(f'checksum mismatch: {rel}')
        verified[rel] = actual
        return json.loads((source / rel).read_text(encoding='utf-8'))

    board = read('tier_board.json')
    done = read('done.json')
    run = _safe_id(board['run'])
    if loc['id'] != f'colab_runs/{run}' or loc['commit'] != board['commit']:
        raise ValueError('run/commit identity differs between LOCATION and board')
    rows = {}
    for cid, initial in sorted(board['board'].items()):
        _safe_id(cid)
        rel = f'campaigns/{cid}/sky_record.json'
        row = {'starting_tier': initial.get('earned'),
               'run_at': done.get(cid, {}).get('run_at'), 'checkpointed': cid in done,
               'source_record': rel, 'tier': 'missing', 'blockers': ['no shipped sky record']}
        if rel in entries:
            rec = read(rel)
            if rec.get('id') != cid:
                raise ValueError(f'record identity differs for {cid}')
            unknown = unmapped_checks([rec])
            if unknown:
                raise ValueError(f'unmapped gate checks for {cid}: {sorted(unknown)}')
            rejection = f'campaigns/{cid}/REJECTION.md'
            rejected = rejection in entries
            if rejected:
                if not (source / rejection).is_file() or sha256_file(source / rejection) != entries[rejection]:
                    raise ValueError(f'checksum mismatch or missing rejection: {cid}')
                verified[rejection] = entries[rejection]
            # A missing budget is never permission to claim heavy-tier eligibility.
            d = decide(rec, spec={}, rejection_note=rejected)
            tier = d.tier if rec.get('status') == 'completed' or d.tier == 'closed' else 'incomplete'
            row.update(tier=tier, status=rec.get('status'), outcome=rec.get('outcome'),
                       evidence=rec.get('evidence'), blockers=d.blockers, decision=d.as_dict(),
                       record_sha256=entries[rel])
        rows[cid] = row
    return {'schema': 'cygnus.colab_tier_audit/1', 'run': run, 'commit': board['commit'],
            'source_utc': board.get('utc'), 'location': loc['id'],
            'source_link': loc.get('links', {}).get('folder'),
            'counts': dict(sorted(Counter(r['tier'] for r in rows.values()).items())),
            'requested': len(rows), 'checkpointed': len(done), 'targets': rows,
            'verification': {'scope': 'tier metadata and sky records only',
                             'manifest_sha256': loc['manifest_sha256'], 'verified_files': verified,
                             'manifest_files': len(entries),
                             'unverified_files': len(entries) - len(verified)}}


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding='utf-8') == text:
        return
    tmp = path.with_name(path.name + '.writing')
    tmp.write_text(text, encoding='utf-8', newline='\n')
    tmp.replace(path)


def mark(result: dict, root: Path) -> None:
    """Write separate tier marks and replace only a run-specific managed STATUS block."""
    run = _safe_id(result['run'])
    root = Path(root)
    out = root / 'docs/colab_runs' / run
    _write(out / 'TIER_MARKS.json', json.dumps(result, indent=2, sort_keys=True) + '\n')
    counts = ', '.join(f'{k}: {v}' for k, v in result['counts'].items())
    lines = [f'# Colab tier audit: {run}', '',
             f"Source commit: `{result['commit']}`; source UTC: {result.get('source_utc') or 'not recorded'}.", '',
             f"Requested: {result['requested']}; checkpointed: {result['checkpointed']}. **{counts}**.", '',
             'Tier means tools earned from the saved checks, not scientific confirmation or tools already executed.',
             'This is a gate audit; draft review markers and evidence levels remain unchanged.', '',
             f"Verified {len(result['verification']['verified_files'])}/{result['verification']['manifest_files']} manifest files (tier inputs only).",
             'Bulk products, light curves and the companion ledger were not verified or imported.', '',
             '| Target | Tier earned | Starting tier | Run at | Outcome | Next-tier blockers |',
             '| --- | --- | --- | --- | --- | --- |']
    for cid, row in result['targets'].items():
        blockers = '; '.join(row['blockers']).replace('|', '/')
        lines.append(f"| {cid} | **{row['tier']}** | {row['starting_tier']} | {row['run_at'] or 'not checkpointed'} | {row.get('outcome', 'not shipped')} | {blockers} |")
    _write(out / 'TIER_MARKS.md', '\n'.join(lines) + '\n')
    status = root / 'docs/STATUS.md'
    old = status.read_text(encoding='utf-8') if status.exists() else '# Project status\n'
    start, end = f'<!-- cygnus:colab-sync:{run}:start -->', f'<!-- cygnus:colab-sync:{run}:end -->'
    block = f'{start}\n\n**Colab sync {run}:** {counts}; {result["checkpointed"]}/{result["requested"]} checkpointed. '
    block += 'Post-run tiers derived from manifest-verified sky records; saved starting board is historical. '
    block += 'Bulk products and scientific interpretations remain unreviewed. '
    block += f'[Tier marks](colab_runs/{run}/TIER_MARKS.md).\n\n{end}'
    if start in old:
        if end not in old:
            raise ValueError('unterminated managed STATUS block')
        a, b = old.index(start), old.index(end) + len(end)
        new = old[:a] + block + old[b:]
    else:
        first, sep, rest = old.partition('\n')
        new = first + '\n\n' + block + '\n' + sep + rest
    _write(status, new)


def fetch(run: str, route: storage.Route | None = None) -> Path:
    """Read only bounded tier inputs under Cygnus; reuse matching cached files."""
    run = _safe_id(run)
    route = route or storage.require_route(run=_background_run)
    rel = f'colab_runs/{run}'
    dest = scratch_dir(f'colab_audit/{run}')

    def copy(names):
        if route.kind == 'path':
            base = Path(route.join(rel))
            for name in names:
                target = dest / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(base / name, target)
        else:
            selection = dest.parent / f'{run}.selection.txt'
            selection.write_text('\n'.join(names) + '\n', encoding='utf-8')
            p = _background_run(['rclone', 'copy', route.join(rel), str(dest),
                                '--files-from-raw', str(selection), '--no-traverse',
                                '--ignore-times', '--transfers', '3', '--checkers', '3',
                                '--timeout', '60s', '--retries', '1'],
                               capture_output=True, text=True, timeout=600)
            if p.returncode:
                raise storage.StorageError('rclone tier-input retrieval failed: ' + p.stderr[-1000:])

    copy(['LOCATION.json', 'MANIFEST.sha256'])
    entries, _ = _manifest(dest)
    selected = [name for name in entries if name in ('tier_board.json', 'done.json') or
                re.fullmatch(r'campaigns/[A-Za-z0-9._-]+/(sky_record.json|REJECTION.md)', name)]
    needed = [name for name in selected if not (dest / name).is_file() or sha256_file(dest / name) != entries[name]]
    if needed:
        copy(needed)
    return dest


def _children(route, rel):
    if route.kind == 'path':
        return [{'Name': p.name, 'IsDir': p.is_dir()} for p in Path(route.join(rel)).iterdir()]
    p = storage._rclone(['lsjson', route.join(rel), '--max-depth', '1'], _background_run, timeout=120)
    if p.returncode:
        raise storage.StorageError('Drive listing failed: ' + p.stderr[-1000:])
    return json.loads(p.stdout)


def _location(route, rel):
    if route.kind == 'path':
        return json.loads(Path(route.join(rel)).read_text(encoding='utf-8'))
    p = storage._rclone(['cat', route.join(rel)], _background_run, timeout=120)
    if p.returncode:
        raise storage.StorageError('Drive location read failed: ' + p.stderr[-1000:])
    return json.loads(p.stdout)


def sync_all(root: Path, route: storage.Route | None = None) -> dict:
    """Discover tiered exports, skip unchanged hashes, and update notes for verified packets."""
    root = Path(root)
    route = route or storage.require_route(run=_background_run)
    summary = {'updated': [], 'unchanged': [], 'skipped_legacy': [], 'errors': {}}
    folders = [r['Name'] for r in _children(route, 'colab_runs') if r['IsDir']]
    if len(folders) != len(set(folders)):
        raise ValueError('duplicate Drive folder names; resolve identity before syncing')
    for run in sorted(folders):
        try:
            rel = f'colab_runs/{run}'
            names = {r['Name'] for r in _children(route, rel) if not r['IsDir']}
            if 'tier_board.json' not in names:
                summary['skipped_legacy'].append(run)
                continue
            _safe_id(run)
            if not {'LOCATION.json', 'MANIFEST.sha256', 'done.json'} <= names:
                raise ValueError('incomplete tiered export: required metadata not shipped')
            loc = storage.validate(_location(route, rel + '/LOCATION.json'))
            if loc['id'] != rel:
                raise ValueError('folder/LOCATION identity mismatch')
            marks = root / 'docs/colab_runs' / run / 'TIER_MARKS.json'
            if marks.is_file():
                previous = json.loads(marks.read_text(encoding='utf-8'))
                if (previous.get('commit') == loc.get('commit') and
                        previous.get('verification', {}).get('manifest_sha256') == loc.get('manifest_sha256')):
                    summary['unchanged'].append(run)
                    continue
            source = fetch(run, route)
            result = audit(source)
            if result['run'] != run:
                raise ValueError('folder/board identity mismatch')
            verified_loc = storage.validate(json.loads((source / 'LOCATION.json').read_text(encoding='utf-8')))
            # Validate the location before changing any repo notes.
            mark(result, root)
            storage.upsert(verified_loc, root / 'storage/locations.jsonl')
            storage.record_visibility(rel, route.label, True, root / 'storage/locations.jsonl',
                                      note='tier metadata and sky records verified; bulk products not checked')
            summary['updated'].append(run)
        except Exception as exc:
            summary['errors'][run] = str(exc)
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--run', help='folder name under Cygnus/colab_runs')
    selection.add_argument('--all', action='store_true', help='discover tiered exports; skip unchanged manifests')
    parser.add_argument('--local', type=Path, help='audit an already retrieved packet without network')
    parser.add_argument('--root', type=Path, default=WORKTREE)
    parser.add_argument('--update-notes', action='store_true')
    parser.add_argument('--log', type=Path, help='write scheduler result JSON (including failures)')
    args = parser.parse_args(argv)
    if args.all:
        if not args.update_notes or args.local:
            parser.error('--all requires --update-notes and does not accept --local')
        started = storage.utc_now()
        try:
            summary = sync_all(args.root)
        except Exception as exc:
            summary = {'updated': [], 'unchanged': [], 'skipped_legacy': [], 'errors': {'sync': str(exc)}}
        summary.update(started_utc=started, finished_utc=storage.utc_now())
        summary['exit_code'] = 1 if summary['errors'] else 0
        text = json.dumps(summary, indent=2) + '\n'
        if args.log:
            _write(args.log, text)
        if sys.stdout is not None:
            print(text, end='')
        return summary['exit_code']
    result = audit(args.local or fetch(args.run))
    if result['run'] != args.run:
        raise ValueError('requested run differs from source board')
    if args.update_notes:
        mark(result, args.root)
    summary = {k: result[k] for k in ('run', 'counts', 'requested', 'checkpointed')}
    summary['verified_files'] = len(result['verification']['verified_files'])
    summary['manifest_files'] = result['verification']['manifest_files']
    summary['verification_scope'] = result['verification']['scope']
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
