# Raspberry Pi + Webcam + Zoneminder

_Captured: 2017-05-06 at 16:09 from [www.holylinux.net](https://www.holylinux.net/content/raspberry-pi-webcam-zoneminder)_

### 0\. Parts & Software

Approximate Total Price: ~$50

Notes and Quirks with webcams:

  * This webcam does _not_ need a self-powered USB hub. Some models do.
  * This model is not found using "zmu -d /dev/video0 -vqV2" (etc) - it does not enumerate. I used v2l utils to identify capabilities.
  * You may want to consider running Zoneminder on a desktop/server machine and use Pi as capture only. I ran it all from Pi to show it can be done.

### 1\. Install

Installing Zoneminder should also install (among others) php/mysql/ffmpeg and apache2 - I like to do Apache separately.
    
    
      sudo apt-get update && sudo apt-get upgrade
      sudo apt-get install apache2
      sudo apt-get install zoneminder
      sudo apt-get install v4l-utils
    

Unfortunately the package for Zoneminder needs some work. Please follow this carefully!

### 2\. Configure Apache/Web and Permissions
    
    
    # Allow www-data to access webcam:
      sudo usermod -aG video www-data
    
    
    
    # Add CGI ScriptAlias if not present after installing:
      sudo nano /etc/zm/apache.conf
    
    
    
    Alias /zm /usr/share/zoneminder
    **ScriptAlias /cgi-bin /usr/share/zoneminder/cgi-bin**
    <Directory /usr/share/zoneminder>
      php_flag register_globals off
      Options Indexes FollowSymLinks
        <IfModule mod_dir.c>
          DirectoryIndex index.php
        </IfModule>
    </Directory>
    
    
    
    
    # Correct ownership/give write+read+execute dir access to www-data group under /var/cache/zoneminder/*
      sudo chown -R root:www-data /var/cache/zoneminder/*
      sudo find /var/cache/zoneminder/ -type d -exec chmod 775 {} +
    
    
    
    # Correct Perl memory bug in zoneminder code if present:
    # REF : http://www.freshports.org/multimedia/zoneminder/files/extra-patch-scripts_ZoneMinder_lib_ZoneMinder_Memory.pm.in
      sudo nano /usr/share/perl5/ZoneMinder/Memory.pm
    
    
    
    # SymLink Apache file to conf.d:
      sudo ln -s /etc/zm/apache.conf /etc/apache2/conf.d/zoneminder.conf
    
    
    
    # Install Cambozola Java Plugin
      mkdir ~/tmp && cd ~/tmp
      wget http://www.andywilcock.com/code/cambozola/cambozola-latest.tar.gz
      tar xvf cambozola-latest.tar.gz
      sudo cp ./cambozola-*/dist/cambozola.jar /usr/share/zoneminder
      cd ~ && rm -rf ~/tmp  
    

### 3\. Find your webcam formats for zoneminder
    
    
    # Find formats of webcam for zoneminder config:
      zmu -d /dev/video0 -vqV2
    # If that does not work or fails to enumerate, try:
      v4l2-ctl --list-formats
    

### 4\. Kernel shared memory settings:
    
    
    # Set shared memory for 512MB RPi board:
    # 128MB shhmax shared:
      sudo su -
      echo "kernel.shmmax = 134217728" >> /etc/sysctl.conf
      exit
    # 2MB shmall pages:
      sudo su -
      echo "kernel.shmall = 2097152" >> /etc/sysctl.conf
      exit

### 5\. ZM Setup and Testing  


From Pi desktop:  
**<http://localhost/zm>**  
or  
**<http://LAN.IP.FOR.RPI/zm>**  
if on separate pc on local network (Recommended)

Note: Remeber that running a desktop manager under the RPi will use more memory and resources - not advised.

####   
Setup a bandwidth profile:

  * Click Options on far right. Click "High B/W".
  * Change "WEB_H_REFRESH_IMAGE" to "5" (seconds).
  * Make sure "jpeg" is set as method for stream.
  * SAVE.
  * On main console page pick "Low" Bandwidth link and change to "High" Bandwidth.
  * Click Options on far Right and Pick "Images"
  * Look for OPT_CAMBOZOLA and check it.
  * Look for PATH_CAMBOZOLA and you should see or set to: "cambozola.jar" (only)
  * Look for PATH_FFMPEG and set to: "/usr/bin/ffmpeg"
  * **Note:** For Cambozola to work, you may need to set an exception on it's Java jar. (Self-Signed as of this writing)
  * SAVE.

-> Select "/dev/video0 (0)" Link (or your default device)

  * Source: Local
  * Function: Monitor (later you can change this if everything works to MoDetect)
  * Set frame rate at 5. Set 10 as max.

(Setup web/security camera using settings found above in STEP 3).  
(Many cheaper webcams use NTSC or PAL + YUYV or MPEG1 compression)

  * Channel = 0
  * 320x240 -> (Set capture width @ 320 or less. Set capture height @ 240 or less.)
  * SAVE.
  * Click 'Monitor-1" (default monitor) from main console page.
  * You should see: a stream if using Cambozola, or a new JPG every 5 secs if not using it.
  * Note on Cambozola: You may need to edit security for your Java client and add an exception for your IP address/site to avoid Java execution errors or warnings. (The Jar file is self-signed.)
![](https://www.holylinux.net/files/pi-with-webcam.jpg)

> _You should now have a basic working Zoneminder install on your Pi!_
    
    
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Notes 2/11/2015:
     This has been running for 4 days now with motion detect set/recording.  It
    has caught 12 events so far. CPU load was an issue originally  and I had to
    tweak FPS, kernel shhmax, and kernel shmall many times before there were no
    errors found in zm logs and RPi seemed stable.  When you get yours  working
    pay attention to /var/log/syslog and dmesg.  Watch for shared memory errors
    and permission problems. If you find any make sure your kernel settings are
    as above.
    
     If you find any errors in this document let me know and I will update.
    
     GOOD LUCK! Happy RPing
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    

References:  
<http://www.zoneminder.com/wiki/index.php/FAQ> (Specifically Kernel memory use)  
<http://paul-ik.blogspot.com/2012/09/starting-with-zoneminder.html>  
<https://www.lisenet.com/2013/zoneminder-installation-on-debian-wheezy-with-logitech-quickcam-pro-5000/>  
<http://rainbow.chard.org/2012/04/24/using-zoneminder-with-a-cheap-cctv-camera/>
