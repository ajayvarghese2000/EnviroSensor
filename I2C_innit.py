from machine import Pin
from i2c_responder import I2CResponder as I2C
from time import sleep

i2c = I2C(0,sda_gpio=0,scl_gpio=1, responder_address=0x4C)

data=[6,6,3,2,1,6645,0,0,66696,2]
while True:
    if i2c.read_is_pending():
        i2c.put_read_data("33")
        print("sent")
       
    

