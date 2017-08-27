# Raspberry Pi Plex Server: Setup Your Very Own Media Server

_Captured: 2017-08-18 at 18:54 from [pimylifeup.com](https://pimylifeup.com/raspberry-pi-plex-server/)_

![Raspberry Pi Plex Server](https://pimylifeup.com/wp-content/uploads/2016/06/Raspberry-Pi-Plex-Server.jpg)

In this tutorial I go through all the steps to getting your very own Raspberry Pi plex server up and running. This is perfect for anyone who wants to have a media server that can be accessed by anyone within a household. You can also set it up to be accessed outside your local network.

Plex is a client server setup where the client simply streams data from the plex media server. This means you can have all your movies, music and photos located on the one device, the server. In this case we will be using the Raspberry Pi. You can then have multiple clients connect to the same server. This is great as you don't need have multiple copies of the same media across several devices.

The [plex client](https://www.plex.tv/) is supported on a ton of devices including Windows, Apple, Android, [Amazon FireTV](https://pimylifeup.com/out/amazon/firetv), Chromecast, Xbox, PlayStation, Linux and so many more. It really is an amazing home media solution.

If you just want a single client without the whole server setup then something like the [Raspberry Pi XBMC (Kodi)](https://pimylifeup.com/raspberry-pi-xbmc-media-center/) media centre might interest you more.

If you want to hear me go through all the steps, then you can find the video below. If you do like the video and would love to stay up to date, then please make sure you subscribe!

You will need the following equipment to be able to complete this Raspberry Pi Plex server tutorial.

### Recommended:

[Ethernet Cord](https://pimylifeup.com/out/amazon/ethernetcord) or [Wifi dongle](https://pimylifeup.com/out/amazon/wifidongle) (Best to stick with Ethernet for a media server though)

### Optional:

** NOTE:** This will not work at all on older versions of the Pi. Only Raspberry Pi 2 or later will work.

##  Setting up the Raspberry Pi Plex Server

In this tutorial I will be using Raspbian Jessie so if you haven't got it installed then check out my guide on [how to setup Raspbian here](https://pimylifeup.com/noobs-raspberry-pi/). If you want to run a slim version of Raspbian then you should take a look at installing Raspbian lite.

It's important to make sure you have expanded the SD card to the full size, this setting is found in [the Raspi-config](https://pimylifeup.com/raspi-config-tool/). If you installed via the NOOB installer then you don't need to do this.

Since there is no official ARM plex server we will need to download and use a repackaged ARM version from [day2dev](https://www.dev2day.de/typo3/projects/plex-media-server/).

**1.** As with any software tutorial let's first make sure our Pi is up to date
    
    
    sudo apt-get update
    sudo apt-get upgrade

**2.** We next need to enable the HTTPS transport package so we can access HTTPS packages using apt-get. Enter the following line to download, install & activate it.
    
    
    sudo apt-get install apt-transport-https

**3.** Next we need to add a crypt o key for the dev2day website to our [keyring](https://wiki.debian.org/SecureApt). The | in the following command copies the output from the first command (`wget`) into the second command (`sudo apt-get add - _"**first command output"**_`).
    
    
    wget -O - https://dev2day.de/pms/dev2day-pms.gpg.key  | sudo apt-key add -

**4.** Next we need to add the dev2day repository to our package source list. To do this simply enter the following.
    
    
    echo "deb https://dev2day.de/pms/ jessie main" | sudo tee /etc/apt/sources.list.d/pms.list

**5.** Now we need to update the package list, you can do this by running the following command:
    
    
    sudo apt-get update

If you get the error "`/usr/lib/apt/methods/https could not be found.`" Then the https transport package hasn't been installed. Double check that it has been installed correctly.

**6.** Now run the following to install the plex media server onto the Raspberry Pi.
    
    
    sudo apt-get install -t jessie plexmediaserver

If you get an **error** at this step then be sure to check out my troubleshooting section at the bottom of this tutorial.

**7.**To avoid any annoying permission problems, change plex to run under the Pi user. To do this open the following file.
    
    
    sudo nano /etc/default/plexmediaserver

**8.**Change the user from plex to pi.
    
    
    PLEX_MEDIA_SERVER_USER=pi

**9.**Now restart the plex media server.
    
    
    sudo service plexmediaserver restart

**10.**Now it should all be installed but before we get started we should make sure the Pi has a static IP so it's easy to remember the IP address. To get your current IP address enter the following:
    
    
    hostname -I

**11.** Now open up the cmdline.txt file.
    
    
    sudo nano /boot/cmdline.txt

**12.**At the bottom of this file, add the following line: (Replacing "YOUR IP" with the IP you got from using hostname -I)
    
    
    ip=YOUR IP

**13.**Once done, exit by pressing `ctrl x` and then `y` to save.  
**14.**Now simply restart the Pi by running the following command.
    
    
    sudo reboot

**15.**The Pi should now always start with the same IP. You can also set this on most routers by tying the mac address of your network device (WiFi or Ethernet) to a IP.

Now the Raspberry Pi Plex media server should be all setup and ready to scan your media and stream it any client that wishes to connect. I will go through some basics on setting everything up below.

##  Storing Media on the Raspberry Pi

Now there are several ways to store your media on the Raspberry Pi. I will mention each of the methods below.

You can just hook up an external hard drive with all your music, movies and whatever else you may have. Setting the Plex program to run as the Pi user means you can just plug a USB hard drive in and access the media in Plex without any issues. You can also permanently mount drives; I have already covered this in a previous tutorial so be sure to check out my guide on how to [mount a USB hard drive to the Raspberry Pi](https://pimylifeup.com/raspberry-pi-mount-usb-drive/). Make sure you set the user & group owner of the drive to **Pi**.

You could also set your Pi up to act as a NAS so you can transfer your media across to it without needing to disconnect/reconnect a hard drive. You can set this all up by following my tutorial on setting up a [Raspberry Pi network attached storage](https://pimylifeup.com/raspberry-pi-nas/). Again make sure you set the group & user owner to Pi or whatever the user Plex is running as.

Lastly you can just use the SD card for storage but as you could imagine this will quickly run out of space. You can setup a folder on the SD card to be accessed via the network.

##  Connecting Clients to The Plex Media Server on the Raspberry Pi

If you're using an app on your phone, computer, Xbox, PlayStation or any other device then the Plex client should be able to pick up on the server automatically. You will unfortunately find the official mobile Plex applications are behind a paywall. For example, you will need to pay money to get full access to all the features. However all other apps including the web app should be free with only a small set of features requiring a subscription.

To connect in the browser simply enter the IP followed by the port `32400` and `/web/`. For example, mine is.
    
    
    192.168.1.100:32400/web/

You will be prompted to login, simply sign up or sign in to an existing plex account. You can skip this by just entering by entering the address above in again.

Next you will need to setup your music, movie and TV show libraries. This is incredibly easy and shouldn't be too hard in getting it setup correctly.

**1.** First select add library in the left hand side column.

![Add Library](https://pimylifeup.com/wp-content/uploads/2016/06/add-library.png)

**2.** Next select the type of media that is in the folder. If you have more than one type, then you will need to add a new library for each type of media.

![Media Type](https://pimylifeup.com/wp-content/uploads/2016/06/media-type.png)

**3.** Next you will need select the folder that has all your media in it. For example, mine is on a USB drive that is displayed in the left hand side column or can be found at `/media/pi/ESD-USB`

![Add Folder](https://pimylifeup.com/wp-content/uploads/2016/06/add-folder.png)

**4.** Once you add the library it will now organise your clips in a nice easy to browse interface.

If you need more information on how to setup, name and organise your media library then Plex has an amazing amount of documentation that you can find [here](https://support.plex.tv/hc/en-us/categories/200028098-Media-Preparation).

##  Troubleshooting

One issue I came across when it came to downloading and installing the package was that it couldn't connect to dev2day.de servers. I got the following error. (This is just a snippet of the error)
    
    
    “E: Failed to fetch https://dev2day.de/pms/pool/main/p/plexmediaserver/plexmediaserver_0.9.16.4.1911-ee6e505-2~jessie_all.deb 
    Failed to connect to dev2day.de port 443: Network is unreachable
    
    E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?”

Fixing this problem was surprisingly easy after spending hours of troubleshooting. Simply edit the file with our package source list where we added the dev2day.
    
    
    sudo nano /etc/apt/sources.list.d/pms.list

In here simply change dev2day to just normal http. For example, it should look like this.
    
    
    deb http://dev2day.de/pms/ jessie main

Once that is done simply run _sudo apt-get update_ and then try updating again.

I hope that you have been able to get the Raspberry Pi Plex server up and running without any trouble. If you come across any issues or have some feedback, then please don't hesitate to leave a comment below.
