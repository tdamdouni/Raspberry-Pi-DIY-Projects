#!/usr/bin/python
#--------------------------------------
#
#     Minecraft Python API
#        Tomb Robber
#
# This script randomly places tombs in the
# world for the player to find.
#
# Author : Matt Hawkins
# Date   : 23/06/2016
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

#--------------------------------------
# Define Functions
#--------------------------------------

def getLocation():
  # Find suitable location for tomb
  scan=True
  while scan==True:
  # Random x,z location
    x = random.randint(-120, 120)
    z = random.randint(-120, 120)  
    # Get height of first non-air block in column
    y = mc.getHeight(x,z)-1
  
    # Check what block we have found
    blocks = [block.SAND.id,block.DIRT.id,block.GRASS.id]
    if mc.getBlock(x,y,z) in blocks:
    # Suitable block so end scan
      scan=False
      
  pos=(x,y,z)
  
  return pos

def createTomb(pos,size,depth,material,treasure):
  # Create tomb at a set position with a given material
  # Return position of treasure block
  x1 = pos[0] + (size/2)
  y1 = pos[1] - depth
  z1 = pos[2] + (size/2)
  x2 = pos[0] - (size/2)
  y2 = pos[1] - depth - size
  z2 = pos[2] - (size/2)
  mc.setBlocks(x1,y1,z1,x2,y2,z2,material) 
  mc.setBlocks(x1-1,y1-1,z1-1,x2+1,y2+1,z2+1,block.AIR.id) 
  
  # Add treasure to tomb at position "pos"
  x = pos[0]
  y = pos[1] - (size-1) - depth
  z = pos[2]
  mc.setBlock(pos[0],pos[1] - depth - size + 1,pos[2],treasure)
  
  return [x,y,z]
  
def placeMarker(pos,material):
  # Place marker above tomb
  mc.setBlock(pos[0],pos[1]+20,pos[2],material)    
 
def updateTreasures(treasureList):

  treasures = []

  for treasure in treasureList:
    pos = treasure[0]
    size = treasure[1]
    depth = treasure[2]
    x = pos[0]
      y = pos[1] - (size-1) - depth
      z = pos[2]
    if mc.getBlock(x,y,z)==block.AIR.id:
      # Treasure gone
      time.sleep(1)
    else:
      treasures.append(treasure)  
      
  return treasures
  
#--------------------------------------
#
# Main Script  
#
#--------------------------------------

mc = minecraft.Minecraft.create()

random.seed

treasureList = []

tombCount = 8

mc.postToChat("Let's rob some graves!")

print("Place " + str(tombCount) + " random tombs and treasure")

for tomb in range(tombCount):
  
  tombpos = getLocation()
  
  # Place marker in the sky
  placeMarker(tombpos,block.GLASS.id)
  treasurePos = createTomb(tombpos,4,3,block.STONE.id,block.GOLD_BLOCK.id)  
  treasureList.append(treasurePos)
 
  print("Tomb " + str(tomb) + " placed " + str(tombpos)) 

remainingTreasure = tombCount

mc.postToChat("There are " + str(remainingTreasure) + " treasures to find")

while len(treasureList)>0:
  # There are treasures to find!
  treasureList = updateTreasures(treasureList)
  time.sleep(1)
