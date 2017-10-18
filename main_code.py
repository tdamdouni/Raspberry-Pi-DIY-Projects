#!/usr/bin/env python

#import necessary modules here
import random
import time
import sys
import os
import numpy as np
from operator import itemgetter

import unicornhat as unicorn

from mcpi.minecraft import Minecraft

#set minecraft mode to false by default
minecraftMode = False

#assign total number of lifeforms possible to an argument that can be passed into python
lifeFormTotal = sys.argv[1]

#if the user doesnt know what the input arguments are they can type in '/help' after the program to get instructions
if lifeFormTotal == str("/help"):
	print ('6 variables are required for this program: <initial no. of lifeforms> <processing time> <max no. of lifeforms> <max lifetime> <max aggression factor> <"-mc" for Minecraft Mode (optional)')
	sys.exit()
else:
	lifeFormTotal = int(lifeFormTotal)

#assign the loop delay with a second argument that can be passed into python
timeSet = int(sys.argv[2])

#assign the population limit of lifeforms with a third argument that can be passed into python
popLimit = int(sys.argv[3])

#assign the max time to live possible for lifeforms with a fourth argument that can be passed into python
maxTTL = int(sys.argv[4])

#assign the aggression factor for lifeforms with a fifth argument that can be passed into python
maxAggro = int(sys.argv[5])

#final optional fourth argument that determines whether the program with interact with a running instance of minecraft on the pi
if len(sys.argv) == 7:
	if sys.argv[6] == ('-mc'):

		minecraftMode = True
		mc = Minecraft.create()
		mc.postToChat("PiLife Plugged into Minecraft!")
		
#unicorn hat setup		
unicorn.set_layout(unicorn.AUTO)
unicorn.brightness(0.5)
unicorn.rotation(0)
unicorn.brightness(0.5)

#default setting for lifeformtotalcount which is used for the number of lifeforms currently in existance
lifeFormTotalCount = lifeFormTotal
#default setting for highestconcurrentLifeforms which is used for showing the highest number of lifeforms that existed during a program run
highestConcurrentLifeforms = 0
#initialising a list used for storing positions of lifeforms later
posList = []
#initialise default state for layer variable for setting blocks in minecraft mode
layer = 0

#the main class that handles each lifeforms initialisation, movement, colour, expiry and statistics
class lifeForm(object):
	
	#standard class initialisation
	def __init__(self, Id):
		self.Id = Id
	
	#when this function is called it gives the lifeform of the class instance its properties from the random numbers inserted into it
	def sparkLife(self, seed, seed2, seed3, startX, startY):
		self.lifeSeed = seed
		self.lifeSeed2 = seed2
		self.lifeSeed3 = seed3
		#lifeseed 1 controls the random number generation for the red colour, maximum aggression factor starting direction and maximum possible lifespan
		random.seed(self.lifeSeed)
		self.redColor = random.randint(1, 255)
		self.maxAggressionFactor = random.randint(1, maxAggro)
		self.direction = random.randint(1, 9)
		self.maxLife = random.randint(1, maxTTL)
		#lifeseed 2 controls the random number generation for the green colour, aggression factor between 0 and the maximum from above as well as the time the entity takes to change direction
		random.seed(self.lifeSeed2)
		self.greenColor = random.randint(1, 255)
		self.aggressionFactor = random.randint(0, self.maxAggressionFactor)		
		self.timeToMove = random.randint(1, 25)
		self.timeToMoveCount = self.timeToMove
		#lifeseed 3 controls the random number generation for the green colour, and time to live between 0 and the maximum from above
		random.seed(self.lifeSeed3)
		self.blueColor = random.randint(1, 255)
		self.timeToLive = random.randint(0, self.maxLife)
		self.timeToLiveCount = self.timeToLive
		#reset the global random seed
		random.seed()
		
		#set the starting location of the lifeform from the x and y positions passed into the function
		self.matrixPositionX = startX
		self.matrixPositionY = startY

	#when called this function will display the statistics of the current lifeform in the main loop	
	def getStats(self):
		print ('ID: ' + str(self.Id))
		print ('Seed 1: ' + str(self.lifeSeed))
		print ('Seed 2: ' + str(self.lifeSeed2))
		print ('Seed 3: ' + str(self.lifeSeed3))
		print ('Direction: ' + str(self.direction))
		print ('Time to move total: ' + str(self.timeToMove))
		print ('Time to next move: ' + str(self.timeToMoveCount))
		print ('Total lifetime: ' + str(self.timeToLive))
		print ('Time left to live: ' + str(self.timeToLiveCount))
		print ('Aggression Factor: ' + str(self.aggressionFactor))
		print ('Position X: ' + str(self.matrixPositionX))
		print ('Position Y: ' + str(self.matrixPositionY))
		print ('Color: ' + 'R-' + str(self.redColor) + ' G-' + str(self.greenColor) + ' B-' + str(self.blueColor) + '\n')
	
	#this function will move the entity in its currently set direction (with 8 possible directions), if it hits the edge of the board it will then assign a new random direction to go in, this function also handles the time to move count which when hits 0 will select a new random direction for the entity regardless of whether it has hit the edge of the board or another entity
	def movement(self):
		
		#if the edge of the board is not hit and direction is '1' then move the entity up the X axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity
		if self.direction == 1:
			if self.matrixPositionX < 7:
				self.matrixPositionX += 1
			else:
				self.direction = self.randomiseDirection()
		
		#if the edge of the board is not hit and direction is '2' then move the entity down the X axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity		
		if self.direction == 2:
			if self.matrixPositionX > 0:
				self.matrixPositionX -= 1
			else:
				self.direction = self.randomiseDirection()
				
		#if the edge of the board is not hit and direction is '3' then move the entity up the Y axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity		
		if self.direction == 3:
			if self.matrixPositionY < 7:
				self.matrixPositionY += 1
			else:
				self.direction = self.randomiseDirection()
		
		#if the edge of the board is not hit and direction is '4' then move the entity down the Y axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity		
		if self.direction == 4:
			if self.matrixPositionY > 0:
				self.matrixPositionY -= 1
			else:
				self.direction = self.randomiseDirection()

		#if the edge of the board is not hit and direction is '5' then move the entity up the X and Y axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity
		if self.direction == 5:
			if self.matrixPositionX < 7 and self.matrixPositionY < 0:
				self.matrixPositionX += 1
				self.matrixPositionY += 1
			else:
				self.direction = self.randomiseDirection()

		#if the edge of the board is not hit and direction is '6' then move the entity down the X and Y axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity				
		if self.direction == 6:
			if self.matrixPositionX > 0 and self.matrixPositionY > 0:
				self.matrixPositionX -= 1
				self.matrixPositionY -= 1
			else:
				self.direction = self.randomiseDirection()

		#if the edge of the board is not hit and direction is '7' then move the entity down the X axis and up Y axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity				
		if self.direction == 7:
			if self.matrixPositionY < 7 and self.matrixPositionX > 0:
				self.matrixPositionX -= 1
				self.matrixPositionY += 1
			else:
				self.direction = self.randomiseDirection()

		#if the edge of the board is not hit and direction is '8' then move the entity up the X axis and down Y axis by 1, if it has hit the edge of the board its direction is randomised by the randomisedirection function being called for the entity						
		if self.direction == 8:
			if self.matrixPositionY > 0 and self.matrixPositionX < 7:
				self.matrixPositionX += 1
				self.matrixPositionY -= 1
			else:
				self.direction = self.randomiseDirection()
		
		#if the direction is '9' do not move the entity		
		elif self.direction == 9:
			self.matrixPositionX = self.matrixPositionX
			self.matrixPositionY = self.matrixPositionY
		
		#minus 1 from the time to move count until it hits 0, at which point the entity will change direction from the randomisedirecion function being called
		if self.timeToMoveCount > 0:
			self.timeToMoveCount -= 1
		elif self.timeToMoveCount <= 0:
			self.timeToMoveCount = self.timeToMove
			self.direction = self.randomiseDirection()
			
	#when called this function with select a random new direction for the lifeform that is not the direction it is already going		
	def randomiseDirection(self):
		
		r = range(1,self.direction) + range(self.direction+1, 10)
		return random.choice(r)
	
	#this function counts down a lifeforms time to live from its full lifetime assigned to it when a lifeforms time to live hits zero remove it from the list of lifeforms and set the colours to 0, 0, 0
	def expireEntity(self, iListIn):
		
		if self.timeToLiveCount > 0:
			self.timeToLiveCount -= 1
			return (iListIn)
		elif self.timeToLiveCount <= 0:
			self.redColor = 0
			self.greenColor = 0
			self.blueColor = 0
			iListIn.remove(self.Id)
			return (iListIn)
	
	#function to call for erasing an entity from the board as well as the main list for lifeforms
	def killEntity(self, iListIn):
			self.redColor = 0
			self.greenColor = 0
			self.blueColor = 0
			iListIn.remove(self.Id)
			return (iListIn)
		
	#print the number of lifeforms currently on the board
def printLifeformNo(no):
	
	print("Lifeforms: " + str(no))				

#draw the position and colour of the current lifeform onto the board, if minecraft mode true, also setblocks relative to the player in the game world, adding 1 to the layer every iteration so that each time the current amount of entites are rendered it moves to another layer in minecraft, essentially building upwards
def drawLEDS(x, y, r, g, b, layer):
	unicorn.set_pixel(x, y, r, g, b)
	unicorn.show()
	if minecraftMode == True:
		playerX, playerY, playerZ = mc.player.getPos()
		random.seed(r+g+b)
		randomBlock = random.randint(1, 22)
		random.seed()
		mc.setBlock(playerX+x, playerY+10+layer, playerZ+y, randomBlock)

#clear the unicorn hat led grid	
def clearLEDS():
	unicorn.clear()

#function used for determining percentages of a whole number (deprecated)	
def percentage(percent, whole):
		
	return int(round(percent * whole) / 100.0)

#function used for generating a random number to be used as a seed, this is used to generate all 3 lifeseeds resulting in 1.e+36 possible types of lifeform
def genRandom():
	
	return random.randint(1, 1000000000000)

#function used to determine whether a lifeform is colliding with another currently on the board	
def collisionDetector(boardPositions, posX, posY, Id):
	
	#get the board positions for the current lifeform
	idX = posX
	idY = posY
	
	#clear lists that will be used to temporarily store x, y info for other lifeforms on the board, for comparison
	sItemX = ()
	sItemY = ()

	#for every item in the list of board positions perform a loop
	for item in boardPositions:
		
		#split the items in the sub-list into seperate variables for comparison
		sItemId = itemgetter(0)(item)
		sItemX = itemgetter(1)(item)
		sItemY = itemgetter(2)(item)

		#if the id of the lifeform in the position list matches the id of the lifeform currently being checked, then do nothing - to prevent lifeforms from colliding with themselves
		if sItemId == Id:
			continue
		
		#if the x and y positions match that of a lifeform that is currently on the position list then return the id of the lifeform it collided with
		elif idX == sItemX and idY == sItemY:
			return sItemId

#function for generating a new lifeform within the program			
def generateLifeformAttribsSpark(Id, lifeSeed, lifeSeed2, lifeSeed3, posXGen, posYGen):
				
	holder[Id].sparkLife(lifeSeed, lifeSeed2, lifeSeed3, posXGen, posYGen)	

#function that assign lifeforms ids from the total number recieved by the function and puts them in a list
def assignClasses(total):
	
	iList = []
	for i in range(total):
		i += 1
		iList.append(i)
	
	return (iList)
  
#obtain lifeform id list from the above function  
iList = assignClasses(lifeFormTotal)
#assign all the ids into class instances for each lifeform
holder = {Id: lifeForm(Id=Id) for Id in iList}

#for each id in the list of all lifeform ids assign a random x and y number for the position on the board and create the new lifeform with random seeds for each lifeseed generation
for Id in iList:
	
	posXGen = random.randint(1, 8)
	posYGen = random.randint(1, 8)
	generateLifeformAttribsSpark(Id, genRandom(), genRandom(), genRandom(), posXGen, posYGen)

#wrap main loop into a try: to catch keyboard exit
try:
	while True:
		
		#clear unicorn hat leds and clear position list
		clearLEDS()
		posList = []
		#check the list of entities has items within
		if iList:
			#for time the current set of lifeforms is processed increase the layer for minecraft to set blocks on by 1
			layer += 1
			#for each id in the list use the id of the lifeform to work from
			for Id in iList:	
				#clear colliderscope variable to make sure its fresh from data from the last iteration
				colliderScope = ()
				#call the movement function for the lifeform
				holder[Id].movement()
				#call expiry function for current lifeform and update the list of lifeforms
				iList = holder[Id].expireEntity(iList)
				#if the lifeform has expired then skip the loop as we dont want to continue processing an entity which is no longer on the board
				if Id not in iList:
					continue
				#print stats of current lifeform to console
				holder[Id].getStats()
				#assign variables from information about lifeform for use later
				posX = holder[Id].matrixPositionX
				posY = holder[Id].matrixPositionY
				colR = holder[Id].redColor
				colG = holder[Id].greenColor
				colB = holder[Id].blueColor
				#call function to draw leds with the current lifeforms x and y and r g b data, as well as the current layer
				drawLEDS(posX, posY, colR, colG, colB, layer)
				#append the lifeforms id and x and y location to to the position list to be used by the collisiondetector
				posList.append([Id, posX, posY])
				#check for any collisions with any other entities and return the id of an entity collided with if so
				colliderScope = collisionDetector(posList, posX, posY, Id)
				#get the count of total lifeforms currently active
				lifeFormTotalCount = len(iList)
				#if the current number of active lifeforms is higher than the previous record of concurrent lifeforms, update the concurrent lifeforms variable
				if lifeFormTotalCount > highestConcurrentLifeforms:
					highestConcurrentLifeforms = lifeFormTotalCount
				#if there has been a collision with another entity it will attempt to interact with the other entity
				if colliderScope:
					#list variable for use later is cleared
					transfers = []
					#print information of the collision to screen
					print ('Collision detected: ' + str(Id) + ' collided with ' + str(colliderScope))
					#call the randomise direction function for the entity
					holder[Id].randomiseDirection()
					#if the aggression factor is below 850 the lifeform will attempt to breed with the one it collided with
					if holder[Id].aggressionFactor < 850:
						#the breeding will attempt only if the current lifeform count is not above the population limit
						if lifeFormTotalCount < popLimit:
							#generate 2 random numbers for x and y positions of the new entity
							posXGen = random.randint(1, 8)
							posYGen = random.randint(1, 8)
							
							#check for an entity at this position
							for i in posList:
								colliderScopeBirthConflicter = collisionDetector(posList, posXGen, posYGen, Id)			
								if colliderScopeBirthConflicter:
									posXGen = random.randint(1, 8)
									posYGen = random.randint(1, 8)
									
									#if the aggression factor is too low for the entity collided with and there is an entity at the current location its offspring wants to spawn, it will not do anything and no new entity will spawn
									if holder[colliderScope].aggressionFactor < 250:
										#print infromation and continue to next iteration of the loop
										print 'Nothing killed'
										continue
									
									#if the aggression factor is higher than the entity currently in place, the currently existing entity will be killed and replaced with the new offspring
									elif holder[colliderScope].aggressionFactor > holder[colliderScopeBirthConflicter].aggressionFactor:
										#call the kill entity function for the entity blocking the offspring
										iList = holder[colliderScopeBirthConflicter].killEntity(iList)
										#remove the killed entity from the position list so that it cant be collided with on the next iteration
										posList.remove([colliderScopeBirthConflicter, holder[colliderScopeBirthConflicter].matrixPositionX, holder[colliderScopeBirthConflicter].matrixPositionY])
										#increase lifeform total by 1
										lifeFormTotal += 1
										#append the lifeform total to the list used by the main loop
										iList.append(lifeFormTotal)
										#create a dictionary containing the instance id of the new class instance for the lifeform
										hUpdate = {lifeFormTotal: lifeForm(lifeFormTotal)}
										#update the list containing all of the instance ids of the main entity class
										holder.update(hUpdate)
										
										#the below assigns all 3 lifeseeds with the potential to take the lifeseed from either parent (40% chance each), or whether a new random lifeseed will be inserted (20% chance), resulting in some genetic chaos to change offspring randomly
										transferOptions1 = [holder[Id].lifeSeed, holder[colliderScope].lifeSeed, genRandom()]
										transferOptions2 = [holder[Id].lifeSeed2, holder[colliderScope].lifeSeed2, genRandom()]
										transferOptions3 = [holder[Id].lifeSeed3, holder[colliderScope].lifeSeed3, genRandom()]
										
										#print information to the console
										print 'Conflicter killed'
										
										#generate new lifeform with the chances of taking the information from each lifeseed or a totally new random seed, creating them at the x and y coords determined above
										generateLifeformAttribsSpark(lifeFormTotal, int(np.random.choice(transferOptions1, 1, p=[0.4, 0.4, 0.2])), int(np.random.choice(transferOptions2, 1, p=[0.4, 0.4, 0.2])), int(np.random.choice(transferOptions3, 1, p=[0.4, 0.4, 0.2])), posXGen, posYGen)
										#break the loop as no more needs to be done
										break
									
									#if the aggression factor of the already existing entity is higher then the current entity will be killed and no offspring produced
									elif holder[colliderScope].aggressionFactor < holder[colliderScopeBirthConflicter].aggressionFactor:
										print 'Collider killed'
										iList = holder[colliderScope].killEntity(iList)
										posList.remove([colliderScope, holder[colliderScope].matrixPositionX, holder[colliderScope].matrixPositionY])
										#break the loop as no more needs to be done
										break
								
								#if there is no entity in the place of the potential offspring the new entity will be created at the x and y coords determined above
								else:
									#increas the lifeform total by 1
									lifeFormTotal += 1
									iList.append(lifeFormTotal)
									hUpdate = {lifeFormTotal: lifeForm(lifeFormTotal)}
									holder.update(hUpdate)
							
									#the below assigns all 3 lifeseeds with the potential to take the lifeseed from either parent (40% chance each), or whether a new random lifeseed will be inserted (20% chance), resulting in some genetic chaos to change offspring randomly
									transferOptions1 = [holder[Id].lifeSeed, holder[colliderScope].lifeSeed, genRandom()]
									transferOptions2 = [holder[Id].lifeSeed2, holder[colliderScope].lifeSeed2, genRandom()]
									transferOptions3 = [holder[Id].lifeSeed3, holder[colliderScope].lifeSeed3, genRandom()]
									
									#generate new lifeform with the chances of taking the information from each lifeseed or a totally new random seed, creating them at the x and y coords determined above
									generateLifeformAttribsSpark(lifeFormTotal, int(np.random.choice(transferOptions1, 1, p=[0.4, 0.4, 0.2])), int(np.random.choice(transferOptions2, 1, p=[0.4, 0.4, 0.2])), int(np.random.choice(transferOptions3, 1, p=[0.4, 0.4, 0.2])), posXGen, posYGen)
									break
						
						#if the current amount of lifeforms on the board is at the population limit or above then do nothing
						elif lifeFormTotalCount >= popLimit:
							continue
					
					#if the entities aggression factor is above 850 it will attempt to kill the entity it has collided with instead of breed
					elif holder[Id].aggressionFactor > 850:
						#if the other entities aggression factor is lower it will be killed and removed from the main loops list of entities
						if holder[colliderScope].aggressionFactor < holder[Id].aggressionFactor:
							print ('Other entity killed')
							iList = holder[colliderScope].killEntity(iList)
							posList.remove([colliderScope, holder[colliderScope].matrixPositionX, holder[colliderScope].matrixPositionY])
						#if the other entities aggression factor is higher it will be kill the current entity and it will be removed from the main loops list of entities
						elif holder[colliderScope].aggressionFactor > holder[Id].aggressionFactor:
							print ('Current entity killed')
							iList = holder[Id].killEntity(iList)
							posList.remove([Id, holder[Id].matrixPositionX, holder[Id].matrixPositionY])
						#if the aggression factor of both entities is identical they will reach a stalemate and simply bounce off each other
						elif holder[colliderScope].aggressionFactor == holder[Id].aggressionFactor:
							print ('Neither entity killed')
							continue
		
		#if the main list of entities is empty then all have expired; the program displays final information about the programs run and exits
		elif not iList:
			lifeFormTotalCount = 0
			print ('\n' + 'All Lifeforms have expired.' + '\n' + 'Total lifeforms produced: ' + str(lifeFormTotal) + '\n' + 'Max concurrent Lifeforms was: ' + str(highestConcurrentLifeforms))
			break
		
		#uncomment below line to display the current amount of lifeforms on the board
		#printLifeformNo(lifeFormTotalCount)
		#time to sleep before next loop iteration, controlled from argument above
		time.sleep(timeSet)

#upon keyboard interrupt display information about the program run before exiting
except KeyboardInterrupt:
	print ('\n' + 'Program ended by user.' + '\n' + 'Total lifeforms produced: ' + str(lifeFormTotal) + '\n' + 'Max concurrent Lifeforms was: ' + str(highestConcurrentLifeforms) + '\n' + 'Last count of active Lifeforms: ' + str(lifeFormTotalCount))
