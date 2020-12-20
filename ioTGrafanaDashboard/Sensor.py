import time
import logging
from random import randrange
logging.basicConfig(filename='Speed.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)
import serial
import pynmea2
 
port = "/dev/ttyACM0"
ser = serial.Serial(port, baudrate = 15200, timeout = 0.5)
speed = 0.00

def parseGPS(data):
    global speed
    if data[0:6] == "$GPRMC":
        msg = pynmea2.parse(data)
        speed = msg.spd_over_grnd
        
while True:
    data = ser.readline().decode()
    parseGPS(data)
    if speed is not None:
        print(speed)
        logging.info('Speed={0:0.1f} C '.format(speed))
        time.sleep(1)
        