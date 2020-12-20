from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
from Phidget22.Devices.Magnetometer import *
import time
import csv
from datetime import datetime

Ac = Accelerometer()
# Ac.setOnAccelerationChangeHandler(onAccelerationChange)
Ac.openWaitForAttachment(1000)

# Gy = Gyroscope()
# Gy.setOnAngularRateUpdateHandler(onAngularRateUpdate)
# Gy.openWaitForAttachment(1000)
# 
# Mag = Magnetometer()
# magnetometer0.setOnMagneticFieldChangeHandler(onMagneticFieldChange)
# Mag.openWaitForAttachment(1000)
import time
import serial


ser = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)


while True: 
    acceleration = Ac.getAcceleration()
    print("Acceleration: " + str(acceleration))
    time.sleep(1)
    xcord = acceleration[1]
    ycord = acceleration[2]
    strxcord = str(xcord)
    CurrentTime = datetime.now()
    ser.write(strxcord.encode())
    print(strxcord.encode())
    time.sleep(1)
    with open("test2.csv","a") as f:
            writer = csv.writer(f)
            writer.writerow([CurrentTime,acceleration])
            print(acceleration)
            


