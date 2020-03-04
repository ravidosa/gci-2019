import argparse
import math
import requests
import os
import socket

from pythonosc import dispatcher
from pythonosc import osc_server

def flyto_handler(unused_addr, args):
	requests.get('http://localhost:5430/kml/query/search/' + args)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("port", type=int, default=5005, help="The port for the OSC")
	args = parser.parse_args()

	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/flyto", flyto_handler)

	server = osc_server.ThreadingOSCUDPServer((socket.gethostbyname(socket.gethostname()), args.port), dispatcher)
	print("Serving at {}".format(server.server_address))
	server.serve_forever()
