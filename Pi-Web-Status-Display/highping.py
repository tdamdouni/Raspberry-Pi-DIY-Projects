#!/usr/bin/env python

from __future__ import print_function
import os
import os.path
import time
#from Adafruit_CharLCD import Adafruit_CharLCD

os.environ['TZ'] = 'PST+08PDT,M4.1.0,M10.5.0'
time.tzset()

#include this program in another python script using `import highping` and then call the main function (and pass in arguements) using highping.main()
def main(ping):
    if ping > 100:
        fileWrite(ping)


def fileWrite(ping):
    ping = str(ping)
    
    f = open('/home/pi/Pi-Web-Status-Display/highpings.txt', 'a')
    print(time.strftime("%c") + " -- Ping : " + ping + "ms", file=f)
    print(time.strftime("%c") + " -- Ping : " + ping + "ms")
    f.close()
    
    currentTime = str(time.time( ))
    
    f = open('/home/pi/Pi-Web-Status-Display/highpings.csv', 'a')
    print(currentTime + ", " + ping, file=f)
    print(currentTime + ", " + ping)
    f.close()
