# Tutorial & Review: Enviro pHAT for Raspberry Pi

_Captured: 2017-07-30 at 16:00 from [blog.initialstate.com](http://blog.initialstate.com/tutorial-review-enviro-phat-for-raspberry-pi/)_

![2016-07-26 pHAT enviro Hero](http://blog.initialstate.com/wp-content/uploads/2016/07/2016-07-26-pHAT-enviro-Hero-1024x502.jpg)

The [Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat) from [Pimoroni](https://shop.pimoroni.com/) is an add-on board for Raspberry Pi with a set of sensors on-board to capture temperature, pressure, motion, light, and color. The size of pHAT boards match the size of a Pi Zero giving you a very compact solution that you can discretely deploy in a variety of situations. The Enviro pHAT costs £16 (~$21 USD). When paired with a Pi Zero and required accessories (WiFi dongle, microSD card, power supply) you have a complete solution for under £38 ($50 USD).

Let's create a couple of actual projects with the Enviro pHAT and see how it does in the real world. We will use the Enviro pHAT and a Pi Zero to create a real-time temperature streamer/logger and use the 3-axis accelerometer/magnetometer to create a real-time motion sensor/logger.

## Setup

The Enviro pHAT comes with a 40-pin header that you will need to solder on yourself, just like the Pi Zero. This is pretty common when working with maker components but adds quite a bit of setup time in relation to the rest of the process. Pimoroni provides a great step-by-step guide to soldering headers on pHATs [here](http://learn.pimoroni.com/tutorial/sandyj/soldering-phats).

Once the header has been soldered and the pHAT has been plugged into your Pi Zero, you will need to install the software libraries that will make creating a Python-based project a piece of cake. Make sure you are running an up-to-date version of Raspbian. Open up a terminal and run the command

Installation took me a little under five minutes on a fresh install of Raspbian on a Pi Zero. Reboot your Pi to complete the Enviro pHAT software installation.

We want to stream all of our enviro pHAT data to a cloud service and have that service turn our data into a nice dashboard that we can access from our laptop or mobile device. Our data needs a destination. We will use Initial State as that destination. Follow the detailed instructions [here](https://github.com/InitialState/wunderground-sensehat/wiki/Part-1.-Initial-State) to setup your free Initial State account and install the ISStreamer Python library. The TL;DR version of these instructions are as follows:

  1. Run the command: \curl -sSL https://get.initialstate.com/python -o - | sudo bash
  2. When prompted to automatically get an example script, type y and name the script ./is_example.py.
  3. Run the example script: python is_example.py
  4. Go to your Initial State account and view the new data bucket named "Python Stream Example". You are now ready to create a real project.

Once the software libraries have been installed, reading sensor data from the Enviro pHAT and streaming that data to Initial State will be incredibly simple.

## Temperature Streamer/Logger

Let's take a reading from the Enviro pHAT's temperature sensor. At a terminal, run

This will open up an interactive Python shell. Type the following to read the temperature sensor (in Celsius):

If the number returned seems a bit high, it is because it is. Comparing the measurements of the Enviro pHAT with a Pi Zero to a very accurate DHT22 temperature sensor + GrovePi + Pi3 ([tutorial](https://github.com/InitialState/grovepi/wiki)) over 24 hours looks like the following:

![Screen Shot 2016-07-26 at 11.12.21 PM](http://blog.initialstate.com/wp-content/uploads/2016/07/Screen-Shot-2016-07-26-at-11.12.21-PM.png)

The average measured temperature over 24 hours from the Enviro pHAT was 88.91° F (31.62° C). The average measured temperature from the DHT22 + GrovePi was 76.77° F (24.87° C). That is a significant 12.14° F (6.75° C) difference! The main culprit is the heat generated from the Pi's CPU heating up the air around the Enviro pHAT when it is sitting on top of the Pi.

To make the temperature sensor useful, we need to either get the pHAT away from the Pi (which would eliminate the important benefit of being a compact solution) or try to calibrate the temperature sensor reading. The CPU is the primary cause of the parasitic heat affecting our temperature sensor. We can easily read the CPU temperature using the command

A simple temperature calibration equation based on the CPU temperature is
    
    
    temp_calibrated = temp_c - ((cpu_temp_c - temp_c)/FACTOR)
    
    

For my Pi Zero setup, I chose FACTOR to be 1.3. A 24-hour run comparing CPU, measured Enviro pHAT, calibrated Enviro pHAT, and DHT22+GrovePi temperatures looks like the following:

![Screen Shot 2016-07-26 at 11.39.11 PM](http://blog.initialstate.com/wp-content/uploads/2016/07/Screen-Shot-2016-07-26-at-11.39.11-PM.png)

The average calibrated temperature (the dark purple line) measured 79.34° F (26.3° C). This brings the difference down to 2.57° F (1.43° C). Not perfect, but better. You can see how the calibrated temperature tracks the DHT22 temperature (the blue line) but is considerably more noisy than the DHT22. Unfortunately, you can't use a simple equation to completely correct the temperature measurement. You can see one reason here:

![Screen Shot 2016-07-26 at 11.47.47 PM](http://blog.initialstate.com/wp-content/uploads/2016/07/Screen-Shot-2016-07-26-at-11.47.47-PM.png)

Running a heavy math script will cause a 17% increase in the CPU temperature (the rise in temperature for the pink line at the cursor). While the CPU temperature rises quickly, the air temperature around the board (the green line) rises quite a bit slower. The calibrated temperature (purple line) initially dips 7° F (4.11° C) below the control temperature from the DHT22+GrovePi before settling out a couple of degrees (F) cooler than the DHT22+GrovePi. Once the heavy math script stopped, the CPU temperature quickly lowered while the air temperature took a few minutes to cool.

Fluctuations in CPU temperature and fluctuations in ambient temperature create a more complex affect on the Enviro pHAT measured temperature than a simple equation can completely fix. That being said, the simple calibration equation above works pretty well and makes the temperature sensor useful assuming you are ok with 1-2 degrees average error.

You can run your own experiment comparing CPU, Enviro pHAT, and calibrated Enviro pHAT temperatures with the following script. You will need to place your Initial State access key (found in your Initial State account settings) in the ACCESS_KEY variable assignment on line 11. If you do not do this, your data will not be streamed into your Initial State account, making you very sad and frustrated. You can modify the calibration equation on line 35. Modify the time between temperature readings on line 14.

For example, you can copy the above code to a file named enviro_phat.py, then run the script with the following command: sudo python enviro_phat.py. If you want to stream temperatures from other sensors / Pis into the same dashboard, simply stream that data into the same BUCKET_KEY listed on line 10. My dashboard looks like the following after 24 hours:

![Screen Shot 2016-07-26 at 9.07.04 AM](http://blog.initialstate.com/wp-content/uploads/2016/07/Screen-Shot-2016-07-26-at-9.07.04-AM-1024x498.png)

You can play with this data at:  
Tiles - <https://app.initialstate.com/#/tiles/caf1ff39-de25-472e-9977-a647013e9425>.  
Waves - <https://app.initialstate.com/#/waves/caf1ff39-de25-472e-9977-a647013e9425>  
Lines - <https://app.initialstate.com/#/lines/caf1ff39-de25-472e-9977-a647013e9425>

## Real-Time Motion Streamer/Logger

The Enviro pHAT has a 2g 3-axis accelerometer that we can use detect x, y, z motion. Let's take a reading from the Enviro pHAT's motion sensor. At a terminal, run

This will open up an interactive Python shell. Type the following to read the motion sensor:

Easy enough. Let's build a simple Python script that will read the motion sensor and stream its values to an Initial State dashboard. Just like the last script, you will need to place your Initial State access key on line 9.

Run this script, move the pHAT around, and watch the data change in your dashboard. You can see the +/- 2g limit on the sensor with some quick movement (please don't throw your pHAT across the room). My dashboard looks like the following:

![Screen Shot 2016-07-27 at 10.39.56 AM](http://blog.initialstate.com/wp-content/uploads/2016/07/Screen-Shot-2016-07-27-at-10.39.56-AM-1024x359.png)

You can play with this data at:  
Tiles - <https://app.initialstate.com/#/tiles/faac6370-57dc-4bd6-b164-a64801542002>  
Waves - <https://app.initialstate.com/#/waves/faac6370-57dc-4bd6-b164-a64801542002>  
Lines - <https://app.initialstate.com/#/lines/faac6370-57dc-4bd6-b164-a64801542002>

## Other Sensors

The Enviro pHAT includes a pressure sensor (barometer) and a light/color sensor that we did not extensively test in this review. There is also a pin header and on-board analog-to-digital convertor for bringing in four analog signals. The input signals need to be 3.3V or you will have to build an external voltage divider to step the voltage down to 3.3V. You can read more about these sensors and how to use them at Pimoroni's [Getting Started with Enviro pHAT](http://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat) page.

## Verdict

The Enviro pHAT is an easy-to-use add-on board that can turn your Pi Zero into a tiny sensor box. Accessing the sensor values is as easy as a single line of Python code. The usefulness of the temperature sensor is limited by the parasitic heat radiated from the Pi. A simple calibration can make this sensor useful but no more accurate than +/-1° C. The on-board analog sensor inputs has the potential to be really useful. You may be able address the temperature sensor limitation by adding an external analog temperature sensor like the $1.50 [TMP36](https://www.adafruit.com/products/165?&main_page=product_info&cPath=35&products_id=165) to get distance between the sensor and the Pi for a more accurate temperature measurement (untested).

Overall, the Enviro pHAT is a really fun and useful board with a reasonable price that can come in quite handy for a variety of projects.
