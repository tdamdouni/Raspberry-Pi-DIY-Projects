# Zero LiPo

_Captured: 2017-09-03 at 12:57 from [blog.pimoroni.com](http://blog.pimoroni.com/zero-lipo/)_

The tiniest, slimmest way to power your Pi off-grid!

[Zero LiPo](https://shop.pimoroni.com/products/zero-lipo) is the perfect solution for portable Pi Zero projects, whether it be a scrolling message badge or a collar cam. for your dog.

The board weighs just 2.9g and the PCB is 0.8mm thin, meaning that it can slip right over the GPIO pins on your Pi Zero (or larger Pi), and you can still fit a HAT, pHAT, or other add-on board on top.

We'll have a look at the functionality of the board, and then have a look at the results of some extensive testing we did of the lithium polymer ([LiPo](https://shop.pimoroni.com/products/lipo-battery-pack)) and lithium ion ([LiIon](https://shop.pimoroni.com/products/lithium-ion-battery-pack)) batteries that we're now stocking in the shop.

![Zero LiPo](http://blog.pimoroni.com/content/images/2016/07/zero-lipo-4-1.jpg)

## Features

Zero LiPo has a JST connector, to which you can connect a LiPo, LiIon, or other battery with a JST plug. It converts the 3 - 4.2V input voltage (from the LiPos/LiIons) to 5V, by means of a step-up boost converter, providing a stable 5V supply perfect for powering your Pi.

There are three chips on Zero LiPo: the step-up boost converter, a comparator, and a level shifter.

The step-up boost converter is a TPS61232, and has two large capacitors to smooth the output.

![Boost converter](http://blog.pimoroni.com/content/images/2016/07/zero-lipo-1.jpg)

The comparator defines the low voltage warning, with hysteresis to avoid flutter at the boundary, and toggles when the input voltage drops below 3.4V.

The level shifter shifts the 5V signal from the low voltage warning down to 3.3V, a safe voltage to run into the Pi's GPIO pin 4 (BCM), meaning that you can watch the state of pin 4 and, when it gets pulled high, trigger a safe shutdown of your Pi.

![Comparator and level shifter](http://blog.pimoroni.com/content/images/2016/07/zero-lipo-2.jpg)

There are a couple of LEDs on the board: a blue power LED that comes on when the battery is supplying voltage, and a red low voltage warning LED that comes on when the input voltage from the battery drops below 3.4V.

![LEDs](http://blog.pimoroni.com/content/images/2016/07/zero-lipo-3.jpg)

> _Zero LiPo will switch off altogether when the input voltage drops below 3V, to prevent unsafe operation of any attached LiPo or LiIon battery._

## Battery discharge data

Niko, one of our electrical engineers, carried out some extensive testing of the LiPo and LiIon batteries that we're stocking in our shop, as part of the development of Zero LiPo. We'll go through those data now.

The capacities of batteries that we're stocking are:

  * 105 mAh
  * 150 mAh
  * 500 mAh
  * 1200 mAh
  * 2000 mAh
  * 2200 mAh
  * 4400 mAh
  * 6600 mAh

Niko tested the discharge rates of all of these batteries. Measurements of voltage and current were taken every second, at maximum current, up until the internal voltage cutout threshold was reached at 2.2 - 2.5V. This emergency voltage cutout is part of the circuitry of the battery and prevents unsafe low voltages from damaging the cell permanently.

In general, the capacities measured by Niko tallied closely with the quoted capacities.

You can see the discharge curves (voltage vs. time) for all of the batteries below.

![Discharge curves](http://blog.pimoroni.com/content/images/2016/07/discharge_curves.jpg)

So, at maximum current, you'll see that the largest capacity of battery, the 6600 mAh LiIon battery, lasts for about two and quarter hours before it shuts off.

It's interesting to note that the 2200 mAh LiIon battery reaches the low voltage threshold significantly earlier than the 2000 mAh LiPo battery, despite the 3V shutdown (via Zero LiPo) threshold being reached at almost the same time.

We also measured the current draw from a Pi Zero in a range of typical use cases and then calculated how long you'd get before the low voltage threshold was reached.

The use cases were:

  * Pi Zero plus official WiFi dongle (downloading data)
  * Pi Zero plus camera (recording video)
  * Pi Zero plus camera plus WiFi dongle (streaming video)
  * Pi Zero plus Scroll pHAT (LEDs at full brightness)
  * Pi Zero plus Unicorn pHAT (LEDs at full brightness)
  * Pi Zero plus Blinkt! (LEDs at half brightness)

(The Blinkt! LEDs were at half brightness to give an output limit similar to Unicorn pHAT at full brightness, since a 50% full brightness limit is imposed in the software)

And here are the results.

![Use cases](http://blog.pimoroni.com/content/images/2016/07/discharge_times.jpg)

So, you'll see that, with the largest capacity of LiPo battery, you'll get over 9 hours of use with Scroll pHAT or, in the worst case, about 3 and a half hours use with the camera streaming over WiFi. With the largest LiIon battery, those same times are 15 and a quarter and 5 and three quarter hours respectively.

## More to come!

We'll make all of this testing data available in a GitHub repository soon, and we'll also have some fun little projects going up on [learn.pimoroni.com](http://learn.pimoroni.com).
