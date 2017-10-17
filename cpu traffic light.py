# CPU utilization traffic light - TB 2016
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


def show_graph(v):
    v *= 16
    for x in range(16):
        if (v  < 0):
            r, g, b = 0, 0, 0
        elif (x < 9):
            #green
            r, g, b = 0, 128 , 0
        elif (x >= 9) and (x < 13):
            #orange
            r, g, b = 255, 99, 0        
        elif (x >= 13) and (x < 16):
            #red
            r, g, b = 255, 0, 0
            
        mote.set_pixel(1,x, r, g, b)
        v -= 1

    mote.show()

try:
    while True:
        v = psutil.cpu_percent() / 100
        show_graph(v)
        time.sleep(0.01)    


except KeyboardInterrupt:
	mote.clear()
	mote.show()
	time.sleep(0.1)
