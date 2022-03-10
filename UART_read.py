from machine import UART, Pin
from time import sleep
#uarttx = Pin(0,Pin.ALT)
#uartrx = Pin(1,Pin.ALT)

# Initialisation of pins
enable = Pin(2, Pin.OUT)
reset = Pin(3, Pin.OUT)
buff = ["a"]*64
uart = UART(0,9600)
i = 0
enable.high()
reset.high()

# Start of loops
while i<10:
    # Data Collection
    Buff = str(uart.readline())
    print(i, Buff)
    Dat = ['']*30
    
    # Data Processing
    if Buff[2] == str('B') and Buff[3] == str('M'):
        print("SUCCESS")
        indexj = 0
        indexk = 0
        
        # Loop data and filter into list
        for char in Buff:
            if char == str('x'):
                try:
                    Dat[indexj] = Buff[indexk+1] + Buff[indexk+2]
                except IndexError:
                    print("IndexError")
                indexj = indexj + 1
            indexk = indexk + 1
        print(Dat)
        
    else:
        print("FAIL", Buff[2], Buff[3])
    
    
    sleep(1)
    i = i+1
