#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           Temperature Logger
#  Read data from a BMP180 sensor and
#  send to Thingspeak.com account.
#
# Author : Matt Hawkins
# Date   : 20/06/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
import smbus
import time
import os
import sys
import urllib            # URL functions
import urllib2           # URL functions

import bmp180            # Sensor library
import RPi.GPIO as GPIO  # GPIO library

################# Default Constants #################
# These can be changed if required
DEVICE        = 0x77 # Default device I2C address
SMBUSID       = 1    # Rev 2 Pi uses 1, Rev 1 uses 0
LEDGPIO       = 17   # GPIO for LED
SWITCHGPIO    = 22   # GPIO for switch
INTERVAL      = 1    # Delay between each reading (mins)
AUTOSHUTDOWN  = 1    # Set to 1 to shutdown on switch
THINGSPEAKKEY = 'ABCDEFGH12345678'
THINGSPEAKURL = 'https://api.thingspeak.com/update'
#####################################################

def switchCallback(channel):

  global AUTOSHUTDOWN

  # Called if switch is pressed
  if AUTOSHUTDOWN==1:
    os.system('/sbin/shutdown -h now')
  sys.exit(0)

def sendData(url,key,field1,field2,temp,pres):
  """
  Send event to internet site
  """

  values = {'api_key' : key,'field1' : temp,'field2' : pres}

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
    log = log + 'Server could not fulfill the request. Error code: ' + e.code
  except urllib2.URLError, e:
    log = log + 'Failed to reach server. Reason: ' + e.reason
  except:
    log = log + 'Unknown error'

  print log

def main():

  global DEVICE
  global SMBUSID
  global LEDGPIO
  global SWITCHGPIO
  global INTERVAL
  global AUTOSHUTDOWN
  global THINGSPEAKKEY
  global THINGSPEAKURL

  # Check if config file exists and overwrite
  # default constants with new values
  if os.path.isfile('/boot/templogger.cfg')==True:
    print "Found templogger.cfg"
    f = open('/boot/templogger.cfg','r')
    data = f.read().splitlines()
    f.close()
    if data[0]=='Temp Logger':
      print "Using templogger.cfg"
      DEVICE        = int(data[1],16)
      SMBUSID       = int(data[2])
      LEDGPIO       = int(data[3])
      SWITCHGPIO    = int(data[4])
      INTERVAL      = int(data[5])
      AUTOSHUTDOWN  = int(data[6])
      THINGSPEAKKEY = data[7]
      THINGSPEAKURL = data[8]

  # Setup GPIO
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  # LED on GPIO17
  GPIO.setup(LEDGPIO , GPIO.OUT)
  # Switch on GPIO22 as input pulled LOW by default
  GPIO.setup(SWITCHGPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  # Define what function to call when switch pressed
  GPIO.add_event_detect(SWITCHGPIO, GPIO.RISING, callback=switchCallback)

  bus = smbus.SMBus(SMBUSID)

  try:

    while True:
      GPIO.output(LEDGPIO, True)
      (temperature,pressure)=bmp180.readBmp180(DEVICE)
      sendData(THINGSPEAKURL,THINGSPEAKKEY,'field1','field2',temperature,pressure)
      sys.stdout.flush()

      # Toggle LED while we wait for next reading
      for i in range(0,INTERVAL*60):
        GPIO.output(LEDGPIO, not GPIO.input(LEDGPIO))
        time.sleep(1)

  except :
    # Reset GPIO settings
    GPIO.cleanup()

if __name__=="__main__":
   main()
