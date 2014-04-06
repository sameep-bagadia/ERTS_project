#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Hello World !")
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', 8001), myHandler)
    print 'Started httpserver on port'

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
