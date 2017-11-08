#!/usr/bin/python
import datetime,time,LEDGrid,random

class WordClock:

  myGrid=None
  colors=None

  def __init__(self,grid):
    print('WordClick init:')
    self.myGrid=grid
    self.colors=[grid.colors['red'],grid.colors['blue'],grid.colors['green'],grid.colors['pink'],grid.colors['purple'],grid.colors['orange']]
    self.randomColorChange=False
    self.colorChangeEvery=5.0
    self.colorLastChanged=time.time()

  def showTime(self,font=None,now=time.time()):
    if self.randomColorChange and time.time()-self.colorLastChanged>self.colorChangeEvery:
      self.colorLastChanged=time.time()
      self.myGrid.fg=random.choice(self.colors)
    timeString='It is '
    words=[]
    hour=now.hour
    minute=now.minute
    if minute>=5 and minute <10:
        words=['m_5']
    elif minute>=10 and minute <15:
        words=['m_10']
    elif minute>=15 and minute <20:
        words=['m_15']
    elif minute>=20 and minute <25:
        words=['m_20']
    elif minute>=25 and minute <30:
        words=['m_25']
    elif minute>=30 and minute <35:
        words=['m_30']
    elif minute>=35 and minute <40:
        words=['m_25']
    elif minute>=40 and minute <45:
        words=['m_20']
    elif minute>=45 and minute <50:
        words=['m_15']
    elif minute>=50 and minute <55:
        words=['m_10']
    elif minute>=55 and minute <60:
        words=['m_5']
    if minute>=5 and minute<35:
        words.append('past')
    if minute >=35 and minute<60:
        words.append('to')
        hour+=1
    if hour>12:
        hour-=12
    if hour==0:
        hour=12
    words.append('h_'+str(hour))
    #words=['m_20','past','h_10']
    chars=[]
    for w in words:
        chars.append(font[w])
    self.myGrid.showChar(self.merge(chars))

  def demoTimeList(self,font=None,delay=1,times=[[1,5],[2,10],[3,15],[4,30],[4,35],[5,40],[6,45],[7,50],[8,55],[9,0],[10,5],[11,15],[12,30]],colors=None):
    if (colors==None):
      colors=self.colors
    remCol=self.myGrid.fg
    col=0;
    for t in times:
        self.myGrid.fg=colors[col]
        col=(col+1) % (len(colors)-1)
        tempTime= datetime.datetime.combine(datetime.date.today(),datetime.time(t[0],t[1],0))
        self.showTime(font,tempTime)
        time.sleep(delay)
    self.myGrid.fg=remCol

  def merge(self,words):
    char=[0,0,0,0,0,0,0,0]
    for w in words:
        for x in range(0,8):
            char[x]=char[x] | w[x]
    return char

  def rotateFontCCW(self,font):
    for c in font:
        font[c]=self.myGrid.rotateCCW(font[c])

