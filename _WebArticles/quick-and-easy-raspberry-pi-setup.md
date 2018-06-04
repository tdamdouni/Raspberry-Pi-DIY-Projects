# Quick and Easy Raspberry Pi Setup

_Captured: 2018-04-25 at 07:31 from [dzone.com](https://dzone.com/articles/quick-and-easy-raspberry-pi-setup?edition=375219&utm_source=Zone%20Newsletter&utm_medium=email&utm_campaign=iot%202018-04-24)_

So, you have a shiny new Raspberry Pi and you'd like to install Linux on it.

This is a short guide to help you get Raspbian installed and configured for Wi-Fi and SSH access. You should be able to follow this guide even if you don't connect a keyboard or monitor to your Pi.

**NOTE**: In order to complete all of the steps in this guide, you will need to be able to access and edit files in an ext4 filesystem. I will mark these steps with [ext4]. This may require additional steps and/or software for Windows systems.

First up, you will need to download a couple files.

  * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)  
I usually download the image from raspberrypi.org. There are two images available. The _desktop image_ comes with a GUI front end and a few pre-installed applications. The _lite image_ is a 'headless' install, meaning you will boot to a command prompt and there is no GUI desktop installed. This guide will work for either version, pick whichever version you want.
  * [Etcher](https://etcher.io/)  
Using Etcher makes it easy to flash an image to your SD card.

## Put the SD Card in Your Computer

For the next few steps, keep the SD Card in your computer. You will not put the card in your Pi until we get to the "Boot Your Pi" section below.

### Flash Raspbian to the SD Card

Run Etcher:

  1. Choose the Raspbian ZIP file you downloaded above.
  2. Select your SD card from the list. **WARNING**: Etcher does its best to make sure it only shows SD cards in the list, but you should always make sure it's the card you want to install to -- the selected drive will be formatted!
  3. Click Flash.

If you open your favorite file explorer, you should now see two new drives listed.

  * boot
  * rootfs [ext4]

### Enable SSH Access

  1. Change into boot. (Modify the 'cd' command below to match the path to boot on your system.)
  2. Create an empty file called 'ssh'.

That's it. The first time you boot your Pi, ssh will automatically be enabled. (Don't boot it up yet.)

### Connect Without a Password

Having to type a password everytime you SSH or SCP to your Pi gets old after a while. If you don't mind typing the password every time, you can skip this step. Otherwise...

Add your public key to your Pi [ext4]:

  1. Locate the ssh public key you want to use (example ~/.ssh/id_rsa.pub). If you don't already have one, you can follow the steps in [this guide](https://git-scm.com/book/be/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key).
  2. Change into the Pi home on rootfs. (Modify the 'cd' command below to match the path to rootfs on your system.)
  3. Create the .ssh directory.
  4. Append your public key to the authorized_keys file. (You can repeat this step to append as many keys as you need for the different systems you intend to use.)

If you're not able to access the ext4 partition from your operating system, you can follow [this guide on raspberrypi.org](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md) after you boot up the Pi.

### Enable Wi-Fi [ext4]

  1. Change into rootfs/etc/wpa_supplicant.
  2. Edit wpa_supplicant.conf. (You may need sudo to edit this file.)
  3. Append the following to the end of the file. Replace "Your SSID" and "Your WPA Password" with the values to connect to your Wi-Fi.

  


  4. Save the file.

If you're not able to access the ext4 partition from your operating system, you can follow these instructions after you boot up the Pi with the following changes.

  1. Connect a keyboard and monitor to your Pi.
  2. Change into /etc/wpa_supplicant.
  3. Continue with step 2 above.

Now it's time to...

## Boot Your Pi

Put the SD card in your Pi and boot it up.

If you're not connecting your Pi to a display, you should be able to get its IP address from your Wi-Fi Router admin page.

  1. Connect with ssh.
  2. Change the default Pi user password. (default password: _raspberry_). Even though we set up access using a public key, the Pi can still be accessed with a password, so it's a good idea to set a new password.
  3. Run an update.

## Do Something Fun

At this point, you have a little Linux machine all set up and ready to use for your projects. Go do something fun with it.

If there are other configurations you'd like me to add to the guide, please leave a comment.
