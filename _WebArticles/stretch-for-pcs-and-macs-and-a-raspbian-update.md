# Stretch for PCs and Macs, and a Raspbian update

_Captured: 2018-01-06 at 13:46 from [www.raspberrypi.org](https://www.raspberrypi.org/blog/stretch-pcs-macs-raspbian-update/)_

Today, we are launching the first Debian Stretch release of the Raspberry Pi Desktop for PCs and Macs, and we're also releasing the latest version of Raspbian Stretch for your Pi.

![Raspberry Pi Desktop Stretch splash screen](https://www.raspberrypi.org/app/uploads/2017/11/splashd.png)

## For PCs and Macs

When we released our custom desktop environment on Debian for PCs and Macs [last year](https://www.raspberrypi.org/blog/pixel-pc-mac/), we were slightly taken aback by how popular it turned out to be. We really only created it as a result of one of those "Wouldn't it be cool if…" conversations we sometimes have in the office, so we were delighted by the Pi community's reaction.

Seeing how keen people were on the x86 version, we decided that we were going to try to keep releasing it alongside Raspbian, with the ultimate aim being to make simultaneous releases of both. This proved to be tricky, particularly with the move from the Jessie version of Debian to the Stretch version [this year](https://www.raspberrypi.org/blog/raspbian-stretch/). However, we have now finished the job of porting all the custom code in Raspbian Stretch to Debian, and so the first Debian Stretch release of the Raspberry Pi Desktop for your PC or Mac is available from today.

## The new Stretch releases

As with the Jessie release, you can either run this as a live image from a DVD, USB stick, or SD card or install it as the native operating system on the hard drive of an old laptop or desktop computer. Please note that installing this software will erase anything else on the hard drive -- do not install this over a machine running Windows or macOS that you still need to use for its original purpose! It is, however, safe to boot a live image on such a machine, since your hard drive will not be touched by this.

We're also pleased to announce that we are releasing the latest version of Raspbian Stretch for your Pi today. The Pi and PC versions are largely identical: as before, there are a few applications (such as Mathematica) which are exclusive to the Pi, but the user interface, desktop, and most applications will be exactly the same.

For Raspbian, this new release is mostly bug fixes and tweaks over the previous Stretch release, but there are one or two changes you might notice.

## File manager

The file manager included as part of the LXDE desktop (on which our desktop is based) is a program called PCManFM, and it's very feature-rich; there's not much you can't do in it. However, having used it for a few years, we felt that it was perhaps more complex than it needed to be -- the sheer number of menu options and choices made some common operations more awkward than they needed to be. So to try to make file management easier, we have implemented a cut-down mode for the file manager.

![Raspberry Pi Desktop Stretch - file manager](https://www.raspberrypi.org/app/uploads/2017/11/fm.png)

Most of the changes are to do with the menus. We've removed a lot of options that most people are unlikely to change, and moved some other options into the **Preferences** screen rather than the menus. The two most common settings people tend to change -- how icons are displayed and sorted -- are now options on the toolbar and in a top-level menu rather than hidden away in submenus.

The sidebar now only shows a single hierarchical view of the file system, and we've tidied the toolbar and updated the icons to make them match our house style. We've removed the option for a tabbed interface, and we've stomped a few bugs as well.

One final change was to make it possible to rename a file just by clicking on its icon to highlight it, and then clicking on its name. This is the way renaming works on both Windows and macOS, and it's always seemed slightly awkward that Unix desktop environments tend not to support it.

As with most of the other changes we've made to the desktop over the last few years, the intention is to make it simpler to use, and to ease the transition from non-Unix environments. But if you really don't like what we've done and long for the old file manager, just untick the box for **Display simplified user interface and menus** in the **Layout** page of **Preferences**, and everything will be back the way it was!

![Raspberry Pi Desktop Stretch - preferences GUI](https://www.raspberrypi.org/app/uploads/2017/11/fmpref.png)

> _Battery indicator for laptops_

One important feature missing from the previous release was an indication of the amount of battery life. Eben runs our desktop on his Mac, and he was becoming slightly irritated by having to keep rebooting into macOS just to check whether his battery was about to die -- so fixing this was a priority!

We've added a battery status icon to the taskbar; this shows current percentage charge, along with whether the battery is charging, discharging, or connected to the mains. When you hover over the icon with the mouse pointer, a tooltip with more details appears, including the time remaining if the battery can provide this information.

![Raspberry Pi Desktop Stretch - battery indicator](https://www.raspberrypi.org/app/uploads/2017/11/batt.png)

While this battery monitor is mainly intended for the PC version, it also supports the first-generation pi-top -- to see it, you'll only need to make sure that I2C is enabled in **Configuration**. A future release will support the new second-generation pi-top.

## New PC applications

We have included a couple of new applications in the PC version. One is called PiServer -- this allows you to set up an operating system, such as Raspbian, on the PC which can then be shared by a number of Pi clients networked to it. It is intended to make it easy for classrooms to have multiple Pis all running exactly the same software, and for the teacher to have control over how the software is installed and used. PiServer is quite a clever piece of software, and it'll be covered in more detail in another blog post in December.

We've also added an application which allows you to easily use the GPIO pins of a Pi Zero connected via USB to a PC in applications using Scratch or Python. This makes it possible to run the same physical computing projects on the PC as you do on a Pi! Again, we'll tell you more in a separate blog post this month.

Both of these applications are included as standard on the PC image, but not on the Raspbian image. You can run them on a Pi if you want -- both can be installed from apt.

## How to get the new versions

New images for both Raspbian and Debian versions are available from the [Downloads](https://www.raspberrypi.org/downloads/) page.

It is possible to update existing installations of both Raspbian and Debian versions. For Raspbian, this is easy: just open a terminal window and enter
    
    
    sudo apt-get update
    sudo apt-get dist-upgrade

It is slightly more complex for the PC version, as the previous release was based around Debian Jessie. You will need to edit the files **/etc/apt/sources.list** and **/etc/apt/sources.list.d/raspi.list**, using **sudo** to do so. In both files, change every occurrence of the word "jessie" to "stretch". When that's done, do the following:
    
    
    sudo apt-get update 
    sudo dpkg --force-depends -r libwebkitgtk-3.0-common
    sudo apt-get -f install
    sudo apt-get dist-upgrade
    sudo apt-get install python3-thonny
    sudo apt-get install sonic-pi=2.10.0~repack-rpt1+2
    sudo apt-get install piserver
    sudo apt-get install usbbootgui
    

At several points during the upgrade process, you will be asked if you want to keep the current version of a configuration file or to install the package maintainer's version. In every case, keep the existing version, which is the default option. The update may take an hour or so, depending on your network connection.

As with all software updates, there is the possibility that something may go wrong during the process, which could lead to your operating system becoming corrupted. Therefore, we always recommend making a backup first.

Enjoy the new versions, and do let us know any feedback you have in the comments or on the [forums](https://www.raspberrypi.org/forums/)!
