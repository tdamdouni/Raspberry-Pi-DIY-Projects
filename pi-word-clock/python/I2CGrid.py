#!/usr/bin/python

import datetime,time,LEDGrid
from Adafruit_I2C import Adafruit_I2C

class I2CGrid(LEDGrid.LEDGrid):

  i2c=None

  def __init__(self,address=0x70,debug=False):
    LEDGrid.LEDGrid.__init__(self,debug)
    self.i2c=Adafruit_I2C(address=address)
    self.i2c.write8(0x21,0x00)
    self.i2c.write8(0x81,0x00)
    self.i2c.write8(0xe0 | 0x01,0x00)
  
  def showChar(self,c):
    bytes=[]
    for item in c:
      bytes.append( ((item & 0xFE)>>1)|((item & 0x01)<<7) )
      bytes.append(0x00)
      self.i2c.writeList(0x00,bytes)


  def setBrightness(self,brightness):
    self.i2c.write8(0xe0|brightness,0x00)