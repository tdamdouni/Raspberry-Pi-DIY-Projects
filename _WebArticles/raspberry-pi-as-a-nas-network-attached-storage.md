# Raspberry Pi As a NAS (Network Attached Storage)

_Captured: 2017-08-19 at 18:20 from [www.instructables.com](http://www.instructables.com/id/Raspberry-Pi-As-a-NAS-Network-Attached-Storage/)_

![Raspberry Pi As a NAS \(Network Attached Storage\) ](https://cdn.instructables.com/FSG/7YEF/IPIK968E/FSG7YEFIPIK968E.MEDIUM.jpg)

![224.png](https://cdn.instructables.com/FHI/DOQY/IPIK96FI/FHIDOQYIPIK96FI.MEDIUM.jpg)

A **NAS or network attached storage**, is the best way to keep your data backed up and stream and access content from all the devices connected to the network. But a NAS is really a computer that is connected to the network and computers can draw a large amount of current, especially as it is powered on all the time.

So in today tutorial I'm going to show you how to convert your **Raspberry Pi **as a NAS, a raspberry pi is a low powered device and it would drag only a fraction of what power is used by an actual NAS and also to use a raspberry pi as a NAS it would reduce the cost to. But you would be loosing features like Fire and water proof and some performance when you use a raspberry pi, so unless you want to stream very large files and want to stack up your hard drives in a raid configuration, the Raspberry Pi should work just fine.

You can also check out the video tutorial on how to build this below.

## Step 1: Tools and Components 

![Tools and Components ](https://cdn.instructables.com/FIX/74NJ/IPIK96N4/FIX74NJIPIK96N4.MEDIUM.jpg)

Here is a list of the components and tools required, the list is simple and all you need is

  * A Raspberry Pi 
  * A Serial to USB Cable 
  * External Hard driver 
  * Lan Cable 
  * An SD Card 4Gb or above 
  * A Computer to get the Pi running 
  * An Active internet connection

## Step 2: Getting Started 

![Getting Started ](https://cdn.instructables.com/F4A/Q1AS/IPIK9710/F4AQ1ASIPIK9710.MEDIUM.jpg)

![raspberry pi raspbian-2.PNG](https://cdn.instructables.com/FSO/WPBZ/IPIK9750/FSOWPBZIPIK9750.MEDIUM.jpg)

If you just got your PI or have any other OS running you will first need to install the **Raspbian OS**, the procedure to do this is really very simple.

Fist, you need to visit the Raspberry Pi official website an download a copy of Raspbian OS, after the download is complete you need to download a tool called the **wind32 disk image maker**, this is free software, an alternative to this would be **Power ISO**.

After you have installed the disk image maker it is now time to connect your SD card or micro SD card if you are using a raspberry pi 2/3, to your computer. Next open up the tool and locate the image file on the computer and select the drive to write to.

Once it is done writing plug it into the raspberry pi and you should now have your raspberry pi boot up raspbian OS.

## Step 3: Serial Communication 

![Serial Communication ](https://cdn.instructables.com/FCR/941I/IPIK96LA/FCR941IIPIK96LA.MEDIUM.jpg)

![1.PNG](https://cdn.instructables.com/FWP/NJ56/IPIK96SH/FWPNJ56IPIK96SH.MEDIUM.jpg)

To establish communication between the computer and the raspberry pi I'm using serial, you could also ssh your pi or attach physical keyboard, mouse and monitor to program it. To establish a serial communication I'm using a USB to serial cable I found on eBay you can also use an Arduino to establish this communication. The serial cable has four terminals which connect to the raspberry pi GPIO pins, and the other end to a computer.

Install the drivers for the serial module if you are using windows and find out which port the serial communication is established using device manager in windows.

## Step 4: Updating the Raspberry Pi

![Updating the Raspberry Pi](https://cdn.instructables.com/FA8/60AQ/IPIK96TQ/FA860AQIPIK96TQ.MEDIUM.jpg)

![3.PNG](https://cdn.instructables.com/FZL/AL65/IPIK96U7/FZLAL65IPIK96U7.SMALL.jpg)

![4.PNG](https://cdn.instructables.com/F8N/Y5V1/IPIK96VU/F8NY5V1IPIK96VU.SMALL.jpg)

![5.PNG](https://cdn.instructables.com/FOX/C6C5/IPIK96WL/FOXC6C5IPIK96WL.SMALL.jpg)

After you have set up serial communication between the Pi and a PC, open up putty and select serial as the type of connection. Enter in the right com port and set the baud rate to 115200 and open a connection.

If everything went well you should now see a login page, the default username is 'pi' and password is "raspberry". Now lets update the Pi, now would a good time to plug in the lan cable for internet access if you not already have done it. Type in the command below to update your Raspberry Pi -
    
    
    sudo apt-get update

If you are using a hard disk formatted to ntfs files system you need to install an additional package called ntfs-3g that can be done by typing the following command -
    
    
    sudo apt-get install ntfs-3g

## Step 5: Mounting the Hard Disk 

![Mounting the Hard Disk ](https://cdn.instructables.com/F5W/9YC2/IPIK96WN/F5W9YC2IPIK96WN.MEDIUM.jpg)

![6.PNG](https://cdn.instructables.com/FCU/X01Y/IPIK96WM/FCUX01YIPIK96WM.MEDIUM.jpg)

After you have installed the ntfs package you should now see your drive show up when you type -
    
    
    sudo fdisk -l

And now it is time to mount your drive to the raspberry pi, you can do this via the following command -
    
    
    sudo mkdir /media/USBHDD1

If you have more than one drive you can mount that to now. And to mount your drive to the above directory you just created using this command -
    
    
    sudo mount -t auto /dev/sda1 /media/USBHDD1

Next lets create a folder in the drive that you want to share, (the folder is called "shares") -
    
    
    sudo mkdir /media/USBHDD1/shares

## Step 6: Installing Samba

![Installing Samba](https://cdn.instructables.com/FQQ/QBPD/IPIK96XI/FQQQBPDIPIK96XI.MEDIUM.jpg)

![9.PNG](https://cdn.instructables.com/FEM/O0LA/IPIK96YB/FEMO0LAIPIK96YB.SMALL.jpg)

![10.PNG](https://cdn.instructables.com/FHO/LHR8/IPIK96ZH/FHOLHR8IPIK96ZH.SMALL.jpg)

Now lets install Samba, Samba is the software that turns your raspberry pi as a NAS. You can install samba by typing the following command -
    
    
    _sudo apt-get install samba samba-common-bin_

After installing samba lets configure it this can be done by typin the following commands -

sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.old
    
    
    sudo nano /etc/samba/smb.conf

Scroll down to the bottom of the file and enter these few lines to enable sharing of the folder -
    
    
    [shared]  
    comment = shared folder  
    path = /media/USBHDD1/shares
    valid users = @users
    force group = users
    create mask = 0660
    directory mask = 0771
    read only = no

## Step 7: Adding Users

![Adding Users](https://cdn.instructables.com/F6I/3XV3/IPIK96ZI/F6I3XV3IPIK96ZI.MEDIUM.jpg)

![12.PNG](https://cdn.instructables.com/FSN/LF2F/IPIK9709/FSNLF2FIPIK9709.MEDIUM.jpg)

Now it is time to add users who can access the files on the server -
    
    
    sudo useradd admin -m -G users<br>sudo passwd admin

The user I created is called admin, you can name it anything you want. Now lets samba know about the new user -
    
    
    sudo smbpasswd -a admin

The above commands will ask you for passwords to access the server, you will need to remember that to access the files.

## Step 8: Testing 

Now you have finished installing the NAS server, the server can be accessed by any client connected to the same network as that of the server. You can share user folders and protect them using a password. You can power the raspberry pi using a micro USB cable and a mobile charger, and mount it in an enclosure along with the hard drives.

To add additional users you can repeat the previous step.
