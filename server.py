from data_source import get_data
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        data=get_data()
        self.wfile.write(json.dumps(data).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), RequestHandler)
    print('Starting server at http://localhost:8000')
    server.serve_forever()