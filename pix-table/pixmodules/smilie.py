import threading
import time
from PIL import Image
from pixmodule import PixModule

class Smilie(PixModule):
	
	smilieData = None
	backgroundColor = [30,30,30]
	smilieColor = [100,0,0]

	def __init__(self, spiDevice, base=None):
		super(Smilie,self).__init__(spiDevice)
		self.buildUpSmilieData()
		
	def buildUpSmilieData(self):
		self.smilieData = []
		for i in range(25):
			self.smilieData.insert(i,False)
		self.smilieData[6] = True
		self.smilieData[8] = True
		self.smilieData[12] = True
		self.smilieData[15] = True
		self.smilieData[19] = True
		self.smilieData[23] = True
		self.smilieData[22] = True
		self.smilieData[21] = True
		
	def drawSmilie(self):
		self.pixels = [[self.backgroundColor for x in range(5)] for x in range(5)]
		for i, pixel in enumerate(self.smilieData):
			if pixel == True:
				self.pixels[4-int(i/5)][i%5] = self.smilieColor
		self.correctPixView()

	def render(self):
		self.drawSmilie()	

	def getColor(self):
		return self.smilieColor