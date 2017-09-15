#!/usr/bin/python
#--------------------------------------   
# This script reads data from a 
# HMC5883L 3-axis digital compass
# using the I2C bus.
#
# Author : Matt Hawkins
# Date   : 21/04/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import smbus
import time
import sys

# HMC5883L properties
DEVICE = 0x1e # Device address on I2C
REG_A  = 0    # Configuration Register A
REG_B  = 1    # Configuration Register B
REG_M  = 2    # Mode Register
REG_X  = 3    # X Output Register
REG_Y  = 7    # Y Output Register
REG_Z  = 5    # Z Output Register

SMBUS = 1 # Rev 1 Pi set this to 0

bus = smbus.SMBus(SMBUS) # Rev 2 Pi uses 1

def read_data(device,address):
  # Function to read data from specified register
  # Reads two 8 bit bytes and combines
  # Twos Complement conversion
  d1 = bus.read_byte_data(device, address)   # MSB
  d2 = bus.read_byte_data(device, address+1) # LSB
  d = (d1 << 8) + d2
  # Two's Complement conversion
  if (d >= 0x8000):
    d = -((65535 - d) + 1)
  return d
 
# Configure device  
bus.write_byte_data(DEVICE,REG_A,0x70) # 8 averaged samples, 15Hz
bus.write_byte_data(DEVICE,REG_B,0x20) # Field range 1.3, 1090 LSb/Gauss
bus.write_byte_data(DEVICE,REG_M,0x00) # Continuous measurement mode

x_max = 0
x_min = 0
y_max = 0
y_min = 0

try:
  # Loop until user presses CTRL-C
  f = open('calibration.csv', 'w')
  while True:

    # Read data from output registers
    x = read_data(DEVICE,REG_X)
    y = read_data(DEVICE,REG_Y)
    z = read_data(DEVICE,REG_Z)  

    # Write raw data to text file
    data = "{} {} {}\n".format(x,y,z)
    f.write(data)
    
    # Record max/min values
    if x>x_max: x_max = x
    if x<x_min: x_min = x
    if y>y_max: y_max = y
    if y<y_min: y_min = y  

    print ".",      
    sys.stdout.flush()       
       
    time.sleep(0.1)
  
except KeyboardInterrupt:
  # Display results
  
  f.close()
  
  # X Offset
  x_range = (x_max + abs(x_min))/2
  x_offset = x_range - x_max
  
  # Y Offset
  y_range = (y_max + abs(y_min))/2
  y_offset = y_range - y_max

  print ""
  print "X Values : {} to {}  Y Values : {} to {}".format(x_min,x_max,y_min,y_max)
  print "X Offset : {}  Y Offset : {}".format(x_offset,y_offset)  