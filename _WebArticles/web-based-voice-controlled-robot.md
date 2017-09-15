# Web-Based Voice-Controlled Robot!

_Captured: 2017-09-15 at 10:46 from [www.hackster.io](https://www.hackster.io/rahul-rajan/web-based-voice-controlled-robot-2fee30)_

![Web-Based Voice-Controlled Robot!](https://hackster.imgix.net/uploads/attachments/315170/img_3568_rAGBqftcJm.JPG?auto=compress%2Cformat&w=900&h=675&fit=min)

I wanted to find a cool way to combine Arduino and the Web. I use the annyang javascript library with HTML to create a client-side web interface for speech recognition. The webpage is hosted on an Adafruit Feather HUZZAH with a built-in ESP8266. Because the Feather can only supply 3V, it is not suitable for running the servos on a robot. To fix this, I connected the Feather to a DFRobot Romeo V2 using the Arduino Wire Library. Note this project will also work with a normal Arduino instead of a Romeo V2. Please follow the instructions here- https://www.arduino.cc/en/Reference/Wire to properly wire for your Arduino.

Using the project is pretty simple. just follow these steps:

  * Make sure to follow schematic exactly to properly wire Feather and Romeo
  * Follow the instructions here: `https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide` to get started using the Feather with the Arduino IDE
  * Upload the code attached in this project: HelloServer2 should be uploaded to the Feather and the VoiceServoControlClient should be uploaded to the Romeo. **Make sure to fill in your Wifi Network details in the HelloServer2 program!**
  * Build a simple robot powered by 2 servos. Make sure to wire the servos to the Romeo not the Feather. My code uses pins 4 and 7 for the Servos.
  * Power on Feather + Romeo
  * Connect Feather to computer temporarily, open Arduino Serial monitor, and get the IP address of the server 
  * Disconnect the Feather from the computer
  * On any device with Google Chrome and connected to the same network as the Feather, go to the IP address using Chrome.
  * If the Feather, Romeo, and Servos are wired correctly, you should be able to just say the commands "up","down","left", "right", or "stop" and the robot should move!
  * Enjoy!

![Screen shot 2017 06 18 at 3 12 44 pm jboneeiibs](https://halckemy.s3.amazonaws.com/uploads/attachments/315572/screen_shot_2017-06-18_at_3_12_44_pm_JBoNEEIiBs.png)
