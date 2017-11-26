#!/usr/bin/env python

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
from mpd import MPDClient
import RPi.GPIO as GPIO
import time, textwrap

# Configure the GPIO pins
BUTTON_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup Display
device = ssd1306(port=1, address=0x3C)
small_font = ImageFont.truetype('FreeMono.ttf', 12)
large_font = ImageFont.truetype('FreeMono.ttf', 24)

# Setup MPC
mpc = MPDClient()
mpc.connect("localhost", 6600)   
num_stations = 0

current_station = 0 # index of the currebt station

# Display whatever infrmation is available. With luck, the
# station name and the song title
def display_info():
    station = mpc.currentsong()
    try:
        station_name = station['name'][0:9]
    except:
        station_name = str(current_station + 1) + ' ?'
    try:
        titles = textwrap.wrap(station['title'], 19)
        titles += [''] # so there are always 2
    except:
        titles = ['', '']
    display_message(station_name, titles[0], titles[1])
         
# Display a message on 3 lines, first line big font        
def display_message(top_line, line_2, line_3=''):
    global device
    with canvas(device) as draw:
        draw.text((0, 0),  top_line, font=large_font, fill=255)
        draw.text((0, 40),  line_2, font=small_font, fill=255)
        draw.text((0, 50),  line_3, font=small_font, fill=255)

try:
    mpc.play(current_station)
    while True:
        num_stations = int(mpc.status()['playlistlength'])
        if num_stations == 0:
            display_message('Error', 'add stations', '$mpc add {url}')
        elif GPIO.input(BUTTON_PIN) == False:
            current_station += 1
            if current_station == num_stations:
                current_station = 0
            mpc.play(current_station)
            time.sleep(0.2) # key debounce
        else:
            display_info()
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    mpc.close()              
    mpc.disconnect()