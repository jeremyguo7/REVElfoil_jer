import serial
import pynmea2
from datetime import datetime
import csv

port = "/dev/ttyACM0"
lat = 0
lng = 0
speed = 0


def parseGPS(data):
    global lat
    global lng
    global speed 
    if data[0:6] == "$GPRMC":
        print('GPRMC received')
        msg = pynmea2.parse(data)
        lat = msg.latitude
        lng = msg.longitude
        speed = msg.spd_over_grnd
        gps = "Latitude=" + str(lat) +" " + " and Longitude" +" "+ str(lng) +" and Speed in knots"+str(speed)
        print(gps)

ser = serial.Serial(port, baudrate = 15200, timeout = 0.5)
while True:
    data = ser.readline().decode()
    parseGPS(data)
    if lat is not None:
        with open("gps.csv","a") as f:
           writer = csv.writer(f)
           writer.writerow([datetime.now(),lat,lng])



