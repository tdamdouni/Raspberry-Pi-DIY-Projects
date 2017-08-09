# Turn your Pi into a low-cost HD surveillance cam

_Captured: 2017-05-06 at 15:10 from [www.raspberrypi.org](https://www.raspberrypi.org/blog/turn-your-pi-into-a-low-cost-hd-surveillance-cam/)_

Local government CCTV is awful, and it's everywhere in the UK. But I'm much happier about surveillance in the hands of private people - it's a matter of _quis custodiet ipsos custodes? _(Who watches the watchmen?), and I'm pleased to see the Raspberry Pi bring the price of networked motion-sensitive HD surveillance cameras down to be affordable by consumers. Off the shelf, you're looking at prices in the hundreds of pounds. Use a Pi to make your own HD system, and your setup should come in at under £50, with a bit of shopping around. This is a great use case for the value bundle our distributors are offering at the moment, where [a camera board and a Model A Raspberry Pi with an SD card is coming in at $45](http://www.raspberrypi.org/archives/5048).

[Christoph Buenger has used a Pi and a camera board as the guts of his project](http://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera), and, in a stroke of sheer genius, has waterproofed the kit by housing it in one of those fake CCTV shells you can buy to fool burglars. The fakes are head-scratchingly cheap - I just found [one that looks pretty convincing](http://www.amazon.co.uk/gp/product/B0095RE0K0/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B0095RE0K0&linkCode=as2&tag=raspberrypi06-21) on Amazon for £6.24.

![](https://www.raspberrypi.org/app/uploads/2013/10/camera.jpg)

> _Christoph's camera, snug inside its housing_

Christoph has made build instructions and code available so you can set your own camera up. It does more than just film what's in front of it: he's added some motion-detection capability to run in the background, so if the camera spots something moving, it'll start recording for a set period.

At the moment, Christoph saves video to a Windows shared folder (you can, of course, save it wherever you like if you're not a Windows person). The live stream is also available to be viewed online if you configure your local network.

![](https://www.raspberrypi.org/app/uploads/2013/10/live_picture.jpg)

> _A live (and topical) frame from the camera's video feed_

Christoph's looking at adding more functionality to the setup. [He says](http://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera):

There are a thousand things you can do with such a surveillance cam basic setup now. How about sending [Growl](http://growl.info/) notifications when some motion was detected? [This guide](https://medium.com/p/2d5a2d61da3d) explains how to add this functionality easily.

Or you could easily add a temperature-sensor to the cam. It's only a few bucks and can be [integrated very easily](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing).

We're currently working on integrating the live stream into MediaPortal server so that we can switch to a TV channel to see the live stream from the cam in our office.

If you want extra security, you could also add a battery pack to the camera. Be sure to buy one that is able to charge simultaneously while powering the Raspberry. This would enable you to detect if some bad guy cuts the power strips of your camera and send some alert messages to you (i.e. SMS or email) including the video of the disturber.

Let us know if you set up your own security camera with the Pi. We'd love to see what adaptations you come up with!
