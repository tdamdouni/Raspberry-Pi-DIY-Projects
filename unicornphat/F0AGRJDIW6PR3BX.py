#!/usr/bin/env python

# https://www.hackster.io/masteruan/play-with-raspberry-pi-zero-and-phat-140b9a

import sys
import time
from subprocess import PIPE, Popen
import os

try:
    import psutil
except ImportError:
    sys.exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

import scrollphat

scrollphat.set_brightness(20)

cpu_temp = 0

def get_cpu_temperature():
    process = os.popen('vcgencmd measure_temp').readline()
    return (process.replace("temp=","").replace("'C\n",""))

while True:
    try:
        cpu_temp = int(float(get_cpu_temperature()))
        print (cpu_temp)
        scrollphat.write_string(str(cpu_temp)+"C")
        time.sleep(3)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
