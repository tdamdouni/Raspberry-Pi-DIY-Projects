# How to Update Raspbian: All you need to know!

_Captured: 2017-11-07 at 21:55 from [pimylifeup.com](https://pimylifeup.com/update-raspbian/)_

![How to update Raspbian](https://cdn.pimylifeup.com/wp-content/uploads/2017/08/Updating-Raspbian.jpg)

> _In this guide we will be showing you how to update Raspbian to newer versions of the operating system without having to start off with a new totally clean image._

For the most part upgrading is a fairly simple process but be prepared to deal with some broken packages. Also make sure that any packages you are using now haven't changed radically in some of the newer versions of Raspbian.

Alongside showing you how to update to a newer version of Raspbian we will also be showing you how to simply update packages and give a simplified explanation on how the update, upgrade and dist-upgrade commands actually work.

Afterwards we will show you how to update [Raspbian Wheezy to Jessie](https://pimylifeup.com/update-raspbian/). We will also be exploring how to update [Raspbian Jessie to Stretch](https://pimylifeup.com/update-raspbian/), Stretch being the current latest version of Raspbian available.

There is numerous reasons why you might want to update Raspbian to newer versions. One of the biggest reasons is the ease of access to newer versions of the packages and access to more modern packages that were deemed as to unstable for your current release. For instance PHP 7 is not available in Raspbian Jessie and Wheezy but is easily available in Raspbian Stretch as it was still in its infancy when Raspbian Jessie was pushed out.

##  How to update packages on Raspbian

Luckily for us updating packages on Raspbian is incredibly easy, it involves typing two very simple commands into terminal. It is good to remember the two commands that are shown below as they will quickly become some of your most used [Linux commands](https://pimylifeup.com/linux-commands-cheat-sheet/).
    
    
    sudo apt-get update
    sudo apt-get upgrade

The first of these commands (**_sudo apt-get update_**) makes a call to the **_Advanced Packaging Tool_** (**_apt_**) to update the package list, this is highly important as the **_install_** and **_upgrade_** commands only search the pre-grabbed package list and don't make any attempts to update it themselves.

The **_update_** command works this by searching the **_/etc/apt/sources.list_** file, and then polling all the websites in the list for all available packages creating a list of their download location and their current version.

The default location that Raspbian uses for its packages can be found on [Raspbians mirror director](http://mirrordirector.raspbian.org/raspbian/), this mirror director is designed to automatically direct you to the closest download provider.

Failing to run the **_update_** command before running **_install_** or **_upgrade_** could also cause you to run into download errors especially when packages are moved around on the mirror server.

The second command (**_sudo apt-get upgrade_**) again utilizes the **_Advanced Packaging Tool_** (**_apt_**), but this time it uses it to check all currently installed packages against the package list, if there is a version miss-match for any it will attempt to update it by downloading the new version from the link in the list. The upgrade tool will never remove a package.

Sometimes packages will be held back during an upgrade due to a change in the packages dependencies. To update the packages that are held back we must use a different command. That command is shown below:
    
    
    sudo apt-get dist-upgrade

This command (**_sudo apt-get dist-upgrade_**) again utilizes the **_Advanced Packaging Tool_** (**_apt_**) it starts off by performing an upgrade as normal but when it comes to a package that has changed dependencies it intelligently handles them, this means it could also potentially remove packages in favor of others.

##  How to update Raspbian Wheezy to Jessie

In this segment, we will be showing you how to update Raspbian Wheezy to Jessie. There is a fair few steps to this process as a fair bit changed from Wheezy to Jessie.

We will walk you through the upgrading process and all the steps you need to update to Raspbian Jessie, including installing the new packages that come with the [default install of Raspbian](https://pimylifeup.com/how-to-install-raspbian/) Jessie.

Two things to note before starting the upgrade process **_backup your SD Card_** just in case this fails for some reason. You should also do this using a keyboard and mouse with **_direct access to your Raspberry Pi_** and **_not_** over SSH,

**1.** To begin updating Raspbian we need to first edit the _/etc/apt/sources.list_ file to point to Raspbian Jessie instead of Raspbian Wheezy. We can begin doing this by running the following command in terminal:

**2.** Within the sources.list file find and replace all occurrences of **_Wheezy_** with **_Jessie_**, like we have shown below.

#### **Find**
    
    
    deb http://mirrordirector.raspbian.org/raspbian/ wheezy main contrib non-free rpi

#### **Replace**
    
    
    deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi

Once you have finished replacing **_Wheezy_** with **_Jessie_** you can save and quit by pressing **_Ctrl + X_** then **_Y_** and finally pressing **_Enter_**.

**3.** Next we have to also modify the **_/etc/apt/sources.list.d/raspi.list_** file, this file acts as another way of adding entries to the **_sources.list_** file we modified in the previous step. Run the following command to begin editing the file:
    
    
    sudo nano /etc/apt/sources.list.d/raspi.list

**4.** Within the **_raspi.list_** file we need to modify the first entry changing **_Wheezy_** to **_Jessie_**, we also need to add "**_ui_**" to the end of the line, just like we have shown in our example below.

#### **Find**
    
    
    deb http://archive.raspberrypi.org/debian wheezy main

#### **Replace**
    
    
    deb http://archive.raspberrypi.org/debian jessie main ui

Once you have finished modifying the file you can save and quit by pressing **_Ctrl + X_** then **_Y_** and finally pressing Enter.

**5.** Now before we begin the update process itself, we need to create a directory, this is a requirement for some of the new and updates packages that are provided in Raspbian Jessie. Type the following command into the Raspberry Pi's terminal to create this directory.
    
    
    mkdir /home/pi/.config/autostart

**6.** Now we can finally begin the update process, please be prepared for this to take a couple of hours as it is quite an extensive process. Run the following two commands on your Raspberry Pi to begin the update process:
    
    
    sudo apt-get update
    sudo apt-get dist-upgrade -y

![Pi Book Large](https://cdn.pimylifeup.com/wp-content/uploads/2017/04/pi-book-long.jpg)

> _First boot after updating to Raspbian Jessie_

**1.** Once the update process has completed, you need to reboot your Raspberry Pi. Easiest way to do this is to type the following command into terminal.
    
    
    sudo reboot

**2.** Upon rebooting you will see several messages about "**_Calling CRDA to update world regulatory domain_**", there is no need to worry about these messages, just wait until they stop appearing before proceeding.

**3.** Once the reboot has completed, you can now login to your Raspberry Pi using your Pi user. If the GUI fails to automatically start up you can type the following command into terminal:
    
    
    startx

Be prepared to have to wait several minutes for the desktop to launch. This is due to it requiring having to update files as it loads. The screen will go black during this time, but just be patient and wait for it to finish.

### Adding the new packages from Raspbian Jessie

Now we can move on with adding the new packages that were introduced with a fresh installation of Raspbian Jessie. You can simply run the following command to install these packages.
    
    
    sudo apt-get install rc-gui libreoffice libreoffice-gtk alacarte bluej greenfoot claws-mail

The packages that you are installing, in order of their name are as follows. The new GUI version of the raspi-config command line tool, [LibreOffice](https://www.libreoffice.org) and its GTK extension, the [Alacarte menu editor](https://launchpad.net/alacarte), both the [BlueJ](https://www.bluej.org/) and [Greenfoot](https://www.greenfoot.org/) Java IDE's, and finally we also install the [ClawsMail](http://www.claws-mail.org/) email client.

If you are aiming for a slimmer installation, you can just install **_rc-gui_** and **_alacarte_**, or skip the installation of the packages altogether if you have no intention of using the GUI.

### Fixing the GUI for use with Raspbian Jessie

Finally, we need to fix various issues with the upgrade to the newer Raspbian Jessie UI. To do this we will be user numerous commands, we will explain what each command does underneath it. To proceed type in each of the commands shown below:
    
    
    cp –ax /usr/share/themes/PiX ~/.themes

This makes Raspbian load in the new version of the PiX GTK theme.
    
    
    sudo rm /etc/xdg/autostart/clipit-startup.desktop

This command stops the ClipIt application from automatically starting up on boot.
    
    
    sudo rm /etc/xdg/autostart/wicd-tray.desktop

This command will stop the Wicd network manager from starting up on boot automatically.
    
    
    sudo rm –rf /var/lib/menu-xdg

This removes a massive list of shortcuts that are automatically placed in the "Other" menu, users don't need to deal with these.
    
    
    sudo raspi-config nonint do_boot_behaviour_new B4

This tells your Raspberry Pi to boot to desktop and to automatically login as the default pi user.
    
    
    sudo rm /usr/share/applications/obconf.desktop

This hides the menu shortcut for the **_Openbox Window Manager_**, we no longer need to link to this as its functionality has been replaced by the brand new **_Appearance Settings application_**.

You should now have a Raspberry Pi that has successfully update from Raspbian Wheezy to Jessie. With any luck your upgrade would of occurred without running into any issues. If you continue onward, you can then upgrade your Raspberry Pi from Raspbian Jessie to Stretch.

![Cayenne Large](https://cdn.pimylifeup.com/wp-content/uploads/2016/06/cayenne-raspberry-pi-long-v2-border.jpg)

##  How to update Raspbian Jessie to Stretch

In this part of the article we will be exploring on how to update your Raspberry Pi from Raspbian Jessie to Raspbian Stretch.

Before we start the whole upgrade process make sure you backup your SD Card just in case this fails for some reason. You should also do this using a keyboard and mouse with direct access to your Raspberry Pi and not over SSH. Finally Stretch has not yet officially been released, so there might be bugs.

**1.** Before we begin switching our sources over to Stretch, we will first perform a full system upgrade to ensure we are running the latest available packages in Jessie. To do this run the following two commands in terminal:
    
    
    sudo apt-get update
    sudo apt-get upgrade -y

**2.** In some cases, packages may be held back, this is the last thing we want when upgrading the system to Stretch as it may cause some serious issues down the track. Let's enforce upgrading to the held back packages by running the following command in terminal on the Raspberry Pi.
    
    
    sudo apt-get dist-upgrade -y

**3.** In some cases, packages may be held back, this is the last thing we want when upgrading the system to Stretch as it may cause some serious issues down the track. Let's enforce upgrading
    
    
    sudo rpi-update

**4.** Now to get Raspbian to update to stretch we need to modify the **_/etc/apt/sources.list_** file so it points to Raspbian Stretch instead of Jessie. Begin editing this file by running the following command in terminal:
    
    
    sudo nano /etc/apt/sources.list

**5.** Now that we have done the initial updates we can now modify the **_sources.list_** file and replace all occurrences of **_Jessie_** with **_Stretch_**, like we have shown below. This makes Raspbian search the new Stretch repository for packages.

#### **Find**
    
    
    deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi

#### **Replace**
    
    
    deb http://mirrordirector.raspbian.org/raspbian/ stretch main contrib non-free rpi

Once you have finished switching **_Jessie_** out for **_Stretch_  
** you can save and quit by pressing Ctrl + X then Y and finally pressing Enter.

**6.** With that done we now need to modify the **_/etc/apt/sources.list.d/raspi.list_** file, this file adds additional sources to our **_sources.list_** file that we made modification to in the previous step. Run the following command to begin editing the file:
    
    
    sudo nano /etc/apt/sources.list.d/raspi.list

**7.** Now that we are editing the **_raspi.list_** file we need to change the first entry by replacing **_Jessie_** with **_Stretch_**.

#### **Find**
    
    
    deb http://archive.raspberrypi.org/debian jessie main ui

#### **Replace**
    
    
    deb http://archive.raspberrypi.org/debian stretch main ui

Once you have finished switching **_Jessie_** out for **_Stretch_** you can save and quit by pressing **_Ctrl + X_** then **_Y_** and finally pressing **_Enter_**.

**8.** To ensure we have a fast and smooth updating process, we will also need to remove the package called **_apt-listchanges_**. The reason for removing this package is to stop it from trying to load the changelog for the huge amount of packages that are going to be upgraded.

To remove this package, we need to run the following command in terminal on the Raspberry Pi.
    
    
    sudo apt-get remove apt-listchanges

**9.** Now that we have finished updating both the **_raspi.list_** file and the **_sources.list_** file we can proceed with updating Raspbian to Stretch. Run the following two commands on your Raspberry Pi to begin the update process. Please be prepared for this to take several hours as it is a rather extensive process.
    
    
    sudo apt-get update
    sudo apt-get dist-upgrade -y

You will have to pay attention during this installation process as time to time you will be required to input '**_Y_**' and press **_Enter_** for the upgrade process to continue onwards.

**10.** With our Raspberry Pi now successfully updated to Raspbian Stretch there are a few more things we will want to do. During installation, many packages will be marked as no longer needed due to changed dependencies.

To remove these, we can simply type in the following command into the terminal on the Raspberry Pi:
    
    
    sudo apt-get autoremove -y

**11.** After running **_autoremove_** we should also clean out the package cache, the command we will be using **_autoclean_**, will automatically remove any packages files that are no longer able to be downloaded, and are largely useless.

Run the following command in your Raspberry Pi's Terminal to automatically clean these packages up.
    
    
    sudo apt-get autoclean

**12.** Finally the last thing we should do is reboot the Raspberry Pi to ensure it loads in all the new packages and services correctly.

Simply run the following command in terminal to restart your Raspberry Pi.
    
    
    sudo reboot

I hope that you now know how to update Raspbian and that you now have a Raspberry Pi that has been successfully updated from Raspbian Jessie to Stretch. You can now continue on with [working on some Raspberry Pi projects](https://pimylifeup.com/category/projects/) or just using your Pi as you would normally. If you run into any issues or have any feedback feel free to drop a comment below.
