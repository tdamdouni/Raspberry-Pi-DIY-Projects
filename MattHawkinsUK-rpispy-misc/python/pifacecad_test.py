#!/usr/bin/python
#--------------------------------------
#
#            Raspberry Pi
#     PiFace Control & Display
#
# Test the PiFace Control & Display
# switches (S1-S5)
#
# Author : Matt Hawkins
# Date   : 25/08/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import PiFace library
import pifacecad as pf

cad = pf.PiFaceCAD()
cad.lcd.backlight_on()

cad.lcd.clear()

cad.lcd.write("Press a switch")

while True:

  for x in range(5):
    if cad.switches[x].value==1:
      cad.lcd.clear()
      cad.lcd.write("Switch " + str(x+1))