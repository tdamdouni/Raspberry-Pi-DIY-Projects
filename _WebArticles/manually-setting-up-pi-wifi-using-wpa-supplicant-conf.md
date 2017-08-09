# Manually setting up Pi WiFi using wpa_supplicant.conf

_Captured: 2017-05-18 at 00:20 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/)_

![Pi Zero W WiFi Configuration](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2017/04/pi_zero_w_wifi-1078x516.jpg)

Although you can configure WiFi using the graphical utility within the Raspbian Desktop this requires that you connect a keyboard, mouse and monitor to your Pi. It is sometimes useful to be able to do it before you've booted the Pi. This is especially useful when using the Pi Zero W where attaching a keyboard and mouse requires a USB hub.

The following technique will allow you to take a fresh SD card, configure your WiFi settings and boot a Pi Zero without any other wires than a power cable. It should work for both the Pi Zero and Pi Zero W but it's easier on the W as you don't need to worry about a WiFi dongle.

## Step 1 - Create a blank text file

Create a blank text file named "wpa_supplicant.conf". Use a plain text editor rather than a Word Processor.

If using Windows you need to make sure the text file uses Linux/Unix style line breaks. I use Notepad++ (it's free!) and this is easy to do using "Edit" > "EOL Conversion" > "UNIX/OSX Format". "UNIX" is then shown in the status bar.

Insert the following content into the text file :
    
    
    country=us
    update_config=1
    ctrl_interface=/var/run/wpa_supplicant
    
    network={
     scan_ssid=1
     ssid="MyNetworkSSID"
     psk="Pa55w0rd1234"
    }

Double check the SSID and password. Both the SSID and password should be surrounded by quotes.

The Country Code should be set the [ISO/IEC alpha2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) for the country in which you are using your Pi. Common codes include :

  * GB (United Kingdom)
  * FR (France)
  * DE (Germany)
  * US (United States)
  * SE (Sweden)

## Step 2 - Copy to SD Card

Copy the file to the boot partition on your SD card. In Windows this is the only partition you will be able to see. It will already contain the following files :

  * bootcode.bin
  * loader.bin
  * start.elf
  * kernel.img
  * cmdline.txt

## Step 3 - Eject, Insert and Boot

Safely remove the SD card from your PC and insert into the Pi. Power up the Pi and once it has booted you should be connected to your WiFi network.

You may be able to use your Router admin interface to list connected devices. Your Pi should appear in the list with an assigned IP address.

## Additional Thougths

As Sebastian Bjurbom points out in the comments below you might want to take this opportunity to enable SSH as well. It is disabled by default but it is easy to enable by copying a blank text file named "ssh" to the boot partition. This can be done at the same time "wpa_supplicant.conf" is copied across.

## Troubleshooting

If after waiting a few minutes your Pi is not connected to your WiFi consider the following points :

  * Check wpa_supplicant.conf exists in the boot partition and the filename is correctly spelt
  * Check the file contains the text listed above
  * Double check every character in the SSID
  * Double check every character the password
  * Check the SSID and password are correctly surrounded with double quotes "…."
  * Ensure your text editor is using Linux style line breaks
