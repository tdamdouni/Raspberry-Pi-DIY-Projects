#!/usr/bin/python

from datetime import datetime, timedelta
import random
import sys
from time import sleep

import unicornhat as unicorn

demo = len(sys.argv) > 1 and sys.argv[1] == "--demo"
delay = 0.01
brightness = 0.3
rotation = 180
display = []
colors = [
    [0, 0, 0],
    [255, 255, 0],
    [0, 0, 255],
    [255, 0, 0],
]

    
def set(x, y, val):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return
    display[x][y] = val

def get(x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return
    return display[x][y]

def dot(col, color=1, step=1, start=-1, stop=7, squash=False):
    x = col
    y = start
    while True:
        nextdot = get(x, y + step)
        if not squash and nextdot > 0:
            break
        if squash and nextdot == color:
            break
        set(x, y, 0)
        y += step
        set(x, y, color)
        render()
        if y == stop:
            break
        sleep(delay)

def add_sand():
    cols = []
    for x in xrange(7):
        if get(x, 0) == 0:
            cols += [x]
    if len(cols) == 0:
        return False
    col = random.choice(cols)
    dot(col, color=1)
    return True

def remove_sand():
    cols = []
    for x in xrange(7):
        if get(x, 0) > 0:
            cols += [x]
    if len(cols) == 0:
        return False
    col = random.choice(cols)
    start = 0
    while get(col, start + 1) > 0:
        start += 1
    dot(col, color=1, start=start, stop=8, step=1)
    return True


def add_hour(hour):
    if hour == 0:
        clear_hours()
    elif hour % 5 == 0:
        dot(7, color=3, squash=True)
    else:
        dot(7, color=2)

def _fill_hours():
    for _ in xrange(4):
        dot(7, color=3, delay=0.01)
    for _ in xrange(3):
        dot(7, color=2, delay=0.01)
        
def clear_hours():
    for y in xrange(7, -1, -1):
        color = get(7, y)
        if color == 0:
            return
        dot(7, color=color, start=y, stop=8, step=1)

def render():
    for x in range(8):
        for y in range(8):
            c = colors[display[x][y]]
            unicorn.set_pixel(x, y, c[0], c[1], c[2])
    unicorn.show()

def fill(color=1):
    for x in xrange(7):
        for y in xrange(8):
            set(x, y, color)
    render()

def sand_frame(date):
    fmin = date.minute + (date.second / 60.0)
    pct = fmin / 60.0
    max_frames = (2 * (8 * 7)) + 1
    return int(pct * max_frames)


for x in range(8):
    display += [[0] * 8]

unicorn.clear()
unicorn.brightness(brightness)
unicorn.rotation(180)

was = datetime.now()
if demo:
    now = datetime(2016, 12, 30, 0, 0, 0)
    was = now
    delay = 0.001

frame = 0
hour = 0

while True:
    now = now + timedelta(seconds=10) if demo else datetime.now()
    if now < was or now - was > timedelta(minutes=5):
        delay = 0.001
    was = now
    current = sand_frame(now)

    while frame != current:
        if frame <= (8 * 7):
            add_sand()
        else:
            remove_sand()
        frame += 1
        if frame > 112:
            frame = 0
            fill(0)

    current_hour = now.hour
    while current_hour != hour:
        hour += 1
        if hour >= 24:
            hour = 0
        add_hour(hour)

    if not demo:
        delay = 0.1
        sleep(0.1)

    

