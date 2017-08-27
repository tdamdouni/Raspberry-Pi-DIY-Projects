# Raspberry Pi, Camera, Node.js – Video & Email The Intruder

_Captured: 2017-08-23 at 23:56 from [thejackalofjavascript.com](http://thejackalofjavascript.com/rpi-video-the-intruder/)_

In one of my earlier posts : [Raspberry pi, PIR Sensor and Node.js - An IoT Intruder Alert system](http://thejackalofjavascript.com/rpi-pir-sensor-node-iot-intruder-alert/), I have shown how you can detect intruders with Raspberry Pi and a PIR sensor. And once the intruder is detected, an email will be sent with the time of incident.

This is good but not that helpful. In this post, instead of just sending an email, we will record a video of the intruder as the "act" is performed and then attach that video along with the email. Sweet right!

Below is a quick demo that show how things work

The video is a bit fast and too shaky. So Let me quickly run you through it. First we start the node program. As soon as a intruder is detected, the buzzer gets triggered. At the same time, we start the recording on the camera. We record a video for 10 seconds and then start sending the same in an email.

Pretty sweet right!

You can find the completed code [here](https://github.com/arvindr21/pi_videoEMailIntruder).

So let us get started building this IoT Video and Email The Intruder system!

## Prerequisites

If you are new to Raspberry pi and have not yet installed Node.js on it, I would recommend going through [Getting Started with Raspberry pi and Node.js](http://thejackalofjavascript.com/getting-started-raspberry-pi-node-js/).

If you are new to electronics devices and circuits, I would recommend going through the [video lectures](http://www.allaboutcircuits.com/videos/index.html) from All About Circuits.

### Components needed

  1. 1 - Raspberry pi B+
  2. 1 - Raspberry pi camera
  3. 1 - Breadboard
  4. 1 - PIR Sensor
  5. 9 - Female to Male connectors

If you are new to Raspberry Pi GPIO, please refer [this](http://thejackalofjavascript.com/raspberry-pi-node-js-led-emit-morse-code/#gpio).

I have already written a post that explains how to implement the intruder alert system that sends an email : [Raspberry pi, PIR Sensor and Node.js - An IoT Intruder Alert system](http://thejackalofjavascript.com/rpi-pir-sensor-node-iot-intruder-alert/). I will continue from the output of that post to avoid repetition.

## Setup Filezilla

Before we start capturing stuff, we need an easy way to view all our captures. Since we are going to use ssh to run our capture commands, we will need to retrieve the saved files. Of course you can use VNC to connect to the Pi and view the files too. But for the sake of simplicity, we will use [Filezilla](https://filezilla-project.org/).

> FileZilla is free, cross-platform FTP application software, consisting of FileZilla Client and FileZilla Server. Binaries are available for Windows, Linux, and Mac OS X. It supports FTP, SFTP, and FTPS (FTP over SSL/TLS).

We are going to connect to our pi using Filezilla and access the directories and files.

You can download Filezilla _**client**_ for your OS from [here](https://filezilla-project.org/). We will start using it in a moment.

## Setup Raspberry Pi Camera

If you have not already mounted the Camera on the pi, I would recommend following the below video to do so.

Once that is done, you can test the camera. Make sure the camera module is properly mounted before booting the Pi.

By default the camera module is not enabled, so we need to enable it. Once your Pi is booted completed and you have connected to it via ssh, you can run

sudo raspi-config

This will bring up the config screen, which will look like

Using the down arrow key, select the Enable Camera option. Then press enter and you should see

Use the right arrow key to select Enable and press enter. Once the Camera is enabled, you will be take to the config screen.

Use the right arrow key to select Finish and press enter. You will be asked to reboot, press yes.

Once the reboot is completed, Login to your pi again. Now that we have enabled the camera, lets capture things!

As soon as you ssh into pi, you will be landing inside the _/home/pi_ folder. If you want you can create a folder named _media _to save all the captures and CD into that folder.

We will first capture a picture. From terminal/putty run

raspistill -o myImage.jpg

The camera should turn on (_Red LED next to the lens_) and a picture will be taken _after_ 5 seconds. Once that is done, we will get the saved image to our computer to view it.

Launch FIlezilla. Once Filezilla opens up, Go to File > Site Manager. Here we will create a new Site and hook it up to the Pi. This is an one time operation and from next time on, you can select the site and click on connect button directly.

Click on the New Site button from the Site Manager, located at the bottom left hand corner and update it as below

The Host is the IP address of your Pi and the username/password are pi/raspberry. Now click on connect button to connect to your Pi and you will see a screen like

The left hand section is your local file structure and the right hand is your Pi. Now, you can navigate to the _media_ folder and drag and drop files from right bottom panel to left bottom panel. And you can view your files on your machine!

So everytime you capture something, you can simply drag and drop from right to left.

Simple and easy!

Now we will capture a video. From terminal/putty run

raspivid -o myVideo.h264 -t 10000

And this starts the camera and records a video for 10 seconds. Once that is done, it will be saved as _h264_ video.

Again you can use Filezilla to get the video to your local and you can play it using VLC player.

If you want to convert the _h264_ format to say mp4, you can use [FFmpeg](https://www.ffmpeg.org/). You can download the appropriate version for your OS [here](https://www.ffmpeg.org/download.html).

Once FFmpeg is setup, you can run the below command

ffmpeg -r 30 -i myVideo.h264 -vcodec copy pi_cam_recording.mp4

Now you can play this file with any mp4 player. Simple and easy right!

Now let us use this camera in a real time scenario.

## Building the Intruder Detection System

Continuing from my earlier post, we are now in a state where the embedded system sends an email when an intruder is detected. Now we will update that program.

Updated _index.js_ as below

123456789101112131415161718192021222324252627282930313233343536373839 
var Gpio = require('onoff').Gpio,buzzer = new Gpio(18, 'out'),pir = new Gpio(17, 'in', 'both');var isRec = false;pir.watch(function(err, value) {if (err) exit();buzzer.writeSync(value);console.log('Intruder detected..');if (value == 1 && !isRec) {console.log('capturing video.. ');isRec = true;var exec = require('child_process').exec;var video_path = './video/video' + Date.now() + '.h264';var cmd = 'raspivid -o ' + video_path + ' -t 10000';exec(cmd, function(error, stdout, stderr) {// output is in stdoutconsole.log('Video Saved @ : ', video_path);require('./mailer').sendEmail(video_path);isRec = false;});}});console.log('Pi Bot deployed successfully!');console.log('Guarding...');function exit() {buzzer.unexport();pir.unexport();process.exit();}

We have updated the pir.watch(). If the value reads high, and if the recording is not in progress, we will trigger the recording on line 20. And once that operation is completed, we will trigger the email.

The updated _mailer.js_ would be

Do notice line 28. This where we are attaching the video to the email.

Now to test the application, run

sudo node index.js

And the guarding begins! Once the intruder is detected, the camera should start recording and once done, the email will be sent with the attachment.

You will notice some lag between the trigger and when the video actually starts recording. One solution is to position the PIR sensor in such a way that it detects the intruder a bit early and then by the time the recording starts, the intruder is in frame.

Hope this post gave you an ideas as how to use a Raspberry pi camera module along with a real time use case.

Thanks for reading! Do comment.  
@arvindr21
