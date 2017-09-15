# Raspberry Pi Zero - Power Consumption Comparison

_Captured: 2017-09-03 at 13:05 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-power)_

> **tl;dr**: The Raspberry Pi Zero uses about the same amount of power as the A+, and at least 50% less power than any other Pi (B+, 2 B, 3 B).

On November 26, the Raspberry Pi foundation announced the [Raspberry Pi Zero](https://www.raspberrypi.org/blog/raspberry-pi-zero/), a $5 USD computer that shares the same architecture as the original Raspberry Pi and A+/B+ models, with a slightly faster processor clock (1 Ghz), 512 MB of RAM, and sans many of the essential ports and connectors required for using the Pi as an out-of-the-box computer.

![Raspberry Pi Zero - new with adapter cable](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/pi-zero-new.jpg)

> _The Raspberry Pi Zero - quite a small Linux computer!_

If you're considering buying on Pi Zero and using it as a 'lite' desktop computer, you might want to rethink your strategy; the Pi model 2 B has four full-size USB 2.0 ports, a LAN port, full-size HDMI, audio/video out, and more. This little Zero just has one micro USB port and mini HDMI port (both require adapters for most uses), no network port, no camera (the latest Zero revision includes a mini camera connector!) or display connectors, and if you want a header for GPIO use, you have to solder one on yourself!

But this board _is_ pretty awesome for some use cases, like embedded computing (think popping one into a halloween costume, or using a few in a robotics project), or experimentation where you don't want to worry about accidentally blowing up an expensive computer/control device (figuratively _or_ literally!).

One of the most important questions, then, is how much power does the Pi Zero consume? If you want to use it in an embedded application, you need to make sure it's using as little power as possible.

![Raspberry Pi Zero - Power consumption maximum during boot](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/pi-zero-power-consumption-max-boot.jpg)

> _Consumption stayed around 120-140mA during boot..._

  

![Raspberry Pi Zero - Power consumption minimum during idle](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/pi-zero-power-consumption-min-idle.jpg)

> _...and dropped to 50-70 mA during idle._

  


In the past, for the [Pi Dramble](https://github.com/geerlingguy/raspberry-pi-dramble/wiki) project, I've measured [power consumption for all the other Pi models](https://github.com/geerlingguy/raspberry-pi-dramble/wiki/Power-Consumption) I own (A+, B+, and model 2), so I thought I'd use my [PowerJive USB Power Meter](https://www.amazon.com/PowerJive-Voltage-Multimeter-chargers-capacity/dp/B013FANC9W/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=2fbe64dad50fdda17bcbb7a803c6b717) to measure the usage for the Zero for comparison:

Pi Model Pi State Power Consumption

A+
Idle, HDMI disabled, LED disabled
80 mA (0.4W)

A+
Idle, HDMI disabled, LED disabled, USB WiFi adapter
160 mA (0.8W)

B+
Idle, HDMI disabled, LED disabled
180 mA (0.9W)

B+
Idle, HDMI disabled, LED disabled, USB WiFi adapter
220 mA (1.1W)

model 2 B
Idle, HDMI disabled, LED disabled
200 mA (1.0W)

model 2 B
Idle, HDMI disabled, LED disabled, USB WiFi adapter
240 mA (1.2W)

Zero
Idle, HDMI disabled, LED disabled
80 mA (0.4W)

Zero
Idle, HDMI disabled, LED disabled, USB WiFi adapter
120 mA (0.7W)

As you can see in the table above, the Zero uses a similar amount of power as the long-time power-sipping champ, the A+--both use less than half the power of any other more fully-equipped Pi. This is no doubt due to the lack of extra ports and circuits that are active on the Pi itself. This means that a small battery pack (say, a flat Li-Ion pack rated at 1,400 mAh) should last well over 4 hours, even if you have moderate activity while using a cheap USB WiFi dongle!

If you don't need WiFi or some other network adapter, [disable the ACT/PWR LED](https://www.jeffgeerling.com/blogs/jeff-geerling/controlling-both-pwr-and-act), [follow these other Pi energy-saving tips](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy), and use a 2,000+ mAh battery pack (like one of the cheap ones you can get for phone charging), you can probably eke out a day's worth of Pi Zero usage, or more.

This isn't quite as good as you can get with an Arduino (sipping energy at 10-30 mA, or less if you optimize for power savings), but I'm a lot more likely to run Pi Zeros 24x7 for monitoring projects (as long as their networking needs are limited) than any other Pi model.

See related:
