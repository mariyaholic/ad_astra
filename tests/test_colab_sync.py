"""Post-run tier marks follow manifest-verified records rather than the starting board."""
import json

import pytest

from cygnus import colab, colab_sync


def packet(tmp_path):
    source = tmp_path / 'packet'
    source.mkdir()
    board = {'run': 'test-run', 'commit': 'a' * 40, 'max_tier': 'T2',
             'board': {'one': {'earned': 'T0', 'run_at': 'T0'},
                       'missing': {'earned': 'T0', 'run_at': 'T0'}}}
    (source / 'tier_board.json').write_text(json.dumps(board))
    (source / 'done.json').write_text(json.dumps({'one': board['board']['one']}))
    d = source / 'campaigns' / 'one'
    d.mkdir(parents=True)
    rec = {'id': 'one', 'status': 'completed', 'outcome': 'lead', 'evidence': 'Unverified lead',
           'checks': [{'name': n, 'state': 'passed'} for n in (
               'Period aliases', 'Catalogue cross-match',
               'Event-time comparison vs published ephemerides',
               'Calibrated false-alarm threshold', 'Moving objects at screen-event epochs')]}
    (d / 'sky_record.json').write_text(json.dumps(rec))
    manifest = colab.build_manifest(source, ['tier_board.json', 'done.json', 'campaigns'])
    colab.write_manifest(source / 'MANIFEST.sha256', manifest)
    location = {'id': 'colab_runs/test-run', 'commit': board['commit'],
                'manifest_sha256': colab.sha256_file(source / 'MANIFEST.sha256')}
    (source / 'LOCATION.json').write_text(json.dumps(location))
    return source


def test_retiers_finished_record_and_retains_missing_target(tmp_path):
    result = colab_sync.audit(packet(tmp_path))
    assert result['counts'] == {'T2': 1, 'missing': 1}
    assert result['targets']['one']['tier'] == 'T2'
    assert result['targets']['one']['starting_tier'] == 'T0'
    assert result['targets']['one']['run_at'] == 'T0'
    assert result['targets']['missing']['tier'] == 'missing'
    assert result['verification']['scope'] == 'tier metadata and sky records only'


def test_corrupt_record_cannot_update_notes(tmp_path):
    source = packet(tmp_path)
    (source / 'campaigns/one/sky_record.json').write_text('{}')
    with pytest.raises(ValueError, match='checksum'):
        colab_sync.audit(source)


def test_manifest_traversal_is_rejected(tmp_path):
    source = packet(tmp_path)
    with (source / 'MANIFEST.sha256').open('a') as f:
        f.write('b' * 64 + '  ../outside.json\n')
    with pytest.raises(ValueError):
        colab_sync.audit(source)


def test_note_update_preserves_manual_text_and_is_idempotent(tmp_path):
    result = colab_sync.audit(packet(tmp_path))
    root = tmp_path / 'repo'
    (root / 'docs').mkdir(parents=True)
    status = root / 'docs/STATUS.md'
    status.write_text('# Status\n\nManual decisions remain here.\n')
    colab_sync.mark(result, root)
    first = status.read_bytes()
    colab_sync.mark(result, root)
    assert status.read_bytes() == first
    assert 'Manual decisions remain here.' in status.read_text()
    assert 'T2: 1' in status.read_text()
    assert (root / 'docs/colab_runs/test-run/TIER_MARKS.json').is_file()


def test_incomplete_lead_is_not_marked_t2(tmp_path):
    source = packet(tmp_path)
    path = source / 'campaigns/one/sky_record.json'
    rec = json.loads(path.read_text())
    rec['status'] = 'draft'
    path.write_text(json.dumps(rec))
    manifest = colab.build_manifest(source, ['tier_board.json', 'done.json', 'campaigns'])
    colab.write_manifest(source / 'MANIFEST.sha256', manifest)
    location = json.loads((source / 'LOCATION.json').read_text())
    location['manifest_sha256'] = colab.sha256_file(source / 'MANIFEST.sha256')
    (source / 'LOCATION.json').write_text(json.dumps(location))
    assert colab_sync.audit(source)['targets']['one']['tier'] == 'incomplete'


def test_checkpoint_refreshes_tier_without_relabeling_executed_tools(tmp_path):
    source = packet(tmp_path)
    snapshot = colab_sync.checkpoint_entry(source, 'one', run_at='T0')
    assert snapshot['earned'] == 'T2'
    assert snapshot['run_at'] == 'T0'
    assert snapshot['status'] == 'completed'


def test_notebook_refreshes_before_checkpoint_and_final_board():
    notebook = json.loads((colab_sync.WORKTREE / 'notebooks/cygnus_lead_colab.ipynb').read_text())
    code = '\n'.join(''.join(c['source']) for c in notebook['cells'] if c['cell_type'] == 'code')
    assert 'BOARD[cid] = checkpoint_entry(REPO_DIR, cid, run_at=BOARD[cid][\'run_at\'])' in code
    assert "BOARD.update(DONE)" in code


def test_mounted_fetch_selects_only_tier_inputs_and_reuses_cache(tmp_path, monkeypatch):
    from cygnus.storage import Route
    source = packet(tmp_path)
    mount = tmp_path / 'Cygnus'
    run = mount / 'colab_runs/test-run'
    run.parent.mkdir(parents=True)
    source.rename(run)
    (run / 'bulk.fits').write_bytes(b'large product stand-in')
    cache = tmp_path / 'cache'
    cache.mkdir()
    monkeypatch.setattr(colab_sync, 'scratch_dir', lambda _: cache)
    result = colab_sync.fetch('test-run', Route('path', str(mount), 'test'))
    assert colab_sync.audit(result)['counts'] == {'T2': 1, 'missing': 1}
    assert not (cache / 'bulk.fits').exists()
    record = cache / 'campaigns/one/sky_record.json'
    before = record.stat().st_mtime_ns
    colab_sync.fetch('test-run', Route('path', str(mount), 'test'))
    assert record.stat().st_mtime_ns == before


def test_daily_sync_discovers_tiered_exports_skips_legacy_and_unchanged(tmp_path, monkeypatch):
    from cygnus.storage import Route
    source = packet(tmp_path)
    # Give the synthetic packet the storage index fields required by validate().
    loc_path = source / 'LOCATION.json'
    loc = json.loads(loc_path.read_text())
    loc.update(schema='cygnus.storage_location/1', drive_path='Cygnus/colab_runs/test-run',
               kind='colab_run', writer='Colab drive.mount', producer='test',
               created_utc='2026-10-03T00:00:00Z', files=3, links={}, visible_via={})
    loc_path.write_text(json.dumps(loc))
    mount = tmp_path / 'Cygnus'
    run = mount / 'colab_runs/test-run'
    run.parent.mkdir(parents=True)
    source.rename(run)
    (run.parent / 'legacy-run').mkdir()
    (run.parent / '_probe_mount_visibility').mkdir()
    root = tmp_path / 'repo'
    cache = tmp_path / 'cache'
    cache.mkdir()
    monkeypatch.setattr(colab_sync, 'scratch_dir', lambda _: cache)
    route = Route('path', str(mount), 'test')
    first = colab_sync.sync_all(root, route)
    assert first['updated'] == ['test-run']
    assert first['skipped_legacy'] == ['_probe_mount_visibility', 'legacy-run']
    assert first['errors'] == {}
    assert (root / 'storage/locations.jsonl').is_file()
    second = colab_sync.sync_all(root, route)
    assert second['updated'] == []
    assert second['unchanged'] == ['test-run']


def test_scheduled_failure_is_logged_with_nonzero_exit(tmp_path, monkeypatch):
    def unavailable(*args, **kwargs):
        raise RuntimeError('Drive unavailable')
    monkeypatch.setattr(colab_sync, 'sync_all', unavailable)
    log = tmp_path / 'latest.json'
    assert colab_sync.main(['--all', '--update-notes', '--log', str(log)]) == 1
    assert json.loads(log.read_text())['errors']['sync'] == 'Drive unavailable'


def test_windows_child_process_launch_suppresses_console_creation(monkeypatch):
    import os
    import subprocess
    if os.name != 'nt':
        pytest.skip('Windows process creation policy')
    calls = []
    def capture(args, **kwargs):
        calls.append(kwargs)
        return subprocess.CompletedProcess(args, 0, stdout='', stderr='')
    monkeypatch.setattr(subprocess, 'run', capture)
    colab_sync._background_run(['rclone', 'listremotes'], capture_output=True, text=True)
    assert calls[0]['creationflags'] & subprocess.CREATE_NO_WINDOW
