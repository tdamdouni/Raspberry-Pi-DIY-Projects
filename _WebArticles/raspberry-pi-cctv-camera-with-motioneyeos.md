# Raspberry Pi CCTV Camera with motionEyeOS

_Captured: 2017-08-08 at 17:57 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2017/04/raspberry-pi-cctv-camera-with-motioneyeos/)_

![motionEyeOS Logo and Pi Camera](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2017/04/pi_camera_module_motioneyeos_logo-702x336.jpg)

As I progressed with my original security camera project I realised that I was making slow progress and I would struggle to complete the software in a sensible time-frame.

So I decided to simplify everything. A lot. I settled on motionEyeOS as the basis of my system and install just the hardware I needed. If in the future I wanted to add anything else I could do so but my priority was to get something working within a few weeks. It was time to stop designing and start making with what I had not what I thought I might need. This post described what I ended up with.

The camera looks out over my drive and stores photos and video on the SD card which is inside my garage.

A wireless connection and some router settings allow these to be viewed over the internet using the motionEyeOS web-interface.

Magnetic switches monitor the state of the garage doors and these are shown in the interface.

## Internal Hardware

This is a list of components that were mounted or positioned inside my garage :

The 75cm camera cable allowed me to mount the Pi inside the garage while having some slack for making connections at either end. I used the 3m USB cable to get the WiFi adapter as close to my router as possible.

## External Hardware

This is a list of hardware mounted on the external wall next to my conventional security light :

  * Evatron IP67 ABS (DE Series) 80x73x53mm junction box
  * Pi Camera v1.2
  * 3D printed cylinder camera mount
  * 73mm length of 3mm threaded bar
  * 2x 3mm nyloc nuts
  * 4x 2mm nylon bolts with nuts
  * 1x 8mm metal washer

The junction box was weather proof and came with a clear lid. This made it suitable for mounting a camera in. The camera was mounted with two 3D printed components and some 2mm nylon bolts. These components are detailed in the [Pi Camera 3D Printed Cylinder Mount](http://www.raspberrypi-spy.co.uk/2016/08/pi-camera-3d-printed-cylinder-mount/) and [Pi Camera 3D Printed Magnetic Lens Mount](http://www.raspberrypi-spy.co.uk/2016/08/pi-camera-3d-printed-magnetic-lens-mount/) articles.

The cylinder fits inside the enclosure and pivots on a 3mm threaded bar. Two drilled holes in the side of the enclosure allow the threaded bar to be secured with 3mm nyloc nuts. The cylinder was rotated to adjust the tilt of the camera and the nuts tightened to lock it in position.

The back box was sprayed black inside and out and mounted on a piece of wood. The ribbon cable leaves the back of the box, is routed through a slot drilled into the wood and slips into the garage roof.

## motionEyeOS SD Card Creation

Although my original plan was to write my own software I realised motionEyeOS was going to get me 90% of what I wanted with almost no effort and it's really easy to setup.

motionEyeOS is available for a number of different hardware platforms but I downloaded the image compatible with the "Raspberry Pi 2".

  * Extracted the img file from the archive

On Windows I used 7-zip to extract the image from the archive. Take a look at the [motionEyeOS installation instructions](https://github.com/ccrisan/motioneyeos/wiki/Installation) for more information.

## motionEyeOS Initial Setup

With the SD card created the system was setup using the following steps :

  * Connected Pi camera using suitable ribbon cable
  * Connected WiFi dongle
  * Connected Ethernet cable
  * Inserted the SD card
  * Powered-up the Pi
  * Left for 3 minutes while it did first-boot configuration

Using my router's admin interface I found out the IP address the Pi had been given on the network. Putting this IP address into a browser address bar I could now access the motionEyeOS web interface.

## Essential motionEyeOS Settings

There are lots of settings you can change. The default values are a good starting point but the first settings I changed were the "admin" and "user" passwords.

Clicking the "person" icon brought up the login box:

The default username is "admin" with a blank password. This allowed me to open the settings panel using the other icon. The next thing I changed was to enable "Advanced Settings" and set passwords for the "admin" and "user" users. Clicking the "Apply" button saved these settings.

## Setting Up WiFi

Within the interface and with "Advanced Settings" enabled you can configure Wireless options within the "Network" panel.

If you want to use WiFi without first using Ethernet you will need to follow the [Manually setting up Pi WiFi using wpa_supplicant.conf](http://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/) guide.

## Other motionEyeOS Settings

The following are settings I tend to change from the defaults. Hovering over the little "?" icon next to a setting will give you a short description of what it does.

### > Preferences

As motionEyeOS can support more than one camera you can display their feeds in a grid. With only one camera connected I changed these settings :

  * Layout Columns = 1
  * Layout Rows = 1

### > Expert Settings

As my system used a Pi 2 :

  * Enable CSI Camera Led = OFF
  * Overclocking = Pi2

### > Video Device

  * Camera Name = "Garage"
  * Video Resolution = 1600×1200
  * Frame Rate = 2

If your camera is mounted upside-down you can use the Video Rotation setting to rotate the image. I use this setting with a value of 180. You may also want to experiment with different video resolutions. Bigger is better but higher resolutions will create bigger images and these will take longer to shift over your network/mobile connections. Finding the ideal resolution is a balancing act between quality and performance.

### > Video Streaming

These settings allow you to adjust the properties of the image streamed to the browser. These may require adjusting depending on the performance of your network and/or internet connection.

  * Streaming Frame Rate = 1
  * Streaming Image Resizing = ON
  * Streaming Resolution = 50%
  * Motion Optimization = ON

The image resizing allows the stream to use a lower resolution than the resolution set under "Video Device". A low frame rate reduces the data-rate but still allows you to see what is going on in the scene.

### > Still Images

  * Preserve Pictures "For One Month"

### > Movies

  * Movie Format = H.264 (.mp4)
  * Preserve Movies "For One Week"

### > Motion Detection

You will almost certainly need to experiment with these settings depending on where your camera is and what it can see :

  * Frame Change Threshold = 10%
  * Light Switch Detection = 75%
  * Motion Gap = 20
  * Captured Before = 5
  * Captured After = 5
  * Minimum Motion Frames = 10
  * Show Frame Changes = ON

## Viewing Images and Movies

To view images and movies click on the camera image and use the icons that appear in the top right.

You will then be presented with a gallery of images that you can click on :

Time-stamps are shown so you can see when the media was created. The gallery takes longer to load if there are more images. Play around with it and you will get a feel for how it works.

## Fixed IP Address

To make it easier to find the web interface in the future I like to give my cameras a fixed IP address. The IP address was specified in the Network settings :

## Access from the Internet

In order to access the camera from the internet I setup "port forwarding" in my router settings. This varies depending on the router you have so you will have to use the user manual or Google. Generally you define a port to use and tell your router to forward it to a specific IP address on your network. You then access the camera using your external IP address with the port number after it. To find your external IP address Google "what is my ip". If your external IP address was 12.34.56.78 and your chosen port is 30000 you would access the camera using http://12.34.56.78:30000. Your router settings would forward traffic to port 30000 to the IP address of your camera (in my example 192.168.1.41).

You can then use the next port in the sequence for additional cameras if you have them.

## Door Monitoring

In order to monitor the state of the two garage doors I used magnetic sensors and a motionEyeOS "monitoring" script. The monitoring script displays the state of the doors overlaid on the camera output and can be seen as "D1:SHUT D2:SHUT" in the screenshot above.

This technique will be described in a future blog post.

## Pushover Notifications on Reboot

As I wanted to access the camera over the internet I needed a way of knowing what my external IP address was while I was away from the house. I setup "Pushover" notifications that give me a link to my camera. These are sent to my Android Smartphone and provide a link to the camera with the correct IP address and port number. I can then click the link and view the motionEyeOS interface in a mobile browser.

Pushover is a fantastic service that lets you send notifications to a phone using a range of programming languages. On Android you pay for the app but the service is then free.

I will be writing a blog post to explain how I set this up in more detail.

## Final Thoughts

This system has been running for months 24/7. I don't have to spend much time messing around with it and it just tends to work. It was the inspiration to [create my garage camera with a Pi Zero W](http://www.raspberrypi-spy.co.uk/2017/04/raspberry-pi-zero-w-cctv-camera-with-motioneyeos/).

motionEyeOS is really an amazing bit of software. It's easy to use and adds a whole world of possibilities to the Raspberry Pi. Thank you [Calin Crisan](https://github.com/ccrisan) for your hard work!

Here are some motionEyeOS links that are worth visiting for additional information :

All my motionEyeOS based projects are listed under [the motionEyeOS tag](http://www.raspberrypi-spy.co.uk/tag/motioneyeos/).
