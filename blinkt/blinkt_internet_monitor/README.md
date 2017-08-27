# blinkt_internet_monitor
A script for your Pimoroni blinkt that plays happy lights when your internet works and angry lights when it doesn't.

Code adapted from https://github.com/pimoroni/blinkt

Install into "/home/pi/Pimoroni/blinkt/examples" after installing blinkt from
the link above.

Launch on boot by adding the following to "crontab -e":    
@reboot python /home/pi/Pimoroni/blinkt/examples/inet_monitor.py &

Kill via shutdown script with:    
pgrep -f /home/pi/Pimoroni/blinkt/examples/inet_monitor.py | xargs kill -SIGINT

Tested on Rpi3 with Pimoroni blinkt with Raspbian GNU/Linux 8 (jessie).

Video of the script in action below.  

Shown in the video is the boot and shutdown sequence, note that the monitor goes red because it starts before the interface is up and connected to the wireless router.  When it connects, the lights change.  

This script catches SIGINT to shutdown cleanly so the LEDs do not stay lit when the OS is in shutdown.

[https://www.youtube.com/watch?v=_w-22ylveE4](https://www.youtube.com/watch?v=_w-22ylveE4)
