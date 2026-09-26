"""Transport, checksum and leaf-comparison helpers for a Cygnus batch run on a Google Colab runtime.

``notebooks/cygnus_batch_colab.ipynb`` does the Colab-specific work (CPU check, ``drive.mount()``,
cloning the pinned commit, driving ``python -m cygnus.batch``). Everything that is ordinary Python
lives here, so it can be exercised offline without Colab, Drive or the network:

* ``sha256_file``, ``build_manifest``, ``write_manifest``, ``read_manifest``, ``verify_manifest``:
  a ``MANIFEST.sha256`` over every file a runtime sends back, and an explicit list of problems when
  a local copy does not reproduce it (each problem is a string; an empty list is the only pass).
* ``committed_files``: the files under given paths that ``git add`` would take — tracked files plus
  untracked files ``.gitignore`` does not exclude. That is what keeps a file list honest: no caller
  hand-writes one, so ``*.fits``, ``state/``, ``scratch/`` and the generated
  ``campaigns/*/tic*/sector*/normalized_series.csv`` cannot be swept into an upload by accident —
  ``.gitignore`` itself decides, and the selection cannot drift away from it.
* ``extract_git_archive``: the pinned, read-only baseline of committed campaign outputs, taken from
  git *before* a run so the run cannot overwrite what it is compared against.
* ``compare_campaigns`` and ``render_report``: a leaf-by-leaf comparison of that baseline with a
  Colab run's outputs in which every differing leaf is classified as *bookkeeping* or *science*.

What this module deliberately does **not** do: it never mounts Drive, never calls rclone, never
touches the network, the ledger or Colab, writes only files it is explicitly asked to write, and
decides no science policy. A difference is reported for a human to explain or fix; nothing is
"close enough". Bookkeeping differences are listed rather than hidden — they include checksums,
configuration hashes and run-state flags, which are excluded from the *science* list precisely
because they move with bookkeeping state, and therefore still have to be read.
"""

from __future__ import annotations

import fnmatch
import hashlib
import io
import json
import math
import re
import shutil
import subprocess
import tarfile
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

MANIFEST_NAME = "MANIFEST.sha256"
_BLOCK = 1 << 20
_MISSING = "<absent>"

# --------------------------------------------------------------------------- checksums and manifests
def sha256_file(path: str | Path) -> str:
    """SHA-256 of one file, read in 1 MiB blocks (no size limit and no memory spike)."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for block in iter(lambda: fh.read(_BLOCK), b""):
            digest.update(block)
    return digest.hexdigest()


def _rel_files(root: Path, paths: Iterable[str | Path], suffixes: Iterable[str] | None) -> list[str]:
    """Sorted relative POSIX paths of every regular file under ``paths``; a file is itself, a
    directory is walked recursively. Relative paths (not absolute ones) keep a manifest portable
    between the Colab VM and the workstation. Raises FileNotFoundError for a path that is neither."""
    wanted = tuple(suffixes) if suffixes else None
    found: set[str] = set()
    for entry in paths:
        target = Path(root) / entry
        if target.is_dir():
            candidates: Iterable[Path] = (c for c in target.rglob("*") if c.is_file())
        elif target.is_file() or target.is_symlink():
            candidates = [target]
        else:
            raise FileNotFoundError(f"nothing to include at {entry!r} under {Path(root).as_posix()}")
        for candidate in candidates:
            rel = candidate.relative_to(root).as_posix()
            if wanted is None or rel.endswith(wanted):
                found.add(rel)
    return sorted(found)


def build_manifest(root: str | Path, paths: Iterable[str | Path],
                   suffixes: Iterable[str] | None = None) -> dict[str, str]:
    """``{relative POSIX path: SHA-256}`` for every file under ``paths``, relative to ``root``.

    Directory entries are walked recursively; the result is sorted by path, so two runs over the
    same bytes produce byte-identical manifests."""
    return {rel: sha256_file(Path(root) / rel) for rel in _rel_files(Path(root), paths, suffixes)}


def write_manifest(path: str | Path, manifest: Mapping[str, str], *, comment: str | None = None) -> Path:
    """Write a ``sha256sum``-compatible manifest: ``<sha256>  <relative path>`` lines, LF endings.

    ``comment`` (optional) is written as leading ``#`` lines; a manifest without provenance of what
    it covers is not worth shipping, so callers should use it."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {line}" for line in comment.splitlines()] if comment else []
    lines += [f"{digest}  {rel}" for rel, digest in sorted(manifest.items())]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def read_manifest(path: str | Path) -> dict[str, str]:
    """Parse a manifest written by ``write_manifest`` (or by ``sha256sum``); ``#`` lines are notes.

    Raises ValueError naming the offending line for anything that is not
    ``<64 hex digits>  <path>``, or that repeats a path: a manifest that cannot be parsed exactly is
    not evidence."""
    entries: dict[str, str] = {}
    for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split(None, 1)
        digest = parts[0].strip().lower() if parts else ""
        if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"{Path(path).as_posix()}:{number}: not a '<sha256>  <path>' line: {line[:120]!r}")
        rel = parts[1].strip().lstrip("*")
        if not rel:
            raise ValueError(f"{Path(path).as_posix()}:{number}: empty path")
        if rel in entries:
            raise ValueError(f"{Path(path).as_posix()}:{number}: duplicate entry for {rel}")
        entries[rel] = digest
    return entries


def verify_manifest(manifest: str | Path | Mapping[str, str], root: str | Path, *,
                    ignore_extra: Iterable[str] = ()) -> list[str]:
    """Every problem that stops this copy being the uploaded one, as explicit strings.

    Checks that (1) each listed file exists, (2) its SHA-256 equals the recorded one, and (3) no
    file under ``root`` is missing from the manifest — a manifest that silently omits a file cannot
    be trusted to cover the upload. A ``MANIFEST*`` file at the root of ``root`` is never "extra",
    and neither is a relative path matching ``ignore_extra`` (fnmatch). An empty list is the only
    pass; a non-empty list is a list of real problems, not a score."""
    root = Path(root)
    problems: list[str] = []
    if not root.is_dir():
        return [f"root is missing: {root.as_posix()}"]
    entries = read_manifest(manifest) if isinstance(manifest, (str, Path)) else \
        {str(k): str(v).lower() for k, v in manifest.items()}
    for rel, digest in sorted(entries.items()):
        target = root / rel
        if not target.is_file():
            problems.append(f"missing: {rel}")
            continue
        actual = sha256_file(target)
        if actual != digest:
            problems.append(f"checksum mismatch: {rel} (manifest {digest}, file {actual})")
    for rel in _rel_files(root, ["."], None):
        if rel in entries or Path(rel).name.startswith("MANIFEST"):
            continue
        if any(fnmatch.fnmatch(rel, pattern) for pattern in ignore_extra):
            continue
        problems.append(f"unlisted file: {rel}")
    return problems


# --------------------------------------------------------------------------- git-backed selection
def committed_files(repo: str | Path, paths: Iterable[str | Path]) -> list[str]:
    """Relative POSIX paths under ``paths`` that ``git add`` would take, asked of git itself.

    ``git ls-files --cached --others --exclude-standard`` *is* the definition of committable here:
    tracked files plus untracked files ``.gitignore`` does not exclude. Nothing is hand-listed, so
    the selection cannot drift from ``.gitignore`` — ``*.fits``, ``state/``, ``scratch/`` and
    ``campaigns/*/tic*/sector*/normalized_series.csv`` simply do not appear. The caller still decides
    what to upload; this only decides what counts as a committed file.

    Raises ValueError for a path outside ``repo`` (fail closed rather than list the whole tree) and
    RuntimeError when git is unavailable or fails."""
    repo = Path(repo).resolve()
    if not list(paths):
        raise ValueError("pass at least one path; an empty selection would list the whole repository")
    relative: list[str] = []
    for entry in paths:
        resolved = Path(entry).resolve() if Path(entry).is_absolute() else (repo / entry).resolve()
        try:
            inside = resolved.relative_to(repo).as_posix()
        except ValueError:
            raise ValueError(f"{str(entry)!r} is outside the repository {repo.as_posix()}") from None
        relative.append(inside or ".")
    if shutil.which("git") is None:
        raise RuntimeError("git is not on PATH; committed-file selection cannot be done without it")
    done = subprocess.run(["git", "-C", str(repo), "ls-files", "-z", "--cached", "--others",
                           "--exclude-standard", "--", *relative], capture_output=True)
    if done.returncode != 0:
        raise RuntimeError(f"git ls-files failed in {repo.as_posix()}: "
                           f"{done.stderr.decode('utf-8', 'replace').strip()}")
    names = [name for name in done.stdout.decode("utf-8", "surrogateescape").split("\0") if name]
    return sorted(set(names))


def extract_git_archive(repo: str | Path, commit: str, paths: Iterable[str | Path],
                        dest: str | Path) -> list[str]:
    """Extract ``paths`` as they were at ``commit`` into ``dest``; returns the files that landed.

    Read-only by construction: ``git archive`` reads objects from the repository and never touches
    the index or the working tree, so a baseline taken this way cannot be overwritten by the run it
    is compared against. Raises RuntimeError when ``commit`` is not in ``repo`` (or git fails).
    Python's tar extraction filter refuses absolute or parent-escaping members where it exists."""
    repo, dest = Path(repo), Path(dest)
    wanted = [str(p) for p in paths]
    if shutil.which("git") is None:
        raise RuntimeError("git is not on PATH; a pinned baseline cannot be extracted without it")
    done = subprocess.run(["git", "-C", str(repo), "archive", "--format=tar", commit, *wanted],
                          capture_output=True)
    if done.returncode != 0:
        raise RuntimeError(f"git archive {commit} in {repo.as_posix()} failed: "
                           f"{done.stderr.decode('utf-8', 'replace').strip()}")
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(done.stdout)) as archive:
        try:
            archive.extractall(dest, filter="data")   # 3.12+: no absolute/escaping members
        except TypeError:                             # pragma: no cover - older 3.11.x runtimes
            archive.extractall(dest)
    return _rel_files(dest, ["."], None)


# --------------------------------------------------------------------------- bookkeeping vs science
# Excluded from the science list, with the reason string used in the report. Everything not named
# here is a science value: over-reporting a science difference is cheap, hiding one is not.
_RUN_STATE = frozenset({
    "run_id", "run_ids", "ledger_run_id", "config_hash", "attempt", "attempts", "elapsed_s",
    "seconds", "duration_s", "took_s", "host", "hostname", "pid", "user", "machine", "platform",
    "environment", "package_versions", "versions", "python_version", "cygnus_version",
    "fetched_now", "pinned", "sha256", "md5", "checksum", "checksums", "digest",
})
# digests carry the "<...>_sha256" convention too (rows_sha256, product_sha256, …)
_CHECKSUM_SUFFIXES = ("_sha256", "_md5", "_checksum", "_checksums", "_digest", "_hash")
# exact names plus the "<...>_utc" convention used throughout the runner outputs
_TIMESTAMPS = frozenset({
    "date", "timestamp", "utc", "now", "as_of", "generated_at", "created_at", "updated_at",
    "started_at", "finished_at", "retrieved_at", "queried_at", "checked_at",
})
# reference-frame and provenance labels: they describe how a value was sourced, not the measurement
_LABELS = frozenset({
    "epoch", "frame", "equinox", "position_epoch", "epoch_source", "position_source",
    "source_frame", "reference_frame", "frame_label", "epoch_label", "source_label",
    "provenance", "origin",
})
# free-text prose: interpretation, wording and notes, never a number a report quotes
_FREE_TEXT = frozenset({
    "note", "notes", "summary", "comment", "comments", "description", "caveat", "caveats",
    "interpretation", "interpretations", "message", "remarks", "title", "detail", "details",
    "rationale", "prose", "explanation", "abstract", "conclusion", "disclaimer",
})
# keys whose value is a location or a pointer by definition
_LOCATORS = frozenset({
    "spec", "report", "search_log", "url", "urls", "uri", "link", "href", "outputs", "output_dir",
    "root", "location", "scratch", "record", "manifest", "log", "logs", "worktree",
})
# keys that *may* hold a location: a bare name (a product id, say) stays a science value
_AMBIGUOUS_LOCATORS = frozenset({"file", "files", "path", "paths", "dir", "directory", "filepath"})
_AMBIGUOUS_SUFFIXES = ("_file", "_files", "_path", "_paths", "_dir", "_directory")
_PRIVATE_PATH = re.compile(
    r"^(?:[A-Za-z]:[\\/]|\\\\|//|/(?:content|home|tmp|var|mnt|root|media|drive|usr|opt|srv|workspace)(?:/|$)|scratch:)")


def _looks_like_path(value: Any) -> bool:
    if isinstance(value, (list, tuple)):
        return any(_looks_like_path(item) for item in value)
    if not isinstance(value, str) or not value:
        return False
    return ("/" in value or "\\" in value or value.startswith("scratch:")
            or bool(re.match(r"^[A-Za-z]:", value)))


def _classify(key: str, value: Any) -> str | None:
    """The bookkeeping reason for one leaf, or ``None`` when the leaf is a science value."""
    name = key.strip().lower()
    if name in _RUN_STATE or name in _TIMESTAMPS or name.endswith("_utc") \
            or name.endswith(_CHECKSUM_SUFFIXES):
        return "run bookkeeping"
    if name in _LABELS:
        return "reference-frame or provenance label"
    if name in _FREE_TEXT or name.endswith(("_note", "_notes", "_comment", "_comments")):
        return "free-text interpretation"
    if name in _LOCATORS:
        return "path or locator"
    if name in _AMBIGUOUS_LOCATORS or name.endswith(_AMBIGUOUS_SUFFIXES):
        if _looks_like_path(value):
            return "path or locator"
    if isinstance(value, str) and _PRIVATE_PATH.match(value):
        return "absolute or private path"
    return None


_RULE_SUMMARY = {
    "note": ("a leaf is bookkeeping when its key is one of these sets (or matches the stated suffix "
             "rule); every other leaf is a science value"),
    "run_state_keys": sorted(_RUN_STATE),
    "checksum_suffixes": list(_CHECKSUM_SUFFIXES),
    "timestamp_keys": sorted(_TIMESTAMPS),
    "timestamp_suffix": "_utc",
    "label_keys": sorted(_LABELS),
    "free_text_keys": sorted(_FREE_TEXT),
    "free_text_suffixes": ["_note", "_notes", "_comment", "_comments"],
    "locator_keys": sorted(_LOCATORS),
    "ambiguous_locator_keys": sorted(_AMBIGUOUS_LOCATORS),
    "ambiguous_locator_suffixes": list(_AMBIGUOUS_SUFFIXES),
    "private_path_value_pattern": _PRIVATE_PATH.pattern,
    "structural_differences": ("a key or file present on one side only, a changed value type and a "
                               "changed list length are reported as science differences"),
    "numeric_tolerance": ("opt-in: compare_campaigns(numeric_rtol=...) treats two numbers that agree "
                          "within that relative tolerance as a 'numerical' difference — reported with "
                          "the exact relative difference, never equal and never a science value. "
                          "The default is strict: every numeric difference is a science difference."),
}


def _leaf_key(leaf: str) -> str:
    """The key a leaf path ends in, with any list indices removed (``/a[0]/b[2]`` -> ``b``)."""
    tail = leaf.rsplit("/", 1)[-1]
    return re.sub(r"(\[\d+\])+$", "", tail)


def _show(value: Any, limit: int = 160) -> str:
    if value is _MISSING:
        return _MISSING
    try:
        text = json.dumps(value, ensure_ascii=False, default=str)
    except (TypeError, ValueError):   # pragma: no cover - json.dumps(default=str) rarely raises
        text = repr(value)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _matches(value: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(value, pattern) for pattern in patterns)


def _ignored_pattern(rel: str, leaf: str, ignore: Iterable[str]) -> str | None:
    identifier = f"{rel}::{leaf}"
    for pattern in ignore:
        if fnmatch.fnmatch(identifier, pattern) or fnmatch.fnmatch(leaf, pattern):
            return pattern
    return None


def _diff(report: dict, rel: str, leaf: str, baseline: Any, candidate: Any,
          ignore: Iterable[str], note: str | None = None) -> None:
    leaf = leaf or "/"
    entry = {"file": rel, "leaf": leaf, "baseline": _show(baseline), "candidate": _show(candidate)}
    if note:
        entry["note"] = note
    pattern = _ignored_pattern(rel, leaf, ignore)
    if pattern is not None:
        entry["reason"] = f"listed in ignore= as {pattern!r}"
        report["ignored"].append(entry)
        return
    key = _leaf_key(leaf)
    reason = _classify(key, candidate if candidate is not _MISSING else baseline)
    if reason:
        entry["reason"] = f"{reason}: {key!r}"
        report["bookkeeping"].append(entry)
    else:
        report["science"].append(entry)


def _diff_numeric(report: dict, rel: str, leaf: str, baseline: Any, candidate: Any,
                  ignore: Iterable[str], tolerance: float, relative: float) -> None:
    """Record one within-tolerance numeric difference: reported, never equal, never science.
    An ignore= pattern still applies first, as for every other class."""
    leaf = leaf or "/"
    entry = {"file": rel, "leaf": leaf, "baseline": _show(baseline), "candidate": _show(candidate),
             "relative": relative,
             "note": f"within the declared numeric tolerance {tolerance!r}: relative difference {relative:.3e}"}
    pattern = _ignored_pattern(rel, leaf, ignore)
    if pattern is not None:
        entry["reason"] = f"listed in ignore= as {pattern!r}"
        report["ignored"].append(entry)
        return
    report["numerical"].append(entry)


def _compare(baseline: Any, candidate: Any, leaf: str, rel: str, report: dict,
             ignore: Iterable[str], numeric_rtol: float | None) -> None:
    if isinstance(baseline, dict) and isinstance(candidate, dict):
        for key in sorted(set(baseline) | set(candidate), key=str):
            child = f"{leaf}/{key}"
            if key in baseline and key in candidate:
                _compare(baseline[key], candidate[key], child, rel, report, ignore, numeric_rtol)
            elif key in candidate:
                _diff(report, rel, child, _MISSING, candidate[key], ignore, "key only in the candidate")
            else:
                _diff(report, rel, child, baseline[key], _MISSING, ignore, "key only in the baseline")
        return
    if isinstance(baseline, list) and isinstance(candidate, list):
        if len(baseline) != len(candidate):
            _diff(report, rel, leaf or "/", len(baseline), len(candidate), ignore, "list length differs")
        for index, (left, right) in enumerate(zip(baseline, candidate)):
            _compare(left, right, f"{leaf}[{index}]", rel, report, ignore, numeric_rtol)
        return
    report["_leaves"] += 1
    if isinstance(baseline, float) and isinstance(candidate, float) \
            and math.isnan(baseline) and math.isnan(candidate):
        return
    numeric = (isinstance(baseline, (int, float)) and isinstance(candidate, (int, float))
               and not isinstance(baseline, bool) and not isinstance(candidate, bool))
    if baseline == candidate and (type(baseline) is type(candidate) or numeric):
        return
    if numeric and numeric_rtol is not None:
        scale = max(abs(baseline), abs(candidate), 1e-300)
        relative = abs(baseline - candidate) / scale
        if relative <= numeric_rtol:
            _diff_numeric(report, rel, leaf, baseline, candidate, ignore, numeric_rtol, relative)
            return
    note = None if type(baseline) is type(candidate) else \
        f"type changed from {type(baseline).__name__} to {type(candidate).__name__}"
    _diff(report, rel, leaf, baseline, candidate, ignore, note)


def _finalise(report: dict, ignore: Iterable[str], ignore_files: Iterable[str],
              max_items: int, numeric_rtol: float | None) -> dict:
    counts = {
        "files_compared": report["files_compared"],
        "leaves_compared": report.pop("_leaves"),
        "bookkeeping": len(report["bookkeeping"]),
        "numerical": len(report["numerical"]),
        "science": len(report["science"]),
        "ignored": len(report["ignored"]),
        "ignored_files": len(report["ignored_files"]),
        "files_only_in_baseline": len(report["files_only_in_baseline"]),
        "files_only_in_candidate": len(report["files_only_in_candidate"]),
        "not_compared": len(report["not_compared"]),
        "problems": len(report["problems"]),
    }
    if report["problems"]:
        status = "incomplete"
    elif report["science"] or report["files_only_in_baseline"] or report["files_only_in_candidate"]:
        status = "science_differences"
    elif report["bookkeeping"] or report["numerical"] or report["ignored"] or report["ignored_files"]:
        status = "bookkeeping_only"
    else:
        status = "identical"
    report["counts"] = counts
    report["status"] = status
    report["identical"] = status == "identical"
    report["numeric_rtol"] = numeric_rtol
    report["ignore"] = sorted(set(ignore))
    report["ignore_files"] = sorted(set(ignore_files))
    report["max_items"] = max_items
    report["rules"] = _RULE_SUMMARY
    return report


def compare_campaigns(baseline_dir: str | Path, candidate_dir: str | Path, *,
                      ignore: Iterable[str] = (), ignore_files: Iterable[str] = (),
                      suffixes: Iterable[str] = (".json",), max_items: int = 40,
                      numeric_rtol: float | None = None) -> dict:
    """Compare a committed campaign baseline with a run's outputs, leaf by leaf.

    Both directories are campaign directories (``campaigns/<id>/``); every file with one of
    ``suffixes`` (default ``.json``) is parsed and compared recursively. Each differing leaf becomes
    one entry classified as *bookkeeping* or *science* (see ``_RULE_SUMMARY`` / the ``rules`` key of
    the result). Structural differences — a key or file on one side only, a changed value type, a
    changed list length — are science differences, because a record that is shaped differently is
    not the same record. Files with another suffix are never compared leaf by leaf and are listed
    under ``not_compared`` so nothing is silently invisible.

    ``numeric_rtol`` is an explicit, recorded decision, and the default is strict: every numeric
    difference is a science difference. When a tolerance is declared (for example round-off from
    different BLAS builds on two runtimes), two numbers agreeing within that *relative* tolerance
    are recorded under ``numerical`` with their exact relative difference — always listed, never
    equal, never science; a difference beyond the tolerance is still a science difference. The
    declared value is stored in the result itself, so the artifact names its own tolerance.

    ``ignore`` holds fnmatch patterns over ``<file>::<leaf>`` or the leaf alone; ``ignore_files``
    holds patterns over relative file paths. Both are reported with the pattern that matched, so an
    ignored difference is a documented decision rather than a hidden one. Neither side is modified.

    The result is a plain dict: ``status`` (``identical``, ``bookkeeping_only``,
    ``science_differences`` or ``incomplete``; ``bookkeeping_only`` covers declared-tolerance
    numeric differences too), ``counts``, and the entry lists ``bookkeeping``, ``numerical``,
    ``science``, ``ignored``, ``ignored_files``, ``files_only_in_baseline``,
    ``files_only_in_candidate``, ``not_compared`` and ``problems``."""
    base, cand = Path(baseline_dir), Path(candidate_dir)
    report: dict = {
        "baseline": base.as_posix(), "candidate": cand.as_posix(), "files_compared": 0, "_leaves": 0,
        "bookkeeping": [], "numerical": [], "science": [], "ignored": [], "ignored_files": [],
        "files_only_in_baseline": [], "files_only_in_candidate": [], "not_compared": [], "problems": [],
    }
    for label, directory in (("baseline", base), ("candidate", cand)):
        if not directory.is_dir():
            report["problems"].append(f"{label} directory is missing: {directory.as_posix()}")
    if report["problems"]:
        return _finalise(report, ignore, ignore_files, max_items, numeric_rtol)

    baseline_files = set(_rel_files(base, ["."], None))
    candidate_files = set(_rel_files(cand, ["."], None))
    suffix_list = list(suffixes)
    for rel in sorted(baseline_files | candidate_files):
        if _matches(rel, ignore_files):
            report["ignored_files"].append({"file": rel, "reason": "listed in ignore_files="})
            continue
        if not rel.endswith(tuple(suffix_list)):
            report["not_compared"].append({"file": rel, "reason": f"not one of {suffix_list}"})
            continue
        if rel not in candidate_files:
            report["files_only_in_baseline"].append(rel)
            continue
        if rel not in baseline_files:
            report["files_only_in_candidate"].append(rel)
            continue
        try:
            before = json.loads((base / rel).read_text(encoding="utf-8"))
            after = json.loads((cand / rel).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            report["problems"].append(f"{rel}: not comparable JSON ({exc})")
            continue
        report["files_compared"] += 1
        _compare(before, after, "", rel, report, ignore, numeric_rtol)
    return _finalise(report, ignore, ignore_files, max_items, numeric_rtol)


def render_report(result: Mapping[str, Any], *, title: str = "Colab equivalence comparison") -> str:
    """Render a ``compare_campaigns`` result as the markdown a reviewer reads (and ships back).

    Long lists are truncated with a count of what was left out; the full list is in the result
    itself, which the caller writes beside the markdown. Differences are presented for a decision,
    never as a pass."""
    counts = result.get("counts", {})
    maximum = int(result.get("max_items", 40) or 40)
    status = result.get("status", "unknown")
    science = list(result.get("science", []))
    bookkeeping = list(result.get("bookkeeping", []))
    numerical = list(result.get("numerical", []))
    ignored = list(result.get("ignored", []))
    tolerance = result.get("numeric_rtol")
    lines = [
        f"# {title}", "",
        f"- baseline: `{result.get('baseline')}`", f"- candidate: `{result.get('candidate')}`",
        f"- status: **{status}**",
        f"- declared numeric tolerance: {tolerance!r} (strict: every numeric difference is a science "
        f"difference)" if tolerance is None else
        f"- declared numeric tolerance: {tolerance!r} — numbers agreeing within it are reported under "
        f"'numerical' with their relative difference, never equal and never science",
        f"- files compared: {counts.get('files_compared', 0)}; leaves compared: "
        f"{counts.get('leaves_compared', 0)}",
        f"- science differences: {counts.get('science', 0)}; bookkeeping differences: "
        f"{counts.get('bookkeeping', 0)}; declared-tolerance numeric differences: "
        f"{counts.get('numerical', 0)}; explicitly ignored: {counts.get('ignored', 0)} "
        f"(+{counts.get('ignored_files', 0)} ignored file(s))",
        f"- files only in the baseline: {counts.get('files_only_in_baseline', 0)}; only in the "
        f"candidate: {counts.get('files_only_in_candidate', 0)}; not compared: "
        f"{counts.get('not_compared', 0)}; problems: {counts.get('problems', 0)}", "",
        "Every difference below needs a decision: explain it (and record the explanation) or fix the "
        "code. A bookkeeping difference is not a pass — it is a difference whose class the pilot "
        "expects to be harmless, and it still has to be read: checksums, configuration hashes and "
        "run-state flags live in that class.", "",
        "## Science differences (the pilot is not equivalent until each is explained or fixed)", "",
    ]
    lines += _table(science, maximum)
    lines += ["", "## Bookkeeping differences (expected class; read them)", ""]
    lines += _table(bookkeeping, maximum)
    if numerical:
        worst = max(numerical, key=lambda entry: float(entry.get("relative") or 0.0))
        lines += ["", "## Differences within the declared numeric tolerance "
                  f"(reported, not science; the largest is {float(worst['relative']):.3e} relative)", ""]
        lines += _table(numerical, maximum)
    lines += ["", "## Explicitly ignored (caller-supplied; a decision, not a pass)", ""]
    lines += _table(ignored, maximum)
    if result.get("ignored_files"):
        lines += ["", "Files excluded from leaf comparison:",
                  *[f"- `{entry['file']}` — {entry['reason']}" for entry in result["ignored_files"]]]
    if result.get("files_only_in_baseline"):
        lines += ["", "## Files only in the baseline (the run did not reproduce them)", "",
                  *[f"- `{rel}`" for rel in result["files_only_in_baseline"]]]
    if result.get("files_only_in_candidate"):
        lines += ["", "## Files only in the candidate (not in the committed baseline)", "",
                  *[f"- `{rel}`" for rel in result["files_only_in_candidate"]]]
    if result.get("not_compared"):
        lines += ["", "## Not compared leaf by leaf", "",
                  *[f"- `{entry['file']}` — {entry['reason']}" for entry in result["not_compared"]]]
    if result.get("problems"):
        lines += ["", "## Problems (the comparison could not be completed)", "",
                  *[f"- {problem}" for problem in result["problems"]]]
    lines += ["", "## How leaves are classified", "",
              "A leaf is bookkeeping when its key is in the run-bookkeeping, timestamp (`*_utc`), "
              "reference-frame/provenance-label, free-text or locator sets, when it ends in the "
              "documented locator suffixes with a path-like value, or when its value is an absolute "
              "or private path; every other leaf is a science value. Keys, suffixes and the path "
              "pattern are listed in full in the machine-readable report (`rules`). Structural "
              "differences (a key or file on one side only, a changed type, a changed list length) "
              "are science differences. When a numeric tolerance was declared, numbers that agree "
              "within it are reported under 'numerical' with their relative difference; beyond it, "
              "or with no tolerance declared (the default), every numeric difference is science.", ""]
    return "\n".join(lines)


def _table(entries: list[dict], maximum: int) -> list[str]:
    if not entries:
        return ["None."]
    rows = ["| file | leaf | baseline | candidate | note |", "|---|---|---|---|---|"]
    for entry in entries[:maximum]:
        rows.append("| `{file}` | `{leaf}` | {baseline} | {candidate} | {note} |".format(
            file=entry["file"], leaf=entry["leaf"],
            baseline=_escape(entry["baseline"]), candidate=_escape(entry["candidate"]),
            note=_escape(entry.get("reason") or entry.get("note") or "")))
    if len(entries) > maximum:
        rows.append(f"| … | | | | {len(entries) - maximum} more (see the machine-readable report) |")
    return rows


def _escape(text: str) -> str:
    return str(text).replace("|", "\\|")
