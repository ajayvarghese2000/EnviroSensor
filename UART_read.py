from machine import UART, Pin
from time import sleep
#uarttx = Pin(0,Pin.ALT)
#uartrx = Pin(1,Pin.ALT)
enable = Pin(2, Pin.OUT)
reset = Pin(3, Pin.OUT)

uart = UART(0,9600)
i = 0
enable.high()
reset.high()

while True:
    #Buff = uart.readline()
    print(i, uart.readline())
    sleep(1)
    i = i+1
