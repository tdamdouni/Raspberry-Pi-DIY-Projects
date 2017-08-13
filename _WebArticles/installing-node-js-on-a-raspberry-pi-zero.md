# Installing node.js on a Raspberry Pi Zero

_Captured: 2017-08-13 at 09:27 from [blog.miniarray.com](https://blog.miniarray.com/installing-node-js-on-a-raspberry-pi-zero-21a1522db2bb)_

I recently switched one of my projects from a [Raspberry Pi 3](https://www.amazon.com/Raspberry-Pi-RASP-PI-3-Model-Motherboard/dp/B01CD5VC92?&_encoding=UTF8&tag=miniarray-20&linkCode=ur2&linkId=1afb51024aeabc438e832209aac70d23&camp=1789&creative=9325) over to a [Raspberry Pi Zero](https://www.amazon.com/Raspberry-Pi-RASP-PI-3-Model-Motherboard/dp/B01CD5VC92?&_encoding=UTF8&tag=miniarray-20&linkCode=ur2&linkId=1afb51024aeabc438e832209aac70d23&camp=1789&creative=9325). Since they both run _very_ similar hardware, I was able to just pop out the sdcard from the Rpi 3 and just insert it into the zero and _Voila_ everything just worked.. or so I thought.

The main app(s) I was using to serve up a couple of pages was no longer working. `npm`and `nodejs`. But, after doing a bit o' research, I found that `node` requires special compilation instructions for the different ARM chips:

> _"Unfortunately this is because RaspPi is ARMv6 while the 'armhf' Debian distro is for ARMv7 and above. We need to have an arch check in the setup script to make sure this is stated at install time." -- __[rvagg, Dec 6, 2014_](https://github.com/nodesource/distributions/issues/44#issuecomment-65916201)

Luckily, there is a solution:

First, we will need to download an earlier version of node (v4.2.4) built specifically for armv6l

Now, extract it to the `/usr/local` directory
    
    
    $ cd /usr/local  
    $ sudo tar xzvf ~/node-v4.2.4-linux-armv6l.tar.gz --strip=1

Finally, (if you haven't already) remove the nodejs debian package
    
    
    $ sudo apt-get remove --purge npm node nodejs

Now we can verify that everything is good to go:
    
    
    $ node -v  
    v4.2.4

### Optional (but highly recommended)

This install method comes with npm version 2.x which is known for slow installs due to the method in which it handles dependencies. We can upgrade it easily with the following command:
    
    
    $ sudo npm install -g npm

So meta.
