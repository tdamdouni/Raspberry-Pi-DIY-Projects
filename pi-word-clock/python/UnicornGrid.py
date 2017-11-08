#!/usr/bin/python

import datetime,time,unicornhat,LEDGrid

class UnicornGrid(LEDGrid.LEDGrid):

  def __init__(self,debug=False):
    LEDGrid.LEDGrid.__init__(self,debug)
  
  def showChar(self,c):
    for x in range(8):
      for y in range(8):
        if c[y] & 1<<(7-x):
          self.setPixel(x,y,self.fg[0],self.fg[1],self.fg[2])
        else:
          self.setPixel(x,y,self.bg[0],self.bg[1],self.bg[2])
    unicornhat.show()


  def setBrightness(self,brightness):
    unicornhat.brightness(brightness)

  def setPixel(self,x, y, r, g, b):
    unicornhat.set_pixel(x,y , r, g, b)

  def show(self):
    unicornhat.show()

  