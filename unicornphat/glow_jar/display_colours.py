from time import sleep
from colour import Color  # python module to do simple colour gradients -or however we want to spell it - color? colour?
from weather import *  # weather.py I wrote myself to fetch weather API info from MET office site

"""
# Uncomment this out when actually running on the Raspberry Pi
import unicornhat as unicorn
unicorn.set_layout(unicorn.PHAT) # mini hat
unicorn.brightness(0.5)
unicorn.rotation(0)
"""

# Make these global values to save calculating them each time
white = Color("white")
blue = Color("blue")
green = Color("green")
yellow = Color("yellow")
red = Color("red")

blue_to_white = list(blue.range_to(white, 11))
white_to_green = list(white.range_to(green, 11))
green_to_yellow = list(green.range_to(yellow, 11))
yellow_to_red = list(yellow.range_to(red, 11))

colours_range_total = blue_to_white + white_to_green[1:] + green_to_yellow[1:] + yellow_to_red[1:]
# Got to make sure we get rid of repeated fencepost colours


def temperature_to_hue(temperature):
    if temperature < -10:
        colour_choice = one_range_to_255_range(blue.rgb)
    elif temperature > 30:
        colour_choice = one_range_to_255_range(red.rgb)
    else:
        index = int(temperature) + 10
        colour_choice = one_range_to_255_range(colours_range_total[index].rgb)

    return colour_choice


def hue_to_RGB(hue_name):
    """ Take an RGB colour name and turn it into
    a tuple representation of that colour
    Eg hue_to_RGB("red") = (255, 0, 0)
    """
    colour_tuple = Color(hue_name)
    print(colour_tuple)
    result = one_range_to_255_range(colour_tuple.rgb)
    return result


def one_range_to_255_range(RGB_tuple):
    RGB = []
    for i in range(0, 3):
        result = int(RGB_tuple[i] * 255.0)
        RGB.append(result)
    vals = tuple(RGB)
    return vals


def show_colour_on_unicorn(RGB):
    width,height = unicorn.get_shape()
    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,RGB[0], RGB[1], RGB[2])
    unicorn.show()


def display_temperature_output_spectrum():
    print("Pooping temperature based rainbows")
    sleep(0.5)
    for i in range(-5, 35):
        sleep(1)
        print("Colour for temperature: {0} deg C".format(i))
        show_colour_on_unicorn(temperature_to_hue(i))
        sleep(1)


if __name__ == "__main__":
    # display_temperature_output_spectrum()
    Andrews_Field = "3684"  # Get data from here since it's closest to
    # my geographic location in Cambridge at the moment.
    print("I'm getting the latest temperature data measured at location {0}".format(Andrews_Field))
    latest_temp_history = extract_API_temperatures(get_MET_weather_observations(Andrews_Field))
    display_temp = extract_latest_temperature(latest_temp_history)
    print("Now displaying on Pi for your viewing pleasure.")
    show_colour_on_unicorn(temperature_to_hue(display_temp))
    sleep(60)