Displays the Raspberry Pi's time on a Sense Hat

Each digit is 3x4 pixels so the time is shown as:

H H

M M 

on the Sense Hat

I've set it up in crontab to run every minute.

```sudo crontab -e```

Add the following to run it every minute:

```* * * * * /home/pi/clock/clock.py >/dev/null 2>&1```

This assumes the python program is in directory ```/home/pi/clock/```

