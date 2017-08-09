# Raspberry Pi Zero AirPlay Speaker

_Captured: 2017-05-20 at 16:15 from [frederickvandenbosch.be](http://frederickvandenbosch.be/?p=1447)_

Looking for a new project to build around the Raspberry Pi Zero, I came across the pHAT DAC from Pimoroni. This little add-on board adds audio playback capabilities to the Pi Zero. Because the pHAT uses the GPIO pins, the USB OTG port remains available for a wifi dongle. Perfect for a small wireless speaker project!

The project is fairly simple and requires following components:

  * Raspberry Pi Zero
  * WiPi wifi dongle
  * Two 100 ohms resistors
  * Speaker (4-8 ohms)

The Raspberry Pi Zero is obviously the brains of the project and will run the Shairport software to wirelessly stream music to. The pHAT DAC is a neat little add-on board adding audio to the Raspberry Pi. It has a jack output, and the possibility to add RCA connectors to it. The fact that the RCA connectors are not presoldered is a bonus, as it exposes the audio lines and keeps a low profile. A small mono amplifier from Adafruit then takes the audio from the pHAT and amplifies it (what else?), playing audio from the speaker. A wifi dongle connected via the USB OTG port provides wireless network connectivity for streaming.

I decided to make a mono speaker to keep things smaller. Making this project with stereo support would imply having a second speaker and replace the mono amplifier by a stereo one.

![Screen Shot 2016-01-20 at 22.36.19](http://frederickvandenbosch.be/wp-content/uploads/2016/01/Screen-Shot-2016-01-20-at-22.36.19-1024x818.png)

![IMG_0674](http://frederickvandenbosch.be/wp-content/uploads/2016/01/IMG_0674.jpg)

I know this isn't the nicest way to convert stereo to mono (at all?), but it works. I tried to tackle the problem from a software point of view by [downmixing](http://alsa.opensrc.org/Asoundrc#Downmix_stereo_to_mono) the stereo to mono, but with no success. If I do manage to find a proper solution, ideally in software, I'll be sure to update this post. If anyone has tips on how to achieve this in a simple way, feel free to leave it in the comments!

On the software side, nothing too difficult either.

I started off from the latest Raspbian Jessie image which can be [downloaded](https://www.raspberrypi.org/downloads/raspbian/) from the official Raspberry Pi website.

Using "dd", I put the downloaded image on a 8Gb microSD card and then used it to boot the Pi Zero from.

sudo diskutil unmountDisk /dev/disk3sudo dd if=Downloads/2015-11-21-raspbian-jessie.img of=/dev/disk3 bs=1msudo diskutil unmountDisk /dev/disk3

Once booted, I set up the wifi in the graphical desktop environment by selecting the correct SSID and entering the wifi password. With the Pi Zero connected to the network, I could update the software.

Then came the time to install the project specific software: support for the pHAT DAC and the AirPlay software.

## pHAT DAC

A tutorial on how to install and use the pHAT DAC is [available](http://learn.pimoroni.com/tutorial/phat/raspberry-pi-phat-dac-install) on the Pimoroni website. I did things slightly differently though, as I didn't disable the default sound driver.

Device-tree overlay is used to describe hardware. As the pHAT DAC uses the same hardware as the HiFi Berry, the same overlay can be used by appending the following lines to the config file:

After rebooting, I listed the audio devices using the "aplay" application, and there it was: _card 1 - HiFi Berry_.

12345678910111213141516171819 
pi@raspberrypi:~ $ aplay -l**** List of PLAYBACK Hardware Devices ****card 0: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]Subdevices: 8/8Subdevice #0: subdevice #0Subdevice #1: subdevice #1Subdevice #2: subdevice #2Subdevice #3: subdevice #3Subdevice #4: subdevice #4Subdevice #5: subdevice #5Subdevice #6: subdevice #6Subdevice #7: subdevice #7card 0: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]Subdevices: 1/1Subdevice #0: subdevice #0card 1: sndrpihifiberry [snd_rpi_hifiberry_dac], device 0: HifiBerry DAC HiFi pcm5102a-hifi-0 []Subdevices: 1/1Subdevice #0: subdevice #0

To make it the default for audio playout, I updated the asound.conf file and replaced every reference to "card 0" by "card 1".

1234567891011 
pi@raspberrypi:~ $ sudo nano /etc/asound.confpcm.!default {type hwcard 1}ctl.!default {type hwcard 1}

A final reboot ensured everything was applied.

## ShairPort

Shairport is an Airtunes emulator, allowing compatible iOS devices or iTunes to stream audio to the device running it.

A few dependencies need to be met before Shairport can be installed and run.

123456 
pi@raspberrypi:~ $ git clone https://github.com/njh/perl-net-sdp.git perl-net-sdppi@raspberrypi:~ $ cd perl-net-sdp/pi@raspberrypi:~/perl-net-sdp $ perl Build.PLpi@raspberrypi:~/perl-net-sdp $ sudo ./Buildpi@raspberrypi:~/perl-net-sdp $ sudo ./Build testpi@raspberrypi:~/perl-net-sdp $ sudo ./Build install

With the dependencies taken care of, the actual Shairport software can be installed.

At this stage, it's possible to test if everything was installed properly by manually running the shairport.pl script.

Afetr confirming everything works as expected, the shairport application can be daemonized in order to have it automatically start at boot.

Finally, the shairport file needs to be modified in order to specify the name of the AirPlay device. This could be anything you want. In my case, I picked something generic, such as "AirPi".

Reboot the Pi. Shairport should be running automatically.

Time to package the working AirPlay speaker into something nice, by making a good looking enclosure for it.

This was actually the hardest part of the project. Mainly because I wanted to make it out of wood and with a slightly tricky shape. It meant doing some maths before cutting pieces at the right length using the miter saw and then ensuring the correct angles were cut as well in order to properly connect the pieces. As I'm not a woodworker, and the tools at my disposal are not the most suited either, the results are not always as accurate as you'd expect. That's where sanding paper and wood filler come to the rescue …

![Screen Shot 2016-01-21 at 20.07.53](http://frederickvandenbosch.be/wp-content/uploads/2016/01/Screen-Shot-2016-01-21-at-20.07.53.png)

![Screen Shot 2016-01-21 at 20.05.28](http://frederickvandenbosch.be/wp-content/uploads/2016/01/Screen-Shot-2016-01-21-at-20.05.28.png)

Some accents were given to the build by adding 3D printed parts: the side panels and the speaker grill. One of the side panels was not glued into place and can be removed if needed, in order to access the electronics. I was hesitating to paint the 3D printed parts in a different color for a chrome or brass look, but ended up leaving the pieces as is. It gives the build a little funky side, no ?

![IMG_0708](http://frederickvandenbosch.be/wp-content/uploads/2016/01/IMG_0708.jpg)

Like the project? What else would you make with a Pi Zero? Let me know in the comments!
