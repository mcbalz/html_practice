"""Local dev server – serves the project root at http://localhost:8000"""
import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = 8000
ROOT = Path(__file__).parent


def serve() -> None:
    # optional: uv run serve week1/index.html
    path = sys.argv[1] if len(sys.argv) > 1 else ""
    handler = http.server.SimpleHTTPRequestHandler
    __import__("os").chdir(ROOT)
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        url = f"http://localhost:{PORT}/{path}"
        print(f"Serving {ROOT} at http://localhost:{PORT}  (Ctrl-C to stop)")
        webbrowser.open(url)
        httpd.serve_forever()


if __name__ == "__main__":
    serve()
