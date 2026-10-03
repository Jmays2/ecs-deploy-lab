import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("VERSION", "unknown")
PORT = int(os.environ.get("PORT", "8080"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")
            return

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            message = f"Hello from ECS! Version: {VERSION}\n"
            self.wfile.write(message.encode())
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        print(format % args)


server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"Starting server on port {PORT}")
print(f"Version: {VERSION}")

server.serve_forever()
