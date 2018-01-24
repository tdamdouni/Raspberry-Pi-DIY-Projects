# PiKrellCam - OSD Motion Detect Program

_Captured: 2017-11-04 at 11:12 from [billw2.github.io](http://billw2.github.io/pikrellcam/pikrellcam.html)_

![PiKrellCam Image](http://billw2.github.io/pikrellcam/images/email.jpg)

Overview

PiKrellCam is an audio/video recording motion detect program with an OSD web interface that detects motion using the Raspberry Pi camera motion vectors. Audio can be optionally recorded if a USB sound card + microphone is connected. PiKrellCam's architecture is built around full featured internal motion detection without any dependence on an external motion detect program and it centralizes built in functionality for simplified web page interaction.

#### Features

  * Camera mjpeg streaming to a web displaying OSD user interface. Text, graphics and motion vectors are overlay drawn on the mjpeg stream. Audio can also be streamed but currently may not work in all browsers. 
  * Pi camera MMAL motion vector detection and motion video recording with configurable one second resolution pre capture, post capture and event gap times. 
  * Motion detect videos are saved with a corresponding thumbnail image that is a snapshot crop of the moving object in the video. So at a glance you can see the cause of the motion detect (car, animal, person, etc). 
  * Built in motion start event, end event and motion preview jpeg save event command execution. Email a motion event jpeg or scp the motion video to one or more off site locations. The above image is a jpeg PiKrellCam emailed to me when it motion detected one of my roadrunners. 
  * Motion detect regions of any number, size and position that are real time graphically edited from the web page. Motion regions are configured as presets or can be saved/loaded by name. 
  * Real vector processing of the camera motion vectors with multiple passes to get good motion detect sensitivity and noise immunity. Dual motion detect algorithms with configurable sensitivites operate in parallel. One algorithm is tuned to detect smaller (possibly slower moving) objects at a distance and the other is tuned to detect larger or very close objects. 
  * Command scheduling for shell scripts, FIFO commands or system commands is built in. Commands can be time and frequency scheduled from a dynamically reloaded arbitrary length list of commands. 
  * Video record with pause function and timelapse with hold function for flexible record timings that can be scheduled from the command list. 
  * Multiple settings presets which can be cycled through with single clicks of a web page button. Each setting preset can be configured with a set of motion detect regions and motion detect sensitivities. 
  * Built in servo control using Pi hardware PWM GPIOs or optionally ServoBlaster. Graphical OSD configuration of servo position presets, servo pan/tilt limits and servo smooth motion timings. Moving between position presets is a single click web page button and each position preset has its own set of multiple settings presets. 

The pikrellcam program, source, scripts, and www web files are all installed under /home/pi in the pikrellcam sub directory and the program runs as the user pi. The goal is that the install be as localized as possible, however, the media directory may optionally be relocated to some other convenient location.

This video shows the PiKrellCam OSD:

And this is a motion detect video PiKrellCam recorded. It demonstrates the pre capture and post capture times which are both set to 5 seconds. Roadrunners don't really fly, but they can hop "fly" into a tree and then glide down from a tree branch which is what this roadrunner did:

Motion Detection

The Pi camera gives us vectors, so PiKrellCam processes vectors and does not treat them as if they were scalars. The interesting result is that detecting motion gets reduced to object position and movement detection.

The program makes a few passes over the vector array. First, as a noise filter for what I call sparkles, it removes vectors which pass the magnitude limit test but have no adjacent passing vectors. Then it builds composite motion region vectors and uses dot product to filter vectors for direction to get better final composite vectors. The direction filtering requires individual vectors to have the same direction as the overall composite vector to within a few degree spread. Failing vectors are rejects which are effective in identifying noisy frames. Final vector density tests must be passed before a motion event is considered valid and the end result is that motion detection can be sensitive and yet have good noise immunity. PiKrellCam can run with really low composite vector magnitude/count limits and a setting of 5/4 is reasonable.

However, to run with low settings there should be good placement of motion regions to avoid detecting wind blown trees or tall grass. With PiKrellCam this is a quick real time graphical motion region edit from the web page that can be done in minutes.

Motion detection is a tradeoff of distance, size and speed of an object, but to give you an idea of PiKrellCam's sensitivity, the roadrunner in the above emailed jpeg was about 40 feet away and has been detected farther away.. A slow walking animal like a cat might need to be a bit closer and human detection, depending on walking speed and angle across the field of view, can be over 120 feet with a 5/4 setting. This is with the camera resolution at 1080p narrow field of view. I think the immunity to sun/cloud light level changes is pretty good.

Install

The install uses nginx as the web server because for it there is no special setup required for a web site outside of /var/www.

PiKrellCam is installed from a github git repository using the command line. The install is cloning the repository in the /home/pi directory and running the install script (an install for a user other than pi is possible):
    
    
    cd /home/pi
    git clone https://github.com/billw2/pikrellcam.git
    cd pikrellcam
    ./install-pikrellcam.sh
    

The install-pikrellcam.sh script installs needed packages and prompts for three things to configure:

  * Port number for the nginx web server to listen on. The default is 80, but an alternate non standard port number can be used in which case the PiKrellCam web page would be accessed with the URL:  
http://your_pi:port_number 
  * Auto start: if enabled a line will be added to /etc/rc.local so that pikrellcam will be auto started at boot. If this is not enabled, pikrellcam will need to be started from the web page or from a terminal after each boot. 
  * Password protection: if set a login will be required to access the PiKrellCam web pages. 

Any time you want to change how you configured these three configurations, just rerun the install script.

First Usage

Go to the PiKrellCam web page in your browser (omit the port number if it was left at default 80):  
http://your_pi:port_number

  * Expand the System panel and start the PiKrellCam prgram by clicking the button Start   
After 2 - 4 seconds, the preview image from the camera should appear. If it does not you should get in its place an error image indicating that the camera could not be started. This can happen if the camera is busy (another program is using it) or if there is a problem with the ribbon cable camera connection. If this happens, you should fix the issue with the camera and restart PiKrellCam. 
  * After the preview image appears, turn on motion detection by clicking the button Enable: Motion 
  * The OSD then shows that motion detection is ON and PiKrellCam is now operating with its default settings. 
  * Wait for motion to be detected and watch the OSD for the video record progress.  
After the video ends, view it by going to the Thumbs (or Videos) page by clicking: Media: Thumbs 
  * On the button bar, click the buttons Show: Timelapse Regions Vectors   
to toggle showing information PiKrellCam can display on the OSD. This information shows real time motion detection information and gives a feel for motion magnitudes and counts which can be configured to tune motion detection. 
  * A basic first configuration to consider is enabling motion detection to be turned on each time PiKrellCam is started. To do this, use the OSD menu system:  

    * Expand the Setup panel. 
    * The OSD will show a horizontal menu with Startup_Motion highlighted (underlined). 
    * Turn the option ON by clicking 
  * In the System panel click the Help button for a description of how pikrellcam works and how to configure it. 

Upgrades

After the initial command line git clone to install the PiKrellCam distribution, subsequent upgrades to the latest version are a simple one button click and the OSD will inform you if there was anything upgraded.

Expand the front page System panel and click the Upgrade button.  
After an upgrade to a new version PiKrellCam should be stopped and restarted from the System panel and the web pages should be reloaded to pick up any possible web page changes.

Configuration

Read the Help web page in the System panel, the configuration files in ~/.pikrellcam and the files in the scripts directory to get an idea of what can be configured.

#### Configuration files in ~/.pikrellcam

  * pikrellcam.conf - edit this file to set motion event commands, filename templates, and directories. Many other configuration variables in this file can be set from the web interface. If you edit this file, you should stop pikrellcam and restart it to pick up the changes. 
  * at-commands.conf - edit this file to set scheduled commands at a particular time and frequency. If you edit this file, it will be automatically reloaded into pikrellcam and you do not need to restart. 
  * motion-regions.conf - it's difficult to hand edit this file. Just graphically adjust your motion regions through the web interface and save. You can save name qualified region configurations which will be named motion-regions-name.conf. The special name "default" references the default file motion-regions.conf. 

#### Configuration Notes:

  * While the www directory itself is fixed, the media directory can be relocated from its /home/pi/pikrellcam/media default to something like /home/pi/media, /mnt/media or even /tmp/media which with /tmp as a tmpfs can be a useful SD card saving special case configuration as long as the limited space is managed. For this, edit media_dir in pikrellcam.conf, restart and the web page link to the new media directory will be automatically updated. 
  * If you have a flash drive plugged in that you want automatically mounted on the media directory for storing videos, stills and timelapse, edit scripts/startup and set the MOUNT_DISK variable. The mounting will automatically track the media_dir in pikrellcam.conf should you change it. If media_dir is in a tmpfs, it will not be mounted. 
  * If you want motion detect videos immediately archived to another machine you can edit scripts/motion-end and have pikrellcam scp the videos to anywhere. To enable scp copying, put your machine information into the script and enable the on_motion_end command in pikrellcam.conf. But read the warning about ssh authentication. 
  * In the ~/.pikrellcam/at-commands.conf file add any commands to run at a desired time and frequency. You can set up a scheduled timelapse run with hold times, motion detect on/off times or complex video record times with interleaved pause/run intervals. There is no limit to the number of at commands and at commands can be any pikrellcam script you write, a FIFO command, or any Pi system command. 
  * Edit ~/.pikrellcam/pikrellcam.conf and enable the on_motion_preview_save command with your email address and pikrellcam will email you a jpg of each motion detect event. 
  * The on_timelapse_end command in pikrellcam.conf is pre-configured to run the default timelapse-end script in the scripts directory. This script uses avconv to convert timelapse jpegs into a mp4 which is saved into the videos directory and then the individual timelapse files are deleted. If you want to do something different like copy timelapse files to a more powerful machine for conversion or not delete the timelapse jpegs, you will have to modify the setup.  
With the default setup on a Pi 2, avconv converts 100 timelapse jpegs into about a 17 second 12 MByte video in about 4 minutes. Toggle show timelapse on the OSD to monitor the converted MP4 size progress. A B+ with one core can be 12 times slower. 

Building From Source

To build pikrellcam, a git clone of raspberrypi/userland is not required. If you modify the source, building a new pikrellcam binary is:
    
    
       $ cd ~/pikrellcam/src
       $ make
    
    or if on a Pi 2,
    
       $ make -j4
    
    and the resulting binary will be up one directory:
    
       /home/pi/pikrellcam/pikrellcam
    

However, be aware that if you modify the web or C code source, you are effectively creating a git branch of the PiKrellCam repository and you will need to know about git so that you can manage that. You need to at least be aware that if you do the one button click upgrade from the web page any edits you have made to the source will be lost. But edits you have made to user configuration or script files will not be lost.

Internal Commands

Internal commands you put in the at-commands.conf file should be preceded by an '@' character but if echoed to the FIFO port, do not use the '@'. For example, here's some commands to put into the at-commands.conf if you wanted to timelapse something that goes on only in the mornings and evenings on weekdays:
    
    
    Mon  7:30  "@tl_start 30"
    Mon-Fri 7:30 "@tl_hold off"
    Mon-Fri 9:00 "@tl_hold on"
    Mon-Fri 17:00 "@tl_hold off"
    Mon-Fri 18:00 "@tl_hold on"
    Fri 18:00 "@tl_end"
    

So with that you will have a timelapse running off and on all week and will have a video produced in the videos directory Friday night (or Saturday morning if you are on a B+).

Many commands are for interaction with the web page, but some commands likely to be useful in at-command.conf are:
    
    
    record [on|off]
    record_pause
    still
    tl_start period
    tl_hold
    tl_end
    motion_enable [on|off|toggle]
    motion load_regions NAME
    motion limits magnitude_limit count_limit
    

Scripts can also write commands to the FIFO and some commands are specific to a script. For example the timelapse-end script sends inform status that it is converting a mp4 to the FIFO. Later I intend to add a generalized inform interface so scripts can send information to display on the OSD.

PiKrellCam Files
    
    
    The git clone should be done in /home/pi and creates the pikrellcam distribution directory:
    
        /home/pi/pikrellcam/                    # pikrellcam install root
                            pikrellcam          # pikrellcam executable
                            src/                # pikrellcam source directory
                            www/                # Web root in /etc/nginx/sites-available/pikrellcam
                            www/media           # Link to media_dir configured in pikrellcam.conf
                            scripts/            # User scripts for pikrellcam events or at commands
                            scripts-dist/       # Git managed scripts. Seeds the scripts dir
                            libkrellm/          # Local libraries needed for compiling pikrellcam
    
    
    Running the install-pikrellcam.sh script creates or alters files:
    
        /etc/rc.local                           # Line optionally added to autostart pikrellcam
        /etc/nginx/nginx.conf                   # Line edited to disable access_log
        /etc/nginx/sites-available/pikrellcam   # Custom config installed for pikrellcam
        /etc/nginx/sites-enabled/pikrellcam     # link to sites-available/pikrellcam
        /etc/sudoers.d/pikrellcam               # Gives permission for pikrellcam to be run as
                                                #   user pi by the web server (user www-data).
        /usr/local/bin/pikrellcam               # Link to /home/pi/pikrellcam/pikrellcam
    
        /home/pi/.pikrellcam/                   # pikrellcam configuration files are created if
                            pikrellcam.conf     #   they don't already exist
                            at-commands.conf    # 
                            motion-regions.conf #
    
    
    Running pikrellcam uses/creates these:
    (mjpeg_dir and media_dir can be changed in pikrellcam.conf)
    
        /run/pikrellcam/                        # Directory for the mjpeg.jpg stream
                            mjpeg.jpg           # The stream jpeg file
        /home/pi/pikrellcam/media/              # Default directory: media_dir for media files
                            videos              # Fixed videos directory under media_dir
                            stills              # Fixed stills directory under media_dir
                            timelapse           # Fixed timelapse directory under media_dir
    
    
