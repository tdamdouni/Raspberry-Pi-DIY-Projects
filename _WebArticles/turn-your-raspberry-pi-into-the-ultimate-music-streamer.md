# Turn your Raspberry Pi into the ultimate music streamer

_Captured: 2017-05-19 at 15:42 from [www.cnet.com](https://www.cnet.com/how-to/turn-your-raspberry-pi-into-the-ultimate-music-streamer/)_

![raspberry-pi-3-things-to-consider.jpg](https://cnet3.cbsistatic.com/img/zCLI4RlSMOkCr-pJnPZWt-WqrCY=/fit-in/370x0/2016/05/19/e082d6e9-b0fa-439a-82ef-1032fa6d37cd/raspberry-pi-3-things-to-consider.jpg)

> _Taylor Martin/CNET_

The number of [things you can do with a Raspberry Pi](https://www.cnet.com/pictures/13-fun-things-to-try-with-your-raspberry-pi/) is astounding. For a little over $35, you can create a networked media server for streaming all your digital movies to your TV or give your existing printer wireless capabilities. And that's just the tip of the iceberg.

If you've yet to decide on what you want to do with your Raspberry Pi, this project shows you how to turn it into a Chromecast Audio-like music streamer. This means you could set up several Raspberry Pis this way, connect each one to a speaker, place them around your house and stream music to each those speakers remotely in a highly configurable way. You can control the music from your phone, tablet or computer.

It's an easy project that you can have set up and running in under an hour.

### What you will need

For starters, you will need a [Raspberry Pi ](https://www.amazon.com/gp/product/B01CD5VC92/)(1, 2 or 3) and the [Pi MusicBox operating system](http://www.pimusicbox.com/). Installation and setup will be easier with the older two Raspberry Pi models. It is possible with a Raspberry Pi 3, but the process will be slightly more involved, since the latest update to the code was written for the Raspberry Pi 2.

Additionally, you need an SD or microSD card, a [Wi-Fi adapter for the Raspberry Pi](https://www.amazon.com/Raspberry-Pi-WIFI-Adapter-Dongle/dp/B009FA2UYK) (even for the Raspberry Pi 3, despite its in-built Wi-Fi) and a speaker or sound system. A computer is necessary to write the images to the SD card and the initial setup, but to control what music is playing, you can use just about any device with access to a web browser.

### Installing Pi MusicBox

To install Pi MusicBox, first download the latest image from [pimusicbox.com](http://www.pimusicbox.com/). Extract the contents of the ZIP and locate the image file.

From this point, the installation process is like with any other operating system installation on a Raspberry Pi without NOOBS. Follow the same instructions [found here](https://www.cnet.com/how-to/install-raspbian-on-a-raspberry-pi-without-noobs/), substituting the Pi MusicBox image in the place of the Raspbian.

#### If you have a Raspberry Pi 3

Up to this point, the installation for the Raspberry Pi 3 is identical. But in order to get the software to boot on your Pi 3, you will need to make some changes, as [noted by Bennett Hollstein](http://bennetthollstein.de/wordpress/?p=147).

  * Download the previous version (read: _not_ the most current version) of the Raspbian Jessie Lite image from the [Raspberry Pi Foundation website](https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2016-03-18/). An update to the kernel in the most recent version of Jessie Lite breaks this workaround. 
  * Extract the contents of the ZIP file and open the image. On Mac, you can do this by right clicking the file and selecting **Open With > DiskImageMounter**. On Windows, Hollstein suggests using a program like **PowerISO** to open the image file.
  * Copy all the files ending in .dat, .elf and .dtb, as well as bootcode.bin over from the Jessie Lite image to to the root directory of the Pi MusicBox SD card. When prompted, choose to overwrite the existing files.

Once you have overwritten all the files with those from the Jessie Lite image, you should be able to boot Pi MusicBox on the Raspberry Pi 3.

### Setting it up as a music streamer

This operating system does not require an external display. You will control the music and settings of the Raspberry Pi through a web browser. As such, you will need to change some settings before ejecting the SD card and inserting it into the Raspberry Pi.

Open the drive on which you just installed Pi MusicBox and locate the **config** folder. Inside this folder is a file called **settings.ini**. Open this file in a text editor and locate the **Network Settings** section. Enter your wireless network's SSID beside **wifi_network** and the password beside **wifi_password**. (_Note: Pi MusicBox only works with WPA security, not WEP._) Don't forget to save your changes when you're finished.

Optionally, you can enter your credentials for Spotify, Last.fm, SoundCloud, Google Play Music, YouTube, Dirble, Subsonic and TuneIn Radio before saving your changes and inserting the SD card into the Raspberry Pi. To enable these services, locate the enabled field in the **settings.ini** file and replace "**false**" with "**true**." The more changes you make to the **settings.ini** file prior to the first boot, the higher the risk of having to perform the installation again, but I was able to insert my Spotify credentials and enable it prior to the initial boot without a problem.

### **Playing music**

Once you've inserted the SD card into the Raspberry Pi, power on the device by inserting the power adapter and give it a few minutes to boot.

Then navigate to **http://musicbox.local** in a web browser -- this can be done from a computer, smartphone or tablet. Open **Settings** and enable and enter your login credentials for any streaming services you plan to use. You can enable SSH for remotely controlling the Raspberry Pi through a terminal, enable AirPlay and change the name of the device (to something like LivingRoom or Kitchen) or set the default volume (your ears will thank you later). When you're finished, click **Update settings (reboot)** at the bottom and wait for the Raspberry Pi to fully reboot. This seems to take just a little longer than a standard Pi reboot.

To play music, navigate back to the Pi MusicBox web portal. If you changed the name of the device, you will also need to use a different URL to access the Raspberry Pi. The first part of the URL will be the name of the device. For example, if you renamed it to **Kitchen**, you will need to go to **http://kitchen.local**.

You can view all your playlists under the **Playlist** section, browse stations on TuneIn Radio or top charts on Spotify under **Browse**, play streams directly with a URI under **Streams** or search one or all connected services with the **Search** tab. When you click on a song, it should automatically begin playing on the speaker you have connected to the Raspberry Pi.
