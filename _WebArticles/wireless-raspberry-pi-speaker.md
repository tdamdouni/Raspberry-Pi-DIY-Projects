# Wireless Raspberry Pi speaker

_Captured: 2017-05-19 at 15:44 from [www.google.de](https://www.google.de/amp/s/www.gadgetdaily.xyz/wireless-raspberry-pi-speaker/amp/)_

Every house needs a good speaker system, and a good speaker system is even better if it can be accessed by multiple devices over the wireless network. AirPlay uses Apple technology that was reverse-engineered in 2011, which means that third-party devices can now participate in the fun. AirPlay allows any Apple device to broadcast whatever is coming out of its speakers to an AirPlay receiver (which will be our Pi in this case). There is a way to send audio from PulseAudio to AirPlay receivers, as well as an application for Android called AirAudio. Sadly, the Android application requires root to access the audio of other applications running on the device. To keep things simple, we're going to use an iPad as the test client.

![Essential components](http://gadgetmag.wpengine.com/wp-content/uploads/2015/01/RaspberryPiSpeaker.png)

> _Essential components_

### Resources

Latest Raspbian image raspberrypi.org/downloads  
Wireless (or wired) network  
USB wireless dongle  
Speaker system  
USB sound card (optional)  
Small speaker amp (optional)

### Step-by-step

**Step 01** Set up Wi-Fi  
Connect everything to your Raspberry Pi and power it  
up. Log in to the Raspbian system with the username pi and the password raspberry. Then, make sure your wireless interface is working by typing iwconfig. You should see an entry there for wlan0. If you look in /etc/network/interfaces, there should already be a section that looks like this:
    
    
    ￼￼allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface default inet dhcp

If it doesn't, then add it at the end. This configuration makes the wireless adapter connect once the network in wpa_supplicant. conf is in range. This means the only thing left to do is to edit the wpa_supplicant.conf file, which needs your SSID (wireless network name) and the passphrase. You can do this with:
    
    
    $ sudo bash -c “wpa_passphrase my_network my_ passphrase >> /etc/wpa_supplicant/wpa_supplicant.conf”

…which will result in a wpa_supplicant.conf file that looks like this:
    
    
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
       ￼￼￼￼￼￼￼￼￼￼ssid=“my_network”
       #psk=“my_passphrase” 
       psk=17661426f1af334010ad2058d8b8f583ec501....
    }

The easiest way to get things going is to reboot the Pi with sudo reboot. Once your Pi is back up, check that you have an IP address on wlan0 with ip addr.

**Step 02** Install Shairport dependencies

These instructions are based on a write-up by Drew Lustro (http://drewlustro.com). We need to compile Shairport, but before we can do that we have to install its dependencies:
    
    
    $ sudo apt-get update; sudo apt-get install git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils libmodule-build-perl libasound2-dev libpulse-dev

Now we have to compile a Perl module called Net::SDP.
    
    
    $ cd perl-net-sdp/
    $ git clone https://github.com/njh/perl-net-sdp.git perl-net-sdp
    $ sudo bash -c “perl Build.PL; ./Build; ./Build test; ./Build install”
    $ cd ..

**Step 03** Compile and install Shairport

Now we get to compile and install Shairport, which might take a minute or so:
    
    
    $ git clone https://github.com/abrasive/shairport.git
    $ cd shairport/
    $ ./configure; make; sudo make install

After this, the Shairport binary will be installed but it won't be started at boot, which is unhelpful. To fix this, we need to install the init script:
    
    
    $ sudo cp scripts/debian/init.d/shairport /etc/init.d/shairport
    $ sudo chmod 755 /etc/init.d/shairport
    $ sudo update-rc.d shairport defaults

Finally, Shairport needs its own user that is a member of the audio group. You can create one with:
    
    
    $ sudo useradd -g audio shairport

**Step 04** Change the hostname

Shairport will show up as whatever the hostname of the system is. If you don't want the name to be raspberrypi, then you can change it like so:
    
    
    $ sudo bash -c “echo PiPlay > /etc/hostname”
    $ sudo hostname PiPlay
    $ sudo sed -i ‘s/raspberrypi/PiPlay/g’ /etc/hosts

**Step 05** Set the default sound card

If you have a USB sound card then you'll want to make that the default. You'll also want to make sure the volume is set to 100 per cent so that your amplifier is getting a nice signal. Use aplay -L to list the audio devices on your system. Our expert's sound card had an entry like this:
    
    
    front:CARD=U0x41e0x30d3,DEV=0
       USB Device 0x41e:0x30d3, USB Audio
       Front speakers

To set that card as default, you do:
    
    
    $sudo bash -c ‘echo pcm.!default front:U0x41e0x30d3 > /etc/asound.conf’

You can set the volume by going into alsamixer, pressing F6 to select the appropriate sound card and then using the up and down arrows to change the volume. Once you are done, you can make the changes the default with sudo alsactl store 1, where 1 is the card number. If you are using the built-in sound card then you should use 0 instead.

Finally, you can test the sound card is working with speaker- test -c 2, which sends a test signal to the left speaker and then the right speaker. You can exit the test with Ctrl+C.

**Step 06** A final reboot

After this reboot, Shairport should start automatically. To test it out, get your client and see if it can find the PiPlay. On an iOS device, slide up from the bottom, tap the AirPlay button and select PiPlay. It might take a couple of seconds to buffer, but once it's playing it should be fine.

**Step 07** Make it one unit

This is the freestyle part of the tutorial. Our expert decided to turn his setup into a single unit. You can see that in the image at the top of this page. Obviously, it could always be tidier, but that would involve cutting cables and we didn't have any spares.
