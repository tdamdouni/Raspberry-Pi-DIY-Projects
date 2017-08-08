# Streaming Airplay to your Pi

_Captured: 2017-05-23 at 20:06 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/streaming-airplay-to-your-pi)_

We've put together a really easy little installer to set up your Pi as an Airplay speaker, letting you stream music from your iPhone (sorry Android users). The installer gives you the choice of setting it up with support for three of our pHATS - [pHAT BEAT](https://shop.pimoroni.com/products/phat-beat), [pHAT DAC](https://shop.pimoroni.com/products/phat-dac), or [Speaker pHAT](https://shop.pimoroni.com/products/speaker-phat) \- or just with the standard audio through the Pi's 3.5mm stereo jack.

This tutorial is perfect for the [Pirate Radio Kit](http://shop.pimoroni.com/products/pirate-radio-pi-zero-w-project-kit), or if you want to use our [Speaker pHAT](http://shop.pimoroni.com/products/speaker-phat) board to give new life to an old radio by wiring it up to the radio's existing speaker.

We'll cover preparation that's needed for each device, and then go through how to run the installer. Note that you'll need a keyboard, mouse, and display connected to your Pi for this.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/pi-airplay-hires.jpg)

## Installing Raspbian

We recommend using the very latest version of Raspbian **Lite**, and you'll need an internet connection to install the Mopidy packages later. We'd recommend using either the NOOBS installer, which you can find [here](https://www.raspberrypi.org/downloads/noobs/) (ensure that you select Raspbian Jessie **Lite** when installing), or downloading Jessie Lite from [here](https://www.raspberrypi.org/downloads/raspbian/) and then using the [Etcher](https://etcher.io/) tool to burn the image to your SD card.

Currently, our airdac installer is best supported by Jessie Lite, and may not work properly in the full version of Raspbian. Because Jessie Lite is... liter (_sic_) it should also run a bit more snappily than the full Raspbian.

## Using the Pi's built-in 3.5mm stereo jack

If you're using the built-in audio on your Pi model B+, 2, or 3, then there's no other preparation needed other than popping in your SD card and making sure that you have an internet connection, either from wired ethernet or by connecting to Wi-Fi (more on how to connect to Wi-Fi in Jessie Lite below).

## Using pHAT DAC

If you're using our pHAT DAC board, then you need to solder the 2x20 pin female header (that comes with it) to your pHAT DAC (and also solder a 2x20 pin male header to your Pi Zero or Pi Zero W, if you're using one). We have a guide on how to solder headers to pHATs [here](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats).

## Using pHAT BEAT or the Pirate Radio Kit

If you're using the Pirate Radio Kit and haven't already built it, then follow our guide [here](https://learn.pimoroni.com/tutorial/sandyj/assembling-pirate-radio) to learn how to put it all together.

If you're just using pHAT BEAT, then make sure that you've soldered the 2x20 pin female header to it. Again, you can follow our [guide](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats) to soldering pHATs. Connect a couple of speakers (or just one) to your pHAT BEAT's push fit speaker terminals.

## Using Speaker pHAT

If you're using Speaker pHAT, then follow our guide to soldering it [here](https://learn.pimoroni.com/tutorial/sandyj/assembling-speaker-phat).

## Running the installer

Just to reiterate, you'll need an internet connection to run this installer. Pop the SD card into your Pi, make sure that the audio board that you're using is attached to your Pi (on its GPIO pins) if you're using one, and then plug in the power and boot up your Pi. Because you're using Jessie Lite, your Pi will boot straight to a terminal, but don't be scared!

You'll need to connect to Wi-Fi. To do this, you need to edit a file called `wpa_supplicant.conf`. Type the following:
    
    
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    

Use the arrow keys to move to the bottom of the file, and add the following, replacing the parts that say "YOUR_SSID" and "YOUR_PASSWORD" with the SSID and password for the Wi-Fi network to which you'd like to connect.
    
    
    network={
    ssid="YOUR_SSID"
    psk="YOUR_PASSWORD"
    }
    

Once you've made those changes, press `control` and `x`, then `y`, and then `enter` to save and close the file.

Now, type `sudo reboot` and press `enter` to reboot. Your Pi should now be connected to Wi-Fi.

To run the installer, type the following:
    
    
    curl -sS get.pimoroni.com/airdac | bash
    

The installer will prompt you several times, and you should type `y` for all of these, with the exception of the device selection. When it prompts you to select a device, then type the number of the device that you'd like to install. Note that if you're using the built-in audio through the 3.5mm jack then you should select option 0 here.

The installer should also ask if you'd like to reboot once the installation is complete. If it doesn't, then restart by typing `sudo reboot` again.

## What the installer does

The installer will do several things, that you don't necessarily have to worry about, so stop reading this section now if that's the case!

First, if you're using one of our audio boards like pHAT DAC, pHAT BEAT, or Speaker pHAT, then the installer will configure your Pi's ALSA audio to route audio out through I2S, the interface used by these boards.

Second, it will install any additional software required, like the software that controls the LEDs on Speaker pHAT and pHAT BEAT. These both use an ALSA audio plugin that actually processes the audio data (using FFT) and displays it on the LEDs. It's called [pivumeter](https://github.com/pimoroni/pivumeter).

Third and last, it will install the [shairport-sync](https://github.com/mikebrady/shairport-sync) software that allows you to stream via Airplay to your Pi. This will be set to run at boot, so as soon as the installer is finished and your Pi has rebooted it should automagically appear as an Airplay device.

## Streaming Airplay

Assuming that worked, you should now be able to stream to your Pi from your iPhone. Start your music playing, and then tap on the Airplay icon and select the device that will have the name "Raspberrypi", unless you have changed the hostname on your Pi.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/airplay-renders.jpg)

_Note that if you're using on of our I2S devices with an amp. (Speaker pHAT or pHAT BEAT), you may hear a slight pop when the device connects and disconnects the audio stream. This is due to the way that the Raspberry Pi and ALSA cut the audio stream when audio is not being output, to prevent overheating of your connected speaker._
