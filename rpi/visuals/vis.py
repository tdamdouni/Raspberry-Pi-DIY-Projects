import unicornhat as uh
import time, math, colorsys 
uh.brightness(.5)

def sinfun(x,y,step):
    print math.sin(x*math.pi)
    return math.sin(x*math.pi)
        
def t(x,y,step):
    
    uh.set_pixel(x,y,int(abs(sinfun(x,y,step))*255),0,0)
    return 0

def swirl(x, y, step):
    x -= 4
    y -= 4

    dist = math.sqrt(pow(x, 2)+pow(y,2)) / 2.0
    angle = (step / 10.0) + (dist * 3)
    
    

    s = math.sin(angle);
    c = math.cos(angle);    
    
    xs = x * c + y * s;
    ys = x * s - y * c;

    r = abs(xs + ys)
    r = r * 64.0
    r -= 20
    
    return (r, r + (s * 130), r + (c * 130))

def set_half_pixel(x,y,r,g,b):
    xrem = x%1
    yrem = y%1
    x = int(x-xrem)
    y = int(y-yrem)
    rem_r = int(xrem*r)
    rem_g = int(xrem*g)
    rem_b = int(xrem*b)
    r = r-rem_r
    g = g-rem_g
    b = b-rem_b
    print x,y, r,g,b, rem_r, rem_g, rem_b
    uh.set_pixel(x,y,r,g,b)
    uh.set_pixel(x+1, y+1, rem_r, rem_g, rem_b)

def rotate(x,y, angle):
    angle = math.pi/2.0
    xs = x*math.cos(angle) + y*math.sin(angle)
    ys = -x*math.sin(angle) + y*math.cos(angle)
    return xs, ys

if __name__ == "__main__":
    step = 0
    
    setpix = [[4,3], [4,4], [5,3], [5,4]]
    for s in setpix:
        uh.set_pixel(s[0], s[1], 0,0,255)
    uh.show()
    time.sleep(2)
    angle = 0
    
    for x in range(8):
        for y in range(8):
            if uh.get_pixel(x,y) != (0,0,0):
                uh.set_pixel(x,y,0,0,0)
                xs, ys = rotate(x,y,angle)
                set_half_pixel(xs,ys,0,0,255)
    uh.show()
    time.sleep(5)



