import serial,string,time
import serial
from time import strftime
from datetime import datetime, time

ser = serial.Serial('/dev/ttyACM0',115200)

startTime = datetime.now()

try:
    while 1:
        line=ser.readline().rstrip()
        temp,outsidetemp=line.split(",")
        now = datetime.now()
        elapsedTime = now-startTime
        elapsedSeconds = (elapsedTime.microseconds+(elapsedTime.days*24*3600+elapsedTime.seconds)*10**6)/10**6
        f=open('/home/pi/sensors/sensordata/temperaturedata.csv','a')
        print >>f,("%s,%s,%s,%s"%(now.strftime("%Y-%m-%d %H:%M:%S"),elapsedSeconds,temp,outsidetemp))
      f.close
except KeyboardInterrupt:
print "\ndone"
