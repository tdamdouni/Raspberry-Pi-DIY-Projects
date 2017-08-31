#!/usr/bin/python
#
#     Lightweight Motion Detection using python picamera libraries
#        based on code from raspberry pi forum by user utpalc
#        modified by Claude Pageau for this working example
#     ------------------------------------------------------------
# original code on github https://github.com/pageauc/picamera-motion

# This is sample code that can be used for further development

verbose = True
if verbose:
    print "Loading python libraries ....."
else:
    print "verbose output has been disabled verbose=False"

import picamera
import picamera.array
import datetime
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fractions import Fraction

#Constants
SECONDS2MICRO = 1000000  # Constant for converting Shutter Speed in Seconds to Microseconds

# User Customizable Settings
imageDir = "images"
imagePath = "/home/pi/pimotion/" + imageDir
imageNamePrefix = 'capture-'  # Prefix for all image file names. Eg front-
imageWidth = 1980
imageHeight = 1080
imageVFlip = False   # Flip image Vertically
imageHFlip = False   # Flip image Horizontally
imagePreview = False

numberSequence = False

threshold = 10  # How Much pixel changes
sensitivity = 100  # How many pixels change

nightISO = 800
nightShutSpeed = 6 * SECONDS2MICRO  # seconds times conversion to microseconds constant

# Advanced Settings not normally changed 
testWidth = 100
testHeight = 75

def checkImagePath(imagedir):
    # Find the path of this python script and set some global variables
    mypath=os.path.abspath(__file__)
    baseDir=mypath[0:mypath.rfind("/")+1]
    baseFileName=mypath[mypath.rfind("/")+1:mypath.rfind(".")]

    # Setup imagePath and create folder if it Does Not Exist.
    imagePath = baseDir + imagedir  # Where to save the images
    # if imagePath does not exist create the folder
    if not os.path.isdir(imagePath):
        if verbose:
            print "%s - Image Storage folder not found." % (progName)
            print "%s - Creating image storage folder %s " % (progName, imagePath)
        os.makedirs(imagePath)
    return imagePath

def takeDayImage(imageWidth, imageHeight, filename):
    if verbose:
        print "takeDayImage - Working ....."
    with picamera.PiCamera() as camera:
        camera.resolution = (imageWidth, imageHeight) 
        # camera.rotation = cameraRotate #Note use imageVFlip and imageHFlip variables
        if imagePreview:
            camera.start_preview()
        camera.vflip = imageVFlip
        camera.hflip = imageHFlip
        # Day Automatic Mode
        camera.exposure_mode = 'auto'
        camera.awb_mode = 'auto'
        camera.capture(filename)
    if verbose:  
        print "takeDayImage - Captured %s" % (filename)
    return filename

def takeNightImage(imageWidth, imageHeight, filename):
    if verbose:
        print "takeNightImage - Working ....."
    with picamera.PiCamera() as camera:
        camera.resolution = (imageWidth, imageHeight) 
        if imagePreview:
            camera.start_preview()
        camera.vflip = imageVFlip
        camera.hflip = imageHFlip
        # Night time low light settings have long exposure times 
        # Settings for Low Light Conditions 
        # Set a frame rate of 1/6 fps, then set shutter
        # speed to 6s and ISO to approx 800 per nightISO variable
        camera.framerate = Fraction(1, 6)
        camera.shutter_speed = nightShutSpeed
        camera.exposure_mode = 'off'
        camera.iso = nightISO
        # Give the camera a good long time to measure AWB
        # (you may wish to use fixed AWB instead)
        time.sleep(10)
        camera.capture(filename)
    if verbose:  
        print "checkNightMode - Captured %s" % (filename)
    return filename

def takeMotionImage(width, height, daymode):
    with picamera.PiCamera() as camera:
        time.sleep(1)
        camera.resolution = (width, height)
        with picamera.array.PiRGBArray(camera) as stream:
            if daymode:
                camera.exposure_mode = 'auto'
                camera.awb_mode = 'auto' 
            else:
                # Take Low Light image            
                # Set a framerate of 1/6 fps, then set shutter
                # speed to 6s and ISO to 800
                camera.framerate = Fraction(1, 6)
                camera.shutter_speed = nightShutSpeed
                camera.exposure_mode = 'off'
                camera.iso = nightISO
                # Give the camera a good long time to measure AWB
                # (you may wish to use fixed AWB instead)
                time.sleep( 10 )
            camera.capture(stream, format='rgb')
            return stream.array

def scanIfDay(width, height, daymode):
    data1 = takeMotionImage(width, height, daymode)
    while not motionFound:
        data2 = takeMotionImage(width, height, daymode)
        pCnt = 0L;
        diffCount = 0L;
        for w in range(0, width):
            for h in range(0, height):
                # get the diff of the pixel. Conversion to int
                # is required to avoid unsigned short overflow.
                diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
                if  diff > threshold:
                    diffCount += 1
            if diffCount > sensitivity:
                break; #break outer loop.
        if diffCount > sensitivity:
            motionFound = True
        else:
            # print "Sum of all pixels=", pxCnt
            data2 = data1              
    return motionFound
           
def scanMotion(width, height, daymode):
    motionFound = False
    data1 = takeMotionImage(width, height, daymode)
    while not motionFound:
        data2 = takeMotionImage(width, height, daymode)
        diffCount = 0L;
        for w in range(0, width):
            for h in range(0, height):
                # get the diff of the pixel. Conversion to int
                # is required to avoid unsigned short overflow.
                diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
                if  diff > threshold:
                    diffCount += 1
            if diffCount > sensitivity:
                break; #break outer loop.
        if diffCount > sensitivity:
            motionFound = True
        else:
            data2 = data1              
    return motionFound

def getFileName(imagePath, imageNamePrefix, currentCount):
    rightNow = datetime.datetime.now()
    if numberSequence :
        filename = imagePath + "/" + imageNamePrefix + str(currentCount) + ".jpg"
    else:
        filename = "%s/%s%04d%02d%02d-%02d%02d%02d.jpg" % ( imagePath, imageNamePrefix ,rightNow.year, rightNow.month, rightNow.day, rightNow.hour, rightNow.minute, rightNow.second)
    return filename    

def motionDetection():
    print "Scanning for Motion threshold=%i sensitivity=%i ......"  % (threshold, sensitivity)
    isDay = True
    currentCount= 1000
    while True:
        if scanMotion(testWidth, testHeight, isDay):
            filename = getFileName(imagePath, imageNamePrefix, currentCount)
            if numberSequence:
                currentCount += 1
            if isDay:
                takeDayImage( imageWidth, imageHeight, filename )
            else:
                takeNightImage( imageWidth, imageHeight, filename )
             
if __name__ == '__main__':
    try:
        motionDetection()
    finally:
        print ""
        print "+++++++++++++++"
        print "Exiting Program"
        print "+++++++++++++++" 
        print ""        

    
    
    
