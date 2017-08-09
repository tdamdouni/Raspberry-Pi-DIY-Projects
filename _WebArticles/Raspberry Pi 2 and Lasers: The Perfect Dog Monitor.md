# Raspberry Pi 2 and Lasers: The Perfect Dog Monitor

_Captured: 2016-01-19 at 13:36 from [www.element14.com](http://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/2015/06/02/a-raspberry-pi-laser-tripwire-dog-watcher?CMP=SOM-TWITTER-PRG-BLOG-DYOUNG-RASPIDOGMONITOR)_

![wallace and gromit](http://www.element14.com/community/servlet/JiveServlet/downloadImage/38-20252-223833/297-232/gromit.png)

> _[wallace and gromit](http://www.element14.com/community/servlet/JiveServlet/showImage/38-20252-223833/gromit.png)_

My dog Penny is one of the best. She has the two critical commands of 'come' and 'stay' down pat so well that I can go for a run with her off-leash here in Denver.

![Penny.jpg](http://www.element14.com/community/servlet/JiveServlet/downloadImage/38-20252-223815/126-223/Penny.jpg)

She's gentle with our newborn baby, and she doesn't destroy things. Her only issue is that she goes BONKERS for food. My wife and I have done a great job training it out of her when we're around so we no longer have to worry about a cheese board sitting on the low coffee table, but I know she gets on the counters any time we are away. Sounds like a job for a machine!

![0528151441d.jpg](http://www.element14.com/community/servlet/JiveServlet/downloadImage/38-20252-223816/401-226/0528151441d.jpg)

I decided that it might be helpful to have a surrogate to defend the counters when she's home alone. After the success of the [Silent Laser Doorbell](http://www.element14.com/community/groups/arduino/blog/2014/06/06/arduino-xbee-project-silent-laser-tripwire-doorbell), I decided that a Laser Dog Watcher could be similarly effective. Here are the features:

  * Setup a Laser tripwire using the same mechanical system in the Silent Laser Doorbell<link>
  * There is a calibration knob to allow for various levels of ambient light.
  * There is an 'enable' switch to disable the audio and photo features to allow the user to line up and calibrate for ambient light.
  * If the first audio file doesn't get her off the counter and reestablish the beam, it plays up to two more audio files before disabling itself. That way it won't loop over and over in case the system was knocked out of alignment.

Here's the system in action! I put a bit of food on the counter and left for a while with a video camera setup.

I've put a step-by-step tutorial below and attached full documentation to this article for those that would like to build one, but first a few design decisions that had to be made.

Raspberry Pi2 Choice:

I've been keen to use my Pi2, and this seemed like a great chance. Although it doesn't really use the muscle behind the new version I like knowing that expansion of this project would be no problem. Who knows - maybe I'll do image processing to recognize her and generate a trigger! Here is a spec comparison for the Rev 1 vs. Rev 2 Raspberry Pi:

![Pi Pi2_compare_jan30.png](http://www.element14.com/community/servlet/JiveServlet/downloadImage/38-20252-223821/464-252/Pi+Pi2_compare_jan30.png)

Calibration:

In the Silent Doorbell project, I implemented a clever moving average system to automatically calibrate for ambient light. This was certainly needed in sunny Denver, CO. However the Raspberry Pi doesn't have any analog inputs that would be required for such an algorithm. Since this design is intended to be used indoors with mostly stable ambient light and the sensor is mostly enclosed, a calibration knob makes on leg of the resistor divider variable and gave plenty of stability (i.e. lights on, lights off, etc…). The way to calibrate is to have the beam broken and make sure the status LED shows that the beam is broken by turning on. Turn on all the lights in the room to be sure it will work in all conditions. Then aim the beam to the sensor and be sure the status LED turns off. Check out the schematic:

<insert schematic image>

Enable Switch:

During laser aiming and calibration, I was annoyed by constantly hearing myself yell at the dog, and poor penny was so worried and confused! It took me about 5 seconds to decide that an enable switch is needed.

Status LED:

When the enable switch turns off audio output, one needs an LED to show that the laser is broken during aiming and calibration! It was a huge help.

Camera:

Catching animals in the act is hilarious! Also, I want to be sure the system is working properly and count the number of times that it was tripped.

There you have it! If you want to build one for yourself, follow the tutorial below and let us know in the comments how it goes!

**Tutorial:**

1\. Download the NOOBS files and follow the [tutorial created by Raspberry Pi](https://www.raspberrypi.org/help/noobs-setup/). It's a big file so grab a coffee/tea/beer and build the circuit hardware described on the [Silent Laser Doorbell](http://www.element14.com/community/groups/internet-of-things/blog/2015/01/07/connecting-a-laser-doorbell-to-the-cloud) page.

2\. Plug the Pi into a monitor, keyboard, and mouse and power up the pi

3\. Select 'Raspian' for your operating system and set your desired language and keyboard. The install takes a while so now's a great time to re-up your beverage of choice.

4\. After the install completes, the Pi restarts itself in the Configuration Tool. Go into 'Advanced Options > SSH' to enable SSH. Go into 'Enable Camers" > 'Enter' > 'Finish'

5\. Reboot the system and if you'd like to SSH into the Pi you can remove the monitor, keyboard, and mouse.

6\. Update and upgrade the packages. This takes a bit. Probably time for another beverage.

> sudo apt-get update
> 
> sudo apt-get upgrade

7\. Install the RPIO package to allow reading the GPIO lines, Alsa audio drivers, the mpg123 MP3 player, and the PiCamera library

> sudo easy_install -U RPIO
> 
> sudo apt-get install alsa-utils mpg123
> 
> sudo apt-get install python-picamera

8\. Reboot the Pi

9\. Load the sound drivers and set the system to use the 3.5mm audio jack output

> sudo modprobe snd_bcm2835
> 
> sudo amixer cset numid=3 1

10\. Create a folder to hold your MP3 files and python script, and another one (in the dogwatcher folder) for the image files

> mkdir dogwatcher #in the pi directory
> 
> mkdir photos #in the dogwatcher directory

11\. Transfer your MP3's to your Raspberry Pi into your 'dogwatcher' folder. There are many ways to do this. My two favorite methods are (1) login to your Pi with an SFTP (SSH File Transfer Protocol) client like FileZilla and copy them to the desired directory or (2) Use a thumb drive to transfer the files. My files are 'hey.mp3' 'uhoh.mp3' and 'baddog.mp3'

12\. Test to be sure that you can play the file desired to your 3.5mm audio jack by running the following command in your folder:

13\. Install the Rpi.GPIO module on the Pi
    
    
    sudo apt-get install python-dev python-rpi.gpio

14\. Upload the python script to the dogwatcher folder. Feel free to use mine; attached here as 'watcher.py'

15\. Build the laser detection hardware and enable switch circuit described in the schematic

16\. Turn on the Pi, navigate to the dogwatcher folder, and run the python script.

> cd dogwatcher
> 
> sudo python watcher.py

17\. Calibrate the sensor, then enable the switch to make sure everything runs as planned. You can pull photos off in the same way you added the MP3's, but I'm a big fan of doing it over SSH FTP with Filezilla.

18\. Setup the Pi to activate the system on boot using your favorite method (instructable listed below for the method I used, or you can use the included 'launcher.sh' file of mine attached here).

19\. Test it! It should run on bootup.

**Attached Design Files:**

watcher.py: Python script that runs the system

hey.mp3: One of the audio files that I used (in case you need a known-good audio file to test your system)

**Helpful Links:**

to start a python script at boot: <http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/?ALLSTEPS>
