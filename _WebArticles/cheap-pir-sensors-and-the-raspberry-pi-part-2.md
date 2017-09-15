# Cheap PIR Sensors and the Raspberry Pi – Part 2

_Captured: 2017-09-09 at 16:48 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2013/02/cheap-pir-sensors-and-the-raspberry-pi-part-2/)_

![PIR Module #2](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2013/01/pir_module_2-702x336.jpg)

Following on from my first [PIR sensor module article](https://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/) I thought I would create a Python script that allowed me to easily measure the reset time.

That way I could attach a module, run the script and measure the time it took for the output pin to drop back to the Low state. Then I could tweak the trimming resistor and adjust the reset time to my preferred value in a more controlled and precise way.

## Example Python Script

The following script assumes you have your PIR module connected to the GPIO header as shown in [Part 1](https://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/). The example uses GPIO7 (Pin 26).

Cut and paste the script below into a text file and transfer to the Pi or download the script directly using [this link](https://www.raspberrypi-spy.co.uk/archive/python/pir_2.py) (recommended).

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364
`#!/usr/bin/python``#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+``#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|``#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+``#``# pir_2.py``# Measure the holding time of a PIR module``#``# Author : Matt Hawkins``# Date   : 20/02/2013``# Import required Python libraries``import` `time``import` `RPi.GPIO as GPIO``# Use BCM GPIO references``# instead of physical pin numbers``GPIO.setmode(GPIO.BCM)``# Define GPIO to use on Pi``GPIO_PIR ``=` `7``print` `"PIR Module Holding Time Test (CTRL-C to exit)"``# Set pin as input``GPIO.setup(GPIO_PIR,GPIO.IN)      ``# Echo``Current_State  ``=` `0``Previous_State ``=` `0``try``:``print` `"Waiting for PIR to settle ..."``# Loop until PIR output is 0``while` `GPIO.``input``(GPIO_PIR)``=``=``1``:``Current_State  ``=` `0``print` `"  Ready"``# Loop until users quits with CTRL-C``while` `True` `:``# Read PIR state``Current_State ``=` `GPIO.``input``(GPIO_PIR)``if` `Current_State``=``=``1` `and` `Previous_State``=``=``0``:``# PIR is triggered``start_time``=``time.time()``print` `"  Motion detected!"``# Record previous state``Previous_State``=``1``elif` `Current_State``=``=``0` `and` `Previous_State``=``=``1``:``# PIR has returned to ready state``stop_time``=``time.time()``print` `"  Ready "``,``elapsed_time``=``int``(stop_time``-``start_time)``print` `" (Elapsed time : "` `+` `str``(elapsed_time) ``+` `" secs)"``Previous_State``=``0``except` `KeyboardInterrupt:``print` `"  Quit"``# Reset GPIO settings``GPIO.cleanup()`

Alternatively the script can also be easily downloaded onto your Pi directly using this command line :

1
`wget https:``//www``.raspberrypi-spy.co.uk``/archive/python/pir_2``.py`

The script can then be run using :

1
`sudo` `python pir_2.py`

When run the script waits for the output pin to go Low. Just like in pir_1.py it prints a message to the screen when movement is detected. The main difference is that it now measures the elapse of time between the output pin going High and it returning to Low.

You can use a small screwdriver to tweak the "time" control to increase or decrease the time. Once you've triggered the module it is important to stay still so you don't increase the time the output stays High which will mess up your results.

A half turn will result in the reset time being increased by a few minutes so it's best to make adjustments in small increments.

are available on eBay.
