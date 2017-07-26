import sys
import pygame
from pygame import locals
from picamera import PiCamera
from time import sleep, time
import subprocess 
import os
import shlex
import glob
import tweepy  

# 2 commands needed to make the ramdisk if planning to run from ramdisk to gain some speed
# sudo mkdir /mnt/ramdisk
# sudo mount -t tmpfs -o size=50m tmpfs /mnt/ramdisk

#folder = "/mnt/ramdisk/"
folder = "/home/pi/chromaCam/"

fuzzpercent = "20%"

width = 640
height = 480

# Consumer keys and access tokens, used for OAuth  
consumer_key = 'YOUR KEY HERE'  
consumer_secret = 'YOUR KEY HERE'  
access_token = 'YOUR KEY HERE'  
access_token_secret = 'YOUR KEY HERE'

# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
   
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)

# create Picamera instance
camera = PiCamera()

# create a (hopefully) unique part for saved files.
leader = str(time())
print("leader is "+ leader)

# use glob to catalog all .jpg files in the folder to get the backgrounds

bgimages = glob.glob(folder + 'background/*.jpg')
print ("len bgimages : " + str(len(bgimages)))
for x in range(0,len(bgimages)):
    os.remove(bgimages[x])
print("deleted images")
sleep(0.1)


bgimages = glob.glob(folder + 'sourcebg/*.jpg')
print("bgimages is "+str(bgimages))
for x in range(0, len(bgimages)):
    sections = bgimages[x].split("/")
    bgimage = sections[len(sections)-1]
    print("background is "+bgimage)
    commandis = 'convert'
    commandis = "convert "+folder+"sourcebg/"+bgimage+"  -resize "+str(width)+"x"+str(height)+ " "+folder+"background/"+bgimage

    print("\n\r")
    os.system(commandis)
    
bgimages = glob.glob(folder + 'background/*.jpg')

print(bgimages)
bgnum = len(bgimages)
print("bgnum is " + str(bgnum))


# set up pygame 
pygame.init()
screen = pygame.display.set_mode((width,height),)
pygame.display.set_caption("chromaCam")

# set camera resolution
camera.resolution = (width, height)
camera.vflip = True

# variable use to stay in while unless QUIT is executed
running = True

# do first capture to use to get Chroma Key
camera.capture(folder+'imagecam.png')

# Get Chroma Key RGB value for top left corner (10 pixels in and 10 pixels down)
command_line = "/usr/bin/convert -limit thread 4 "+folder+"imagecam.png[1x1+10+10] -format '%[fx:int(255*r)],%[fx:int(255*g)],%[fx:int(255*b)]' info:"
args = shlex.split(command_line)
print(args)
out = subprocess.Popen(args, stdout=subprocess.PIPE)
output,err = out.communicate()
print(str(output))
stroutput = str(output)
start = stroutput.split("'")
print(start)
rgb = start[0].split(",")
print(rgb)
red =int(rgb[0])
green = int(rgb[1])
blue = int(rgb[2])
print (red)
print (green)
print (blue)

print ("red is" + str(hex(red)))
redh = str(hex(red))
greenh = str(hex(green))
blueh = str(hex(blue))

print("redh is " + redh)
print("greenh is " + greenh)
print("blueh is " + blueh)

print("redh most right " + redh[len(redh)-1])
print("led redh " + str(len(redh)))

if len(redh) == 3:
    redhash = "0" + redh[len(redh)-1]
else:
    redhash = str(redh[2:])
print("redhash is " + redhash)    

if len(greenh) == 3:
    greenhash = "0" + greenh[len(greenh)-1]
else:
        greenhash = str(greenh[2:])
print("greenhash is " + greenhash)  

if len(blueh) == 3:
    bluehash = "0" + blueh[len(blueh)-1]
else:
        bluehash = str(blueh[2:])

print("bluehash is " + bluehash)  
rgbnum = redhash + greenhash + bluehash
print (rgbnum)

savenum=1
imagenum = 0 

imagebg = pygame.image.load(bgimages[imagenum])
imageover = pygame.image.load(folder+"WimJam13Nov16.png")

changebg =""
dotweet = ""

pygame.joystick.init()
try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print('Enabled joystick: ' + j.get_name())
    joystick  = True
except pygame.error:
    print('no joystick found.')
    joystick = False
    

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
                # change the background
                if event.key == pygame.K_LEFT:
                    changebg = "left"
                
                # change the background
                if event.key == pygame.K_RIGHT:
                    changebg = "right"
                
                # Save the current image
                if event.key == pygame.K_RETURN:
                    dotweet = True

                if event.key == pygame.K_q:
                    running = False
        print("checking gaempad")
        
        if  joystick == True:
            if event.type == pygame.locals.JOYBUTTONDOWN:
                print ("button down"+str(event.button))
                print(" Gamepad button pressed")
                if event.button == 2:
                    changebg = "left"
                if event.button == 1:
                    changebg = "right"
                    
                if event.button == 0:
                    dotweet = True

                if event.button == 9:
                    running = False




# Change the background                    
    if changebg == "left":
        imagenum = imagenum -1
        if imagenum == -1:
            imagenum = bgnum-1
        imagebg = pygame.image.load(bgimages[imagenum])

    if changebg == "right":
        imagenum = imagenum + 1
        if imagenum == bgnum:
            imagenum = 0
        imagebg = pygame.image.load(bgimages[imagenum])

    # reset cghangebg so it doesn't keep changing
    changebg =""

# Send the Tweet
    if dotweet == True:
        savedimage = folder+"saved/chroma"+leader+str(savenum)+".jpg"
        pygame.image.save(screen,savedimage)
        savenum = savenum+1
        
        tweet_text = "Having fun at Wimbledon Raspberry Jam #RJam"  
        photo_path = savedimage

        api.update_with_media(photo_path, status=tweet_text)  

        print("image saved")

    dotweet = False
    
    # capture image
    camera.capture(folder+'imagecam.png')
    # add transparency to image based on sample from above.  
    print("get transparent image")
    commandis = '/usr/bin/convert -limit thread 4 ' + folder +'imagecam.png -fuzz '+fuzzpercent+' -transparent "#'+rgbnum +' " ' + folder + 'imagecamt.png'
    print (commandis)
    os.system('/usr/bin/convert -limit thread 4 ' + folder +'imagecam.png -fuzz '+fuzzpercent+' -transparent "#'+rgbnum +' " ' + folder + 'imagecamt.png')  
    # load image so pygame can display it
    print("Add the images together")
    imagebg = pygame.image.load(bgimages[imagenum])
    imagecam = pygame.image.load(folder+'imagecamt.png')
    imageover = pygame.image.load(folder+'overlay_640.png')
    screen.fill((255,255,255))
    screen.blit(imagebg,(0,0))
    screen.blit(imagecam,(0,0))
    screen.blit(imageover,(0,0))
    pygame.display.update()
    print("all added")
    
