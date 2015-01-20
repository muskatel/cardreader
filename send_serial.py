#! /bin/python2.7

import sys
import ast
import serial
import time

ser = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)
ser.write(chr(2))
c = ser.read(4)
print c.encode("hex")
