import argparse
import math
import requests
import os
import socket
import serial
import time

from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="192.168.86.201",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  serial_port = '/dev/cu.usbmodem14201';
  baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
  ser = serial.Serial(serial_port, baud_rate)

  print('''The script will begin execution in 5 seconds.
  Please navigate to Galaxy Earth.''')

  #time.sleep(5)

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  while True:
    line = ser.readline();
    client.send_message("/nav", line)
