import threading
import random
from pixmodule import PixModule

class Pong(PixModule):

	speed = 0
	speedcounter = 0
	direction = 1
	position = 0
	stats = (0,0)
	startSleep = 0

	def render(self):
		if(self.stats is (0,0) and self.startSleep < 4000):
			self.startSleep += 1
		elif self.stats[0] == 9:
			if self.leftPressed():
				self.stats = (0,0)
		elif self.stats[1] == 9:
			if self.rightPressed():
				self.stats = (0,0)
		else:
			self.renderPong()

	def testDirection(self):
		if self.leftPressed():
			self.direction=(self.direction+1)%4
		if self.rightPressed():
			self.direction=(self.direction-1)%4

	def updatePong(self):
		if self.position == 24 and self.rightPressed():
			self.direction = -1
			self.speed += 1
			return
		if self.position == 0 and self.leftPressed():
			self.direction = 1
			self.speed += 1
			return
		if (self.position == 0 and self.direction == -1):
			self.stats = (self.stats[0],self.stats[1]+1)
			self.resetGame()
			return
		if (self.position == 24 and self.direction == 1):
			self.stats = (self.stats[0]+1,self.stats[1])
			self.resetGame()
			return
		self.leftPressed()
		self.rightPressed()
		self.position+=self.direction

	def resetGame(self):
		self.speed = 0
		self.speedcounter = 0
		boolean =  bool(random.getrandbits(1))
		self.position =  24 if boolean else 0
		self.direction = -1 if boolean else 1
		self.startSleep = 0

	def renderPong(self):
		self.pixels = [[[0 for x in range(3)] for x in range(5)] for x in range(5)]
		self.pixels[0][0] = (255,255,0)
		self.pixels[4][4] = (255,255,0)
		for i in range(self.stats[0]):
			i = i + 1
			self.pixels[int(i/5)][(i%5)] = (0,0,50)			
		for i in range(self.stats[1]):
			i = 23 - i
			self.pixels[int(i/5)][(i%5)] = (0,50,0)
		self.pixels[int(self.position/5)][(self.position%5)] = (255,255,255)
		self.speedcounter += 1
		if(self.speedcounter > (10 - (self.speed))):
			self.speedcounter = 0
			self.updatePong()

	def getColor(self):
		return [255,255,0]
