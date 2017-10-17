# Adapted from blinkt example
import math
import time

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

from mote import Mote
mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)


def show_graph(v, r, g, b):
    v *= 8
    for x in range(8):
        if v  < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v,1.0) * c) for c in [r,g,b]]
        mote.set_pixel(1,x, r, g, b)
        v -= 1

    mote.show()


try:
    while True:
        v = psutil.cpu_percent() / 100.0
        show_graph(v, 255, 0, 255)
        time.sleep(0.01)

except KeyboardInterrupt:
	mote.clear()
	mote.show()
	quit()
