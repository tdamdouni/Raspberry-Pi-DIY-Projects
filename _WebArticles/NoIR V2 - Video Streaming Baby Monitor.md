# NoIR V2 - Video Streaming Baby Monitor

_Captured: 2016-04-29 at 23:45 from [www.element14.com](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/2016/04/25/noir-v2-video-streaming-baby-monitor)_

### No I.R.

Despite its name, the new NoIR V2 camera for the Raspberry Pi isn't something designed for filming 1940's mobster movies. What makes it special isn't an additional feature, but rather what it lacks. Most digital cameras are designed to capture images in the same spectrum of light as a normal human eye, producing realistic photos and videos. While cameras can view light outside of this range, filters are use to ensure that only the desired light makes it in the final image.

![NoIRV2.jpg](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-22945-270327/1600-736/NoIRV2.jpg)

The NoIR camera does what it says in its name - unlike most cameras, it has no filter for the infrared spectrum of light. This makes photos look very alien and unnatural. Most of the colour is incorrect and any bright surfaces are extremely washed out. You might think this makes the NoIR camera nothing more than a novelty, but it has a very big advantage - being able to see in very low light environments, or capture pictures in complete darkness by using an invisible Infrared light source. The resulting pictures might not be something you would want to frame, but they are significantly more visible compared to those shot on a standard camera in the dark.

You can see a video and collection of photographs of the [NoIR V2 camera under Infrared illumination in complete darkness here](https://www.element14.com/community/community/raspberry-pi/blog/2016/04/25/video-infrared-night-vision-with-the-noir-v2), and the same for a range of more [artistic daylight images here](https://www.element14.com/community/community/raspberry-pi/blog/2016/04/25/testzing).

### 

### Video Streaming

A great use for the camera modules is to use the in built wireless networking on the Raspberry Pi 3 to stream live video across a network. In doing this there are two main network configuration options:

  * The Raspberry Pi 3 can operate as its own access point that devices connect to directly, enabling it to operate independently of other networks. This option would be the way to go if you wanted to have a single device, like an old phone or tablet, dedicated to being the display for the video stream.
  * Connect the Raspberry Pi 3 to a standard wireless router or access point. This would let users view the video stream on a smart phone or tablet without having to switch between a home, internet enabled wireless network and a separate one used for the video stream. However, if the home WiFi network is heavily used, having the Raspberry Pi stream video over it might cause problems with network congestion and bandwidth.

### Baby monitor

Combining the night vision and wireless streaming capabilities of the NoIR camera and Raspberry Pi 3 combination, I put together a project to make a video baby monitoring system. It's something that a parent would use to keep an eye on a resting child with a live video feed to a phone or tablet, and give notifications when the baby wakes or becomes restless.

![NoIRvIR.jpg](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-22945-270329/1600-899/NoIRvIR.jpg)

> _A Standard camera versus the NoIR V2: Night and Day_

For this project I opted to connect the Raspberry Pi to a standard network. Setting up WiFi can be done using terminal, but it's much simpler to connect an HDMI monitor and use the Raspbian desktop environment. Set up the Raspberry Pi to use a WiFi network like normal, with the networking icon in the task bar. To make it simpler to find the video stream later, right click on the icon and set the wireless interface to use a static IP address.

### Casing it out

Crafting a case and mount for this project presents some challengers. It needed to be flexible to allow the camera to be positioned to get a good shot of the baby while it sleeps.

Like all of the camera modules, the NoIR camera connects to the Raspberry Pi with a 16mm wide ribbon cable. Initially I had the idea to put the camera on the end of a short flexible pole with the Pi in a case at its base. This had a problem - having a small thing sticking out that a baby could fit in its mouth isn't a good idea. I had to keep the unit big enough to not present a choking hazard. The best way to go about it was to integrate the camera and the Raspberry Pi together in a case and pivot the whole unit to get the correct angle.

I used a hinged plastic mount designed for attaching a GPS to a cars windscreen. Attached to this is an official Raspberry Pi 3 case, mounted upside down. I drilled a hole inside the lid of the case and used mounting tape to secure the camera module on the inside, letting the lens slightly poke out. The short ribbon cable flexed around to the socket on the Raspberry Pi. I also drilled holes and mounted two of these Infrared LED's in the lid. I combined them in series and added the appropriate resistor and used female jumper leads to connect them to the 5v terminal on the GPIO header. It can be a tight fit under the lid, so it is important to be careful that no leads touch any other pins or the main board of the Raspberry Pi.

![Case1.jpg](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-22945-270328/Case1.jpg)

The hinged mount is attached to a wall with adhesive picture frame pads - I didn't want to use suction cups as they can be unreliable for long term use. The case with the camera inside is then facing downward from the wall over a babies crib, and the hinge can be adjusted to get an optimal viewing angle.

### Coding

To get the baby monitor system up and running I experimented with a few coding options. Python has extensive libraries for interfacing with both the standard and NoIR camera modules, including network streaming options. While coding for the camera in python is extensively customizable, I found that using the server socket transmission commands had significant latency issues when streaming an HD feed over a network. The camera can also be interfaced with by using standard Linux terminal commands and scripting. It's efficient for basic functionality, but isn't very well suited for a complex program like what is required for this project.

The solution I opted to use is the [RPi Cam Web Interface suite](https://www.element14.com/community/external-link.jspa?url=http%3A%2F%2Felinux.org%2FRPi-Cam-Web-Interface). It is very flexible with configuration, but importantly it streams live video over a standard web interface - making it compatible with just about any smart device with a web browser. It also allows the Raspberry Pi to be shut down correctly with a button on the web interface. I didn't bother to put security on the video stream because it'll only be viewable on an encrypted WiFi network. The RPi Cam Web Interface does, however, support password prompt access and a range of permissions.

Before installation the camera needs to be enabled inside of Raspbian. Under Preferences in the main menu load the Raspberry Pi Configuration program and set the camera option to enable. With the camera enabled, installing the Interface software is done by pasting the following lines into a terminal window.

After that you'll see a dialog box with some options. Unless you have specific requirements, hit Enter to start the installation with the default settings. After it has rebooted accessing the software is done by entering the IP address of the Raspberry Pi into a browser. This can be done on the Pi itself or on any device connected to the same network.

![Screen Interface](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-22945-269924/screeninterface.jpg)

I played around with the video resolution, bitrate and framerate setting to get optimal performance over a wireless network. Devices like this are often placed far away from the router and through a few walls, so signal strength may not be the best.

  * _Video res: 720x1280_ \- I found the sweet spot in resolution to be 720p HD. Opposite to what is normal, I used a vertical 720x1280 video frame to fill the screen of a smart phone when used in portrait mode.
  * _Video fps: 20_ \- The default 25 frames per second is somewhat overkill for observing a baby that isn't moving very much while sleeping. Bumping the frame rate down to 20 still allows viewers to see if the baby is moving but slightly relaxes the demand it places on the wireless network.
  * _Brightness: 60_ \- Increasing the brightness does wash out the picture a little, but gives more clarity in low light.
  * _Exposure Mode: nightpreview _\- The NoIR V2 is good in low light, but turning the exposure to nightpreview cleans up the image just a little more.
  * _Image Quality: 100, Preview Quality: 100_ \- Maxing out the image quality and preview quality didn't seem to have any impact on the streaming performance, but made the overall clarity just a little better. Setting the preview width to 720 allows the live video to be the full quality captured.
  * _Motion detect mode: External_

I changed the default on screen title to something a bit more appropriate - Baby Cam. I left the complete hours, minutes and seconds time stamp there. Having the seconds constantly counting gives a good indicator that the video feed is live and hasn't malfunctioned.

There are some settings I had to change manually outside of the web based UI, done by editing the file _/etc/raspimjpeg_.

  * Adding the line '_fullscreen true_' to the bottom of the file. This makes the Index page of the camera interface default to full screen video, rather than showing the option buttons.
  * Changing the pre existing line _motion_detection_ from _false_ to _true_ makes the system start motion detection automatically at boot.

### Motion sensing

I implemented a system to send alerts when the baby starts to get restless during nap time. The RPi Cam Web Interface has integrated motion sensing algorithms that are well suited to detecting both subtle and more obvious motion. I tuned through trial and error and ended up with the following settings, configured under the 'Edit motion settings' button on the default index page.

  * _On_event_start: python /etc/home/pi/alert.py_ \- When motion is detected the named python script will be executed to send out an alert.
  * _Threshold: 2100_ \- This is a tricky one. The motion detection sensitivity is defined by a number between 1 and 2147483647. Every use and scenario is different depending on the sensitivity required. Having the number too high results in it being triggered with no perceivable motion at all. 2100 seemed to work well for me.
  * _Lightswtich: 55_ \- Useful when the baby sleeps with the curtains slightly open on an overcast day. This option stops the sun moving out from behind clouds resulting in a false trigger due to the change in lighting.
  * _Minimum_motion_frames: 3_ \- The number of consecutive frames that motion needs to be present before the sensor is tripped. A baby doesn't move like The Flash, so having it a little higher than 1 gives less false triggers.

Under the schedule settings I cleared the boxes under Motion Start and Motion Stop. These are used when recording is to start when motion is detected. For a baby monitor a live alert is required, not a video recording.

Unfortunately the motion service can have complications when executing some commands. Searching around, I found that it was a bug that many users have encountered with no great solution. If you find that the alert script isn't executing, starting the motion program out of daemon mode from the command line makes it function properly. It's a work around rather than a solution, but it can be automatically done every time the Raspberry Pi boots. Edit _bashrc_ via the command '_sudo nano .bashrc_' and add the line 'motion -n' to the bottom of the file and the problem should be avoided.

### Sending alerts

I used the _on_motion_start_ parameter to trigger and execute a python script that sends out notifications. There is a range of different providers that offer applications on iOS and Android to receive notifications from inside a python script. I used Instapush, although other services work equally as well. Using it is done by signing up on their website, creating a new application then pasting the provided code with the unique appid and secret code parameters into a python script.

The Instapush API also needs to be installed on the Raspberry Pi, done simply with the following line in a terminal window.

I placed this script in the default _/home/pi _directory and named it '_alert.py_'.

  1. if input_state == Falseand os.path.isfile('active') == False: 
  * Lines 1 through 4 import the necessary modules for the script.
  * Line 5 - 7 sets the numbering system for the GPIO pins on the Raspberry Pi, selects a pin number and sets it up for use as a switch trigger then gives it the variable '_input_state_'.
  * Line 8 is a if statement to check two conditions:
    1. If the switch attached between GPIO pin 4 and a ground pin is active. I put a jumper to bridge pin 4 to the neighbouring ground pin. Removing the jumper disables the notifications from being sent.
    2. If a file named '_active_' is in the current directory. This is part of the method used to ensure that notifications are only sent once every 10 minutes to prevent a huge flood of alerts being sent consecutively.
  * Line 9 creates a blank file titled '_active_' in the current directory.
  * Lines 10 and 11 are the Instapush provided code to trigger the sending of notifications.
  * Line 12 waits for 600 seconds, or 10 minutes.
  * Line 13 deletes the file '_active_'.

### ![OnTheWall.jpg](https://www.element14.com/community/servlet/JiveServlet/downloadImage/38-22945-270331/1563-899/OnTheWall.jpg)

### Final thoughts

The NoIR V2 camera is a great way to get clear images in low light situations, and the increased fidelity with the V2 makes for great quality images and videos. Outside of just monitoring sleeping babies, combining the Interface, the NoIR camera and a Raspberry Pi 3 together can make a very sophisticated security camera system. More than sending alerts, a relay could be added to the system to sound an alarm, turn the lights on in a room or lock a door with a solenoid. Nearly anything that a Raspberry Pi can do is able to be triggered by detecting motion. Plus the whole unit is smaller and cheaper yet higher fidelity than many commercial surveillance systems. Combining it with a big source of Infrared light, such as an array of LED's or a large bulb, the NoIR V2 camera could view a large area in absolute darkness.

If you have any questions about this project or the NoIR V2 in general, leave them in the comments below or hit me up on Twitter - [@aaronights](https://www.element14.com/community/external-link.jspa?url=http%3A%2F%2Ftwitter.com%2Faaronights).

  

* [ 2 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ 2000 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ 2015 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ 3d_printing ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ actuators ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ adafruit ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ aeronautics ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ airplay ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ analogue_inputs ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ animated_grim ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ apache ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ arcade_machine14 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ architecture ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ art ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ attiny ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ audio_sensor ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ b+ ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ battery_power ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ biology ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ boiler ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ build ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ bundle ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ cabeatwell ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ camera ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ cases ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ chemistry ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ communication ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ complete ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ computing ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ control ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ controller ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ cooking ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ decoration ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ display ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ diy ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ dl-fldigi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ doors ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ drinkmotizer ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ driving ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ dwinhold ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ dyoung ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ ebook ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ economics ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ education ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ educational ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ electric ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ electronic ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ element14 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ email ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ epaper ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ fan ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ file_server ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ finance ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ flying ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ foginator ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ foginator2000 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ fuel-cell ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ geexbox ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ gpio ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ gqrx ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ graphing ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ gsm ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ hab ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ halloween ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ halloween15 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ halloween2015 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ halloween_2014 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ halloween_2015 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ hat ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ heat_sink ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ heatsink ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ hmi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ home ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ home_security ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ hub ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ hydrogen ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ idea ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ iluvpi2 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ imac ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ infrared ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ init.d ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ internet ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ internet_of_things ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ iot ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ java ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ lamp ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ languages ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ lcd ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ light_sensor ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ lighting ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ linux ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ management ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ mechanical ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ medical ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ microphone ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ minecraft ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ mod ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ motion_sensor ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ motor_control ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ music ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ networking_and_servers ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ new ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ news ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ noir ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ noobs ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ ntx2 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ nursing ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ nutrition ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ oled ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ openelec ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ or ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pack ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ party ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pharmaceutical ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ phone ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ physics ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi hat ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi2 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi2candydispenser ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi_noir ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi_sun ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pi_zero ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ picam ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pieintheface ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ piface ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ piface_control&display ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ piface_digital ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pinoir ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ police ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ power_monitoring ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ project ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ projects ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pumpkinpi2015 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ pumpkinpi_2015 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ python ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rapiro ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rasberrypi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberry ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberry pi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberry-pi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberry_pi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberry_pi_2 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberrypi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspberrypi2 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ raspbian ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ relays ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ roadtest ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ robot ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ robot_arm ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ router ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpi cooling ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpi3 ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpibeg ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpibeginner ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpiexpert ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ rpiintermediate ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ santa_catcher ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ science ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ science_and_technology ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ screen ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ security ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ sense ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ sensor ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ sensors ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ serial ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ server ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ servo ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ soldering ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ stem ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ tech ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ tech_art ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ temperature_sensor ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ the ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ torrent ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ touch ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ trick ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ trivia ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ tutorial ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ twitter ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ uav ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ ultimate ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ ultimate_road_test ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ usb ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ valentine_pi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ vehicles ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ vncserver ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ vpn ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ water ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ weapons ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ web_server ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ webcam ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ wi-pi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ wifi ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ wireless ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ xcore ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ xmos ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ xmos_startkit ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
* [ year's ](https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/tags)
