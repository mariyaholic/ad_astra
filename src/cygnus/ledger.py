"""Provenance ledger: SQLite-backed record of products, runs, measurements.

Mechanically enforces AGENTS.md rules 4/5 ('verifiable telemetry only',
'distinguish measurement from inference'):

* every downloaded product is registered with archive, product ID, retrieval
  timestamp and checksum;
* every measurement references a logged run (script, code version, config
  hash, seed) and may reference the products it was computed from;
* every candidate carries an evidence level; the Known-Object Gate writes its
  results into ``prior_art`` so dossiers can cite them.

Conventions: timestamps are ISO-8601 UTC strings (``YYYY-MM-DDTHH:MM:SSZ``);
numeric values are stored as text with explicit units to avoid silent
coercion; ``candidate_id`` is always a working ``CYG-*`` identifier.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .config import ledger_path as _default_ledger_path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    archive TEXT NOT NULL,
    product_id TEXT NOT NULL,
    url TEXT,
    local_path TEXT,
    checksum TEXT,
    license TEXT,
    retrieved_utc TEXT NOT NULL,
    last_seen_utc TEXT NOT NULL,
    extra_json TEXT,
    UNIQUE (archive, product_id)
);
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY,
    script TEXT NOT NULL,
    config_hash TEXT,
    code_version TEXT,
    seed INTEGER,
    started_utc TEXT NOT NULL,
    finished_utc TEXT,
    status TEXT NOT NULL DEFAULT 'open',
    summary TEXT
);
CREATE TABLE IF NOT EXISTS measurements (
    id INTEGER PRIMARY KEY,
    run_id INTEGER NOT NULL,
    candidate_id TEXT,
    product_ids_json TEXT NOT NULL DEFAULT '[]',
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    unit TEXT,
    uncertainty TEXT,
    method TEXT,
    notes TEXT,
    created_utc TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY,
    candidate_id TEXT NOT NULL UNIQUE,
    evidence_level TEXT NOT NULL,
    summary TEXT,
    coordinates TEXT,
    created_utc TEXT NOT NULL,
    updated_utc TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS prior_art (
    id INTEGER PRIMARY KEY,
    candidate_id TEXT NOT NULL DEFAULT '',
    gate TEXT NOT NULL,
    service TEXT NOT NULL,
    query TEXT NOT NULL DEFAULT '',
    retrieved_utc TEXT NOT NULL,
    result TEXT NOT NULL,
    UNIQUE (candidate_id, service, query)
);
CREATE INDEX IF NOT EXISTS idx_pa_candidate ON prior_art (candidate_id);
"""


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def file_sha256(path: str | Path) -> str:
    """Streaming SHA-256 of a (potentially multi-GB) file."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _pkg_version() -> str:
    try:
        from importlib.metadata import version

        return "cygnus-" + version("cygnus")
    except Exception:
        return "cygnus-0.1.0+source"


@dataclass
class RunHandle:
    """Mutable handle for a run opened by :meth:`Ledger.recorded_run`."""

    id: int
    status: str = "completed"
    summary: str | None = None


class Ledger:
    """Provenance database. Pass ``:memory:`` for ephemeral test instances."""

    def __init__(self, path: str | Path | None = None, code_version: str | None = None):
        if path is None:
            path = _default_ledger_path()
        self._path = str(path)
        self.db = sqlite3.connect(self._path if self._path != ":memory:" else ":memory:", timeout=60)
        self.db.row_factory = sqlite3.Row
        self.code_version = code_version or _pkg_version()
        self.db.executescript(_SCHEMA)
        self.db.commit()

    @classmethod
    def open_readonly(cls, path: str | Path) -> "Ledger":
        """Open an existing ledger without creating or migrating anything.

        Used by the publication layer (``cygnus.publish``): the SQLite URI
        ``mode=ro`` makes any write raise, so exporting can never alter
        provenance. A missing file raises instead of creating an empty DB.
        """
        path = Path(path)
        if not path.is_file():
            raise FileNotFoundError(f"ledger not found: {path}")
        self = cls.__new__(cls)
        self._path = str(path)
        self.db = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True)
        self.db.row_factory = sqlite3.Row
        self.code_version = _pkg_version()
        return self

    def runs(self, script: str | None = None) -> list[dict[str, Any]]:
        if script is None:
            rows = self.db.execute("SELECT * FROM runs ORDER BY id")
        else:
            rows = self.db.execute("SELECT * FROM runs WHERE script=? ORDER BY id", (script,))
        return [dict(r) for r in rows.fetchall()]

    def measurements_for_run(self, run_id: int) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT * FROM measurements WHERE run_id=? ORDER BY id", (int(run_id),)
        )
        return [dict(r) for r in rows.fetchall()]

    def close(self) -> None:
        self.db.close()

    # ---------------------------------------------------------------- products
    def add_product(
        self,
        archive: str,
        product_id: str,
        *,
        url: str | None = None,
        local_path: str | Path | None = None,
        checksum: str | None = None,
        license_: str | None = None,
        extra: dict[str, Any] | None = None,
    ) -> int:
        """Register (or re-confirm) one archive product; idempotent on IDs."""
        ts = now_utc()
        self.db.execute(
            """
            INSERT INTO products
                (archive, product_id, url, local_path, checksum, license,
                 retrieved_utc, last_seen_utc, extra_json)
            VALUES (?,?,?,?,?,?,?,?,?)
            ON CONFLICT(archive, product_id) DO UPDATE SET
                url = COALESCE(excluded.url, url),
                local_path = COALESCE(excluded.local_path, local_path),
                checksum = COALESCE(excluded.checksum, checksum),
                license = COALESCE(excluded.license, license),
                last_seen_utc = excluded.last_seen_utc,
                extra_json = excluded.extra_json
            """,
            (
                archive,
                product_id,
                url,
                str(local_path) if local_path is not None else None,
                checksum,
                license_,
                ts,
                ts,
                json.dumps(extra or {}, sort_keys=True),
            ),
        )
        self.db.commit()
        row = self.db.execute(
            "SELECT id FROM products WHERE archive=? AND product_id=?",
            (archive, product_id),
        ).fetchone()
        return int(row["id"])

    def products(self, archive: str | None = None) -> list[dict[str, Any]]:
        if archive is None:
            rows = self.db.execute("SELECT * FROM products ORDER BY archive, product_id")
        else:
            rows = self.db.execute(
                "SELECT * FROM products WHERE archive=? ORDER BY product_id", (archive,)
            )
        return [dict(r) for r in rows.fetchall()]

    def count_products(self, archive: str | None = None) -> int:
        if archive is None:
            (n,) = self.db.execute("SELECT COUNT(*) FROM products").fetchone()
        else:
            (n,) = self.db.execute(
                "SELECT COUNT(*) FROM products WHERE archive=?", (archive,)
            ).fetchone()
        return int(n)

    # -------------------------------------------------------------------- runs
    def log_run(self, script: str, *, config_hash: str | None = None, seed: int | None = None) -> int:
        cur = self.db.execute(
            "INSERT INTO runs (script, config_hash, code_version, seed, started_utc)"
            " VALUES (?,?,?,?,?)",
            (script, config_hash, self.code_version, seed, now_utc()),
        )
        self.db.commit()
        return int(cur.lastrowid)

    def close_run(self, run_id: int, status: str, summary: str | None = None) -> None:
        if status not in ("completed", "failed", "aborted"):
            raise ValueError(f"run status must be completed|failed|aborted, got {status!r}")
        row = self.db.execute("SELECT status FROM runs WHERE id=?", (run_id,)).fetchone()
        if row is None:
            raise KeyError(f"no run id={run_id}")
        if row["status"] != "open":
            raise ValueError(f"run id={run_id} is already {row['status']!r}; refusing to overwrite its outcome")
        self.db.execute(
            "UPDATE runs SET status=?, finished_utc=?, summary=COALESCE(?, summary) WHERE id=?",
            (status, now_utc(), summary, run_id),
        )
        self.db.commit()

    def run(self, run_id: int) -> dict[str, Any]:
        row = self.db.execute("SELECT * FROM runs WHERE id=?", (run_id,)).fetchone()
        if row is None:
            raise KeyError(f"no run id={run_id}")
        return dict(row)

    @contextmanager
    def recorded_run(self, script: str, *, config_hash: str | None = None, seed: int | None = None):
        """Open a run and guarantee it is closed: ``completed`` on success, ``failed`` on an
        exception, ``aborted`` on interrupt. Yields a :class:`RunHandle`; set ``handle.summary``
        (and optionally ``handle.status``) inside the block.

        This is what keeps the ledger from accumulating runs stuck at ``open``.
        """
        handle = RunHandle(self.log_run(script, config_hash=config_hash, seed=seed))
        try:
            yield handle
        except KeyboardInterrupt:
            self.close_run(handle.id, "aborted", handle.summary or "interrupted (KeyboardInterrupt)")
            raise
        except BaseException as exc:
            self.close_run(handle.id, "failed", f"{type(exc).__name__}: {str(exc)[:500]}")
            raise
        else:
            self.close_run(handle.id, handle.status, handle.summary)

    def completed_run(self, script: str, config_hash: str) -> dict[str, Any] | None:
        """Most recent completed run of ``script`` with this config hash (for idempotent steps)."""
        row = self.db.execute(
            "SELECT * FROM runs WHERE script=? AND config_hash=? AND status='completed' ORDER BY id DESC LIMIT 1",
            (script, config_hash),
        ).fetchone()
        return dict(row) if row else None

    def close_stale_runs(self, *, started_before_utc: str, note: str) -> list[int]:
        """Mark runs still ``open`` that started before a cutoff as ``aborted``, with an explanatory note.

        For repairing runs whose process died without closing them; it records that the outcome is
        unknown rather than guessing completed or failed. Returns the affected run ids.
        """
        ids = [int(r["id"]) for r in self.db.execute(
            "SELECT id FROM runs WHERE status='open' AND started_utc < ? ORDER BY id", (started_before_utc,))]
        for i in ids:
            self.close_run(i, "aborted", f"closed retrospectively {now_utc()}: {note}")
        return ids

    # ------------------------------------------------------------- measurements
    def add_measurement(
        self,
        run_id: int,
        name: str,
        value: Any,
        *,
        unit: str | None = None,
        uncertainty: str | None = None,
        method: str | None = None,
        notes: str | None = None,
        candidate_id: str | None = None,
        product_ids: Iterable[str] = (),
    ) -> int:
        """Insert a measurement for an existing run.

        ``product_ids`` are free-form references, deliberately not enforced against the
        products table: the publication layer surfaces an unresolved reference as
        "unresolved" rather than hiding it. The run must exist.
        """
        if isinstance(value, (dict, list)):
            value = json.dumps(value, sort_keys=True)
        if self.db.execute("SELECT 1 FROM runs WHERE id=?", (int(run_id),)).fetchone() is None:
            raise KeyError(f"no run id={run_id}; log the run before its measurements")
        cur = self.db.execute(
            "INSERT INTO measurements"
            " (run_id, candidate_id, product_ids_json, name, value, unit,"
            "  uncertainty, method, notes, created_utc)"
            " VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                int(run_id),
                candidate_id or "",
                json.dumps(list(product_ids)),
                name,
                str(value),
                unit,
                uncertainty,
                method,
                notes,
                now_utc(),
            ),
        )
        self.db.commit()
        return int(cur.lastrowid)

    def measurements_for_candidate(self, candidate_id: str) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT m.*, r.script FROM measurements m LEFT JOIN runs r ON r.id=m.run_id"
            " WHERE m.candidate_id=? ORDER BY m.id",
            (candidate_id,),
        )
        return [dict(r) for r in rows.fetchall()]

    # --------------------------------------------------------------- candidates
    def add_candidate(
        self,
        candidate_id: str,
        *,
        evidence_level: str = "unverified_lead",
        summary: str | None = None,
        coordinates: str | None = None,
    ) -> int:
        self.db.execute(
            "INSERT INTO candidates (candidate_id, evidence_level, summary, coordinates,"
            " created_utc, updated_utc)"
            " VALUES (?,?,?,?,?,?)"
            " ON CONFLICT(candidate_id) DO UPDATE SET"
            "   evidence_level=excluded.evidence_level,"
            "   summary=COALESCE(excluded.summary, summary),"
            "   coordinates=COALESCE(excluded.coordinates, coordinates),"
            "   updated_utc=excluded.updated_utc",
            (candidate_id, evidence_level, summary, coordinates, now_utc(), now_utc()),
        )
        self.db.commit()
        row = self.db.execute(
            "SELECT id FROM candidates WHERE candidate_id=?", (candidate_id,)
        ).fetchone()
        return int(row["id"])

    def get_candidate(self, candidate_id: str) -> dict[str, Any] | None:
        row = self.db.execute(
            "SELECT * FROM candidates WHERE candidate_id=?", (candidate_id,)
        ).fetchone()
        return dict(row) if row else None

    def set_candidate(
        self,
        candidate_id: str,
        *,
        evidence_level: str | None = None,
        summary: str | None = None,
        coordinates: str | None = None,
    ) -> None:
        self.db.execute(
            "UPDATE candidates SET"
            " evidence_level=COALESCE(?, evidence_level),"
            " summary=COALESCE(?, summary),"
            " coordinates=COALESCE(?, coordinates),"
            " updated_utc=?"
            " WHERE candidate_id=?",
            (evidence_level, summary, coordinates, now_utc(), candidate_id),
        )
        self.db.commit()

    def candidates(self) -> list[dict[str, Any]]:
        rows = self.db.execute("SELECT * FROM candidates ORDER BY candidate_id")
        return [dict(r) for r in rows.fetchall()]

    # ---------------------------------------------------------------- prior art
    def add_prior_art(
        self,
        service: str,
        result: str,
        *,
        gate: str = "catalog",
        query: str | None = None,
        candidate_id: str | None = None,
        retrieved_utc: str | None = None,
    ) -> int:
        service = service.strip()
        result = result.strip()
        query = (query or "").strip()
        cid = candidate_id or ""
        ts = retrieved_utc or now_utc()
        if not service or not result:
            raise ValueError("prior-art entries require non-empty service and result")
        self.db.execute(
            "INSERT INTO prior_art (candidate_id, gate, service, query, retrieved_utc, result)"
            " VALUES (?,?,?,?,?,?)"
            " ON CONFLICT(candidate_id, service, query) DO UPDATE SET"
            "   gate=excluded.gate, result=excluded.result,"
            "   retrieved_utc=excluded.retrieved_utc",
            (cid, gate, service, query, ts, result),
        )
        self.db.commit()
        row = self.db.execute(
            "SELECT id FROM prior_art WHERE candidate_id=? AND service=? AND query=?",
            (cid, service, query),
        ).fetchone()
        return int(row["id"])

    def prior_art_for(self, candidate_id: str) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT * FROM prior_art WHERE candidate_id=? ORDER BY service",
            (candidate_id or "",),
        )
        return [dict(r) for r in rows.fetchall()]

    # ------------------------------------------------------------- retention
    def mark_product_drive_only(self, archive: str, product_id: str, *,
                                extra: dict[str, Any] | None = None) -> None:
        """Retention helper: clear the local path (Drive hosts the file).

        Used by the pack's retire step after a verified upload; unlike
        ``add_product`` the local path is set to NULL rather than kept.
        """
        sets = ["local_path = NULL"]
        params: list[Any] = []
        if extra is not None:
            sets.append("extra_json = ?")
            params.append(json.dumps(extra, sort_keys=True))
        params.extend([archive, product_id])
        self.db.execute(
            f"UPDATE products SET {', '.join(sets)} WHERE archive=? AND product_id=?",
            params,
        )
        self.db.commit()
