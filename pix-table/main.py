import sys
import time
import curses
import pkgutil
import RPi.GPIO as GPIO
from pixmodules import *


leftPin = 22
rightPin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftPin,GPIO.IN)
GPIO.setup(rightPin,GPIO.IN)

def displayClasses(pix):
	subclasses = PixModule.__subclasses__()
	for x in range(len(subclasses)):
		pix.pixels[int((x/5)*2)][int(x%5)] = subclasses[x](None).getColor()

def displayMenu(pix, selectedItem):
	subclasses = PixModule.__subclasses__()
	for x in range(5):
		pix.pixels[int((x/5)*2+1)][int(x%5)] = [0,0,0]
	for x in range(len(subclasses)):
		if x == selectedItem:
			pix.pixels[int((x/5)*2+1)][int(x%5)] = [255,255,255]
	pix.pixels[1] = pix.pixels[1][::-1]
	pix.pixels[3] = pix.pixels[3][::-1]

def test_input_on_pin(pin):
	inpu = 0
	while True:
		if (GPIO.input(pin)):
			inpu = 1
			time.sleep(0.02)
			continue
		else:
			return inpu
	return inpu

def runModuleMenu(spidev):
	# start menu
	pix = PixModule(spidev)
	pix.start()
	displayClasses(pix)
	selectedItem = 0
	try:
		while True:
			displayMenu(pix,selectedItem)
			if(test_input_on_pin(leftPin)): #left (NEXT)
				selectedItem = (1+selectedItem) % len(PixModule.__subclasses__())
			if(test_input_on_pin(rightPin)): #right (ENTER)
				break
			time.sleep(0.05)
	except:
		raise Exception()
	finally:
		pix.stop()
		pix.join()
	return selectedItem

def runSelectedMenu(selectedItem):
	a = 0
	pix = PixModule.__subclasses__()[selectedItem](spidev)
	pix.start()
	try:
		while True:
			if(test_input_on_pin(leftPin)): #left (NEXT)
				pix.left()
				if a < 5:
					a += 1
				else:
					a = 0
			if(test_input_on_pin(rightPin)): #right (ENTER)
				pix.right()
				if a > 4:
					a += 1
				else:
					a = 0
			time.sleep(0.01)
			if a == 10:
				break
	except:
		raise Exception()
	finally:
		pix.stop()
		pix.join()

if __name__ == '__main__':	
	print "Pix gestartet"
	spidev = file("/dev/spidev0.0", "wb")
	try:
		while True:
			# select item
			selectedItem = runModuleMenu(spidev)
			# run item
			runSelectedMenu(selectedItem)
	except Exception as e:
		print e
	print "Pix beendet"

