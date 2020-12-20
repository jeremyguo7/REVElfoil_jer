import mysql.connector
import serial
import pynmea2
from datetime import datetime

port = "/dev/ttyACM0"
ser = serial.Serial(port, baudrate = 15200, timeout = 0.5)
lat = 0
lng = 0
time = 0

def parseGPS(data):
    global lat
    global lng
    global time

    if data[0:6] == "$GPRMC":
        msg = pynmea2.parse(data)
        lat = msg.latitude
        lng = msg.longitude
        time = msg.timestamp
        gps = str(time) +" "+str(lat)+ " "+str(lng)

while True:
    data = ser.readline().decode()
    parseGPS(data)
    #MySQL connection
    cnx = mysql.connector.connect(user='<yourown>',
                              password='<yourown>',
                              host='<yourown>',
                              database='<yourown>')
    cursor = cnx.cursor()
    add_longNlat = ("INSERT INTO GPSCoordinates "
                    "(Time,GPS_long,GPS_lat)"
                    "VALUES(%s,%s,%s)")
    timenow = datetime.now()
    print(timenow,lat,lng)
    data_longNlat = (timenow,lat,lng)

    #excution
    cursor.execute(add_longNlat,data_longNlat)

    #data commition
    cnx.commit()

    cursor.close()
    cnx.close()

