# Home Automation Sonoff-Tasmota Sensors, LEDs Development Board, ESP12

_Captured: 2017-11-12 at 03:13 from [www.instructables.com](http://www.instructables.com/id/Home-Automation-Sonoff-Tasmota-Sensors-LEDs-Develo/)_

![](https://cdn.instructables.com/FKQ/S70Y/J9JFSZKD/FKQS70YJ9JFSZKD.MEDIUM.jpg)

I have been blown away by the capability of the Sonoff-Tasmota firmware for the Sonoff devices. These, combined with a Raspberry Pi loaded with Node-Red and a MQTT broker (Mosquitto) provides huge scope for delivering many home automation needs. The Sonoff-Tasmota firmware enables a good deal more than the as-supplied Sonoff units. Some examples have appeared showing sensors, such as temperature and humidity being wired in. I was concerned that this might be unsafe and may not comply with EU and US regulations because the Sonoff circuit boards may not meet the requirements for double insulation. The track separation distances on the Sonoff Basic do not appear to comply. The development here gives an alternative and safe way to explore the additional capability. This board can be powered for most applications via a USB charger. The LED strings may need greater current capability, and the 12v RGB LEDs will also require a 12v supply.

The objective of this instructable is to provide a 'get started' reference for this additional capability. It took a while to find some of the code needed and hopefully this reference will smooth the way to whatever automation task you have in mind.

Node-Red has been used as the automation client, running on a Raspberry Pi. This Instructable can be seen as an extension of my earlier [Powerful Standalone Home Automation System - Pi, Sonoff, ESP8266 and Node-Red](https://www.instructables.com/id/Powerful-Standalone-Home-Automation-System-Pi-Sono/). The examples should however be easily transferable to other platforms.

The ESP12 can be programmed in-situ by connecting a USB serial converter.

The additional functionality targeted by the ESP12 breakout board here is:

  * Temperature and humidity sensor (e.g. AM2301) 
  * I2C device/devices (temperature, pressure, humidity, ambient light - see list on the [wiki](https://github.com/arendst/Sonoff-Tasmota/wiki/Sensor-Configuration)) 
  * 5v, individually addressable RGB LED strings (Neopixels/WS2812) 
  * 12v, RGB LED strings (single programmable colour) 
  * Proximity sensor, or other sensor with on/off output 
  * IR remote control 
  * Up to 3 relays

Quite a few of these can be handled by a single ESP12! The latter two use the open collector outputs used for the RGB LED string plus appropriate changes to the configuration (that can be done via Node-Red). The system does not support both types of LED strings on one device.

So with one ESP12 device (costing £1.60) plus this board you could:

  * Measure temperature and humidity. 
  * Communicate with a range of I2C devices for temperatue, humidity, pressure, ambient light. 
  * Drive a NeoPixel LED light string display. This could be used to make a mood-light. 
  * Add a proximity sensor for house alarm (email alert) 
  * Select TV, HiFi etc. settings using the IR via a remote control interface(s) on ones smartphone. 
  * Drive a couple of relays for other devices.

The board is small and cheap enough that one would be happy to use it for just one of these features. The principles can be applied to other setups and breadboard based development.

I will show the connections and initial programming for each of these devices and then show an automation example - turning on an electric blanket in time for bedtime, if the room temperature is below a selected value.

## Step 1: Circuit Board

![](https://cdn.instructables.com/FZ0/OEB5/J98RXR5R/FZ0OEB5J98RXR5R.MEDIUM.jpg)

I have attached the PCB artwork. The same result could be achieved via breadboard or stripboard, but the PCB makes a much neater solution.

I have not included an overall circuit diagram as the PCB is single sided and hence easy to reverse engineer for breadboard/stripboard from the PCB picture and artwork.

Components required:

PCB (from attached artwork)

AMS1117 3.3 (20off for £0.99 on ebay)

3 off SOT-23 N channel MOSFET - see comment below

0805 4148 diode

5mm LED green (or red)

0805 ceramic capacitors >6v working voltage):

3 off 0.1uf

1 off 22uF

1 off 4.7uF

1206 resistors

2 off 0ohm

0805 resistors:

1 off 10ohm

1 off 100ohm

3 off 3k3ohm

1 off 5k1ohm

4 off 10kohm

0.1" Pin header 19 ways

2mm pinheader 16 ways

2 off 6mm tactile switch

ESP-12E or F (latter has better range)

I used an obsolete (but high current) MOSFET in the prototype when I realised that the popular 2N7002 was not going to drive more than around 30LEDs. My next boards will use the PMV40UN2 , Farnell code: 2242071. These have an on resistance of 50mohms with only 2.5v on the gate. There will be plenty more options. Check for working voltage over 15V and on resistance below 250mohms with 3v gate voltage.

My approach to PCB making is to print the artwork twice onto tracing paper. I then overlay these to double the contrast and cover any small imperfections in the printing (I use a laser printer). I punch holes in the edge of the upper layer, place Sellotape across the holes, align and then press on the holes to stick. I have a UV exposure unit. I used to use a UV black light that worked fine with spray coated PCBs and should work fine with positive photoresist boards. I use weak sodium hydroxide solution (drain cleaner) to develop and Di-Sodium Peroxodisulphate Hexahydrate to etch. Take special precautions with the chemicals, especially the sodium hydroxide that attacks flesh instantly. I then expose again and develop to get rid of the film over the tracks and finish off with some immerse tin (quite expensive - and limited life). The latter step is optional.

I drilled the holes for the for the LED and the 2mm pin strip for the ESP-12F at 0.7mm and the rest at 0.9mm.

For component placement see photo below. I use solder paste. Hence the approach - place component, place small blob of paste, solder. Move through all the components. Then apply paste to all the unsoldered pins and then solder these. I leave through-hole parts until after the SMD parts have been be completed.

Note that the LED cathode (flat on base) goes towards the USB connector edge.

Lastly add some guide marks on the board to show +, -, 5v TX and RX:

![](https://www.instructables.com/files/deriv/FHK/MN0O/J9JFT2TB/FHKMN0OJ9JFT2TB.MEDIUM.jpg)

## Step 2: Initial Programming and Set-up

![](https://cdn.instructables.com/FXH/3C42/J9IRABS1/FXH3C42J9IRABS1.MEDIUM.jpg)

A good starting point is to have set up a raspberry pi with Node-Red and mosquito as described in [Powerful Standalone Home Automation System - Pi, Sonoff, ESP8266 and Node-Red](https://www.instructables.com/id/Powerful-Standalone-Home-Automation-System-Pi-Sono/)

The key however is to have Node-Red running and connected to a MQTT broker.

I will also assume you have set up an Arduino IDE with the Sonoff-Tasmota firmware as also described in [Powerful Standalone Home Automation System - Pi, Sonoff, ESP8266 and Node-Red](https://www.instructables.com/id/Powerful-Standalone-Home-Automation-System-Pi-Sono/)

The first stage of the setup is to program the ESP-12F. Connect Ground, TXD and RXD from a USB to 3.3v serial converter. Power up the board either by connecting a USB lead to a USB host/power supply or connecting the serial converters 5v pin to one of the two 5v pins on the board. Set up the Arduino IDE as described in Instructable above, except that the flash size (Tools) can be set to 4M(1M SPIFFS). Also edit the user-config.h file with at least your wifi SSID and password and MQTT_HOST IP address. Now press and hold the GPIO 0 button while pressing and releasing the reset button, and continue to hold for at least 3 seconds. Then click upload and wait for confirmation this has been completed. Disconnect the serial converter, apply power via USB lead, and press the reset to restart the ESP.

If you are continuing where my earlier Instructable left off you will have set up usernames and passwords for security. It is easier to disable these while adding new devices. So log onto your pi via a PuTTY session (or direct) and change the mosquito config file to allow anonymous users:

**_sudo /etc/init.d/mosquitto stop_**

**_cd /etc/mosquitto/conf.d/_**

**_sudo nano mosquitto.conf_** This starts the editor.

Insert a _#_ at start of the lines "allow_anonymous false" and "password_file /etc/mosquitto/conf.d/passwd" . This comments these lines out and is easy to uncomment later.

Save and exit **_(Ctrl+X)_**, **Y**, **_enter_**.

Restart mosquitto via **_sudo /etc/init.d/mosquitto restart _**.

This disables the password security. Enable later as described in the Security step on my earlier Instructable.

Now log on to Node-Red using the Pi IP address:1880

In Node-Red, if you don't already have it, add an mqtt input node and set the topic to a catch-all **_+/+/+_**. Connect this to a debug node to show the mqtt traffic:

Also, if you don't already have it, set up an inject node and connect to an mqtt output node. Leave the mqtt node topic blank as we will set this in the inject node. The mqtt out node will need the IP address of the mqtt server (**_localhost_** if both are running on the same device):

The inject node (with Payload set to string) will be used to send combinations of Topic and Payload to set up the ESP-12F and set the GPIO pins to their appropriate functions.

**Initial setup**.

First it is useful to give the unit a new name/Topic. The firmware defaults to 'sonoff' that is a good starting point but can only be one off.

I named the unit 'sensor' by entering **_cmnd/sonoff/Topic_** as Topic and **_sensor_** as Payload in the inject mode. Click deploy and then when the mqtt nodes show connected click grey box on the LHS of the inject node to send (publish) the command (data). Check the responses in the debug tab - a restart with the new name.

We now need to tell the firmware what type of module it is loaded on. The nearest is a WeMos D1 mini, code 18. So send Topic: **_cmnd/sensor/Module_**, Payload: **_18_** . Deploy and send. The unit will restart and show "Module":"WeMos D1 mini".

Now we can start playing.

![](https://cdn.instructables.com/FG2/3YW1/J9EHBCU5/FG23YW1J9EHBCU5.MEDIUM.jpg)

![](https://cdn.instructables.com/F2B/CR5W/J98RXR5P/F2BCR5WJ98RXR5P.MEDIUM.jpg)

![](https://cdn.instructables.com/FZO/D4AU/J9EHBCU2/FZOD4AUJ9EHBCU2.SMALL.jpg)

![](https://cdn.instructables.com/FQ5/WVAF/J9EHBCU7/FQ5WVAFJ9EHBCU7.MEDIUM.jpg)

![](https://www.instructables.com/files/deriv/FW8/P8BD/J9JFXO2S/FW8P8BDJ9JFXO2S.MEDIUM.jpg)

> _We need to set gpio15 for the IR. So send topic cmnd/sensor/gpio15 with payload 8._

![](https://cdn.instructables.com/FHY/CXBR/J98RXR5T/FHYCXBRJ98RXR5T.MEDIUM.jpg)

> _The input goes to gpio12 and the action is switch1 in follow mode (1)._

![](https://cdn.instructables.com/FPS/KHMG/J9EH1XEC/FPSKHMGJ9EH1XEC.SMALL.jpg)
