# Raspberry Pi Zero W CCTV Camera with motionEyeOS

_Captured: 2017-05-25 at 13:27 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2017/04/raspberry-pi-zero-w-cctv-camera-with-motioneyeos/)_

![](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2017/04/pi_zeroview_camera-1078x516.jpg)

After the successful deployment of my first motionEyeOS Pi security camera last year I was keen to get another setup. I wanted to use a Pi Zero W so I could mount it inside my conservatory using a Pi Hut "ZeroView". This is a mount for the Pi Zero that lets you stick a Pi camera to a glass window.

motionEyeOS makes it so easy to setup a security camera and the difficult bit is usually the practicality of physically mounting it all. By using the ZeroView mount even this stage can be straightforward. The Pi Zero W would also allow me to put the camera in a place where I had no Ethernet available.

The following instructions explain how to quickly create a motionEyeOS based CCTV camera with a Pi Zero W.

## Hardware

The components you will need for this project are :

  * Raspberry Pi Zero W (or Pi Zero with WiFi dongle)
  * Official Pi Camera
  * Camera ribbon cable
  * Pi "ZeroView" camera mount
  * Official 5V power supply

I chose a standard camera rather than the Pi NoIR version as I've got standard motion activated flood lights which can provide illumination at night.

You can use a different sized SD card but I think 16GB is a good starting point.

## Step 1 - Download motionEyeOS SD Card Image

motionEyeOS is available for a number of different hardware platforms. For the Pi Zero you need to download the image compatible with the "Raspberry Pi 1" rather than those available for the Pi 2 and Pi 3.

  * Extract the img file from the archive

On Windows I used 7-zip to extract the image from the archive.

## Step 2 - Configure Wireless

This is a crucial step when using the Pi Zero W. In order to configure the Wireless without messing about with monitors and keyboards you can configure it manually. To do this you need to add a text file to the boot partition on the SD card named "wpa_supplicant.conf". Instructions for creating the wpa_supplicant.conf can be found in the [Manually setting up Pi WiFi using wpa_supplicant.conf](http://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/) tutorial.

Pay careful attention to this step as a mistake can result in the Pi Zero failing to boot. You may need to re-write the SD card and start again in order to get a network connection.

## Step 3 - Assemble Components

Next you should assemble the components :

  * Attach Pi and camera to the ZeroView mount
  * Insert microSD card
  * Attach ZeroView to window
  * Connect power supply

## Step 4 - First Boot

Once everything was connected turn on the power. During the first boot the system performs some configuration so is best left for a few minutes.

Assuming the Pi has connected to your WiFi you need to find its IP address. You can either look in your router admin interface or use an IP scanner. "[Angry IP Scanner](http://angryip.org/download/)" is suitable for this and is available for Windows, Linux and Mac.

Once you have the IP address you can enter it into the address bar of your browser to load the motionEyeOS web interface. With any luck you should see the output of your camera :

The icon in the top left can be used to open the settings side panel. Click the "person" icon to login :

Use "admin" as the username and leave the password blank. Click "Login" and you can now access the settings side panel.

## Step 5 - Settings

Under general settings you should set passwords for "Admin Password" and "Surveillance Password". I usually change the default "Camera Name" to something more unique and this is particularly useful if you have more than one camera.

Click the "Apply" button to save these changes.

## Step 6 - Advanced Settings

By setting "Advanced Settings" to "ON" and clicking "Apply" switch you can enable a lot of useful extra settings :

These include the ability to :

  * change the Time Zone
  * change the Hostname
  * check for updates
  * Shutdown
  * Reboot

## Step 7 - Other Settings

The following are settings I tend to change from the defaults.

### > Preferences

As motionEyeOS can support more than one camera you can display their feeds in a grid. With only one camera I change these settings :

  * Layout Columns = 1
  * Layout Rows = 1

### > Expert Settings

As we are using a Pi Zero :

  * Enable CSI Camera Led = OFF
  * Overclocking = PiZero

### > Video Device

  * Camera Name = "Garden"
  * Video Resolution = 1600×1200
  * Frame Rate = 2

If your camera is mounted upside-down you can use the Video Rotation setting to rotate the image. I use this setting in my Garage camera. You may also want to experiment with different video resolutions. Bigger is better but higher resolutions will create bigger images and these will take longer to shift over your network/mobile connections. Finding the ideal resolution is a balancing act between quality and performance.

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

## Step 7 - Fixed IP Address (Optional)

To make it easier to find the web interface in the future I like to give my cameras a fixed IP address. The IP address can be specified in the Network settings :

## Step 8 - Viewing Images and Movies

Now the camera is up and running you just need to sit back relax.

To view images and movies you can click on the camera image and use the icons that appear in the top right.

You will then be presented with a gallery that you can click on.

Timestamps are shown so you can see when the media was created. The gallery takes longer to load if there are more images. Play around with it and you will get a feel for how it works.

## Final Thoughts

I am very impressed with motionEyeOS and it does almost everything I would expect. It's easy to setup which allows more time to worry about mounting the camera. It is the main reason I decided to not continue creating my own software.

It is worth experimenting with the settings (resolution, motion detection percentages etc) to get the best performance for your location given the number of detection events you are likely to get on a day-to-day basis.

It's worth looking at the motionEyeOS Wiki for details on the settings as well as other features that I haven't covered here. The github page also has an "issues" section where you can research any problems you may experience. It may be worth asking questions in the Google Group unless you are sure you have found a genuine issue.

## motionEyeOS Links

Here are some motionEyeOS links that are worth visiting for additional information :

All my motionEyeOS based projects are listed under [the motionEyeOS tag](http://www.raspberrypi-spy.co.uk/tag/motioneyeos/).
