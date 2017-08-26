from __future__ import print_function
import time
from papirus import Papirus
import RPi.GPIO as GPIO
from eink_images import drawImage_forecast, drawImage_sunInfo, drawImage_next2Days, drawImage_tempGraph, drawImage_weatherAlert

import forecastio as f
from apikey import api_key

# Set up display
papirus = Papirus()
papirus.clear()

# Get initial weather forecast
lat = 50.755600
lng = -1.297771
forecast = f.load_forecast(api_key, lat, lng, units='si')
print("[INFO] Weather update: {h:02d}:{m:02d}:{s:02d}".format(h=time.localtime().tm_hour, m=time.localtime().tm_min, s=time.localtime().tm_sec))

# Initial image
img = drawImage_forecast(forecast)
papirus.display(img)
papirus.update()

weather_update = time.time()
display_update = time.time()
secondary_display = time.time()
return_to_default = False # Boolean to decide whether to return to default image. Set to True after secondary display shown.

# Set up buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)
# GPIO 26 is first from left
# GPIO 19 is second from left
# GPIO 20 is third from left
# GPIO 16 is fourth from left
# GPIO 21 is fifth from left

while True:
	try:
		# Update weather forecast every 5 minutes
		if (time.time() - weather_update) > 5*60:
			try: # sometimes getting the forecast fails, if it does fail then wait for next time
				forecast = f.load_forecast(api_key, lat, lng, units='si')
				print("[INFO] Weather update: {h:02d}:{m:02d}:{s:02d}".format(h=time.localtime().tm_hour, m=time.localtime().tm_min, s=time.localtime().tm_sec))
				update_display = 'full'
			except:
				print("[WARNING] Weather update failed: {h:02d}:{m:02d}:{s:02d}".format(h=time.localtime().tm_hour, m=time.localtime().tm_min, s=time.localtime().tm_sec))
				pass
			weather_update = time.time()

		# Draw image
		img = drawImage_forecast(forecast)
		papirus.display(img)
		
		if GPIO.input(26) == False:
			img = drawImage_sunInfo(forecast)
			papirus.display(img)
			papirus.update()
			secondary_display = time.time()
			return_to_default = True
		
		if GPIO.input(19) == False:
			img = drawImage_next2Days(forecast)
			papirus.display(img)
			papirus.update()
			secondary_display = time.time()
			return_to_default = True
		
		if GPIO.input(20) == False:
			img = drawImage_tempGraph(forecast)
			papirus.display(img)
			papirus.update()
			secondary_display = time.time()
			return_to_default = True
		
		if GPIO.input(21) == False:
			img = drawImage_weatherAlert(forecast)
			papirus.display(img)
			papirus.update()
			secondary_display = time.time()
			return_to_default = True

		# Revert to default display 10 seconds after showing secondary
		if time.time() - secondary_display > 10 and return_to_default:
			papirus.update()
			return_to_default = False
		
		# Update default display every 30 seconds
		if time.time() - display_update > 30:
			papirus.partial_update()
			display_update = time.time()

	except KeyboardInterrupt:
		papirus.clear()
		break
