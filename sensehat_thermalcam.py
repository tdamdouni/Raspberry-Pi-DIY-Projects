"""
An adaptation of Adafruit's thermal camera example which
uses the sense hat to display temperatures.

Martin O'Hanlon
@martinohanlon
stuffaboutco.de
"""
from sense_hat import SenseHat
from Adafruit_AMG88xx import Adafruit_AMG88xx
from colour import Color
from time import sleep

COLORDEPTH = 1024
MINTEMP = 20
MAXTEMP = 30

sense = SenseHat()
sensor = Adafruit_AMG88xx()

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

try:
    while True:
        #read the pixels
        temps = sensor.readPixels()
        pixels = []
        for temp in temps:
            temp = max(MINTEMP, min(MAXTEMP, temp))
            
            #find the colour                             
            color_no = int((COLORDEPTH / (MAXTEMP - MINTEMP)) * (temp - MINTEMP))
            color = colors[color_no - 1]
            pixels.append(color)

        sense.set_pixels(pixels)
        sleep(0.1)
        
except KeyboardInterrupt as e:
        
    sense.clear()
