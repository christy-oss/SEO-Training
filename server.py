#!/usr/bin/env python3
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import base64

PASSWORD = os.environ.get('APP_PASSWORD', 'password123')
PORT = int(os.environ.get('PORT', 8080))

class AuthHandler(SimpleHTTPRequestHandler):
          def do_GET(self):
                        auth_header = self.headers.get('Authorization')

        if not auth_header:
                          self.send_response(401)
                          self.send_header('WWW-Authenticate', 'Basic realm="SEO Training"')
                          self.send_header('Content-type', 'text/html')
                          self.end_headers()
                          self.wfile.write(b'<h1>401 Unauthorized</h1><p>Password required.</p>')
                          return

        try:
                          auth_type, auth_data = auth_header.split(' ', 1)
                          if auth_type.lower() != 'basic':
                                                self.send_response(401)
                                                self.end_headers()
                                                return

                          decoded = base64.b64decode(auth_data).decode('utf-8')
                          username, password = decoded.split(':', 1)

            if password != PASSWORD:
                                  self.send_response(401)
                                  self.send_header('WWW-Authenticate', 'Basic realm="SEO Training"')
                                  self.send_header('Content-type', 'text/html')
                                  self.end_headers()
                                  self.wfile.write(b'<h1>401 Unauthorized</h1><p>Invalid password.</p>')
                                  return
                          except:
            self.send_response(401)
                                            self.end_headers()
            return

        super().do_GET()

if __name__ == '__main__':
          server = HTTPServer(('0.0.0.0', PORT), AuthHandler)
    print(f'Starting server on port {PORT}')
    sys.stdout.flush()
    server.serve_forever()
