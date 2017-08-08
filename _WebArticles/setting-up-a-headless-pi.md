# Setting up a Headless Pi

_Captured: 2017-05-11 at 23:00 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/setting-up-a-headless-pi)_

This quick tutorial will show you how to set up a Raspberry Pi that's completely headless. That means that you won't need a display, keyboard, or mouse attached to your Pi to use it or even to set it up! If you're used to using a laptop or desktop computer at home, and don't want the hassle of connecting everything up to your Pi to use it, then this is the ideal solution.

You'll need a little familiarity with the terminal, as this is how you will connect to your Pi, using SSH. SSH stands for Secure Socket Shell, and is a remote way of accessing a terminal on another machine. If you've ever used one of our one-line-installers for our Pi HATs and pHATs, then you'll have used the terminal.

Because we're connecting remotely to the Pi, you'll need a Pi with Wi-Fi, such as the Pi Zero W or Pi 3 (or you could use a Wi-Fi dongle).

## Installing Raspbian Lite

We recommend using the very latest version of Raspbian **Lite**. We'd recommend using either the NOOBS installer, which you can find [here](https://www.raspberrypi.org/downloads/noobs/) (ensure that you select Raspbian Jessie **Lite** when installing), or downloading Jessie Lite from [here](https://www.raspberrypi.org/downloads/raspbian/) and then using the [Etcher](https://etcher.io/) tool to burn the image to your SD card.

This will work perfectly well on Raspbian Pixel, but it will take longer to burn the image to your SD card, and most of the extra stuff in Pixel is related to the GUI - the desktop, etc. - which you'll have no need for since you're using the terminal.

Once you've burned Raspbian Lite to your SD card, leave it in your computer since we'll be modifying the files before you even put the SD card into your Pi! Note that if you've used Etcher to burn your SD card it will have been ejected afterwards and you'll need to remove it and then replace it to get it to mount again.

## Setting up Wi-Fi

You'll notice that your SD card that is mounted on your computer is showing a single partition called `boot`. We'll be adding a couple of files straight into there that will allow your Pi to connect to your Wi-Fi and to enable SSH on it.

Create a new text file and call it `wpa_supplicant.conf`. It's extremely important that this file has that exact filename, and no extra extensions on the end like `.txt` that may be added by your text editor.

You'll need to know the SSID (the name) of the network to which you want to connect, for instance `MyWiFiNetwork` and the password or pre-shared key.

In your `wpa_supplicant.conf` file, enter the following:
    
    
    network={
        ssid="MyWiFiNetwork"
        psk="password123"
    }
    

Replace `MyWiFiNetwork` with the SSID of your Wi-Fi network, and `password123` with your password, making sure to keep the quotes, as above.

If you have more than one Wi-Fi network that you want to add, for instance home and work, then you can simply duplicate that whole block of text, change the SSID and PSK, and add it to the bottom of that file. Save the file.

Now, create a completely blank file with the filename `ssh`, ensuring that there's no extension. Save it in that same `boot` partition.

Eject the SD card from your computer, pop it into your Pi, and plug in the power.

## Connecting to your Pi

Assuming that all worked, your Pi should now be connected to your Wi-Fi and visible on your network. We're going to use SSH to connect to the Pi now.

Open a terminal on your Mac, Windows, or Linux computer. You can also use a client like Putty on Windows to connect.

As well as having an IP address assigned to it, your Pi will appear with the hostname `raspberrypi.local`. If you're not able to find the IP address of your Pi (you should be able to find it on your router admin page, or with a tool like Angry IP Scanner or Fing) then you can use the hostname instead. We'll do that here.

Type the following to SSH into your Pi:
    
    
    ssh pi@raspberrypi.local
    

Press enter, and then type `yes` when it prompts you as to whether you want to connect. When it asks for the password, type `raspberry`, the default password in Raspbian.

Assuming that was successful, you should land in a terminal that is running on your Pi! You can now do things like install software, program HATs and pHATs, etc, all without having a display, keyboard, or mouse attached to your Pi!

To shutdown your Pi, simply type `sudo shutdown -h now`, or press `control` and `d` if you want to disconnect but leave your Pi running.

Note that if you have a program running over SSH and you disconnect, then the program will likely stop as soon as you disconnect. The best way round this is to use `screen`, but we'll save that for another tutorial!
