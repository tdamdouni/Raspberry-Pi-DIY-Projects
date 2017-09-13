#!/usr/bin/python
#--------------------------------------
#
#     Minecraft Python API
#        Castle Builder
#
# This script creates a castle complete
# with moat and perimeter walls.
#
# Author : Matt Hawkins
# Date   : 07/06/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

mc.postToChat("Let's build a castle!")

#--------------------------------------
# Define Functions
#--------------------------------------

def CreateWalls(size,baseheight,height,material,battlements,walkway):
  # Create 4 walls with a specified width, height and material.
  # Battlements and walkways can also be added to the top edges.
  
  mc.setBlocks(-size,baseheight+1,-size,size,baseheight+height,-size,material) 
  mc.setBlocks(-size,baseheight+1,-size,-size,baseheight+height,size,material)
  mc.setBlocks(size,baseheight+1,size,-size,baseheight+height,size,material) 
  mc.setBlocks(size,baseheight+1,size,size,baseheight+height,-size,material) 

  # Add battlements to top edge
  if battlements==True:
    for x in range(0,(2*size)+1,2):
      mc.setBlock(size,baseheight+height+1,(x-size),material) 
      mc.setBlock(-size,baseheight+height+1,(x-size),material) 
      mc.setBlock((x-size),baseheight+height+1,size,material) 
      mc.setBlock((x-size),baseheight+height+1,-size,material)
      
  # Add wooden walkways
  if walkway==True:  
    mc.setBlocks(-size+1,baseheight+height-1,size-1,size-1,baseheight+height-1,size-1,block.WOOD_PLANKS)   
    mc.setBlocks(-size+1,baseheight+height-1,-size+1,size-1,baseheight+height-1,-size+1,block.WOOD_PLANKS)  
    mc.setBlocks(-size+1,baseheight+height-1,-size+1,-size+1,baseheight+height-1,size-1,block.WOOD_PLANKS)   
    mc.setBlocks(size-1,baseheight+height-1,-size+1,size-1,baseheight+height-1,size-1,block.WOOD_PLANKS)  

def CreateLandscape(moatwidth,moatdepth,islandwidth):
  # Set upper half to air
  mc.setBlocks(-128,1,-128,128,128,128,block.AIR) 
  # Set lower half of world to dirt with a layer of grass
  mc.setBlocks(-128,-1,-128,128,-128,128,block.DIRT)
  mc.setBlocks(-128,0,-128,128,0,128,block.GRASS)
  # Create water moat
  mc.setBlocks(-moatwidth,0,-moatwidth,moatwidth,-moatdepth,moatwidth,block.WATER)
  # Create island inside moat
  mc.setBlocks(-islandwidth,0,-islandwidth,islandwidth,1,islandwidth,block.GRASS)  

def CreateKeep(size,baseheight,levels):
  # Create a keep with a specified number
  # of floors levels and a roof
  height=(levels*5)+5
  
  CreateWalls(size,baseheight,height,block.STONE_BRICK,True,True)
  
  # Floors & Windows
  for level in range(1,levels+1):
    mc.setBlocks(-size+1,(level*5)+baseheight,-size+1,size-1,(level*5)+baseheight,size-1,block.WOOD_PLANKS)

  # Windows
  for level in range(1,levels+1):
    CreateWindows(0,(level*5)+baseheight+2,size,"N")
    CreateWindows(0,(level*5)+baseheight+2,-size,"S")
    CreateWindows(-size,(level*5)+baseheight+2,0,"W")
    CreateWindows(size,(level*5)+baseheight+2,0,"E")

  # Door
  mc.setBlocks(0,baseheight+1,size,0,baseheight+2,size,block.AIR)

def CreateWindows(x,y,z,dir):

  if dir=="N" or dir=="S":
    z1=z
    z2=z
    x1=x-2
    x2=x+2

  if dir=="E" or dir=="W":
    z1=z-2
    z2=z+2
    x1=x
    x2=x

  mc.setBlocks(x1,y,z1,x1,y+1,z1,block.AIR)
  mc.setBlocks(x2,y,z2,x2,y+1,z2,block.AIR) 

  if dir=="N":
    a=3
  if dir=="S":
    a=2
  if dir=="W":
    a=0
  if dir=="E":
    a=1

  mc.setBlock(x1,y-1,z1,109,a)
  mc.setBlock(x2,y-1,z2,109,a)
  
#--------------------------------------
#
# Main Script  
#
#--------------------------------------
  
print("Create ground and moat")
CreateLandscape(33,10,23)  

print("Create outer walls")
CreateWalls(21,1,5,block.STONE_BRICK,True,True)

print("Create inner walls")
CreateWalls(13,1,6,block.STONE_BRICK,True,True)

print("Create Keep with 4 levels")
CreateKeep(5,1,4)

print("Position player on Keep's walkway")
mc.player.setPos(0,30,4)