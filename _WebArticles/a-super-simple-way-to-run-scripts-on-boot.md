# A super-simple way to run scripts on boot

_Captured: 2017-08-26 at 11:57 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/running-scripts-at-boot)_

Here's a super-simple way to run scripts automatically on boot on your Raspberry Pi, using cron, that you can have up and running in literally a few seconds.

## Cron

The secret sauce here is cron. Cron is a Unix program for scheduling jobs, and is _incredibly_ versatile in terms of what it can do. Need to run a script every 15 minutes? Need to run a script a 6:05pm every day? Need to run a script at 20 minutes past every hour? Cron can handle it.

However, we won't be using those time-based features of cron here. We'll use its `@reboot` feature to run a python script whenever your Pi boots.

## Blinkt! rainbows!

Let's say that you want to build a little rainbow light with a Blinkt! and a Pi Zero, and have it run our rainbow animation example whenever it's plugged in and turned on, without having to plug in a keyboard, mouse and display to open the terminal and run the script.

This assumes that you've already installed our Blinkt! library. You can follow our [Getting Started with Blinkt!](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt) tutorial to get you up to speed.

## Editing your crontab

Open a terminal, and type `crontab -e`. If it's the first time that you've edited your crontab, then it will ask you to choose which editor you'd like to use. I prefer to use nano, and this is the default, so you can just press enter to select it.

At the top of the crontab, you'll see a lot of blurb about how to use it, on lines that are commented out (they begin with #). Scroll all the way down past these lines to the bottom (using the down arrow key) and type, on the last line, the following:
    
    
    @reboot python /home/pi/Pimoroni/blinkt/examples/rainbow.py &
    

We're using the full path to the script, all the way from the root. Last, we add `&` to the end to run the script in the background, so that the Pi will boot as normal.

Once you've added that line, press `control-x`, `y` and `enter` to exit nano.

It should say `crontab: installing new crontab` assuming you saved the crontab successfully.

Type `sudo reboot` to reboot your Pi, and the rainbow example should run after a few seconds.

To remove the `@reboot` command, just type `crontab -e` again, delete the offending line, and then exit and save as before.
