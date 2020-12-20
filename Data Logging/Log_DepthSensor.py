import ms5837
import time
import csv

sensor = ms5837.MS5837_02BA()
freshwaterDepth = sensor.depth() # default is freshwater
sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
saltwaterDepth = sensor.depth() # No nead to read() again
sensor.setFluidDensity(1000) # kg/m^3
time.sleep(5)
while True:
	print("P: %0.1f mbar  %0.3f psi\tT: %0.2f C  %0.2f F") % (
        sensor.pressure(), # Default is mbar (no arguments)
	pressure = sensor.pressure()
        sensor.pressure(ms5837.UNITS_psi), # Request psi
        sensor.temperature(), # Default is degrees C (no arguments)
        sensor.temperature(ms5837.UNITS_Farenheit)) # Request Farenheit

