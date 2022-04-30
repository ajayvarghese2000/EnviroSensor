try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    light = LTR559()
except ImportError:
    import ltr559
from bme280 import BME280
from pms5003 import PMS5003, ReadTimeoutError as pmsReadTimeoutError
from enviroplus import gas
from time import sleep


class Enviro:
    def __init__(self):
        # BME280 temperature/pressure/humidity sensor
        self.bme280 = BME280()

        # PMS5003 particulate sensor
        self.pms5003 = PMS5003()
        
        return

    def get_cpu_temperature(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = f.read()
            temp = int(temp) / 1000.0
        return temp

    def get_temperature(self):
        cpu_temps=[]
        factor = 1.5
        cpu_temp = self.get_cpu_temperature()
        cpu_temps = cpu_temps[1:] + [cpu_temp]
        avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
        raw_temp = self.bme280.get_temperature()
        data = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
        return data

    def get_gas(self):
        gas_data={}
        data = gas.read_all()
        gas_data["co"] = data.oxidising/1000
        gas_data["no2"] = data.reducing/1000
        gas_data["nh3"] = data.nh3/1000
        return gas_data

    def get_air(self):
        air={}
        data = self.pms5003.read()
        air["pm1"] = data.pm_ug_per_m3(1.0)
        air["pm2_5"] = data.pm_ug_per_m3(2.5)
        air["pm10"] = data.pm_ug_per_m3(10)
        return air

    def get_pressure(self):
        return self.bme280.get_pressure()

    def get_humidity(self):
        return self.bme280.get_humidity()

    def get_light(self):
        return light.get_lux()

'''
# Testing
enviro = Enviro()

while True:
    print(str(enviro.get_light())+"\n")
    sleep(0.1)
'''