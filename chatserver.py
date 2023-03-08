from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from socketserver import ThreadingMixIn
import sys
import json
import chatgpt
import logging

logging.basicConfig(level = logging.DEBUG, 
                    filename = "/data/openai/log/chatserver.log", 
                    format = "%(asctime)s %(filename)s %(funcName)s: line %(lineno)d %(levelname)s %(message)s", 
                    datefmt = '%Y-%m-%d %H:%M:%S')

class ChatServer(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "access-control-allow-origin, authority, Authorization, content-type, version-info, X-Requested-With")

    def do_GET(self):
        self.send_response(200)
 
        self._send_cors_headers()
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'result': 'HTTP SERVER OK\n'}))
 
    def do_POST(self):
        self.send_response(200)
        datas = self.rfile.read(int(self.headers['content-length']))
        print('headers', self.headers)
        print("-->> post:", self.path, self.client_address)
        data = str(datas.decode()) #need to decode because type of datas is byte
        logging.debug("sending {} ...".format(data))

        status, res = chatgpt.chatgpt(data)
        logging.debug("get response status:{}, res:{}".format(status, res))
        self._send_cors_headers()
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if (status != 200):
            res = "error: " + res
        self.wfile.write(json.dumps(res, ensure_ascii = False))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
        
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def run(port, bind, 
        server_class = ThreadingHTTPServer,
        handler_class = ChatServer):

    with server_class((bind, port), handler_class) as httpd:
        print(
            f"Serving HTTP on {bind} port {port} "
            f"(http://{bind}:{port}/) ..."
        )
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            httpd.server_close()
            sys.exit(0)