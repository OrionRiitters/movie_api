from http.server import HTTPServer, BaseHTTPRequestHandler
import time, json
from python import omdb_request

class Serv (BaseHTTPRequestHandler):
    
    def assemble_submit_response(self):
        omdb_url = self.path.replace('/placeholder?', '')
        omdb_raw = omdb_request.omdb_get(omdb_url)
        omdb_dict = omdb_request.condense_response(omdb_raw)

        return str(json.dumps(omdb_dict))



    def do_GET(self):
        if self.path =='/':
            self.path = '/index.html'
        try:
            write_info = open(self.path[1:]).read()
            self.send_response(200)
        except:
            if self.path.split('?')[0] == '/placeholder':
                write_info = self.assemble_submit_response()
                self.send_response(200)
            else:
                write_info = "File not found"
                self.send_response(404)

        self.end_headers()

        self.wfile.write(bytes(write_info, 'utf-8'))






try:
	server = HTTPServer(('', 8080), Serv)
	print('Started httpserver on port 8080, nice!')
	server.serve_forever()

except KeyboardInterrupt:
	print(' You pressed ^C - shutting down server')
	server.socket.close()
	

