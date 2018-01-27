# Website/WiFi Controlled LED Strip With Raspberry Pi

_Captured: 2018-01-24 at 15:27 from [www.instructables.com](http://www.instructables.com/id/WebsiteWiFi-Controlled-LED-Strip-With-Raspberry-Pi/)_

## Introduction: Website/WiFi Controlled LED Strip With Raspberry Pi

![Picture of Website/WiFi Controlled LED Strip With Raspberry Pi](https://cdn.instructables.com/F02/AX8N/JBMJVWZO/F02AX8NJBMJVWZO.LARGE.jpg)[ ](https://cdn.instructables.com/F02/AX8N/JBMJVWZO/F02AX8NJBMJVWZO.LARGE.jpg)

### Background:

I am a teenager, and have been designing and programming small electronics projects for the past few years, along with participating in robotics competitions.

I was recently working on updating my desk setup, and I decided that a nice addition would be some mood lighting. At first, I just bought a 5v battery powered LED strip controlled by a remote, but it wasn't a very fulfilling process and I had an idea. I had a few spare parts lying around, and had been trying to think of something to do with the Raspberry Pi I had got for Christmas. During a particularly boring day in science class, I realized I could use the Raspberry Pi's GPIO pins to control the LED lights, so long as I had them output RGB values.

My initial design plan was to have the lights controlled by a touchscreen display mounted on my wall or desk, but after some revisions I decided the easiest way to go would be to control it with another device. While I considered writing an app for my phone in Java, a small website seemed much more efficient.

**This project is open to many improvements, and while my html + php are sort of sketchy, they get the job done.**

### Topics:

The main points this guide will hit are---

  1. Controlling GPIO on the Raspberry Pi 
  2. Hosting an Apache web server on the Pi 
  3. Using the web server to control a RGB LED light strip

## Step 1: Required Materials and Supplies

### 

  * 1 x Raspberry Pi ( I used a Pi 2 Model B) 
  * MicroSD card
  * Something to power your Pi (USB cable and AC power adapter) 
  * 1 x USB WiFi adapter OR an Ethernet Connection 
  * Multiple Colors of solid core wire 
  * An enclosure
  * 3 x NPN type transistors(I used BC547b transistors)
  * 1x 5V LED light strip

![Picture of Setting Up the Pi's Environment](https://cdn.instructables.com/F1W/7R8F/JB3ZPVWC/F1W7R8FJB3ZPVWC.MEDIUM.jpg)[ ](https://cdn.instructables.com/F1W/7R8F/JB3ZPVWC/F1W7R8FJB3ZPVWC.LARGE.jpg)![Picture of Setting Up the Pi's Environment](https://cdn.instructables.com/FR7/B24S/JB3ZPX1I/FR7B24SJB3ZPX1I.MEDIUM.jpg)[ ](https://cdn.instructables.com/FR7/B24S/JB3ZPX1I/FR7B24SJB3ZPX1I.LARGE.jpg)

![Picture of Getting Your Pi Set Up \(Part 1\)](https://cdn.instructables.com/FGJ/RCVF/JB6TW7LO/FGJRCVFJB6TW7LO.LARGE.jpg)[ ](https://cdn.instructables.com/FGJ/RCVF/JB6TW7LO/FGJRCVFJB6TW7LO.LARGE.jpg)

![Picture of Circuit Design](https://cdn.instructables.com/FPX/OQRR/JBMJV498/FPXOQRRJBMJV498.LARGE.jpg)[ ](https://cdn.instructables.com/FPX/OQRR/JBMJV498/FPXOQRRJBMJV498.LARGE.jpg)

![Picture of Buttering Your Bread . . . Board](https://cdn.instructables.com/F64/NUED/JBMJV4XG/F64NUEDJBMJV4XG.LARGE.jpg)[ ](https://cdn.instructables.com/F64/NUED/JBMJV4XG/F64NUEDJBMJV4XG.LARGE.jpg)

![Picture of Testing](https://cdn.instructables.com/FQP/45CA/JBMJVDF9/FQP45CAJBMJVDF9.LARGE.jpg)[ ](https://cdn.instructables.com/FQP/45CA/JBMJVDF9/FQP45CAJBMJVDF9.LARGE.jpg)

## Introduction: Website/WiFi Controlled LED Strip With Raspberry Pi

### Background:

I am a teenager, and have been designing and programming small electronics projects for the past few years, along with participating in robotics competitions. 

I was recently working on updating my desk setup, and I decided that a nice addition would be some mood lighting. At first, I just bought a 5v battery powered LED strip controlled by a remote, but it wasn't a very fulfilling process and I had an idea. I had a few spare parts lying around, and had been trying to think of something to do with the Raspberry Pi I had got for Christmas. During a particularly boring day in science class, I realized I could use the Raspberry Pi's GPIO pins to control the LED lights, so long as I had them output RGB values. 

My initial design plan was to have the lights controlled by a touchscreen display mounted on my wall or desk, but after some revisions I decided the easiest way to go would be to control it with another device. While I considered writing an app for my phone in Java, a small website seemed much more efficient. 

**This project is open to many improvements, and while my html + php are sort of sketchy, they get the job done.**

### Topics:

The main points this guide will hit are---

  1. Controlling GPIO on the Raspberry Pi 
  2. Hosting an Apache web server on the Pi 
  3. Using the web server to control a RGB LED light strip

Add TipAsk Question

## Step 1: Required Materials and Supplies

### 

  * 1 x Raspberry Pi ( I used a Pi 2 Model B) 
  * MicroSD card
  * Something to power your Pi (USB cable and AC power adapter) 
  * 1 x USB WiFi adapter OR an Ethernet Connection 
  * 1 x USB to Serial Cable - [ https://www.sparkfun.com/products/12977](https://www.sparkfun.com/products/12977)
  * 1 x GPIO breakout - [ https://www.sparkfun.com/products/13717](https://www.sparkfun.com/products/13717)
  * 1 x small breadboard - [ https://www.sparkfun.com/products/12002](https://www.sparkfun.com/products/12002)
  * USB to MicroSD - [ http://a.co/hwilifZ](http://a.co/hwilifZ)
  * Multiple Colors of solid core wire 
  * An enclosure
  * 3 x NPN type transistors(I used BC547b transistors)
  * 1x 5V LED light strip
  * Female to Male jumper wires - [ http://a.co/4jkTk8t](http://a.co/4jkTk8t)

Add TipAsk Question

## Step 2: Setting Up the Pi's Environment

I used a slanted plastic box to enclose the project so it wouldn't stand out on my shelf. I drilled a hole in the side for the serial USB cable, and positioned the Pi next to the breadboard and Pi Wedge.

Add TipAsk Question

## Step 3: Getting Your Pi Set Up (Part 1)

For this project I used the latest version of non-desktop Raspbian

A guide on how to install Raspbian can be found here: [https://www.raspberrypi.org/documentation/installa...](https://www.raspberrypi.org/documentation/installation/installing-images/)

(You may need a USB to microSD adapter for your computer)

Once Raspbian is installed onto the SD card, you can proceed to plug it in to the Raspberry Pi, and connect the Ethernet cable or USB WiFi adapter to the Pi 

Next, install Tera Term to your computer, which allows you to interface with the Raspberry Pi's terminal through your PC : [https://osdn.net/projects/ttssh2/downloads/68719/t...](https://osdn.net/projects/ttssh2/downloads/68719/teraterm-4.97.exe/)

Then, plug in the USB serial cable from the Pi wedge into the PC. It can be accessed through Tera Term. Make sure the serial port baud rate is set to 115200.

First, the Pi will post a prompt to sign in if the OS has been properly installed

The default username and password are:

Username: pi

Password: raspberry

Add TipAsk Question

## Step 4: Getting Your Pi Set Up (Part 2)

**Setting up WiFi**

In the terminal, run the command 

    
    
    sudo nano /etc/network/interfaces

Then, paste in this code and substitute the SSID and PSK with your router's name and password

    
    
    auto lo 
    
    iface lo inet loopback
    
    iface eth0 inet dhcp 
    
    allow-hotplug wlan0
    
    auto wlan0
    
    iface wlan0 inet dhcp        
    
    	wpa-ssid "ssid"
    
    wpa-psk "password"

This file lets the Pi connect to your WiFi

Next, restart the Pi with the line

    
    
    sudo reboot
    

**Installing Web Server**

Log in, and then install the Apache server with

    
    
    sudo apt-get install apache2 -y
    

and

    
    
    sudo apt-get install php libapache2-mod-php -y

To find your Pi's IP address run the command

    
    
    hostname -I

Use your browse to access the IP that is shown in order to check if it works.

For example, in Google Chrome I would type 192.168.1.72 into the address bar.

Documentation you should follow can be found at [https://www.raspberrypi.org/documentation/remote-a...](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)

The PiGPIO library also needs to be installed, which allows you to control the data being sent over the GPIO pins.

    
    
    sudo apt-get install build-essential unzip wget

and

    
    
    wget http://abyz.co.uk/rpi/pigpio/pigpio.zip && unzip pigpio.zip && cd PIGPIO && sudo make install

Add TipAsk Question

## Step 5: Writing the Code

Navigate to /var/www/html with the line

    
    
    cd /var/www/html

In the directory, there will be a default html file, which you will need to edit.

    
    
    sudo nano index.html

Inside Nano, delete anything already there and replace it with the following code.

(Tera Term can be a little funky with copying and pasting, but usually once you have copied text, alt+v should do the job)

    
    
    <html>
    <head>
    <script>
    function readRGB(color){
    if (color.length == 0) {
    	document.getElementById("txtHint").innerHTML = "";
    	return;
    }
    else {
    	var xmlhttp = new XMLHttpRequest();
    	xmlhttp.onreadystatechange = function() {
    		if (this.readyState == 4 && this.status == 400) {
    			document.getElementById("txtHint").innerHTML = this.responseText;
    		}
    	};
    	temp = encodeURIComponent(color);
    	xmlhttp.open("GET", "action_page.php?q=" + temp, true);
    	xmlhttp.send();
    	}
    }
    </script>
    </head>
    <body>
    <form action="/action_page.php" method="post">
    	Select A Color:
    	<input type="color" name="favcolor" value="#ff0000" onchange="readRGB(this.value)">
    
    </body>
    </html>

Then save it as main.html, instead of index.html

The code above acts as the button you press, and as the code that sends the color you select to the other file.

Next, run the command

    
    
    sudo nano

and paste in

    
    
    <?php
    //get the q parameter from URL
    $q = $_REQUEST["q"];
    
    $hint = "";
    $hex = urldecode($q);
    list($r, $g, $b) = sscanf($hex, "#%02x%02x%02x");
    
    echo "$hex -> $r $g $b";
    exec("pigs p 17 $g");
    exec("pigs p 22 $r");
    exec("pigs p 22 $b");
    ?>
    

and save it as action_page.php

This code receives the RGB value, and sets the PWM values on the LED strip.

Add TipAsk Question

## Step 6: Circuit Design

Now that all the software is set up, it is time to work on the hardware.

The goal of the circuit is to send PWM (Pulse Width Modulated) signals from the Pi to the LED array.

The LED strip has four pins: red, green, blue, and power (5 volts in my case).

Each PWM pin controls one of the three colors through a transistor, which acts as a switch.

Each transistor has three pins: collector, base, and emitter.

The PWM signal controls the duty cycle (how long the switch turns on and off).

The duty cycle results in the lights being darker or brighter.

Because the lights switch on and off so fast, people see it as solid light with varying brightness. 

NOTE: In the schematic, the LED symbols represent the LED array and the current limiting resistors within the wire.

Add TipAsk Question

## Step 7: Buttering Your Bread . . . Board

While making connections, be sure to have the Pi powered off.

Place the Pi wedge with one row of pins on either half of the breadboard, and connect it to the Pi with the ribbon cable. I used solid core wire to reduce the clutter on the breadboard, and to make sure nothing would get accidentally unplugged.

Place the transistors on the upper half of the breadboard (column A), and connect the LED array on the lower half (rows H, I, or J).

Connect the negative power rail to the GND pin on the wedge, and the positive rail to the 5V pin.

Connect the positive power rail to the LED array's power supply pin.

For each transistor,connect the emitter pin to the negative power rail and connect the collector pin to separate rows corresponding to the LED array's pins (I used row 1 as 5v, and 2, 3, and 4 as green, red, and blue, in column f). Then, connect four male to female jumper wires from the breadboard to the LED strip. 

Finally, connect the green transistor's base pin to pin 17 on the wedge, red transistor base to pin 22, and blue transistor base to pin 24.

Add TipAsk Question

## Step 8: Testing

In a web browser, navigate to the Pi's IP address, and after it write /main.html

Select a color, and be amazed by the "wonders of modern technology"!

Add TipAsk Question

## Step 9: Contact Me If You Have Any Questions/Feedback

If you have any questions or suggestions feel free to leave a comment or DM me on here and I will try to reply asap.

Good luck!

