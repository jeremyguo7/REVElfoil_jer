import serial
import time
import string
import pynmea2
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

port = "/dev/ttyACM0"
pnChannel = "REV GPS Tracker";
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "<yourkey>"
pnconfig.publish_key = "<yourkey>"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
pubnub.subscribe().channels(pnChannel).execute()
 
def parseGPS(data):
    if data[0:6] == "$GPRMC":
        print('GPRMC received')
        msg = pynmea2.parse(data)
        lat = msg.latitude
        lng = msg.longitude
        try:
            envelope = pubnub.publish().channel(pnChannel).message({
            'lat':lat,
            'lng':lng
            }).sync()
            print("publish timetoken: %d" % envelope.result.timetoken)
        except PubNubException as e:
            handle_exception(e)

 
ser = serial.Serial(port, baudrate = 15200, timeout = 0.5)
while True:
   data = ser.readline().decode()
   parseGPS(data)

