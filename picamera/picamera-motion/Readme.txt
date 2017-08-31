                  Lightweight python Motion Detection
                         picamera Lite version
                  -----------------------------------
Summary
-------
based on original code written by brainflakes and modified by pageauc
user utpalc rewrote motion detection using picamera stream and pageauc
modified this sample code to this example application
This code uses the picamera python libraries rather than raspistill.
Posted on Raspberry Pi forum under Lightweight Python Motion Detection
Sample video posted at http://youtu.be/ZuHAfwZlzqY
Code modified to exit image scanning loop as soon as the sensitivity value
is exceeded. This speeds taking larger photo if motion detected early in scan
This code is available on github at https://github.com/pageauc/picamera-motion
Note:
This version uses picamera python libraries but does not integrate
give synchronization.  This is basically sample code to assist development

Install Instructions
--------------------
1. Log in to RPI using putty ssh or raspberry pi console terminal session
2. To install perform the following commands

cd ~
mkdir pimotion
cd pimotion
mkdir images
sudo apt-get install python-imaging
sudo apt-get install python-picamera
wget https://raw.github.com/pageauc/picamera-motion/master/picamera-motion.py
wget https://raw.github.com/pageauc/picamera-motion/master/Readme.txt
python ./picamera-motion.py

Note: you may have to install other libraries and make sure your
raspberry pi is running a current updated version of raspbian.

Tuning
------
To change motion detection settings edit the pimotion.py file using nano
it is recommended you make a backup copy just in case.
from a logged in putty ssh or console terminal session edit using nano.  You
can also use IDLE if desired.
   
That's it
Please note this code is pretty basic but a good learning tool if
you need to implement a simple python only motion detection application
using the picamera python libraries.

Claude Pageau