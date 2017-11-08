#!/usr/bin/python

import datetime,time,random,colorsys

class LEDGrid:

  debug=False
  bg=[0x00,0x00,0x00]
  fg=[0xFF,0xFF,0xFF]
  colors={
  'red':[0xff,0x00,0x00],
  'blue':[0x00,0x00,0xff],
  'green':[0x00,0xff,0x00],
  #'yellow':[0xff,0xff,0x00],
  'pink':[0xff,0x00,0xff],
  #'cyan':[0x00,0xff,0xff],
  'orange':[0xff,0x96,0x00],
  #'lime':[0x96,0xff,0x00],
  'purple':[0x66,0x00,0xff],
  }

  def __init__(self,debug=False):
    self.debug=debug
  
  def showChar(self,c):
    pass

  def playAnimation(self,font,animation,speed=1):
    delay=0.5**speed
    for frame in animation:
      self.showChar(font[frame])
      time.sleep(delay);

  def playAnimation2(self,font,animation):
    for frame in animation:
      self.setBrightness(frame['b'])
      self.showChar(font[frame['name']])
      time.sleep(frame['delay']);


  def scrollString(self,font,message='hello',speed=1,spacing=0):
    delay=0.5 ** speed
    length=len(message)
    charRange=range(length-1)
    for charPos in charRange:
      leftChar=font[message[charPos]]
      rightChar=font[message[charPos+1]]
      for shift in range(8+spacing):
        bytes=[0,0,0,0,0,0,0,0]
        for col in range(8):
          if col>=shift:
            bytes[col]=leftChar[col-shift]
          elif col<shift-spacing:
            bytes[col]=rightChar[col-shift+spacing]
          else:
            bytes[col]=0
        self.showChar(bytes)
        time.sleep(delay)

  def scrollStringH(self,font,message='hello',speed=1,spacing=0):
    delay=0.5 ** speed
    length=len(message)
    charRange=range(length-1)
    for charPos in charRange:
      leftChar=font[message[charPos]]
      rightChar=font[message[charPos+1]]
      for shift in range(8+spacing):
        bytes=[0,0,0,0,0,0,0,0]
        for col in range(8):
          bytes[col]=bytes[col]|leftChar[col]<<shift
          bytes[col]=bytes[col]|rightChar[col]>>8-shift;
        self.showChar(bytes)
        time.sleep(delay)


  def scrollStringOld(self,font,message='hello',speed=1):
    delay=0.5 ** speed
    length=len(message)
    charRange=range(length-1)
    for charPos in charRange:
      leftChar=font[message[charPos]]
      rightChar=font[message[charPos+1]]
      for shift in range(8):
        bytes=[0,0,0,0,0,0,0,0]
        for col in range(8):
          if col>=shift:
            bytes[col]=leftChar[col-shift]
          else:
            bytes[col]=rightChar[col-shift+8]
        self.showChar(bytes)
        time.sleep(delay)

  def scrollStringDown(self,font,message='hello',speed=1):
    delay=0.5 ** speed
    length=len(message)
    charRange=range(length)
    for charPos in charRange:
      leftChar=font[message[charPos]]
      rightChar=font[message[charPos+1]]
      for shift in range(8):
        bytes=[0,0,0,0,0,0,0,0]
        for col in range(8):
          bytes[col]=bytes[col]|leftChar[col]<<shift
          self.showChar(bytes)
        time.sleep(delay)


  def setBrightness(self,brightness):
    pass

  def printHex(self,c):
    for x in c:
      print ('0x{0:0=2x}'.format(x))

  @staticmethod
  def randomColor():
    s=0.8
    v=random.random();
    h=0.1*v
    rgb=colorsys.hsv_to_rgb(h,s,v)
    r = int(rgb[0]*255.0)
    g = int(rgb[1]*255.0)
    b = int(rgb[2]*255.0)
    return [r,g,b]

  @staticmethod
  def randomColourFromSet():
    c=random.sample(LEDGrid.colors,1)[0]
    #print (c)
    return LEDGrid.colors[c]

  @staticmethod
  def rotateFontCW(font):
    for c in font:
        font[c]=LEDGrid.rotateCW(font[c])

  @staticmethod
  def rotateFontCCW(font):
    for c in font:
        font[c]=LEDGrid.rotateCCW(font[c])

  @staticmethod
  def flipX(c):
    result=[0,0,0,0,0,0,0,0]
    for x in range(0,8):
      for y in range(0,8):
        temp=7-x
        result[x]=result[x] | (c[temp] & 0x01<<y) >> 0
    return result

  @staticmethod
  def flipFontX(f):
    result=[0,0,0,0,0,0,0,0]
    for l in f:
      f[l]=LEDGrid.flipX(f[l])
    return f

  @staticmethod
  def rotateFontCCW(f):
    result=[0,0,0,0,0,0,0,0]
    for l in f:
      f[l]=LEDGrid.rotateCCW(f[l])
    return f

  @staticmethod
  def rotateCCW(c):
    result=[0,0,0,0,0,0,0,0]
    for x in range(0,8):
      for y in range(0,8):
        #print '{0:2d} {1:2d} {2:8b} {3:0=8b}'.format(x,y,c[x],(c[x]&0x01<<y))
        result[x]=result[x] | ( (c[y] & 0x01<<x) >> x <<y)
    return result

  @staticmethod
  def rotateCW(c):
    result=[0,0,0,0,0,0,0,0]
    for x in range(0,8):
      for y in range(0,8):
        result[x]=result[x] | ( (c[7-y] & 0x01<<x) >> x <<y)
    return result
