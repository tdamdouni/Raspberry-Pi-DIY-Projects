# How to install Kodi on a Raspberry Pi 3: Get a dedicated HD streamer for cheap

_Captured: 2016-12-30 at 01:02 from [www.alphr.com](http://www.alphr.com/media-centres/1000077/how-to-turn-a-raspberry-pi-into-an-xbmc-media-center-build-a-fully-functional)_

![](http://cdn2.alphr.com/sites/alphr/files/styles/16x9_640/public/2016/10/how_to_install_kodi_raspberry_pi_3.jpg?itok=5myIWxT6)

The Raspberry Pi 3 is one of the best microcomputers around, because it combines impressive speed with good value in a tiny form factor. It's also versatile too, so it can be used for loads of projects - from making a cat feeder, to a local FM Radio transmitter. However, you can also use a Raspberry Pi 3 with Kodi, one of the best bits of streaming software around, and you'll end up with a speedy, dedicated media dongle on the cheap. With nothing more than a Raspberry Pi, a few cables and an open-source Linux distribution, you can network all your media together and display it on your big, shiny flat screen. Interested? Here's how to do it.

### **1\. Installating Kodi onto a Raspberry Pi 3**

If you want to use your Raspberry Pi as a media centre, there are a number of purpose-built OSes to help you get started. Our favourite is [OSMC](http://www.raspbmc.com/download/), a version of Kodi (formerly XBMC) optimised for the Pi.

![](http://cdn2.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/53/how-to-use-raspberry-pi-as-home-media-center-raspmbc-noobs-select.jpg?itok=Ynft0xb-)

Luckily for those unfamiliar with microSD card flashing, disk images and Linux distros, Raspbmc is one of the default OS options pre-packaged with the Raspberry Pi Foundation's [NOOBS installer](http://www.raspberrypi.org/downloads/). Simply follow our [beginner's guide to setting up a Raspberry Pi](http://www.alphr.com/features/391627/how-to-set-up-a-raspberry-pi-b), but when prompted to select a distro package to install, select Raspbmc from the list rather than Raspbian.

![](http://cdn2.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/54/how-to-use-raspberry-pi-as-home-media-center-raspbmc-install.jpg?itok=ydTXGtqi)

### **2\. Setting up Wi-Fi**

Once it's installed and booted up, the first thing you'll want to do is connect to your Wi-Fi network. Head over to the Programs tab, and go into the Raspbmc Settings menu. The Network tab of this menu will allow you to edit your wireless configuration by entering your network name and password, after which you should be fully connected.

![](http://cdn1.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/55/how-to-use-raspberry-pi-as-home-media-center-wifi-setup.jpg?itok=9WblBzwo)

However, as the Pi Zero doesn't have onboard Wi-Fi, for this model you'll need a USB adapter/dongle. Linux, and the Raspberry Pi in particular, can be very fussy about which adapters it works with, so make sure to check out this [list of compatible models](http://elinux.org/RPi_USB_Wi-Fi_Adapters) and purchase a new one if necessary.

### **3\. Adding a remote control**

The next task is adding a remote control to your Raspberry Pi - no-one wants to have a keyboard and mouse cluttering up their entertainment center. The good news is that if your TV supports HDMI CEC, your standard TV remote will work just fine with your Pi, and allow you to browse through your content from the comfort of your couch.

![](http://cdn1.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/63/remote.jpg?itok=aOBGekE7)

You can also control it through the web interface, by going to Raspbmc's system info menu, noting down the IP address of your Raspberry Pi and typing that address into your browser. Of course, it will have to be prefaced with "http://", and both computers will have to be on the same network. Once done, the web UI will open up; select the 'remote' tab, and a control interface will appear that you can use to navigate to your hearts content.

If you own a smartphone or tablet, you can also use that to control your Pi. As an open-source project, there are numerous apps available for this function. All you need to do is download one, and link it to your Raspbmc by entering the MAC address and port details, which can be found in Raspbmc's system menu.

![](http://cdn1.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/57/how-to-use-raspberry-pi-as-home-media-center-ios-remote-interface.jpg?itok=WXBetlbb)

### **4\. Playing your files**

Now that you're all set up, you can get down to the fun part - watching all your movies and TV. Playing your files is a snap - simply plug in a flash drive or external hard disk with your media on it, and your Raspberry Pi will automatically recognize it.

![](http://cdn1.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/58/how-to-use-raspberry-pi-as-home-media-center-file-browser.jpg?itok=OvefC3Mx)

From there, just navigate to the appropriate tab (music, movies or video), select your storage device, and your files should be there waiting to be played. If you own a NAS drive, Raspbmc is also capable of retrieving your files from there, but we find it's much simpler to simply use a thumb drive.

### **5\. Setting up AirPlay**

If you're an Apple fan with a lot of content from the iTunes store, you can also set up your Raspberry Pi as an AirPlay receiver. Simply go into the AirPlay tab in the services menu (found in the settings section) and tick 'allow XBMC to receive AirPlay content'. That done, your Apple device will detect your Raspberry Pi as an Airplay Receiver, and you'll be ready to stream all your iTunes content directly.

![](http://cdn2.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/8/59/how-to-use-raspberry-pi-as-home-media-center-airplay-ios-setup.jpg?itok=YBV5DLwu)

With all that done, you're ready to start streaming all your content, instantly and in HD. Due to the open-source nature of Rasbmc, it's constantly being updated, and there are numerous add-ons and options to let you tweak your experience to your hearts content, so you can have your entertainment exactly the way you want it. You'll never go back to normal TV again.

![](http://cdn1.alphr.com/sites/alphr/files/styles/insert_main_wide_image/public/9/06/raspberry-pi-media-center.jpg?itok=p2ozpPfk)
