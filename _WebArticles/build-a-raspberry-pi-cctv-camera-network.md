# Build a Raspberry Pi CCTV camera network

_Captured: 2017-05-06 at 16:13 from [www.techradar.com](http://www.techradar.com/how-to/build-a-raspberry-pi-cctv-camera-network)_

![](http://cdn.mos.cms.futurecdn.net/kQpc3tmEbFYgBfyvexCcK8-320-80.png)

Viewers of Crimewatch UK will be familiar with the grainy images of suspected criminals in off-licences and jewellery shops across Britain. Members of the public are asked to come forward and identify someone's face from an image that looks like it's been smudged with a calloused thumb.

This is particularly hard for people used to viewing videos on YouTube and Vimeo in crisp HD. As much as we all would like to do our civic duty and bring people to justice, this is hard without buying a state of the art CCTV system and having sufficient storage space for high-quality video.

Until now, this has been beyond the reach of the average person but since the invention of the [Raspberry Pi](http://www.techradar.com/reviews/pc-mac/pc-mac-desktops/raspberry-pi-3-1316838/review) and inexpensive HD webcams, it's perfectly possible to network several Raspberry Pis into a state of the art security system at a fraction of the usual cost.

![](http://cdn.mos.cms.futurecdn.net/jmvUCYFwFEDLt44Yut5sp7-320-80.jpg)

> _With a matte-black finish that would put bakelite to shame, the fish eye lens also allows a 180 panoramic view_

### Planning your layout

The requirements for this project are fairly minimal. It's helpful, initially, to sketch out what set up you want. You may wish, for instance, only to have a single camera above your front door so you can see who is outside each time the doorbell rings.

Alternatively, you might want multiple cameras dotted around the place for you to survey from up on high in your hermetically sealed bedroom.

Once you have planned a basic layout for your security camera network, you will have an idea of the equipment you'll need.

The most sensible setup is to have a Raspberry Pi 2 or 3 as your central computer for viewing the camera feeds and storing footage and a Raspberry Pi Zero with camera for each additional area you want covered by CCTV. You should also pay careful consideration to your casing.

One excellent and easy setup is to use the Pi Camera Bundle from [ModMyPi](https://www.modmypi.com/) . Note: you may recognise these as Nwazet products but they've been rebranded as ModMyPi.

The bundles come with a special case for a Raspberry Pi B+/2/3 made from acrylic and include a fisheye lens for a panoramic view. It has a neat magnetic connector that enables you to connect the Pi camera to the lens and snap it into place.

If you're handy with a drill and rawl plugs, the casing also comes with screws so it can be mounted to a wall. If you are more of a hobbyist, it's also possible to pick up fake CCTV cameras from your local bargain bin and place your Raspberry Pi inside, though naturally you'll need to drill holes to allow entry of the power cable and find your own way to mount the Raspberry Pi camera.

On the subject of cameras, there are several options. The Nwazet casing is designed to work with the official Raspberry Pi Camera. Version 2 of the Camera module, which was released back in April 2016, is a staggering improvement on the original.

It uses a Sony IMX219 8-megapixel sensor and therefore has no trouble recording HD videos and photos.

It can be attached to the CSI port on your Raspberry Pi in a couple of minutes. If the area you want to monitor is poorly lit, you may want to consider using the Pi NoIR infrared camera module which does everything the standard camera module does but allows the camera to see in the dark with infrared.

For those on a shoestring, the Raspberry Pi also supports a number of USB webcams although this can be very much trial and error. For the purposes of this tutorial, a [Microsoft HD-3000 USB webcam](https://www.amazon.co.uk/Microsoft-LifeCam-HD-3000-Webcam-Packaging/dp/B0099XD1PU/ref=sr_1_1?ie=UTF8&qid=1481556840&sr=8-1&keywords=Microsoft+HD-3000+USB+webcam) was attached to a Raspberry Pi Zero to work as an additional camera and worked out of the box, with some help from a USB OTG cable.

If you decide to keep costs down and use a Raspberry Pi Zero for additional security cameras but still want to use the official Raspberry Pi or Pi NoIR camera modules, bear in mind the camera port is smaller on the Zero. Luckily, you can buy a camera adaptor cable from the [Pi Hut](https://thepihut.com/).

The easiest way to access additional cameras is over a wireless network, and it makes sense to have a Wi-Fi dongle for each Pi-camera you want. The Pi 3 comes with its own Wi-Fi chip.

![](http://cdn.mos.cms.futurecdn.net/tKsepgZYjWznHdguZeLEq7-320-80.jpg)

> _Not only can the Pi NoIR see in the dark, it comes with a blue gel for monitoring the health of your plants_

Naturally, each Raspberry Pi will also need a microSD card to store the OS. For your principal Raspberry Pi which will run the security software, you may also wish to attach external storage such as a USB stick to have plenty of space for photos/footage.

A final consideration before beginning your set up is placing your Raspberry Pi security cameras so that they are near to a power supply. If you want to place one in a particularly hard to reach location, either run a power line there or use a rechargeable battery pack.

![](http://cdn.mos.cms.futurecdn.net/UXTBGLXibrPfWHdSdVGcq7-320-80.jpg)

MotionEyeOS supports multiple security cameras which will allow you to monitor a number of areas at once. If you're using the official Raspberry Pi Camera Module or the Pi NoIR, then simply follow steps 1-3 in the walkthrough on the next page to install MotionEyeOS on the additional Raspberry Pi and add the video stream on your main Raspberry Pi.

To set up a Raspberry Pi with a USB camera, then read on. First, set up your extra Wi-Fi-enabled Raspberry Pi with a clean install of Raspbian but don't connect your USB camera just yet.

**stream_localhost = ON**

Use Ctrl+x to exit and save your changes. Next, run the command sudo nano /etc/default/ motion to open the config file then scroll down and change **start_motion_daemon = no** to 'yes' . Now connect your USB camera to the Raspberry Pi. You can run the **lsusb** to make sure the Raspberry Pi can detect it. Next, start the motion service with sudo service motion start .

You can test that streaming is working by opening a web page on any device and visiting http://192.168.x.x:8081 where 192.168.x.x is the IP address of your Raspberry Pi. Finally, you will need to add the camera stream in the MotionEyeOS admin panel by clicking on the dropdown box at the top left and choosing 'add camera'.

### I spy with my MotionPie 

[MotionEyeOS](https://github.com/ccrisan/motioneyeos) (formerly named MotionPie) is a customised OS for your Raspberry Pi, which will turn it into a CCTV system out of the box.

The basic steps for setting it up are outlined over the page. Once installation of the OS is complete, all you need is the IP of your Raspberry Pi to be able to log into the handy web interface.

You can obtain this from logging into your router or if you have an Android phone, install the handy app Fing from the Google Play Store which will list the IP address of all devices connected to your network.

Next, use the device of your choice to go to this IP address. If you are asked to log in, use username 'admin' and leave the password field blank. The user interface is very slick and intuitive.

If you have a supported camera connected, then the feed from this will show right away. For the sake of security, click on the Settings icon at the top left, enable Advanced Settings and set an admin password to make sure no one else has access.

Next, it's worth expanding the Network tab and entering the name and password for your wireless network. This is necessary if you wish to add other cameras to your system.

Once your camera has been added, the Video Device tab can be expanded to change some of the default settings. This is where you can name your camera to something more illuminating than 'Camera 1' such as 'Front Door.' You can also alter the resolution of the camera.

Experimentation with a Raspberry Pi 3 showed that a resolution of 800x480 and a framerate of 30 is an excellent trade-off between speed and avoiding traditional blurry CCTV video quality.

The Video Device tab also has a handy rocker switch for 'Light Switch detection' to only start recording when lights are switched on. 'Automatic Brightness' can also be enabled to allow the Raspberry Pi to set the brightness level though it's best to set this yourself as the automatic feature can be quite erratic.

If you favour crisp black and white footage, saturation can also be set to zero. The File Storage tab stipulates where any photos or video footage are stored. If you have an external drive, enter the path to it here, as the microSD card will fill up quickly.

Fortunately, MotionEyeOS also tells you how much storage space is available. There are also options to add more cameras and specify under which conditions the camera is to record.

The Video Streaming section is the most useful if you want information on how to view the camera's footage passively. The 'Streaming URL' will provide a link to the camera feed without the control panel, so make sure to note this down.

If you wish to embed the live stream inside a web page there's also an embed URL. You can also click on the 'Footage' button for each camera from within the Admin interface to see all movies/pictures recorded by that camera.

  
![](http://cdn.mos.cms.futurecdn.net/23DtYpE9AUesQnAW5t8sp7-320-80.jpg)

You can configure how, when and where the camera records footage using the MotionEyeOS Control Panel. The 'File Storage' tab can be used to specify the path to your external drive. You can also choose to upload media files to Google Drive or Dropbox. Next, head over to the General Settings tab and switch on the 'Advanced Settings'. Work your way down to the Video Device tab to fine tune the settings. Choose a video resolution and frame rate. You may need to use trial and error to make sure the quality is consistent.

The Motion Detection tab has the option to 'Show Frame Changes' meaning that any movement will be highlighted in red. Here you can also alter the Frame Change threshold and 'Minimum Motion frames' to determine movement sensitivity. Both the Still Images and Movies tab have a rocker switch to the left to turn them on or off and both are enabled by default.

The 'File Name' box in both tabs allows you to specify a file name beyond the time and date.

The Capture Mode on both tabs also allows you to choose between recording only when motion is detected (default) and recording continuously. Finally, if you're concerned about storage space, the Preserve drop-down tab allows you to delete media files after a certain length of time.

Once your Raspbery Pi Camera network is up and running, it's essential to follow some simple steps to keep it secure.

As with installing any camera system, make sure the cameras are covering only areas where you have permission to record- in the UK this is any public area.

A sign warning visitors they are on candid camera is the courteous thing to do. Should anything happen to the principal camera running MotioneyeOS or its storage device, then any footage that you have captured will be lost, so do keep this in a secure location.

If your system is set to record video when motion is detected, bear in mind that the framerate can slow down, so if detail is important in your images, it may be better to have your cameras take a series of still images instead.

Although it's technically possible to have more than one camera connected to the same Raspberry Pi e.g. the official Raspberry Pi Camera Module and a USB camera, this will place more strain on the Raspberry Pi and reduce video quality. It's far better to have one Raspberry Pi per camera if you can afford to do it.

If you don't relish the prospect of drilling into brick walls to mount cameras, you may want to try use velcro strips instead. This is particularly useful indoors as it's simple both to install the cameras and move them around.

By default, MotionEyeOS only allows you to view your camera feeds while connected to your home network. If you're going to be away, open the admin panel and expand the Motion Notifications tab.

![](http://cdn.mos.cms.futurecdn.net/9Mf2VyGV5o7tNwNLhqRiq7-320-80.jpg)

> _Serving suggestion : Use velcro to place your Pi. It's inexpensive so although it can be ripped off, you won't be. Why not?_

There are settings here to upload your media files to a web service, such as Google Drive, when movement is detected inside your property. You also have option to set up web hook notifications or even to run a Python script.

This opens up the possibility to interface MotionEyeOS with servos to lock all your doors or link it with speakers to sound an alarm.

### Set up your security camera network

### 1\. Download MotionEyeOS 

![](http://cdn.mos.cms.futurecdn.net/kZ8UKxh6muuCrXaJyR6Bq7-320-80.jpg)

First, you will need to [download the MotionEyeOS IMG file](https://github.com/ccrisan/%20motioneyeos/releases). Make sure it's the correct version for your particular Raspberry Pi.

Once that's done use your favourite archiving tool to extract the .img file. Follow [these Windows instructions](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md) to install the Image to a microSD card.

### 2\. Install MotionEyeOS to SD card

![](http://cdn.mos.cms.futurecdn.net/rUFavKpBMzdQuhEQtXwLm7-320-80.jpg)

If you're on Linux, insert your microSD card. Use **cd** to navigate to the MotionEyeOS IMG file, then run the following:
    
    
    sudo dd bs=4M if=nameofyourmotioneyeosimagehere.img of=/dev/sdx

You'll need to substitute /dev/sdx for the correct path to your microSD card e.g. /dev/sdb.

### 3\. Find your Raspberry Pi's IP addres

![](http://cdn.mos.cms.futurecdn.net/XyYxHFv2RqhCEXA8sRRPm7-320-80.jpg)

Safely remove the microSD card and insert into your Raspberry Pi. Connect the Raspberry Pi to your router via Ethernet cable.

To connect to the Raspberry Pi, you'll need to find its IP address. The easiest way to do this is by using a mobile app such as Fing , which is available for [Android](https://play.google.com/store/apps/details?id=com.overlook.android.fing&hl=en_GB) and [iOS](https://itunes.apple.com/gb/app/fing-network-scanner/id430921107?mt=8). It will list all devices in your network.

### 4\. Adding cameras to MotionEye OS 

![](http://cdn.mos.cms.futurecdn.net/usiyCmJfvGgTT3SiybfWm7-320-80.jpg)

In any web browser enter the IP address of your device, using port 80 e.g **http://192.168.1.20:80**. This will take you to the login screen.

The default username is admin and the password is blank. You'll be asked to click to add a camera. Choose the correct type of camera under 'Camera Type' and click 'OK'.

### 5\. Configure the camera

![](http://cdn.mos.cms.futurecdn.net/RwY83Nret8Mw6TGHtcZVm7-320-80.jpg)

You're now logged into the admin control panel for MotionEyeOS. Head over to the 'General Settings' tab and expand to set an admin password.

Under the 'Video Device' tab you can also set a new name for the camera e.g 'Living Room'. Click the orange 'Apply' button at the top to save your changes.

### 6\. Adding additional cameras

![](http://cdn.mos.cms.futurecdn.net/VUUT2NFWoCmhsxybZjSEm7-320-80.jpg)

If you have previously set up any other cameras on MotionEyeOS, you can now add them to the main feed easily enough.

Click on the dropdown box at the top left and choose 'add camera'. Repeat the previous step 5 to rename each camera according to its location e.g 'Upstairs Cheese Overflow Storage'

  * Enjoyed this article? Expand your knowledge of Linux, get more from your code, and discover the latest open source developments inside Linux Format. [Read our sampler today and take advantage of the offer inside.](http://issuu.com/futurepublishing/docs/lxf204.sampler_tr?e=1191357/31271343)
