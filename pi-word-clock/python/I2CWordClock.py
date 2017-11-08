#!/usr/bin/python
import time,os,datetime,sys,getopt,argparse,fonts,I2CGrid,WordClock


def demo(message='',font=None,delay=1):
    for m in message:
        grid.showChar(font[m])
        time.sleep(delay)


def demoAllTimes(font=None,grid=None,delay=0.5):
    for m in range(0,720,5):
        tempTime= datetime.datetime.combine(datetime.date.today(),datetime.time(1,0,0))+datetime.timedelta(minutes=m)
        showTime(font,grid,tempTime)
        time.sleep(delay)

def demoQuick(font=None,grid=None,delay=1):
    for m in range(0,720,65):
        tempTime= datetime.datetime.combine(datetime.date.today(),datetime.time(1,0,0))+datetime.timedelta(minutes=m)
        showTime(font,grid,tempTime)
        time.sleep(delay)

def demoTimeList(font=None,grid=None,delay=1,times=[[1,5],[2,10],[3,15],[4,30],[4,35],[5,40],[6,45],[7,50],[8,55],[9,0],[10,5],[11,15],[12,30]]):
    for t in times:
        tempTime= datetime.datetime.combine(datetime.date.today(),datetime.time(t[0],t[1],0))
        showTime(font,grid,tempTime)
        time.sleep(delay)
        
print ("I2C Pi Word Clock")

parser=argparse.ArgumentParser()
parser.add_argument("--demo","-d",help="run through some example times",action="store_true")
parser.add_argument("--address","-a",help="I2C address default is 0x70",default='0x70')
parser.add_argument("--brightness","-b",help="LED brightness (0->15) default is 0",default='0')
args=parser.parse_args()

address=int(args.address,16)
brightness=int(args.brightness,10)
grid=I2CGrid.I2CGrid(address=address,debug=False)
wordClock=WordClock.WordClock(grid)
grid.setBrightness(brightness)
wordClock.rotateFontCCW(fonts.clockFont1)
#fonts.printFont(fonts.clockFont1)
fonts.shapes=grid.rotateFontCCW(fonts.shapes)
#fonts.textFont1=grid.flipFontX(fonts.textFont1)
#fonts.printFont(fonts.textFont1)
#grid.scrollString(textFont1,"{}[]~^|ABCDEFGHIJKLMNOPQRSTUVWXYZ=@<>\"'#?()+*!:\/_-0123456789abcdefghijklmnopqrstuvwxyz",speed=4)

grid.rotateFontCCW(fonts.textFont1)
#fonts.printFont(fonts.textFont1)

if args.demo:
    print ('demo mode on' )  
    demoAnim=['smile','heart1','heart1F','heart2','heart2F','empty']
    grid.playAnimation(fonts.shapes,demoAnim,speed=0.1)
    grid.scrollString(fonts.shapes,demoAnim,speed=4,spacing=1)
    while True:
        demoTimeList(fonts.clockFont1,grid,1.75)

grid.scrollString(fonts.textFont1," GurgleApps.com Word Clock ",speed=4)    
while True:
    wordClock.showTime(fonts.clockFont1,datetime.datetime.now())
    
