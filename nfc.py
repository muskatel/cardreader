import serial

ser = None
CARD_BYTES = 4

def init():
    global ser
    ser = serial.Serial(port='/dev/ttyAMA0', baudrate=9600)
    ser.write(chr(2))
    
def read_card():
    c = ser.read(CARD_BYTES)
    return c.encode("hex")

def cleanup():
    ser.close()