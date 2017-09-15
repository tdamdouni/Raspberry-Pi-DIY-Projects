# Cheap PIR Sensors and the Raspberry Pi – Part 1

_Captured: 2017-09-09 at 16:47 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/)_

![PIR Module #1](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2013/01/pir_module_1-702x336.jpg)

A great little sensor you can add to your Raspberry Pi projects is a PIR module. These 5V "Passive Infra Red" sensors are available for a few pounds from eBay. They can be powered from 5V and output 3V so can be connected directly to pins on the Pi's GPIO header without any other components.

The module sets a single output pin high whenever it detects movement within its field of view. It holds this pin High (3.3V) for a minimum period of time. If continuous movement is detected the output pin will stay High. When the time has elapsed and no more movement is detected the output pin returns Low (0V).

I am currently using one in an alarm system and it works great for such a small and cheap device.

## PIR Connections

Here is a diagram showing the pin-out on the PIR module and how I connected it to my Raspberry Pi :

The device has two variable resistors that you can adjust to tweak the performance of the module.

The first one (left-hand side on the photo) determines the sensitivity of the device. The default setting is usually 50%.

The second control (right-hand side on the photo and usually marked "time" on the PCB) allows you to adjust the amount of time the output pin stays at 3V (high) when it is triggered by movement. This can be set from a few seconds to 200 seconds. The default setting is usually a few seconds.

You can find on eBay vary in specification but they are all very similar.

## Python Example Script

If you connect your module as shown in the diagram above the following Python script will allow you to get started. Cut and paste the script below into a text file and transfer to the Pi or download the script directly using [this link](https://www.raspberrypi-spy.co.uk/archive/python/pir_1.py).

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263
`#!/usr/bin/python``#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+``#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|``#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+``#``# pir_1.py``# Detect movement using a PIR module``#``# Author : Matt Hawkins``# Date   : 21/01/2013``# Import required Python libraries``import` `RPi.GPIO as GPIO``import` `time``# Use BCM GPIO references``# instead of physical pin numbers``GPIO.setmode(GPIO.BCM)``# Define GPIO to use on Pi``GPIO_PIR ``=` `7``print` `"PIR Module Test (CTRL-C to exit)"``# Set pin as input``GPIO.setup(GPIO_PIR,GPIO.IN)      ``# Echo``Current_State  ``=` `0``Previous_State ``=` `0``try``:``print` `"Waiting for PIR to settle ..."``# Loop until PIR output is 0``while` `GPIO.``input``(GPIO_PIR)``=``=``1``:``Current_State  ``=` `0``print` `"  Ready"``# Loop until users quits with CTRL-C``while` `True` `:``# Read PIR state``Current_State ``=` `GPIO.``input``(GPIO_PIR)``if` `Current_State``=``=``1` `and` `Previous_State``=``=``0``:``# PIR is triggered``print` `"  Motion detected!"``# Record previous state``Previous_State``=``1``elif` `Current_State``=``=``0` `and` `Previous_State``=``=``1``:``# PIR has returned to ready state``print` `"  Ready"``Previous_State``=``0``# Wait for 10 milliseconds``time.sleep(``0.01``)``except` `KeyboardInterrupt:``print` `"  Quit"``# Reset GPIO settings``GPIO.cleanup()`

This script can also be downloaded onto your Pi directly using this command line :

1
`wget https:``//www``.raspberrypi-spy.co.uk``/archive/python/pir_1``.py`

This can then be run using :

When run the script waits for the output pin to go Low. It then prints a message to the screen every time the output state changes. This is either when movement is detected (output changes to High) or the device sees no movement (outout changes to Low).

Try changing the reset time by turning the "time" resistor clockwise by a few degrees. Run the script again, trigger the device and then wait to see how long it takes to go back to the ready state.

## Photos

Here some more detailed photos of the PIR pins and two trimming controls :

## Calibration

In [Cheap PIR Sensors and the Raspberry Pi - Part 2](https://www.raspberrypi-spy.co.uk/2013/02/cheap-pir-sensors-and-the-raspberry-pi-part-2/) I show you how to calibrate your sensor to fine tune its performance.

## Applications

The applications of this circuit include :

  * Security systems
  * Automatic photographs
  * Robot sensors

Here are some of my other articles you might find interesting if you enjoyed this one :
