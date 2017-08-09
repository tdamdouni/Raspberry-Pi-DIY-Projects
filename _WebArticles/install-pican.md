# Install PiCan

_Captured: 2017-05-11 at 22:08 from [www.janssuuh.nl](http://www.janssuuh.nl/de/2016/03/10/pican/)_

The PICAN board is an additional piece of hardware that you connect to your Raspberry. The board fits all Raspberry versions.

![Untitled-9](http://www.janssuuh.nl/wp-content/uploads/2016/03/Untitled-9-300x174.jpg)

It is since the later versions of [Raspbian](https://downloads.raspberrypi.org/raspbian_latest) fairly easy to install hardware skpang.co.uk the PICAN.

You can use the [sudo raspi-config] command, which allows you to turn on the SPI functionality (and to boot automatically when you start your Pi).

![Untitled-9](http://www.janssuuh.nl/wp-content/uploads/2016/03/Untitled-9-1-300x203.jpg)

Selecteer:  
[8 Advanced Options]  
[A6 SPI]  
[Enable SPI]

Then update your current software:  
[sudo apt-get update]  
[sudo apt-get upgrade]  
[sudo reboot]

Subsequently some settings have to be added to your config.txt.  
[sudo nano /boot/config.txt]

Add the following 3 lines at the bottom of the file:  
[dtparam=spi=on]  
[dtoverlay = mcp2515-c, oscillator = 16 million pesetas, interrupt = 25]  
[dtoverlay=spi-bcm2835-overlay]

Your software is now installed, briefly reboot.  
After restart you can bring your interface "up" by the following command to give:  
[sudo /sbin/ip link set can0 up type can bitrate 100000]

(You need to adjust the bitrate to the bitrate of the canbus to measure activities to your desired hardware. In my case this is the Audi A4B6 Infotainmentbus, who has a bitrate of 100 KB per second.)

On [ifconfig] you can see if your can0 bus runs.  
On [ip -s -d link show can0] you can see whether bytes are sent or received.

![Knipsel](http://www.janssuuh.nl/wp-content/uploads/2016/03/Knipsel.png)

Ok, your canbus is now up and running. One last step is to install a number of small utilities / tools which are usefull to be able to make use of sending and receiving of can messages. To do this, enter the following commands:

[git clone _https://github.com/linux-can/can-utils.git]  
_[cd can-utils]  
[./autogen.sh]- gave me an error message, no effect  
[make]  
[make install]

If you prefer to download the files directly here:  
[ Can_Utils (82 downloads) ](http://www.janssuuh.nl/en/download/186/)
