"""Local preview server for the built site (127.0.0.1 only, read-only).

Serves files from the build directory and nothing else: paths are resolved
and must stay inside the root, dotfiles are refused, only GET/HEAD are
accepted, and responses carry the same security headers recommended for the
production static host (see ``docs/PUBLISHING.md``).
"""

from __future__ import annotations

import mimetypes
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

SECURITY_HEADERS = {
    "Content-Security-Policy": "default-src 'self'; img-src 'self' data:; style-src 'self'; "
                               "script-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "no-referrer",
    "Permissions-Policy": "interest-cohort=()",
}

mimetypes.add_type("text/markdown; charset=utf-8", ".md")
mimetypes.add_type("application/yaml", ".yaml")


def safe_resolve(root: Path, url_path: str, base_path: str = "/") -> Path | None:
    """Map a URL path to a file under root, or None (traversal, dotfile, missing)."""
    path = unquote(urlsplit(url_path).path)
    base = "/" + base_path.strip("/") + "/" if base_path.strip("/") else "/"
    if not path.startswith(base):
        return None
    rel = path[len(base):]
    parts = [p for p in rel.split("/") if p]
    if any(p in ("..", ".") or p.startswith(".") or "\\" in p or ":" in p for p in parts):
        return None
    root = root.resolve()
    target = (root.joinpath(*parts)).resolve() if parts else root
    if not target.is_relative_to(root):
        return None
    if target.is_dir():
        target = target / "index.html"
    return target if target.is_file() else None


class Handler(SimpleHTTPRequestHandler):
    root: Path
    base_path: str = "/"

    def end_headers(self) -> None:
        for k, v in SECURITY_HEADERS.items():
            self.send_header(k, v)
        super().end_headers()

    def send_head(self):  # type: ignore[override]
        path = unquote(urlsplit(self.path).path)
        target = safe_resolve(self.root, self.path, self.base_path)
        if target is not None and target.name == "index.html" and not path.endswith("/") \
                and not path.endswith(".html"):
            self.send_response(HTTPStatus.MOVED_PERMANENTLY)
            self.send_header("Location", path + "/")
            self.end_headers()
            return None
        if target is None:
            page = self.root / "404.html"
            body = page.read_bytes() if page.is_file() else b"Not found"
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self._body = body
            return None
        ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        if ctype.startswith("text/") and "charset" not in ctype:
            ctype += "; charset=utf-8"
        f = open(target, "rb")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(target.stat().st_size))
        if target.relative_to(self.root.resolve()).parts[:1] == ("files",):
            self.send_header("Content-Disposition", f'attachment; filename="{target.name}"')
        self.end_headers()
        return f

    def do_GET(self) -> None:  # noqa: N802
        self._body = None
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()
        elif self._body:
            self.wfile.write(self._body)

    def do_HEAD(self) -> None:  # noqa: N802
        f = self.send_head()
        if f:
            f.close()

    def _refuse(self) -> None:
        self.send_error(HTTPStatus.METHOD_NOT_ALLOWED)

    do_POST = do_PUT = do_DELETE = do_PATCH = _refuse  # noqa: N815


def make_server(root: Path, port: int = 8765, base_path: str = "/") -> ThreadingHTTPServer:
    handler = type("BoundHandler", (Handler,), {"root": Path(root).resolve(), "base_path": base_path})
    return ThreadingHTTPServer(("127.0.0.1", port), partial(handler))


def serve(root: Path, port: int = 8765, base_path: str = "/") -> None:
    httpd = make_server(root, port, base_path)
    print(f"serving {root} at http://127.0.0.1:{port}{base_path}  (Ctrl+C to stop)", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
