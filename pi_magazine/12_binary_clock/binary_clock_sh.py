#!/usr/bin/env python

from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

year_color = (0, 255, 0)
month_color = (0, 0, 255)
day_color = (255, 0, 0)
hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundrefths_color = (127, 127, 0)
off = (0, 0, 0)

hat.clear()

def display_binary(value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x, row, color)
		else:
			hat.set_pixel(x, row, off)

while True:
	t = datetime.datetime.now()
	display_binary(t.year % 100, 0, year_color)
	display_binary(t.month, 1, month_color)
	display_binary(t.day, 2, day_color)
	display_binary(t.hour, 3, hour_color)
	display_binary(t.minute, 4, minute_color)
	display_binary(t.second, 5, second_color)
	display_binary(t.microsecond / 10000, 6, hundrefths_color)
	time.sleep(0.0001)