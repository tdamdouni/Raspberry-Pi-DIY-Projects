# Mount a Raspberry Pi SD card on a Mac (read-only) with osxfuse and ext4fuse

_Captured: 2017-08-24 at 18:01 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blog/2017/mount-raspberry-pi-sd-card-on-mac-read-only-osxfuse-and-ext4fuse)_

![So you're telling me I can read files from a Raspberry Pi microSD card?](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/images/so-youre-telling-me-so-youre-telling-me-i-can-read-files-from-a-raspberry-pi-micro-sd-card.jpg)

For my [Raspberry Pi Time-Lapse App](https://github.com/geerlingguy/pi-timelapse), I find myself having to either copy hundreds (or thousands!) of 3+ MB image files, or a 1-2 GB video file from a Raspberry Pi Zero W to my Mac.

Copying over the WiFi network _works_, but it's extremely slow (usually topping out around 5 Mbps... which means it could take a couple hours to copy). So I decided to finally try to mount the Raspberry Pi's drive directly on my MacBook Pro (running macOS Sierra 10.12). This is normally a bit tricky, because the Raspberry Pi uses the Linux `ext4` filesystem--which is not compatible with either macOS or Windows!

In the past, I would [use the `dd` utility to back up the entire card](https://raspberrypi.stackexchange.com/a/313/6506), and then I would mount that backup disk image and read data off of it. But this is annoying, because `dd` will back up the _entire_ microSD card, not just the data I want. So it takes a really long time.

Luckily, there are open source tools that allow ext4 filesystems to be mounted on a Mac (read-only, but that's all I need to copy off the time-lapse stills and video).

Here's how to mount the Raspberry Pi's ext4 filesystem on a Mac (almost everything will be done in the Terminal app (in Applications > Utilities)):

  1. Plug the microSD card into a card reader connected to your Mac. The `boot` volume will be automatically mounted, but it doesn't contain all the files from the Pi's primary filesystem.
  2. Make sure you have [Homebrew](https://brew.sh) installed (instructions [here](https://brew.sh)), so you can install the tools you need to mount the filesystem.
  3. Using Homebrew, install osxfuse and ext4fuse (find out more about the tools on the [FUSE for macOS](https://osxfuse.github.io) website): 
    1. `brew cask install osxfuse`
    2. `brew install ext4fuse`
  4. Use Disk Utility on the command line to find the Raspberry Pi's partition ID; run `diskutil list` to get output like below:
    
        $ diskutil list
    /dev/disk0 (internal):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                         500.3 GB   disk0
       1:                        EFI EFI                     314.6 MB   disk0s1
       2:                  Apple_HFS Macintosh HD            499.3 GB   disk0s2
       3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
    
    /dev/disk2 (external, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:     FDisk_partition_scheme                        *32.0 GB    disk4
       1:             Windows_FAT_32 boot                    66.1 MB    disk4s1
       2:                      Linux                         31.9 GB    disk4s2
    

You should be able to tell which drive is your Pi drive by the description (`external, physical`), the 'Linux' partition type, and the size of the disk (e.g. `31.9 GB` for my 32 GB card). The ID is the `disk4s2` in my case, in the `IDENTIFIER` column.

  5. Create a 'mount point'--a folder on your Mac where you will 'mount' the Linux partition so you can read data from it: `sudo mkdir /Volumes/rpi` (`sudo` requires you to enter your Mac account's admin password, since it performs actions with elevated privileges--enter your password when prompted.)

  6. Mount the drive using `ext4fuse`: `sudo ext4fuse /dev/disk2s2 /Volumes/rpi -o allow_other`

> The `-o allow_other` is required to make sure the mounted disk is readable by everyone (and not just the `sudo`/`root` user). See this issue: [Unable to open ext4 mounted partition on El Captain](https://github.com/gerard/ext4fuse/issues/36).

Now you'll see the `rpi` volume mounted in the Finder. You can open it and read from it just like any other disk, card, or flash drive you connect to your Mac.

Once you're finished, make sure you safely unmount the disk, by either ejecting the disk in the finder, or running `sudo umount /Volumes/rpi` in Terminal. After that, you can unplug the card and put it back in your Pi, where it will be ready to do more awesome Pi things!
