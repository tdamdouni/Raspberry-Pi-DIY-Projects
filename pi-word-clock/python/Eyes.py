#!/usr/bin/python
import time,os,datetime,sys,argparse,fonts,I2CGrid,threading,json,random,atexit,signal
#import UnicornGrid
print ("Eyes (0) (0)")
currentAnim='stareAndBlink'
parser=argparse.ArgumentParser()
parser.add_argument("--addressLeft","-al",help="I2C address left eye default is 0x70",default='0x70')
parser.add_argument("--addressRight","-ar",help="I2C address right eye default is 0x71",default='0x71')
parser.add_argument("--brightness","-b",help="LED brightness (0->15) default is 0",default='15')
args=parser.parse_args()

addressLeft=int(args.addressLeft,16)
addressRight=int(args.addressRight,16)
brightness=int(args.brightness,10)
leftEye=I2CGrid.I2CGrid(address=addressLeft,debug=False)
rightEye=I2CGrid.I2CGrid(address=addressRight,debug=False)
leftEye.setBrightness(brightness)
rightEye.setBrightness(brightness)
fonts.eyes=leftEye.rotateFontCCW(fonts.eyes)
fonts.textFont1=leftEye.rotateFontCCW(fonts.textFont1)
scroll=True
message=' Spooky '

#unicorn=UnicornGrid.UnicornGrid()
#unicorn.setBrightness(0.2)
#unicorn.showChar(fonts.eyes['straight'])

#Code to turn the LED off when stopped or killed
def cleanup():
  print 'Terminating'
  leftEye.showChar(fonts.shapes['empty'])
  rightEye.showChar(fonts.shapes['empty'])

atexit.register(cleanup)
signal.signal(signal.SIGTERM,cleanup)

class myThread (threading.Thread):
  def __init__(self, threadID, name, eye, anim):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.eye=eye
      self.anim=anim
  def run(self):
      if scroll:
        if self.name=='left':
          text='   '+message
        else:
          text=message+'   '
        self.eye.scrollString(fonts.textFont1,text,5)
      else:
        self.eye.playAnimation2(fonts.eyes,self.anim)

def loadAnims():
  data={}
  fileName=os.path.dirname(os.path.realpath(__file__))+'/EyeAnimations.json'
  #print os.path.dirname(os.path.realpath(__file__))
  try:
    with open(fileName) as infile:
      data=json.load(infile)
  except EnvironmentError as err:
      print('Oops problem loading JSON! ')
      print (err)
  return data

anims=loadAnims()

def nextAnim():
  global currentAnim,scroll,message
  scroll=False
  r=random.randint(0,30)
  #r=29
  if r==1:
      currentAnim='stareAndBlink'
  elif r==1:
      currentAnim='stareFadeOutIn'
  elif r==2:
    currentAnim='leftABit'
  elif r==3:
    currentAnim='left'
  elif r==4:
    currentAnim='rightABit'
  elif r==5:
    currentAnim='right'
  elif r==6:
    currentAnim='crossEyedMiddle'
  elif r==7:
    currentAnim='growEyes'
  elif r==8:
    currentAnim='flashEyes'
  elif r==9:
    currentAnim='loopLeft'
  elif r==10:
    currentAnim='ghosts1'
  elif r==11:
    message=' Trick or Treat '
    scroll=True
  elif r==12:
    message=' Spooky '
    scroll=True
  elif r>12 and r<15:
    currentAnim='stareAndBlink'
  elif r==15:
    currentAnim='upABit'
  elif r==16:
    currentAnim='downABit'
  elif r==17:
    currentAnim='up'
  elif r==18:
    currentAnim='down'
  elif r==19:
    currentAnim='winkLeft'
  elif r==20:
    currentAnim='winkRight'
  elif r==21:
    currentAnim='growEyes2'
  elif r>21 and r<25:
    currentAnim='growEyes2'
    doFrame()
    doFrame()
  elif r==25:
    currentAnim='downLeftABit'
  elif r==26:
    currentAnim='downRightABit'
  elif r==27:
    currentAnim='upLeftABit'
  elif r==28:
    currentAnim='upRightABit'
  elif r==29:
    currentAnim='roll'

def doFrame():
  threadLeft=myThread(1,'left',leftEye,anims[currentAnim]['left'])
  threadRight=myThread(2,'right',rightEye,anims[currentAnim]['right'])
  threadLeft.start()
  threadRight.start()
  threadLeft.join()
  threadRight.join()

try:
  while True:
    nextAnim()
    doFrame()
finally:
  cleanup()
