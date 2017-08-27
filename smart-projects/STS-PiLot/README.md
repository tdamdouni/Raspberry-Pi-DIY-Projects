# STS-PiLot
AJAX remote control web interface with live video for the [Pimoroni STS-Pi](https://shop.pimoroni.com/products/sts-pi) and other robotics projects.
This is an educational application with the focus on keeping the code simple and understandable.
The live streaming part is based on the example code provided by Miguel Grinberg https://github.com/miguelgrinberg/flask-video-streaming. For better stability and performance network connectivity is provided by the [Gevent](http://www.gevent.org) WSGI server.
Pictures and videos on the Hackaday.io project page: https://hackaday.io/project/20149-sts-pilot-robotics-remote-control

## Features
* Responsive (portrait and landscape mode) AJAX interface for use on desktops, laptops, tablets and phones.
* Designed for [Pimoroni STS-Pi](https://shop.pimoroni.com/products/sts-pi) and [Explorer Hat Pro](https://shop.pimoroni.com/products/explorer-hat) as hardware interface, but can be adapted for other boards.
* Frontend requires only HTML, Javascript and CSS - no proprietary plugins needed.
* Works without modification when no Raspberry Pi camera is detected - But you are missing something!
* Easy web-API to control the robot from your own application.
* API provides JSON readout of analog and digital inputs.
* API provides both "tank track" style (Y-Y) and joystick style (X-Y) interface.
* Robot stops automatically when connection is lost.
* Data and video connection is automatically reestablished after connection loss.
* Threaded (fast, low latency) capture interface.
* Alternative non-threaded (slower, low CPU usage) video capture for lower spec. computers like the Raspberry Pi Zero.
* Use camera_cv.py for standard webcams (requires python-opencv).
* Use io_wrapper_dummy.py for IO board emulation.

## Requirements
* STS-Pi with Raspberry Pi and Explorer Hat Pro
* Computer / Tablet / Phone with web browser that supports MJPEG
* Tested with the following browsers:  
Linux and Windows: Firefox, Chrome and Opera.  
Android (5.1 on Fairphone 2): Lightning, IceCat Mobile, Chromium.  
CAVEAT: MS Edge and Internet Explorer do not support MJPEG natively.  
Apple Safari and iOS browsers have limited or broken MJPEG support.  
Please use one of the tested browsers instead.

## Install Dependencies (Picamera, Flask, Gevent, Simplejson)
sudo apt-get install python-picamera python-flask python-gevent python-simplejson
For generic webcam support (camera_cv.py) add: sudo apt-get install python-opencv python-pil

## Install Explorer Hat support (not needed for io_wrapper_dummy.py)
follow these instructions: https://github.com/pimoroni/explorer-hat

## Install STS-PiLot
Clone or download the application into a directory of your choice:
git clone https://github.com/mark-orion/STS-PiLot.git
You can update the already cloned application from within its directory:  
git remote update  
git pull

## Running the program (as normal user, no "sudo" required)  
cd STS-PiLot  
python app.py  

## Start the program automatically while booting
cd STS-PiLot  
chmod +x autostart.sh  
open /etc/rc.local with your preferred editor and add the following line BEFORE the last line reading "exit 0":  
/home/pi/STS-PiLot/autostart.sh  
You may have to change the path if your STS-PiLot lives at another location.  
Restart the STS-Pi and test if program starts at boot:  
The green LED will flash quickly for about 1 second to indicate STS-PiLot has started.

## Using STS-PiLot
The web interface runs on port 5000 of the Raspberry Pi. You can access it via http://ip_goes_here:5000 or at http://hostname.local:5000 if you have Avahi / mDNS running on your Pi and the client. Hostname is the hostname of your STS-Pi that can be changed with raspi-config (advanced settings).  
http://ip_goes_here:5000/?video=300 Opens the slower, non-threaded interface. This interface will grab a single video frame at the given interval in milliseconds (300 in the example).  
http://ip_goes_here:5000/?video=n opens the interface without live video.  
Using the webinterface is fairly easy:  
At the center you have the live video with the controls for the two motors to the left and to the right. In portrait mode the controls appear under the video.  
Tapping / clicking on the motor controls sets the forward or reverse speed of the motor.  
For ease of use a quick double click / tap will set the speed for both motors simultaneously. A single tap / click in the center (video) area of the screen will immediately stop the motors - emergency stop!  
The coloured tiles numbered 1-4 at the bottom of the screen control the corrosponding touchpads / LEDs on the Explorer Hat.
Pads 1 and 2 (blue, yellow) control output 1 and 2 of the Explorer Hat.  
Touching pad 3 (red) on the screen or the physical device immobilizes the device by toggling the "chocks".  
The orange "HUD" button toggles the Status Display (HUD).

## Shutting down the STS-Pi with pad 4 (green LED)
The STS-Pi can be shut down completely by activating the "chocks" (red LED flashing) and then pad 4 (green LED flashing). The shutdown will happen after a few seconds and can be interrupted by releasing the chocks (touching pad 3 again).  

## Web API / URLs to control the robot

### URL example for "half speed forward": http://192.168.1.17:5000/motor?l=50&r=50

### /motor?l=[speed]&r=[speed]
Set speed for the motors (l=left, r=right). Usable values: -100 (full reverse) to 0 (stop) to 100 (full forward).

### /joystick?x=[xaxis]&y=[yaxis]
Two axis interface for the motors. Usable values: -100 (full left/down) to 0 (center) to 100 (full right/up).

### /heartbeat
Resets watchdog timer. All systems stop (chocks_on) if not called every 10 seconds (default setting).  
Returns JSON object with analog and digital input (Sensor) readouts.

### /touchpad?pad=[1-4]
Toggles Explorer Hat touchpads 1-4 and LEDs. 1 and 2 control output 1 and 2 as well.

### /video_feed.mjpg
No frills, bells and whistles MJPEG video feed from the camera.

### /single_frame.jpg
Non threaded (low CPU) single frame JPEG output.

### /
The root serves the web interface itself.

### /?video=n
Calls the web interface without live video enabled.

### /?video=[msecs]
Use non-threaded video with [msecs] delay between frames.

## Files
* app.py - the main application.
* config.py - application wide global variables.
* camera_pi.py - camera module for RPi camera module.
* camera_cv.py - camera module for generic (web)cams.
* io_wrapper.py - IO wrapper configured for Explorer HAT/pHAT.
* io_wrapper_dummy.py - Dummy IO wrapper (no hardware required).
* autostart.sh - script to start the program via /etc/rc.local.
* static - this folder contains HTML, CSS and javascript files for the web interface.
* client - example programs to control your STS-PiLot instance from another computer.

Enjoy! Mark Dammer, Forres, Scotland 2017
