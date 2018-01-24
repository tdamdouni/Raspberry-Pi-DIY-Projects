# How to setup a Raspberry Pi Node.js Webserver and control GPIOs

_Captured: 2017-10-27 at 18:55 from [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/setup-raspberry-pi-node-js-webserver-control-gpios/)_

![Raspberry Pi Node.JS Logo](https://tutorials-raspberrypi.com/wp-content/uploads/2016/10/Raspberry-Pi-Node.JS-Logo-1024x627.png)

Node.JS is a server platform that uses JavaScript. Originally developed for the[Google Chrome browser](https://tutorials-raspberrypi.com/google-chrome-for-raspberry-pi/), it is very resource-efficient, which makes the use of a Raspberry Pi Node.JS web server interesting. In addition to the advantages of asynchronous applications, Node.JS offers a very simple but powerful method to install and use different plugins or libraries, using the internal package manager "npm".

This tutorial shows you how to set up and configure a Raspberry Pi NodeJS server. In addition, I have written a small program for Node, which can control the GPIOs of the Raspberry Pi.

A NodeJS server is a prerequisite for many different applications, such as [HomeBridge](https://github.com/nfarina/homebridge). Many other projects, for which a server is needed, can also be realized with a Raspberry Pi and NodeJS.

## Used Hardware

Because of the better performance compared to the previous versions and especially because of the ARMv8 architecture, I recommend a Raspberry Pi 3. In addition, your router must support portforwarding, if you want to call the applications outside of your home network. I recommend for this a FRITZ!Box or similar.

In order to be able to reproduce the small example at the end, the following hardware is also required:

In addition, I recommend using the [SSH access](https://tutorials-raspberrypi.com/raspberry-pi-remote-access-by-using-ssh-and-putty/), as well as optimally from an [FTP service](https://tutorials-raspberrypi.com/raspberry-pi-ftp-server-installation/), to simply transfer files to the Raspberry Pi.

## Installation of Node.JS on the Raspberry Pi

Before we install Node, we update the packages and package sources to have everything you need:
    
    
    sudo apt-get update
    sudo apt-get full-upgrade

The process may take some time. Since Node.JS is not in the predefined package sources, we must add it first. The latest LTS version can be viewed on the [Node.JS website](https://nodejs.org/en/download/) and adapted accordingly.
    
    
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

Now we can easily install Node via the internal package manager, which may take a little time:
    
    
    sudo apt-get install -y nodejs

## First Test

If the installation went through without any problems, we can simply write the following in the console to see if everything has worked:
    
    
    node --version

The [latest version](https://nodejs.org/en/download/) should now be displayed.

Now let's begin with a little [Hello-World!](https://howtonode.org/hello-node) program. We are creating a new file.
    
    
    sudo nano hello-world.js

Here we add the following content:

1234567891011121314 
// Load the http module to create an http server.var http = require('http');// Configure our HTTP server to respond with Hello World to all requests.var server = http.createServer(function (request, response) {response.writeHead(200, {"Content-Type": "text/plain"});response.end("Hello World\n");});// Listen on port 8000, IP defaults to 127.0.0.1server.listen(8000);// Put a friendly message on the terminalconsole.log("Server running at http://127.0.0.1:8000/");

We then save and close the editor (CTRL + O, CTRL + X). You can now start the server simply by entering the following in the terminal:
    
    
    node hello-world.js

You can now view the page in the browser. Enter either the IP of your Pi in the network including the port (e.g., 192.168.1.68:8000) or (if your router supports it) simply the name of the host including port. For me, this is <http://raspberrypi:8000/>

![node-js-hello-world-preview](https://tutorials-raspberrypi.com/wp-content/uploads/2016/10/Node.js-Hello-World-Preview.png)

PS: We use port 8000 in this example. The default port for web servers is 80. However, Node.js requires [root privileges](http://stackoverflow.com/questions/18947356/node-js-app-cant-run-on-port-80-even-though-theres-no-other-process-blocking-t) for ports that are less than 1000.

If you want to permanently access the server from outside your home network, it makes sense to install a DNS server. Of course, the selected ports must also be selected and enabled in your router via port forwarding for the internal IP address of your Raspberry Pi.

## NPM - NodeJS Package Manager

With the help of the [NPM](https://www.npmjs.com/) (Node.js Package Manager), additional libraries can be easily installed and used in a node project. Typically, a created project has a file named "package.json" in the root directory. In this file "dependencies" are used to specify the packages used (minimum required). If you use / download another project, the required packages must first be installed. To do this, change to the directory where the package.json is located and enter:
    
    
    npm install

All necessary packages are installed. However, it is not absolutely necessary that you enter your used packages by hand. If you want to use a new package (in our case it is [rpio](https://www.npmjs.com/package/rpio)) you can specify the parameter `\--save` and the package will be automatically added to the package.json file:
    
    
    npm install rpio --save

For further instructions and explanations, you can take a look at the [NPM documentation](https://docs.npmjs.com/).

## Control Raspberry Pi GPIOs via web interface

If your sample file is still running, you can terminate it by pressing CTRL + C.

I have written a small application that allows you to control your GPIOs via the web interface (desktop PC browser, smart phone, tablet). Since this is only a small example, the output can only be controlled. However, it is also easy to define GPIOs as inputs and to read them out. As a basis I took the NPM package [rpio](https://www.npmjs.com/package/rpio).

For a simple test, you can clone the [GitHub](https://github.com/tutRPi/Raspberry-Pi-Simple-Web-GPIO-GUI) package:
    
    
    git clone https://github.com/tutRPi/Raspberry-Pi-Simple-Web-GPIO-GUI
    cd Raspberry-Pi-Simple-Web-GPIO-GUI

Before we start the server, the other packages have to be installed:
    
    
    npm install

The Raspberry Pi Node.JS server can then be started. Since we use the GPIOs we have to start it with sudo. So I decided to run the server on port 80, because we can easily access it via the hostname or internal IP of the Pi without specifying the port. The prerequisite is that nothing else is running on this port (such as Apache2). So we start now:
    
    
    sudo npm start

Back in the web browser, you can see the user interface for controlling the GPIOs (no port required). For this, it must be said that the GPIOs are initially displayed as "OFF", even if another application has previously connected one of the pins. This is because the library unfortunately can not read the output state of the GPIOs. Although you could start the web app all GPIOs to the low level, but I have decided to not do that. If this bothers you, you are free to adjust it.

![Raspberry Pi Node.js Webserver installieren und GPIOs schalten](https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-Node.js-Webserver-GPIOS-403x500.png)

Furthermore, I've recorded it to show how the control would look through the web interface. If you want to see the structure of the sample circuit, you can do this here. Basically, however, it is quite simple, since an LED with a series resistor was simply attached to the individual (controllable) GPIOs.

## Auto boot of the Raspberry Pi Node.js Server

Finally, we want to start the server automatically after rebooting of the Raspberry Pi. Otherwise, the server would end at shutdown and you would have to be activated again by hand.

Before we can create the entry for automatic starting from our server application, we have to find the path where Node is located (by default, this is `/usr/bin/node`).
    
    
    pi@raspberrypi:~ $ which node
    /usr/bin/node

Now we need the complete the path where our javascript file (`app.js`) is located. By using `ls`, we can display the files that are present in the folder and with `pwd` the path.

These two values are copied to create now a new entry:
    
    
    sudo crontab -e

At the end of this file, entries can be added, which are run e.g. after a reboot or at a certain point in time. To start our application automatically after rebooting, we add the following line to the end of the file (if necessary, adjust the paths):
    
    
    @reboot sudo /usr/bin/node /home/pi/Raspberry-Pi-Simple-Web-GPIO-GUI/app.js &

Save it with CTRL + O and exit with CTRL + X (Nano Editor). To check if everything has worked, you can restart the Raspberry Pi (`sudo reboot`) and then call the URL in your browser again. If the page is displayed, everything has worked.

The applications that you can run on your Raspberry Pi Node.JS server are almost unlimited. From the pure GPIO control, via a surface for home automation to the monitoring server for individual services or sensors. Due to the low power consumption of the Raspberry Pi and still comparatively high performance, the Raspberry Pi is an ideal server for small (hobby) projects.
