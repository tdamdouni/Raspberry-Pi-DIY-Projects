# Get the Voice Kit SD Image

_Captured: 2017-05-19 at 11:12 from [aiyprojects.withgoogle.com](https://aiyprojects.withgoogle.com/voice#makers-guide-5-1--log-data-and-debugging)_

![Materials](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/materials.jpg)

![Assemble the hardware image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/hardware-1.jpg)

![Assemble the hardware image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/hardware-2.jpg)

![Assemble the hardware image 3](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/hardware-3.jpg)

![Assemble the hardware image 7](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/hardware-7.jpg)

![Build the box image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/box-1.jpg)

![Build the box image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/box-2.jpg)

![Build the box image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/frame-1.jpg)

![Build the box image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/frame-2.jpg)

![Build the box image 3](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/frame-3.jpg)

![Put it all together image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/together-1.jpg)

![Put it all together image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/together-2.jpg)

![Put it all together image 3](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/together-3.jpg)

![Plug peripherals in](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/peripherals.jpg)

> _Now that your box is assembled, plug your peripherals in:_

![Build the box image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/insert-1.jpg)

![Build the box image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/connect-1.jpg)

![Check audio image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/audio-1.png)

![Check audio image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/assembly/audio-2.png)

![Check WiFi image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/wifi-1.png)

![Check WiFi image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/wifi-2.png)

![Log into GCP 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/log-1.jpg)

![Create a project 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/create-1.png)

![Create a project 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/create-2.png)

![Create a project 3](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/create-3.png)

![Turn on the Google Assistant API image 1](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/api-1.png)

![Turn on the Google Assistant API image 2](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/api-2.png)

![Turn on the Google Assistant API image 3](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/users/api-3.png)
    
    
    
    
       
    
     
    
        
    
           
            
             
              
            self.value = value
    
        def run(self, command):
            GPIO.output(self.gpio, self.value)
    

Then add the following lines to `~/voice-recognizer-raspi/src/action.py` below the comment "Add your own voice commands here":
    
    
        # =========================================
        # Makers! Add your own voice commands here.
        # =========================================
    
        actor.add_keyword('light on', GpioWrite(4, True))
        actor.add_keyword('light off', GpioWrite(4, False))
    

![GPIO](https://aiyprojects.withgoogle.com/static/images/aiy-projects-voice/makers/sensors.png)

Function GPIO Description

Button
23
button is active low

LED
25
LED is active high

Driver0/GPIO4
4
500mA drive limit, can be used as GPIO

Driver1/GPIO17
17
500mA drive limit, can be used as GPIO

Driver2/GPIO27
27
500mA drive limit, can be used as GPIO

Driver3/GPIO22
22
500mA drive limit, can be used as GPIO

Servo0/GPIO26
26
25mA drive limit, can be used as GPIO

Servo1/GPIO6
6
25mA drive limit, can be used as GPIO

Servo2/GPIO13
13
25mA drive limit, can be used as GPIO

Servo3/GPIO5
5
25mA drive limit, can be used as GPIO

Servo4/GPIO12
12
25mA drive limit, can be used as GPIO

Servo5/GPIO24
24
25mA drive limit, can be used as GPIO

I2S
20, 21, 19
used by Voice HAT ALSA driver, not available to user

Amp Shutdown
16
used by Voice HAT ALSA driver, not available to user

I2C
2, 3
available as GPIO or I2C via Raspbian drivers

SPI
10, 9, 11, 24, 26
available as GPIO or SPI via Raspbian drivers

UART
14, 15
available as GPIO or UART via Raspbian drivers

You can view logs to get a better sense of what's happening under the (cardboard) hood if you're running the voice-recognizer as a service.

With the voice-recognizer running manually or as a service, you can view all log output using journalctl.

`sudo journalctl -u voice-recognizer -n 10 -f`
    
    
    Clap your hands then speak, or press Ctrl+C to quit...
    [2016-12-19 10:41:54,425] INFO:trigger:clap detected
    [2016-12-19 10:41:54,426] INFO:main:listening...
    [2016-12-19 10:41:54,427] INFO:main:recognizing...
    [2016-12-19 10:41:55,048] INFO:oauth2client.client:Refreshing access_token
    [2016-12-19 10:41:55,899] INFO:speech:endpointer_type: START_OF_SPEECH
    [2016-12-19 10:41:57,522] INFO:speech:endpointer_type: END_OF_UTTERANCE
    [2016-12-19 10:41:57,523] INFO:speech:endpointer_type: END_OF_AUDIO
    [2016-12-19 10:41:57,524] INFO:main:thinking...
    [2016-12-19 10:41:57,606] INFO:main:command: light on
    [2016-12-19 10:41:57,614] INFO:main:ready...
    

  1. Any lines before and including this one are part of the initialization and are not important
  2. Here is where the main loop starts
  3. Each successful trigger is logged
  4. Once a trigger is recognized the audio recording will be activated
  5. … and a new session with the Cloud Speech API is started
  6. For this a new token is generated to send the recognition request
  7. Same as line 7

  8. Same as line 7
  9. Back in the application, where we dispatch the command
  10. The command that has been dispatched
  11. The app is ready and wait for a trigger again

## Project complete!

You did it! Whether this was your first hackable project or you're a seasoned maker, we hope this project has sparked new ideas for you. Keep tinkering, there's more to come.
