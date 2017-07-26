#!/usr/bin/env python3

# Peter Simonyi  1 June 2012

import time
from itertools import izip_longest as zip_longest
from datetime import datetime
from pytz import timezone

england = timezone('Europe/London')

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

#unicornPHAT things

import unicornhat as u

u.set_layout(u.PHAT)
u.brightness(0.3)
u.rotation(180)

binaryDict = {'1': (255,255,255), '0': (0,0,0)}
hours = {'1': (255,0,0), '0': (0,0,0)}
mins = {'1': (0,255,0), '0': (0,0,0)}
secs = {'1': (0,0,255), '0': (0,0,0)}
white = (0,0,0)

while True:
    Now = datetime.now(england).strftime('%H%M%S')
    Time = main()

    matrix = [
        [hours[Time.split()[0][0]], hours[Time.split()[0][1]], white, mins[Time.split()[0][2]], mins[Time.split()[0][3]], white, secs[Time.split()[0][4]], secs[Time.split()[0][5]]],
        [hours[Time.split()[1][0]], hours[Time.split()[1][1]], white, mins[Time.split()[1][2]], mins[Time.split()[1][3]], white, secs[Time.split()[1][4]], secs[Time.split()[1][5]]],
        [hours[Time.split()[2][0]], hours[Time.split()[2][1]], white, mins[Time.split()[2][2]], mins[Time.split()[2][3]], white, secs[Time.split()[2][4]], secs[Time.split()[2][5]]],
        [hours[Time.split()[3][0]], hours[Time.split()[3][1]], white, mins[Time.split()[3][2]], mins[Time.split()[3][3]], white, secs[Time.split()[3][4]], secs[Time.split()[3][5]]],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    ]

    u.set_pixels(matrix)
    u.show()

    time.sleep(1)
