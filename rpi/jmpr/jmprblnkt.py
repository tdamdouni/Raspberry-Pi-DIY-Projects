import sys
import tty
import termios
import numpy
import threading
import random, time
import colorsys

import blinkt as uh

GLOBAL_BRIGHTNESS = .05
uh.set_brightness(GLOBAL_BRIGHTNESS)


#Input defintions
#I found this somewhere for keyboard key usage. Maybe @gadgetoid? Thanks!
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

#Game related stuff

#field color
fieldcolor = [255,255,255]

#fancy jumper colors
jmprcolors = []
for h in [0, 15, 30]:
    jmprcolors.append([int(c*255) for c in colorsys.hsv_to_rgb(h/360.0, 1.0, 1.0)])


class jmpr(threading.Thread):
    def __init__(self):
        self._stopevent = threading.Event()
        self.gameover = 0
        self.score = 0
        self.cycle = .35
        self.field = [[0,0,0]] + [fieldcolor for x in range(7)] 
        self.dot = {"pos":[0,1], "height":0}
        threading.Thread.__init__(self)
        
    def step(self):
        obstacle = random.random()
        if obstacle > .80 and self.field[0] != [0,0,0] and self.field[1] != [0,0,0]:
            self.field.insert(0, [0,0,0])
            self.field.pop()
        else:
            self.field.insert(0, fieldcolor)
            self.field.pop()
        
    def draw(self):
        for c, cell in enumerate(self.field):
            uh.set_pixel(c, cell[0], cell[1], cell[2])
        cycle_jmpr = jmprcolors[self.dot["height"]]
        uh.set_pixel(6, cycle_jmpr[0], cycle_jmpr[1], cycle_jmpr[2], brightness = GLOBAL_BRIGHTNESS*(self.dot["height"]+1))
        #get jmpr back to the ground
        if self.dot["height"] > 0:
            self.dot["height"] -= 1
        #pitfall or no?
        if self.field[6] == [0,0,0] and self.dot["height"] == 0:
            self.gameover = 1
        if self.field[6] == [0,0,0] and self.dot["height"] != 0:
            self.score += 1
            #level up
            if not self.score % 5:
                self.cycle *= .9
        uh.show()
        time.sleep(self.cycle)
        
    def run(self):
        while not self.gameover:
            self.draw()
            self.step()
        self._stopevent.set()
        self.end()
        
    def set_jump(self, press):
        if press == "w":
            if self.dot["height"] < len(jmprcolors)-1:
                self.dot["height"]+=1

    def end(self):
        for p in range(8):
            uh.set_pixel(p, 255,0,0)
            uh.show()
            time.sleep(.02)
        self._stopevent.set()
        
jmpman=jmpr()
jmpman.daemon = 1
jmpman.start()

while 1:
    user_input = readkey()
    if user_input == "x" or jmpman.gameover:
        break
    if user_input != "x":
        jmpman.set_jump(user_input)
    else:
        continue
    

print "You reached level {}! Your score: {}.".format(jmpman.score / 3 + 1, jmpman.score)
jmpman.gameover = 1
jmpman.join()

