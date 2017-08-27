---
title: ReSpeaker 2-Mics Pi HAT
category: Arduino
bzurl: https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html
prodimagename: 2mics-zero-high-res.jpg
surveyurl: https://www.research.net/r/ReSpeaker_2-Mics_Pi_HAT
sku: 107100001
---

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/2mics-zero-high-res.jpg?raw=true)

ReSpeaker 2-Mics Pi HAT is a dual-microphone expansion board for Raspberry Pi designed for AI and voice applications. This means that you can build a more powerful and flexible voice product that integrates Amazon Alexa Voice Service, Google Assistant, and so on.


The board is developed based on WM8960, a low power stereo codec. There are 2 microphones on both sides of the board for collecting sounds and it also provides 3 APA102 RGB LEDs, 1 User Button and 2 on-board Grove interfaces for expanding your applications. What is more, 3.5mm Audio Jack or JST 2.0 Speaker Out are both available for audio output.

[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png)](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html)

## Features

* Raspberry Pi compatible(Support Raspberry Pi Zero and Zero W, Raspberry Pi B+, Raspberry Pi 2 B and Raspberry Pi 3 B)
* 2 Microphones
* 2 Grove Interfaces
* 1 User Button
* 3.5mm Audio Jack
* JST2.0 Speaker Out

## Application Ideas

* Voice Interaction Application
* AI Assistant

## Hardware Overview

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/mic_hatv1.0.png?raw=true)

- BUTTON: a User Button, connected to GPIO17
- MIC\_L & MIC\_R: 2 Microphones on both sides of the board
- RGB LED: 3 APA102 RGB LEDs, connected to SPI interface
- WM8960: a low power stereo codec
- Raspberry Pi 40-Pin Headers: support Raspberry Pi Zero, Raspberry Pi 1 B+, Raspberry Pi 2 B and Raspberry Pi 3 B
- POWER: Micro USB port for powering the ReSpeaker 2-Mics Pi HAT, please power the board for providing enough current when using the speaker.
- I2C: Grove I2C port, connected to I2C-1
- GPIO12: Grove digital port, connected to GPIO12 & GPIO13
- JST 2.0 SPEAKER OUT: for connecting speaker with JST 2.0 connector
- 3.5mm AUDIO JACK: for connecting headphone or speaker with 3.5mm Audio Plug

## Usage

### Connect ReSpeaker 2-Mics Pi HAT to Raspberry Pi

Mount ReSpeaker 2-Mics Pi HAT on your Raspberry Pi, make sure that the pins are properly aligned when stacking the ReSpeaker 2-Mics Pi HAT.

![connection picture1](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/connection1.jpg?raw=true)
![connection picture2](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/connection2.jpg?raw=true)
![connection picture3](https://github.com/yexiaobo-seeedstudio/MIC_HATv1.0_for_raspberrypi/blob/master/img/stack-on-zero.jpg?raw=true)

### Setup the driver on Raspberry Pi

While the upstream wm8960 codec is not currently supported by current Pi kernel builds, upstream wm8960 has some bugs, we had fixed it. we must build it manually. Or you could download and use our [raspbian image(click for guidance)](#about-our-raspbian-image), in which the driver is pre-installed.

Get the seeed voice card source code.

```
git clone --depth=1 http://git.oschina.net/seeed-se/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh
reboot
```

Check that the sound card name matches the source code seeed-voicecard.

```
pi@raspberrypi:~ $ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: seeedvoicecard [seeed-voicecard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

Next apply the alsa controls setting

```
sudo alsactl --file=asound.state restore
```

If you want to change the alsa settings, You can use `sudo alsactl --file=asound.state store` to save it.

Test, you will hear what you say to the microphones(don't forget to plug in an earphone or a speaker):

```
arecord -f cd -Dhw:0 | aplay -Dhw:0
```

Enjoy!

### Configure sound settings and adjust the volume with **alsamixer**

**alsamixer** is a graphical mixer program for the Advanced Linux Sound Architecture (ALSA) that is used to configure sound settings and adjust the volume.

```
pi@raspberrypi:~ $ alsamixer
```

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/alsamixer.png?raw=true)

The Left and right arrow keys are used to select the channel or device and the Up and Down Arrows control the volume for the currently selected device. Quit the program with ALT+Q, or by hitting the Esc key. [More information](https://en.wikipedia.org/wiki/Alsamixer)

To test the volume after configuration:

```
arecord -f cd -Dhw:0 | aplay -Dhw:0
```

### Getting started with **Google Assistant**

There are 2 ways to get started with Google Assistant([what is  Google Assistant](https://assistant.google.com/)), the first is that you could integrate the Google Assistant Library into your raspberry pi system. Here is the link to [Google official guidance](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/run-sample). And the other way is that you could download the [raspbian image](#about-our-raspbian-image) we built, in which the Google Assistant Library and example are pre-installed. The following guide will show you how to get started with Google Assistant when using our raspbian image.

1. Configure a Developer Project and get JSON file

    Follow step 1. 2. 3. 4. in the  [guide](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/config-dev-project-and-account#config-dev-project) to configure a project on Google Cloud Platform and create an OAuth Client ID JSON file. Don't forget to copy the JSON file to your Raspberry Pi.

2. Authorize the Google Assistant SDK sample to make Google Assistant queries for the given Google Account. Reference the JSON file you copied over to the device in a previous step.
```
pi@raspberrypi:~ $ google-oauthlib-tool --client-secrets /home/pi/client_secret_client-id.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless
```
   * `/home/pi/client_secret_client-id.json` should be the path of your JSON file, your should modify the commmand above
   * After running the command, it should display as shown below. Copy the URL and paste it into a browser (this can be done on your development machine, or any other machine). After you approve, a code will appear in your browser, such as "4/XXXX". Copy this and paste this code into the terminal.
```
Please go to this URL: https://...
Enter the authorization code:
```
   * It should then display: OAuth credentials initialized.
   * If instead it displays: InvalidGrantError then an invalid code was entered. Try again, taking care to copy and paste the entire code.

3. Install **pulseaudio** and let it run in background
```
pi@raspberrypi:~ $ sudo apt install pulseaudio
pi@raspberrypi:~ $ pulseaudio &
[1] 1244
pi@raspberrypi:~ $ W: [pulseaudio] server-lookup.c: Unable to contact D-Bus: org.freedesktop.DBus.Error.NotSupported: Unable to autolaunch a dbus-daemon without a $DISPLAY for X11
W: [pulseaudio] main.c: Unable to contact D-Bus: org.freedesktop.DBus.Error.NotSupported: Unable to autolaunch a dbus-daemon without a $DISPLAY for X11
E: [pulseaudio] bluez4-util.c: org.bluez.Manager.GetProperties() failed: org.freedesktop.DBus.Error.UnknownMethod: Method "GetProperties" with signature "" on interface "org.bluez.Manager" doesn't exist
```

* the pulseaudio error log could be ignored here

4. Start the Google Assistant demo
```
pi@raspberrypi:~ $ alsamixer    // To adjust the volume
pi@raspberrypi:~ $ source env/bin/activate
(env) pi@raspberrypi:~ $ env/bin/google-assistant-demo
```

5. Say *Ok Google* or *Hey Google*, followed by your query. The Assistant should respond. If the Assistant does not respond, follow the [troubleshooting instructions](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/troubleshooting#hotword).

    ![run demo](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/okgoogle.jpg?raw=true)

6. See the [Troubleshooting](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/troubleshooting) page if you run into issues.


### How to use the on-board APA102 LEDs

Each on-board APA102 LED has an additional driver chip. The driver chip takes care of receiving the desired colour via its input lines, and then holding this colour until a new command is received.

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/led.gif?raw=true)

- Activate SPI: `sudo raspi-config`; Go to "Interfacing Options"; Go to "SPI"; Enable SPI; Exit the tool and reboot
- Get the APA102 Library and sample light programs(if you are using our [raspbian image](#about-our-raspbian-image), please skip this step):

```
cd ~/
git clone https://github.com/KillingJacky/APA102_Pi.git
```

- You might want to set the number of LEDs to match your strip: `cd ~/APA102_Pi && nano runcolorcycle.py`; Update the number, Ctrl-X and "Yes" to save.
- Run the sample lightshow: `python runcolorcycle.py`
- [More informations](https://github.com/KillingJacky/APA102_Pi)

### How to use User Button

There is an on-board User Button, which is connected to GPIO17. Now we will try to detect it with python and RPi.GPIO.

```
sudo pip install rpi.gpio    // install RPi.GPIO library
nano button.py               // copy the following code in button.py
```

```
import RPi.GPIO as GPIO
import time

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

while True:
    state = GPIO.input(BUTTON)
    if state:
        print("off")
    else:
        print("on")
    time.sleep(1)
```

Save the code as button.py, then run it. It should display "on" when you press the button:

```
pi@raspberrypi:~ $ python button.py
off
off
on
on
off
```


### User Button triggers Google Assisant

There is an esay way to use a button(instead of speaking "ok google") to trigger Google Assisant.

- Modify `pushtotalk.py`

```
// when using our Raspbian image
cd /usr/local/lib/python2.7/dist-packages/googlesamples/assistant/grpc
sudo nano pushtotalk.py
```

Go to the buttom of the file(Line 301), then modify as the following code and save:  

```Python
    with SampleAssistant(conversation_stream,
                         grpc_channel, grpc_deadline) as assistant:
        # If file arguments are supplied:
        # exit after the first turn of the conversation.
        if input_audio_file or output_audio_file:
            assistant.converse()
            return

        # If no file arguments supplied:
        # keep recording voice requests using the microphone
        # and playing back assistant response using the speaker.
        # When the once flag is set, don't wait for a trigger. Otherwise, wait.
        wait_for_user_trigger = not once
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.IN)
        while True:
            if wait_for_user_trigger:
                state = GPIO.input(17)
                logging.info('Press the button to send a new request...')
                if state:
                    continue
                else:
                    pass
               # click.pause(info='Press Enter to send a new request...')
            continue_conversation = assistant.converse()
            # wait for user trigger if there is no follow-up turn in
            # the conversation.
            wait_for_user_trigger = not continue_conversation

            # If we only want one conversation, break.
            if once and (not continue_conversation):
                break


if __name__ == '__main__':
    main()
```

- Run the command to test:

```
$ googlesamples-assistant-pushtotalk
```

- The demo will be displayed as below:

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/button.jpg?raw=true)


### About our Raspbian image

We have built a Raspbian iamge for your convenience, in which ReSpeaker 2-Mics Pi HAT driver, the Google Assistant Library and APA102 LEDs library are pre-installed.

- [Download our Raspbian image](https://s3-us-west-2.amazonaws.com/wiki.seeed.cc/001share/seeed-raspbian-jessie-20170523.7z)

- [How to install the image](https://www.raspberrypi.org/documentation/installation/installing-images/)


## Resources
- [Download our Raspbian image](https://s3-us-west-2.amazonaws.com/wiki.seeed.cc/001share/seeed-raspbian-jessie-20170523.7z)
- [Schematics in Eagle](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/src/ReSpeaker%202-Mics%20Pi%20HAT.sch)
- [PCB in Eagle](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/src/ReSpeaker%202-Mics%20Pi%20HAT.brd)
