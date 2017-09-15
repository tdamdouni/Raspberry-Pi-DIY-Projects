#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  Temperature Logger 2
#  Read data from a BMP180 sensor and
#  send to Thingspeak.com account.
#
#  cfg.DISPlay data on a Nokia 5110 Screen
#
# Author : Matt Hawkins
# Date   : 18/10/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------

# General
import time
import os
import sys
import urllib            # URL functions
import urllib2           # URL functions
import RPi.GPIO as GPIO  # GPIO library

# Configuration
import templogger2_cfg as cfg

# I2C/BMP180
import smbus
import bmp180            # Sensor library

# SPI/Nokia
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

def switch1Callback(channel):
  # Called if switch 1 is pressed
  cfg.LCDSTYLE=cfg.LCDSTYLE+1
  if cfg.LCDSTYLE>5:
    cfg.LCDSTYLE=1
  print "Mode:" + str(cfg.LCDSTYLE)
  updateAll(cfg.DISP)

def switch2Callback(channel):
  # Called if switch 2 is pressed
  cfg.LCDCONTRAST = cfg.LCDCONTRAST + 5
  if cfg.LCDCONTRAST>70:
    cfg.LCDCONTRAST = 40
  cfg.DISP.set_contrast(cfg.LCDCONTRAST)
  print "Contrast:" + str(cfg.LCDCONTRAST)

def switch3Callback(channel):
  # Called if switch 3 is pressed
  print "Shutdown"    
  cfg.LCDSTYLE=1
  updateLCD(cfg.DISP,0,0)
  if cfg.AUTOSHUTDOWN==1:
    os.system('/sbin/shutdown -h now') 
  sys.exit(0)
  
def sendData(url,key,field1,field2,temp,pres):
  # Send event to internet site
  values = {'key' : key,'field1' : temp,'field2' : pres}

  postdata = urllib.urlencode(values)
  req = urllib2.Request(url, postdata)

  log = time.strftime("%d-%m-%Y,%H:%M:%S") + ","
  log = log + "{:.1f}C".format(temp) + ","
  log = log + "{:.2f}mBar".format(pres) + ","

  try:
    # Send data to Thingspeak
    response = urllib2.urlopen(req, None, 5)
    html_string = response.read()
    response.close()
    log = log + 'Update ' + html_string

  except urllib2.HTTPError, e:
    log = log + 'Server could not fulfill the request. Error code: ' + str(e.code)
  except urllib2.URLError, e:
    log = log + 'Failed to reach server. Reason: ' + str(e.reason)
  except:
    log = log + 'Unknown error'

  print log

def updateAll(disp,temperature,pressure):
  updateMinMax(temperature,pressure)      
  updateLCD(disp,temperature,pressure)

def updateMinMax(temperature,pressure):
  # Update min max values
  if temperature>cfg.MAXTEMP:
    cfg.MAXTEMP = temperature

  if pressure>cfg.MAXPRES:
    cfg.MAXPRES = pressure

  if temperature<cfg.MINTEMP:
    cfg.MINTEMP = temperature

  if pressure<cfg.MINPRES:
    cfg.MINPRES = pressure

def updateLCD(disp,temp,pres):

  # Create 1-bit colour blank image for drawing.
  image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

  # Get drawing object to draw on image.
  draw = ImageDraw.Draw(image)

  # Load fonts
  scriptpath = os.path.dirname(os.path.abspath(__file__))
  font0 = ImageFont.truetype(scriptpath + '/5x7_practical.ttf', 16)
  font1 = ImageFont.truetype(scriptpath + '/F25_Bank_Printer_Bold.ttf', 18)
  font2 = ImageFont.truetype(scriptpath + '/F25_Bank_Printer_Bold.ttf', 10)  
  font3 = ImageFont.truetype(scriptpath + '/F25_Bank_Printer_Bold.ttf', 20)
  font4 = ImageFont.truetype(scriptpath + '/F25_Bank_Printer_Bold.ttf', 30)

  draw.rectangle((0,0,83,47), outline=255, fill=255)  

  if cfg.LCDSTYLE==1:
    # Temp and Pressure
    draw.text((0,0), "Temperature", font=font0)  
    draw.text((17,10), "{:.1f}".format(temp), font=font1)
    draw.text((0,28), "Pressure", font=font0)   
    draw.text((17,38), "{:.2f}".format(pres) , font=font2)

  if cfg.LCDSTYLE==2:
    # Temp
    draw.text((15,5), "Temperature", font=font0)  
    draw.text((2,15), "{:.1f}".format(temp), font=font4)
  
  if cfg.LCDSTYLE==3:
    # Pressure
    draw.text((20,5), "Pressure", font=font0)  
    draw.text((0,15), "{:.1f}".format(pres), font=font3)

  if cfg.LCDSTYLE==4:
    # Min Max values
    draw.text((0,0),  "Temp", font=font0)  
    draw.text((14,8),  "Min : " + "{:.1f}".format(cfg.MINTEMP), font=font0)
    draw.text((10,16), "Max : " + "{:.1f}".format(cfg.MAXTEMP), font=font0) 
    draw.text((0,24), "Pres", font=font0)  
    draw.text((14,32), "Min : " + "{:.2f}".format(cfg.MINPRES), font=font0)  
    draw.text((10,40), "Max : " + "{:.2f}".format(cfg.MAXPRES), font=font0)

  if cfg.LCDSTYLE>=5:
    # System settings
    draw.rectangle((0,0,83,47), outline=255, fill=255)  
    draw.text((0,0), "IP :" + cfg.IP, font=font0)
    draw.text((0,15), "Contrast :" + str(cfg.LCDCONTRAST), font=font0)    

  disp.image(image)
  disp.display()  

def getip(interface='eth0'):
  # Read ifconfig.txt and extract IP address
  try:
    filename = 'ifconfig_' + interface + '.txt'
    os.system('/sbin/ifconfig ' + interface + ' > /home/pi/' + filename)
    f = open('/home/pi/' + filename, 'r')
    line = f.readline() # skip 1st line
    line = f.readline() # read 2nd line
    line = line.strip()
    f.close()

    if line.startswith('inet addr:'):
      a,b,c = line.partition('inet addr:')
      a,b,c = c.partition(' ')
    else:
      a = 'None'

  except:
    a = 'Error'
    
  return a

def main():
  
  # Setup SPI
  cfg.DISP = LCD.PCD8544(cfg.DC, cfg.RST, spi=SPI.SpiDev(cfg.SPI_PORT, cfg.SPI_DEVICE, max_speed_hz=4000000))

  # Initialize library
  cfg.DISP.begin(contrast=cfg.LCDCONTRAST)

  # Clear cfg.DISPlay
  cfg.DISP.clear()
  cfg.DISP.display()

  # Get IP address
  cfg.IP = getip('wlan0')

  # Setup GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  # Switches setup as inputs pulled HIGH by default
  GPIO.setup(cfg.SWITCH1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(cfg.SWITCH2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(cfg.SWITCH3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  # Define function to call when switch pressed
  GPIO.add_event_detect(cfg.SWITCH1, GPIO.FALLING, callback=switch1Callback, bouncetime=300)
  GPIO.add_event_detect(cfg.SWITCH2, GPIO.FALLING, callback=switch2Callback, bouncetime=300)
  GPIO.add_event_detect(cfg.SWITCH3, GPIO.FALLING, callback=switch3Callback, bouncetime=300)
  
  bus = smbus.SMBus(cfg.SMBUSID)

  # Initial sensor reading
  (temperature,pressure)=bmp180.readBmp180(cfg.DEVICE)  
  
  try:

    while True:
      sendData(cfg.THINGSPEAKURL,cfg.THINGSPEAKKEY,'field1','field2',temperature,pressure)
      sys.stdout.flush()
      
      # 2 second loops
      for i in range(0,cfg.INTERVAL*30):
        time.sleep(2)
        (temperature,pressure)=bmp180.readBmp180(cfg.DEVICE)
        updateAll(cfg.DISP,temperature,pressure)

  except :
    # Reset GPIO settings
    print "error", sys.exc_info()[0]
    GPIO.cleanup()

if __name__=="__main__":
   main()
