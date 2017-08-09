# Internet Radio on your Pirate Radio

_Captured: 2017-05-18 at 23:01 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/internet-radio-on-your-pirate-radio)_

In this guide, we'll be turning your Pirate Radio into a proper internet radio. We've even configured the buttons on the pHAT BEAT to skip between stations, control the volume, and trigger a safe shutdown. The VU meter will display the volume level of your music too!

![](https://learn.pimoroni.com/static/repos/learn/sandyj/internet-radio-on-your-pirate-radio-large.jpg)

> _We've wrapped the whole process up into a nifty one-line-installer that will install and configure everything for you, but we'll explain what it all does too in case you want to hack it yourself._

Because this software relies on the buttons on [pHAT BEAT](https://shop.pimoroni.com/products/phat-beat), it won't work (without some hacking) on pHAT DAC or Speaker pHAT, but it's perfect for the [Pirate Radio Kit](https://shop.pimoroni.com/products/pirate-radio-pi-zero-w-project-kit), or your own setup with pHAT BEAT.

We recommend using the very latest version of Raspbian **Lite**, and you'll need an internet connection to install VLC and such later (we'll explain how to do that in Raspbian Lite below). We'd recommend using either the NOOBS installer, which you can find [here](https://www.raspberrypi.org/downloads/noobs/) (ensure that you select Raspbian Jessie **Lite** when installing), or downloading Jessie Lite from [here](https://www.raspberrypi.org/downloads/raspbian/) and then using the [Etcher](https://etcher.io/) tool to burn the image to your SD card.

Currently, our internet radio installer is best supported by Jessie Lite, and may not work properly in the full version of Raspbian. Because Jessie Lite is... liter (_sic_) it should also run a bit more snappily than the full Raspbian.

## Building the Pirate Radio Kit

If you're using the Pirate Radio Kit and haven't already built it, then follow our guide [here](https://learn.pimoroni.com/tutorial/sandyj/assembling-pirate-radio) to learn how to put it all together.

If you're just using pHAT BEAT, then make sure that you've soldered the 2x20 pin female header to it. Again, you can follow our [guide](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats) to soldering pHATs. Connect a couple of speakers (or just one) to your pHAT BEAT's push fit speaker terminals.

Pop the pHAT BEAT onto your Pi's GPIO pins, if you haven't already.

## Running the installer

Just to reiterate, you'll need an internet connection to run this installer. Pop the SD card into your Pi, make sure that the pHAT BEAT board is attached to your Pi (on its GPIO pins), and then plug in the power and boot up your Pi. Because you're using Jessie Lite, your Pi will boot straight to a terminal, but don't be scared!

You'll need to connect to Wi-Fi. To do this, you need to edit a file called `wpa_supplicant.conf`. Type the following:
    
    
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    

Use the arrow keys to move to the bottom of the file, and add the following, replacing the parts that say "YOURSSID" and "YOURPASSWORD" with the SSID and password for the Wi-Fi network to which you'd like to connect (make sure to keep the quotes; they're important).
    
    
    network={
    ssid="YOURSSID"
    psk="YOURPASSWORD"
    }
    

Once you've made those changes, press `control` and `x`, then `y`, and then `enter` to save and close the file.

Now, type `sudo reboot` and press `enter` to reboot. Your Pi should now be connected to Wi-Fi.

To run the installer, type the following:
    
    
    curl https://get.pimoroni.com/vlcradio | bash
    

The installer will prompt you several times, and you should type `y` for all of these, and the installer should also ask if you'd like to reboot once the installation is complete. If it doesn't, then restart by typing `sudo reboot` again.

## What the installer does

The installer does a few things.

The first is that it installs and configures the pHAT BEAT software, including the Python library, configuring the ALSA audio settings to route the audio out through the I2S DAC/amp on pHAT BEAT, and installing the ALSA plugin that drives the VU meter LEDs to display volume levels.

Second, it installs VLC, a versatile, cross-platform media playback and streaming program that also works via the command line. Our internet radio software uses VLC to stream and play back internet radio stations. It's pre-configured with 4 stations, including Slay Radio and Planet Rock, but you can add more, and we'll see how to do that later.

Last, it installs a couple of daemons to run the VLC process itself, and a script that enables the button controls. Daemons are programs that stay running in the background and will kick in when your system boots and restart if they crash for any reason.

## Using your internet radio

Assuming the installation went successfully, your Pi should have rebooted and will now be streaming internet radio! What's that? You can't hear anything? To start playback, you'll need to press the play button on the pHAT BEAT. The buttons are labelled on the pHAT BEAT board itself and on the front of the Pirate Radio.

The functions of the buttons should all be fairly self-explanatory. The volume up and down buttons... turn the volume up and down. The forward and back buttons cycle through the stations, and the play/pause button will stop and start playback, although it won't pause it. The power button will trigger a safe shutdown of your Pi (note that it doesn't completely cut power, and to do that you'll need to switch off or unplug the power supply once the activity lights have gone out on your Pi).

## Adding your own stations

The list of stations is in a file in `/home/pi/.config/vlc` called `playlist.m3u`. You can edit it by typing `sudo nano /home/pi/.config/pi/vlc/playlist.m3u` in a terminal, adding the URLs for the stations, one per line, and then pressing `control` and `x`, then `y`, then `enter` to save and exit. After rebooting (type `sudo reboot`) the new stations should be available.

There's also an easier way to do this. Shut down your Pi (type `sudo shutdown -h now` in the terminal) and remove the micro SD card. Pop it into your desktop or laptop's SD card slot, and it should mount the `boot` partition. You can now use your favourite text editor to add the URLs of the internet radio stations, one per line, saving the file with the filename `playlist.m3u`. When you put the SD card back into your Pi, our software will copy that file across to `/home/pi/.config/pi/vlc/playlist.m3u` and the new stations that you added should be available.

You should be able to find URLs for streaming internet radio stations by Google-ing something like "internet radio stream URLs".

## Taking it further

VLC actually includes a rudimentary web interface for controlling the stream remotely. You should be able to access this by going to the URL `http://raspberrypi.local:8080` or `http://192.168.0.2:8080` (where 192.168.0.2 is the IP address of your Pi) in your browser.
