# Installing PiCAN for Raspberry 2 Model B

_Captured: 2017-05-11 at 22:47 from [skpang.co.uk](http://skpang.co.uk/blog/archives/1165)_

This blog shows the steps required to install the software on the Raspberry 2 Model for use with [PiCAN board](http://skpang.co.uk/catalog/pican-canbus-board-for-raspberry-pi-p-1196.html)

All the previous kernel modules will not work with the current Raspbian (2015-02-16) for the Raspberry Pi 2. However the next version of the kernel will have the mcp251x driver compiled in. We can upgrade the firmware now with the new driver. These instruction will also work on the Raspberry B+.

Start by installing a brand new version of Raspbian (2015-02-16) kernel 3.18

Enable the SPI interface by running raspi-config.
    
    
    cd /usr/bin 
    
    
    sudo ./raspi-config

Select Advanced Options.

![](http://www.skpang.co.uk/blog/wp-content/uploads/2015/03/3.png)

> _Select A6 SPI_

![](http://www.skpang.co.uk/blog/wp-content/uploads/2015/03/4.png)

> _Confirm you want the SPI interface enabled. Confirm you want the SPI kernel module to be loaded by default, then exit._

Do an update first.
    
    
    sudo apt-get update 
    
    
    sudo apt-get upgrade 
    
    
    sudo reboot

Add the overlays by:
    
    
    sudo nano /boot/config.txt

Add these 3 lines to the end of file:
    
    
    dtparam=spi=on 
    
    
    dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25 
    
    
    dtoverlay=spi-bcm2835-overlay
    
    
    ![](http://www.skpang.co.uk/blog/wp-content/uploads/2015/03/2.png)

Reboot Pi:
    
    
    sudo reboot

You can now bring the CAN interface up:
    
    
    sudo /sbin/ip link set can0 up type can bitrate 500000

Download and copy the [CAN test](http://www.skpang.co.uk/dl/can-test_pi2.zip) programs to the Pi.

To send a CAN message use :
    
    
     ./cansend can0 7DF#0201050000000000

This will send a CAN ID of 7DF. Data 02 01 05 - coolant temperature request.

Installing [can-tools.  
](http://elinux.org/Can-utils)

To write your own CAN-Bus program follow [this blog](http://skpang.co.uk/blog/archives/1199).
