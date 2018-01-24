# Raspberry Pi Zero W and Node-RED MQTT Surveillance Camera for Home Assistant

_Captured: 2017-11-08 at 23:39 from [diyprojects.io](https://diyprojects.io/raspberry-pi-zero-w-node-red-mqtt-surveillance-camera-home-assistant/#.WgOGxkq1Kf0)_

**Since version 1.3, the Raspberry Pi Zero has a camera connector on which the 8MP camera of the Raspberry Pi can be connected by means of an adapter**. Home Assistant supports many cameras. In this project, we will be manufacturing - very quickly - a mini surveillance camera using Node-RED. Node-RED will be used to take a snapshot at regular intervals and send the image to Home Assistant by an MQTT message.

Home Assistant supports many types of camera (full list). Since version 0.46, Netgear's Arlo cameras are partially supported.

To make a DIY surveillance camera from a Raspberry Pi Zero W, we have several solutions at our disposal:

  * [FFmpeg Camera](https://home-assistant.io/components/camera.ffmpeg/): There is no official package for Raspbian. It is therefore necessary to [compile the sources](http://engineer2you.blogspot.fr/2016/10/rasbperry-pi-ffmpeg-install-and-stream.html) directly on the Raspberry which is rather long.
  * [Raspberry Pi Camera](https://home-assistant.io/components/camera.rpi_camera/): Convenient to monitor your desktop if the Home Assistant server is running on a Raspberry Pi

To write this article, I started (probably like everyone!) To install Motion on my Raspberry Pi Zero and built-in Home Assistant video stream using the Generic MJPEG IP Camera component. But it does not work. Currently, (unless I'm mistaken), Home Assistant does not display any images on the views. In the detail view only the image (video stream) is displayed.

So I turned to MQTT. The advantage of MQTT is that it is possible to create a smart connected surveillance camera. Using MQTT to communicate with Home Assistant, you can add other functions to the camera:

  * Lighting
  * Connect a speaker and broadcast audio recordings: alarm, dog barking, siren …
  * Trigger the opening of a gate or a gate
  * Transforming the camera into a video door entry system
  * …

**Why Node-RED. Simply because there will be absolutely no programming to do! Three nodes are enough to create a connected surveillance camera!**

There are three versions of the Raspberry Pi Zero. If you take the train en route, here is a short summary

  1. The first version of the Raspberry Pi Zero is marketed at a price of $6 in 2015.
  2. A few months later, the foundation adds a camera connector. This is version 1.3.
  3. In 2017, the Raspberry Pi Zero W integrating WiFi and Bluetooth 4.0 is launched at [the price of $13](http://geni.us/kOl0).
![raspberry pi zero camera surveillance node-red home assistant](https://projetsdiy.fr/wp-content/uploads/2017/06/raspberry-pi-zero-camera-surveillance-node-red-home-assistant.jpg)

Here are some camera models you can buy to make a surveillance camera from a Raspberry Pi Zero. The NoIR model is best suited as it allows, with additional lighting (2 infrared LED for example) to obtain a night surveillance camera up to 10 m approx.

![raspberry pi v2.1 noir camera official](https://projetsdiy.fr/wp-content/uploads/2017/01/raspberry-pi-v2.1-noir-camera-official.jpg)

![noir compatible camera raspberry pi](https://projetsdiy.fr/wp-content/uploads/2017/01/noir-compatible-camera-raspberry-pi.jpg)

The camera connector that equips the Raspberry Pi Zero W is different from the Raspberry Pi 3 (or earlier). There is a version specific to Zero. In fact, it is the connection cable that changes. If you already have an Asian camera or clone, you can buy a compatible tablecloth for [about $2](https://www.banggood.com/search/ribbon-camera-raspberry-pi.html?p=RA18043558422201601).

![adaptateur nappe camera raspberry pi zero 1.3](https://projetsdiy.fr/wp-content/uploads/2017/01/adaptateur-nappe-camera-raspberry-pi-zero-1.3.jpg)

If you have just purchased your Raspberry Pi Zero W, follow these steps to prepare your system:

Start by activating the camera using raspi-config

Go to option (5) Interfacing Option

![raspberry pi i2c raspi-config](https://projetsdiy.fr/wp-content/uploads/2017/06/1-raspberry-pi-i2c-raspi-config-.jpg)

Then activate the camera module (P1)

![raspberry pi i2c activate raspi-config](https://projetsdiy.fr/wp-content/uploads/2017/06/2-raspberry-pi-i2c-activate-raspi-config-.jpg)

This done, run the following command to change the driver of the camera

The loading of the driver at the start is made permanent by executing

Now restart the system to activate the changes

For this project, we will use the flow **node-red-contrib-camerapi** which allows to take a snapshot using the Python Picamera library (presented in detail in [this tutorial](https://diyprojects.io/picamera-version-1-9-control-the-raspberry-pi-camera-in-python/)). Run this command to install it.

Open the palette manager

![node-red manage palette](https://www.projetsdiy.fr/wp-content/uploads/2016/10/6.-node-red-manage-palette.png)

Enter the camera in the search field and then start installing the module by pressing install.

![camera raspberry pi zero node-red](https://projetsdiy.fr/wp-content/uploads/2017/06/1-camera-raspberry-pi-zero-node-red.jpg)

Everything is ready to encode your surveillance camera.

Now that everything works, we will use Node-RED to capture an image at regular intervals. MQTT is not designed to support a video stream. On the other hand, as messages will circulate on your local network and potentially be sent to your smartphone when you leave your home, it is necessary to limit the size of the image. It's a shame when you have an 8MP camera, but we will have to limit the resolution. If you are using the mobile app for iOS, limit it to 320 x 240 pixels. For use on a LAN only, you can increase the resolution to 640 x 480 pixels.

It's gone for programming. Drop an Inject node. Select the repeat type and specify the shooting interval. As for the resolution, it is useless to be too greedy. A shot every 5 seconds is enough to see what's in a room.

![cliche camera raspberry pi](https://projetsdiy.fr/wp-content/uploads/2017/06/0-cliche-camera-raspberry-pi.png)

In the search box, type camera to find the module's take-up node

![camerapi node-red take picture raspberry pi zero](https://projetsdiy.fr/wp-content/uploads/2017/06/2-camerapi-node-red-take-picture-raspberry-pi-zero.png)

Place it on the flow and double click and edit the parameters like this:

  * **File Mode**: buffermode. No files will be stored locally. MQTT supports sending the buffer.
  * **Resolution**: 320 x 240 (recommended)
  * You can orient or reverse the image according to the position of the camera with the flip and rotate option
  * You can adjust the contrast, brightness …
  * Finally (unnecessary for a surveillance camera), you can add an effect (negative, blur …)
![camera raspberry pi node-red node configuration](https://projetsdiy.fr/wp-content/uploads/2017/06/4-camera-raspberry-pi-node-red-node-configuration.png)

As you can see, there is no compression. This is also a reason to limit the size of the image.

![camera debug buffermode correct raspberry pi zero](https://projetsdiy.fr/wp-content/uploads/2017/06/3-camera-debug-buffermode-correct-raspberry-pi-zero.png)

To test that everything works well, you can plug in a node debug and deploy flow. In the debug tab, you must get an object containing a number table (the buffer of the image). If you get an empty string, go to the end of the tutorial to identify and fix the problem.

MQTT is natively supported by Node-RED. Look for the MQTT flow in the palette and place an MQTT output node on the flow.

MQTT is natively supported by Node-RED. Look for the MQTT flow in the palette and place an MQTT output node on the flow.

![](https://projetsdiy.fr/wp-content/uploads/2017/06/5-node-red-mqtt-input-output-node.png)

Open the node to edit it.

Click the pencil to set up a new connection. On the first tab, enter the IP address (or Internet address if you are using an online Broker)

![](https://projetsdiy.fr/wp-content/uploads/2017/06/6-node-mqtt-output-connection-broker-mosquitto.png)

If you have set up a password authentication, go to the second tab and fill in the Username and Password fields

Validate the connection by clicking **Add**. Back on the MQTT node control panel, select the connection from the list. Finally, indicate an MQTT Topic. Here, all images will be published on the Topic camera/pizerow . As the images are published regularly, you can leave the QoS on 0 (the messages are sent without warranty of reception) and retain on false (when a new client connects, it will not be able to recover the old messages - images). Click **Done** to finish.

![](https://projetsdiy.fr/wp-content/uploads/2017/06/8-mqtt-node-red-send-image-camera-security-home-assistant-raspberry-pi.png)

The programming of your camera is complete. Deploy Flow

![camera security raspberry pi zero w node-red flow](https://projetsdiy.fr/wp-content/uploads/2017/06/9-camera-security-raspberry-pi-zero-w-node-red-flow.png)

Paste this code and modify the parameters before deploying the flow

Start by adding a mqtt section and specify the connection parameters to your broker. If you have password enabled, fill in username and password, otherwise delete the settings.

1234567 
mqtt: Broker: localhost Port: 1883 Keepalive: 60 Username: <user> Password: <password> Protocol: 3.1.1

Then add a new camera section. Specify the topic on which Home Assistant must retrieve the images. Here camera / pizerow

Add the camera to a group using. Here, this will give **camera.pizerow**. To change the displayed label, add the

After rebooting, the camera is fully integrated into Home Assistant

![](https://diyprojects.io/wp-content/uploads/2017/07/raspberry-pi-zero-w-camera-surveillance-diy-node-red-mqtt.jpg)

The camerapi module for Node-RED is based on the Picamera library, if it is not installed, you will have this message

The Pictures directory does not exist on Raspbian Jessie Lite by default. You may get this error message when you first deploy flow Node-RED.

Open a Terminal and run this command to create the missing folder

Save the configuration (XTRL + X then Y - O) and restart Home Assistant

And now, thanks to Node-RED and MQTT, we have just manufactured a surveillance camera connected 100% DIY. You have a total control of the images that are sent to your home automation server or on your smartphone when you leave your home. In the next tutorial, we will add a motion detector that will send (or simply) a notification, an email or trigger a scenario on the home automation server.
