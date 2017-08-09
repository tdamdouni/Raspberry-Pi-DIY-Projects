# Pi Cam Part 1

_Captured: 2017-03-27 at 22:44 from [hackmypi.com](https://hackmypi.com/PiCamPart1.php)_

by MWAGNER

![](https://hackmypi.com/images/PiCam/FinishedMounted.jpg)

**Raspberry Pi Security System Part 1: The camera.**

A family member asked me to put a camera in our garage recently, and immediately I decided to use a Pi Zero. Back when I was interviewing for my current job, I was dabbling with the idea of making a wireless, battery powered IP camera that I was going to attach to my dog, and get some cool footage of my dog running around. I never fully finished that project because, at the time, giving the Pi Zero wifi involved either soldering on a wifi chip to the bottom of the Pi, or using the MicroUSB port. Also, at the time, battery powering a Pi Zero project was a bit outside my skillset.

Recently, with the help of Red Bear Labs, I was able to make a few of these IP cameras. I started the build back before the Pi Zero W came out, so this hardware guide is how to build one of these cameras on the Pi Zero 1.3. This project will be part 1 of a multi-part project, incorporating a few Pi zero's, a Pi 3, some software and some hardware. Ending, hopefully, with a fully functional security system that notifies the owner when there is movement.

#### **Hardware you'll need: **

![](https://hackmypi.com/images/PiCam/Parts.jpg)

> _A Raspberry Pi Zero 1.3_

  * ![](https://hackmypi.com/images/PiCam/PiPart.jpg)

> _Red Bear IoT pHAT_

  * ![](https://hackmypi.com/images/PiCam/IoTpHATPart.jpg)

> _Pimoroni Zero LiPo_

  * ![](https://hackmypi.com/images/PiCam/ZeroLiPoPart.jpg)

> _2x20 header pins_

  * ![](https://hackmypi.com/images/PiCam/2x20Part.jpg)

> _Raspberry Pi camera_

  * ![](https://hackmypi.com/images/PiCam/PiCamPart.jpg)

> _Pi Zero Camera Cable_

  *   
![](https://hackmypi.com/images/PiCam/PiCamCablePart.jpg)

> _SD card_

  *   

  * **1500maH battery**  

  * **Basic Soldering equipment (Solder Iron, solder, solder wick)**  


## Here's how to make it:

Start out by soldering the 2x20 pins onto the Pi Zero. These pins are necessary to attach any HAT's to the project. Start by soldering a pin on one corner, then one on the opposite side of the Pi. Doing it this way allows for the rest of the pins to be held securely in place as you solder them. I recommend always doing it this way when soldering anything, as it is easier to solder things that aren't moving.

![](https://hackmypi.com/images/PiCam/Pi_2x20.jpg)

After the pins are soldered onto the Pi Zero, the next step is attaching the Red Bear IoT pHAT (If you are using a Pi Zero W, this step can be skipped). Similar to earlier start by soldering one pin on one corner, then solder a pin on the far side. Having one on either side will keep everything still while you solder the rest of the pins into place.

![](https://hackmypi.com/images/PiCam/Pi_IoTpHAT.jpg)

At this point you have soldered the Pi to the wifi HAT properly. The next part that we need to solder on is the Pimoroni ZeroLiPo. This board gives us a small JST connector that will allow for this project to be powered by a battery. It gets soldered onto the end 8 pins on the pi. This board is small enough that it should remain stable after just one solder connection.

![](https://hackmypi.com/images/PiCam/ZeroLiPo_Attached.jpg)

Here, we have all the tricky hardware parts done. The Pi has the wifi capabilities it needs, as well as the battery power it needs. Next we need to attach the camera. The thick end of the camera cable gets put into the camera ribbon slot. Metal contact side up towards the board. The thinner side of the cable gets put into the Pi, again with the metal connectors facing towards the Pi's circuit board.

![](https://hackmypi.com/images/PiCam/FinishedUnmounted.jpg)

I chose to use some double sided tape to mount the camera onto the body of the Pi System. The camera fits nicely next to the Zero LiPo. Go ahead and mount the camera like this if you wish, otherwise find an alternate solution.

The hardware side of this guide is done. Next we just need to get the Pi setup to stream it's video wirelessly. Start by loading up an SD card with standard rasbian Pixel. If unsure how to do this, reference my guide on it, [here](https://www.hackmypi.com/SDimage.php). Once the OS is loaded, put the SD card into the Pi, let the Pi bootup, and settle on the desktop. Connect the Pi to the wifi (top right corner). First thing to do will be change the hostname/password. Run the command:   
`sudo raspi-config`   
in a terminal window. From this menu, change your hostname to whatever you wish, change the password on the pi, and enable the camera. Once those settings are done, reboot the Pi.

Once the Pi comes back up, open up a terminal and type:   
`ifconfig`   
Under wlan0 you will see your Pi's IP addess. Make sure to note it down somewhere. The next few commands will install a package called Motion, and configure it to stream whatever the camera sees wirelessly. Run the following command to update your Pi:   
`sudo apt-get update`   
Depending on you internet connection, this command may take some time to do everything. Once the update command is done, run the following command:   
`sudo apt-get install motion` After the install is over, we will configure Motion properly.

A few notes before we start, Motion will by default record motion detection. For some reason, this is crashing my Pi Zero, so for now we will disable motion detection. At a later date we will be setting up a Pi 3 to handle input from multiple of these IP cameras. At that point we will have the Pi 3 handle the motion detection. First thing we need to do to configure Motion is tell the daemon to always be on. Run the following command:   
`sudo nano /etc/default/motion`   
to open and edit a config file, change `start_motion_daemon=no` to `start_motion_daemon=yes`

The next command will bring up the configuration file for motion itself: `sudo /etc/motion/motion.conf`   
In here you are going to need to find the following lines, and modify them to match mine:   
daemon on   
width 640   
height 480   
framerate 100   
stream_localhost off   
set motion threshold to 300000   
set stream fps to 30   
These will set the stream resolution, the local framerate, allow for it to be viewed wirelessly, practically disable motion activation, and set the stream framerate.

After this, there is just one more section. Currently, the Pi will work properly, but the proper drivers are not loaded for the Pi Camera. Run the following command:   
`sudo /etc/init.d/motion`  
In this file, add the line `sudo modprobe bcm2835-v4l2` after the line that says 'chown'. Reboot the pi, and if you open up a web browser on another computer to "ipaddresofpi:8081" you should see the camera streaming whatever it sees!
