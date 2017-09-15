# Setting up pHAT DAC

_Captured: 2017-09-07 at 10:13 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/phat/raspberry-pi-phat-dac-install)_

This guide will explain how to get pHAT DAC up and running on your Raspberry Pi using the Raspbian operating system.

Before you start, you should make sure that Raspbian is up-to-date, either by [following our guide](http://learn.pimoroni.com/tutorial/raspberry-pi/keeping-your-raspberry-pi-updated) or [downloading and installing the latest version](https://www.raspberrypi.org/downloads/raspbian/).

pHAT DAC provides a line-level output, which means you should connect it to some speakers or a stereo system ready to test your set up. Don't use headphones!

Note that this configuration will disable the default sound modules on your Pi, so that sound will _only_ play through the DAC. We're looking into a better configuration to allow switching between the two, but for now this is the way to go.

## Automated Set Up

First you should fire up Terminal on your Raspberry Pi. If you boot up to it, great, you're set, if you boot to desktop you can find it in the Raspberry Pi menu under Accessories.

The easiest way to get going with your shiny new pHAT DAC is to use our one-line installer, like so:
    
    
    curl https://get.pimoroni.com/phatdac | bash
    

This script will set everything up for you whether you are running Raspbian Wheezy or Jessie (including Jessie Lite). You will need to reboot your Pi after the script has completed.

Once that is done and your Pi has been rebooted you may, if you like, run the above script again and it will offer you to test your setup summarily. PLEASE set your speakers at a low volume first however, then progressively raise the levels if you can't hear any sound coming out the pHAT DAC!

## Manual Set Up

If you are interested in what the script mentioned above is doing, keep reading, though for most users that isn't necessary, unless you can't hear any sound coming out of the pHAT DAC after running the automatic set up steps as laid out above.

Note that those instructions were initially written for Raspbian Wheezy and meant as a troubleshooting guide outlining the principle of exchanging the default bcm2835 chip for the pHAT DAC to pipe audio through. Additions were made to cover Raspbian Jessie however.

### Step 1: All The Modules

In Terminal, type: `sudo nano /etc/modprobe.d/raspi-blacklist.conf` to open the module blacklist file. This file prevents certain modules from loading at startup. With the file open, comment out the lines corresponding to the modules we want to load by changing:
    
    
    blacklist i2c-bcm2708
    blacklist snd-soc-pcm512x
    blacklist snd-soc-wm8804
    

To:
    
    
    #blacklist i2c-bcm2708
    #blacklist snd-soc-pcm512x
    #blacklist snd-soc-wm8804
    

If some or all of those entry are not present, don't worry, you are trying to disable those modules anyhow!

Finally, close nano by pressing `CTRL+C` followed by `y` for yes, and finally `enter` to confirm. You'll need to remember how to do this in the next few steps, too.

### Step 2: Be Gone, Default Sound

Still in Terminal, open the modules file by typing: `sudo nano /etc/modules`. This file, in contast to the blacklist, lists modules which we do want to load. We're going to remove the default sound driver with a comment, so change the line:
    
    
    snd_bcm2835
    

To:
    
    
    #snd_bcm2835
    

To prevent it loading (this entry should exist, if not you are likely running Raspbian Jessie, which configures the audio chip differently - this will be handled by Step 4).

### Step 3: Sound Config

Finally, create a new `asound.conf` by typing `sudo nano /etc/asound.conf` and entering the following:
    
    
    pcm.!default  {
     type hw card 0
    }
    ctl.!default {
     type hw card 0
    }
    

### Step 4: Device Tree

The last step is to edit your `config.txt`, type `sudo nano /boot/config.txt` and add the line:
    
    
    dtoverlay=hifiberry-dac
    

pHAT DAC uses the same hardware as HiFi Berry, so we're borrowing their device-tree overlay!

While you have that file open, check for the following entry, and if it exists, comment it out:
    
    
    #dtparam=audio=on
    

## Reboot

Finally, reboot your Raspberry Pi and with any luck your audio should now blast through your connected speakers.

Need something for this project? You can use the links below to add products to your [Pimoroni Shop](http://shop.pimoroni.com/) basket for easy checkout.

Want to checkout or change something? Click here to [view your cart](http://shop.pimoroni.com/cart).

## Phil Howard

Phil is Pimoroni's software guru, instantly recognisable by his somewhat pirate-themed moustache growing attempts. Usually found buried neck deep in Python libraries, he's also been known to escape on occasion and turn out crazy new products. If you need a helping hand, he's a prolific Twitter user and rampages around the forums like a T-Rex. Ask him if you need help with Pimoroni's software libraries, or Propeller HAT.
