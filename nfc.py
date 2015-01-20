import serial

ser = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)

def init():
    ser.write(chr(2))
    
def read_card():
    c = ser.read(4)
    return c.encode("hex")