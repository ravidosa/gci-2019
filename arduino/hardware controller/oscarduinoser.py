import argparse
import math
import requests
import os
import socket

from pythonosc import dispatcher
from pythonosc import osc_server
from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboardcontrol = Controller()

def nav_handler(unused_addr, args):
        line = args.decode("utf-8").split(" ")
        yaw = float(line[0])
        pitch = float(line[1])
        roll = float(line[2])
        print(str(yaw) + ", " + str(pitch) + ", " + str(roll))
        if (roll > 10):
        keyboardcontrol.release(Key.down)
        keyboardcontrol.press(Key.up)
        elif (roll < -10):
            keyboardcontrol.release(Key.up)
            keyboardcontrol.press(Key.down)
        else:
            keyboardcontrol.release(Key.up)
        keyboardcontrol.release(Key.down)
        if (pitch > 10):
            keyboardcontrol.release(Key.left)
            keyboardcontrol.press(Key.right)
        elif (pitch < -10):
            keyboardcontrol.release(Key.right)
            keyboardcontrol.press(Key.left)
        else:
            keyboardcontrol.release(Key.left)
            keyboardcontrol.release(Key.right)
        if (yaw > 10):
            keyboardcontrol.release('-')
            keyboardcontrol.press('+')
        elif (yaw < -10):
            keyboardcontrol.release('+')
            keyboardcontrol.press('-')
        else:
            keyboardcontrol.release('-')
            keyboardcontrol.release('+')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("port", type=int, default=5005, help="The port for the OSC")
	args = parser.parse_args()

	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/nav", nav_handler)

	server = osc_server.ThreadingOSCUDPServer((socket.gethostbyname(socket.gethostname()), args.port), dispatcher)
	print("Serving at {}".format(server.server_address))
	server.serve_forever()
