# Raspberry Pi Shutdown / Restart Button

_Captured: 2017-08-25 at 10:04 from [www.hackster.io](https://www.hackster.io/glowascii/raspberry-pi-shutdown-restart-button-d5fd07?ref=similar&ref_id=50988&offset=5)_

![Raspberry Pi Shutdown / Restart Button](https://hackster.imgix.net/uploads/attachments/335000/_DEqLJOi6rp.Z?auto=compress%2Cformat&w=900&h=675&fit=min)

I'm helping to build some [crazy singing Tesla coils](https://www.coupdefoud.re/) for Burning Man, and we're having trouble with our controllers, so I've researched how to set up a script that runs in the background and can shut down or restart the Pi. This should help prevent data corruption (hopefully!). It's super quick and easy!

Grab a momentary switch (push button) and cut a female-female jumper wire in half. Strip the cut ends, and solder them to the button's terminals. Place these female connectors on pin 18 and a GND pin.

If you want separate "shut down" and "reboot" buttons, do this twice, and place the second one on pin 23 and another GND pin.

![](https://hackster.imgix.net/uploads/attachments/334361/img_5808_L3keW4IYPj.JPG?auto=compress%2Cformat&w=680&h=510&fit=max)

> _I've marked my Pi's GND pins with Sharpie, to help with identification._

We're going to follow, modify, and add to [this tutorial by Inderpreet Singh](https://www.element14.com/community/docs/DOC-78055/l/adding-a-shutdown-button-to-the-raspberry-pi-b).

Do everything he says about creating the **Scripts** folder and the **shutdown_pi.py** file. However, we're going to modify it a bit:
    
    
    #!/bin/python 
    # Simple script for shutting down the raspberry Pi at the press of a button. 
    # by Inderpreet Singh 
    import RPi.GPIO as GPIO  
    import time  
    import os  
    # Use the Broadcom SOC Pin numbers 
    # Setup the Pin with Internal pullups enabled and PIN in reading mode. 
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    # Our function on what to do when the button is pressed 
    def Shutdown(channel):  
       os.system("sudo shutdown -h now")  
    def Restart(channel):
       os.system("sudo shutdown -r now")
    # Add our function to execute when the button pressed event happens 
    GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
    GPIO.add_event_detect(23, GPIO.FALLING, callback = Restart, bouncetime = 2000) 
    # Now wait! 
    while 1:  
       time.sleep(1) 
    

All we've done here is add the Restart code, in case you wanted it.

Next, to make it auto-run, I found that it was unclear where to place the extra Python code in the **rc.local** file. So, after saving and exiting, go to:
    
    
    sudo nano /etc/rc.local
    

And then place this line *before the final `exit 0` *:
    
    
    python /home/pi/Scripts/shutdown_pi.py &
    

(You apparently don't need the sudo here, either, since **rc.local** runs as root.)

...Annnd, ta-dah! You're done! Save and quit. To test this, go run
    
    
    sudo shutdown -r now
    

in your console, wait for it to reboot, and test your button-pushing skills. I bet you're a pro. _Here's a testing video, just for fun:_
