#! usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import time
import unicornhat as unicorn


### unicorn stuff
unicorn.set_layout(unicorn.PHAT)
unicorn.rotation(0)
unicorn.brightness(1)
width,height=unicorn.get_shape()


### calculate color from temperature
def calculate_color_from_kelvin(name):
    global r
    global g
    global b
    tmpKelvin = float(name)

    if tmpKelvin < 1000:
        tmpKelvin = 1000
    if tmpKelvin > 40000:
        tmpKelvin = 40000

    tmpKelvin = tmpKelvin / 100

    if tmpKelvin <= 66:
        r = 255
    else:
        tmpCalc = tmpKelvin - 60
        tmpCalc = 329.698727466 * (tmpCalc ** (-0.1332047592))
        r = tmpCalc
        if r < 0:
            r = 0
        if r > 255:
            r = 255

    if tmpKelvin <= 66:
        tmpCalc = tmpKelvin
        tmpCalc = 99.4708025861 * math.log(tmpCalc) - 161.1195681661
        g = tmpCalc
        if g < 0:
            g = 0
        if g > 255:
            g = 255
    else:
        tmpCalc = tmpKelvin - 60
        tmpCalc = 288.12216952383 * (tmpCalc ** (-0.0755148492))
        g = tmpCalc
        if g < 0:
            g = 0
        if g > 255:
            g = 255

    if tmpKelvin >= 66:
        b = 255
    elif tmpKelvin <= 19:
        b = 0
    else:
        tmpCalc = tmpKelvin - 10
        tmpCalc = 138.5177312231 * math.log(tmpCalc) - 305.0447927307
        b = tmpCalc
        if b < 0:
            b = 0
        if b > 255:
            b = 255
    r = round(r)
    g = round(g)
    b = round(b)
    return r, g, b



def set_phat_color(r,g,b):
    for x in range(0, 4):
        i = 0
        for i in range(0, 8):
            unicorn.set_pixel(i, x, r , g, b)
            unicorn.show()

def sunrise(delay=0, steps=20):
    unicorn.brightness(1)
    temperature = 1000
    while temperature < 5000:
        calculate_color_from_kelvin(temperature)
        set_phat_color(r, g, b)
        temperature += steps
        time.sleep(delay)
        print('\r Temperature: %s K;  Corresponding R,G,B = %s, %s, %s '%(temperature, r, g, b),end='',  flush = True)
    unicorn.off()




def main():
    sunrise(delay=2, steps=5)

if __name__ == "__main__":
    # execute only if run as a script
    main()
