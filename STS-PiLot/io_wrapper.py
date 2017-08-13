#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:56:25 2017

@author: Mark Dammer
"""

import explorerhat as xhat

explorerhat = True

# Inputs: Digital

def input_one_read():
    digital = xhat.input.one.read()
    return digital

def input_two_read():
    digital = xhat.input.two.read()
    return digital

def input_three_read():
    digital = xhat.input.three.read()
    return digital

def input_four_read():
    digital = xhat.input.four.read()
    return digital

# Inputs: Analog

def analog_one_read():
    analog = xhat.analog.one.read()
    return analog

def analog_two_read():
    analog = xhat.analog.two.read()
    return analog

def analog_three_read():
    analog = xhat.analog.three.read()
    return analog

def analog_four_read():
    analog = xhat.analog.four.read()
    return analog

# Outputs: Motors

def motor_one_speed(speed):
    xhat.motor.one.speed(speed)
    return

def motor_two_speed(speed):
    xhat.motor.two.speed(speed)
    return

# Outputs: Digital

def output_one_on():
    xhat.output.one.on()
    return

def output_one_off():
    xhat.output.one.off()
    return

def output_two_on():
    xhat.output.two.on()
    return

def output_two_off():
    xhat.output.two.off()
    return

def output_three_on():
    xhat.output.three.on()
    return

def output_three_off():
    xhat.output.three.off()
    return

def output_four_on():
    xhat.output.four.on()
    return

def output_four_off():
    xhat.output.four.off()
    return

# Outputs: LEDs

def light_blue_on():
    xhat.light.blue.on()
    return

def light_blue_blink(freq):
    xhat.light.blue.blink(freq)
    return

def light_blue_off():
    xhat.light.blue.off()
    return

def light_yellow_on():
    xhat.light.yellow.on()
    return

def light_yellow_blink(freq):
    xhat.light.yellow.blink(freq)
    return

def light_yellow_off():
    xhat.light.yellow.off()
    return

def light_red_on():
    xhat.light.red.on()
    return

def light_red_blink(freq):
    xhat.light.red.blink(freq)
    return

def light_red_off():
    xhat.light.red.off()
    return

def light_green_on():
    xhat.light.green.on()
    return

def light_green_blink(freq):
    xhat.light.green.blink(freq)
    return

def light_green_off():
    xhat.light.green.off()
    return