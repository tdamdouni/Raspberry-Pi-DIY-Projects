#!/usr/bin/python
#--------------------------------------
#
#     Raspberry Pi Minecraft
#     Operation Counterstrike
#
# Defuse the all bombs before you
# run out of time!
#
# Can display status messages
# to a PiFace Control & Display
#
# Author : Matt Hawkins
# Date   : 09/07/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# import standard libraries
import sys
import time
import math
import random as rand

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

# Import PiFace library
#import pifacecad as pf

def message(msg):
  # Send messages to game, PiFace and command line
  #cad.lcd.clear()
  msg_one_line = msg.replace('\n',' ')
  mc.postToChat(msg_one_line)
  print msg_one_line
  #cad.lcd.write(msg)

def plant_device():
  # Place TNT block at random location
  # returning its location and timer
  x=rand.randint(-100,100)
  y=100
  z=rand.randint(-100,100)

  # Lower if block underneath is air or water
  current_block=mc.getBlock(x,y-1,z)
  while current_block==block.AIR.id or current_block==block.WATER_STATIONARY.id:
    y=y-1
    current_block=mc.getBlock(x,y-1,z)

  # Bury under ground but not sea bed
  if mc.getBlock(x,y+1,z)!=block.WATER_STATIONARY.id:
    y = rand.randint(y-3,y-1)

  # Place TNT block
  mc.setBlock(x,y,z,block.TNT)

  return [x,y,z,rand.randint(80,180)]

def nearest_device():
  # Find distance to nearest device
  playerPos = mc.player.getTilePos()
  min_dist=9999
  for dev in devices[:]:
    dist = math.sqrt((playerPos.x-dev[0])**2 + (playerPos.y-dev[1])**2 + (playerPos.z-dev[2])**2)
    if dist<min_dist:
      min_dist=dist

  return int(min_dist)

def time_bonus(bonus):
  # Add bonus time to all device timers
  message(str(bonus) + " sec bonus")
  for i in xrange(len(devices)):
    devices[i][3]=devices[i][3]+bonus   
 
def count_down(increment):
  # Countdown each device timer
  min_time=9999
  for i in xrange(len(devices)):
    devices[i][3]=devices[i][3]-increment
    if devices[i][3]<min_time:
      min_time=devices[i][3]
  return min_time

mc=minecraft.Minecraft.create()
  
#cad = pf.PiFaceCAD()
#cad.lcd.backlight_on()

message("Standby ...")

# Get command line arguments
if len(sys.argv)==2:
  num_devices=int(sys.argv[1])
else:
  num_devices=3

# Initialise variables
game_on=True
devices = []

# Create devices
for i in range(0,num_devices):
  devices.append(plant_device())

message(str(num_devices) + "\nBombs activated ...")

while num_devices>0 and game_on:
  time.sleep(2)

  # Check what devices remain
  current_devices = []
  for dev in devices[:]:
    if mc.getBlock(dev[0],dev[1],dev[2])!=block.TNT.id:
      time_bonus(60)
      message("Device defused\n" + str(num_devices-1) + " remaining")
    else:
      current_devices.append(dev)
  devices=current_devices

  # Count remaining devices
  num_devices=len(devices)
  # Distance to nearest device
  distance = nearest_device()
  # Update device timers
  min_time=count_down(2)

  # Issue status if game is still active
  if num_devices>0 and min_time>0:
    message("R: " + str(distance) + "m\nT: " + str(min_time))
  elif min_time<=0:
    game_on=False

# Either all devices were found or
# one of them has exploded
if game_on:
  message("Congratulations!")
else:
  message("**BOOOM**\nYou failed!")