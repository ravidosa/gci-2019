import serial
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

serial_port = '/dev/cu.usbmodem14201';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
keyboardcontrol = Controller()

ser = serial.Serial(serial_port, baud_rate)

print('''The script will begin execution in 5 seconds.
Please navigate to Galaxy Earth.''')

#time.sleep(5)
while True:
    line = ser.readline();
    line = line.decode("utf-8").split(" ")
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