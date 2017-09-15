#!/usr/bin/env python

# https://www.hackster.io/masteruan/play-with-raspberry-pi-zero-and-phat-140b9ap

import time
import random
import scrollphat


scrollphat.set_brightness(10)
values = [0,0,0,0,0,0,0,0,0,0,0]

while True:
    print("Generating random")  
    for i in range(0,11):
       values[i] = random.randint(0,5)
    print values
    scrollphat.graph(values,0,5)
    time.sleep(0.2)
    scrollphat.clear()
