# Accessing full Raspberry Pi SD card on a Mac

_Captured: 2017-08-14 at 10:10 from [blog.gbaman.info](http://blog.gbaman.info/?p=328)_

It can be annoying that on Windows and Mac by default they are unable to see the data partition on a Raspberry Pi SD card.

It is able to see the BOOT partition as it is formatted FAT32, a standard format used by a lot of different types of removable drives like flash drives and it can be read by just about every operating system.

The other partition, the one with the data on it is EXT3, the standard Linux filesystem format. Windows and Mac do not officially support it but as Mac OS is Unix based, it is a little easier to implement a driver for it that with Windows.

# Warning

Just a word of warning, the fuse-ext2 driver is far from as polished as the NTFS (Windows) and HFS (Mac OS) drivers built by companies with entire teams to maintain them. Because of this there is a much higher chance you will corrupt or kill your SD card.

Although it has never happened to me, the chance it there.

**You have been warned**

## Fuse for OS X

The first bit needed is Fuse (Filesystem in UserSpacE). Basically Fuse allows you to load additional filesystem drivers in as a userspace program. AKA it loads new filesystem drivers as user programs!

So go grab the most recent version (currently 2.7.0) from [here](http://sourceforge.net/projects/osxfuse/files/) and run the installer.

The important bit is when you get to the "Installation Type" section you must select all 3 options (including MacFUSE Compatibility Layer").

Once the installation is complete, restart your computer.

## Fuse-ext2

Now we have the ability to add filesystem drivers, lets actually add the one we want. Although the name of the driver is Fuse-ext2, it also supports ext3 so we are fine.

You can download Fuse-ext2 from [here ](http://sourceforge.net/projects/fuse-ext2/files/fuse-ext2/fuse-ext2-0.0.7/fuse-ext2-0.0.7.dmg/download)then run the installer selecting all the default options.

That is it, ext3 filesystems connected to your Mac should now pop up as normal external devices in Finder.

## But wait, I can't edit them? They are read only!

Correct, by default Fuse-ext2 disables write access as it is still experimental and dramatically increases the chance of corrupting the SD card.

If you are happy with read only access and want to play it safe, reboot your computer to make sure everything is cleared out and you are done.

If though you want read/write access and you have read my big warning and are happy to take the risk, then open a terminal (search in spotlight for terminal or it is in utilities in your applications folder) and enter in

`sudo nano -c /System/Library/Filesystems/fuse-ext2.fs/fuse-ext2.util `

This will open up the fuse-ext2 configuration file in a commandline text editor called nano.

Scroll down (using the arrow keys to move around) till you find the mount function. Comment out the OPTIONS= and copy in the new line.
    
    
    OPTIONS="auto_xattr,defer_permissions,rw+"

The final section should look like this.
    
    
    function Mount ()
    {
        LogDebug "[Mount] Entering function Mount..."
        # Setting both defer_auth and defer_permissions. The option was renamed
        # starting with MacFUSE 1.0.0, and there seems to be no backward
        # compatibility on the options.
        # OPTIONS="auto_xattr,defer_permissions"
        OPTIONS="auto_xattr,defer_permissions,rw+"
    
        # The local option is only enabled on Leopard. It causes strange
    

To save the text file, hold the ctrl+x keys, then hit y followed by enter.

Now, just for good measure do one last reboot and that should be it.

## Final Warning

One final suggestion, make sure you properly eject any filesystem using the ext2 driver! Pulling it out without ejecting is a sure fire way to get the SD card corrupt and only costs you a few seconds. Remember pulling out a pen drive without ejecting has a small chance of corrupting it and with this because you are using a driver that is a lot less stable, you are dramatically increasing the chance!
