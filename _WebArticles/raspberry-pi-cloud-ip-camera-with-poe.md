# Raspberry Pi Cloud IP Camera With POE

_Captured: 2017-05-06 at 16:11 from [www.instructables.com](http://www.instructables.com/id/Raspberry-Pi-Cloud-IP-Camera-with-POE/)_

![Raspberry Pi Cloud IP Camera With POE](https://cdn.instructables.com/FKV/8MCO/IE2NDAYA/FKV8MCOIE2NDAYA.MEDIUM.jpg?width=614)

![DSC_0095_white_bg_cp.jpg](https://cdn.instructables.com/F6G/5DMK/IE2NDBPZ/F6G5DMKIE2NDBPZ.LARGE.jpg)

![DSC_0085.jpg](https://cdn.instructables.com/F2M/7X77/IE17X2SN/F2M7X77IE17X2SN.LARGE.jpg)

I was inspired by scavix's work with the instructable [Raspberry Pi as low-cost HD surveillance camera](https://www.instructables.com/id/Raspberry-Pi-as-low-cost-HD-surveillance-camera/) so I decided to make my own Raspberry PI based IP camera that also features POE and supports integration with the [Google Drive](https://www.google.com/drive/).

The video streaming can be simply viewed from a web browser. Most desktop browsers should work, I have also tested with Firefox for Android and it seems to work fine. It is also possible to view the video stream from multiple cameras the same time by making a simple HTML file, but more about that later.

The camera footage is saved in the form of JPEG images instead of video files in order to make the uploading to the Google Drive easier for Internet connections with low upload speeds. To prevent Google Drive from running out of space, every one hour the system checks for any images that are older from a specific threshold (e.g. 2 days) and automatically deletes them. After that it syncs the local footage directory with the Google Drive.

All the partitions on the microSD are read-only to prevent corruption from power failures. An external USB drive is also used to keep the _/var_ and _/home_ partitions which they both need to be read-write. That way the system is unlikely to become unbootable from a power failure since the microSD is 100% read-only.

I built two of those IP cameras a while ago and they have been tested on production environment (a small retail store) for more than a year and they have shown absolutely no issues. Since the day they have been installed both cameras have 100% uptime. So I'm pretty confident that they can be used as low cost alternative to commercial IP cameras in a small business.

## Step 1: Tools and Parts

![Tools and Parts](https://cdn.instructables.com/FS4/DNME/IE17X2OC/FS4DNMEIE17X2OC.MEDIUM.jpg?width=614)

![DSC_0054.jpg](https://cdn.instructables.com/FT8/3B1B/IE17X2M6/FT83B1BIE17X2M6.LARGE.jpg)

![DSC_0056.jpg](https://cdn.instructables.com/FKN/EL75/IE17X2MB/FKNEL75IE17X2MB.LARGE.jpg)

![DSC_0045.jpg](https://cdn.instructables.com/FC1/F5IL/IE17X2FM/FC1F5ILIE17X2FM.LARGE.jpg)

![DSC_0033_01.jpg](https://cdn.instructables.com/FVP/YZF7/IE17X2FA/FVPYZF7IE17X2FA.LARGE.jpg)

**To build the camera you will need the following parts:**

  * A **Raspberry Pi Model B+**_[30€]_ \- It will also work with a Model B but it won't fit in the housing I used. I haven't tested it with a Raspberry Pi 2 but I think it should work.
  * A **Raspberry Pi Camera Module**_[30€]_ \- Plus at least two screws that fit its mounting holes.
  * An 8GB Class10 **MicroSD**_[5€]_ \- I used a [Kingston SDC10](http://www.kingston.com/us/support/technical/products?model=SDC10). A larger capacity MicroSD can also be used but it won't make a big difference.
  * A Low-profile **USB Flash Drive** at least 8GB _[6€]_ \- I used an 8GB [SanDisk Cruzer Fit CZ33](http://www.sandisk.com/products/usb/drives/cruzer-fit/).
  * A [TP-LINK TL-POE10R](http://www.tp-link.com/en/products/details/cat-4794_TL-POE10R.html)**POE Splitter**_[16€]_ \- You can use any POE Splitter that supports the 802.3af POE standard but this particular one fits perfectly inside the housing I used.
  * A **POE Injector** (or a POE Switch) - This is not part of the camera itself but you will need it to power the camera. I used a[ TP-LINK TL-SF1008P](http://www.tp-link.com/en/products/details/cat-42_TL-SF1008P.html) POE Switch _[40€]_ since I have more that one IP camera (it supports up to four), but for just one camera I recommend the [TP-LINK TL-POE150S](http://www.tp-link.com/en/products/details/cat-4794_TL-POE150S.html) POE Injector _[25€]_. If you can't find either of those, any injector or switch that supports the 802.3af POE standard should work. 
  * 1 x **Dummy IP Camera** for the housing _[9€]_ \- I highly recommend getting the [same](https://cdn.instructables.com/FVP/YZF7/IE17X2FA/FVPYZF7IE17X2FA.LARGE.jpg) with me because all the hardware fits perfectly inside. You can find it fairly easily if you search on ebay for "dummy ip ir camera" (you can find it in either silver or black color).
  * 2 x **RJ45 jacks** plus a small piece of **UTP cable** (Cat5e or Cat6) _[less than 1€]_
  * 2 x Female to Female **Jumper Wires **_[less than 1€]_
  * 1 x Hot Glue Stick
  * Solder Wire and Solder Wick

**And the following tools:**

  * A Soldering Iron
  * A Hot Glue Gun
  * A Desoldering Pump - Optional if you have solder wick.
  * A Dremel with a disk that can cut plastic plus drill bits
  * An RJ45 Crimping Tool

_The total cost of the camera parts (excluding the POE Injector/Switch and the tools) is around 100€. The prices can vary depending where you live and from where you bought them._

## Step 2: Preparing the MicroSD

**Burning the Installer Image to the microSD:**

As base for the system I decided to use a bare minimum Raspbian install and on top of it install only the required packages. That way the system is going to be more secure, more stable and there will be no waste of resources for things that are not required.

To get started first download the Raspbian NetInstall image from [Github](https://github.com/debian-pi/raspbian-ua-netinst/releases)and burn it to your microSD.

If you are using Linux just download the latest **raspbian-ua-netinst-<latest-version-number>.img.xz** file and use the following command:
    
    
    xzcat /path/to/raspbian-ua-netinst-<latest-version-number>.img.xz > /dev/sdX

Where **X** is the letter of the device that corresponds to your microSD e.g. **c**. Before running the command make sure that there are no mounted partitions that belong to the microSD. In case there are use the following command to unmount each one of them:
    
    
    umount /dev/sdXY

In case you got a permission denied error try the following command:
    
    
    xzcat /path/to/raspbian-ua-netinst-<latest-version-number>.img.xz | sudo tee /dev/sdX > /dev/null

But be extremely carefully here, using the wrong letter in place of **X** may do irreversible damage to your system and ruin your day. Before running the command double check that the letter you typed in place of **X** is really the one that corresponds to the microSD.

If you are using Windows download the **raspbian-ua-netinst-<latest-version-number>.zip** file instead. Format then your microSD as **FAT32** and extract the installer files in it.

**Installing the System:**

When the installer is finally written to the microSD it's time to install the system. The installation process is completely automated and non-interactive, the only thing you need to do is to insert the microSD to your Raspberry Pi, plug it in to your router using an Ethernet cable, connect the camera module, plug the power cable and it will automatically start to download and install the packages. The installation process takes around 45 to 60 minutes depending on the speed of your Internet connection. If you have an HDMI cable and a monitor you can keep an eye to the installation process. If you don't have a display attached you can monitor the Ethernet controller LEDs to guess activity.

![Assembling the Camera](https://cdn.instructables.com/FQ7/GS5F/IE17X2HP/FQ7GS5FIE17X2HP.MEDIUM.jpg?width=614)
