#!/usr/bin/env python3
from data_source import get_data
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

#https://gist.github.com/bsingr/a5ef6834524e82270154a9a72950c842
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        data=get_data(True)
        self.wfile.write(json.dumps(data).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8181), RequestHandler)
    print('Starting server at http://localhost:8181')
    server.serve_forever()