#!/usr/bin/env python3
"""Local preview server.

Python's plain `http.server` 404s on extensionless paths, so `/about` breaks
locally even though it works fine once deployed — Netlify's pretty_urls setting
resolves it there. This subclass does the same thing, so what you see locally
matches what ships.

    python3 serve.py [port]
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler


class PrettyURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        # "/about" -> "about.html", when the bare path isn't already a file.
        if not os.path.exists(local) and not path.endswith("/"):
            candidate = local + ".html"
            if os.path.isfile(candidate):
                return candidate
        return local

    def end_headers(self):
        # Never cache during development; netlify.toml handles caching in prod.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Serving on http://localhost:{port}  (Ctrl-C to stop)")
    HTTPServer(("", port), PrettyURLHandler).serve_forever()
