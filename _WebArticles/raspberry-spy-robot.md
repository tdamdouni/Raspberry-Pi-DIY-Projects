# Raspberry SPy Robot

_Captured: 2017-11-21 at 10:14 from [www.instructables.com](http://www.instructables.com/id/Raspberry-SPy-Robot/)_

![](https://cdn.instructables.com/F8X/S469/J9YJE8U1/F8XS469J9YJE8U1.MEDIUM.jpg)

![](https://cdn.instructables.com/F4X/H1KW/J9YJE8TY/F4XH1KWJ9YJE8TY.MEDIUM.jpg)

This project allows you to drive a robot via a webpage and view a livestream. It can be used to spy on pets, make sure nothing is burning in your oven, and even bird watch! [DFRobot ](https://www.dfrobot.com)provided the [Raspberry Pi 3](https://www.dfrobot.com/product-1419.html) and the [Raspberry Pi camera module](https://www.dfrobot.com/product-1179.html).

## Step 1: The Robot Electronics

![](https://cdn.instructables.com/FJG/NC9Z/J9YJE8T6/FJGNC9ZJ9YJE8T6.MEDIUM.jpg)

I began by assembling the 2WD MiniQ chassis kit from DFRobot. I slid the wheels onto the motor shafts, then inserted them into brackets and attached them to the chassis. Finally, I added the metal supports. Now it was time to build the main board. The L293d motor driver got soldered in place, along with wires running to the Raspberry Pi's GPIO pins. Next, I soldered a connector for the battery, as that will provide the main power. After the power source was added, I installed a 5V regulator.

## Step 2: Setting Up the Pi

![](https://cdn.instructables.com/FW5/KOTE/J9YJE8T5/FW5KOTEJ9YJE8T5.MEDIUM.jpg)

DFRobot reached out to me and sent their Raspberry Pi 3 and Raspberry Pi Camera Module. So after I opened up the boxes I got right to work by setting up the SD card. First I went to the [Raspberry Pi Downloads page](https://www.raspberrypi.org/downloads/raspbian/) and downloaded the most recent version of Raspbian. I then extracted the file and put it into a convenient directory. You can't just copy/paste a .img file to an SD card, you have to "burn it" onto the card. You can download a burning utility like [Etcher.io ](http://etcher.io/) to easily transfer the OS image. After the .img file was on my SD card I inserted it into the Raspberry Pi and gave it power. After about 50 seconds I unplugged the cord and removed the SD card. Next I put the SD card back into my PC and went to the "boot" directory. I opened up notepad and saved it as a blank file named "ssh" with NO extension. There was also a file I added called "wpa_supplicant.conf" and put this text into it:

network={  
ssid=<"SSID"> psk=<"PASSWD"> }

Then I saved and ejected the card and put it back into the Raspberry Pi 3. This should now allow for the usage of SSH and connecting to WiFi.

## Step 3: Getting the Camera Ready

![](https://cdn.instructables.com/FSB/QPOK/J9YJE8TF/FSBQPOKJ9YJE8TF.MEDIUM.jpg)

By default, the camera is disabled on the Pi, so you must open the terminal type **sudo raspi-config** to bring up the menu. Go to "interfacing options" and then enable the camera. Now just select "Finish" and insert the ribbon cable of the camera module into the correct area of the Pi.

## Step 4: Installing Software

There are several different softwares that can stream video, such as vlc and motion, but I decided to use the [mjpeg-streamer](https://github.com/jacksonliam/mjpg-streamer) due to its low latency and easy installation. According to the instructions on the site, do a **git clone https://github.com/jacksonliam/mjpg-streamer.git** into a folder, then type **sudo apt-get install cmake libjpeg8-dev** to install the needed libraries. Change your directory into the folder you downloaded and then type **make** followed by **sudo make install** to compile the software. Finally enter **export LD_LIBRARY_PATH=.** and to run it type ** ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"** You can access the stream by heading to http:// <The Pi's IP>:8080/stream.html to view the stream.

## Step 5: Controller

![](https://cdn.instructables.com/FBV/IIME/J9YJE8U2/FBVIIMEJ9YJE8U2.MEDIUM.jpg)

![](https://cdn.instructables.com/F6G/2MS1/J9YJE8TG/F6G2MS1J9YJE8TG.MEDIUM.jpg)

Then came the part of how to control a Raspberry Pi over WiFi, because   
Bluetooth has too little range. I decided on using a Flask server running on the Raspberry PI and an ESP8266 ESP12E module to send data to it. The ESP8266 only has one analog input, which means I couldn't use the joystick directly, as it takes two analog inputs. The best option was the ADS1115, which is an I2C device that reads analog signals at 16 bits of resolution. I simply connected SDA to 4 and SCL to 5, along with VCC and GND. The joystick X axis connects to A0 on the ADS1115, and the Y axis connects to A1. BUT, I accidentally burned out the ADS1115, so I had to resort to the next-best thing: buttons! So now my setup is an ESP8266 Sparkfun Thing Dev Board with 3 buttons- forward, right, and left. Now whenever one is pressed, it sends data to turn the wheels in that direction.

## Step 6: The Code for the Robot

![](https://cdn.instructables.com/FUE/9DZ4/J9YJE8T7/FUE9DZ4J9YJE8T7.MEDIUM.jpg)

I made a [previous project](https://www.hackster.io/gatoninja236/ww2-tank-laser-tag-sherman-panther-cdc98f) that utilized the Pi's GPIO PWM library to control motors via json, so I just re-purposed the code to accept data via a Flask app instead. Flask is a Python library that essentially turn your Pi into a webserver capable of sending and receiving data. By using PWM, the motors can be controlled with greater precision compared to tank drive. This also means the robot can go at variable speeds rather than a fixed one. My flask app is configured to change the PWM of the motors once it receives data from a GET request via http from the ESP12e. It also uses the subprocess.Popen library to run the webstreaming script in the background. I have attached code to the project page, so all that is necessary is a download.

## Step 7: Controller Code

The code was pretty simple, just take readings from the 3 pins, run them through some if statements to determine wheel direction, and finally send those values to the Raspberry Pi. The ESP8266 board addition for the Arduino IDE comes with the HTTPClient library, which handles headers and sending data. The Flask server needs to receive data via a POST call, so the code starts a connection with the Raspberry Pi webserver, then adds a header to the data denoting that it's JSON encoded, and finally it sends the data in the form of a JSON object. I added a 40 ms delay to prevent the Raspberry Pi from becoming overloaded with data.

## Step 8: Running the Raspberry SPy

![](https://cdn.instructables.com/FZ2/QDB1/J9YJE8SS/FZ2QDB1J9YJE8SS.MEDIUM.jpg)

![](https://cdn.instructables.com/F9X/QT77/J9YJE8UA/F9XQT77J9YJE8UA.MEDIUM.jpg)

All that is required is typing **sudo python ****.py** ! You should see the camera light up, and by going to the web address of the pi with the port 8080 the stream should be visible. Now you can use the controller anywhere in the house and have a live feed as well.
