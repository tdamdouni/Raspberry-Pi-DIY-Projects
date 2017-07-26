#!/usr/bin/python

# Raspberry Pi and NeoPixel Stock Symbol Price Monitor LEDs
# A simple stock ticker price change monitor of today's positive or negative change using an Adafruit NeoPixel RGB LED Strip
# Shows a full red/green solid color 1x8 matrix

import datetime
import time
import ystockquote
import atexit
import sys
import os
import urllib2

from socket import error as SocketError
import errno

from decimal import *
from neopixel import *

debug = 0

# Stock quote configuration:
tickerSymbol = 'AAPL'

# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 4       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.

def solidColor(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()

def lightsOut():
	# Turn off all the LEDs.
	if debug == 1:
		print ('Turning off all LEDs.')

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()

	for i in range(strip.numPixels()):
		strip.setPixelColor(i, 0)
		strip.show()

def marketClosed():
	print "Stock Market Closed.", now
	lightsOut()
	time.sleep(60)

atexit.register(lightsOut)



if debug == 1:
	allInfo = ystockquote.get_all(tickerSymbol)
	print allInfo
# 	quote = ystockquote.get_change(tickerSymbol)
# 	print quote

# print tickerSymbol + " Price = " + allInfo["price"]
# print tickerSymbol + " Change = " + allInfo["change"]
# print allInfo["change"]

# print allInfo

getcontext().prec = 8

def getQuote(change):
	if debug == 1:
		print "Function getQuote"

	try:
		change = ystockquote.get_change(tickerSymbol)
	except urllib2.HTTPError as err:
		if err.code == 404:
			print "404 ERROR"
		else:
			print "err.code: ", err.code
			# pass
	except SocketError as err:
	    if err.errno == errno.ECONNRESET:
	        print "Connection reset by peer."
	    	pass
	# price = ystockquote.get_price(tickerSymbol)

	while change == 'N/A':
		print "ERROR: NO PRICE CHANGE DATA!"
		time.sleep(60)
		change = ystockquote.get_change(tickerSymbol)

	changedecimal = Decimal(change)
	# pricedecimal = Decimal(price)
	# changedecimal = 0
	print "$ Change: ", changedecimal
	# print pricedecimal

	# lastclose = Decimal(pricedecimal) - Decimal(changedecimal)

	# print lastclose

	# Negative
	if changedecimal < 0:
		LED_BRIGHTNESS = abs(int(round(100 * changedecimal)))
		if LED_BRIGHTNESS > 255:
			LED_BRIGHTNESS = 255
		if debug == 1:
			print "Brightness: ", LED_BRIGHTNESS
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		strip.begin()
		# Colors: GREEN, RED, BLUE
		solidColor(strip, Color(0, 255, 0))

	# Positive
	if changedecimal > 0:
		LED_BRIGHTNESS = int(round(100 * changedecimal))
		if LED_BRIGHTNESS > 255:
			LED_BRIGHTNESS = 255
		if debug == 1:
			print "Brightness: ", LED_BRIGHTNESS
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		strip.begin()
		# Colors: GREEN, RED, BLUE
		solidColor(strip, Color(255, 0, 0))

	# Zero
	if changedecimal == 0:
		if debug == 1:
			print "Zero Change!"
		LED_BRIGHTNESS = 10
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		strip.begin()
		strip.setPixelColor(0, Color(0, 255, 0))
		strip.setPixelColor(1, Color(255, 0, 0))
		strip.setPixelColor(2, Color(0, 255, 0))
		strip.setPixelColor(3, Color(255, 0, 0))
		strip.setPixelColor(4, Color(0, 255, 0))
		strip.setPixelColor(5, Color(255, 0, 0))
		strip.setPixelColor(6, Color(0, 255, 0))
		strip.setPixelColor(7, Color(255, 0, 0))
		strip.show()

	time.sleep(1)

# Main program logic follows:
if __name__ == '__main__':

	try:
		while True:
			now = datetime.datetime.now()
			# print now

			# Between Monday - Friday
			if 0 <= now.weekday() <= 5:
				if debug == 1:
					print "Weekday: ", now.weekday()
				# print now.hour

				# Between 9AM - 5PM
				if now.hour == 9:
					if debug == 1:
						print "Hour 9AM"
					if now.minute >= 30:
						if debug == 1:
							print "Minute 30 or later"
						if 9 <= now.hour <= 17:
							# print "Hour: ", now.hour
							# print now.time()

							if debug == 1:
								print "Calling function getQuote"

							getQuote(0)

					else:
						marketClosed()

				else:
					if 9 <= now.hour <= 15:
						if debug == 1:
							print "Hour between 10AM-4PM"
						# print "Hour: ", now.hour
						# print now.time()

						if debug == 1:
							print "Calling function getQuote"

						getQuote(0)

					else:
						marketClosed()

			else:
				marketClosed()

	except KeyboardInterrupt:
		lightsOut()
		print ' - Exiting'
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
