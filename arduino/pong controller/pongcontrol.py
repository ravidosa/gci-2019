import serial
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

serial_port = '/dev/cu.usbmodem14201';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
keyboardcontrol = Controller()

ser = serial.Serial(serial_port, baud_rate)

print('''The script will begin execution in 5 seconds.
Please navigate to the page running Galaxy Pong and press <space> when you are ready to start.''')

time.sleep(5)
while True:
    line = ser.readline();
    line = line.decode("utf-8")
    roll = float(line.strip())
    if (roll > 0):
        keyboardcontrol.release('s')
        keyboardcontrol.release('w')
        keyboardcontrol.press('s')
    elif (roll < 0):
        keyboardcontrol.release('s')
        keyboardcontrol.release('w')
        keyboardcontrol.press('w')