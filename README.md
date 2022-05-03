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
- `get_cpu_temperature()` - This returns the CPU temperature of a RPi, usefull in compensating the `get_temperature()` function.

------------

## Test Plan

*to be added*

<div align="center">

|Objective|Testing Strategy|Expected Output|Current Output|Pass/Fail|
|--|--|--|--|:--:|

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



------------
