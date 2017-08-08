# Turn your Raspberry Pi into a Wireless Access Point

_Captured: 2016-12-30 at 00:58 from [www.pi-point.co.uk](https://www.pi-point.co.uk/)_

![_MG_8219b.jpg](https://www.pi-point.co.uk/files/4113/5627/8185/_MG_8219b.jpg)

Welcome and thank you for dropping by. If you're a Raspberry Pi owner and are curious about some of the things you can do with it then this is where you can learn how to turn it into a WiFi Access Point.

There's all sorts of reasons why you may want to do this...

  * Extend your existing WiFi network
  * Learn more about wireless networking
  * Create a free Access Point
  * Build a honeytrap to learn about network-hardening
  * Learn about sniffing packets
  * Provide guest wireless access firewalled off/through your main network
  * Closed wifi monitoring station, e.g. temperature sensor, weather recording
  * Create a Raspberry Pi WiFi HotSpot

Given that you have a Pi, though one of the main reasons is likely to be '_because you can'_ !

To get started, follow the Documentation link above to be guided through setting up a Pi-Point from operating system install to fully working, I hope you find this useful!

\- Guy Eastwood

# HowTo updated for raspberry Pi 3

**8th August 2016** \- Finally reworked and re-tested the HowTo so that it now works as expected on a Raspberry Pi 3 with the new networking changes that use dhcpcd instead of /etc/network/interfaces.

The SD Card page should also now be working again shortly when I've tested some images!

# **Get a preloaded Pi-Point 8GB Class10 Micro SD Card**

We're making preloaded Pi-Point micro SD cards available for £9.95 each with free postage. If you don't want to configure you own card then this is the ideal way to get a Pi-Point up and running!

You can get yourself a preloaded card via the ordering page below.

# Pi-Point is one of the top ten projects on TechRepublic

While rummaging around Google Analytics I spotted that Pi-Point is listed on TechRepublic as one of the top ten projects to try with your raspberry Pi along with making a mobile phone and a Pi cluster. Nice to be ranked alongside such innovative projects!

You can find the top ten here at [Techrepublic's site](http://www.techrepublic.com/pictures/the-top-10-projects-to-try-out-with-your-raspberry-pi-3/10/)

# Site transitioned to HTTPS

You can visit LetsEncrypt yourself at <https://letsencrypt.org>.

# Pi2 problem solved

**7 Nov 2015** \- I've had a few queries from users saying they're having difficulties with their Pi2 and the Pi-Point setup which I finally got around to this weekend. I took the working setup test SD Card from my PiB and put it into my Pi2, which usually runs KODI. I popped the known-to-work USB dongle in and it wouldnt work.

I discovered that the firmware wasn't loading on the USB which seemed to be due to a USB timeout issue. This shows in the syslog as an error 110 when loading the nl80211 firmware. I found a post claiming that these timeouts were often caused by low USB power so I switched the Pi2 from being powered by the AV Amp USB to a phone charger and after booting the 'Test' AP reappeared.

So if you're having problems with getting Pi-Point to work on a Pi2 you might want to try a beefier power source.

# Tested on the Raspberry Pi V3

**18 Apr 2016** \- All seems fine on the Pi3 here, added a couple of informational notes to the doc for Pi3 users.

# Setup documentation re-checked

**22 Sep 2015** \- It's been a good while and a fair few Raspbian releases since I last checked the documentation's validity to see if it still works. Prompted by a few questions from Pi-Point user Royston I decided to follow the docs once more using the latest Raspbian on a Model B and I'm happy to report that it still worked first time here for me from a clean install. Not tried it yet on the Pi2 - will update this entry when I have switched the card from the B to the '2 and given it a go.

# ClosedCloud Walkthrough - a contributed article

Dr Michael Dye has been in touch asking for a few tips on making a closed cloud which he has been kind enough to contribute back to the site as a complete walkthrough guide which you can find via the link below. Thank you very much for your time and effort, Michael!

[Click here for Michael's walkthrough](https://www.pi-point.co.uk/closedcloud-walkthrough/)

# Find the Pi-Point in this month's MagPi magazine!

The Pi-Point project has made it into a four page article in this month's (issue 11) MagPi magazine, check out the writeup and other great tips and tutorials at <http://www.raspberrypi.org/archives/3641>.

# Turn your Raspberry Pi into a web-controlled Torrent Manager

Check out my new tutorial on how to turn your Pi into a completely remote-controlled headless Torrent Manager box with its own web-based front end!

[Click here for the tutorial](https://docs.google.com/document/d/1yEunzA1DHaYake4jQYlgh4IPoxfcHP5CXLqQR_dSGHs/edit?usp=sharing).

# New WPA2-Personal hostapd config added

A big thanks to Simon Gibbon for his hostapd config contribution [here](https://www.pi-point.co.uk/configs-hostapd/wpa2-personal-config/).
