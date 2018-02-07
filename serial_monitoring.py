#!/usr/bin/env python3
import serial
ser = serial.Serial('/dev/tty.usbmodemFA131', 115200)
while True:
    print(ser.readline())
ser.close()
