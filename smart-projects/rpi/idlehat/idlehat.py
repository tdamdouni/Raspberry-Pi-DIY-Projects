import unicornhat as uh
import random, time

uh.brightness(.3)

def randomizr():
    for i in range(8):
        for j in range(8):
            color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
            uh.set_pixel(i,j,color[0], color[1], color[2])
    uh.show()
    while 1:
        color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        uh.set_pixel(random.randint(0,7), random.randint(0,7), color[0], color[1], color[2])
        uh.show()
        time.sleep(.05)
        
def uniformr():
    while 1:
        pix = int(abs(random.gauss(4, 2)))
        oc = uh.get_pixel(0, pix)
        for i in range(8):
            uh.set_pixel(i, pix, oc[0]+1, oc[1]+1, oc[2]+1)
        uh.show()

def langtonant():
    #for i in range(32):
    #    uh.set_pixel(random.randint(0,7), random.randint(0,7), 255, 255, 255)
    antpos = [random.randint(0,7), random.randint(0,7)]
    antdir = random.randint(0,3) #0 up, 1 r, 2 down, 3 l
    while 1:
        atpos = uh.get_pixel(antpos[0], antpos[1])
        if atpos == (255,255,255):
            antdir = (antdir +1) % 4
            uh.set_pixel(antpos[0], antpos[1], 0,0,0)
            print "white", antdir, antpos[0], antpos[1]
        elif atpos  == (0,0,0):
            antdir = (antdir -1) % 4
            uh.set_pixel(antpos[0], antpos[1], 255,255,255)
            print "black", antdir, antpos[0], antpos[1]
        if antdir == 0:
            antpos = [antpos[0]%8, (antpos[1]+1)%8]
        if antdir == 1:
            antpos = [(antpos[0]+1)%8, (antpos[1])%8]
        if antdir == 2:
            antpos = [antpos[0]%8, (antpos[1]-1)%8]
        if antdir == 3:
            antpos = [(antpos[0]-1)%8, antpos[1]%8]
        uh.show()
        time.sleep(.005)
            
            
    
    

if __name__ == "__main__":
    #randomizr()
    #uniformr()
    langtonant()
