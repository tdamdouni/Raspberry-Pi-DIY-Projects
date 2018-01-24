# PiJuice – portable battery power for your Raspberry Pi – a review

_Captured: 2017-11-14 at 11:39 from [www.recantha.co.uk](http://www.recantha.co.uk/blog/?p=17790)_

![](http://www.recantha.co.uk/blog/wp-content/uploads/2017/11/PiJuice-Battery-Back-Left.png)

The **[PiSupply PiJuice](https://www.pi-supply.com/?s=pijuice&post_type=product&tags=1&limit=5&ixwps=1)** is finally here!

## What is the PiJuice?

It's a battery power pack HAT for your Raspberry Pi.

## The Review

[Tim Richardson](https://twitter.com/Geeky_Tim) ([@Geeky_Tim](https://twitter.com/Geeky_Tim)) has joined me on this review to give his insight, so we'll be moving back and forth between our two viewpoints. We were handed the PiJuice review bundle at a recent [CamJam](http://camjam.me) so decided to do a joint review!

## Some background

It all started [over two years ago on Kickstarter](https://www.kickstarter.com/projects/pijuice/pijuice-a-portable-project-platform-for-every-rasp) as a really good idea that went awry. It's taken Aaron Shaw and the team that two years to get the final product to their backers. A lot of that time, unfortunately for both them and us backers, they have had numerous issues which have been endlessly discussed in the over 2000 comments on their [Kickstarter pages.](https://www.kickstarter.com/projects/pijuice/pijuice-a-portable-project-platform-for-every-rasp) We won't go over those issues again here as some is speculation and it's hard to know fact from fiction; but the product is finally here and (almost) ready to ship to backers and to go on general sale. So, let's take a look.

## The Hardware

_Tim_: The final product has certainly not been rushed. It is a very clean circuit board that will plug into all 40 pin Pis. You can power your Pi from the battery (a Motorola BP7X 1820mAh phone battery) alone, or by powering the Pi directly, leaving the battery as a backup, power the board itself, or both. Why would you want to power both the Pi and the board at the same time? The PiJuice allows you to run the Pi from the mains while you use another supply, be it mains or one of the solar panels either available from PiSupply or elsewhere, to keep the battery charged. Then, if you lose power, the battery will automatically take over and keep your Pi running. Within the first few minutes of testing I wanted to swap the power over from one supply to the other and unplugged the Pi; it kept running happily without interruption.

_Mike_: I, too, was impressed with the hardware. The main PiJuice board is absolutely gorgeous on the underside with a huge amount of components squeezed in. I even love the colour of the PCB (a kind of 'hot pink') which closely matches the packaging. It's a nice, completely irrelevant touch. I love it.

![](http://www.recantha.co.uk/blog/wp-content/uploads/2017/11/PiJuice-HAT-Bottom.png)

The battery is a hard-cased Lithium Ion affair, rather than a LiPo (which tend to be a bit… squishier…) so is potentially much safer for it.

![](http://www.recantha.co.uk/blog/wp-content/uploads/2017/11/Battery-Top.png)

The board is fully hot-swappable. I placed it on the Pi while it was turned on and powered by a PSU and it worked fine. I removed the PSU, it was still 'on'. I removed it in the same cavalier fashion with the PSU plugged in and the Pi remained up and didn't reboot or anything.

I have to say, I'm not crazy about the PiJuice automatically being 'on'. As soon as I plugged it into the Pi (with the Pi off), it started up with no warning or any kind of button press. It's a small thing, but given that I'd just finished testing the GoPiGo, which has a power-on button, it's something I noticed.

Another thing to say is that the small buttons on the side of the PiJuice are labelled in the most tiny font imaginable, due to the space available. They also seem in a strange order: SW2, SW3, SW1 from left-to-right.

I experienced a **possible **interaction with the Pi 3's wi-fi - my connection was quite a bit weaker with the PiJuice on top than without it. That might be a result of where I was (at the bottom of my garden) or it _could _indicate some RF interference by having the battery and circuitry so close to the Pi 3.

The LED on the side still flashes occasionally when the PiJuice is not plugged into the Pi. I would prefer to have had some way of turning it completely 'off' and not draining the battery at all, but that's a small thing: you can always remove the battery; in fact, that's probably the best advice if you want to ensure that the PiJuice is truly 'off'.

_Tim_: With the growth of the IoT (Internet of Things) over the last few years, being able to power your projects even in the event of power failure is going to be extremely useful (although loss of network power may cause you problems!). With many smaller devices now being battery powered, being able to continue to have a Raspberry Pi hub on your premises is going to be essential.

The PiJuice pass-through header means that you can plug another HAT on top of the PiJuice HAT. The three buttons and two LEDs can be configured to do what you need them to, and there are two further interfaces that I have not yet found full documentation for, but to be honest, this is not unusual for unreleased hardware; I am sure PiSupply will supply more information in due course.

_Mike_: Even though the battery is quite thick, HATs and pHATs will still fit on the extended header provided. I tried it fitted with a HAT that had a low-profile header (in my case, the [Pimoroni UnicornHAT](https://shop.pimoroni.com/products/unicorn-hat)) and, of course, with a full-sized header, like on the [RasPiO Pro HAT](http://rasp.io/prohat/) (the one with the pins in the correct order and the breadboard on top) and also the [Pimoroni Explorer HAT](https://shop.pimoroni.com/products/explorer-hat). An extended header is, of course, an old solution to the issue of stacking HATs, but it does work very well here and the battery doesn't get in the way unless you have a lot of components sticking out on the bottom of your stacked HAT/pHAT. The good news is that the PiJuice uses only I2C and power pins, so there is no clashing of hardware. Even if there _is_ an address conflict, the PiJuice's I2C address is configurable via the software package, which we will now look at.

In use, the power supplied by the battery is steady and reliable. Here is a quote from [The MagPi review](https://www.raspberrypi.org/magpi/pijuice-review/) about how long the battery lasts:

> "We performed a simple uptime test with a Python script that periodically logged how long the Pi had been running. On an idling Pi 3, it averaged around 4 hours. A little shorter than we'd hoped for, but on a Pi Zero or A+ you should be able to achieve near double that."

Now, of course, you can get very high-capacity USB power banks that will last longer than that, but if you're looking for a more compact solution, the PiJuice has a lot to recommend it.

## The Software

_Tim_: Setting up the PiJuice is as simple as it can be; stack the PiJuice on top of your Pi and that is it. As long as the battery has charge, the Pi will run. However, there is a control package that will enhance your experience, installed with the simple one line:
    
    
    sudo apt-get install pijuice

This will install the PiJuice configuration tool that will show you how much juice you have left, whether it's charging and allows you to configure how the supply and Pi reacts to various events. These events include a low power warning and a "charge-reached" trigger. You can also start your Pi on a schedule, and program the three buttons on the side of the PiJuice to do what you'd like them to do such as shutdown, reboot or any other action.

_Mike_: After you've installed the software, you get a nice little battery-level icon which appears near to the Bluetooth and wifi icons on the taskbar of Raspbian. Hovering over it gives you the current battery level.

![](http://www.recantha.co.uk/blog/wp-content/uploads/2017/11/power_icon.png)

Right-clicking the icon lets you into the configuration software where you can:

  * Set a 'wake-up alarm' so that the Pi starts up at a specified time.
  * Configure various events to happen on low charge, low voltage and other events.
  * Configure user scripts that can be used in conjunction with other settings.
  * Change the I2C addresses of both the HAT and the Real-Time Clock.
  * Change the actions of the buttons and what happens when you press, release, single-press, double-press and long-press them.
  * Configure the LED to behave in a certain way.
  * Take a look at the various pre-configured integral options. You can customise them if you want to.
  * Update the Firmware of the board.

The interface is a little basic-looking but is very flexible in practice, and that is far more important on a product such as this. On other products, such as the cheap 'UPS' boards you can get from China, there is no software at all!

## Conclusion

_Mike_: There _are_ other solutions out there for powering your Pi. You _can _pick up a Chinese equivalent for about half the price and use a LiPo battery to do it. However, I much prefer the Li-ion battery that comes with the PiJuice. It seems safer, seems a better package and it clips into the HAT rather than being glued or taped on top. You could use a USB power bank to do it, but of course these tend to be much less compact than the PiJuice's HAT and battery combination. And none of these other solutions come with the software that PiJuice comes with - and this is important. If you want your Raspberry Pi to know about your charge level, the PiJuice is an easy-to-recommend solution. If you want your power solution to be well-designed, the same can be said.

_Tim_: At this stage, the documentation is quite 'light', which means you are going to be on your own until more people have their hands on the HAT and have explained what each of the settings means; the UI shows a lot of promise for customisation, but until we know more about what goes in which box, the majority of users will be stumped. In the relatively short time that I have had the review unit I have not had the time for a project which will allow me to get the full potential out of it.

_Mike_: I can see this being used for a variety of different projects (some of which are in the [Quick Start guide](https://github.com/PiSupply/PiJuice/blob/master/Documentation/PiJuice%20Guide.pdf)) such as a camera, weather station or just as a UPS for your Pi to get a better guarantee of uptime.

_Tim_: If you just want to power your Pi for, say, a robot, then you may be better off using a 'lipstick' type phone charger - they are cheaper, but less versatile. For anything else, where you need your Pi powered away from a socket, or you need to ensure that power is not lost during brown- or black-outs, then I **recommend** the PiJuice. It's a well-made piece of hardware and, despite documentation being limited at this early stage, it's powerful (excuse the pun).

_Mike_: Overall, I have to say the PiJuice is **very promising** and I'm offering a **cautious recommendation**. Get the documentation finished and the examples up on the website and PiSupply will be onto a winner.

## Buying it

You can [take a look at the various PiJuice packages here](https://www.pi-supply.com/?s=pijuice&post_type=product) which start at £48\. They will be available within the next few months once the Kickstarter pledges have been fulfilled.
