import serial,string,time
import os
from time import sleep
from datetime import datetime
import csv

ser = serial.Serial('/dev/ttyACM0',115200)

while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8', errors = 'ignore').strip('\r\n')
        datasplit = cookedserial.split(' ')
        for line in datasplit:
            storedata = line.split('\t')
        with open ("test4.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(),storedata]) #do storedata[] if key individual parameters needed to be seperate