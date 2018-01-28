# Raspberry Pi Wifi Controlled Video Streaming Robot

_Captured: 2017-11-16 at 10:26 from [www.instructables.com](http://www.instructables.com/id/Raspberry-Pi-Wifi-Video-Streaming-Robot/)_

![](https://cdn.instructables.com/F9J/MY3S/J9SVVRMP/F9JMY3SJ9SVVRMP.MEDIUM.jpg)

Ever thought about building a cool robot with a camera on it ? Well, you came to the right place, I will show you step by step about how to build this robot.

With this you can go ghost hunting at night by controlling and seeing the video feed on your computer or drive it outside and just explore while sitting inside, it is very fun to drive.

## Step 1: Materials Required

![](https://cdn.instructables.com/FVP/4R5O/J9SW35DU/FVP4R5OJ9SW35DU.MEDIUM.jpg)

1\. Raspberry Pi

2\. USB WiFi Adapter (If you are using raspberry pi 2)

3\. USB Webcam

4\. SD Card with Raspbian installed

5\. Power Bank

6\. Robot Chassis with Motors (I used 300 rpm motors)

7\. L293D IC or L298 Motor Driver

8\. 9v Battery or a Battery Pack (If you are using a 9v battery then I would recommend to connect 2 in parallel)

9\. A Switch

10\. Breadboard or PCB if you prefer to solder

11\. M/M and and M/F Jumper wires

Tools

1\. Soldering Iron

2\. Screwdriver

3\. Double Sided Tape

## Step 2: Assembling the Chassis

![](https://cdn.instructables.com/FSZ/JNEU/J9SW37B9/FSZJNEUJ9SW37B9.MEDIUM.jpg)

Solder wires onto the motors and mount the motors on the chassis. If you don't have a soldering iron then you can twist the wires and attach them with electrical tape but it is not recommended as it will be quite a weak joint. Then insert the wheels into motor shafts and screw them down.

## Step 3: Preparing the Raspberry Pi

![](https://cdn.instructables.com/FTO/TOKT/J9SW3VD2/FTOTOKTJ9SW3VD2.MEDIUM.jpg)

![](https://cdn.instructables.com/FPU/R6VL/J9SW3VD0/FPUR6VLJ9SW3VD0.SMALL.jpg)

![](https://cdn.instructables.com/FV8/QE2A/J9SW3VD4/FV8QE2AJ9SW3VD4.SMALL.jpg)

1\. Install Raspbian on a SD Card and boot raspberry pi with a monitor, keyboard, mouse, wifi adapter and webcam connected.

2\. From the raspi-config menu enable ssh

3\. Go into the desktop and connect to your wifi network from the wifi option on the top right corner

4\. Once connected check your Pi's ip address by typing ifconfig in the terminal

5\. Open IDLE 2 from the programming tab from the taskbar and copy the code pi_robot and save it

6\. To install the webcam I want you to watch this video made by Anand Nayyar

7\. The other things I did was to change the resolution to 720p instead of 480p and search for "stream_maxrate" and change it to 3. To achieve a higher fps in streaming I also overclocked the Pi to 1ghz

TROUBLESHOOTING

When I tried to run the code in terminal with the command "cd Videos"(Because that's where I saved it) then "python pi_robot.py" it said syntax error so what I did was open the code in terminal with the command "sudo nano pi_robot.py" and erased the lines that already written in python and are not a part of the code and after that it worked. I don't know what was wrong so if anyone knows I would be happy to hear an explanation about this in the comments.

## Step 4: Circuit

![](https://cdn.instructables.com/FYG/KU6X/J9OWHVW8/FYGKU6XJ9OWHVW8.MEDIUM.jpg)

![](https://cdn.instructables.com/FHO/21OO/J9OWHV1V/FHO21OOJ9OWHV1V.SMALL.jpg)

![](https://cdn.instructables.com/FXX/ZUML/J9SVUQKT/FXXZUMLJ9SVUQKT.MEDIUM.jpg)

The circuit is pretty simple and it gets even simpler if you use a L298 motor driver board. If you are using a L298 motor driver board then you just have to wire the gpio pins like in the second schematic.

## Step 5: Mounting Everything on the Chassis

![](https://cdn.instructables.com/FQX/VX1V/J9SVUQMR/FQXVX1VJ9SVUQMR.MEDIUM.jpg)

![](https://cdn.instructables.com/FWH/FNQZ/J9SVUQU1/FWHFNQZJ9SVUQU1.SMALL.jpg)

![](https://cdn.instructables.com/FBU/OEX8/J9SVUQQ0/FBUOEX8J9SVUQQ0.SMALL.jpg)

Well the pictures tell pretty much everything about how I have assembled it but of course yours will be different if you use a different chassis. I used double sided foam tape to mount everything on the chassis and try to use shorter wires so , it looks better.

## Step 6: How to Operate It

![](https://www.instructables.com/files/deriv/FE0/OC08/J9SVURP2/FE0OC08J9SVURP2.MEDIUM.jpg)

![](https://cdn.instructables.com/F1D/T356/J9SW3VSB/F1DT356J9SW3VSB.SMALL.jpg)

![](https://cdn.instructables.com/FFP/7OC2/J9SW39GO/FFP7OC2J9SW39GO.SMALL.jpg)

To start controlling your robot follow the following steps -

1\. Switch on the Raspberry Pi but do not flip on the switch that connects the battery pack to the L293D yet

2\. Connect to it through ssh using the program putty if you are on windows

3\. Type in the command "sudo motion" and then open your internet browser and type in your Pi's IP address with 8081 at the end like "192.168.45.64:8081" and you should get the video feed. If it doesn't work then type 8080 instead of 8081

4\. Now go back to the terminal and locate where you had saved your pi_robot.py file. I had saved it in the Videos folder, so the command is,"cd Videos" then "python pi_robot.py". Remember, everything is case sensitive

5\. After that the program will start running. Now flip on the switch, now you should be able to control the robot from the arrow keys of your keyboard

6\. Press the forward arrow and check if both the motors are moving in the right direction. If one of the motors is moving in the wrong direction then switch the two motor connections that connect to the L293D

## Step 7: Controlling From a Phone

![](https://cdn.instructables.com/FR5/3YY5/J9SVUWF1/FR53YY5J9SVUWF1.MEDIUM.jpg)

![](https://cdn.instructables.com/FYX/8BQZ/J9SVUWEZ/FYX8BQZJ9SVUWEZ.SMALL.jpg)

![](https://cdn.instructables.com/FGN/1ZDJ/J9SVUWF0/FGN1ZDJJ9SVUWF0.SMALL.jpg)

All the steps are the same, you just have download the app "JuiceSSH" from the play store. To control the robot you need arrow keys but a normal smartphone keyboard doesn't have arrow keys so we need to download an app Hacker's Keyboard'. Then connect to it like you did in windows.

## Step 8: Some Pictures and Videos
