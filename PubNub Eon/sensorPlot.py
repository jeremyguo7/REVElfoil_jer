import os
import time
import sys
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException
from random import randrange
import serial
import pynmea2

pnChannel = "REV Sensors";
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "<yourown>"
pnconfig.publish_key = "<yourown>"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
pubnub.subscribe().channels(pnChannel).execute()

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
        dictionary = {"eon": {"Speed in Knots": speed}}
        pubnub.publish().channel(pnChannel).message(dictionary).sync()
        time.sleep(1)

