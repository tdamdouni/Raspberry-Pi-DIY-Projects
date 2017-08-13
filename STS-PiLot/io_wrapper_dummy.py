#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:56:25 2017

@author: Mark Dammer

This is a hardware independent replacement for the original io_wrapper.py.
It does not interface to any specific IO board, but returns random values for
the sensors and prints the output values to the console.
"""
from __future__ import division
import random

explorerhat = False

# Inputs: Digital

def input_one_read():
    digital = bool(random.getrandbits(1))
    return digital

def input_two_read():
    digital = bool(random.getrandbits(1))
    return digital

def input_three_read():
    digital = bool(random.getrandbits(1))
    return digital

def input_four_read():
    digital = bool(random.getrandbits(1))
    return digital

# Inputs: Analog

def analog_one_read():
    analog = random.randrange(0, 5000) / 1000
    return analog

def analog_two_read():
    analog = random.randrange(0, 5000) / 1000
    return analog

def analog_three_read():
    analog = random.randrange(0, 5000) / 1000
    return analog

def analog_four_read():
    analog = random.randrange(0, 5000) / 1000
    return analog

# Outputs: Motors

def motor_one_speed(speed):
    print('Motor One: ' + str(speed))
    return

def motor_two_speed(speed):
    print('Motor Two: ' + str(speed))
    return

# Outputs: Digital

def output_one_on():
    print('Output One On')
    return

def output_one_off():
    print('Output One Off')
    return

def output_two_on():
    print('Output Two On')
    return

def output_two_off():
    print('Output Two Off')
    return

def output_three_on():
    print('Output Three On')
    return

def output_three_off():
    print('Output Three Off')
    return

def output_four_on():
    print('Output Four On')
    return

def output_four_off():
    print('Output Four Off')
    return

# Outputs: LEDs

def light_blue_on():
    print('Light Blue On')
    return

def light_blue_blink(freq):
    print('Light Blue Blink: ' + str(freq))
    return

def light_blue_off():
    print('Light Blue Off')
    return

def light_yellow_on():
    print('Light Yellow On')
    return

def light_yellow_blink(freq):
    print('Light Yellow Blink: ' + str(freq))
    return

def light_yellow_off():
    print('Light Yellow Off')
    return

def light_red_on():
    print('Light Red On')
    return

def light_red_blink(freq):
    print('Light Red Blink: ' + str(freq))
    return

def light_red_off():
    print('Light Red Off')
    return

def light_green_on():
    print('Light Green On')
    return

def light_green_blink(freq):
    print('Light Green Blink: ' + str(freq))
    return

def light_green_off():
    print('Light Green Off')
    return