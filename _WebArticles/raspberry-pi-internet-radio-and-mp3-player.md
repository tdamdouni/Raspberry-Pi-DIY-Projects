# Raspberry Pi Internet Radio and MP3 Player

_Captured: 2018-03-30 at 11:41 from [www.hackster.io](https://www.hackster.io/Granpino/raspberry-pi-internet-radio-and-mp3-player-1aa591?utm_source=Hackster.io+newsletter&utm_campaign=d118c2eb03-EMAIL_CAMPAIGN_2017_07_26&utm_medium=email&utm_term=0_6ff81e3e5b-d118c2eb03-141949901&mc_cid=d118c2eb03&mc_eid=1c68da4188)_

![Raspberry Pi Internet Radio and MP3 Player](https://hackster.imgix.net/uploads/attachments/452880/20180321_163838_oqHwHllX2w.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

Raspberry pi internet radio and mp3 player

This internet radio and mp3 player uses a 3.5 HDMI LCD touch screen for operation. The original project was published by Adafruit. [https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen/overview](https://learn.adafruit.com/raspberry-pi-radio-player-with-touchscreen/overview.) The project uses MPC , MPD and Pygame.

**Installation:**

  * Download the raspbian stretch image and burn to a 8GB or bigger SD card. To start you should be know how to SSH to the raspberry pi. You can also connect a mouse and keyboard to the pi and install everything locally. See <https://www.raspberrypi.org/documentation/>
  * Attach the LCDscreen to the raspberry pi. 
  * Open the terminal screen and type

sudo raspi-config

  * set internationalisation options and change Timezone 
  * Go to Advanced Options and enable VNC, SSH and set the resolution to 640x480
  * Exit and reboot.
  * The stretch image takes a lot of space on the SD card and we need to make room for the MP3 music. SSH to the Pi and delete Wolfram and Libreoffice, or use the mouse on the Pi and select add/remove.

_sudo apt-get purge wolfram-engine libreoffice* -y _

_sudo apt-get clean _

_sudo apt-get autoremove _

_sudo apt-get update _

_sudo apt-get upgrade_

  * After the upgrade you are ready for the installation. Now install the LCD drivers.

_git clone https://github.com/goodtft/LCD-show.git_

_chmod -R 755 LCD-show_

_cd LCD-show_

_sudo ./MPI3508_600_400-show_

  * The resolution used with the pi-radio is 640x480, therefore you need change the config.txt.

_sudo nano /boot/config.txt_

  * and change the resolution at the bottom of the file to 640x480. Save, exit and reboot.

_sudo reboot_

  * At this point the Pi should boot to the stretch desktop and the touchscreen working. Now install the Pi-radio files.

_sudo apt-get install mpc mpd_

_cd_

_chmod -R 755 Pi-Radio-mp3-_

_cd_ _Pi-Radio-mp3- _

_sudo ./install.sh_

  * The installation file will create the required playlists for mp3 and internet radio. There should be an icon on the raspberry desktop. To open the Pi-radio double tap on the radio shortcut. To change the desktop for a single click go to file manager, click on Edit and at the very bottom select preferences. Select 'open files with single click'.
  * The application uses pygame and the touchscreen will only run under lx-terminal. I you run the application from SSH, the touchscreen will work upside down. I elected to run the app from the desktop because I want to run other apps on the same Pi that use the LCD screen. I did not have to calibrate the screen to make it work. I included some sample mp3 files and radio stations for your testing. To add other radio stations to the playlist go to <http://www.radiosure.com/stations/> and copy the m3u links. 

_mpc add <link of station>_

_mpc save playlist _

  * or edit the file 

_sudo nano ~/var/lib/mpd/playlists/playlist _

  * To add other mp3 files, transfer these to the Music folder and type 

_sudo ls -1 /home/pi/Music/*.mp3 > /var/lib/mpd/playlists/mp3.m3u_

This project was a lot of fun to put together and I learned a lot about python. There is a lot of room for improvement. In the future I would like to add Pandora.
