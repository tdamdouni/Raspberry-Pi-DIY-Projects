#!/usr/bin/python
#--------------------------------------
#
#     Minecraft Python API
#        What Is That?
#
# This script returns the ID of the block
# underneath the player.
#
# Author : Matt Hawkins
# Date   : 08/06/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

playerPos = mc.player.getTilePos()
blockBelowPlayer = mc.getBlockWithData(playerPos.x, playerPos.y - 1, playerPos.z)

mc.postToChat("You are standing Block ID : {} Data : {}".format(blockBelowPlayer.id,blockBelowPlayer.data))