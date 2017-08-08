# Arduino vs Raspberry Pi: Which Is The Mini Computer For You?

_Captured: 2015-11-12 at 10:14 from [www.makeuseof.com](http://www.makeuseof.com/tag/arduino-vs-raspberry-pi-which-is-the-mini-computer-for-you/)_

[Ads by Google](https://support.google.com/adsense/troubleshooter/1631343?url=http%3A%2F%2Fwww.makeuseof.com%2Ftag%2Farduino-vs-raspberry-pi-which-is-the-mini-computer-for-you%2F&client=ca-pub-9894449314507324)

![arduino vs raspberry pi](http://cdn.makeuseof.com/wp-content/uploads/2013/05/featured-pi-vs-arduino.jpg?bccfec)

> _arduino vs raspberry pi_

You're looking for a small computer to power a laser turret that can shoot multi-coloured balloons - it's a common situation we all find ourselves in at one point or another - and you've heard good things about both Arduino and Raspberry Pi. But you can't decide - which the best mini-computer for your project? Which is going to prevail as the most useful once you've disassembled the turret thanks to that incident with the neighbour's cat? Which could you play movies on? Don't worry, James is here to explain all!

## What's The Difference?

The Arduino and Raspberry Pi may look quite similar - they're both cute little circuit boards with some chips and pins on them - but they are in fact very different devices. The Arduino is in fact a micro-controller; not a mini-computer. A micro-controller is just a small part of what makes a computer, and only provides a subset of the functionality of the Rapsberry Pi.

Although the Arduino can be programmed with small C-like applications, it cannot run a full scale "operating system" and certainly won't be replacing your media center anytime soon. The Raspberry Pi on the other hand, is a computer. If you're reading this site, I'm just going to assume you know what that means.

## Strengths & Weaknesses

So is the Arduino useless then? Hardly - an Arduino is perfect for _electronics projects. _It contains a set of input and output that can often be connected directly to components and sensors, and is incredibly easy to just jump straight into making something. This makes it ideal for prototyping things.

The Arduino runs the Arduino firmware - a basic bit of core software which allows it to communicate with a computer over USB and gives access to all the features. You generally wouldn't replace this firmware, but it is possible. Once your application has been loaded, you can just plug it in anywhere and it'll start working immediately - you don't need to reboot, plug in a keyboard, or choose an application to run. It does the one job it's been programmed to do, and it does it immediately.

![arduino vs raspberry pi](http://cdn.makeuseof.com/wp-content/uploads/2011/09/photo-arduino.jpg?bccfec)

> _arduino vs raspberry pi_

The Raspberry Pi on the other is a complete, functional, mini-computer. It requires an _operating system_ - the first thing you need to choose that will dramatically affect your experience - and has all the bits and pieces you might expect a full computer to have (just in a smaller scale). Storage is provided from a micro-SD card, while built-in Ethernet allows for networking (you can get [networking on Arduino](http://www.makeuseof.com/tag/give-your-arduino-project-its-own-mini-webserver-with-an-ethernet-shield/) too, but it requires an add-on "shield").

At the heart of the Pi is a Broadcom Arm-v6 CPU; it has memory, and a graphics processor driving the HDMI output. You can plug in a keyboard and monitor, load up Linux, and the less technically savvy might have no clue how tiny the machine driving everything really is. The Pi is an incredibly powerful platform in a very small package - perfect for embedded systems, or projects requiring more interactivity and processing power.

![arduino vs raspberry](http://cdn.makeuseof.com/wp-content/uploads/2013/04/muo-rasppi-sd.jpg?bccfec)

> _arduino vs raspberry_

That said, the Raspberry is significantly more complex for simple electronics projects. For example, everyone's first project is some derivative of [flashing an LED on and off](http://www.makeuseof.com/tag/arduino-traffic-light-controller/). On the Arduino, this involves connecting an LED and resistor to two pins, then uploading about 8 lines of code. That's it. On the Raspberry Pi - assuming you have a fully functional operating system already installed and set up as you like - you then need to install some libraries to help you control the GPIO pins (that's the bits you connect components to).

There are lots of libraries to choose from though, depending on which language you want to program in - including visual designers such as [Scratch](http://cymplecy.wordpress.com/2013/04/22/scratch-gpio-version-2-introduction-for-beginners/). [WiringPi](https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/3-more-leds-and-a-button/) lets you write in the same language that Arduino is derived from. Finally, you may need to compile your app before running it. The point is, you can do nearly everything an Arduino can, on a Pi - but it's more complicated.

![arduino vs raspberry](http://cdn.makeuseof.com/wp-content/uploads/2013/05/scratch.jpg?bccfec)

> _arduino vs raspberry_

Another important point to remember here is that Arduino is the most popular platform for electronics projects, so even though electronics projects are possible on Raspberry Pi (and there certainly are [a few](http://blog.makezine.com/2013/04/14/47-raspberry-pi-projects-to-inspire-your-next-build/)), you won't find as nearly as many beginner tutorials to help you. It might be best to consider the Pi as an upgrade once you're ready to handle bigger and more demanding projects.

On the other hand, the Raspberry Pi is a mini-computer, the Arduino isn't. To understand that point a little more clearly, here's a small selection of operating systems you can install on the Raspberry Pi:

  * Raspian (based on Debian linux, and the "default").
  * Android ([barely](http://androidpi.wikia.com/wiki/Android_Pi_Wiki), but official support [is coming](http://www.raspberrypi.org/archives/1700)).
  * [RiscOS](https://www.riscosopen.org/content/).
  * [Plan 9](http://plan9.bell-labs.com/plan9/screenshot.html).

There's a nice test and usability reviews of some of these over [at TechRadar](http://www.techradar.com/news/software/operating-systems/raspberry-pi-operating-systems-5-reviewed-and-rated-1147941). There's even an [app-store](http://store.raspberrypi.com/projects).

![arduino vs raspberry](http://cdn.makeuseof.com/wp-content/uploads/2013/05/openelec.jpg?bccfec)

> _arduino vs raspberry_

And here's a list of operating systems you can install on the Arduino:

  * None

So, you're decided? Great. Start by checking out all our [Raspberry Pi](http://www.makeuseof.com/tags/raspberry-pi/) or [Arduino tutorials](http://www.makeuseof.com/tags/arduino/).

## WAIT! Why Choose At All?

Actually, you can have the best of both worlds; the Pi may be a more complex Arduino, and the Arduino can't nearly handle as much as the Pi - but have you considered using them together? This project - [AlaMode](http://hackaday.com/2012/07/23/the-proper-way-to-put-an-arduino-in-a-raspberry-pi/) - puts a stackable Arduino clone directly on top of the Pi, giving instant access to all the usual Arduino functions.

![arduino vs raspberry pi](http://cdn.makeuseof.com/wp-content/uploads/2013/05/alamode.jpg?bccfec)

> _arduino vs raspberry pi_

Or if Python is more your thing, just plug your Arduino into the USB of your Pi and use [this interface](http://www.doctormonk.com/2012/04/raspberry-pi-and-arduino.html).

I hope you're clearer on the differences between Arduino and Raspberry Pi now, but if not, the comment form is but a few hundred pixels away and I'd be happy to help where I can.
