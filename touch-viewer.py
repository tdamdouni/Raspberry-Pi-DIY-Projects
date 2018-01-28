#!/usr/bin/env python2

# https://gist.github.com/Gadgetoid/8bc3bbbd64d7f96f585920eb1ef6abde

# HyperPixel Touchscreen Viewer

import time
import sys
import smbus
import pygame
from pygame.locals import *

ADDR = 0x5c

bus = smbus.SMBus(3)

WINDOW_SIZE = 10

ROWS = 8
COLS = 14

H = 480
W = 800

STEP_Y = float(H) / (ROWS - 1)
STEP_X = float(W) / (COLS - 1)

data = [[0] * WINDOW_SIZE] * (ROWS + COLS)

def read_byte(address, delay=0):
    return bus.read_byte_data(0x5c,address)

def smbus_read_touch():
    raw_adc = bus.read_i2c_block_data(ADDR, 0x00, 32) + bus.read_i2c_block_data(ADDR, 0x20, 12)
    adc_out = [0] * (ROWS + COLS)

    y = 0
    for x in range(0,len(raw_adc),2):
        val = (raw_adc[x] << 8) | raw_adc[x+1]
        data[y].insert(0, val)
        data[y] = data[y][:WINDOW_SIZE]
        y += 1

    for x in range(ROWS+COLS):
        val = 0
        for y in range(WINDOW_SIZE):
            val += data[x][y]
        adc_out[x] = int(val / WINDOW_SIZE)

    touch_x = list(reversed(adc_out[8:]))
    touch_y = adc_out[:8]

    #print(str(int(time.time() * 1000)) + " y: " + " ".join([str(x).rjust(4,' ') for x in touch_y]) + " | x: " + " ".join([str(x).rjust(4,' ') for x in touch_x]))
    touches = []
    found = []

    ignore_factor = 0.6

    while True:
        max_x = max(touch_x)
        max_y = max(touch_y)

        io_x = touch_x.index(max_x)
        io_y = touch_y.index(max_y)

        if max_x < 100 or max_y < 100 or (io_x, io_y) in found:
            break

        io_x = touch_x.index(max_x)
        io_y = touch_y.index(max_y)

        found.append((io_x, io_y))

        b_x = (STEP_X * io_x) # + STEP_X / 2
        b_y = (STEP_Y * io_y) # + STEP_Y / 2

        adc_x = touch_x[io_x]
        adc_y = touch_y[io_y]

        if io_x < (COLS-1):
            b_x -= 1.0 - (float(touch_x[io_x + 1]) / adc_x) * (STEP_X / 2)
            touch_x[io_x + 1] *= ignore_factor

        if io_x > 0:
            b_x += 1.0 - (float(touch_x[io_x - 1]) / adc_x) * (STEP_X / 2)
            touch_x[io_x - 1] *= ignore_factor

        if io_y < (ROWS-1):
            b_y -= 1.0 - (float(touch_y[io_y + 1]) / adc_y) * (STEP_Y / 2)
            touch_y[io_y + 1] *= ignore_factor

        if io_y > 0:
            b_y += 1.0 - (float(touch_y[io_y - 1]) / adc_y) * (STEP_Y / 2)
            touch_y[io_y - 1] *= ignore_factor

        touch_x[io_x] *= ignore_factor
        touch_y[io_y] *= ignore_factor

        touches.append((int(b_x), int(b_y), adc_x, adc_y))

    touches = sorted(touches, key=lambda touch: touch[0])
    #print(touches)
    return touch_x, touch_y, touches


def smbus_config_touch():
    bus.write_byte_data(0x5c,0x6e,0b00001110)

def text(screen, text, position, size, color):
    font = pygame.font.SysFont("droidsansmono", size)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    textpos.centerx, textpos.centery = position
    screen.blit(text, textpos)
    return textpos

DR_STATIC = 0
DR_TOUCH = 1

if __name__ == "__main__":
    pygame.init()
    margin_x = 100
    margin_y = 20
    screen = pygame.display.set_mode((W + margin_x, H + margin_y))
    pygame.mouse.set_visible(False)

    smbus_config_touch()

    dirty_rects = []

    while True:
        blanked_rects = []
        for rect in dirty_rects:
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                rect[1],
                0
            )
            if rect[0] == DR_TOUCH:
                blanked_rects.append((DR_STATIC, rect[1]))
        dirty_rects = blanked_rects

        touch_x, touch_y, touches = smbus_read_touch()

        touch_y = reversed(touch_y)
        for idx, value in enumerate(touch_y):
            offset_y = int(idx * (H / ROWS)) + (H / ROWS / 2)
            color = (0, 120, 0) if value > 100 else (120, 120, 120)
            rect = text(screen, "{:06.1f}".format(value), (30, offset_y), 20, color)
            dirty_rects.append((DR_STATIC, rect))

        for idx, value in enumerate(touch_x):
            offset_x = int(idx * (W / COLS)) + (W / COLS / 2)
            color = (0, 120, 0) if value > 100 else (120, 120, 120)
            rect = text(screen, "{:06.1f}".format(value), (margin_x + offset_x, 10), 20, color)
            dirty_rects.append((DR_STATIC, rect))

        for idx, touch in enumerate(touches):
            x, y, adc_x, adc_y = touch
            position = margin_x + x -1, margin_y + H - y - 1
            rect = (position, (2, 2))
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                rect,
                0
            )
            dirty_rects.append((DR_TOUCH, rect))
            position = position[0], position[1] + 10
            rect = text(screen, "{:d}={:06.1f}:{:06.1f}".format(idx+1, adc_x, adc_y), position, 30, (90, 90, 90))
            dirty_rects.append((DR_TOUCH, rect))

        pygame.display.update([rect[1] for rect in dirty_rects])

        time.sleep(1.0/240)