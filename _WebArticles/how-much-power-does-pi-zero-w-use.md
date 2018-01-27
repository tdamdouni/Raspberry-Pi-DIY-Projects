# How much power does Pi Zero W use?

_Captured: 2017-10-11 at 09:44 from [raspi.tv](http://raspi.tv/2017/how-much-power-does-pi-zero-w-use)_

![Pi Power Usage chart adding Zero W](http://raspi.tv/wp-content/uploads/2017/02/Pi-Power-Usage-Zero-W-150x150.png)

It's become traditional for me to do power measurements of any new Pi and update my chart. People have even started asking me about it on launch days (the cheek of it)…

Needless to say I have done some power measurements in my Zero W testing and here are the results. Essentially, the Pi Zero W seems to require 20 mA more than the no-wifi Zero. This is almost certainly due to the new radio chip.

### Methodology

Measurements were taken using my standard procedure (same as for the last several Pi models launched). Current and voltage are measured using my eMeter with a calibrated 20 Amp shunt whilst performing four different activities. "Shooting video" is done without saving the video output to the SD card. Watching video is done with a 1080p video on the SD card. The rest is self-explanatory. The camera module is unplugged for all but the shooting video test. Only HDMI and a USB keyboard dongle were plugged in. The Pi Zero W was connected to wifi, but no bluetooth devices were in use.

![Pi Power Usage table adding Zero W](http://raspi.tv/wp-content/uploads/2017/02/Pi-Power-Usage-Zero-W-table-1024x246.png)

> _Pi Power Usage table adding Zero W (at 5.19V)_

### Why Anomolous?

No doubt you will wonder why the shooting video figure is anomolously lower on the Zero W. I do too. But it could be experimental error - we are pushing the limits of the eMeter's resolution here. These figures are just a guide. If you need something really accurate, you'll need to buy expensive gear and do some measurements. But my measurements usually line up pretty well with the official figures and those of people like Dave Akerman who DO have fancy-pants meters by the likes of Fluke. So, if you need a guide to work out your probable battery duration, these are fine, but if you're going to use the figures for something that really matters, well, don't! Here's the chart…

![Pi Power Usage chart adding Zero W](http://raspi.tv/wp-content/uploads/2017/02/Pi-Power-Usage-Zero-W-1024x612.png)

> _Pi Power Usage chart adding Zero W (at 5.19V)_

So I hope these figures are a useful guide, but don't bet your life on them please.
