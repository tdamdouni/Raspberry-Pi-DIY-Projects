# How to Upgrade to a Raspberry Pi 3

_Captured: 2016-03-16 at 22:30 from [www.makeuseof.com](http://www.makeuseof.com/tag/upgrade-raspberry-pi-3/)_

![How to Upgrade to a Raspberry Pi 3](http://cdn.makeuseof.com/wp-content/uploads/2016/03/raspberry-pi-3-644x373.jpg?187746)

> _[Raspberry Pi 3 - the latest, most powerful version](http://www.makeuseof.com/tag/raspberry-pi-3-faster-better-wi-fi-bluetooth/)_

You've just received a brand new of the popular mini-computer that has taken the "maker" world by storm. If this is your first Pi, then you'll need to get a copy of the Raspbian OS installed. But if this is just the latest in a long line of Pis, you might prefer to upgrade your existing install, which is almost as simple as transferring the microSD card from your older Pi into the new model and booting.

_Almost_ as simple, but not quite. Let's take a look at what you actually need to do.

## Install an Operating System on the Raspberry Pi 3

You have three options for installing an operating system - typically Raspbian - on the Raspberry Pi 3.

The first is to download and [install Raspbian](http://www.makeuseof.com/tag/install-operating-system-raspberry-pi/).

For a simple alternative, the [NOOBs installer](http://www.makeuseof.com/tag/how-noobs-for-raspberry-pi-can-help-first-time-users/) presents a list of available operating systems, from Raspbian and OpenElec to Arch Linux, and makes their installation far simpler.

If you own a Raspberry Pi already, meanwhile, you can upgrade the existing operating system with a simple command. Once this is done, you will be able to take advantage of some of the new features, such as built in Bluetooth and wireless networking, as well as OpenGL 3D support.

## Upgrade Your MicroSD for Raspberry Pi 3

To get started, ensure that your microSD card is still in your OLD [Raspberry Pi B+](http://www.makeuseof.com/tag/the-raspberry-pi-b-is-here-whats-changed/) or [Raspberry Pi 2](http://www.makeuseof.com/tag/5-things-raspberry-pi-2-can-do/). With it powered on, and [connected via SSH ](http://www.makeuseof.com/tag/setting-raspberry-pi-headless-ssh/)or with a mouse and keyboard, open a terminal and enter
    
    
    sudo apt-get update

This refreshes the package list. Next, upgrade the operating system with
    
    
    sudo apt-get dist-upgrade

![muo-diy-rpi3-dist-upgrade](http://cdn.makeuseof.com/wp-content/uploads/2016/03/muo-diy-rpi3-dist-upgrade.png?187746)

Follow the instructions, agreeing to install the upgrade, and when this is done, reboot your Pi to apply the changes with
    
    
    sudo shutdown -r now

Once the Pi has rebooted, shutdown safely with
    
    
    sudo shutdown -h now

Now that you older Pi has been switched off, it is safe to switch the microSD card out from the old Pi and into the new Raspberry Pi 3.

## Enable OpenGL Acceleration

One addition to the Raspberry Pi 2 and 3 which is likely to prove a massive hit with hobbyist game developers is the addition of OpenGL 3D support. Note that once enabled, this will prevent you switching your microSD card into a Model A+, B+ or [Raspberry Pi Zero](http://www.makeuseof.com/tag/getting-started-raspberry-pi-zero/) due to the RAM requirements (Raspbian will fail to boot on any device with less than 1GB RAM once this is installed).

Note also that OpenGL support is currently experimental. To take a look, install the driver:
    
    
    sudo apt-get update && sudo apt-get install xcompmgr libgl1-mesa-dri

## Getting Your Raspberry Pi 3 Online, Wirelessly

Perhaps the biggest draw for the Raspberry Pi 3 is the inclusion of wireless networking and Bluetooth technology. This means that you no longer have to plug in USB dongles to gain access to Wi-Fi and connect Bluetooth hardware.

You have two ways to get online. The first, naturally, is via the desktop GUI, which can be accessed either with a mouse and keyboard, or [via VNC](http://www.makeuseof.com/tag/run-remote-desktop-raspberry-pi-vnc/). Simply find the network icon in the top-right corner (near the clock) and select the network name, or SSID, that you wish to connect to.

![muo-diy-rpi3-dongles](http://cdn.makeuseof.com/wp-content/uploads/2016/03/muo-diy-rpi3-dongles.jpg?187746)

When prompted, enter the passkey, and click **OK.** You should shortly join the network.

To set up access to a wireless network via the command line, you'll need to begin with the following command:
    
    
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

![muo-diy-rpi3-wireless-settings](http://cdn.makeuseof.com/wp-content/uploads/2016/03/muo-diy-rpi3-wireless-settings.png?187746)

This opens the **wpa_supplicant.conf** configuration file in the nano text editor. From here, use the arrow keys to move to the end of the file and enter the following, substituting your network's SSID and passkey where indicated:
    
    
    network={
    
    ssid="SSID"
    
    psk="PASSKEY"
    
    key_mgmt=WPA-PSK
    
    }

Press **CTRL+X, then Y** to save and exit, and wait a few moments for the Pi to establish the connection to the wireless network.

![muo-diy-rpi3-wlan0](http://cdn.makeuseof.com/wp-content/uploads/2016/03/muo-diy-rpi3-wlan0-640x211.png?187746)

Confirm connection by running the **ifconfig wlan0** command. You should see an IP address on your local network. If you had the Ethernet cable connected, you can now disconnect it, but you'll needs to login remotely again if you were using SSH.

## Install Bluetooth Support

With wireless networking setup, you may like to get Bluetooth up and running too. To install Bluetooth drivers, all you need is a single command:
    
    
    sudo apt-get install pi-bluetooth

![muo-diy-rpi3-bluez](http://cdn.makeuseof.com/wp-content/uploads/2016/03/muo-diy-rpi3-bluez.png?187746)

Various Raspberry Pi projects utilize Bluetooth, such as the Pi Beacon which is capable of _Minority Report_-style [personalized advertising and notices](http://www.makeuseof.com/tag/build-diy-ibeacon-raspberry-pi/), or an [auto-locking office door](http://www.makeuseof.com/tag/auto-locking-office-door-smartphone-proximity-sensor/).

## How the Raspberry Pi 3 Impacts Your Projects

You now have a Raspberry Pi 3 with four USB ports available, wireless networking, Bluetooth and optional OpenGL! Your projects have been considerably upgraded. But just how does this new device impact existing - and future - projects.

Well for a start off, the Raspberry Pi 3 features a BCM2837 SoC, which uses the 64-bit ARMv8 architecture. For the time being, Raspbian will continue to be developed as a 32-bit operating system (the Raspberry Pi Foundation's [Eben Upton](http://www.makeuseof.com/tag/raspberry-pi-featureinterview/) says he is waiting to be convinced about developing as a 64-bit OS), but the potential for a more powerful Raspberry Pi experience is there.

For young and amateur coders who have embraced the Raspberry Pi for homebrew game development, the fact that the main CPU is now capable of keeping up with the already-powerful GPU means that we're going to see more complex games developed for the platform. If you're into emulation (such as with the RetroPie system) this means that emulating consoles should be smoother, and improves the potential for emulating newer consoles.

![muo-diy-rpi3-pcb](http://cdn.makeuseof.com/wp-content/uploads/2016/03/muo-diy-rpi3-pcb.jpg?187746)

Finally, there's also the huge benefit that the built-in wireless connectivity delivers. First off, you have all four USB slots now freed up, allowing you to all-but-abandon your USB hub. Into these (or via the GPIO pins) you can connect sensors cameras, turning your Raspberry Pi 3 into an Internet of Things wireless sensor device.

The possibilities on offer with the Raspberry Pi 3 are superb, but before you get started with any new projects or upgrade previous efforts, make sure you have upgraded correctly, setup wireless networking, and installed Bluetooth support.

**Do you have a Raspberry Pi 3? What have you done with it so far? Are you planning to upgrade? Tell us about it in the comments.**

Image Credits:[Raspberry](http://www.shutterstock.com/pic.mhtml?id=216916480) by Tim UR via Shutterstock
