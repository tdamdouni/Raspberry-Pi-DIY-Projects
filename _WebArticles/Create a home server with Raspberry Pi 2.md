# Create a home server with Raspberry Pi 2

_Captured: 2015-12-15 at 12:04 from [www.itworld.com](http://www.itworld.com/article/2901051/create-a-home-server-with-raspberry-pi-2.html)_

![server](http://images.techhive.com/images/article/2015/03/server-100575204-primary.idge.jpg)

Gone are the days when we used to have one, shared 'family' PC. Also gone are the days when we used to carry USB drives to move data between devices. Now each of us works on multiple devices -- desktops, laptops, tablets, Chromebooks, smartphones, etc. And we want to be able to access data across all of these devices.

We can use cloud services to access such data, but there is much more data that we don't need (or want) to put in the cloud, including movies, TV-shows, music, pictures and documents. If you have guests and you want to show them recent family pictures there is no need to go grab your laptop. You can display them directly on your phone, tablet or even the TV. If you want to show them a home video of your son, you don't have to upload it to YouTube just to watch it again locally.

**[ Related: [10 insanely innovative, incredibly cool Raspberry Pi projects](http://www.itworld.com/article/2895970/10-insanely-innovative-incredibly-cool-raspberry-pi-projects.html) ]**

The answer is simple: set-up your own file server. And you don't have to spend a whole lot of money to do it. We are going to deploy the $35 Raspberry Pi 2 to do the job.

You should be someone who is well versed with Linux and is comfortable with command line.

### What we need

We need some hardware and software to get started. We need the latest Raspberry Pi 2, a 5V, 2mA charger, a microSD card (minimum capacity 8GB), external hard drives which will be used as storage and optional keyboard and an HDMI monitor (for initial set-up only). We will be using the Pi headless.

Connect all the hardware and burn the Raspbian image on the microSD card.

### How to install Raspbian

Raspbian is a Debian based distribution optimized for Raspberry Pi that is powered by an ARMv7 processor. Download the OS from the official site (Don't download any software, even if it's open source, from unknown sources). Extract the .zip file to get an .img file.

Then plug in the SD card to the PC and run _lsblk_ command, which will give you the device node for your card. It should be something like _/dev/sdX_. Instead of X it would be something like a,b,c,d...in my case it was _/dev/sdc_. Once you have determined the device node, run the dd command to convert and copy the operating system files to the sdcard:

`sudo bs=4M dd if=/path_of_raspbian.img of=/dev/sdX`

One important note: While running the above command, do not use any number followed by the device node, so it should not be _/dev/sde1_, it must be _/dev/sde._

Once the image is written to the SD card, plug it into the Pi, connect the device to the ethernet cable, connect the monitor, power cable and keyboard and mouse.

Once you boot into Pi, it will throw some instructions to optimize the OS for the device. Just follow the instructions. Step 1, 2 are important so don't skip them, the second step will allow you to create a password for your Pi. If you want to give a custom name to your Pi (the name that will show up on your local network) then also click on the step 8 [Advanced Options] and click on A2 to change the Hostname. You are all set and just click on <Finish>.

If (and only if) you don't have a monitor and keyboard to spare, you can manage your Pi from a different PC via ssh. To do this, first find the IP address of the device from your modem settings and then _ssh_ into the Pi. You may need to install openssh packages on your main PC:

`ssh pi@IP_ADDRESS`

Example:

`ssh pi@10.0.0.110`

In order to run the Raspbian configuration via ssh, just run the `sudo raspi-config` command and you will be greeted by the configuration window.

### Update the OS and install the needed software

By default, the system user is pi and the password is root. Now update and upgrade the OS so it's secure.

`sudo apt-get update`  
`sudo apt-get dist-upgrade`

Once your system is fully up-to-date, install samba server

`sudo apt-get install samba samba-common samba-common-bin`

Then add the user 'pi' to samba group:

`sudo smbpasswd -a pi`

### Mount the external hard drive

Now we need to mount the external hard drive where all your data is saved. I am assuming that the drive is formatted in 'ext4' format. If the drive is NTFS (which I won't recommend) then you also need to install _ntfs-3g_ packages.

Connect the hard drive and find the UUID of the partition where your data is stored:

`blkid`

It will give you an output similar to this:

`pi@swapi ~ $ blkid `

`/dev/mmcblk0p1: SEC_TYPE="msdos" LABEL="boot" UUID="140A-14B7" TYPE="vfat" `

`/dev/mmcblk0p2: UUID="f24a4949-f4b2-4cad-a780-a138695079ec" TYPE="ext4" `

`/dev/sda1: LABEL="EFI" UUID="67E3-17ED" TYPE="vfat" `

`/dev/sda2: LABEL="MyBook" UUID="94240D3D240D2438" TYPE="ntfs" `

Here 'sda2' is the partition on the HDD where all my files are. Now what we need from here is the UUID number. Note it down.

Now create the mount point:

`sudo mkdir /media/storage`

Exchange 'storage' with your desired name (it must be short and in lower-case). Change the permissions of the mount point:

`sudo chmod 770 /media/storage`

Now we have to mount the partition with proper permissions.

`sudo mount -t ntfs-3g -o uid=1000,gid=1000,umask=007 /dev/sda1 /media/storage`

In the above command replace 'ntfs-3g' with the format of your partition and and 'storage' with your mount point.

All we have to do now is add the mount point to _fstab_ so the drive auto mounts between reboots. Open the fstab file:

`sudo nano /etc/fstab`

Then add the following lines at the end:

`UUID=0AC4D607C4D5F543 /media/storage ntfs-3g uid=1000,gid=1000,umask=007 0 0`

You have to make three changes in the above code: change UUID's number to the one you found for your partition, exchange 'storage' with the mount point you created and if not using the NTFS partition, change it to the appropriate file system. Save and close the file then reboot the system. Your drive should auto mount now.

### Configure Samba server

Now edit the Samba config file to add the partitions that we want to share over the local network.

`sudo nano /etc/samba/smb.conf`

At the end of the file add a section for shared directories using the following pattern. If you have different kinds of data and you want to restrict access and keep things clean, you can create different sections for each data type. In my case I have created different sections for movies, music, pictures and documents:

`[Movies] #The name of the shared directory`  
`path = /media/storage/movies #The path of the shared directory `  
`read only = No #Ensures that it's not read only`  
`browsable = yes #Ensures that the subfolder of the directory are browsable `  
`writeable = yes # Ensures that user can write to it from networked device`  
`valid users = swapnil #The system user`

Now restart the Samba server:

`sudo service samba restart`

You are all set. Now you can access all the files on the storage drive from any of the devices connected to the same local network.

If you are on Android, install the _E S File Manager_ from the Play Store, go to LAN settings and give the ip address, username and password for the samba server. You have your files on your Android. You can play videos, listen to music, see pictures and edit and read documents.

If you are on iOS you can grab any file manager that supports 'Samba' such as FileExplorer. Open the app click on the '+' icon and then select the 'Linux/UNIX', it will show you the 'Pi' server in the list. Click on it and choose 'Registered user', and then give the samba user and password. All of your files are there on your iPad.

If you are on Linux (unfortunately each desktop environment deals with it differently), open the file manager and then go to the 'network' option. Provide the IP address, username, and password when asked. If you are on Mac OS X, then go to **Finder > Go > Connect to the server** option.

You can also use the current set-up as a media streaming server. I have earlier written two articles on [how to use Samba as media server](http://www.itworld.com/article/2896576/how-to-install-android-apps-on-amazon-fire-tv-stick-and-turn-it-into-a-media-center.html), check them out.

**This article is published as part of the IDG Contributor Network. [Want to Join?](http://www.itworld.com/contributor-network/signup.html)**
