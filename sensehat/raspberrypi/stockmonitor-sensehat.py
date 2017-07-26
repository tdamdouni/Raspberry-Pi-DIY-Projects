#!/usr/bin/python

# Raspberry Pi and Sense Hat Stock Symbol Price Monitor
# A simple stock ticker price change monitor of today's positive or negative change using the Sense Hat
# Shows a full red/green solid color 8x8 matrix

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

from sense_hat import SenseHat

sense = SenseHat()

debug = 0

# Stock quote configuration:
tickerSymbol = 'AAPL'


# Define functions which animate LEDs in various ways.

def lightsOut():
	# Turn off all the LEDs.
	if debug == 1:
		print ('Turning off all LEDs.')

	sense.clear()

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
		if LED_BRIGHTNESS < 50:
			LED_BRIGHTNESS = 50
		if debug == 1:
			print "Brightness: ", LED_BRIGHTNESS
		sense.clear([LED_BRIGHTNESS, 0, 0])

	# Positive
	if changedecimal > 0:
		LED_BRIGHTNESS = int(round(100 * changedecimal))
		if LED_BRIGHTNESS > 255:
			LED_BRIGHTNESS = 255
		if LED_BRIGHTNESS < 50:
			LED_BRIGHTNESS = 50
		if debug == 1:
			print "Brightness: ", LED_BRIGHTNESS
		sense.clear([0, LED_BRIGHTNESS, 0])

	# Zero
	if changedecimal == 0:
		if debug == 1:
			print "Zero Change!"
		sense.clear([50, 50, 50])

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
