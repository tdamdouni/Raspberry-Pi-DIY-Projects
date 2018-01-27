# Mulesoft With IoT: LEDs and a Raspberry Pi

_Captured: 2017-12-10 at 20:39 from [dzone.com](https://dzone.com/articles/mulesoft-with-iot-leds-and-a-raspberry-pi?edition=343111&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=Daily%20Digest%202017-12-10)_

The Internet of Things is the network of physical devices, vehicles, and other items embedded with electronics, software, sensors, actuators, and network connectivity that enable these objects to collect and exchange data. IoT is supposed to have 10 times the impact of the web itself, which means it has potentially 10 times the risk of complication, and, with its ubiquity, 10 times the risk to security. Each "Thing" we encounter in our daily and professional lives could potentially be connected within the next couple years. And with so many more players, manufacturers, protocols, and programming languages, it all gets exponentially more complicated.

MuleSoft's lightweight Runtime Engine can be used to expose microservices and APIs on any IoT device. In this post, I will demonstrate how users can use MuleSoft and a Python script to create a simple API that lights up an LED bulb 10 times in a loop.

## Project Steps

### Build the LED Blink Project

Set up your Raspberry Pi and make sure it is running and that you can SSH into it using an IP (preferably a static IP).

Ensure the Raspberry Pi is connected to your router (wireless or LAN cable).

You'll need the following in order to follow along with this tutorial:

  * Raspberry Pi

  * MMC

  * Python script (provided below)

  * Resistors

  * Power supply

  * LED bulbs

### Setup Instructions

You should be able to SSH into the Raspberry Pi. Ensure it is connected to Wi-Fi.

The GPIO pins on the Raspberry Pi are what makes it powerful. These pins are a physical interface between the Pi and the outside world. In layman's terms, you can think of them as switches that you can turn on or off (input) or that the Pi can turn on or off (output). Of the 40 pins, 26 are GPIO pins, and the others are power or ground pins. You can program the pins to interact in amazing ways with the real world.

We are using a very basic Python script that can control GPIO commands to blink the LED bulb.

Python Script (ledBlink.py):

Install an MMC instance on the Raspberry Pi. Develop a Mule app that gets a Twitter feed and can call the Python script. Call the Python script in localhost (Raspberry Pi), then deploy it on the Raspberry Pi Mule instance.

The Mule app will get the feed from the Twitter account and call the Python script, which, in turn, will turn the LEDs on.

This demonstrates how a Mule instance running on a tiny Raspberry Pi controls turning on/off lights.

MuleSoft's Runtime Engine can be used in various innovative ways to connect devices, data, and applications. This is a basic example of the Internet of Things with Mulesoft
