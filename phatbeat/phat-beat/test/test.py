#!/usr/bin/env python

import sys
import time

import phatbeat


@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin):
    print("Fast Forward pressed!")
@phatbeat.on(phatbeat.BTN_REWIND)
def fast_forward(pin):
    print("Rewind pressed!")
@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def fast_forward(pin):
    print("Play/Pause pressed!")
@phatbeat.on(phatbeat.BTN_VOLUP)
def fast_forward(pin):
    print("Volume Up pressed!")
@phatbeat.on(phatbeat.BTN_VOLDN)
def fast_forward(pin):
    print("Volume Down pressed!")
@phatbeat.on(phatbeat.BTN_ONOFF)
def fast_forward(pin):
    print("Power On/Off  pressed!")
    phatbeat.clear()
    phatbeat.show()
    sys.exit("exiting...")

try:
    while True:
        phatbeat.set_all(0,128,0,0.1,channel=0)
        phatbeat.set_all(255,155,0,0.1,channel=1)
        phatbeat.show()
        time.sleep(1)

except KeyboardInterrupt:
    pass
