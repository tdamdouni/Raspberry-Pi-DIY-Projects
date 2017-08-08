# Run Skype on Raspberry Pi

_Captured: 2017-07-31 at 22:18 from [dzone.com](https://dzone.com/articles/run-skype-on-raspberry-pi)_

Skype is available on many platforms, but not on Raspberry Pi (or ARM-based Chromebooks). In this post, we will tell you how to run Skype on Raspberry Pi 2 and Raspberry Pi 3 using [ExaGear Desktop](https://eltechs.com/product/exagear-desktop/), which allows us to run x86 apps on ARM mini PCs.

We had a lot of requests about running Skype with ExaGear, but could not publish a corresponding instruction earlier. The thing is that for playing sound, Skype uses PulseAudio sound server, which was not stable on Raspberry Pi. Fortunately, starting with Raspbian (launched in May 2016), things have become better. Below, we give some hints how to configure PulseAudio and run Skype on your RPi 2 or RPi 3.

PS: Keep in mind that with ExaGear Desktop, you can use not only Skype but other chat (i.e. Telegram), music (i.e. Spotify), productivity (i.e. Dropbox), and many other apps on your Raspberry Pi.

## Raspberry Pi Test Stand Configuration

**Model**

Raspberry Pi 2 Model B

Raspberry Pi 3

**Frequency**

1000 MHz

1200 MHz

**Memory**

1 GB RAM

1 GB RAM

O**perating System**

Raspbian Jessie from Jan 2017

Raspbian Jessie from Jan 2017

**Software**

Skype for Linux v4.3.0.37

Eltechs ExaGear Desktop for Raspberry Pi 2

Skype for Linux v4.3.0.37

Eltechs ExaGear Desktop for Raspberry Pi 3

Now, here's how you can install Skype on your Raspberry Pi.

## 1\. Configure Host Raspbian System

**Configure PulseAudio**. As described in [release notes of Raspbian](https://www.raspberrypi.org/blog/another-update-raspbian/), remove the volumealsa plugin from the taskbar. Just right-click anywhere on the taskbar, choose **_Add/Remove Panel Items_**, and remove the **_Volume Control (ALSA)_** item from the list.

![Raspbian-Task-Bar-Add-Remove-Panel-Items-700x467](https://eltechs.com/wp-content/uploads/2017/02/Raspbian-Task-Bar-Add-Remove-Panel-Items-700x467.png)

![Raspbian Panel Applets - Volume Control \(ALSA\)](https://eltechs.com/wp-content/uploads/2017/02/Raspbian-Volume-Control-ALSA-700x467.png)

**Reboot the system** to apply PuleAudio configuration changes.

**Please note that you should set your Raspberry Pi 2 device overclocked in order to achieve good quality Skype voice calls**. Open Terminal (command line) and execute `$ sudo raspi-config`.

**Select Overclock section and then Pi2** (1000 MHz).

## 2\. Install ExaGear Desktop

**Download ExaGear Desktop archive** with installation packages and license key. Unpack downloaded archive using the following command in Terminal: `$ tar -xvzpf exagear-desktop-rpi3.tar.gz`.

Install and activate ExaGear on your ARM device by running `install-exagear.sh` script in a directory with deb packages and one license key: `$ sudo ./install-exagear.sh`.

## 3\. Launch Guest x86 System

Enter the guest x86 system using `$ exagear`.

Now you are in the x86 environment that can be checked by running `$ arch`.

It is recommended to update `apt-get` repositories on the first launch of the guest system: `$ sudo apt.get` update.

## 4\. Install Skype

Download Skype for Debian: `$ sudo apt-get install wget`.

Install Skype: `$ sudo dpkg -i skype-debian_4.3.0.37-1_i386.deb; sudo apt-get install -f`.

### Run Skype

Run Skype from Raspbian Start menu.

![Run Skype on Raspberry Pi using ExaGear Desktop](https://eltechs.com/wp-content/uploads/2017/02/Run-Skype-on-Raspberry-Pi-using-ExaGear-Desktop-700x467.png)

> _Check that Skype Sound Devices use PulseAudio server._

![Skype Options - Sound Devices](https://eltechs.com/wp-content/uploads/2017/02/Skype-options-Sound-Devices-700x388.png)

> _This is it. Now you can make your Skype calls._

## Final Notes

It is also worth noting that with ExaGear Desktop, you can run other x86 apps on Raspberry Pi 2 and Raspberry Pi 3. ExaGear also supports other ARM-based devices such as Odroid, Banana Pi, Beagleboard, Cubox, Jetson, Cubieboard, etc.

Please note that running Skype on Raspberry Pi 1 and Raspberry Pi Zero is not possible because of lack of NEON support in the hardware of these devices.
