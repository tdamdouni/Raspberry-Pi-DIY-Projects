from sense_hat import SenseHat

sense = SenseHat()

while True:
    sense.show_message("Astro Pi is awesome!!", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
