# Best Raspberry Pi Projects 

_Captured: 2016-12-30 at 01:00 from [www.expertreviews.co.uk](http://www.expertreviews.co.uk/raspberry-pi-foundation/1404017/best-raspberry-pi-projects/page/0/3)_

![Raspberry Pi logo red background](http://cdn2.expertreviews.co.uk/sites/expertreviews/files/styles/er_main_wide/public/2015/10/pi_logo.jpg?itok=QWPZFHpH)

> _Raspberry Pi logo red background_

## Make a video intercom system

On the previous page we showed you how to receive real-time alerts on your smartphone when someone presses your doorbell. Although you may be satisfied with your Wi-Fi doorbell and the satisfaction of never missing a caller at your door again, we promised you more, such as photos of callers and a live video stream of who's at your front door. As we'll show you, this is possible with a Raspberry Pi and a bit of tinkering.

It's possible to use the Pushover service, which we used to send alerts from your Raspberry Pi to your smartphone, to log how many times your doorbell has been pressed. However, the logs only take the form of how many alerts per day have been sent. This clearly won't be enough to convince a courier company's customer complaints department that they were to blame for the failed delivery, rather than you. If your complaint is more serious than a failed delivery - perhaps troublesome youths are pranking you with frequent games of Cherry Knocking, for example - you'll want more than a text file to prove guilt.

What you need is incontrovertible evidence that someone approached your door with untoward intentions, and that's best done with a video. It's best to use the Raspberry Pi's bespoke [Camera Module](http://cpc.farnell.com/jsp/search/productdetail.jsp?sku=SC13023) (£20.15), as this can use the Pi's graphics processing unit and so leave the main processing unit with some headroom for other tasks. We've previously discussed how to connect the Camera Module's strange ribbon cable to the Pi, but the [Raspberry Pi Foundation's video](http://www.raspberrypi.org/help/camera-module-setup) is a clear guide. Once the camera is plugged in securely and the Pi has booted up, you'll need to activate the camera by launching the Pi Console (type 'sudo raspi-config') and selecting the Enable Camera option (use the arrow keys on your keyboard to navigate the menu). Once the camera is enabled, select Finish and agree to reboot.

![Enable cam](http://cdn2.expertreviews.co.uk/sites/expertreviews/files/styles/er_main_wide/public/8/93/enable_cam_0.jpg?itok=18wA3bb6)

> _Enable cam_

**Don't forget to enable the Camera Module before you do anything else with your Pi**

Update Raspbian with the 'sudo apt-get update' command, and then update your applications with 'sudo apt-get -y upgrade'. You should now be able to test the camera. Type 'raspistill -v -o test.jpg' and you'll see the right LED on the Camera Module itself light up and a load of photography-related information appear on your screen. You can double-check the camera is working by typing 'ls' to list the contents of the folder you're currently looking at - you should see a file called test.jpg.

If you haven't before, now is the time to set a fixed IP address for your Pi. This is best done by assigning the Pi its own IP address from your router's setup pages. You'll need to reboot your Pi for it to pick up its new, fixed IP address, so type 'sudo reboot'.

### Your call may be recorded

An easy way to integrate the Camera Module into your doorbell system would be to modify the Python script that monitors your doorbell and sends the Pushover notification to your phone, so that it also takes a picture, possibly with a file name that contains the current date and time. Doing so is slightly tricky, as the Pushover script is based on Python rather than the more basic Bash. First, we needed to install the Python version of picamera: 'sudo apt-get install -y python-picamera'. It could well be that this is installed already, but it's best to check.

![doorbell.py](http://cdn2.expertreviews.co.uk/sites/expertreviews/files/styles/er_main_wide/public/8/94/take_photo_0.jpg?itok=l0nuxi2_)

**Add a few lines of code, and your doorbell can automatically take a photo or video of your caller, as well as buzz your phone**

After this, edit your doorbell.py file ('sudo nano doorbell.py') and enter the following lines at specific points in the script, to keep the code tidy. Under the four 'import' lines add:

import picamera  
import datetime

camera = picamera.PiCamera()  
filename = datetime.datetime.now().strftime("%Y_%m_%d-%S_%M_%H.jpg")

The hard return space between these groups isn't entirely necessary, but it keeps things neat. The first two lines import some dependencies: the Python library for the Camera Module and the datetime module, which will let us name pictures taken by the camera according to the current time and date.

Next, navigate to the section of code toward the end, after the 'if' statement. Add the line 'camera.capture(filename)' on its own line and then save and exit. Every time someone presses your doorbell, your Pi will take a picture and save the image named according to the time and date. You could also take a 10-second video by using the following code instead of the 'camera.capture' line:

camera.start_recording(filename)  
sleep(10)  
camera.stop_recording()

To do the job properly you'll want a video that starts recording as soon as someone comes into view of your front door, however, and not just when someone has pressed the bell. We used such an application in Advanced Projects, Shopper 315, where we used a Raspberry Pi to make a CCTV system - the application is called Motion. More precisely, we used the version of Motion ported to run on the Pi by dozencrows of the Raspberry Pi forum, which he or she has called motion-mmal. Installing motion-mmal is fairly convoluted, so refer to the smart doorbell guide on the previous page of this article.

Unfortunately, you won't be able to take still photos with the code above at the same time as record video with the applications below. This is because whichever application - photo or video - gets hold of the camera first during Pi bootup will refuse to share the camera with anything else.

We had a little trouble getting motion-mmal to start automatically when the Pi reboots, probably due to an update for Raspbian. Therefore, instead of editing its daemon behaviour (with the command 'sudo nano /etc/default/motion') we added motion-mmal as a cronjob by adding the line '@reboot motion' to the end of the file. Access the cron tab by typing 'sudo crontab -e'; the process for adding the cronjob is the same as we covered previously. You might also want to check some of the settings in motion-mmal's config file.

Motion-mmal can also provide a live video stream, allowing you to see who's at your door in real-time: see someone with a clipboard and you'll probably just get on with the weeding, for example. However, only certain smartphone browsers understand motion-mmal's live video feed; Chrome hasn't got a clue, Maxthon crashes, Opera Mobile ignores you, Dolphin tries to download the video stream and UC Browser just gives you a page of raw code. The only mobile browsers we found to work were Safari and Firefox. If you're lucky enough to use either of those as your default browser, then you can just use motion-mmal to provide the live stream and thus turn your phone into a CCTV monitor.

![](http://cdn1.expertreviews.co.uk/sites/expertreviews/files/styles/insert_main_half/public/8/96/safari_box.jpg?itok=V79mHw9p)

**Create a video stream via motion-mmal and you can see who's at your door in Firefox or (as here) Safari**

### Who's at the door?

If you don't use Safari or Firefox as your main web browser on your phone, and don't wish to switch, you'll have a dilemma: either you can record motion-activated videos using vi motion-mmal, or you can use MJPG Streamer to send live video to your phone. If you choose the latter, don't install motion-mmal and instead use jacksonliam's experimental version of MJPG Streamer. This project integrates support for the Pi's Camera Module, making for a much easier install process. We thank Miguel Mota for bringing this project to our attention. Type the following commands into your Pi.

sudo apt-get install -y libjpeg62-dev cmake  
git clone <https://github.com/jacksonliam/mjpg-streamer.git> ~/mjpg-streamer  
cd ~/mjpg-streamer/mjpg-streamer-experimental  
make clean all  
sudo rm -rf /opt/mjpg-streamer  
sudo mv ~/mjpg-streamer/mjpg-streamer-experimental /opt/mjpg-streamer  
sudo rm -rf ~/mjpg-streamer  
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 640 -y 480" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &

The first line installs a couple of dependencies, while the second connects you to the project's 'respository' (the collection of project-wide source code) on GitHub (an online library of repositories). The rest of the commands follow jacksonliam's instructions for setting up his software, while the last line actually executes MJPG Streamer.

If you cast your mind back to our first look at the Camera Module, you'll find some of the commands in that last line familiar. The letters preceded with dashes are called switches, and describe a certain parameter or setting for the main command 'input_raspicam.so'. For example, '-fps 15' sets the frame rate of the video at 15fps, '-q 50' sets the quality to 50 per cent, and so on. We've played with these values - particularly lowering the quality value to increase the resolution - but couldn't see much difference in the final video so in the end left them at their defaults. To see for yourself, open a web browser on any device on your network and point it toward your Pi's IP address followed by ':9000' (as specified by the '-p' port switch). In our example we'd type in 192.168.1.100:9000. Usually the Stream tab is fine, but on some browsers you might have to use the JavaScript or other tabs to see the video.

**Use MJPG Streamer to provide the live video stream, and you can view it in any browser you wish. We doubt you'd want to open the door to either of these callers**

However, we want the video stream to start automatically whenever the Pi is powered up, so we're going to write a quick Bash script. First, though, you need to stop MJPG Streamer. Find its process ID (PID) by typing 'pgrep mjpg_streamer'; your Pi will return a four-digit number, so type 'kill pid XXXX', replacing the Xs with that number. We want the Bash script to be created somewhere easily accessed, so type 'cd' to go back to the /home/pi folder, and then 'sudo nano streamer.sh' to create a Bash script called streamer.sh and open it in a text editor. Enter the following before saving and exiting.

#!/bin/bash

if pgrep mjpg_streamer > /dev/null  
then  
echo "MJPG Streamer is already running"  
else  
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 640 -y 480" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &  
echo "MJPG Streamer is not running"  
fi

Make this script executable by typing 'sudo chmod ugo+x streamer.sh' and then add the script to the crontab; type 'sudo crontab -e', then add to the end of the file 'sudo bash /home/pi/streamer.sh' and save and exit. Reboot your Pi to check that the Pushover service works and the video stream starts automatically.

![Bash script](http://cdn2.expertreviews.co.uk/sites/expertreviews/files/styles/er_main_wide/public/8/97/bash_streamer_0.jpg?itok=50yQmAF1)

> _Bash script_

**Knock together a quick Bash script to automate the live video stream neatly**

### Linking up and limitations

To finish the job, whether you use motion-mmal or MJPG Streamer, you need to add the URL of your video feed to your Pushover alert. Edit the doorbell script by typing 'sudo nano doorbell.py' and scroll to the bottom to find the alert text. Then enter the URL of the video stream you want to access. In our example, where our Raspberry Pi's IP address is 192.168.1.100, if the stream is from motion-mmal we'd enter <http://192.168.1.100:8081>, and if it's from MJPG Streamer we'd enter <http://192.168.1.100:9000/stream>. Save and exit, reboot and you're all set.

While we expect some limitations on a computer costing £27, having to choose between recording video or seeing live video does rankle, as the capability to do both is clearly there in the Pi. We got our hopes up when we saw silvanmelchior's [RPi_Cam_Web_Interface](http://www.raspberrypi.org/forums/viewtopic.php?f=43&t=63276), which not only streams live video to any browser (using Motion, no less) but presents lots of camera settings in a very friendly way. However, despite our best efforts, we couldn't get Silvan's project to work. Similarly, we had hoped to be able to talk to our doorbell via our smartphone - our voice would be played through the same speakers that play the doorbell chime, so we could ask the caller to be patient, or to come and find us in the garden. Unfortunately we couldn't get this to work as the required Android and iOS apps weren't compatible with the Pi. If you want to talk to your doorbell, or even the person standing near to it, you'll either have to shout like the rest of us, or delve into Raspberry Pi-based VoIP applications. And that's a topic for another day.

**The RPI_Cam_Web_Interface is exactly what we wanted from our doorbell-based live video streaming service, but we couldn't get it to work reliably**
