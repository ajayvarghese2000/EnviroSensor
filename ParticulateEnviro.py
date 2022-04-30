#!/usr/bin/env python3

import time
import colorsys
import sys
import ST7735
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280
from pms5003 import PMS5003, ReadTimeoutError as pmsReadTimeoutError
from enviroplus import gas
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fonts.ttf import RobotoMedium as UserFont

# BME280 temperature/pressure/humidity sensor
bme280 = BME280()

# PMS5003 particulate sensor
pms5003 = PMS5003()

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up


for v in variables:
    values[v] = [1] * WIDTH

def get_temperature():
	factor = 2.25 	# Tuning factor for compensation, decrease to lower
					#temp, increase to raise temp
	cpu_temp = get_cpu_temperature()
	# Smooth out with some averaging to decrease jitter
	cpu_temps = cpu_temps[1:] + [cpu_temp]
	avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
	raw_temp = bme280.get_temperature()
	data = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
	return data
	
def get_gas():
	data = gas.read_all()
	gas["co"] = data.oxidising/1000
	gas["no2"] = data.reducing/1000
	gas["nh3"] = data.nh3/1000
	return gas

def get_air():
	data = pms5003.read()
	air["pm1"] = data.pm_ug_per_m3(1.0)
	air["pm2_5"] = data.pm_ug_per_m3(2.5)
	air["pm10"] = data.pm_ug_per_m3(10)
	return air


        












