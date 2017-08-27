import sys
import tty
import termios
import numpy
import threading
import random, time

from operator import itemgetter
from itertools import groupby

try: 
    import unicornhat as uh
    unicorn = 1
    uh.brightness(.8)
    uh.rotation(180)
except ImportError:
    unicorn = 0

def show_matrix(mat):
    for i in mat:
        print " ".join([str(x[0]) for x in i])    

def makefield():
    field = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append([0,0,0])
        field.append(row)
    return field

fd=''
def readchar():
    global old_settings
    global fd
    fd = sys.stdin.fileno()

    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

level=1
r=[255,0,0]
g=[0,255,0]
b=[0,0,255]
y=[255,255,0]
c = [0,255,255]
colors = [r,g,b]#,y,c]
gameover = 0

class bitris(threading.Thread):
    def __init__(self):
        self.score = 0
        self.gameover = 0
        self.newcol = 0
        self.nextlevel = 10
        self._stopevent = threading.Event()
        self._sleepperiod = 0.5
        self.field = makefield()
        self.activetris = 0
        threading.Thread.__init__(self)

    def run(self):
        while not self._stopevent.isSet():
            if not self.activetris:
                if self.solvetriples():
                    self.draw()
                self.find_gap()
                if self.solvetriples():
                    self.draw()
                self.find_gap()
                self.starttris()
                self.activetris = 1
            self.drop()
            self.draw()
            if self.score > self.nextlevel:
                self._sleepperiod -= 0.1
                self.nextlevel += 10
                if self.newcol == 0:
                    colors.append([255,255,0])
            self._stopevent.wait(0.01)
            if gameover:
                self.end()

    def drop(self):
        """
        each timestep, move the tris one down
        """
        single = 0
        if max(ypos) < 7 and max(xpos) <= 7:
            #only catches if horizontal
            if ypos[0] == ypos[1]:

                if self.field[xpos[0]][ypos[0]+1] == [0,0,0] and self.field[xpos[1]][ypos[1]+1] == [0,0,0] and single == 0:
                    #clean trail up
                    self.field[xpos[0]][ypos[0]] = [0,0,0]
                    self.field[xpos[1]][ypos[1]] = [0,0,0]
                    #drop the tris
                    ypos[0] += 1
                    ypos[1] += 1
                    
                    #if orientation horizontal:
                    self.field[xpos[0]][ypos[0]] = col1
                    
                    #if self.field[xpos[1]][ypos[1]] == [0,0,0]:
                    self.field[xpos[1]][ypos[1]] = col2
                        
                    
                else:
                    self.activetris = 0
            elif ypos[0] == ypos[1]+1 and single == 0: #if vertical
                if self.field[xpos[0]][ypos[0]+1] == [0,0,0]: #if below empty
                    self.field[xpos[0]][ypos[0]] = [0,0,0]
                    self.field[xpos[1]][ypos[1]] = [0,0,0]
                    ypos[0]+=1
                    ypos[1]+=1
                    
                    self.field[xpos[1]][ypos[1]] = col1
                    self.field[xpos[0]][ypos[0]] = col2
                    
                else:
                    
                    self.activetris = 0
                
            else:
                self.activetris = 0    
        else:
            self.activetris = 0    
    
    def draw(self, delay = 0):
        if delay == 0:
            delay = self._sleepperiod
        if unicorn:
            for x in range(8):
                for y in range(8):
                    col = self.field[x][y]
                    uh.set_pixel(x,y,col[0], col[1], col[2])
            uh.show()
            time.sleep(delay)
        else:
            show_matrix(self.field)
            time.sleep(1)
 
    
    def join(self, timeout=None):
          self._stopevent.set( )
          threading.Thread.join(self, timeout)
    
    def find_gap(self):
        matrix = self.field
        tmat = []
        for row in matrix:
            tcol = [x for x in row[::-1] if x != [0,0,0]]
            
            for c in range(len(matrix) - len(tcol)):
                tcol.append([0,0,0])
            tmat.append(tcol[::-1])
            
        if matrix != tmat:
            self.field = tmat
            self.draw()

    def solvetriples(self):
        solve = []
        change = 0
        for col in colors:
            for i, row in enumerate(self.field):
                matches = [z for z, x in enumerate(row) if x == col]
                for k, g in groupby(enumerate(matches), lambda (i,x):i-x):
                    found = map(itemgetter(1), g)
                    if len(found) > 2:
                        change = 1
                        self.score+=len(found)
                        for l in found:
                            if xpos[0] == i and ypos[0] == l:
                                col1 = [0,0,0]
                            if xpos[1] == i and ypos[1] == l:
                                col2 = [0,0,0]
                            solve.append([i,l])
        
        
        tmat = [list(i) for i in zip(*self.field)]
        for col in colors:
            for i, row in enumerate(tmat):
                matches = [z for z, x in enumerate(row) if x == col]
                for k, g in groupby(enumerate(matches), lambda (i,x):i-x):
                    found = map(itemgetter(1), g)
                    if len(found) > 2:
                        change = 1
                        self.score+=len(found)
                        for l in found:
                            if xpos[0] == i and ypos[0] == l:
                                col1 = [0,0,0]
                            if xpos[1] == i and ypos[1] == l:
                                col2 = [0,0,0]
                            solve.append([l,i])
        
        for pos in solve:
            self.field[pos[0]][pos[1]] = [255,255,255]
            self.draw(delay = .015)
            self.field[pos[0]][pos[1]] = [0,0,0]
            
        return change

    def starttris(self):
        global xpos
        global ypos
        global col1
        global col2
        global ori 
        global gameover
        col1 = colors[random.randint(0,len(colors)-1)]
        col2 = colors[random.randint(0,len(colors)-1)]
        if self.field[3][0] == [0,0,0] and self.field[4][0] == [0,0,0]:
            self.field[3][0] = col1
            self.field[4][0] = col2
            xpos = [3,4]
            ypos = [0,0] 
            self.activetris = 1
        else:
            gameover = 1
        
    def movetris(self, press):
        if self.activetris:
            if press == 'a': #left
                if max(ypos) < 7:
                    if xpos[1] > xpos[0]:
                        if xpos[0] > 0:
                            if self.field[xpos[0]-1][ypos[0]] == [0,0,0]:
                                xpos[0] -= 1
                                xpos[1] -= 1
                                self.field[xpos[1]+1][ypos[1]] = [0,0,0]
                                self.field[xpos[0]+1][ypos[0]] = [0,0,0]
                    elif xpos[1] == xpos[0]:
                        if xpos[0] > 0:
                            if self.field[xpos[0]-1][max(ypos)] == [0,0,0]:
                                xpos[0] -= 1
                                xpos[1] -= 1
                                self.field[xpos[1]+1][ypos[1]] = [0,0,0]
                                self.field[xpos[0]+1][ypos[0]] = [0,0,0]
            if press == "d": #right
                if max(ypos) < 7 and max(xpos) < 7:
                    
                    if self.field[max(xpos)+1][max(ypos)] == [0,0,0]:
                        if self.field[max(xpos)+1][max(ypos)+1] == [0,0,0]:
                            if self.field[max(xpos)][max(ypos)+1] == [0,0,0]:
                                xpos[0] += 1
                                xpos[1] += 1
                                self.field[xpos[1]-1][ypos[1]] = [0,0,0]
                                self.field[xpos[0]-1][ypos[0]] = [0,0,0]

    def rotate(self):
        if self.activetris:
            if xpos[0] != xpos[1]: #if horizontal
                if max(ypos) < 7:
                    if self.field[xpos[0]][max(ypos)+1] == [0,0,0]:
                        self.field[xpos[1]][ypos[1]] = [0,0,0]
                        xpos[1] -= 1  
                        ypos[1] -= 1
                        self.field[xpos[0]][ypos[0]] = col1

            else: #if vertical  
                if max(xpos) < 7 and max(ypos) < 7:
                    if self.field[xpos[1]+1][ypos[1]+1] == [0,0,0]:
                        self.field[xpos[1]][ypos[1]] = [0,0,0]
                        xpos[1]+=1
                        ypos[1]+=1

    def end(self):
        for row in range(8):
            for j in range(8):
                uh.set_pixel(row, j, 255,0,0)
                uh.show()
                time.sleep(.001)
        self._stopevent.set()

thread1=bitris()
thread1.daemon = 1
thread1.start()

while 1:
    if gameover:
       if thread1._stopevent.isSet():
            thread1.join()
            break
        
    if thread1.gameover==True:
        print "GAMEOVER"
        break

    user_input = readkey()
    if user_input=='a':
        if xpos[0] > 0:
            thread1.movetris(press = user_input)
    if user_input=='d':
        if max(xpos) < 7:
            thread1.movetris(press = user_input)
    if user_input=='w':
        thread1.rotate()
    if user_input == 'x':
        thread1.gameover = 1
    if ypos[0] == 7:
        thread1.activetris = 0
    if ypos[1] == 7:
        thread1.activetris = 0
    elif user_input=='t':
        thread1.join() 
    else:
        continue
thread1.join()
