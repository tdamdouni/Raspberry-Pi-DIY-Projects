# How To Autorun A Python Script On Raspberry Pi Boot

_Captured: 2017-05-06 at 15:57 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2015/02/how-to-autorun-a-python-script-on-raspberry-pi-boot/)_

![systemd Screenshot](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2015/10/systemd_screenshot-702x336.png)

There are lots of techniques for running a script when the Pi boots and which one you choose will depend on exactly what the script does and what you expect. In this post I'll explain a technique where the Pi automatically logins as the Pi user and immediately executes a Python script.

This has one major advantage over another popular method (see [Running A Python Script At Boot Using Cron](http://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/)) in that because the terminal is up and running text output from the script is visible before you are returned to a usable command line prompt.

## Auto Login Setup (optional)

The first step is to enable the Pi to login automatically without requiring any user intervention. This step is optional.

At the command prompt or in a terminal window type :
    
    
    sudo raspi-config

followed by Enter.

Select "Boot Options" then "Desktop/CLI" then "Console Autologin"

## Prepare Script

My test script is called "[myscript.py](https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/myscript.py)" and is located in /home/pi/. This is what it contains :

1234567
`#!/usr/bin/python``print``(``"******************************************************"``)``print``(``"* This is a test script. There are many like it,     *"``)``print``(``"* but this one is mine. My script is my best friend. *"``)``print``(``"* It is my life. I must master it as I must master   *"``)``print``(``"* my life.                                           *"``)``print``(``"******************************************************"``)`

You can download this directly to your Pi by using the following command :
    
    
    wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/myscript.py

I strongly suggest getting this working before trying any other scripts!

## Auto-run Script Setup

Now we need to tell the operating system to run the script for the Pi user. In the command prompt or in a terminal window type :
    
    
    sudo nano /etc/profile

Scroll to the bottom and add the following line :
    
    
    sudo python /home/pi/myscript.py

where "/home/pi/myscript.py" is the path to your script.

Type "Ctrl+X" to exit, then "Y" to save followed by "Enter" twice.

## Reboot and Test

To test if this has worked reboot your Pi using :
    
    
    sudo reboot

When it starts up your script will run and you will see something like this :

Due to the technique we've used the script is run whenever the Pi user logs in. This means if you create other terminal sessions (via SSH for example) the script will run each time.

## Troubleshooting

If it doesn't work here are some things to try :

  * Run your script manually and check it works correctly
  * Use my example script and check that works
  * Double check the initial steps
