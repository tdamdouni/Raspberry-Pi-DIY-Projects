#!/usr/bin/env python
#===============================================================================
# clock.py
#
# Simple clock demo.
#
# 2014-09-12
# Carter Nelson
#===============================================================================
import time

from rpi_weather import RpiWeather
from led8x8icons import LED8x8ICONS as ICONS

display = RpiWeather()

def time2int(time_struct, format24=False):
    """Convert time, passed in as a time.struct_time object, to an integer with
    hours in the hundreds place and minutes in the units place. Returns 24
    hour format if format24 is True, 12 hour format (default) otherwise.
    """
    if not isinstance(time_struct, time.struct_time):
        return None
    h = time_struct.tm_hour
    m = time_struct.tm_min
    if not format24:
        h = h if h <= 12 else h - 12
    return h*100+m

def update_display(new_val, old_val):
    """Update the display, one digit at a time, where values differ."""
    if not (isinstance(new_val, int) and isinstance(old_val, int)):
        return
    if new_val == old_val:
        return
    for i in xrange(3,-1,-1):
        new_d = new_val % 10
        old_d = old_val % 10
        if i == 0 and new_d == 0:
            # removes zero padding
            display.scroll_raw64(ICONS['ALL_OFF'], i)           
        elif new_d != old_d:
            display.scroll_raw64(ICONS['{0}'.format(new_d)], i)
        new_val /= 10
        old_val /= 10

#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
old_val = time2int(time.localtime())
display.disp_number(old_val)
while True:
    """Loop forever, updating every 2 seconds."""
    new_val = time2int(time.localtime())
    update_display(new_val, old_val)
    old_val = new_val
    time.sleep(2)
