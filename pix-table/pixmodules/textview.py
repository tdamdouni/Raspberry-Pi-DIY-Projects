import threading
import time
from PIL import Image
from pixmodule import PixModule

class TextView(PixModule):
	
	text = "Hello YouTube! "
	font = "/home/pi/pix-table/pixmodules/font.gif"
	# image file for font
	fontData = None
	stringMap = None
	textPosition = 0
	textPositionCounter = 0
	fontColor = [200,200,200]
	backgroundColor = [27,68,29]

	def __init__(self, spiDevice, base=None):
		super(TextView,self).__init__(spiDevice)
		fontMap = Image.open(self.font)
		fontMap = fontMap.convert("RGBA")
		self.fontData = fontMap.getdata()
		self.stringMap = self.getStringMap(self.text)
		
	def render(self):
		self.textPositionCounter += 1
		if self.textPositionCounter > 15:
			self.textPositionCounter = 0
			self.textPosition += 1
			self.rollOutPixMap()	

	def rollOutPixMap(self):
		#self.displayLetterByLetter()
		self.displayRunningText()
		pass

	# merges two lettern to a single to get running effect (OK)
	def displayRunningText(self):
		letterPosition = self.textPosition % (len(self.stringMap)*4)
		absoluteLetterPosition = letterPosition % 4
		firstLetter = self.stringMap[int(letterPosition/4)]
		secondLetter = self.stringMap[((int(letterPosition / 4)) +1) % len(self.stringMap)]
		mergeLetter = []
		for i in range(20):
			mergeLetter.insert(i+(int(i/4)*4),firstLetter[i])
			mergeLetter.insert(i+4+(int(i/4)*4),secondLetter[i])
		self.pixels = [[self.backgroundColor for x in range(5)] for x in range(5)]
		for i in range(25):
			if mergeLetter[(i%5)+(i/5)*8+absoluteLetterPosition] == True:
				self.pixels[4-int(i/5)][4-i%5] = self.fontColor
		self.correctPixView()

	# display text in seperated letters (OK)
	def displayLetterByLetter(self):
		letterMap = self.stringMap[(self.textPosition % len(self.stringMap))]
		self.pixels = [[self.backgroundColor for x in range(5)] for x in range(5)]
		index = 0
		for pixel in letterMap:
			if pixel == True:
				self.pixels[4-int(index/4)][index%4] = self.fontColor
			index+=1
		self.correctPixView()

	# array of 5x4 letter arrays (OK)
	def getStringMap(self, string):
		stringMap = []
		for char in string:
			letterMap = self.getLetterMap(char)
			stringMap.append(letterMap)
		return stringMap


	# 5x4 array (20 elements) for one character (OK)
	def getLetterMap(self,c):
		number = ord(c)
		data = []
		for letter in range(20):
			x = (number * 4) % (16 * 4) + (letter % 4)
			y = (int(number / 16) * 16 * 4 * 6) + int(letter / 4) * 64
			data.append((True if self.fontData[x+y][0] < 100 else False))
		return data


	def getColor(self):
		return [27,68,29]