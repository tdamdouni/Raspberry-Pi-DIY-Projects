#!/usr/bin/env python

import colorsys
import time

import phatbeat


print("""
pHAT BEAT: Hue Control

Press the top (On/Off) button to turn the LEDs on/off.

Press Fast-Forward or Play/Pause to change the left bar colour.

Press Volume Up/Down to change the right bar colour.

Press Rewind to reset the bar colours.

Press Ctrl+C to exit!

""")

hue_l = 0
hue_r = 0
on = True

@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin):
    global hue_l

    print("FF Pressed")

    hue_l += 1
    hue_l %= 360

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def play_pause(pin):
    global hue_l

    print("PP Pressed")

    hue_l -= 1
    hue_l %= 360

@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin):
    global hue_r

    print("VU Pressed")

    hue_r += 1
    hue_r %= 360

@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin):
    global hue_r

    print("VD Pressed")

    hue_r -= 1
    hue_r %= 360

@phatbeat.on(phatbeat.BTN_REWIND)
def rewind(pin):
    global hue_l, hue_r

    print("RR Pressed")

    hue_l, hue_r = 0, 0

@phatbeat.on(phatbeat.BTN_ONOFF, repeat=False)
def onoff(pin):
    global on

    print("OO Pressed")

    on = not on

def set_channel_hue(channel, hue):
    
    r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
    phatbeat.set_all(r, g, b, channel=channel)

try:
    while True:
        if on:
            set_channel_hue(0, hue_l)
            set_channel_hue(1, hue_r)
        else:
            phatbeat.clear()

        phatbeat.show()

        time.sleep(0.01)

except KeyboardInterrupt:
    pass
