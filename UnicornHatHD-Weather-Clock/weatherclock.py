#!/usr/bin/env python

import pyowm
import time
from itertools import izip_longest as zip_longest
from datetime import datetime
from pytz import timezone
import unicornhathd as u

# WEATHER
owm = pyowm.OWM('YOUR API KEY HERE')
observation = owm.weather_at_place('YOUR LOCATION HERE')
w = observation.get_weather()

# TIME
england = timezone('Europe/London')

# CREATING BINARY CLOCK MATRIX (Code for binary clock by Peter Simyoni: gist.github.com/psimonyi/2856099)
def main():
    return(vertical_strings(bcd(Now)))

# bcd :: iterable(characters '0'-'9') -> [str]
def bcd(digits):
    'Convert a string of decimal digits to binary-coded-decimal.'
    def bcdigit(d):
        'Convert a decimal digit to BCD (4 bits wide).'
        # [2:] strips the '0b' prefix added by bin().
        return bin(d)[2:].rjust(4, '0')
    return (bcdigit(int(d)) for d in digits)

# vertical_strings :: iterable(str) -> str
def vertical_strings(strings):
    'Orient an iterable of strings vertically: one string per column.'
    iters = [iter(s) for s in strings]
    concat = ''.join
    return '\n'.join(map(concat,
                         zip_longest(*iters, fillvalue=' ')))

# UNICORN
u.rotation(270)
u.brightness(0.6)

# clock
def set_hours():
    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][0]) == 1:
            u.set_pixel(2,i,240,40,100)
            u.set_pixel(3,i,240,40,100)
            u.set_pixel(2,i+1,240,40,100)
            u.set_pixel(3,i+1,240,40,100)
        else:
            u.set_pixel(2,i,0,0,0)
            u.set_pixel(3,i,0,0,0)
            u.set_pixel(2,i+1,0,0,0)
            u.set_pixel(3,i+1,0,0,0)

    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][1]) == 1:
            u.set_pixel(4,i,240,40,100)
            u.set_pixel(5,i,240,40,100)
            u.set_pixel(4,i+1,240,40,100)
            u.set_pixel(5,i+1,240,40,100)
        else:
            u.set_pixel(4,i,0,0,0)
            u.set_pixel(5,i,0,0,0)
            u.set_pixel(4,i+1,0,0,0)
            u.set_pixel(5,i+1,0,0,0)

def set_mins():
    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][2]) == 1:
            u.set_pixel(6,i,40,240,130)
            u.set_pixel(7,i,40,240,130)
            u.set_pixel(6,i+1,40,240,130)
            u.set_pixel(7,i+1,40,240,130)
        else:
            u.set_pixel(6,i,0,0,0)
            u.set_pixel(7,i,0,0,0)
            u.set_pixel(6,i+1,0,0,0)
            u.set_pixel(7,i+1,0,0,0)

    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][3]) == 1:
            u.set_pixel(8,i,40,240,130)
            u.set_pixel(9,i,40,240,130)
            u.set_pixel(8,i+1,40,240,130)
            u.set_pixel(9,i+1,40,240,130)
        else:
            u.set_pixel(8,i,0,0,0)
            u.set_pixel(9,i,0,0,0)
            u.set_pixel(8,i+1,0,0,0)
            u.set_pixel(9,i+1,0,0,0)

def set_secs():
    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][4]) == 1:
            u.set_pixel(10,i,40,90,255)
            u.set_pixel(11,i,40,90,255)
            u.set_pixel(10,i+1,40,90,255)
            u.set_pixel(11,i+1,40,90,255)
        else:
            u.set_pixel(10,i,0,0,0)
            u.set_pixel(11,i,0,0,0)
            u.set_pixel(10,i+1,0,0,0)
            u.set_pixel(11,i+1,0,0,0)

    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][5]) == 1:
            u.set_pixel(12,i,40,90,255)
            u.set_pixel(13,i,40,90,255)
            u.set_pixel(12,i+1,40,90,255)
            u.set_pixel(13,i+1,40,90,255)
        else:
            u.set_pixel(12,i,0,0,0)
            u.set_pixel(13,i,0,0,0)
            u.set_pixel(12,i+1,0,0,0)
            u.set_pixel(13,i+1,0,0,0)

def set_time():
    set_hours()
    set_mins()
    set_secs()

# border
for i in range(0,16):
    if weather.lower() == 'rain':
        u.set_pixel(i,0,70,130,255)
        u.set_pixel(0,i,70,130,255)
        u.set_pixel(i,15,70,130,255)
        u.set_pixel(15,i,70,130,255)
    elif weather.lower() == 'clouds':
        u.set_pixel(i,0,160,160,170)
        u.set_pixel(0,i,160,160,170)
        u.set_pixel(i,15,160,160,170)
        u.set_pixel(15,i,160,160,170)
    elif weather.lower() == 'sunny':
        u.set_pixel(i,0,255,230,40)
        u.set_pixel(0,i,255,230,40)
        u.set_pixel(i,15,255,230,40)
        u.set_pixel(15,i,255,230,40)
    else:
        u.set_pixel(i,0,255,255,255)
        u.set_pixel(0,i,255,255,255)
        u.set_pixel(i,15,255,255,255)
        u.set_pixel(15,i,255,255,255)

#top and bottom bars
for i in range(3,13):
    u.set_pixel(i,2,255,255,255)
    u.set_pixel(i,13,255,255,255)

#temperature bar
def roundTo(x, base):
    return int(base * round(float(x)/base))

tempDots = roundTo(w.get_temperature('celsius')['temp'],5)/5

for i in range(0,tempDots):
    u.set_pixel(i+3,2,255,185,20)

#humidity bar
humidityDots = roundTo(w.get_humidity(),10)/10

for i in range(0,humidityDots):
    u.set_pixel(i+3,13,110,130,255)

count = 0

#do the things
while True:
    Now = datetime.now(england).strftime('%H%M%S')
    Time = main()
    set_time()

    count+=1

    if count == 4:
        w = observation.get_weather()

        tempDots = roundTo(w.get_temperature('celsius')['temp'],5)/5
        humidityDots = roundTo(w.get_humidity(),10)/10

        for i in range(0,tempDots):
            u.set_pixel(i+3,2,255,185,20)

        for i in range(0,humidityDots):
            u.set_pixel(i+3,13,110,130,255)

        count = 0

    u.show()
    time.sleep(1)






