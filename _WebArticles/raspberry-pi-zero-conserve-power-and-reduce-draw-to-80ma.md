# Raspberry Pi Zero - Conserve power and reduce draw to 80mA

_Captured: 2017-09-03 at 13:04 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy)_

[**Update 2015-12-01**: I bought a [PowerJive USB power meter](http://www.amazon.com/gp/product/B013FANC9W) and re-tested everything, and came up with ~80 mA instead of the ~30 mA reported by the Charger Doctor that I was using prior. This seems to be more in line with the results others were measuring with _much_ more expensive/accurate meters in the Raspberry Pi forums: [Raspberry Pi Zero power consumption](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=127210&p=851245#p851245). I've updated the numbers in the post below to reflect this change. Seems the Pi Zero is only incrementally better than the A+--still excellent news, but not nearly as amazing as I originally thought :(]

Yesterday my post [comparing the Raspberry Pi Zero's power consumption to other Pis](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-power) hit the Hacker News front page, and commenters there offered a few suggestions that could be used to reduce the power draw even further, including disabling HDMI, changing the overclock settings, and futzing with the lone ACT LED.

![Raspberry Pi Zero - new with adapter cable](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/pi-zero-new.jpg)

I decided to spend some time testing these theoretical power-saving techniques on my Pi Zero, and here are some of the tips I've come up with (note that these techniques work with any Pi, not just the Zero):

Technique Power Saved Notes

Disable HDMI
25mA
If you're running a headless Raspberry Pi, there's no need to power the display circuitry, and you can save a little power by running `/usr/bin/tvservice -o` (`-p` to re-enable). Add the line to `/etc/rc.local` to disable HDMI on boot.

Disable LEDs
5mA per LED
If you don't care to waste 5+ mA for each LED on your Raspberry Pi, you can [disable the ACT LED](https://www.jeffgeerling.com/blogs/jeff-geerling/controlling-pwr-act-leds-raspberry-pi) on the Pi Zero.

Minimize Accessories
50+ mA
Every active device you plug into the Raspberry Pi will consume some energy; even a mouse or a simple keyboard will eat up 50-100 mA! If you don't need it, don't plug it in.

Be Discerning with Software
100+ mA
If you're running five or six daemons on your Raspberry Pi, those daemons can waste energy as they cause the processor (or other subsystems) to wake and use extra power frequently. Unless you absolutely need something running, don't install it. Also consider using more power-efficient applications that don't require a large stack of software (e.g. LAMP/LEMP or LEMR) to run.

A few other seemingly obvious optimizations, like under-clocking the CPU, don't make a discernible impact on idle power consumption, and make a minimal difference in any real-world projects that I've measured. Do you have any other sneaky techniques to steal back a few mA?

For the Raspberry Pi Zero, I used all the above techniques, and here were the results:

  1. Raspbian Jessie Lite nothing besides microSD card, and ACT LED on: **100 mA @ idle**
  2. Same as #1, but disable ACT LED and disable HDMI: **80 mA @ idle**
  3. Same as #1, but plug in a display, keyboard, trackpad, and WiFi adapter: **310 mA @ idle**(!!)

As you can see, it pays to conserve--if you don't need it, cut it away to save power! With the Pi Zero and these power saving techniques, you can extract a _lot_ of usage even in low-power scenarios, like solar energy or running off a battery.

See related:
