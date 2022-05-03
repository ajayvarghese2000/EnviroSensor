<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/VwT4NrJ.png" width=650></a>
	<p align="center"> This repository is part of  a collection for the 21WSD001 Team Project. 
	All other repositories can be access below using the buttons</p>
</p>

<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/rBaZyub.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Dashboard"><img src="https://i.imgur.com/fz7rgd9.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Cloud-Server"><img src="https://i.imgur.com/bsimXcV.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Drone-Firmware"><img src="https://i.imgur.com/yKFokIL.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Simulated-Drone"><img src="https://i.imgur.com/WMOZbrf.png" alt="drawing" height = 33/></a>
</p>

<p align="center">
	Below you can find buttons that link you to the repositories that host the code for the module itself. These can also be found linked in the collection repository: <a href="https://github.com/lboroWMEME-TeamProject/Drone-Firmware">Drone Firmware</a>. 
</p>


<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/Main-Pi"><img src="https://i.imgur.com/4knNDhv.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/EnviroSensor"><img src="https://i.imgur.com/lcYUZBw.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Geiger-Counter"><img src="https://i.imgur.com/ecniGik.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Thermal-Camera"><img src="https://i.imgur.com/kuoiBTc.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/ai-cam"><img src="https://i.imgur.com/30bEKvR.png" alt="drawing" height = 33/></a>
</p>

------------

# Enviro Sensor

This repository contains code to interface the Enviro+ sensor board with the Main Pi so that data on the surrounding environment can be collected and send to the server.

------------

## Table of Contents

- [Subsystem Overview](#Subsystem-Overview)
    - [Wiring Diagram](Wiring-Diagram)
- [Code Overview](#Code-Overview)
- [Test Plan](#Test-Plan)
- [Installation](#Installation)
- [Deployment](#Deployment)

------------

## Subsystem Overview



**Subsystem Diagram :** The Enviro+ has many subsystems onboard that can be interfaced with using I2C and SPI bus
<p align="center">
	<img src="https://i.imgur.com/LSUJ2IL.png" alt="High Level Diagram"/>
</p>



### Wiring Diagram

As the Enviro+ is a Pi-Hat is can be simply slotted on to the Pi's GPIO Pins.
<p align="center">
	<img src="https://i.imgur.com/nJ8fABR.png" alt="High Level Diagram"/>
</p>


------------

## Code Overview

The `Enviro+.py` file contains the Enviro class that has member functions that allow you to access the data from the sensors. Once the Enviro object has been created you can call the following functions to get the data from the respective sensors.


- `get_temperature()` - This returns the temperature in celsius from the Enviro sensor
- `get_gas()` - This returns a dictionary with key value pairs for the concentration of CO, NO2 and NH3 in PPM
- `get_air()` - This returns a dictionary with key value pairs for the concentration of PM1, PM2.5 and PM10 particulates in ug/m³
- `get_pressure()` - This returns the atmospheric pressure in hPa
- `get_humidity()` - This returns the humidity of the air as a percentage
- `get_light()` - This returns the level of light in Lux
- `get_cpu_temperature()` - This returns the CPU temperature of a RPi, useful in compensating the `get_temperature()` function.

------------

## Test Plan

<div align="center">

|Objective|Testing Strategy|Expected Output|Current Output|Pass/Fail|
|--|--|--|--|:--:|
|Testing the functionality of the Temperature sensor.|Log the temperature sensors value continuously to the terminal and wait for it to equalise to room temperature. Then check the value against a thermometer and heat the sensor up with a flame for 10 seconds. Finally wait for it to return to room temperature |The sensor should display room temperature at first which should be roughly the same as the reading from the thermometer, then the reading should increase rapidly when next to the flame before coming back down to the previous value.|The temperature reading does start at room temperature which does match the reading from the thermometer. When the flame is next to the sensor the temperature value does increase before settling back to room temp when the flame is removed.|:heavy_check_mark:|
|Testing the functionality of the Particulates sensor.|Switch the sensor on and set the sensor to log the values to the console. Then spray an aerosol for 5 seconds.|The value should settle down to some constants, once that aerosol has been sprayed the PM10 and PM2.5 particles should increase dramatically for a while before settling down back to the old constants |The sensor does settle to a baseline, when the aerosols is sprayed the sensor values increase dramatically before settling back down to the original baseline.|:heavy_check_mark:|
|Testing the functionality of the Pressure sensor.|Switch the sensor on and log its value to the console|The expected output should be around 1,013.25 hPa|The value given by the sensor is about that value and changes very little|:heavy_check_mark:|
|Testing the functionality of the Humidity sensor.|Switch the sensor on and log its value to the console. This should be done outside.|The value from the sensor should roughly equal to the value found from weather sites of the testing area|The value does match the expected output within a few percentage points.|:heavy_check_mark:|
|Testing the functionality of the Light sensor.|Set the sensor to continuously log its reading into the console. The use a torch to test the sensor readings. |When the torch is shining the sensors Lux reading should increase and will continue to increase the closer the light source is to the sensor.|The sensor behaves as expected, when the torch is on the reading increases and the closer the torch is to the sensor the higher the Lux reading|:heavy_check_mark:|
|Testing the functionality of the Gas sensor.|As we can not test the gas sensor in a safe manor with the facilities we have access to, this sensor will not be tested but rather the raw readings will be taken as is for the demonstration.|*n/a*|*n/a*|:cross_mark:|

</div>

------------

## Installation

**Step 1** : Clone the repo to the target device, If you have git installed you can do so by running the following.

```
git clone https://github.com/lboroWMEME-TeamProject/EnviroSensor
```

**Step 2** : Install the Python dependencies and setup the required peripherals using the supplied install script.

```
sudo ./install.sh
```

**Setp 3** : Reboot the system to apply the changes
```
sudo reboot
```

Once the system reboots you should be able to run `Enviro+.py` without problems.

------------

## Deployment

Deployment is easy once the installation is complete. You can copy the `Enviro+.py` file to your project directory and import the `Enviro` class. You can then create an object of the class and call the functions to get the data from the sensors.

A testing example is provided below and can be found in the `Enviro+.py` file.

```
## [Testing]

# Creating the Enviro object
enviro = Enviro()

while True:

    # Getting the Light data
    light_data = enviro.get_light()

    # Printing the data to console
    print(str(light_data))

    # Sleeping not to overload the sensors
    sleep(0.1)

```

for a full list of all member functions and their parameters see the `Enviro.py` file, or the [Code Overview](#Code-Overview) section.


------------
