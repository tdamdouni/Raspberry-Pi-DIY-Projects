#!/usr/bin/env python

# Designed by Chris Butcher to overcome Three (3) Digit Limit
# On the ScrollPhat by Pimoroni

import scrollphat
import time, sys, os

# Using the 'set_pixel' command to create custom numbers allowing 
# four (4) number to fit ontop the 11x5 LED Matrix.

# This then calls the numbers as required by the 'strftime' module
# to display the clock on the LED Matrix

# The only addition was the centre flashing to simulate the seconds

# please see disclaimer at bottom of file

# Setup ScrollPhat for Brightness and Rotation
scrollphat.set_brightness(1)
scrollphat.rotate = True

# Centre Flashing Colon (ON)
def sec_gap_on():
    scrollphat.set_pixel(5,1,1)
    scrollphat.set_pixel(5,3,1)

# Centre Flashing Colon (OFF)
def sec_gap_off():
    scrollphat.set_pixel(5,1,0)
    scrollphat.set_pixel(5,3,0)


    
# First Digit Number List
def num_1_1():
    scrollphat.set_pixel(0,0,0)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,0)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,0)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,0)
    scrollphat.set_pixel(1,4,1)
    
def num_1_2():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,0)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,0)
    scrollphat.set_pixel(0,3,1)
    scrollphat.set_pixel(1,3,0)
    scrollphat.set_pixel(0,4,1)
    scrollphat.set_pixel(1,4,1)
    
def num_1_3():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,0)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,0)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,1)
    scrollphat.set_pixel(1,4,1)
    
def num_1_4():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,0)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,0)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,0)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,0)
    scrollphat.set_pixel(1,4,1)

def num_1_5():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,0)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,0)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,1)
    scrollphat.set_pixel(1,4,1)
    
def num_1_6():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,0)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,0)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,1)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,1)
    scrollphat.set_pixel(1,4,1)
    
def num_1_7():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,0)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,0)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,0)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,0)
    scrollphat.set_pixel(1,4,1)
    
def num_1_8():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,0)
    scrollphat.set_pixel(1,2,0)
    scrollphat.set_pixel(0,3,1)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,1)
    scrollphat.set_pixel(1,4,1)

def num_1_9():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,0)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,0)
    scrollphat.set_pixel(1,4,1)
    
def num_1_0():
    scrollphat.set_pixel(0,0,1)
    scrollphat.set_pixel(1,0,1)
    scrollphat.set_pixel(0,1,1)
    scrollphat.set_pixel(1,1,1)
    scrollphat.set_pixel(0,2,1)
    scrollphat.set_pixel(1,2,1)
    scrollphat.set_pixel(0,3,1)
    scrollphat.set_pixel(1,3,1)
    scrollphat.set_pixel(0,4,1)
    scrollphat.set_pixel(1,4,1)
    
    
    
# Second Digit Number List
def num_2_1():
    scrollphat.set_pixel(3,0,0)
    scrollphat.set_pixel(4,0,1)
    scrollphat.set_pixel(3,1,1)
    scrollphat.set_pixel(4,1,1)
    scrollphat.set_pixel(3,2,0)
    scrollphat.set_pixel(4,2,1)
    scrollphat.set_pixel(3,3,0)
    scrollphat.set_pixel(4,3,1)
    scrollphat.set_pixel(3,4,0)
    scrollphat.set_pixel(4,4,1)
    
def num_2_2():
    scrollphat.set_pixel(3,0,1)
    scrollphat.set_pixel(4,0,1)
    scrollphat.set_pixel(3,1,0)
    scrollphat.set_pixel(4,1,1)
    scrollphat.set_pixel(3,2,1)
    scrollphat.set_pixel(4,2,0)
    scrollphat.set_pixel(3,3,1)
    scrollphat.set_pixel(4,3,0)
    scrollphat.set_pixel(3,4,1)
    scrollphat.set_pixel(4,4,1)
    
def num_2_6():
    scrollphat.set_pixel(3,0,1)
    scrollphat.set_pixel(4,0,0)
    scrollphat.set_pixel(3,1,1)
    scrollphat.set_pixel(4,1,0)
    scrollphat.set_pixel(3,2,1)
    scrollphat.set_pixel(4,2,1)
    scrollphat.set_pixel(3,3,1)
    scrollphat.set_pixel(4,3,1)
    scrollphat.set_pixel(3,4,1)
    scrollphat.set_pixel(4,4,1)
    
def num_2_0():
    scrollphat.set_pixel(3,0,1)
    scrollphat.set_pixel(4,0,1)
    scrollphat.set_pixel(3,1,1)
    scrollphat.set_pixel(4,1,1)
    scrollphat.set_pixel(3,2,1)
    scrollphat.set_pixel(4,2,1)
    scrollphat.set_pixel(3,3,1)
    scrollphat.set_pixel(4,3,1)
    scrollphat.set_pixel(3,4,1)
    scrollphat.set_pixel(4,4,1)
    
    
   
# Third Digit Number List
def num_3_1():
    scrollphat.set_pixel(6,0,0)
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(6,1,1)
    scrollphat.set_pixel(7,1,1)
    scrollphat.set_pixel(6,2,0)
    scrollphat.set_pixel(7,2,1)
    scrollphat.set_pixel(6,3,0)
    scrollphat.set_pixel(7,3,1)
    scrollphat.set_pixel(6,4,0)
    scrollphat.set_pixel(7,4,1)
    
def num_3_2():
    scrollphat.set_pixel(6,0,1)
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(6,1,0)
    scrollphat.set_pixel(7,1,1)
    scrollphat.set_pixel(6,2,1)
    scrollphat.set_pixel(7,2,0)
    scrollphat.set_pixel(6,3,1)
    scrollphat.set_pixel(7,3,0)
    scrollphat.set_pixel(6,4,1)
    scrollphat.set_pixel(7,4,1)
    
def num_3_3():
    scrollphat.set_pixel(6,0,1)
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(6,1,0)
    scrollphat.set_pixel(7,1,1)
    scrollphat.set_pixel(6,2,1)
    scrollphat.set_pixel(7,2,1)
    scrollphat.set_pixel(6,3,0)
    scrollphat.set_pixel(7,3,1)
    scrollphat.set_pixel(6,4,1)
    scrollphat.set_pixel(7,4,1)
    
def num_3_4():
    scrollphat.set_pixel(6,0,1)
    scrollphat.set_pixel(7,0,0)
    scrollphat.set_pixel(6,1,1)
    scrollphat.set_pixel(7,1,0)
    scrollphat.set_pixel(6,2,1)
    scrollphat.set_pixel(7,2,1)
    scrollphat.set_pixel(6,3,0)
    scrollphat.set_pixel(7,3,1)
    scrollphat.set_pixel(6,4,0)
    scrollphat.set_pixel(7,4,1)

def num_3_5():
    scrollphat.set_pixel(6,0,1)
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(6,1,1)
    scrollphat.set_pixel(7,1,0)
    scrollphat.set_pixel(6,2,1)
    scrollphat.set_pixel(7,2,1)
    scrollphat.set_pixel(6,3,0)
    scrollphat.set_pixel(7,3,1)
    scrollphat.set_pixel(6,4,1)
    scrollphat.set_pixel(7,4,1)
    
def num_3_0():
    scrollphat.set_pixel(6,0,1)
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(6,1,1)
    scrollphat.set_pixel(7,1,1)
    scrollphat.set_pixel(6,2,1)
    scrollphat.set_pixel(7,2,1)
    scrollphat.set_pixel(6,3,1)
    scrollphat.set_pixel(7,3,1)
    scrollphat.set_pixel(6,4,1)
    scrollphat.set_pixel(7,4,1)
    
def num_3_():
    scrollphat.set_pixel(6,0,0)
    scrollphat.set_pixel(7,0,0)
    scrollphat.set_pixel(6,1,0)
    scrollphat.set_pixel(7,1,0)
    scrollphat.set_pixel(6,2,0)
    scrollphat.set_pixel(7,2,0)
    scrollphat.set_pixel(6,3,0)
    scrollphat.set_pixel(7,3,0)
    scrollphat.set_pixel(6,4,0)
    scrollphat.set_pixel(7,4,0)

    
    
# Fourth Digit Number List
def num_4_1():
    scrollphat.set_pixel(9,0,0)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,0)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,0)
    scrollphat.set_pixel(10,4,1)
    
def num_4_2():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,0)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,0)
    scrollphat.set_pixel(9,3,1)
    scrollphat.set_pixel(10,3,0)
    scrollphat.set_pixel(9,4,1)
    scrollphat.set_pixel(10,4,1)
  
def num_4_3():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,0)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,1)
    scrollphat.set_pixel(10,4,1)
    
def num_4_4():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,0)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,0)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,0)
    scrollphat.set_pixel(10,4,1)

def num_4_5():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,0)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,1)
    scrollphat.set_pixel(10,4,1)
    
def num_4_6():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,0)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,0)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,1)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,1)
    scrollphat.set_pixel(10,4,1)
    
def num_4_7():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,0)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,0)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,0)
    scrollphat.set_pixel(10,4,1)
    
def num_4_8():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,0)
    scrollphat.set_pixel(10,2,0)
    scrollphat.set_pixel(9,3,1)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,1)
    scrollphat.set_pixel(10,4,1)

def num_4_9():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,0)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,0)
    scrollphat.set_pixel(10,4,1)
    
def num_4_0():
    scrollphat.set_pixel(9,0,1)
    scrollphat.set_pixel(10,0,1)
    scrollphat.set_pixel(9,1,1)
    scrollphat.set_pixel(10,1,1)
    scrollphat.set_pixel(9,2,1)
    scrollphat.set_pixel(10,2,1)
    scrollphat.set_pixel(9,3,1)
    scrollphat.set_pixel(10,3,1)
    scrollphat.set_pixel(9,4,1)
    scrollphat.set_pixel(10,4,1)

  
# Adjusted 1/2 Second Delay       
delay = 0.397
    
    
# Pogram to Simulate the Clock, this will run until QUIT
while True:
    try:
        num_1_1()
        num_2_2()
        num_3_0()
        num_4_0()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_1()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_2()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_3()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_4()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_5()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_6()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_7()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_8()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_9()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        
        
        num_3_1()
        num_4_0()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_1()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_2()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_3()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_4()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_5()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_6()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_7()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_8()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_9()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        
        
        num_3_2()
        num_4_0()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_1()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_2()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_3()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_4()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_5()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_6()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_7()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_8()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_9()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        
        
        num_3_3()
        num_4_0()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_1()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_2()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_3()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_4()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_5()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_6()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_7()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_8()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_9()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        
        
        num_3_4()
        num_4_0()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_1()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_2()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_3()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_4()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_5()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_6()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_7()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_8()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_9()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        
        
        num_3_5()
        num_4_0()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_1()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_2()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_3()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_4()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_5()
        
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_6()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_7()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_8()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        num_4_9()
        sec_gap_on()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        sec_gap_off()
        
        time.sleep(0.1)
        scrollphat.update()
        
        time.sleep(delay)
        
        #sys.exit(-1)
        
    except KeyboardInterrupt:
        
        # Clears ScrollPhat and Screen on QUIT
        scrollphat.clear()
        os.system("clear")
        sys.exit(-1)
