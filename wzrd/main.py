import adafruit_thermistor
import analogio
import board
import neopixel
import time
import wzrd
import urandom

import WizardRing

# Initial setup:
brightness_high = 0.2
brightness_low = 0.05
offset = 0
pixel_off = (0, 0, 0);
color = (60, 60, 60);
tick_duration = 0.01

# https://github.com/adafruit/Adafruit_CircuitPython_Thermistor
thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

random_pin = analogio.AnalogIn(board.A4)

photocell = analogio.AnalogIn(board.A8)
def photocell_value(input):
    return input.value * 330 // (2 ** 16)

ext_pixels = WizardRing.WizardRing(board.A3, 24, 6)
onboard_pixels = WizardRing.WizardRing(board.NEOPIXEL, 10, 5)

last_temp = thermistor.temperature
last_photocell = photocell_value(photocell)
last_colorswitch = 0
while True:
    t = time.monotonic()
    ext_pixels.animate()
    onboard_pixels.animate()

    # Check inputs and see if we should switch colors every 5 secs:
    switch = False
    if (t - last_colorswitch) > 5:
        current_photocell = photocell_value(photocell)
        if abs(last_photocell - current_photocell) > 10:
            onboard_pixels.set_color(ext_pixels.get_color())
            urandom.seed(random_pin.value)
            ext_pixels.randomize_color()
            switch = True
        last_photocell = current_photocell
        # print(last_photocell, current_photocell)

        current_temp = thermistor.temperature
        if abs(last_temp - current_temp) > 1:
            onboard_pixels.set_color(wzrd.get_color_for_temp(thermistor.temperature))
            switch = True
        last_temp = current_temp
        # print(last_temp, current_temp)

    if switch:
        last_colorswitch = t

    time.sleep(tick_duration)
