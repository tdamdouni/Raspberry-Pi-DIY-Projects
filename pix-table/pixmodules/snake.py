import threading
import random
from pixmodule import PixModule

class Snake(PixModule):

	direction = 0
	snakecounter = 0
	point = 3,3
	snake = [(1,0),(0,0)]
	intro = True
	introState = 0

	def render(self):
		if self.intro==True:
			self.renderIntro()
		else:
			self.renderSnake()
			self.correctPixView()

	def testDirection(self):
		if self.leftPressed():
			self.direction=(self.direction+1)%4
		if self.rightPressed():
			self.direction=(self.direction-1)%4

	def snakePosition(self):
		old = self.snake[0]
		if self.snake[0]==self.point:
			self.snake.insert(len(self.snake),self.snake[:-1])
			self.point = (random.randint(0,4),random.randint(0,4))
		for x in xrange(1,len(self.snake)):
			safe = self.snake[x]
			self.snake[x] = old
			old = safe
		self.snake[0] = {
			0:((self.snake[0][0]+1)%5,(self.snake[0][1])%5),
			1:((self.snake[0][0])%5,(self.snake[0][1]+1)%5),
			2:((self.snake[0][0]-1)%5,(self.snake[0][1])%5),
			3:((self.snake[0][0])%5,(self.snake[0][1]-1)%5)
		}[self.direction]

	def renderSnake(self):
		self.snakecounter+=1
		self.pixels = [[[0 for x in range(3)] for x in range(5)] for x in range(5)]
		self.pixels[self.point[0]][self.point[1]][0]=255
		for dot in self.snake:
			self.pixels[dot[0]][dot[1]][1]=255					
		if(self.snakecounter>20):
			self.snakecounter=0
			self.testDead()
			self.snakePosition()
		self.testDirection()

	def testDead(self):
		for a in range(len(self.snake)):
			for b in range(len(self.snake)):
				if( self.snake[a] == self.snake[b] and a != b):
					self.direction = 0
					self.snakecounter = 0
					self.point = 3,3
					self.snake = [(1,0),(0,0)]
					self.intro = True
					self.introState = 0
					return

	def renderIntro(self):
		if self.introState == 0:
			self.pixels = [[[0 for x in range(3)] for x in range(5)] for x in range(5)]
			for x in range(5):
				self.pixels[0][x][2]=255
		elif self.introState == 50:
			for x in range(5):
				self.pixels[1][x][2]=255
		elif self.introState == 100:
			for x in range(5):
				self.pixels[2][x][2]=255
		elif self.introState == 150:
			for x in range(5):
				self.pixels[3][x][2]=255
		elif self.introState == 200:
			for x in range(5):
				self.pixels[4][x][2]=255

		for x in range(5):
			for y in range(5):
				if self.pixels[x][y][2] > 2:
					self.pixels[x][y][2] -= 2

		self.introState += 1
		if(self.introState >= 350):
			self.intro=False

	def getColor(self):
		return [0,255,0]
