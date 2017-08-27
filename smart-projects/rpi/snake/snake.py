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
    uh.brightness(.5)
    uh.rotation(0)
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

bodyc = [[255,0,0]]
for i in range(63):
    bodyc.append([0,255,255])

class snake(threading.Thread):
    def __init__(self):
        self.body = [[4,4], [4,5], [4,6]]
        self.direction = 2
        self._stopevent = threading.Event()
        self.bitten = 0
        self.outofbounds = 0
        self.gameover = 0
        self.apple = [2,2]
        self.score = 0
        self.freedoms = [x for x in [0,1,2,3] if x != self.direction] 
        self.cycle = .5
        threading.Thread.__init__(self)
        
        
    def move(self):
        prior = self.body[0]
        if self.direction == 0: #up
            n = [prior[0], prior[1]+1]
        if self.direction == 1: #right
            n = [prior[0]+1, prior[1]]
        if self.direction == 2: #down
            n = [prior[0], prior[1]-1]
        if self.direction == 3: #left
            n = [prior[0]-1, prior[1]]
        if n in self.body:
            self.gameover = 1
        if n[0] < 0 or n[0] > 7 or n[1] < 0 or n[1] > 7:
            self.outofbounds = 1
        if n not in self.body and n != self.apple:
            self.body.insert(0, n)
            c = self.body.pop()
            uh.set_pixel(c[0], c[1], 0,0,0)
        if n not in self.body and n == self.apple:
            uh.set_pixel(self.apple[0], self.apple[1], 255,255,255)
            self.body.insert(0, n)
            self.score+=1
            print self.score
            if not self.score % 5:
                print "speedup"
                self.cycle -= .1
            self.apple = [random.randint(0,7), random.randint(0,7)]
        self.freedoms = [x for x in [0,1,2,3] if x != self.direction]
    
    def eat(self):
        return 0
        
    def draw(self):
        if not self.outofbounds:
            for i, part in enumerate(self.body):
                #if part[0] <8 and part[1] < 8 and part[0] >= 0 and part[1] >= 0:
                uh.set_pixel(part[0], part[1], bodyc[i][0], bodyc[i][1], bodyc[i][2])
            uh.set_pixel(self.apple[0], self.apple[1], 255, 255, 0)
            uh.show()
            time.sleep(self.cycle)
        else:
            self.gameover = 1

    def run(self):
        while not self.gameover:
            self.move()
            #self.direction = random.choice([x for x in [0,1,2,3] if x != self.direction])
            self.draw()
        #self.explode()
        self._stopevent.set()
        self.explode()
        if self.gameover:
            self.end()
        
    def join(self, timeout=None):
          self._stopevent.set( )
          threading.Thread.join(self, timeout)

    def set_direction(self, press):
        olddirection = self.direction
        if press == "a":
            if self.direction != 3:
                self.direction = 1
        if press == "d":
            if self.direction != 1:
                self.direction = 3
        if press == "s":
            if self.direction != 0:
                self.direction = 2
        if press == "w":
            if self.direction != 2:
                self.direction = 0
        else:
            self.direction = self.direction
    
    def explode(self):
        for c in range(4):
            for i, part in enumerate(self.body):
                uh.set_pixel(part[0], part[1], 255, 255, 255)
            uh.show()
            time.sleep(.1)
            for i, part in enumerate(self.body):
                uh.set_pixel(part[0], part[1], 255, 0, 0)
            uh.show()
            time.sleep(.1)
    def end(self):
        for row in range(8):
            for j in range(8):
                uh.set_pixel(row, j, 255,0,0)
                uh.show()
                time.sleep(.001)
        uh.clear()
        uh.show()
        self._stopevent.set()  
         


if __name__ == "__main__":
    user_input = ""
    while user_input != "x":
        thread1=snake()
        thread1.daemon = 1
        thread1.start()

        while 1:
            
            user_input = readkey()
            if user_input == "x":
                thread1.gameover = 1
                thread1.join()
                print "thread gameover"
                break
            if thread1._stopevent.isSet():
                #user_input = "x"
                thread1.gameover = 1
                thread1.join()
                print "thread stopevent"
                break
            if user_input != "x":
                thread1.set_direction(user_input)
                print "normal move"
           
            else:
                continue

        thread1.gameover = 1
        thread1.join()
