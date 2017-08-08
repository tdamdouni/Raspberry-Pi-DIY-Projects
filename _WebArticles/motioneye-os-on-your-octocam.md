# motionEye OS on your OctoCam

_Captured: 2017-05-11 at 22:56 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/motioneye-os-on-your-octocam)_

The motionEye OS software makes it possible to set your OctoCam up as a motion-triggered security camera that will capture images and videos and let you view them on another computer, tablet, or phone on your local network.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-large.jpg)

> _It also has a bunch of advanced features like fast network video streaming, webhooks to integrate with services like IFTTT, and Dropbox and Google Drive integration to allow you to upload images and video to the cloud._

We'll see here how to install motionEye OS on your SD card, how to set Wi-Fi up, and how to do some basic configuration including how to set up schedules and how to enable fast network streaming.

If you haven't already built your OctoCam, then check out our [Assembling OctoCam tutorial](https://learn.pimoroni.com/tutorial/sandyj/assembling-octocam) for tips on how to put it all together.

## Burning motionEye OS to a micro-SD card

motionEye OS is a complete operating system for your Pi, and you burn it to a micro-SD card the same way that you would with Raspbian. Because of the potentially large amount of images and video being stored, it's a good idea to use a decent-sized micro-SD card, at least 16GB if not 64GB.

We like to use the [Etcher](https://etcher.io/) tool to burn images to our SD card, as it works well, is cross-platform, and will check the integrity of the burnt image after burning.

Download the [latest motionEye OS image](https://github.com/ccrisan/motioneyeos/releases), making sure that you select the one that begins `motioneyeos-raspberrypi-xxxxxxxx.img.gz`, rather than either of the images for the Raspberry Pis 2 and 3.

Pop your SD card into your computer and open Etcher. Select the downloaded image file; there's no need to unzip the gzipped file as Etcher will do this on the fly for you. Select your SD card, although if you only have one mounted then it should be selected automatically by Etcher. Burn the image.

Once the image is burned, the SD card will be unmounted automatically by Etcher and you need it mounted again for the next part, so pop it out and back in again to mount it.

## Setting up Wi-Fi

Don't put the SD card into your Pi just yet. First, we'll configure the Wi-Fi so that your Pi Zero W will connect to your network as soon as it boots for the first time.

You'll need to know the SSID and the password for the Wi-Fi network to which you'd like to connect. The SSID is the Wi-Fi network name, and you'll be able to find it by looking at your phone/tablet/laptop's network settings and looking at the name of the network to which you're connected

Open a new text document on your computer with the SD card mounted. It's very important that this is a plain text document and not rich text or some other format. We'd recommend using a text editor like [Sublime Text](https://www.sublimetext.com/3) or [Atom](https://atom.io/) to create this file, as they should both give you the option of saving as plain text.

In that new file, place the following:
    
    
    update_config=1
    ctrl_interface=/var/run/wpa_supplicant
    
    network={
        scan_ssid=1
        ssid="MyWiFiNetwork"
        psk="password123"
    }
    

Replace `MyWiFiNetwork` with the SSID of your Wi-Fi network, and `password123` with your password, making sure to keep the quotes, as above.

Now save that file with the filename `wpa_supplicant.conf` in the boot partition of your SD card. The SD card should be mounted as a drive called `boot`; drop the file straight in there. Make sure that your file doesn't have any extensions on the end of the filename like `.txt`, it should just be called `wpa_supplicant.conf`.

If you want to enable SSH for debugging purposes, then you'll need to create a completely blank file called `ssh` and drop it into the boot partition where you put the `wpa_supplicant.conf` file. This will enable SSH when your Pi boots for the first time.

## Booting for the first time

Safely unmount/eject the SD card from your computer and pop it into the SD card slot on your Pi Zero W, and then plug in the power supply. If you have a display connected, then you should see a bunch of text appear as your Pi boots.

Booting for the first time will take a few minutes to get everything set up. If you're doing this headless, i.e. without a monitor and keyboard connected, then wait for a good 5 minutes or so before proceeding.

Because we provided the credentials for the Wi-Fi network, your Pi should have connected to it. You can use an app like Fing to check that it is connected and to find its IP address. Open a browser on your computer (or tablet, or phone), and type `http://192.168.0.161`, for example, replacing that IP address with the IP address of _your_ OctoCam, into the address bar.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-1.jpeg)

All being well, you should see a page like the one above, showing the view from your OctoCam! We'll log in as the administrator so that we can tweak the settings. Click on the icon that looks like a little person at the top left corner of the menubar to log in. The username is `admin` and the password is blank by default. Click `Login`.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-2.jpeg)

> _To take the camera full screen at any time, click on the camera image and then on the square icon to go full screen. Press Esc to exit full screen again._

The photograph and play symbol icons let you access any captured images and video respectively, and the spanner lets you change the settings for your camera.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-9.jpeg)

## Changing settings

We'll go through some of the more important/relevant settings now. Click on the hamburger menu at the top left corner to pop out the settings menu.

The first thing that you should do is to change the `Admin Password` and `Surveillance Password`, i.e. add them! Also click the toggle switch next to `Advanced Settings` to get access to all of the advanced settings.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-4.jpeg)

Once you've changed any settings, click the orange `Apply` button at the top, but note that it may need to reboot to apply the changes, so if you have a bunch of settings that you need to change then wait until you've done them all before clicking `Apply`.

You may want to change the video settings from the default, which is fairly low resolution. In our testing, 1280x720 at about 10 frames per second gives you a decent balance between quality and performance.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-5.jpeg)

If you just want to set your OctoCam up as a streaming video camera, without any of the motion-activated capture of images and video, then you can enable the `Fast Network Camera` option. This will stream video at a surprisingly high frame rate and barely any lag, but disables all of the motion-activated capture features. We found that 1280x720 at 20 frames per second, and 25% image quality gave really good performance, but your mileage may vary depending on your network speed and load.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-6.jpeg)

If you _are_ using motion detection, then there are a bunch of settings you can change to alter the sensitivity, etc, but we found that the default settings worked well in an indoor setting, capturing movement of people.

The last relevant settings section is the `Working Schedule`. This allows you to schedule when the video and image capture triggered by motion is active. For instance, you might want it only to be active during the day, while you're out of the house at work. Or, if you're using the IR version of our [Zero camera](https://shop.pimoroni.com/products/raspberry-pi-zero-camera-module), then you might want it only to be active during the night.

![](https://learn.pimoroni.com/static/repos/learn/sandyj/motioneye-os-on-your-octocam-8.jpeg)

> _You'll also find Software Update , Shut Down , and Reboot options in the General Settings section._

## Taking it further

As we mentioned, OctoCam works really well with the IR version of our [Zero camera](https://shop.pimoroni.com/products/raspberry-pi-zero-camera-module), so you could use it in combination with an IR light source to turn OctoCam into a night vision camera.

motionEye OS also allows you to add multiple cameras, so you could have an OctoCam in your living room, and another set up as a baby monitor, for example.

You can also trigger scripts to run, or send webhooks to services like Slack or IFTTT, and even sync your images and video to Dropbox or Google Drive (look in the `File Storage` section of the settings menu). Explore the settings in depth to discover all of the bells and whistles that motionEye OS has.
