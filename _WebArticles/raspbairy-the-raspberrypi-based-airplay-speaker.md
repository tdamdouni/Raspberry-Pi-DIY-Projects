# RaspbAIRy - the RaspberryPi-based Airplay Speaker

_Captured: 2017-05-19 at 15:43 from [www.google.de](https://www.google.de/amp/www.instructables.com/id/raspbAIRy-the-RaspberryPi-based-Airplay-speaker/%3Famp_page%3Dtrue)_

![RaspbAIRy - the RaspberryPi-based Airplay Speaker](https://cdn.instructables.com/FD5/WYUW/HAQ3C8VV/FD5WYUWHAQ3C8VV.MEDIUM.jpg?width=614)

With the delivery of my second RaspberryPi I finally got the chance to start this long-planned project:

I wanted to replace my old bathroom radio with a more contemporary device by building a network-enabled speaker. Because I'm a user of several iDevices, the idea of making the speaker AirPlay-compatible became the basis of my further work.  
After some googling I discovered James Laird's amazing [shairport](https://github.com/albertz/shairport) client for Linux. The initial installation on the RasPi worked like a charm, so I decided to take the project one step further by making it wireless. With a little help from Google again and some twiddling I finally got it to work and started writing this Instructable.

Have fun reading how it all went down and maybe build your own version of the raspb**AIR**y.

## Step 1: Parts & Tools

![Parts & Tools](https://cdn.instructables.com/FTB/JFN5/HBNXV58S/FTBJFN5HBNXV58S.MEDIUM.jpg)

This Instructable is based on the metric system and originates from Germany, thus dimensions are in millimeters and line voltage is 220V. I got most of the parts at my local electronics retailer or already had them laying around. The RasPi was ordered online at [Farnell](http://export.farnell.com/rp/order/?COM=raspi-group), the speaker cloth was found on [eBay](http://ebay.com) and the MDF was bought and already cut in width at a local hardware store.

  * **RaspberryPi**
  * **Sound**
  * **Case**
  * **Tools**

Saw  
Screwdriver and screws  
Soldering iron and solder  
Stapler  
Other typical workshop equipment

## Step 2: Electronics

![Electronics](https://cdn.instructables.com/FO6/15CO/HBUZF531/FO615COHBUZF531.MEDIUM.jpg?width=614)

  * **Stereo to Mono**

Following the great guide of Dennis Bohn "[Why not Wye](http://www.rane.com/note109.html)", I chose to integrate an easy summing circuit or actually two, one for each audio input.

  * **Input Switch**

A simple dip switch (ON-ON) for selecting the audio input for the amp. I added this to be able to connect other audio sources and to use the device as a 'normal' speaker, independent from the RasPi.

  * **Mono Amp and speaker**

The selected amplifier was wired according to the datasheet. Basically it accepts input voltages from 5 to 12V DC and a mono input signal through an optional potentiometer for volume control. I connected a 8Ω broadband speaker, which sounds surprisingly good for only 10€.

  * **Power Supply**

I chose to integrate two separate power units to be able to independently turn off the amp/speaker while keeping the RasPi running. This is mainly due to the boot time of Raspbian of about 30-40 seconds. Because I had them laying around I used two plug-in adapters, one providing 5V DC (max. 2500mA) for the RasPi and the other providing 12V DC (max. 1500mA) for the whole audio setup.

## Step 3: Installation

![Installation](https://cdn.instructables.com/FTI/P91J/HAQ39MSI/FTIP91JHAQ39MSI.MEDIUM.jpg?width=614)

  * **Raspbian 'wheezy'**

After downloading the [official image](http://www.raspberrypi.org/downloads) and following these [easy steps](http://elinux.org/RPi_Easy_SD_Card_Setup), the RasPi was set up in a few minutes.  
The following steps require some basic command line skills but if you stick to the linked tutorials you should be good.

  * **Shairport**

I found two different documentations to be of great help, one in [English](http://pi-raspberry.blogspot.de/2012/08/shairport-raspberry-pi.html) and one in [German](http://www.forum-raspberrypi.de/Thread-tutorial-airplay-mit-dem-raspberry-pi-shairport-installation). These include nearly the same steps:

  1. Install some packages and their dependencies, that shairport uses, via _apt-get_
  2. Get shairport and the perl module Net::sdp via _git_
  3. Install shairport as a service and make it run at startup 
  * **Wifi**

Support for some Wifi chipsets is already included in Raspbian. I found a USB Adapter with the RT5370 chipset for a few bugs at a local electronics store. In addition to its Linux ability it is also very economical on power. It therefore can be driven on one of the onboard USB ports of the RasPi. A [video tutorial](http://www.adafruit.com/blog/2012/09/07/how-to-wifi-wireless-internet-on-raspberry-pi-piday-raspberrypi-raspberry_pi/) from Adafruit then did the trick for me.

  * **Here is what I did (commands in_ italic_):**
  1. Updated apt-get 
    * __$ _sudo apt-get update_
  2. Installed vim (personal preference) 
    * __$ _sudo apt-get install vim_
  3. List USB devices to get infos on wifi dongle 
    * _$ lsusb_
  4. Installed Ralink-Firmware 
    * _$ sudo apt-get install firmware-ralink_
  5. Modified the interfaces config 
    * _$ sudo vim /etc/network/interfaces_
    * auto lo  
iface lo inet loopback  
iface eth0 inet dhcp  
auto wlan0  
iface wlan0 inet dhcp  
wpa-ssid "_my_ssid_"  
wpa-psk "_my_password_"
  6. Reboot 
    * _$ sudo reboot_
  7. Checked that wifi is running 
    * _$ ifconfig -a_
  8. Installed all dependencies for shairport 
    * _$ sudo apt-get install git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils_
  9. Installed Net::SDP for iOS6 support 
    * _$ git clone https://github.com/njh/perl-net-sdp.git perl-net-sdp _
    * _$ cd perl-net-sdp_
    * _$ perl Build.PL_
    * _$ sudo ./Build _
    * _$ sudo ./Build test _
    * _$ sudo ./Build install _
    * _$ cd .._
  10. Got shairport from git 
    * _$ sudo git clone https://github.com/albertz/shairport.git shairport_
  11. Changed to shairport directory and compiled 
    * _$ cd shairport/_
    * _$ sudo make_
    * _$ sudo make install_
  12. Copied the init sample to startup folder and set rights 
    * _$ sudo cp shairport.init.sample /etc/init.d/shairport_
    * _$ cd /etc/init.d_
    * _$ sudo chmod a+x shairport_
    * _$ sudo update-rc.d shairport defaults_
  13. Changed name of shairport client 
    * _$ sudo vim shairport_
    * changed the following lines: 
    * NAME=ShairPort  
DAEMON="/usr/local/bin/shairport.pl"  
PIDFILE=/var/run/$NAME.pid  
DAEMON_ARGS="-w $PIDFILE -a raspbAIRy"
  14. Set audio output to line 
    * _$ amixer cset numid=3 1_
  15. Started shairport 
    * _$ sudo /etc/init.d/shairport start_

## Step 4: Case

![Case](https://cdn.instructables.com/FAG/WFF0/HAQ39MO8/FAGWFF0HAQ39MO8.MEDIUM.jpg)

![P1080967.jpg](https://cdn.instructables.com/FZY/ZQ9Z/HAQ39MO9/FZYZQ9ZHAQ39MO9.LARGE.jpg)

![P1080969.jpg](https://cdn.instructables.com/F2R/OK9R/HAQ39MOA/F2ROK9RHAQ39MOA.LARGE.jpg)

![P1080970.jpg](https://cdn.instructables.com/FBB/2GBB/HAQ39MOB/FBB2GBBHAQ39MOB.LARGE.jpg)

![P1080972.jpg](https://cdn.instructables.com/FFQ/79E3/HAQ39MOC/FFQ79E3HAQ39MOC.LARGE.jpg)

> _Show All Items_

![P1080973.jpg](https://cdn.instructables.com/FWQ/VWZ4/HAQ39MOD/FWQVWZ4HAQ39MOD.LARGE.jpg)

  * The case is a simple 200 x 200 x 210mm cube-shaped box made of 5mm MDF, with the side parts being mitered with a 45° angle.
  * On the front I made cutouts for the speaker, the volume knob and the power LED. It was covered with light-grey speaker cloth and clipped on with wooden dowels.
  * The back shows holes for the power chord, power switch, audio jack and input switch and is held in place by wood screws.

## Step 5: Wiring

![Wiring](https://cdn.instructables.com/F9G/MIPS/HAQ39MUN/F9GMIPSHAQ39MUN.MEDIUM.jpg?width=614)

![P1090001.jpg](https://cdn.instructables.com/FYV/IPN4/HAQ39MUO/FYVIPN4HAQ39MUO.LARGE.jpg)

![P1090003.jpg](https://cdn.instructables.com/FQA/EZQS/HAQ39MUP/FQAEZQSHAQ39MUP.LARGE.jpg)

![P1090006.jpg](https://cdn.instructables.com/FTA/1FJD/HAQ39MUQ/FTA1FJDHAQ39MUQ.LARGE.jpg)

![P1090008.jpg](https://cdn.instructables.com/FLZ/VO5K/HAQ39MUS/FLZVO5KHAQ39MUS.LARGE.jpg)

![P1090009.jpg](https://cdn.instructables.com/FX8/WJA5/HAQ39MUT/FX8WJA5HAQ39MUT.LARGE.jpg)

## Step 6: Final Closeups

![02.jpg](https://cdn.instructables.com/FMM/N07Y/HAQ3C8VX/FMMN07YHAQ3C8VX.LARGE.jpg)

![03.jpg](https://cdn.instructables.com/FEU/09XP/HAQ3C8VY/FEU09XPHAQ3C8VY.LARGE.jpg)

![04.jpg](https://cdn.instructables.com/FJO/PJ8L/HAQ3C8W0/FJOPJ8LHAQ3C8W0.LARGE.jpg)

![05.jpg](https://cdn.instructables.com/FY2/DWPQ/HAQ3C8W1/FY2DWPQHAQ3C8W1.LARGE.jpg)

> _Show All Items_

![06.jpg](https://cdn.instructables.com/FVT/U44U/HAQ3C8W2/FVTU44UHAQ3C8W2.LARGE.jpg)

## Step 7: Modifications and Future Plans

![Modifications and Future Plans](https://cdn.instructables.com/F40/1QAT/HAQ3C90C/F401QATHAQ3C90C.MEDIUM.jpg?width=614)
