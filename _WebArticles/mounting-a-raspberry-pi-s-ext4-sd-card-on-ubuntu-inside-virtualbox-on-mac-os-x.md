# Mounting a Raspberry Pi's ext4 SD card on Ubuntu 14.04 inside VirtualBox on Mac OS X

_Captured: 2017-08-24 at 18:02 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blogs/jeff-geerling/mounting-raspberry-pis-ext4-sd)_

Since I'm running a Mac, and don't have a spare linux-running machine that can mount ext4-formatted partitions (like those used by default for official Raspberry Pi distributions like Raspbian on SD cards), I don't have a simple way to mount the boot partition on my Mac to tweak files on the Pi; this is a necessity if, for example, you break some critical configuration and the Pi no longer boots cleanly.

To mount an ext4-formatted SD or microSD card on a Mac, the easiest option is to use VirtualBox (and, in my case, Vagrant with one of [Midwestern Mac's Ubuntu boxes](http://files.jeffgeerling.com/)). Boot a new linux VM (any kind will do, as long as it's modern enough to support ext4), shut it down, go into Settings for the VM inside VirtualBox and enable USB, then reboot.

Follow these steps once the VM is booted, to mount the flash drive:

  1. Plug in the flash drive once the VM is booted.
  2. Click on the USB icon in VirtualBox's window, and select the flash drive to 'capture' it inside the VM.
  3. List all visible drives on the system: `$ sudo fdisk -l`, and it should be one of `/dev/sdb1` or /dev/sdb2 (usually, whichever is larger, with 'System' of 'Linux'.
  4. Make a directory into which you'll mount the drive: `$ mkdir /media/usb`
  5. Mount the drive: `$ sudo mount /dev/sdb2 /media/usb`
  6. All finished! cd into `/media/usb` and browse the contents of the drive.

This process was tested with Ubuntu 14.04, but should work with most Linux distros.
