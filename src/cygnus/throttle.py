"""A cross-process request throttle per archive host.

``cygnus.batch run --jobs N`` runs N campaigns as separate processes, and each queries the same
archives. Without coordination N jobs make N times the request rate of one. :func:`wait` spaces the
*starts* of requests to one host by at least ``min_interval_s`` across every process sharing the
scratch directory, using a lock file and a timestamp file per host (no daemon, no shared memory).

The interval defaults to ``$CYGNUS_RATE_S`` (seconds; ``0`` disables the throttle), else
:data:`DEFAULT_INTERVAL_S`. A lock older than :data:`STALE_LOCK_S` is taken over (its holder died).
"""

from __future__ import annotations

import os
import re
import time
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_INTERVAL_S = 0.5          # at most ~2 request starts per second per host, whatever --jobs is
STALE_LOCK_S = 30.0


def host_key(url_or_host: str) -> str:
    host = urlparse(url_or_host).hostname if "://" in url_or_host else url_or_host
    return re.sub(r"[^A-Za-z0-9.\-]", "_", (host or "unknown").lower())


def interval(env: dict | None = None) -> float:
    env = os.environ if env is None else env
    try:
        return max(0.0, float(env.get("CYGNUS_RATE_S", DEFAULT_INTERVAL_S)))
    except ValueError:
        return DEFAULT_INTERVAL_S


def _state_dir() -> Path:
    from .config import scratch_dir

    d = scratch_dir("ratelimit")
    d.mkdir(parents=True, exist_ok=True)
    return d


def _acquire(lock: Path, deadline: float) -> bool:
    while True:
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            return True
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > STALE_LOCK_S:
                    lock.unlink(missing_ok=True)
                    continue
            except FileNotFoundError:
                continue
            if time.time() > deadline:
                return False
            time.sleep(0.02)


def wait(url_or_host: str, min_interval_s: float | None = None, *, state_dir: Path | None = None,
         clock=time.time, sleep=time.sleep) -> float:
    """Block until a request to this host may start; returns the seconds waited."""
    gap = interval() if min_interval_s is None else min_interval_s
    if gap <= 0:
        return 0.0
    d = state_dir or _state_dir()
    key = host_key(url_or_host)
    lock, stamp = d / f"{key}.lock", d / f"{key}.last"
    if not _acquire(lock, time.time() + 60):
        return 0.0                       # never deadlock a campaign on the throttle itself
    try:
        try:
            last = float(stamp.read_text(encoding="ascii") or 0)
        except (FileNotFoundError, ValueError):
            last = 0.0
        waited = max(0.0, last + gap - clock())
        if waited:
            sleep(waited)
        stamp.write_text(repr(clock()), encoding="ascii")
        return waited
    finally:
        lock.unlink(missing_ok=True)
