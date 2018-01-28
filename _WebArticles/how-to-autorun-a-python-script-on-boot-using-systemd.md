# How To Autorun A Python Script On Boot Using systemd

_Captured: 2017-11-19 at 15:44 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)_

![systemd Screenshot](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2015/10/systemd_screenshot-702x336.png)

With the latest release of Raspbian I started to struggle to autorun Python scripts on bootup using Cron or rc.local. It appears that the Raspbian boot sequence has changed and these processes run at different points in that sequence. How much of an issue this is depends on what your Python script is trying to do and what resources it needs.

The point at which your Python script is run in the startup sequence is vital if your script relies on any system features being available at that point in time. For me this often includes :

  * Network is connected and available
  * The /home/pi directory is mounted and read for use
  * System time has been updated by NTP

I decided to use "systemd" as this seems to the recommended way of launching custom features and lots of Linux distributions are adopting it. systemd is a software suite for central management and configuration of a Linux system and aims to replace other popular tools that previously fulfilled this role. As a result it seems to have plenty of enemies but you can read all about the controversy on [the systemd Wikipedia page](https://en.wikipedia.org/wiki/Systemd).

systemd is quite scary. Or easy. Depending on your level of experience. My goal was just to get it to launch one of my scripts with the minimum of fuss and without having to do too much typing I didn't understand.

## Step 1 - Your Python Script

My example script was stored in the /home/pi directory and named "myscript.py". Obviously your script can be called something else but keep an eye on where it is referenced in the commands and text below.

## Step 2 - Create A Unit File

Next we will create a configuration file (aka a unit file) that tells systemd what we want it to do and when :
    
    
    sudo nano /lib/systemd/system/myscript.service

Add in the following text :
    
    
    [Unit]
    Description=My Script Service
    After=multi-user.target
    
    [Service]
    Type=idle
    ExecStart=/usr/bin/python /home/pi/myscript.py
    
    [Install]
    WantedBy=multi-user.target

You can save and exit the nano editor using [CTRL-X], [Y] then [ENTER].

This defines a new service called "My Script Service" and we are requesting that it is launched once the multi-user environment is available. The "ExecStart" parameter is used to specify the command we want to run. The "Type" is set to "idle" ensures the ExecStart command is only run when everything else has loaded. For my GPIO based scripts the default type of "simple" didn't work.

Note that the paths are absolute and fully define the location of Python as well as the location of our Python script.

In order to store the script's text output in a log file you can change the ExecStart line to :
    
    
    ExecStart=/usr/bin/python /home/pi/myscript.py > /home/pi/myscript.log 2>&1

The permission on the unit file needs to be set to 644 :
    
    
    sudo chmod 644 /lib/systemd/system/myscript.service

## Step 3 - Configure systemd

Now the unit file has been defined we can tell systemd to start it during the boot sequence :
    
    
    sudo systemctl daemon-reload
     sudo systemctl enable myscript.service

Reboot the Pi and your custom service should run :
    
    
    sudo reboot

## Step 4 - Check status of your service

You can check the status of your service using :
    
    
    sudo systemctl status myscript.service

## Other useful resources for systemd
