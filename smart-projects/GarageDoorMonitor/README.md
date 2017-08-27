# README #

This repo contains the source code for a system of MQTT networked ESP32 based devices to help monitor door switch status and light up LEDs based on the door status. Specifically created for garage doors.

Features:

* two build outputs: switch monitor build and led indicator build
* MQTT based, business logic is implemented "elsewhere." FWIW: I used Node-RED to manage the switch events and handle the logic to light up the indicator unit.

## Target Hardware ##

### Components ###

* [Sparkfun ESP32 Thing](https://www.sparkfun.com/products/13907)
* [Adafruit NeoPixel Digital RGB LED Strip - Black 60 LED](https://www.adafruit.com/products/1461)
* Code as published assumes 60 LEDs per device, but is easy to change.

### Wiring / GPIO usage ###
* GPIO 5: LED and crude CPU usage monitor
* GPIO 21: LED Strip data connection
* GPIO 16: Switch 1
* GPIO 17: Switch 2
* 3.3v: tied to switches

It is assumed (and recommended) that the LED Strip itself is externally powered, due to heavy peak current demands with some LED patterns.

## Setup ##

### Minimum Requirements ###

* [ESP-IDF](https://github.com/espressif/esp-idf) installed correctly on the development system. This code was tested against the latest IDF as of early March 2017. *NOTE: The ESP-IDF is a rapidly moving target. Your mileage may vary.*
* FWIW, development for this project was performed using Mac OSX, and using Eclipse for editing
* I used the ESP32 Thing's built in serial bootloader to download new application code builds using the IDF's "make flash" feature. For faster downloads, I highly suggest using "make menuconfig" to increase the bootloader's serial bit rate AND use compression.

### Configuration ###

#### Wifi and MQTT ####

* The wifi setup may be updated via "make menuconfig". See "Component Config"->"EshThing" to update SSID and password.
* The target MQTT server may be updated via "make menuconfig". See "Component Config"->"EshThing" to update the target MQTT server.
* The MQTT clientID may be updated via "make menuconfig". See "Component Config"->"EshThing" to update the MQTT ClientId.

#### MQTT Topics ####

The switch monitor will publish the state of the switch, when the state changes, to the following MQTT topic:

/EshThings/Events/**CLIENT_ID**/Switch**NUM**/Status

The indicator unit subscribes to the following topic:

/EshThings/Indicators/**CLIENT_ID**/Pattern

Patterns:

* '0' None
* '1' Hann Window Pulse (single pulse then off)
* '2' Hann Window Pulse (repeats forever)
* '3' Random Noise
* '4' Morse Code SOS Pattern
* '5' Same as '1', but scaled for different color range
* '6' Same as '2', but scaled for different color range
* '7' Knight Rider!
* '8' Solid all white
* '9' First half all white
* '10' Second half all white


## Third Party ##

Third party code and modules required or included directly in this project:

* [ESP-IDF](https://github.com/espressif/esp-idf) 
* [ESP32_LED_STRIP aka led_strip](https://github.com/Lucas-Bruder/ESP32_LED_STRIP) 
* [esp32-mqtt](https://github.com/tuanpmt/esp32-mqtt)

Other resources:

* [Code - heatmaps and color gradients](http://www.andrewnoske.com/wiki/Code_-_heatmaps_and_color_gradients)


## Who do I talk to? ##

* Feel free to contact [Matthew Eshleman](https://covemountainsoftware.com/consulting/) if any interest or issues with this code.
* Reach out to the [ESP32 community](http://esp32.com/) for ESP32 or ESP32-IDF specific issues.
