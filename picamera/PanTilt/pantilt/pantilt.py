#Raspberry-Pi pan and tilt using arrow keys script
#must be run from Pi's terminal!
#use code "python pantilt.py" after you cd into the correct folder!

#By Tucker Shannon @ tucksprojects.com 11-08-16

#importing required libraries
import curses
import os
import time
import picamera

#setting up camera
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()



#activating servo blaster (servod must be in the same folder as this script!)
os.system('sudo ./servod')

#flipping the camera for so its not upside down
camera.vflip = True
camera.hflip = True

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

#setting start up serrvo positions
#positions range from (50-250)
servo1 = 100
servo2 = 100
# print doesn't work with curses, use addstr instead
pic = 1
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            #if q is pressed quit
            break
        if char == ord('p'):
            #if p is pressed take a photo!
            camera.capture('image%s.jpg' % pic)
            pic = pic +1
            screen.addstr(0, 0, 'picture taken! ')
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right ')
            if servo1 > 50:
                servo1 = servo1 -2
            os.system("echo 0=%s > /dev/servoblaster" %servo1) 
            time.sleep(0.005)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            if servo1 < 150:
                servo1 = servo1 +2
            os.system("echo 0=%s > /dev/servoblaster" %servo1) 
            time.sleep(0.005)
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up ')
            if servo2 < 150:
                servo2 = servo2 +2
            os.system("echo 1=%s > /dev/servoblaster" %servo2) 
            time.sleep(0.005)
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            if servo2 > 50:    
                servo2 = servo2 -2
            os.system("echo 1=%s > /dev/servoblaster" %servo2) 
            time.sleep(0.005)
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
