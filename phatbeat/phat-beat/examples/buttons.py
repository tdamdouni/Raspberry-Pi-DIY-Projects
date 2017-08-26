#!/usr/bin/env python

import signal

import phatbeat


print("""
pHAT BEAT: Buttons

Shows off the various ways you can configure buttons on PHAT BEAT.

Press Ctrl+C to exit!

""")

@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin):
    print("FF Pressed")

@phatbeat.hold(phatbeat.BTN_FASTFWD, hold_time=2)
def hold_fast_forward(pin):
    print("FF Held")

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def play_pause(pin):
    print("PP Pressed")

@phatbeat.hold(phatbeat.BTN_PLAYPAUSE, hold_time=2)
def hold_play_pause(pin):
    print("PP Held")

@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin):
    print("VU Pressed")

@phatbeat.hold(phatbeat.BTN_VOLUP)
def hold_volume_up(pin):
    print("VU Held")

@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin):
    print("VD Pressed")

@phatbeat.hold(phatbeat.BTN_VOLDN)
def hold_volume_down(pin):
    print("VD Held")

@phatbeat.on(phatbeat.BTN_REWIND)
def rewind(pin):
    print("RR Pressed")

@phatbeat.hold(phatbeat.BTN_REWIND)
def hold_rewind(btn):
    print("RR Held")

@phatbeat.on(phatbeat.BTN_ONOFF)
def onoff(pin):
    print("OO Pressed")

@phatbeat.hold(phatbeat.BTN_ONOFF)
def hold_onoff(pin):
    print("OO Held")

signal.pause()
