from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path =='/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))




try:
	server = HTTPServer(('', 8080), Serv)
	print('Started httpserver on port 8080, nice!')
	server.serve_forever()

except KeyboardInterrupt:
	print(' You pressed ^C - shutting down server')
	server.socket.close()
	

