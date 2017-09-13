#!/usr/bin/python
#--------------------------------------
#
#     Raspberry Pi Minecraft
#            Pyramids
#
# Create pyramids in Minecraft
#
# Author : Matt Hawkins
# Date   : 01/09/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import standard libraries
import time
import math

# Import specific Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

# Block definitions
# See http://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/ for more blocks
AIR       = 0
DIRT      = 3
SAND      = 12
SANDSTONE = 24
GOLD      = 41

mc = minecraft.Minecraft.create()

def CreatePyramid(posx,posy,posz,width,mybase,mywalls,mytopblock):
  # Function to create a pyramid at x,y,z
  # with specified width using the specified
  # block materials for the base, walls and top.
  
  mc.postToChat("About to create pyramid!")
  
  # May sure width is odd number so pyramid ends
  # with a single block
  if width%2==0:
    width=width+1
  
  height = (width+1)/2
  halfsize = int(math.floor(width/2))
  
  print "Player : {} {} {}".format(posx,posy,posz)
  print "Size : {} Height : {} Halfsize : {}".format(width,height,halfsize)
   
  # Create base for pyramid
  print "Create solid base"
  mc.setBlocks(posx-halfsize-2,posy-2,posz-halfsize-2,posx+halfsize+2,posy-2,posz+halfsize+2,DIRT)      
  mc.setBlocks(posx-halfsize-2,posy-1,posz-halfsize-2,posx+halfsize+2,posy-1,posz+halfsize+2,mybase)      
    
  # Create solid Pyramid
  print "Create Pyramid"  
  for y in range(posy,posy+height):
    mc.setBlocks(posx-halfsize,y,posz-halfsize,posx+halfsize,y,posz+halfsize,mywalls) 
    halfsize = halfsize-1
	  
  # Change top block
  print "Set top block"   
  mc.setBlock(posx,posy+height-1,posz,mytopblock)  
		
  print "Position player on top" 
  mc.player.setPos(posx,posy+height,posz)

# Get player position
mc.player.setPos(0,1,0)
playerPos = mc.player.getPos()
playerPos = minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))

# Set lower half of world to Sandstone
mc.setBlocks(-128,0,-128,128,-128,128,SANDSTONE)

# Set upper half to air
mc.setBlocks(-128,1,-128,128,128,128,AIR)  

# Create Pyramids
CreatePyramid(0,1,0,51,SANDSTONE,SANDSTONE,GOLD)

CreatePyramid(-40,1,40,21,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(-40,1,-40,21,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(40,1,40,21,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(40,1,-40,21,SANDSTONE,SANDSTONE,SANDSTONE)

CreatePyramid(0,1,45,31,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(0,1,-45,31,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(45,1,0,31,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(-45,1,0,31,SANDSTONE,SANDSTONE,SANDSTONE)
