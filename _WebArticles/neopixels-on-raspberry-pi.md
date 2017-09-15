# NeoPixels on Raspberry Pi

_Captured: 2017-09-03 at 13:13 from [learn.adafruit.com](https://learn.adafruit.com/neopixels-on-raspberry-pi?view=all)_

The are some reports that this library does not work with the new Raspberry Pi 2. Be warned that the library is not confirmed to work with the Pi 2 hardware yet--only the first generation Pi is known to work.

Wouldn't it be fun to add bright, beautiful NeoPixels to your Raspberry Pi project? However NeoPixels, and the WS2811/2812 LEDs that make them up, require a data signal with very specific timing to work correctly. Because the Raspberry Pi runs a multi-tasking Linux operating system it doesn't have real-time control over its GPIO pins and can't easily drive NeoPixels. Typically a small microcontroller like a Trinket or Teensy can be used to communicate with the Raspberry Pi and generate the NeoPixel data signal. However thanks to the excellent [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library created by [Jeremy Garff](https://github.com/jgarff), you can now control NeoPixels or WS2811/WS2812 LEDs directly from your Raspberry Pi!

Jeremy's library solves the real-time control problem by using the PWM and DMA hardware on the Raspberry Pi's processor. The PWM (pulse-width modulation) module can generate a signal with a specific [duty cycle](http://en.wikipedia.org/wiki/Duty_cycle), for example to drive a servo or dim an LED. The DMA (direct memory access) module can transfer bytes of memory between parts of the processor without using the CPU. By using DMA to send a specific sequence of bytes to the PWM module, the [NeoPixel data signal](https://learn.adafruit.com/../../../../adafruit-neopixel-uberguide/advanced-coding) can be generated without being interrupted by the Raspberry Pi's operating system.

The great thing about Jeremy's library is that it does all the hard work of setting up PWM and DMA to drive NeoPixels. On top of rpi_ws281x I've added a small Python wrapper which makes the library look and feel like the Arduino NeoPixel library. This guide will show you how to install the rpi_ws281x library and Python wrapper so you can use NeoPixels in your own Raspberry Pi projects!

Before you get started you will want to be familiar with how to [connect to a Raspberry Pi's terminal using SSH](https://learn.adafruit.com/../../../../adafruits-raspberry-pi-lesson-6-using-ssh/overview). It will also be helpful to check out the [NeoPixel Uberguide](https://learn.adafruit.com/../../../../adafruit-neopixel-uberguide/overview) for more information on using NeoPixels.

![leds_levelshifter_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/019/658/large1024/leds_levelshifter_bb.png?1410393346)

![leds_diode_bb.png](https://cdn-learn.adafruit.com/assets/assets/000/019/659/large1024/leds_diode_bb.png?1410393412)
