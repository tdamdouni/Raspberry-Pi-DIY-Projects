#!/usr/bin/env python

import time
import scrollphathd
from subprocess import Popen, PIPE
from scrollphathd.fonts import font3x5

print("This example will display your Pi's CPU temperature in degrees celsius. Press Ctrl+C to exit.")


while True:
    # Get temp from vcgencmd in the format: "temp=XY.Z'C"
    # and reduce to the format "XYZC" for display
    temperature = Popen(["vcgencmd", "measure_temp"], stdout=PIPE)
    temperature = temperature.stdout.read().decode('utf-8')

    # Rempve "temp=" and the "." and "'" chars
    temperature = temperature[5:].replace("'", "").strip()

    scrollphathd.clear()
    scrollphathd.write_string(temperature, x=0, y=1, font=font3x5, brightness=0.5)
    scrollphathd.show()

    time.sleep(1)
