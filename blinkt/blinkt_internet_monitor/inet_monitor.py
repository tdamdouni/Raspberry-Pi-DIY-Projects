#!/usr/bin/env python
"""
Code adapted from https://github.com/pimoroni/blinkt

Plays happy lights on your blinkt as long as you can resolve DNS.

Plays angry red lights on your blinkt when you can't.

Install into "/home/pi/Pimoroni/blinkt/examples" after installing blinkt from
the link above.

Launch on boot by adding the following to "crontab -e":
@reboot python /home/pi/Pimoroni/blinkt/examples/inet_monitor.py &

Kill via shutdown script with:
pgrep -f /home/pi/Pimoroni/blinkt/examples/inet_monitor.py | xargs kill -SIGINT

Tested on Rpi3 with Pimoroni blinkt with Raspbian GNU/Linux 8 (jessie).

Date:   08/16
Author:  randomInteger
"""
import colorsys
import signal
import random
import socket
import time
import sys
from blinkt import set_brightness, set_pixel, show

def signal_handler(signal, frame):
    """
    This signal handler allows us to background
    the process and send it a simple SIGINT to tell it to
    exit cleanly.
    """
    sys.exit(0)

#Start the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

spacing = 360.0 / 16.0
hue = 0
set_brightness(0.1)
hostname = 'google.com'

while True:
    #Test for the ability to open a socket and resolve DNS.
    try:
        socket.gethostbyname(hostname)
        dns = True
    except socket.gaierror as e:
        dns = False

    x = 0
    while x < 50:
        if dns:
            #We have internet, play the happy lights.
            for i in range(8):
                set_pixel(i, random.randint(0,255), random.randint(0,255), random.randint(0,255))
        else:
            #DNS and/or internet services are down, play the angry lights
            for i in range(8):
                set_pixel(i, 255, 0, 0)
        show()
        x += 1
        time.sleep(0.10)
