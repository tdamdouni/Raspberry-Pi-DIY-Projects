# Raspberry Pi: Launch Python Script on Startup

_Captured: 2017-08-26 at 10:21 from [www.instructables.com](http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/)_

![Raspberry Pi: Launch Python Script on Startup](https://cdn.instructables.com/FGW/QX50/HUKFQ0UQ/FGWQX50HUKFQ0UQ.MEDIUM.jpg)

As I've been working on my own Pi projects, I've been discovering many little tricks and tips by scouring various websites and assembling information, testing and optimizing.

So, here is another one of my "meat-and-potatoes" Raspberry Pi Instructables.

This Instructable will show you how to setup your Raspberry Pi to automatically launch a Python script upon startup.

First of all, I know this is a lame picture. If you can come up with a better one, I'm open to suggestions.

The Arduino has auto-launch built into it; the Pi does not. This will make your Pi a more powerful electronics platform and is essential if, for example, you want to use your Pi as a video kiosk using GPIO controls.

Before doing this Instructable, please make sure you have your Raspberry Pi up and running, which you can do with [The Ultimate Raspberry Pi Configuration Guide](https://www.instructables.com/id/Ultimate-Raspberry-Pi-Configuration-Guide/) Instructable.

I'm using the Mac OS for this guide, but you can extend the principles to other operating systems.

## Step 1: Make a Launcher Sript

![Make a Launcher Sript](https://cdn.instructables.com/FMM/360P/HUKFQ0W0/FMM360PHUKFQ0W0.MEDIUM.jpg)

I'm building out a new project called **Black Box Timelapse **(Instructable coming soon...).

My python script is called : **bbt.py** and lives in a directory called **bbt** that is in the root directory. You can substitute your own director/Python script name instead of using mine.

We will use the Linux crontab to run the Python script.

I've had trouble with crontab and directory management and my solution is to amke a shell script, which always navigates to the proper directory and will launch my _bbt.py _Python script.

Let's create the shell script!

I'm using ssh to access to Raspberry Pi. My IP address for the SD card for this is 10.0.1.68. Your IP address may be different -- just change the address accordingly.

Open the Terminal window and on the command line, type:
    
    
    ssh pi@10.0.1.68

If you are running directly hooked into the monitor, you can skip this step.

Type in:
    
    
    cd bbt

then:
    
    
    nano launcher.sh

Will launch your editor, type in this script

#!/bin/sh  
# launcher.sh  
# navigate to home directory, then to this directory, then execute python script, then back home

cd /  
cd home/pi/bbt  
sudo python bbt.py  
cd /

**Cntl-X, Return** to save.

What this script will do is to navigate to the root directory, then to the bbt directory, launch the Python script and then return to the root directory.

## Step 2: Make It Executable

![Make It Executable](https://cdn.instructables.com/F9R/8BX1/HUKFQ0WE/F9R8BX1HUKFQ0WE.MEDIUM.jpg)

We need to make the launcher script an executable, which we do with this command
    
    
    chmod 755 launcher.sh

Now test it, by typing in:
    
    
    sh launcher.sh

This should run your Python code.

## Step 3: Add Logs Directory

![Add Logs Directory](https://cdn.instructables.com/FXB/5TML/HUK2ETVF/FXB5TMLHUK2ETVF.MEDIUM.jpg)

We will get to using crontab in a minute, but first we need to make a directory for the any errors in crontab to go.

Navigate back to your home directory:
    
    
    cd

Create a logs directory:
    
    
    mkdir logs

## Step 4: Add to Your Crontab

![Add to Your Crontab](https://cdn.instructables.com/FUI/MEE9/HUK2EU0E/FUIMEE9HUK2EU0E.MEDIUM.jpg)

crontab is a background (daemon) process that lets you execute scripts at specific times. It's essential to Python and Raspberry Pi. The details are confusing, as is often the case with Linux. Once I got the hang of the format, I've found it to be incredibly easy to use.

[Here's the Linux reference](http://linux.about.com/od/commands/l/blcmdl5_crontab.htm) and [here are some more crontab](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/) examples.

Type in:
    
    
    sudo crontab -e

This will brings up a crontab window.

Now, enter the line:
    
    
    @reboot sh /home/pi/bbt/launcher.sh >/home/pi/logs/cronlog 2>&1

What this does is rather than executing the launcher script at a specific time, it will execute it once upon startup.

## Step 5: Reboot and See If It Works

Unplug the power or just type in:
    
    
    sudo reboot

Wait for startup and see if your script automatically launches.

If it doesn't work, check out the log file:
    
    
    cd logs
    
    
    cat cronlog

This will show you any errors that you might have.

## Step 6: Always Make an Exit Plan!

You'll want to have an easy way to exit the code, so that you don't get stuck in an endless buggy loop.

The way I do this is to plug in the keyboard (not plugged in for standard kiosk usage) and exit the script this way.

In a standard Python script, you can always hit cntl-C, which will exit.

If using the pygame libraries, you can do an exit on keydown, such as:
    
    
    while not done:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                done = True

## Step 7: Extra: Crontab for Timed Scripts

Another way you can use crontab is to execute scripts at specific times, such as every minute, every hour, at a specific time. This is especially helpful for projects such as Twitterbots, which I'm using for my [Bot Collective](http://www.botcollective.com) project

In this case, you want to make sure your Python script exits and isn't stuck in a loop, otherwise you may end up launching the script multiple times.

Here are some examples, with the same bbt.py/launcher code:

# every 2 minutes  
*/2 * * * * /home/pi/justdiedbot/launcher.sh >/home/pi/logs/cronlog.log 2>&1

# at 6:22 EST, 3:22 PST (we are on PST); 15:22  
22 15 * * * /home/pi/marktwainbot/launcher.sh >/home/pi/logs/cronlog.log 2>&1
