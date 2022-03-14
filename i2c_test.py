from machine import Pin, I2C

i2c = I2C(0,scl=Pin(1),sda=Pin(0))

devices = i2c.scan()

# print address of all devices connected to the i2c bus
if devices:
    for d in devices:
        print(hex(d))

