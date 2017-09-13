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
import math

# HMC5883L properties
DEVICE = 0x1e # Device address on I2C
REG_A  = 0    # Configuration Register A
REG_B  = 1    # Configuration Register B
REG_M  = 2    # Mode Register
REG_X  = 3    # X Output Register
REG_Y  = 7    # Y Output Register
REG_Z  = 5    # Z Output Register

# Custom calibration offsets
X_OFFSET = -40
Y_OFFSET = 70

# Local declination offset
MYDECLINATION = -2 # -2 degrees

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

def calc_bearing(x,y,mode): 
  # Function to calculate bearing
  # mode=1 returns degrees
  bearing = math.atan2(y,x)
  if (bearing < 0):
    bearing += 2 * math.pi
  if (mode==1):  
    bearing = math.degrees(bearing)    
  return bearing
  
def configure():
  # Configure device  
  bus.write_byte_data(DEVICE,REG_A,0x70) # 8 averaged samples, 15Hz
  bus.write_byte_data(DEVICE,REG_B,0x20) # Field range 1.3, 1090 LSb/Gauss
  bus.write_byte_data(DEVICE,REG_M,0x00) # Continuous measurement mode

def read_values():
  x = read_data(DEVICE,REG_X)
  y = read_data(DEVICE,REG_Y)
  z = read_data(DEVICE,REG_Z)  
  return x,y,z

def main():

  configure()

  # Loop until user presses CTRL-C
  while True:

    # Read data from output registers
    #x = read_data(DEVICE,REG_X)
    #y = read_data(DEVICE,REG_Y)
    #z = read_dacd cta(DEVICE,REG_Z)  
    x,y,z = read_values()

    # Calculate bearing in degrees
    bearing = calc_bearing(x,y,1)
  
    print "Bearing: {:0.2f} degrees".format(bearing)
  
    time.sleep(1)

if __name__ == '__main__':
  main()