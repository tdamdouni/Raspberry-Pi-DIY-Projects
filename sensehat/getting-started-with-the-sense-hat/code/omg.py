from sense_hat import SenseHat
import time

sense = SenseHat()

sense.show_letter("O",text_colour=[255,0,0])
time.sleep(1)
sense.show_letter("M",text_colour=[0,0,255])
time.sleep(1)
sense.show_letter("G",text_colour=[0,255,0])
time.sleep(1)
sense.show_letter("!",text_colour=[0,0,0],back_colour=[255,255,255])
time.sleep(1)
sense.clear()
