from sense_hat import SenseHat
import time
import random

sense = SenseHat()

r = random.randint(0,255)
sense.show_letter("O",text_colour=[r,0,0])
time.sleep(1)

r = random.randint(0,255)
sense.show_letter("M",text_colour=[0,0,r])
time.sleep(1)

r = random.randint(0,255)
sense.show_letter("G",text_colour=[0,r,0])
time.sleep(1)

sense.show_letter("!",text_colour=[0,0,0],back_colour=[255,255,255])
time.sleep(1)
sense.clear()
