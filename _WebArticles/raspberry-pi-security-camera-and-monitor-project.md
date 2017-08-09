# Raspberry PI Security Camera and Monitor Project

_Captured: 2017-05-06 at 16:24 from [startingelectronics.org](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/)_

This Raspberry PI security camera project is probably the easiest way to use a Raspberry PI board and camera for security or other video monitoring. Hardware setup is easy for beginners and the software installation is simple.

The Raspberry PI security camera and monitor allows live video to be streamed from the camera to a web browser. The camera can also be set up to sense motion and start recording video or take a picture when triggered by movement.

All that is needed is a Raspberry PI board, Raspberry PI camera, micro SD card, power supply and Ethernet connection to a network. WiFi can also be used instead of a wired LAN. A USB camera can be used instead of a Raspberry PI camera, or in addition to a RPI camera.

The following video demonstrates the camera in action as seen in a web browser.

## Raspberry PI Security Camera and Monitor Hardware

The main hardware required for the project is shown below. Not shown is a power supply and Ethernet cable which will also be needed. A WiFi dongle will be needed if the camera is to be used with WiFi and the board does not have built-in WiFi, but initial setup is done over the LAN.

![Raspberry PI security camera hardware parts](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/rpi-security-camera-parts.jpg)

> _Raspberry PI Security Camera Hardware Parts_

In the image, the Raspberry PI camera can be seen at the top. The Raspberry PI board is a Raspberry PI B+ model, but any Raspberry PI board should work. The Raspberry PI B+ uses a micro SD card, which comes with an adapter also shown in the image. The adapter might be needed when writing the software to the card from a laptop that may only have the full sized SD card socket.

### Connecting the Raspberry PI Camera

How to connect the Raspberry PI camera to a Raspberry PI board is shown in the image below. Be sure to use the connector labelled **CAMERA** on the Raspberry PI board. The other connector that looks the same is labelled DISPLAY and meant connecting an LCD screen.

Lift the plastic clamp on the CAMERA connector up and insert the flat cable from the camera with the exposed metal contacts on the end facing away from the USB connectors as shown in the image. When the cable has been inserted all the way to the bottom of the connector, push the connector clamp down on both sides to lock it in place.

![Raspberry PI Camera Connection](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/raspberry-pi-camera-connection.jpg)

> _Raspberry PI Camera Connection - the Exposed Metal Contacts on the Ribbon Cable Face Away from the USB Connectors_

### Connecting the Other Hardware

After installing the software to the SD card, as described in the next section, insert the SD card into the SD card socket on the Raspberry PI board. Connect the Ethernet connector of the board to your router or hub using an Ethernet cable. Finally power up the board by connecting the power supply to the board.

## Raspberry PI Security Camera and Motion Detector Software

After connecting the camera to the Raspberry PI board, software needs to be installed to turn the Raspberry PI into a security camera.

### Raspberry PI Security Camera Software Overview

This project uses the **motionEyeOS** software to turn the RPI into a security or monitoring camera. The basic steps are:

  * Download and install the motionEyeOS image file to the SD card.
  * Connect the Raspberry PI to the network and power it on.
  * Find the IP address of the Raspberry PI.
  * Access the Raspberry PI security camera from a web browser.

The motionEyeOS software is a complete operating system with the Raspberry PI camera software included. This makes it very easy to get the camera working - it is just a matter of installing the software to SD card. Settings and preferences can be changed once the RPI is accessed from a web browser by making changes in the web browser.

### Installing motionEyeOS to SD Card

#### Downloading motionEyeOS

motionEyeOS is available for several different boards and not just the Raspberry PI. There are also different releases of the software for each different type of Raspberry PI, namely, the original Raspberry PI, Raspberry PI 2 and Raspberry PI 3. Click the above link and find the heading closest to the top of the page that says **Latest release**. Now scroll down and find **Downloads**. A list of files can be found under the Downloads heading for different boards and different Raspberry PI releases.

For example, the newest or latest version of the software at the time of writing was **20160410** and the version needed for the Raspberry PI B+ model was **motioneyeos-raspberrypi-20160410.img.gz**.

#### Installing motionEyeOS

After downloading the correct file, the image file must be extracted from it because it is a compressed or zipped file. On a Windows computer, [use 7-zip to open the file](http://www.7-zip.org/) and extract the image file from it. The extracted image file will have the same name as the downloaded file, but without **.gz** at the end, e.g. **motioneyeos-raspberrypi-20160410.img**.

The image file can be installed onto the SD card using the [same method used to install the Raspbian operating system image file for Linux, Mac OS and Windows](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) as described on the Raspberry PI website (look under the **WRITING AN IMAGE TO THE SD CARD** heading). Just use the motionEyeOS image that you extracted instead of the Raspbian image when following the instructions. On a Windows computer this involves [downloading and using Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) to copy the image file to the SD card.

Installation instructions on the [motionEyeOS wiki page](https://github.com/ccrisan/motioneyeos/wiki/Installation) are also available.

## Using the Raspberry PI Security Camera

Because the Raspberry PI is being used as a security camera, it does not need to have a monitor, keyboard or mouse attached. In fact when using motionEyeOS it is pointless even connecting a screen, keyboard and mouse because they are not used by the software. The RPI is accessed exclusively through a web browser, but first the IP address of the RPI must be found before it can be accessed.

### Finding the Raspberry PI IP Address

#### Booting the RPI for the First Time

After installing motionEyeOS to the SD card, insert the card into the socket on the RPI board. Connect the board to your network using an Ethernet cable (even if you intend to use WiFi later) and power the board up by connecting a power supply to it. Allow the board about 2 minutes to boot up the first time before trying to find it on the network.

#### Finding the IP Address using the Router

The easiest way to find the IP address of the RPI is to log in to your router. All routers are slightly different, but the general idea is to find the IP address of your router by looking in the router documentation, then open a web browser and enter the router IP address into the address bar of the browser. A web page from the router will load and allow you to log in to the router. Default login credentials vary from router to router, but they often use **admin** as the default user name and password. If this does not work, check your router documentation.

An example of finding the IP address of the RPI using a NetGear router is shown below. Also see the wiki page information on [booting motionEyeOS for the first time](https://github.com/ccrisan/motioneyeos/wiki/Installation#first-boot).

#### Finding the Raspberry PI IP Address on a NetGear Genie DGN2200 Router

The principal of finding the IP address on this router will be similar on other NetGear router models and other router brands will probably just have a different appearance and menus.

From the NetGear documentation, the router can be found at **http://routerlogin.net** - other routers may just give an IP address instead, e.g. this router can also be found at **http://192.168.0.1/**. After opening a browser and entering the address of the router in the address bar, a login dialog box opens allowing you to log in.

![Router Login Dialog Box](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/router-login.jpg)

> _Router Login Dialog Box_

Log in to the router using the user name **admin** and **password** for the password. The default router web page will then be displayed.

![Default Router Web Page](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/router-main-page.jpg)

> _Default Router Web Page_

Click **Attached Devices** on the menu or the Attached Devices image on the home page to open a page that will show the IP addresses of all devices attached to the router.

![Attached Devices Router Page](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/router-attached-devices.jpg)

> _Attached Devices Router Page_

As can be seen in the above image, the Raspberry PI has a name starting with **MEYE-** when running motionEyeOS. In this example, the IP address of the RPI is **192.168.0.6** as shown in the IP Address column.

### Connecting to the RPI and Viewing the Camera Video Image

Now that you have the IP address of the Raspberry PI camera, enter it in the address bar of a web browser to see the camera video image and the camera settings.

The image below shows a web browser after entering the camera IP address.

![Camera Video Image Shown in a Web Browser](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/camera-video.jpg)

> _Camera Video Image Shown in a Web Browser_

### Basic motionEyeOS Operating Modes

#### User Mode

When you first visit the RPI security camera web page, you are logged in as a user. In user mode there are minimal settings that can be changed as it is intended as the normal operating and video monitoring mode. The available user settings can be seen by clicking the top left menu icon (the three horizontal bars).

If you open the login dialog box as described below and then close it, the video image will disappear because you have effectively logged out. Open the login dialog box again and log in with **user** as the user name, leaving the password field blank. This will log you back in to user mode and the video will be displayed again.

#### Administrator Mode

Click the second icon at the top left of the web page (the head and shoulders icon) to change to administrator mode. A dialog box will open as shown below. Enter **admin** as the user name, leaving the password field blank to log in as an administrator.

![motionEyeOS Login Dialog Box](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/motion-eye-os-login.png)

> _motionEyeOS Login Dialog Box_

When the main menu is opened in administrator mode, there will be many more settings and options available.

### Operating the Camera from WiFi

Before WiFi can be used, a USB WiFi dongle must be inserted into one of the USB sockets on the Raspberry PI board if it is not a newer model that already has built-in WiFi.

To change to using the camera over WiFi, log in as administrator as described above. Have your WiFi network user name and password ready. You may need to log into your router again to get these.

Open the main menu on the camera web page and enable **Advanced Settings** under the **General Settings** menu item as shown below.

![Enabling the Camera Advanced Settings](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/camera-advanced-settings.png)

> _Enabling the Camera Advanced Settings_

Now fill in your WiFi user name and password as shown in the image below. Finally click the **Apply** button at the top of the page which appears only if changes to settings are made.

![Camera WiFi Settings](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/camera-wifi-settings.png)

> _Camera WiFi Settings_

### Setting a Static IP Address for the Camera

Most routers will be set up to dynamically assign an IP address to any device that is connected to the network by using DHCP. The problem with this is that every time you reboot your router or the Raspberry PI the IP address of the RPI may change. You will then need to find the new IP address of the RPI in order to access it. The solution is to use a fixed IP address for the RPI camera.

To use a static IP address, an IP address must first be reserved in the router settings and then the camera must be set up to use the reserved IP address. You will need to log in to your router to do this. Again, different routers will be slightly different. An example of using the NetGear Genie router can be found below.

#### Reserving an IP Address on a NetGear Genie DGN2200 Router

Log in to the router as already described and click the **ADVANCED** tab at the top of the router web page. Now click the **Setup** menu item to expand it and then click **LAN Setup** below it.

Scroll down to the bottom of the **LAN Setup** page to the section called **Address Reservation** and click the **Add** button as shown below.

![Router Address Reservation](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/router-address-reservation.jpg)

> _Router Address Reservation_

After clicking the Add button, the page shown below will appear. Find the RPI in the list and click the radio button next to it to select it. The IP address for the device can then be changed. I decided to change mine to 192.168.0.50. Finally click the **Add** button at the top of the page to save the changes.

![Adding a Reserved IP Address](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/adding-reserved-ip.png)

> _Adding a Reserved IP Address_

#### Change to using a Static IP Address on the Camera

After reserving an IP address on the network, the camera must be set to use this static IP address.

Log in to the camera as administrator as previously described and switch to **Advanced Settings** (button found under General Settings). Now change the **IP Configuration** setting under the **Network** menu item to **Manual (Static IP)**. Change the IP Address in the field below the IP configuration to the IP address that you reserved in your router as shown below. Change the **Default Gateway** to the IP address of your router. Finally click the **Apply** button at the top of the page. The camera will reboot. If you changed the IP address of the camera, you will need to close the web page and connect to the camera again using the new IP address.

![Camera Static IP Configuration](https://startingelectronics.org/projects/raspberry-PI-projects/easy-rpi-security-camera/camera-static-ip-configuration.jpg)

> _Camera Static IP Configuration_

### General Information and Changing Camera Settings

#### Switching the Camera Off

The camera should be switched off using the motionEyeOS menu from a web browser. When logged in as administrator and with advanced settings enabled, click the **Shut Down** button under **General Settings** and wait for the system to shut down before switching the power off.

#### motionEyeOS Wiki Pages

This section is an index into the [motionEyeOS wiki](https://github.com/ccrisan/motioneyeos/wiki) to make it easy to find the answers various questions about the Raspberry PI security camera and where to change camera settings.

[Initial setup](https://github.com/ccrisan/motioneyeos/wiki/Configuration#initial-setup) gives information on things that you will want to do to set the camera up, like setting the time zone and passwords for admin and user.

[The normal use section](https://github.com/ccrisan/motioneyeos/wiki/Configuration#normal-use) describes general information on using the camera that you should know.

Different camera configurations are described in the [usage scenarios section](https://github.com/ccrisan/motioneyeos/wiki/Usage-Scenarios), including how to use more than one camera with a single RPI board, and various scenarios that use more than one RPI board.

[Action buttons](https://github.com/ccrisan/motioneyeos/wiki/Action-Buttons) can be used to execute custom commands to switch on a light or alarm by clicking buttons that are overlaid on the video image.

[The tweaks section](https://github.com/ccrisan/motioneyeos/wiki/Tweaks) provides more advanced information and advanced settings for motionEyeOS.

[The FAQ](https://github.com/ccrisan/motioneyeos/wiki/FAQ) is worth reading to find answers to common questions.

There is a page describing [how to get a Raspberry PI model A connected to WiFi](https://github.com/ccrisan/motioneyeos/wiki/Troubleshooting-Raspberry-PI-Model-A). The A model does not have a wired network connection.

The solutions to various problems can be found in [the troubleshooting section](https://github.com/ccrisan/motioneyeos/wiki/Troubleshooting).

Sponsored Links

.

[EverQuote Insurance Quotes](https://article.everquote.com/?h1=startup&h2=brilliant_company&auuid=101acd74-66e0-43c5-b688-57867aa8cc2d&&tid=584&subid=2014&utm_medium=disqus-widget-safetylevel20longtail14&utm_title=Scottown%2C+Ohio%3A+This+Brilliant+Company+Is+Disrupting+a+%24200+Billion+Industry&utm_thumbnail=http%3A%2F%2Fstatic.evq1.com%2F842358f8-5b24-4b74-83b6-85ae4273465d.png)[Scottown, Ohio: This Brilliant Company Is Disrupting a $200 Billion IndustryEverQuote Insurance Quotes](https://article.everquote.com/?h1=startup&h2=brilliant_company&auuid=101acd74-66e0-43c5-b688-57867aa8cc2d&&tid=584&subid=2014&utm_medium=disqus-widget-safetylevel20longtail14&utm_title=Scottown%2C+Ohio%3A+This+Brilliant+Company+Is+Disrupting+a+%24200+Billion+Industry&utm_thumbnail=http%3A%2F%2Fstatic.evq1.com%2F842358f8-5b24-4b74-83b6-85ae4273465d.png)

[GameOfGlam](http://gameofglam.com/marriedwith-children-now-christina-applegate-brave-fought-mesothelioma-cancer/?utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail14&utm_campaign=493340&utm_term=What+Marcy+D%27Arcy+Looks+Like+Now+Will+Make+You+Shiver&utm_content=http%3A%2F%2Fcdn.taboolasyndication.com%2Flibtrc%2Fstatic%2Fthumbnails%2F98fbd21db423319d42561bee6458113d.jpg)[What Marcy D'Arcy Looks Like Now Will Make You ShiverGameOfGlam](http://gameofglam.com/marriedwith-children-now-christina-applegate-brave-fought-mesothelioma-cancer/?utm_source=taboola&utm_medium=disqus-widget-safetylevel20longtail14&utm_campaign=493340&utm_term=What+Marcy+D%27Arcy+Looks+Like+Now+Will+Make+You+Shiver&utm_content=http%3A%2F%2Fcdn.taboolasyndication.com%2Flibtrc%2Fstatic%2Fthumbnails%2F98fbd21db423319d42561bee6458113d.jpg)

[Save On Dental](http://saveondentalimplant.com?utm_source=tboo&utm_medium=CPC&utm_term=Dental Implants&utm_campaign=DentalImplant_01_M&utm_targeting=disqus-widget-safetylevel20longtail14&adid=37949983&subsrc=500284&src=Desktop&keyword=Dental Implants&token=CiRiY2IxNTU2Ni1hZDZhLTRlNzEtYjY2OC05MTk1YjQ5MDBjZWESDXJpZ2h0cmVhY2gtc2M&campaign=34843910)[Here's What New Dental Implants Should CostSave On Dental](http://saveondentalimplant.com?utm_source=tboo&utm_medium=CPC&utm_term=Dental Implants&utm_campaign=DentalImplant_01_M&utm_targeting=disqus-widget-safetylevel20longtail14&adid=37949983&subsrc=500284&src=Desktop&keyword=Dental Implants&token=CiRiY2IxNTU2Ni1hZDZhLTRlNzEtYjY2OC05MTk1YjQ5MDBjZWESDXJpZ2h0cmVhY2gtc2M&campaign=34843910)

[Rate Marketplace Quotes](http://thefinancestandard.com/mortgage-reporting/?t202id=618954&t202kw=tabref-3&utm_source=taboola&utm_medium=referral)[Forget Social Security if you Own a Home (Do This)Rate Marketplace Quotes](http://thefinancestandard.com/mortgage-reporting/?t202id=618954&t202kw=tabref-3&utm_source=taboola&utm_medium=referral)

[Frank151](http://adrzr.com/5bd7?utm_source=taboola&utm_campaign=taboola_US_desktop_frank151-statephotos-us-d-taboola_24_5bd7_20170331_dl_5052&utm_term=disqus-widget-safetylevel20longtail14&utm_medium=disqus-widget-safetylevel20longtail14&utm_term=disqus-widget-safetylevel20longtail14)[Each State Hilariously Depicted By One Stereotypical PhotoFrank151](http://adrzr.com/5bd7?utm_source=taboola&utm_campaign=taboola_US_desktop_frank151-statephotos-us-d-taboola_24_5bd7_20170331_dl_5052&utm_term=disqus-widget-safetylevel20longtail14&utm_medium=disqus-widget-safetylevel20longtail14&utm_term=disqus-widget-safetylevel20longtail14)

[Livingly](http://www.livingly.com/The+Must-See+Runway+Looks+From+London+Fashion+Week+Spring+2016?utm_source=tabo&utm_medium=cpc&utm_campaign=Tabo-LV-US-Desktop-Specials-London-Fashion-Week&utm_content=disqus-widget-safetylevel20longtail14_This+Gown+At+The+London+Fashion+Week+Left+The+Crowd+Speechless)[This Gown At The London Fashion Week Left The Crowd SpeechlessLivingly](http://www.livingly.com/The+Must-See+Runway+Looks+From+London+Fashion+Week+Spring+2016?utm_source=tabo&utm_medium=cpc&utm_campaign=Tabo-LV-US-Desktop-Specials-London-Fashion-Week&utm_content=disqus-widget-safetylevel20longtail14_This+Gown+At+The+London+Fashion+Week+Left+The+Crowd+Speechless)

![](https://match.adsrvr.org/track/cmf/generic?ttd_pid=054f32o&ttd_tpi=1)

![](https://tags.bluekai.com/site/35702?id=bcb15566-ad6a-4e71-b668-9195b4900cea&redir=%2F%2Ftrc.taboola.com%2Fsg%2Fbluekai%2F1%2Fcm%3Ftaboola_hm%3D%24_BK_UUID)

![](https://aa.agkn.com/adscores/g.pixel?sid=9212237748&puid=bcb15566-ad6a-4e71-b668-9195b4900cea)
