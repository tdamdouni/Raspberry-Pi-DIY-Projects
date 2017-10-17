#!/usr/bin/env python

# https://forums.pimoroni.com/t/unicorn-hat-cpu-status-indicator/6150

# Import the relevant modules
import unicornhat as uh
try:
    import psutil
except ImportError:
    exit("This script requires psutil.n\Install with: sudo pip install psutil")

# Set the brightness of the UnicornHAT - 1.0 is blindingly bright!
uh.brightness(0.5)

# Run in an infinite loop and display relevant colour on the UnicornHAT.
# Create your own 10 step gradient via http://www.perbang.dk/rgbgradient/
while True:
    cpu_raw = psutil.cpu_percent(interval=1)
    cpu = int(cpu_raw)
    #print cpu      # Uncomment out to show CPU usage in the terminal
    if cpu < 10:
        uh.set_all(0,255,0)         # Green
        uh.show()
    elif (cpu > 11) and (cpu < 20):
        uh.set_all(56,255,0)
        uh.show()
    elif (cpu > 21) and (cpu < 30): # Lime
        uh.set_all(113,255,0)
        uh.show()
    elif (cpu > 31) and (cpu < 40):
        uh.set_all(170,255,0)
        uh.show()
    elif (cpu > 41) and (cpu < 50): # Yellow
        uh.set_all(226,255,0)
        uh.show()
    elif (cpu > 51) and (cpu < 60):
        uh.set_all(255,226,0)
        uh.show()
    elif (cpu > 61) and (cpu < 70): # Orange
        uh.set_all(255,170,0)
        uh.show()
    elif (cpu > 71) and (cpu < 80):
        uh.set_all(255,113,0)
        uh.show()
    elif (cpu > 81) and (cpu < 90):
        uh.set_all(255,56,0)
        uh.show()
    else:
        uh.set_all(255,0,0)         # Red
        uh.show()
