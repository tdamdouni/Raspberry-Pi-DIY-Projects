# Building a Raspberry Pi Pan/Tilt Face Tracker

_Captured: 2017-05-22 at 10:38 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/electromechanical/building-a-pan-tilt-face-tracker)_

The Mini Pan Tilt is a cool piece of kit for building remote control turrets, but it's even better for pointing a camera towards things. This tutorial will guide you through turning your Raspberry Pi Camera and Mini Pan Tilt kit into a creepy face-tracking camera that will strive to keep your mug right in center frame.

### Step 1: Update your Pi! ( the easy way )

If you don't update your Pi before starting this tutorial, you're going to have a bad time!

Fortunately, it's not too difficult. Type the following command to run our updater from get.pimoroni.com:
    
    
    curl https://get.pimoroni.com/uptodate | bash
    

This will prompt you if you need to reboot, make sure your work is saved and answer Y for yes!

### Step 2: Putting It Together

You should have your Pi, servo driver board, camera and Pan Tilt kit lined up and ready to go.

For the purpose of this guide I'm using the slightly overkill Adafruit Servo Driver Board because it's much better than driving servos directly off the Pi and much, much less hassle than setting up an Arduino as a driver. If you're experienced with driving the Pan/Tilt and have your own preferred method then you can substitute it in the code.

#### Connect the Pan/Tilt

Take the wire from the Pan servo and connect it to Port 0 on the servo driver board. The orange (PWM) wire should be on top, next to the number, the brown (GND) at the bottom and the remaining red in the middle. Connect the Tilt servo to Port 1 in the same fashion.

#### Connect the Servo Driver

Making sure your Pi is turned off, connect the servo driver board. You should connect as follows:

  * VCC -> 3v3 Power
  * SDA -> GPIO 2 / SDA
  * SCL -> GPIO 3 / SCL
  * GND -> Ground

All of these pins are conveniently located on the top left side of the header, so they should be easy enought to find.

#### Connect the Camera

Next you need to connect the camera. Start by attaching the ribbon cable to the camera end- to do this you should use a fingernail to gently slide each side of the connector grip away from the board edge. Tuck the cable into the connector with the blue side facing out towards you, and lock the grip back into place by pushing it firmly.

Likewise, release the grip on your Pi camera connector by pulling it upwards. The camera connector is the one closest to the USB and Ethernet ports, tucked between the HDMI and headphone connector. Make sure the blue side of the ribbon cable is facing towards the USB ports.

#### Attach the Camera to the Pan/Tilt

You're going to have to get a little creative for this step. I used a length of single-core wire, which I threaded through the screw holes on the camera PCB and through the slots in the Pan/Tilt. This actually works pretty well.

I'd recommend against using blue-tac, since it could damage your camera or cable when you try to remove it.

### Step 3: The Software

To get you started, I've created a GitHub repository with software to drive the Camera and PanTilt. It should, hopefully, track your face out of the box.

At this point it's a good idea to make sure you're also looking at your Pi's desktop. The software will create a window for outputting the video from the camera, and this will only work on the desktop.

If you're looking at a terminal, type "startx" to fire up the desktop. Once you're on the desktop, click "LXTerminal" to start up a terminal session, and then you can continue.

#### Install Pre-Requisites

Before you can get started, you'll need to install opencv. This is the library which we'll be using to handle face recognition. Make sure you're sitting in front of a terminal and type:
    
    
    sudo apt-get install python-smbus python-opencv opencv-data
    

#### Clone The Repository

Next, grab the repository from GitHub using the "git" command.
    
    
    git clone https://github.com/pimoroni/PanTiltFacetracker
    cd PanTiltFacetracker
    

This repository includes the Adafruit Servo Driver software, plus a wrapper that abstracts it away into simple "tilt" and "pan" commands that accept a range between 0 and 180 degrees.

"facetracker.py" is the file you're interested in. Run it like so:
    
    
    sudo ./facetracker.py
    
