# Enviro pHAT

_Captured: 2017-09-03 at 12:58 from [blog.pimoroni.com](http://blog.pimoroni.com/enviro-phat/)_

Our newest pHAT, [Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat), hit our shop last night and we think it's one of our most fun _and_ useful boards so far! It packs 5 different sensors onto one little board and lets you measure up to 10 different variables at once, with the 4 analog channels included.

We're going to start doing these blog posts as each of our new products hits the shop, giving some behind-the-scenes detail about the development of the products.

## Features

Enviro pHAT lets you measure temperature, pressure, light level, RGB colour, 3-axis motion, compass heading, and up to 4 analog input channels allowing you to connect and read from analog devices like gas sensors.

### Temperature and pressure

The BMP280 sensor we use on Enviro pHAT is the same sensor that's on our Flotilla weather sensor. It measures temperature and atmospheric pressure, and our Python library takes care of converting the readings into the right units - degrees Celsius and Pascals.

![Weather macro](http://blog.pimoroni.com/content/images/2016/06/weather_macro.jpg)

### Light and colour

The TCS3472 sensor is, again, the same one used on another of our Flotilla modules - the colour sensor. In fact, the motion sensor is also the same as the sensor on our Flotilla motion module. In effect, Enviro pHAT is the Flotilla weather, colour and motion modules rolled into one, with the addition of the ADC.

The TCS3472 measures 4 variables - clear, red, green and blue - with the clear reading being the ambient light level. Behind the scenes, in the software, the clear reading is used as a background against which the red, green and blue readings are calculated.

We've also included a couple of white LEDs either side of the TCS3472 to illuminate objects better when sensing colour. These can be controlled together (but not individually) direct from the GPIO.

![Light macro](http://blog.pimoroni.com/content/images/2016/06/light_macro.jpg)

The LSM303D accelerometer and magnetometer detects 3-axis motion - side-to-side, vertical, and back-and-forth - as well as compass heading.

The readings given by the software are negative and positive for opposite directions on each axis, but the compass heading isn't calibrated to a fixed north point, so you'll need to do that yourself (it's not hard and we show you how in our [getting started guide](http://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat)).

![Motion macro](http://blog.pimoroni.com/content/images/2016/06/motion_macro.jpg)

The ADS1015 is a 4-channel analog to digital converter (ADC) and allows you to read analog inputs. It's important to note that this ADC is only rated in the datasheet up to 3.3V and many analog sensors use 5V logic. In our testing, running 5V into the ADC didn't have any adverse effects, but the readings you get back won't be reliable.

3.3V logic analog sensors will work just fine and, for 5V ones, a simple solution is to use a voltage divider with three fairly high value resistors of equal resistance. Tapping in and out from the correct junctions will step you down from 5V to 3.3V. We give an example of this in our [getting started guide](http://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat)) as well.

![Analog macro](http://blog.pimoroni.com/content/images/2016/06/analog_macro.jpg)

## Development

Developing Enviro pHAT has taken a while. We started designing it at the same time as our pHATs that launched alongside the Pi Zero, but getting it to production has taken a little longer than for those that we've already launched.

Our boards are designed in Eagle. In this case, Phil designed the board and, as with the majority of artwork here at Pimoroni, Paul designed the silkscreen art.

![Eagle board](http://blog.pimoroni.com/content/images/2016/06/eagle.jpg)

Generally, our boards go through at least two prototype spins, where we order a single panel of 21 pHATs or 12 HATs from either Dirty PCBs or Eurocircuits. We laser-cut a Mylar stencil to apply the solder paste to the component pads and then hand-place all of the components with tweezers. The board, with components placed, then goes through the reflow oven to melt the solder and secure the components.

Then, it's a case of thorough hardware testing and developing the software libraries. Often, we'll make tweaks to the routing, move decoupling capacitors, and so on, after the first prototype spin and then double check that everything's just as it should be after the second spin.

When developing our pHATs (and HATs), we always try to think about i) how creatively people will be able to use them and, ii) how they'll work together with our other products. In the case of Enviro pHAT, it goes great with our LED pHATs - [Scroll pHAT](https://shop.pimoroni.com/products/scroll-phat) and [Unicorn pHAT](https://shop.pimoroni.com/products/unicorn-phat) \- for visualising the sensor data - or [Display-O-Tron HAT](https://shop.pimoroni.com/products/display-o-tron-hat) for text display.

## Benchmarking

We ran a couple of benchmarks, on the colour sensor, and on the temperature of the board when mounted on the Pi Zero to get an idea of whether this would have an effect on temperature readings.

### RGB colour

To test the colour sensor, we used red, green, blue and white pieces of Perspex, with the LEDs off and on, and then took stable readings of the RGB values with the Perspex pieces held as close as possible to the sensor.

We also took some reference photos of the Perspex pieces against which we could benchmark the sensor readings. These reference images were all taken using the same settings and processed identically, setting the white balance using the white Perspex piece and exposing each image until the whites matched.

It's worth noting that the Perspex pieces used were quite reflective and gave off a high amount of specular highlight.

You'll see from the results that the hues are correct, but both of the sensor readings, with and without the LEDs, are quite a bit duller than the reference images. Interestingly, the readings taken with the LEDs on are duller than those with them off. This is probably due to the way that the RGB values are calculated against the clear reading, with the higher clear value when the LEDs are on resulting in the RGB values being scaled further down.

![RGB colour test](http://blog.pimoroni.com/content/images/2016/06/rgb_colour_test.jpg)

Of course, you could use methods like this to calibrate your sensor, by setting the white level against a white reference and then calculating RGB values relative to that.

### Temperature

To see how accurate the temperature sensor was and to see how large the difference between ambient temperature and the board temperature was, we used our thermal camera to measure the board's temperature.

![Thermal image](http://blog.pimoroni.com/content/images/2016/06/img_thermal_1466153303302-6.jpg)

You'll see that the board is around 7 degrees (+/- 1 degree) warmer than the surface on which the Pi was. Indeed, the reading from the Enviro pHAT itself was ~26.5 degrees, within the +/- 1 degree accuracy quoted on the BMP280 datasheet.

Given the difference, it may be an idea to calibrate the temperature based on the ambient temperature of the room, although this will vary depending on your setup, so it's not something that we've included in our library.

## Using Enviro pHAT

Enviro pHAT is perfect for sticking on a shelf on top of a Pi Zero and monitoring conditions in your room. With some creative coding you can have it as part of an Internet of Things-type project where you tweet conditions in your rooms, or send alerts when readings pass certain thresholds.

In the coming weeks, we'll be putting some tutorials up on [our learning portal](http://learn.pimoroni.com/) showing you some fun projects with Enviro pHAT.

As always, we've written a lovely [Python library](https://github.com/pimoroni/enviro-phat), so that you can dig in and get started with Enviro pHAT straight away. And there's a comprehensive [getting started guide](http://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat) to show you how to install and use the Enviro pHAT library.

We also spoke about Enviro pHAT in detail on this week's [Bilge Tank 042](https://youtu.be/U3ij4kVSiJo), and showed off some really fun demos.
