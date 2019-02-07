from http.server import HTTPServer, BaseHTTPRequestHandler
import time
from python import combine_dictionaries

class Serv (BaseHTTPRequestHandler):
    


    def assemble_submit_response(self):
        return combine_dictionaries.combine_dictionaries('https://www.rottentomatoes.com/m/matrix', 'http://www.omdbapi.com/?apikey=c346dee9&t=the+matrix')



    def do_GET(self):
        if self.path =='/':
            self.path = '/index.html'
        try:
            print(self.path)
            write_info = open(self.path[1:]).read()
            self.send_response(200)
        except:
            write_info = "File not found"
            self.send_response(404)

        self.end_headers()

        if self.path == '/queryResults.json':
            write_info = self.assemble_submit_response()
        self.wfile.write(bytes(write_info, 'utf-8'))






try:
	server = HTTPServer(('', 8080), Serv)
	print('Started httpserver on port 8080, nice!')
	server.serve_forever()

except KeyboardInterrupt:
	print(' You pressed ^C - shutting down server')
	server.socket.close()
	

