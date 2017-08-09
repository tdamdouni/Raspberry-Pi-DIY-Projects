# Executable files on the Raspberry Pi

_Captured: 2017-05-23 at 18:57 from [bigl.es](http://bigl.es/executable-files-on-the-raspberry-pi/)_

An executable file is a file that can be double clicked and it will run automatically. For Windows users you will be familiar with **.exe** files, but for Linux, what is an executable file?

Linux files have permissions that control who can see, edit or delete a file. But one of those permissions is "allow a file to be executed as a program". So lets take a look at a file that is on a USB stick inserted into our Raspberry Pi.

_We shall be using the terminal for this blog post, specifically I used SSH to remotely connect to my Raspberry Pi but you should do this from the Raspbian / Pixel desktop. Also permissions cannot be changed for drives that are formatted FAT16, FAT32, NTFS or exFAT, permissions are only supported for Linux filesystems._

## Executing Files

So I have a file that I wish to make executable, it's called **test.sh** but yours can be any file.
    
    
    pi@raspberrypi:~ $ ls  
    test.sh  
    

### Permissions

Lets take a look at the test.sh file, specifically its permissions. You can do this by typing
    
    
    ls -lha test.sh  
    

Remember to change the filename to that of your file.
    
    
    -rw-r--r--  1 pi   pi     24 Jan  4 10:02 test.sh
    

You can see "-rw-r--..." etc these show the permissions of a file/directory.

The letters are split into four groups

**File type**

In this case we can see "-" indicating it is a file. If we saw "d" then it is a directory.

**Owner Permissions**

In this case we see "rw-" indicating that the owner can read the file, write to the file, but the "-" means it is not executable by the owner.

**Group Permissions**

In this case we see "r--" indicating that the group, of which the owner belongs, can read the file, but cannot edit or make it executable.

**Other User Permissions**

In this case we see "r--" indicating that any user can read the file, but cannot edit or make it executable.

### So how can I make the file executable?

In the terminal all we now need to do is type
    
    
    chmod +x <filename.  
    

And if we now run
    
    
    ls -lha test.sh  
    

We can see that for the owner permissions we now have an "x" indicating it is executable.
    
    
    -rwxr-xr-x 1 pi pi 24 Jan  4 10:02 test.sh
    

### To run the file

All we need to do now is type
    
    
    ./<filename>
    

To run the executable file.

So in my case it was.
    
    
    ./test.sh
    

That's it! You've learnt a little Linux command line love today!

## Navigating to the USB drive

First plug in your USB drive, the Raspbian / Pixel OS automatically mounts, enabling a USB/hard/DVD drive ready for access, devices when they are plugged in. They are mounted to a specific directory on your Pi, and that directory lives inside
    
    
    /media/pi
    

So to navigate to this directory all I need to do is open a terminal and type.
    
    
    cd /media/pi  
    

Now we are inside the directory, so lets see what is in there, type.
    
    
    ls  
    

Now you should see the contents of the directory. So for me I can see
    
    
    pi@raspberrypi:/media/pi $ ls  
    USB DISK  
    pi@raspberrypi:/media/pi $  
    

**Method 1:**

So USB DISK is my USB drive, so to go into that directory, which is really our USB drive.   
Remember to change the name of the drive to match **your** USB drive name.
    
    
    cd USB\ DISK/  
    

But Les, what is that "\" all about? Well in Linux a space in a filename or directory name MUST have a backslash before it, otherwise Linux thinks there are multiple directories that you wish to enter.

**Method 2**

If you don't like method 1, then this method is a little easier. Just wrap the directory name in quotation marks and press Enter.   
Remember to change the name of the drive to match **your** USB drive name.
    
    
    cd "USB DISK"/  
    

_WOO HOO!_ We are now inside the USB disk!
