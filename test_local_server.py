from http.server import HTTPServer, BaseHTTPRequestHandler
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes
import json
import base64

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(204)

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        try:
            data = json.loads(self.rfile.read(length))
            login = data.get('login')
            ciphertext_b64 = data.get('password')
            print(ciphertext_b64)
            padding_needed = len(ciphertext_b64) % 4

            if padding_needed != 0:
                ciphertext_b64 += "=" * (4 - padding_needed)

            ciphertext = base64.b64decode(ciphertext_b64)

            with open("./example.private.pem", "rb") as priv_file:
                private_key = RSA.import_key(priv_file.read())
            cipher_rsa = PKCS1_v1_5.new(private_key)

            password = cipher_rsa.decrypt(ciphertext, None).decode('utf-8')
            print(f"- login : {login}")
            print(f"- password : {password}")

            self._set_headers()
            self.wfile.write(json.dumps({'status': 'ok'}).encode())
        except:
            self._set_headers(400)
            self.wfile.write(b'{"error":"invalid json"}')

HTTPServer(('', 8080), Handler).serve_forever()

