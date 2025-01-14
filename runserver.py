#!/usr/bin/env python

try:
    import CGIHTTPServer
    import BaseHTTPServer
except ImportError:
    # py3
    import http.server as CGIHTTPServer
    import http.server as BaseHTTPServer

from optparse import OptionParser
import signal
import sys

def signal_handler(signum, frame):
    sys.exit()

signal.signal(signal.SIGTERM, signal_handler)

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 8888

def main():
    parser = OptionParser()
    opts, args = parser.parse_args()
    if args:
        httpd = BaseHTTPServer.HTTPServer((args[0], int(args[1])), Handler)
        print "Collectd-web server running at http://%s:%s/" % (args[0], args[1])
    else:
        httpd = BaseHTTPServer.HTTPServer(("127.0.0.1", PORT), Handler)
        print "Collectd-web server running at http://%s:%s/" % ("127.0.0.1", PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
