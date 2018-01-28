# Raspberry Pi On Off Switch with Power Scheduling

_Captured: 2017-12-08 at 13:18 from [www.averagemanvsraspberrypi.com](http://www.averagemanvsraspberrypi.com/2017/11/pi-on-off-switch.html)_

![Witty Pi on off switch](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2017/11/Raspberry-Pi-On-Off-Switch-with-Power-Scheduling.png)

> _No more unplugging that power cable_

Ask any Raspberry Pi user what they find irritating about the Pi, and I guarantee a good majority will talk about the lack of an on/off switch.

I don't know of any other electrical 'thing' in my life that doesn't have a switch to turn it on or off. Imagine having to plug your kettle in every time you made a brew?

As always, where there's a problem, there's big bucks to be made fixing it. Enter [UUGear](http://www.uugear.com/). They created an add-on board called the Witty Pi to cover all your Pi power management needs, including a much-needed power switch.

Odd name aside, this little chap has made my day-to-day Pi usage tidier and much more convenient. It's also rocking some other cool functions and special sauce that I haven't got a project for yet, but I'm exploring them today anyway.

Let's have a gander!

![Witty Pi 2 assembled](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2017/11/Witty-Pi-Assembled.jpg)

> _The Witty Pi 2_

## First Impressions

I'm generally not a fan of the new breed of add-ons that offer 47 sensors and 72 different ways of using them. The idea is great, and in terms of value it makes sense, but I can't even imagine trying to code stuff like that - they simply scare me off.

So, when the makers of the Witty Pi got in touch offering a sample, I wasn't sure it was for me. The board _appeared_ to have lots of features, jumpers, chips, shiny things and solder. It looked complicated, and I don't do complicated.

I made it clear to the guys at UUGear that I couldn't guarantee a success story, but they confidently sent over a board anyway.

## In The Bag

So what do you get? The board and fixings came in a pretty standard anti-static bag, however retail packaging may be different. In terms of assembly this board is of the pre-soldered surface-mount variety. The only graft you need undertake is the Pi stand-offs and popping in the battery.

![Witty Pi 2 Kit](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2017/11/Witty-Pi-Kit.jpg)

> _The Witty Pi 2 Kit_

## Pi On Off Switch

I'm not covering setup/code here because the [user guide](http://www.uugear.com/doc/WittyPi2_UserManual.pdf) is spot on. It's clear, very detailed and has lots of images to help you.

What I do want to cover is my favourite feature - the switch. Simply put, it does the thing the Pi should have been doing since day 1 - it lets you keep your power cable connected and yet fully power on/off the Pi safely.

I was initially concerned that the add-on board would either use too many pins or would clash with the official touchscreen I was using (as the screen uses I2C), but it turns out it only uses GPIO4 and TXD for the switch. You simply install the provided scripts and the button is ready to use.

_Note: The real-time clock feature seems to cause a clash with the Pi screen's I2C usage - but it also seems that you can remove those pins from the screen and everything continues to work fine._

I'm using mine in conjunction with my [official 7″ display screen](http://amzn.to/2jBKpKJ) and rather fetching [metal stand from PiggiPi](http://www.averagemanvsraspberrypi.com/2016/09/aluminium-screen-stand.html), which due to the open rear fits just fine. Here's a video I posted to Instagram showing it in action:

## Witty GUI & Power Schedules

I get carried away with the switch as I'm finding it so handy, but the Witty Pi also does some really clever power schedule stuff all managed by a GUI they created.

This is a very cool feature, especially for mobile/battery projects where power is a constant constraint. I've played around with some projects that got the Pi to wait for long periods of time between doing something (checking temperature, taking a picture etc), but all the while the Pi was still turned on and using power.

![Witty Pi GUI](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2017/11/Witty-Pi-GUI.png)

> _Use the on-screen interface to set your power schedule_

The GUI lets you easily set automatic shut down/start-up times (or use their [online schedule script generator](http://www.uugear.com/app/wittypi-scriptgen/) for really advanced schedules) without you ever having to be present or press any buttons. It's sorcery I tell you!

This gives me some great ideas for combining with battery add-ons like the [PiJuice](https://www.pi-supply.com/product/pijuice-standard/). I wonder how long a PiJuice would last if you set the Witty Pi to turn on, take a picture (startup script), then turn off again straight after - every hour?

Surely a good while, meaning some very cool time-lapse photography from some very weird and wonderful locations.

## Real-Time Clock

A real-time clock (RTC) keeps your Pi's time/date accurate when power is lost. The Witty Pi has one of these chips built-in, which is why the board comes with a little coin battery - it gives the Witty Pi enough juice to keep time ticking along (a bit like a watch).

As you can imagine, it's quite essential for the Witty Pi to know the correct time otherwise your power schedules would be all over the place. A provided script lets you set the RTC's time and some other options.

However, even if you're not using the power schedules, you can still use the Witty Pi as a RTC and power switch - which is what I'm doing just now.

![Witty Pi Script](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2017/11/RTC-Settings.png)

> _This handy script is provided to help you set up your RTC and power schedules_

## Bank It

Clearly there's a lot of reasons why you'd want to use the Witty Pi with a power bank for remote projects, however some power banks will stop 'offering' power if they don't detect any current draw - that's certainly true for the few I have anyway.

When your Witty Pi shuts down on schedule, your power bank might think it's disconnected and turn off completely.

To counter this, the clever chaps over at UUGear added a little pulsing LED to the board that draws about 100mA of current every 10 seconds. That 'should' keep most power banks awake, but it all depends on what your particular model falls asleep on. Luck of the draw here, no guarantees.

## Not So Complicated After All

So that's it, the Witty Pi 2. Initially I thought it was another 'do everything' board, but on closer inspection it's rocking a few solid features with good links between them:

  * A manual Pi on off switch
  * Power Schedules
  * A real time clock - supporting the power schedules

Ignore the jumpers - they make the board look more complicated, but they're just in place as optional setting to change the GPIO pins used or turn off the trickle power feature. Most of us won't need to touch these, and the guide is there if you do.

## Want One?

The Witty Pi 2 can be bought directly from UUGear. I've also found them for sale at The Pi Hut and Amazon:

UUGear: [http://www.uugear.com/store/witty pi 2](http://www.uugear.com/product/wittypi2/)

The Pi Hut: <https://thepihut.com/collections/brand-uugear>

Amazon: <http://amzn.to/2hHUVza>

Until next time…
