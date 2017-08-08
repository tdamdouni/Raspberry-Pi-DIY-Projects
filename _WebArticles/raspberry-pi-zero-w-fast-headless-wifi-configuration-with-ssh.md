# Raspberry Pi Zero W: fast headless Wifi configuration with SSH

_Captured: 2017-05-23 at 19:00 from [www.albertosarullo.com](http://www.albertosarullo.com/blog/raspberry-pi-zero-w-headless-wifi-ssh-configuration-10-minutes)_

Yesterday I received a **Raspberry Zero W**, that for approximately $10 include Wifi and Bluetooth (byebye dongles) but no Ethernet port.

This post contains the instructions for configuring the Raspberry Pi Zero W so that he connects to the wifi network at the first startup of Linux, without wasting time (after that, you can log on via SSH).

  1. Download Jessie Lite image from the [official repository](https://www.raspberrypi.org/downloads/raspbian/) (5 min)
  2. Download [Etcher](https://etcher.io/) and burn the image on SD card (5 min)
  3. Insert the SD card in your notebook and open the boot folder of the SD Card
  4. Create an (empty) file called **ssh** (this enable SSH on startup)
  5. Create a **wpa_supplicant.conf** file with the following content
    
    
    network={
        ssid="YOUR_WIFI_SSID"
        psk="YOUR_WIFI_PASSWORD"
        key_mgmt=WPA-PSK
    }

Insert the SD in your Raspberry Pi Zero W, attach the power USB, connect your computer to the wifi, scan the network to find the raspberry IP address …and you can connect via **SSH**

![](http://www.albertosarullo.com/blog/wp-content/uploads/2017/03/IMG_20170312_213708-1024x656.jpg)
