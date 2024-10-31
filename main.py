import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def send_custom_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

    def do_GET(self):
        if self.path == '/healthz':
            self.send_custom_response(200, "200 OK")
        else:
            self.send_custom_response(404, "404 Not Found")

def run():
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting httpd server on {host}:{port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
