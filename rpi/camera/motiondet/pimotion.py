import picamera
import numpy as np
import time
import picamera.array
import datetime

w = 50
h = 50
threshold = int(w*h*255*3*0.1)

def getframe():
    with picamera.PiCamera() as camera:
        time.sleep(.5)
        camera.resolution = (w, h)
        camera.exposure_mode = "auto"
        camera.awb_mode = "auto"
   
        with picamera.array.PiRGBArray(camera) as output:
            camera.capture(output, 'rgb')
            return output.array


    
def checkMotion(a, b):
    ar = np.array([])
    for i in range(w):
        for j in range(h):
            for channel in [0,1,2]: 
                ar = np.append(ar, abs(int(a[j][i][channel]) - int(b[j][i][channel])))
    if np.sum(ar) > threshold:
        #print "Movement!"
        motion = 1
    else:
        motion = 0
        #print "Nothing to see, carry on!"
            
    return motion
    
def takepic():
    with picamera.PiCamera() as camera:
        camera.vflip = 1
        camera.hflip = 1
        camera.resolution = (800, 600)
        time.sleep(.5)
        fname = 'motion_{}.jpg'.format(datetime.datetime.utcnow())
        camera.capture(fname)
        print "Capture: " + fname
    return 0
    
    
if __name__ == "__main__":
    a = []
    b = []
    while 1:
        a = getframe()
        if b != []:
            mot = checkMotion(a, b)
            if mot: 
                takepic()
        b = a
        
        time.sleep(5)
        

