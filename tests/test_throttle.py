"""cygnus.throttle: request starts per host are spaced across processes (offline)."""

from __future__ import annotations

import os
import time

from cygnus import throttle as T


class _Clock:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t

    def sleep(self, s):
        self.t += s


def test_host_keys_are_filename_safe():
    assert T.host_key("https://mast.stsci.edu/api/v0/invoke?x=1") == "mast.stsci.edu"
    assert T.host_key("ssp.imcce.fr") == "ssp.imcce.fr"
    assert T.host_key("https://[::1]:8080/") == "__1"


def test_requests_to_one_host_are_spaced_and_other_hosts_are_not(tmp_path):
    c = _Clock()
    kw = dict(state_dir=tmp_path, clock=c, sleep=c.sleep)
    assert T.wait("https://a.org/x", 0.5, **kw) == 0.0
    assert T.wait("https://a.org/y", 0.5, **kw) == 0.5
    assert T.wait("https://b.org/y", 0.5, **kw) == 0.0
    c.t += 2
    assert T.wait("https://a.org/z", 0.5, **kw) == 0.0
    assert not list(tmp_path.glob("*.lock"))


def test_zero_interval_disables_and_env_sets_it(tmp_path):
    assert T.wait("a.org", 0, state_dir=tmp_path) == 0.0 and not list(tmp_path.iterdir())
    assert T.interval({"CYGNUS_RATE_S": "0"}) == 0.0 and T.interval({"CYGNUS_RATE_S": "bad"}) == T.DEFAULT_INTERVAL_S
    assert T.interval({}) == T.DEFAULT_INTERVAL_S


def test_a_stale_lock_from_a_dead_process_is_taken_over(tmp_path):
    lock = tmp_path / "a.org.lock"
    lock.write_text("99999")
    old = time.time() - T.STALE_LOCK_S - 5
    os.utime(lock, (old, old))
    c = _Clock()
    assert T.wait("a.org", 0.5, state_dir=tmp_path, clock=c, sleep=c.sleep) == 0.0
    assert not lock.exists()
