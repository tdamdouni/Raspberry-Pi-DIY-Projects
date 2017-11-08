#!/usr/bin/python

import UnicornGrid,fonts,time,WordClock,datetime,argparse

print ("Pi Word Clock")
parser=argparse.ArgumentParser()
parser.add_argument("--demo","-d",help="run through some example times",action="store_true")
parser.add_argument("--brightness","-b",help="LED brightness (0.0->1.0) default is 0.2",default='0.2')

args=parser.parse_args()
grid=UnicornGrid.UnicornGrid()
grid.bg=[0x00,0x00,0x00]
grid.fg=[0x00,0x00,0xff]
grid.setBrightness(float(args.brightness))
#demoAnim=['smile','heart1','heart1F','heart2','heart2F']
#grid.playAnimation(fonts.shapes,demoAnim,speed=0.1)
#grid.scrollStringH(fonts.textFont1," GurgleApps.com Word Clock ",speed=4)

wordClock=WordClock.WordClock(grid)
wordClock.randomColorChange=True
#grid.rotateFontCCW(fonts.clockFont1)

if args.demo:
    print ('demo mode on' )  
    while True:
      wordClock.demoTimeList(fonts.clockFont1,1.75)

while True:
    wordClock.showTime(fonts.clockFont1,datetime.datetime.now())