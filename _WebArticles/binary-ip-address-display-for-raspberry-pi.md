# Binary IP Address Display for Raspberry Pi

_Captured: 2017-09-15 at 09:57 from [www.hackster.io](https://www.hackster.io/colinodell/binary-ip-address-display-for-raspberry-pi-163cc0)_

![Binary IP Address Display for Raspberry Pi](https://hackster.imgix.net/uploads/attachments/274462/2017-03-15_08_41_58_dk2rkYyy26.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

I recently built [a really cool project](https://www.hackster.io/colinodell/phpunicorn-visualizing-phpunit-tests-896208) using a Raspberry Pi Zero Wireless board and a Pimoroni Unicorn pHAT LED matrix. ([It displays the status of my running unit tests in real time - check it out here](https://www.hackster.io/colinodell/phpunicorn-visualizing-phpunit-tests-896208)). This project is designed to be "headless" \- it's not connected to any display.

This poses a problem - although I've configured the WiFi, I'm using DHCP and therefore don't know what IP the Pi will be using when it boots! Without this information, I can't SSH into the device or connect to my project remotely. I therefore needed a way to have the Pi inform me of its IP address on boot.

My solution: **display the IP address on the Unicorn pHAT LED matrix in binary!** Not only is this practical, but it also boosts my geek cred.

In this tutorial, I'll walk you through how to replicate this solution for your own projects.

This project uses a Raspberry Pi Zero Wireless, but it should work on virtually any Pi device with a 40-pin header.

Besides the Pi, you'll need the following:

  * Pimoroni Unicorn pHAT
  * A 2x20 header
  * Soldering iron

Plus the usual essentials for your Pi:

  * 2 amp MicroUSB power supply
  * Micro SD card with Raspian
  * (optional) USB WiFi dongle, if your Pi doesn't provide on-board WiFi

Assembly is very straight-forward - place the 2x20 header between the Pi and Unicorn pHAT and solder it together. A detailed guide to soldering your pHAT can be found here: <https://learn.pimoroni.com/tutorial/sandyj/soldering-phats>

This script was designed to run on Python 3. Therefore, make sure you install Python 3 on your Pi:
    
    
    sudo apt-get update
    sudo apt-get install python3 python3-dev python3-pip
    

(It probably works on Python 2, but I have not tested this).

We'll also need to install the [unicornhat ](https://github.com/pimoroni/unicorn-hat)library for Python:
    
    
    curl -sS https://get.pimoroni.com/unicornhat | bash
    

Here's the full code listing for our Python script:
    
    
    import socket 
    import time 
    import unicornhat as unicorn 
     
    # From http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/ 
    def getNetworkIp(): 
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
       s.connect(('google.com', 0)) 
       return s.getsockname()[0] 
     
    # Prepare the Unicorn pHAT display
    unicorn.set_layout(unicorn.PHAT) 
    unicorn.rotation(0) 
    unicorn.brightness(0.5) 
     
    # Obtain our IP address and split it into the 4 components ("octets")
    ip = getNetworkIp() 
    octets = ip.split('.') 
     
    # Render the binary representation for each octet
    y = 0 
    for octet in octets: 
     bits = '{0:08b}'.format(int(octet)) 
     x = 0 
     for b in bits: 
       if int(b): 
         unicorn.set_pixel(x, y, 0, 0, 128) 
       x += 1 
     y += 1 
     
    # Render the display
    unicorn.show() 
     
    # Keep the LEDs lit for 30 seconds
    time.sleep(30) 
    

It's very straight-forward: we determine the IP address, split it into four parts (or "octets"), and then render each one in binary

Upload the script to your Pi - perhaps to your home folder (`/home/pi`). Lastly, add this line to your /etc/rc.local file so the script runs on boot:
    
    
    sudo python3 /home/pi/ip.py & 
    

(The ampersand on the end will prevent our script from holding up the rest of the boot process).

Now that everything is in place, let's go ahead and boot up the Pi! If you've previously configured your wireless network, the Pi should join it on bootup and then light up the LEDs like this:

![](https://hackster.imgix.net/uploads/attachments/274463/2017-03-15_08_41_58_yfGIaEymdX.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

> _The display in action on bootup_

This shows a binary representation of your Pi's IP address.

The IP address is displayed in binary - one LED per bit. Each row represents one of the four parts ("octets") of the address. We can decode the values using a table like this:

![](https://hackster.imgix.net/uploads/attachments/274466/selection_238_gG21WqZp24.png?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Decoding the binary_

The table on the left matches the layout of the Unicorn matrix. We simply place an X for each glowing LED and add up the values of each column. For example, in the first row, columns 128 and 64 are lit, so we add 128+64 to get the first octet of the address: 192.

By repeating this process, we can determine that our IP address is 192.168.80.93!
    
    
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
       s.connect(('google.com', 0)) 
       return s.getsockname()[0] 
    
    unicorn.set_layout(unicorn.PHAT) 
    unicorn.rotation(0) 
    unicorn.brightness(0.5) 
    
    octets = ip.split('.') 
    
    for octet in octets: 
     bits = '{0:08b}'.format(int(octet)) 
     for b in bits: 
       if int(b): 
         unicorn.set_pixel(x, y, 0, 0, 128) 
    
    
    time.sleep(30) 
    
