import unicornoverdrive as unicorn

import time, colorsys, random

def color_ambient(cval, flow = 50):
    while True:
	rr = range(cval-flow, cval) + range(cval, cval-flow,-1)
        for z in rr:
            for y in range(8):
                for x in range(8):
                    #rgb = colorsys.hsv_to_rgb(z/360.0,1,random.choice(vs))
                    rgb = colorsys.hsv_to_rgb(z/360.0,1,1)
                    r = int(rgb[0]*255.0)
                    g = int(rgb[1]*255.0)
                    b = int(rgb[2]*255.0)
                    unicorn.set_pixel(x,y,r,g,b)
            unicorn.show()
            time.sleep(0.4)