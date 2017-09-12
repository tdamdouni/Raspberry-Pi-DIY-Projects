import threading
import time

class PixModule(threading.Thread):

	# display array
	pixels = None
	# brightness of lights
	brightness = 0.3
	# spi device to send 
	spiDevice = None	

	def __init__(self, spiDevice, base=None):
		super(PixModule, self).__init__()
		self._stop = threading.Event()
		# keycontrol
		self._left = threading.Event()
		self._right = threading.Event()
		# get device
		self.spiDevice = spiDevice
		# pixels in 3 colors to white
		self.pixels = [[[0 for x in range(3)] for x in range(5)] for x in range(5)]

	def draw(self):
		for row in self.pixels:
			for pixel in row:
				for color in pixel:
					c = int(color*self.brightness)
					self.spiDevice.write(chr(c & 0xFF))
		self.spiDevice.flush()

	def run(self):
		while not self.stopped():
			self.render()
			self.draw()
			time.sleep(0.01)

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()

	def left(self):
		self._left.set()

	def leftPressed(self):
		if(self._left.isSet()):
			self._left.clear()
			return True
		else:
			return False

	def right(self):
		self._right.set()

	def rightPressed(self):
		if(self._right.isSet()):
			self._right.clear()
			return True
		else:
			return False

	def correctPixView(self):
		self.pixels[0] = self.pixels[0][::-1]
		self.pixels[2] = self.pixels[2][::-1]
		self.pixels[4] = self.pixels[4][::-1]

	def getColor(self):
		pass

	def render(self):
		pass
