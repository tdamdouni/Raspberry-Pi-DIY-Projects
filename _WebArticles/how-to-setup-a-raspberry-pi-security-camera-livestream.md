# How to setup a Raspberry Pi Security Camera Livestream

_Captured: 2017-10-27 at 18:54 from [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/raspberry-pi-security-camera-livestream-setup/)_

![Raspberry Pi Überwachungskamera Livestream](https://tutorials-raspberrypi.com/wp-content/uploads/2016/09/Raspberry-Pi-Überwachungskamera-Livestream.png)

After we are able to record individual images with (USB) cameras / webcams, we also want to view live pictures. This can either take place on the smartphone or on a PC fom outside of the home network. For this purpose, we configure the Livestream of the Raspberry Pi security camera. The great thing is that almost every USB camera (also webcams) can be used. Depending on placement, e.g. a camera without an infrared filter can be useful to enable better night shots.

## Equipment

![Raspberry Pi Überwachungskamera Livestream NoIR](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Überwachungskamera-Livestream-NoIR-180x120.jpg)

> _The missing IR filter ensures a higher light sensitivity._

If we want to connect a USB camera, our Raspberry Pi must obviously have a free USB port. However, we can also use the official camera, which is available in two versions:

  * Standardversion in green ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=raspberry+pi+camera+v2+-noir) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=raspberry+pi+camera+v2+-noir)), which has 8MP, and the like. Videos in 1080p can record. Since an infrared filter is installed, it is particularly suitable for daylight recording or for places with sufficient light irradiation.
  * NoIR Version in black ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=raspberry+pi+camera+v2+noir) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=raspberry+pi+camera+v2+noir)): The specifications (resolution, etc.) are the same, but no IR filter is installed, which makes records with bad light conditions better. This is especially recommended for dark scenes.

Both cameras can be directly connected via the CSI connector on board, which means that no USB port is used. The newer Zero models (from generation 2) now also have CSI ports.

Alternatively, any USB Webcam ([US](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=USB+Webcam) / [UK](https://www.amazon.co.uk/s/ref=nb_sb_noss/?tag=755-21&url=search-alias%3Daps&field-keywords=USB+Webcam)) can be used as long as the corresponding drivers for Linux are available. However, this is the case with almost all newer cameras. If our Raspberry Pi does not have an integrated [wifi adapter](https://www.amazon.com/s/ref=nb_sb_noss_2?tag=754u-20&url=search-alias%3Daps&field-keywords=wifi+dongle), we may need one more because a network or Internet connection is unavoidable.

## Preparations for the Livestream

Before we enable the stream of our Raspberry Pi camera or USB Webcam, we need to update the packages:
    
    
    sudo apt-get update
    sudo apt-get upgrade

Then you can install the [Motion](http://lavrsen.dk/foswiki/bin/view/Motion/WebHome) tool, which makes our Livestream possible.
    
    
    sudo apt-get install motion -y

The installation will take some time.

If everything has worked so far, the camera can be connected (if not already done). If you are using a USB webcam, you can check if it has been detected:
    
    
    lsusb

If no special drivers are required, all connected video devices / cameras should be displayed with the following command:
    
    
    ls /dev/video*

If you are using one of the official camera modules, it is important to do the following so that the camera is displayed immediately (preferably by autostart):
    
    
    sudo modprobe bcm2835-v4l2

If only a single webcam / Raspberry Pi camera is connected, by using `/dev/video0` the device should be specified. If you have several devices connected, you have to select the device to transfer the stream.

## Configure the Raspberry Pi Livestream

For the next steps, in which we set some settings, wee need to look at the camera details:
    
    
    v4l2-ctl -V

For my USB Webcam I got the following output. We will immediately specify the information for the resolution, etc. in the configuration file.
    
    
    pi@raspberrypi:~ $ v4l2-ctl -V
    Format Video Capture:
            Width/Height  : 640/480
            Pixel Format  : 'YUYV'
            Field         : None
            Bytes per Line: 1280
            Size Image    : 614400
            Colorspace    : SRGB
            Flags         :

So let's edit Motion's configuration file:
    
    
    sudo nano /etc/motion/motion.conf

The following lines have to be adjusted (the variable can be searched with CTRL + W, the bold values have been changed):
    
    
    # Start in daemon (background) mode and release terminal (default: off)
    **daemon on**
    ...
    # Restrict stream connections to localhost only (default: on)
    **stream_localhost off**
    ...
    # Target base directory for pictures and films
    # Recommended to use absolute path. (Default: current working directory)
    **target_dir /home/pi/Monitor**

The following lines are optimal and should also be changed (we have read them out previously):
    
    
    **v4l2_palette 15**     # Nummer aus der Tabelle davor entnehmen, 15 enstpricht YUYV
    ... 
    # Image width (pixels). Valid range: Camera dependent, default: 352 **
    width 640** 
    
    # Image height (pixels). Valid range: Camera dependent, default: 288 
    **height 480** # Maximum number of frames to be captured per second. 
    
    # Valid range: 2-100. Default: 100 (almost no limit). 
    **framerate 10 **

Save with CTRL + O and close with CTRL + X. Further options (port, etc.) can also be adjusted afterwards (requires a reboot). The brief description of the settings is however very revealing.

Now we only have to activate the daemon so that we can run the service afterwards:
    
    
    sudo nano /etc/default/motion

Here we replace "no" with "yes", after which it should look like the following text:
    
    
    start_motion_daemon=yes

Now we have to create the folder, which we have previously specified as the storage location for the captured frames, and give it the necessary writing rights:
    
    
    mkdir /home/pi/Monitor
    sudo chgrp motion /home/pi/Monitor
    chmod g+rwx /home/pi/Monitor

Then we can start the service:
    
    
    sudo service motion start

## Raspberry Pi Surveillance Camera Livestream Test

In order to test whether our camera is really sending live images, we basically have two options: One way is simply to use the browser (Mozilla Firefox, Chrome, etc.) and the name of the Raspberry Pi followed by the port (default: 8081). If you have not changed the hostname and port, you should be able to see the stream: <http://raspberrypi:8081/> (Alternatively, the local IP address can be used, such as 192.168.1.51:8081).

Some older browsers do not support this stream (Internet Explorer :-D). Those users may choose the Livestream e.g. on the [VLC Player](http://www.videolan.org/vlc/). To do this, simply open the VLC Player and specify in the menu under "Media" -> "Open Network Stream" (CTRL + N) the above address. This is also possible in the VLC Player for smartphones and tablets ([Android](https://play.google.com/store/apps/details?id=org.videolan.vlc), [Apple](https://itunes.apple.com/de/app/vlc-for-mobile/id650377962?mt=8)): Select "Open Media Address" in the menu and the IP address including port.

Depending on the specified Framerate (specified in the configuration file) the image is better or not. Of course, your camera must also support the framerate. If, for example, the camera can send a maximum of 10 frames per second, it does not matter if more are set in the configuration.

## Make it available outside the home network

Since it makes little sense to watch the camera in its own network, we also want to access it from outside. For this we need a fixed IP or a [dDNS service](https://en.wikipedia.org/wiki/Domain_Name_System). Most telecommunication providers provide fixed IP addresses (if at all) only for payment, which is why we want to use a free DNS provider. Of course you can also take another vendor of your choice. If you already have a fixed IP address at home, you can skip this step.

**Note**: Theoretically, you can also use a non-static IP address, but this has the disadvantage that after each reconnect you'll get a new IP address. Since Provider approximately once a day (usually at night) force a reconnect of your router, a DNS service is highly recommended, since the DNS address does not change.

In addition, we have to open the selected port (for example 8081) in our router for port forwarding. This means that we can address this port from outside the network and connect it to it. Since this is something different for each router, refer to the corresponding manual. Under the heading "Port forwarding" or similar, you can specify the port which is opened for a specific local IP address. In my router looks like this for example:

![Raspberry Pi NoIP PortForwarding](https://tutorials-raspberrypi.com/wp-content/uploads/2016/09/Raspberry-Pi-NoIP-PortForwarding.png)

The menu of most routers is accessible via 192.168.1.1 or 192.168.0.1 via the browser. If this is not the case, however, the manual will also tell you how to find the menu.

If you use the VLC Player, you must now of course replace the local IP address, which you have previously specified, with your DNS or static IP address (port is still the same). Some routers may fail to do this within the home network. To test it nevertheless at home, you can use mobile data on your phone for example. Turn wifi off and check if you can see the Livestream of the Raspberry Pi surveillance camera. Depending on the Internet connection (upload speed), the picture may be somewhat delayed.
