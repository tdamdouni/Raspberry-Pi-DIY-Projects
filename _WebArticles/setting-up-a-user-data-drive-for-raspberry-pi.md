# Setting up a "User Data" drive for Raspberry Pi

_Captured: 2017-08-25 at 11:51 from [akashkollipara.blogspot.de](https://akashkollipara.blogspot.de/2017/06/setting-up-user-data-drive-for.html?m=1)_

![Image](https://lh5.googleusercontent.com/-H586sMBmhdE/AAAAAAAAAAI/AAAAAAAAE-8/Q2_brzw8uxI/w168-h168-p-k-no-nu/photo.jpg)

Its been a while working on Raspberry Pi 2, I realized that there is a need for "User Data" drive for the RPi. So with this blog I will be sharing the procedure to make and mount a drive.

To get started, its recommended to have monitor, keyboard and mouse connected to RPi. If its not available then follow my previous blog on [Raspberry Pi](https://akashkollipara.blogspot.in/2017/06/ssh-raspberry-pi-2-in-ubuntu.html).

Connect the drive to RPi, if the drive is formatted then you can skip these steps and jump to mounting, else if the drive is not formatted then open terminal (Ctrl+atl+T), type

this will list the drives attached to RPi. Find the drive to be formatted, now type

**replace 'your disk' with sda/sdb/sdc... whatever that you found using 'lsblk'. Be careful while entering, if you chose the mmc card the OS drive will be formatted**

first enter 'd' followed by 'n', hit enter 4 times and finally enter 'w'. With this you have created a new partition on the disk. To create file-system, type

sudo mkfs -t vfat -n 'labelDrive' /dev/sdx1

replace 'labelDrive' with name you wish for example 'User Data', inverted commas are necessary. Now the file system is created and flash drive is ready to be used. Now you need to mount the drive, so you have to chose if you want to mount it at boot or manually mount.

Before going to mount, you have to create the mount point, for example I have created "/media/pi/User Data"

to do that, type

**Mounting at boot:**

For mounting at boot we need edit /etc/fstab. To do that type

in the last line above comments enter

/dev/sdx1 /media/pi/User\040Data vfat defaults,exec,uid=1000 0 3

here '\040' is the escape character for <space> in the name. If your drive name is abc the replace User\040Data with abc, else if drive name is abc def the replace User\040Data with abc\040def.

And again x=a/b/c... find it from lsblk.

this will mount the drive. -v is the verbose for the method. If you find any errors please do comment so that I can try to help you out.

**Mounting manually:**

To mount manually, type

sudo mount -o defaults,uid=1000 /dev/sda1 /media/pi/User\ Data

this will mount the drive manually.  
just in case needed the unmount command is sudo umount /dev/sdx1

After mounting to make sure the drive has all privileges, type

Now you have a User Data drive mounted on you Raspberry Pi. If you find any errors or need any help please do comment or mail me.
