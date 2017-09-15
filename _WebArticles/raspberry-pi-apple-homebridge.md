# Raspberry Pi – Apple Homebridge

_Captured: 2017-09-03 at 13:06 from [www.studiopieters.nl](https://www.studiopieters.nl/raspberry-pi-apple-homebridge/)_

**What is HomeBridge and why should you use it?**

HomeBridge is a utility that some wonderful geniuses wrote to allow you to tie together all of the various "almost smart" home devices into Apples new HomeKit framework for Siri to control. If you want to learn more about Siri and HomeKit then I would suggest you start reading Apple's website for some examples and details. Now that you are familiar with Siri and HomeKit we can move onto using HomeBridge. HomeBridge is a utility that needs to be run on a device that can stay powered on all the time in the background. Ideally you will want something that doesn't consume lots of power or resources. That's where the Raspberry Pi comes in.

![HomeKit](https://www.studiopieters.nl/wp-content/uploads/2016/06/HomeKit-1024x512.jpg)

**Ok I'm convinced. Now what?**

Now you will need to get everything together and assembled. Some of the things I'll be covering will be optional. Such as you can optionally connect your server via Ethernet or WiFi. In that case, I would suggest Ethernet for quicker response time. You may also want to protect your Raspberry Pi by installing it into a case, and there are hundreds of options out there for you to choose between.Here's what you will need:

  * Raspberry Pi 2 Model B
  * SanDisk Ultra 32GB microSDHC
  * USB 3.0 Card Reader
  * Official Raspberry Pi Case (optional)
  * RJ45 Ethernet Patch Cable (reccomended)

Once you have acquired all the necessary and desired pieced you will need to download the operating system to install on your raspberry pi. You can **[read all about this in my previous blog](https://www.studiopieters.nl/raspberry-pi-ras…operating-system/)**.

Now assemble all the pieces, plug your Raspberry Pi in. You will want to make sure you have a monitor, mouse, keyboard, and ethernet connected so we can set up the basics. Or you can use RDP, You can **[read all about this in my previous blog**](https://www.studiopieters.nl/raspberry-pi-rem…sktop-connection/).

To install Homebridge we use the Terminal Raspbian . In contrast to visual installers this installation will be carried out by entering commands. While this does not always look that easy , it is almost always a matter of copying and pasting codes.

![6BK90wn](https://www.studiopieters.nl/wp-content/uploads/2016/03/6BK90wn.gif)

Open Terminal by clicking upper left of the screen, click the Terminal icon. We start with updating the system. Enter the following commands one at a time followed by Enter:

`sudo apt-get update`  
`sudo apt-get upgrade`

Now we install Node required for Homebridge .

**_Note: If you use a Raspberry Pi 2 Model A? Enter the following commands:_**

`Sudo wget https://nodejs.org/dist/v6.9.2/node-v6.9.2-linux-armv6l.tar.gz`  
`sudo tar -xvf node-v6.9.2-linux-armv6l.tar.gz`  
`cd node-v6.9.2-linux-armv6l`

**_Note: If you use a Raspberry Pi 2 Model B? Enter the following commands:_**

`sudo wget https://nodejs.org/dist/v6.9.2/node-v6.9.2-linux-armv7l.tar.gz`  
`sudo tar -xvf node-v6.9.2-linux-armv7l.tar.gz`  
`cd node-v6.9.2-linux-armv7l`  
Copy to / usr / local / using the following command to execute :

`sudo cp -R * /usr/local/`

Node.js is installed. You can check this by entering the following command . In response you will see the version number ; In this case, 6.9.2 .

`node -v`

Install Avahi with the following command :

`sudo apt-get install libavahi-compat-libdnssd-dev`

All preparations for the installation are now affected .

**Installing Homebridge**

It's finally time for the real installation. This is mostly a matter of waiting and patience .

![goody](https://www.studiopieters.nl/wp-content/uploads/2015/09/goody.gif)

Homebridge to install by typing the following command:

`sudo npm install -g homebridge --unsafe-perm`

You may need to use the -unsafe-perm flag if you receive an error similar to this:

`gyp WARN EACCES user "root" does not have permission to access the dev dir "/root/.node-gyp/5.5.0"`

Installation can take quite some time . Do not worry if you have some errors pass by. Wait quietly until the completion of the installation.  
When the installation is complete, we can start Homebridge for the first time . Enter the following command:

`homebridge`

![52676242697d497a8f3417a9c30e2f0f](https://www.studiopieters.nl/wp-content/uploads/2016/06/52676242697d497a8f3417a9c30e2f0f-1160x680.png)

**Errors on startup**

The following errors are experienced when starting Homebridge and can be safely ignored.

`*** WARNING *** The program 'nodejs' uses the Apple Bonjour compatibility layer of Avahi  
*** WARNING *** Please fix your application to use the native API of Avahi!  
*** WARNING *** For more information see http://0pointerde/avahi-compat?s=libdns_sd&e=nodejs  
*** WARNING *** The program 'nodejs' called 'DNSServiceRegister()' which is not supported (or only supported partially) in the Apple Bonjour compatibility layer of Avahi  
*** WARNING *** Please fix your application to use the native API of Avahi!  
*** WARNING *** For more information see http://0pointerde/avahi-compat?s=libdns_sd&e=nodejs&f=DNSServiceRegister`

![tumblr_mdk0kupsIK1qgxx3q](https://www.studiopieters.nl/wp-content/uploads/2015/11/tumblr_mdk0kupsIK1qgxx3q.gif)
