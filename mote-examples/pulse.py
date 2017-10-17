# Adapted from blinkt example
from mote import Mote
import colorsys
import time

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)



try:
    import numpy as np
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")




def make_gaussian(fwhm):
    x = np.arange(0, 16, 1, float)
    y = x[:, np.newaxis]
    x0, y0 = 3.5, 7.5
    fwhm = fwhm
    gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss

try:
    while True:
        for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
            fwhm = 7.0/z
            gauss = make_gaussian(fwhm)
            start = time.time()
            y = 4
            for x in range(16):
                h = 0.5
                s = 1.0
                v = gauss[x, y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r, g, b = [int(255.0 * i) for i in rgb]
                mote.set_pixel(1,x, r, g, b)
                mote.set_pixel(2,x, r, g, b)
                mote.set_pixel(3,x, r, g, b)
                mote.set_pixel(4,x, r, g, b)
            mote.show()
            end = time.time()
            t = end - start
            if t < 0.04: time.sleep(0.04 - t)
            
except KeyboardInterrupt:
	mote.clear()
	mote.show()
	quit()

