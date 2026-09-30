"""Per-product access states and capped streaming, so failures are recorded, never dropped.

A timeout, HTTP 401, cache miss or format error is an access limit, not absence of data.
"""

from __future__ import annotations

import hashlib
import zlib
from dataclasses import asdict, dataclass

STATES = ("ok", "http_401", "http_403", "http_404", "timeout", "format_error", "error", "not_tried")


@dataclass
class ProductAccess:
    product: str
    state: str = "not_tried"
    detail: str = ""
    bytes: int = 0
    sha256: str | None = None

    def __post_init__(self):
        if self.state not in STATES:
            raise ValueError(f"unknown access state {self.state!r}")

    def as_dict(self) -> dict:
        return asdict(self)


def classify_error(exc: BaseException | None = None, status: int | None = None) -> str:
    if status is not None:
        return {200: "ok", 401: "http_401", 403: "http_403", 404: "http_404"}.get(status, "error")
    name = type(exc).__name__.lower() if exc is not None else ""
    return "timeout" if "timeout" in name or "timedout" in name else "error"


def sniff_container(head: bytes) -> str:
    """'gzip' | 'tar' | 'fits' | 'unknown' from leading bytes; ranged TAR parsing needs 'tar'."""
    if head[:2] == b"\x1f\x8b":
        return "gzip"
    if head[257:262] == b"ustar":
        return "tar"
    if head[:6] == b"SIMPLE":
        return "fits"
    return "unknown"


def capped_stream(response, cap: int, chunk: int = 65536) -> tuple[bytes, str]:
    """Read at most ``cap`` bytes from a streaming response (servers may ignore Range), then close it."""
    buf = bytearray()
    try:
        for part in response.iter_content(chunk_size=chunk):
            buf += part[: cap - len(buf)]
            if len(buf) >= cap:
                break
    finally:
        response.close()
    return bytes(buf), hashlib.sha256(buf).hexdigest()


def gunzip_prefix(data: bytes) -> bytes:
    """Decompress a (possibly truncated) gzip prefix."""
    return zlib.decompressobj(31).decompress(data)
