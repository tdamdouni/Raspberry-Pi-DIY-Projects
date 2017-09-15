import threading
import random
from pixmodule import PixModule

class GameOfLife(PixModule):

	neighbors=lambda self, x, y : [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if -1 < x <= 5 and -1 < y <= 5 and (x != x2 or y != y2)]
	colorchangecounter = 0
	gameoflifecounter = 0
	gameoflifearray = [[True for x in range(5)] for x in range(5)]
	basecolor = 0

	def render(self):
		self.colorchangecounter += 1
		self.gameoflifecounter += 1
		self.updateColor()
		if self.gameoflifecounter > 150:
			self.gameOfLife()
			self.gameoflifecounter = 0
		if self.colorchangecounter > 500:
			self.basecolor = ( self.basecolor + 1 ) % 3
			self.colorchangecounter = 0

	def gameOfLife(self):
		oldgame=self.gameoflifearray
		for x in xrange(0,5):
			for y in xrange(0,5):
				livingneightbours = 0 
				for n in self.neighbors(x,y):
					try:
						if(self.gameoflifearray[n[0]%5][n[1]%5] == True):
							livingneightbours += 1
					except: 
						pass
				if (livingneightbours>3 or livingneightbours<2) and self.gameoflifearray[x][y]==True:
					self.gameoflifearray[x][y]=False
				if(livingneightbours==3 and self.gameoflifearray[x][y]==False):
					self.gameoflifearray[x][y]=True
		if oldgame==self.gameoflifearray:
			self.gameoflifearray=[[(random.random()>0.5) for x in range(5)] for x in range(5)]

	def updateColor(self):
		for x in xrange(0,5):
			for y in xrange(0,5):
				if(self.gameoflifearray[x][y]==True and  self.pixels[x][y][self.basecolor] <255):
					self.pixels[x][y][self.basecolor] = (self.pixels[x][y][self.basecolor] +1)
				if(self.gameoflifearray[x][y]==False and  self.pixels[x][y][0] >=0):
					self.pixels[x][y][0] = (self.pixels[x][y][0] -1)
				if(self.gameoflifearray[x][y]==False and  self.pixels[x][y][1] >=0):
					self.pixels[x][y][1] = (self.pixels[x][y][1] -1)
				if(self.gameoflifearray[x][y]==False and  self.pixels[x][y][2] >=0):
					self.pixels[x][y][2] = (self.pixels[x][y][2] -1)

	def getColor(self):
		return [127,0,127]
