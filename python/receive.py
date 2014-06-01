#!/usr/bin/python

# A simple listener that accepts incoming files and saves them to the cwd
# curl -F "file=@XXXXX" http://x.x.x.x:3301/

import cgi, logging, time
from pprint import pprint
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer

class PostHandler(SimpleHTTPRequestHandler):
	def do_POST(self):
		form = cgi.FieldStorage(
			fp = self.rfile,
			headers = self.headers,
			environ = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type']}
		)

		for item in form.list:
			timeft = time.strftime("%Y%m%d_%H%M%S")
			with open(item.filename + "." + timeft, "wb") as fh:
				fh.write(item.value)
			print "File '%s' was saved to the current directory!" % item.filename
		
		self.send_response(200)
		self.end_headers()
		
port = 3301
httpd = SocketServer.TCPServer(("", port), PostHandler)
print "Started curl receiver on port %d" % port
httpd.serve_forever()

