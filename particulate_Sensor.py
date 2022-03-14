from machine import UART, Pin
from time import sleep
from math import floor


buff = ["a"]*64
uart = UART(0,9600)


def data_process(a):

    # Is Valid Data
    temp = ['']*30
    Data = [0]*13

    if a[2] == str('B') and a[3] == str('M') and len(a) < 150:
        IndexDat = 0
        IndexBuff = 0
        
        # Loop data and filter into list
        for char in a:
            if char == str('x') and IndexDat < len(temp):
                try:          
                    temp[IndexDat] = a[IndexBuff+1] + a[IndexBuff+2]
                except IndexError:  # Error Handling which should not happen
                    print("IndexError")

                IndexDat = IndexDat + 1

            IndexBuff = IndexBuff + 1
    else:
        return

    print(a)
    var = "G"
    # Split output into data array
    for i in range(len(temp) - 4):
        if i%2 == 0:
            var = temp[i+2]
        else:
            var = var + temp[i+2]
            #print(var)
            Data[int(floor(i/2))] = int(var,16)
    #print(temp)
    print(Data)

# Test Loop
for i in range(10):
    # Data Collection
    Buff = str(uart.readline())
    sleep(0.1)
    #print(int("0x9a"))
    data_process(Buff)

