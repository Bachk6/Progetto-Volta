
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Server(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    def do_GET(self):
        self.resp=200
        self.msg=b""
        path = self.get_path()
        if path.startswith("api/"):
            apipath =path.lstrip("api/")
            #GET_FILE è per il fetch di javascript e css#
            if apipath.startswith("get_file/"):
                filename=apipath.lstrip("get_file/")
                self.msg=self.getFile("frontend/public/"+filename)
        else:
            self.resp=404
        self.send_response(self.resp)
        self.end_headers()
        self.wfile.write(self.msg)

    def getFile(self,path):
        try:
            with open(path, "rb") as f:
                data = f.read()
                f.close()
                return data
        except FileNotFoundError as e:
            self.resp = 404
            data = b""
            return data

    def do_POST(self):
        lung = int(self.headers.get("Content-Length"))
        data = self.rfile.read(lung)
        self.resp=200
        self.msg=b""
        self.send_response(self.resp)
        self.end_headers()
        self.wfile.write(self.msg)
    def get_path(self):
        return self.path.rstrip("/").lstrip("/")


def run_server()->None:
    """autoesplicativo"""
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, Server)
    print("Server in esecuzione su http://localhost:8080...")
    httpd.serve_forever()





if __name__=="__main__":
    run_server()
