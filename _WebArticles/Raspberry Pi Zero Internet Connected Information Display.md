# Raspberry Pi Zero Internet Connected Information Display 

_Captured: 2015-12-18 at 00:01 from [frederickvandenbosch.be](http://frederickvandenbosch.be/?p=1365)_

![IMG_0477](http://frederickvandenbosch.be/wp-content/uploads/2015/12/IMG_0477-950x713.jpg)

> _Home Guides Raspberry Pi Zero Internet Connected Information Display_

After [last week's Pi Zero mod](http://frederickvandenbosch.be/?p=1343), I thought I'd try a slightly more useful project. Using an Adafruit OLED display, two push buttons, a wifi dongle and a Pi Zero, I made an internet connected information display. The information could be anything: time and date, weather, social media status, etc … The two push buttons are used to cycle through the data and trigger certain actions.

The hardware consists of the following components:

  * Raspberry Pi Zero
  * Edimax wifi dongle
  * 2 large push buttons

The wiring of the OLED and buttons is rather straightforward, as is illustrated below:

![Screen Shot 2015-12-11 at 09.41.55](http://frederickvandenbosch.be/wp-content/uploads/2015/12/Screen-Shot-2015-12-11-at-09.41.55-300x218.png)

> _[Screen Shot 2015-12-11 at 09.41.55](http://frederickvandenbosch.be/wp-content/uploads/2015/12/Screen-Shot-2015-12-11-at-09.41.55.png)_

The wifi dongle is connected the same way as I did previously with the USB hub:

  * Pi Zero PP1 to dongle 5V
  * Pi Zero PP6 to dongle GND
  * Pi Zero PP22 to dongle D+
  * Pi Zero PP23 to dongle D-

Finally, to keep everything in place, I designed a simple enclosure just large enough to fit everything in. A back panel is screwed in place to keep all components inside, exposing the power input microUSB port on the side.

![IMG_0479](http://frederickvandenbosch.be/wp-content/uploads/2015/12/IMG_0479-300x225.jpg)

![IMG_0480](http://frederickvandenbosch.be/wp-content/uploads/2015/12/IMG_0480-300x225.jpg)

A bit of kapton tape prevents exposed contacts to touch each other and keeps the wiring in place. The wifi dongle is positioned at the top for better connectivity. Its bright blue LED shines through the enclosure, giving a clear indication on its status and activity.

The files for the 3D printable enclosure can be found on thingiverse: <http://www.thingiverse.com/thing:1193350>

For the software side of the project, I started off by creating the microSD card using the latest Raspbian Jessie image available. I booted it from the [Pi Zero/USB hub combo](http://frederickvandenbosch.be/?p=1343) with keyboard and wifi dongle connected. I'm using this approach because this project's Pi Zero's USB port has been hardwired to a wifi dongle and a keyboard can no longer be connected.

I configured the wifi by adding the correct SSID and passphrase in the _/etc/network/interfaces_ file. After testing the wifi connectivity, I put the microSD card back in the correct Pi. With network connectivity, it is possible to log in using SSH and work on the script to display the desired information.

Using the Adafruit OLED SSD1306 Python Library and some custom Python code, I programmed three different displays:

  * Time & date
  * Network settings
  * Social media subscribers/followers

The left button cycles through the different screens, while the right button triggers a custom action per screen.

In the case of the time and date display, the button simply toggles between 12h and 24h representation. For the network settings, it forces the wifi to reconnect by bringing down the interface and forcing it up again. Finally, to avoid excessive traffic, social media information is only retrieved every five minutes, pressing the button forces the retrieval of information.

Of course, this is only a subset of what could be displayed. You could fetch weather information, email, latest tweets, etc … You could also have it cycle through the different screen without the need of pushing a button. Anything is possible.

The current code can be found below. It's far from perfect, but gets the job done.

Finally, to get it to start automatically at boot time, create a launcher script (e.g. "launcher.sh") containing the path to the script, like so:
    
    
    #!/bin/sh
    cd /home/pi
    sudo python info_display.py &

And lastly, add the cronjob using the "sudo crontab -e" command:
    
    
    @reboot sh /home/pi/launcher.sh

Every time the Pi is booted, the script will be launched.

Did you like this project? You would like to see a specific project? Let me know in the comments!

```Python
#!/usr/bin/env python

# @RaspberryPi

# https://gist.github.com/fvdbosch/d8968325fa5d756045c3#file-infodisplay-py

# http://frederickvandenbosch.be/?p=1365

import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
import Image
import ImageFont
import ImageDraw
import os

def display_time():
	# Collect current time and date
	if(time_format):
		current_time = time.strftime("%I:%M")
	else:
		current_time = time.strftime("%H:%M")
		
	current_date = time.strftime("%d/%m/%Y")

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 35)

	# Position time
	x_pos = (disp.width/2)-(string_width(font,current_time)/2)
	y_pos = 2 + (disp.height-4-8)/2 - (35/2)
        
	# Draw time
	draw.text((x_pos, y_pos), current_time, font=font, fill=255)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 8)

	# Position date
	x_pos = (disp.width/2)-(string_width(font,current_date)/2)
	y_pos = disp.height-10

	# Draw date
	draw.text((x_pos, y_pos), current_date, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_social():
	# Collect social media subscribers/followers/... by parsing webpages
	twitter = os.popen("curl https://twitter.com/f_vdbosch?lang=en | grep 'data-nav=\"followers\"' | grep -o '[0-9]\+'").read()
	youtube = os.popen("curl https://www.youtube.com/c/FrederickVandenbosch | grep -o '[0-9]\+ subscribers' | grep -o '[0-9]\+'").read()
	facebook = "0"
	instagram = os.popen("curl https://www.instagram.com/f_vdbosch/ | grep -o '\"followed_by\":{\"count\":[0-9]\+}' | grep -o '[0-9]\+'").read()
	googleplus = "0"

	# Put data in lists that can be iterated over
	channels = ["YouTube", "Twitter", "Facebook", "Instagram", "Google+"]
	subscribers = [youtube, twitter, facebook, instagram, googleplus]

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	font = ImageFont.truetype('Minecraftia.ttf', 8)

	# Iterate over lists
	for i in range(0, 5):
		# Position channel name
		x_pos = 2
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw channel name
		draw.text((x_pos, y_pos), channels[i], font=font, fill=255)

		# Position subcribers/followers/...
		x_pos = disp.width - 2 - string_width(font, subscribers[i])
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw subcribers/followers/...
		draw.text((x_pos, y_pos), subscribers[i], font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_network():
	# Collect network information by parsing command line outputs
	ipaddress = os.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
	netmask = os.popen("ifconfig wlan0 | grep 'Mask' | awk -F: '{print $4}'").read()
	gateway = os.popen("route -n | grep '^0.0.0.0' | awk '{print $2}'").read()
	ssid = os.popen("iwconfig wlan0 | grep 'ESSID' | awk '{print $4}' | awk -F\\\" '{print $2}'").read()

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 12)
        
        # Position SSID
        x_pos = 2
	y_pos = 2

	# Draw SSID
	draw.text((x_pos, y_pos), ssid, font=font, fill=255)
	
	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 8)

	# Position IP
	y_pos += 12 + 10 
        
	# Draw IP
	draw.text((x_pos, y_pos), "IP: "+ipaddress, font=font, fill=255)

	# Position NM
	y_pos += 10 

	# Draw NM
	draw.text((x_pos, y_pos), "NM: "+netmask, font=font, fill=255)

	# Position GW
	y_pos += 10

	# Draw GW
	draw.text((x_pos, y_pos), "GW: "+gateway, font=font, fill=255)
	
	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_custom(text):
	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 8)
        
        # Position SSID
        x_pos = (width/2) - (string_width(font,text)/2)
	y_pos = (height/2) - (8/2)

	# Draw SSID
	draw.text((x_pos, y_pos), text, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()
	
def string_width(fontType,string):
	string_width = 0

	for i, c in enumerate(string):
		char_width, char_height = draw.textsize(c, font=fontType)
		string_width += char_width

	return string_width

# Set up GPIO with internal pull-up
GPIO.setmode(GPIO.BCM)	
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
# 128x64 display with hardware I2C
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)

# Initialize library
disp.begin()

# Get display width and height
width = disp.width
height = disp.height

# Clear display
disp.clear()
disp.display()

# Create image buffer with mode '1' for 1-bit color
image = Image.new('1', (width, height))

# Load default font
font = ImageFont.load_default()

# Create drawing object
draw = ImageDraw.Draw(image)

prev_millis = 0
prev_social = 0
display = 0
time_format = True

while True:
	millis = int(round(time.time() * 1000))

	# Software debouncing
	if((millis - prev_millis) > 250):
		# Cycle through different displays
		if(not GPIO.input(12)):
			display += 1
			if(display > 2):
				display = 0
			prev_millis = int(round(time.time() * 1000))

		# Trigger action based on current display
		elif(not GPIO.input(16)):
			if(display == 0):
				# Toggle between 12/24h format
				time_format =  not time_format
				time.sleep(0.01)
			elif(display == 1):
				# Reconnect to network
				display_custom("reconnecting wifi ...")
				os.popen("sudo ifdown wlan0; sleep 5; sudo ifup --force wlan0")
				time.sleep(0.01)
			elif(display == 2):
				# Refresh social media now
				display_custom("fetching data ...")
				display_social()
				time.sleep(0.01)
			prev_millis = int(round(time.time() * 1000))

	if(display == 0):
		display_time()
		prev_social = 0
	elif(display == 1):
		display_network()
		prev_social = 0
	elif(display == 2):
		# Only fetch social media data every 5 minutes when active
		if((millis - prev_social) > 300000):
			display_custom("fetching data ...")
			display_social()
			prev_social = millis

	time.sleep(0.1)
```
