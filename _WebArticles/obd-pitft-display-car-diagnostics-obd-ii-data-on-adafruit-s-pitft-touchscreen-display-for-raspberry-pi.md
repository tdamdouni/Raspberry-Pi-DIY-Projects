# OBD-PiTFT: Display Car Diagnostics (OBD-II) Data On Adafruit's PiTFT Touchscreen Display For Raspberry Pi

_Captured: 2017-05-11 at 22:45 from [www.cowfishstudios.com](http://www.cowfishstudios.com/blog/obd-pitft-display-car-diagnostics-obd-ii-data-on-adafruits-pitft-touchscreen-display-for-raspberry-pi)_

In this tutorial you will learn how to connect your Raspberry Pi to a Bluetooth OBD-II adapter and display realtime engine data on Adafruit's PiTFT touchscreen display.

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/7910958_orig.jpg)

## **_Hardware Required:_**

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/551576_orig.jpg)

1\. [Raspberry Pi Model B](http://www.raspberrypi.org/products/model-b/) or [B+](http://www.raspberrypi.org/products/model-b-plus/)  
2\. [Adafruit PiTFT Touchscreen Display](http://www.adafruit.com/products/1601)  
3\. [Plugable USB Bluetooth 4.0 Low Energy Micro Adapter](http://www.amazon.com/gp/product/B009ZIILLI/ref=oh_details_o00_s00_i00?ie=UTF8&psc=1)   
4\. [2A Car Supply / Switch](http://www.mausberrycircuits.com/collections/car-power-supply-switches/products/2a-car-supply-switch) or Micro USB Car Charger  
5\. [ELM327 Bluetooth Adapter](http://www.amazon.com/Goliton%C2%AE-Bluetooth-Supper-Compatible-Andriod/dp/B009NPAORC/ref=sr_1_5?s=automotive&ie=UTF8&qid=1428250836&sr=1-5&keywords=ELM327+Bluetooth+Adapter) or [ELM327 USB Cable](http://www.amazon.com/HDE-ELM-327-Diagnostics-Cable/dp/B004O5HXYS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1401569442&sr=1-1&keywords=ELM327+usb)  
6\. [Sweetbox Raspberry Pi Case](http://www.graspinghand.com/product/sweetbox_heatsinks) (*optional)  
7\. [Car Mount Holder](http://www.amazon.com/iOttie-Holder-iPhone-Samsung-Galaxy/dp/B00FXSU43W/ref=sr_1_3?ie=UTF8&qid=1406554415&sr=8-3&keywords=iottie) (*optional)  
8\. Keyboard (*optional)

## **_What is OBD-II?_**

OBD stands for On-Board Diagnostics, and this standard connector has been mandated in the US since 1996. Now you can think of OBD-II as an on-board computer system that is responsible for monitoring your vehicle's engine, transmission, and emissions control components.

Vehicles that comply with the OBD-II standards will have a data connector within about 2 feet of the steering wheel. The OBD connector is officially called a SAE J1962 Diagnostic Connector, but is also known by DLC, OBD Port, or OBD connector. It has positions for 16 pins, and looks like this:

![Picture](http://www.cowfishstudios.com/uploads/2/8/6/1/28619761/7797537_orig.png)

[pyOBD](http://www.obdtester.com/pyobd) (aka pyOBD-II or pyOBD2) is an open source OBD-II (SAE-J1979) compliant scantool software written entirely in Python. It is designed to interface with low-cost ELM 32x OBD-II diagnostic interfaces such as ELM-USB. It will basically allow you to talk to your car's ECU, display fault codes, display measured values, read status tests, etc.

I took a fork of [pyOBD's](http://www.obdtester.com/pyobd) software from their GitHub repository, <https://github.com/peterh/pyobd>, and used this as the basis for my program.

The program will connect through the OBD-II interface, display the gauges available dependent on the particular vehicle and display realtime engine data on Adafruit's PiTFT touchscreen display in an interactive GUI.

## **_Software Installation_**

In order to add support for the 2.8" TFT and touchscreen, we'll need to install a new Linux Kernel. Head over to [Adafruit](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/software-installation) and follow their Software Installation, then come on back!

We'll be doing this from a console cable connection, but you can just as easily do it from the direct HDMI/TV console or by SSH'ing in. Whatever gets you to a shell will work!

Note: For the following command line instructions, do not type the '#', that is only to indicate that it is a command to enter.

Before proceeding, run:

## _**Vehicle**** Installation**_

The vehicle installation is quite simple.

1\. Insert the USB Bluetooth dongle into the Raspberry Pi along with the SD card.

2\. Connect your PiTFT display to the Raspberry Pi.

3\. Insert the OBD-II Bluetooth adapter into the SAE J196216 (OBD Port) connector.

4\. Install your 2A Car Supply / Switch or Micro USB Car Charger.

5\. Finally, turn your key to the ON position.

6\. Enter your login credentials and run:

**7\. Launch BlueZ, the Bluetooth stack for Linux. Pair + Trust your ELM327 Bluetooth Adapter and Connect To: SPP Dev. You should see the Notification "Serial port connected to /dev/rfcomm0"**

**Note: Click the Bluetooth icon, bottom right (Desktop) to configure your device. Right click on your Bluetooth device to bring up Connect To: SPP Dev.**

**8\. Open up Terminal and run:**

**Note: Run,** # python obd_gui_square.py **to use the rounded rectangle gauge.**

**Tap the display to cycle through the gauges!**

**To exit the program just press Control and C or Alt and Esc.**

**The logged data file will be saved under: **  
/home/username/pyobd-pi-TFT/log/

## Enjoy and drive safe!
