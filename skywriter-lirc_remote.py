#!/usr/bin/env python
import skywriter
import signal
from os import system
import time

some_value = 5000

last_airwheel = 0
delay = 5000

@skywriter.flick()
def flick(start,finish):
  if(start == "north" and finish == "south"):
    print "Volume: down"
    system("irsend SEND_ONCE TV KEY_VOLUMEDOWN")
  elif(start == "south" and finish == "north"):
    print "Volume: up"
    system("irsend SEND_ONCE TV KEY_VOLUMEUP")
  elif(start == "west" and finish == "east"):
    print "Channel: prev"
    system("irsend SEND_ONCE Digibox KEY_CHANNELDOWN")
  elif(start == "east" and finish == "west"):
    print "Channel: next"
    system("irsend SEND_ONCE Digibox KEY_CHANNELUP")
  else:
    print "Invalid"

@skywriter.airwheel()
def spinny(delta):
  global some_value
  global last_airwheel
  global delay
  some_value += delta
  if some_value < 0:
    some_value = 0
  if some_value > 10000:
    some_value = 10000
  now = int(round(time.time() * 1000))
  if(now - last_airwheel > delay):
    print("TV & Digibox: power")
    system("irsend SEND_ONCE TV KEY_POWER")
    system("irsend SEND_ONCE Digibox KEY_POWER")
    last_airwheel = now

signal.pause()