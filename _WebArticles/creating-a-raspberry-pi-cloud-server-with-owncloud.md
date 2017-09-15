# Creating a Raspberry Pi cloud server with owncloud

_Captured: 2017-09-14 at 14:53 from [www.1and1.com](https://www.1and1.com/digitalguide/server/configuration/set-up-owncloud-with-raspberry-pi/?utm_campaign=Newsletter+14.09.17_599ffb28597ed722e590f7c7&utm_medium=email&utm_source=newsletter)_

It's becoming increasingly popular to use online storage with personal cloud providers such as Dropbox, Google Drive, or Amazon Drive. With these services, users can store their files in a cloud. This can be accessed at any time, using nothing more than a computer or mobile device with internet access.

However, it's not uncommon for users to raise concerns regarding the reliability of their cloud hosting provider. A common criticism is that customers don't know who else has access to the saved data, and whether the files are really removed from the server when they're deleted. This is particularly important when it comes to the **storage of sensitive data**. If you want full control over your data, however, you can create and manage your own **personal cloud**.

**ownCloud **is a well-established, free, and easy-to-operate piece software developed for this purpose. The cost effective mini-computer, Raspberry Pi, acts as a particularly effective host for owncloud. This tutorial reveals everything you need to do to set up a Raspberry Pi cloud.

## Why the Raspberry Pi/ownCloud combination?

ownCloud is a free file-hosting application that users can use to create a **personal online data storage space**, providing access to their files via a web interface. However, you can also upload and download data and synchronize files over desktop clients and mobile apps. As well as functioning as a file server, ownCloud offers the following diverse functions:

  * Calendar/planner
  * Address book
  * Music and video player
  * Display of images, PDFs, and Microsoft Office files
  * Editor for OpenDocument files
  * Administration of rights (i.e. individual and group rights)

In addition, it's possible to encrypt file transfers as well as the actual files themselves. This feature alone makes ownCloud an attractive alternative to larger cloud services. Many users value the software's ability to **save files on a private server or rented web space**, rather than on the hard drive of a large, faceless corporation, where it could potentially be accessed at any time.

For file hosting, you need a computer with sufficient server software to allow the transfer of files to the internet. There are good arguments for **hosting ownCloud with a Raspberry Pi computer**. For starters, the acquisition cost for the mini-computer and its components is exceptionally good value for money - for setting up a self-hosted personal cloud, a Raspberry Pi computer offers one of the best benefit-cost ratios on the market. Furthermore, the single-board computer's power consumption is very low, which is particularly advantageous for servers that are constantly running.

In general, there are many different programs and approaches for using Raspberry Pi as an ownCloud host. For the ownCloud server described below, an **Apache web server version 2** is used, as Apache HTTP Servers are currently the most popular kind of web servers. The **script language PHP5 **is also used and **SQLite **provides the database (compared to other databases like MySQL, SQLite doesn't rely as heavily on Raspberry Pi's resources).

## Preparation for implementing ownCloud on Raspberry Pi

In order to use your Raspberry Pi to create a cloud server, you need a few extra components in addition to the mini-computer. You also need to change some settings in advance, before installing and setting up ownCloud 9.

### Required components

  * For a Raspberry Pi that functions as a server for ownCloud, we recommend the** Raspberry Pi 2 ****Model B or a more powerful model**, otherwise upload and download speeds can be relatively slow (however, this also depends on the internet connection's file transfer speed).
  * Users also require a **micro-SD memory card with sufficient memory** (at least 8GB is recommended here). The storage capacity required of course depends on the type and number of files you want to save, and whether you just want to store them on the card or on another storage system connected to the Raspberry Pi. ownCloud can also use external storage online (via FTP or WebDAV). Other cloud services such as Dropbox or Amazon S3 can be embedded in an ownCloud. In this tutorial, **Raspbian Jessie** is used as the operating system, which must be installed on the micro SD card. If your Raspberry Pi is still running on Wheezy, Jessie's predecessor, you need to update the system for this tutorial. You can download Raspbian Jessie from the official Raspberry Pi website. 
  * An **internet connection **is of course required (ideally vie **network cable**, otherwise via WiFi).
  * **Power supply** via a **micro USB cable**. 

Users can also use another storage device (such as an external hard drive or a USB memory stick) in order to have more space. These must be implemented separately, however. Furthermore, in some cases, it's helpful to use a ventilator or passive cooling system (less powerful, but with less noise), particularly if you overclock the mini-computer, which was possible with previous models up until Raspberry Pi 3 B. But even if you intend to have your Raspberry Pi running continuously as an ownCloud host, it won't hurt to use a ventilator.

Like most servers, the one in this guide can be used 'headless' (i.e. without a screen, keyboard, or mouse). Since this is the **simplest and most energy-saving solution**, it's advised to make changes to the server via **SSH remote access**. SSH clients like WinSCP and PuTTY for Windows or OpenSSH for Unix operating systems enable users to gain remote access to a server comfortably via a computer or smartphone. They connect with each other by specifying the Raspberry Pi's IPv4 address in the SSH client and activating the connection.

### Creating a static address for the Raspberry Pi

For most users, a personal cloud is only useful if the host can be accessed 24 hours a day. Only then can users retrieve and upload files outside their home network. When setting up a home server that's intended for constant use, the following problem often occurs: the internet connection used only has a **dynamic IP address**, which generally changes after 24 hours. With this kind of internet connection, therefore, it's not possible to access a server continually under the same address.

A static IP address can solve this problem. However, this service is relatively expensive and not offered by every internet provider. Users can therefore use a **dynamic DNS **(**DDNS**) to register and link a domain name with a router or computer. This is done with a program that automatically assigns the IP address of your internet connection to the domain name, making the server permanently available online under the same name. DDNS services are offered by many different providers - some free, some for a fee.

Unless you make your Raspberry Pi accessible under your network address from either a static IP address or a DDNS service, you can basically only access ownCloud from your own network. Even then, having a fileserver can still be useful - for example, if you want to make use of the automatic synchronization of files.

### Preparing the Raspberry Pi for the ownCloud installation process

It's important to ensure that your Raspberry Pi is optimally configured for use as an ownCloud host. The first step in this process is to change the standard **username **('Pi') and **password** ('Raspberry'), if you haven't already done this. Keeping the default settings as your login data is a safety risk, as anybody who finds the server online could easily seize control of it. You can change your username and password with the Raspberry Pi by entering the following command into the console:
    
    
    sudo raspi-config
    

You should ensure that the **computer and any installed packets are up-to-date** before starting the ownCloud installation process on the Raspberry Pi. For this, you should enter the following commands:
    
    
    sudo apt-get update
    
    sudo apt-get upgrade
    

## Installing ownCloud

The private cloud on the Raspberry Pi ultimately does not only consist of ownCloud software, but also diverse programs, which will be installed gradually. Unless otherwise indicated, you should always enter the commands into the Raspberry Pi's console.
    
    
    sudo apt-get install apache2
    

You can check to see if the installation was successful by entering the **Raspberry Pi's IP address **into your **browser's search bar**. All being well, you should be directed to a blank webpage that simply says 'It works!'

To make your ownCloud accessible online, activate port forwarding in your router and redirect router requests from port 433 to the Raspberry Pi. This works differently with every router, although you'll find online tutorials for many different router models. Once you've successfully set up a port forwarding, your Raspberry Pi will be accessible online under your IP address (or under its domain name if you use DDNS). Without port forwarding, you will only have access to the web server in your local network.

You can now install **PHP**, **SQLite**, and other required packages with this command:
    
    
    sudo apt-get install php5 php5-gd sqlite php5-sqlite php5-curl
    
    
    
    sudo service apache2 restart
    
    
    
    wget https://download.owncloud.org/community/owncloud-9.1.0.zip
    

You can easily install another version by changing the numbers at the end of the file name (i.e. _[…] community/owncloud-X.X.X.zip)_. The current, most stable version of the program can always be found in the download section of the ownCloud website.

Whichever option you choose, after downloading the ownCloud .zip file, you must **save and unzip the files in the right folder**:
    
    
    sudo mv owncloud-9.0.4.zip /var/www/html
    cd /var/www/html
    sudo unzip -q owncloud-9.0.4.zip
    
    
    
    sudo mkdir /var/www/html/owncloud/data
    sudo chown www-data:www-data /var/www/html/owncloud/data
    sudo chmod 750 /var/www/html/owncloud/data
    
    
    
    sudo reboot
    

### Configuring ownCloud

Once the program is installed and the file structure has been created, you can take care of **your** **personal ownCloud account**. You can do this in your Raspberry Pi's browser; simply enter the mini-computer's IP address into the taskbar and add the path ('/owncloud') at the end of the address (192.168.X.X/owncloud). If you use the server with a DDNS address, this replaces the IP address.

The ownCloud logon screen should now appear. If a performance warning about SQLite appears, you can simply ignore it - the Raspberry Pi file server is fully functional. You now need to **register an admin account** by setting up a username and password. With this, you have completed the configuration process and your personal ownCloud will be immediately available for use under this account. You can upload and download files here under the menu named 'File'.

## Notes on administration

If you have provided your Raspberry Pi with a static address in advance, you can access your personal ownCloud anywhere using your Raspberry Pi's IP or DDNS address. However, this means that - in theory - other users could have access to the server, so secure passwords are highly recommended. If your Raspberry Pi is accessible externally via the internet, you should also take care to ensure the server is always secure and up-to-date.
