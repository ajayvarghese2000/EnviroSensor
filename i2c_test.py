from ure import I
from machine import Pin, I2C

i2c = I2C(0,scl=Pin(17),sda=Pin(16))

devices = i2c.scan()

if devices:
    for d in devices:
        print(hex(d))