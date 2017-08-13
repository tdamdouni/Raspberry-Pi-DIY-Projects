# Spiral Speaker Build

_Captured: 2017-08-01 at 07:12 from [frederickvandenbosch.be](http://frederickvandenbosch.be/?p=2204)_

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_3241.jpg)

The team at [Pi Supply](https://www.pi-supply.com/) was kind enough to send me a [Justboom Amp Zero pHAT](https://www.justboom.co/product/justboom-amp-zero-phat/) to play with. The Amp Zero combines both DAC (Digital to Analog Converter) and Amp (Amplifier), making it a great choice for a DIY Pi Zero speaker build. To distinguish this build from the many other existing Pi related audio projects, I decided to give it a special twist, literally. The build is inspired by the [spiral plywood vase](http://www.iliketomakestuff.com/spiral-plywood-vase/) by Bob from [I Like to Make Stuff](http://www.iliketomakestuff.com/).

  * [1 Electronics](http://frederickvandenbosch.be/?p=2204)

The electronics are centered around the Amp Zero, but to add a bit of dynamicity to the whole, a Scroll pHAT is used to display the spectrum of the audio in real time.

This makes the list of electronics components, the following:

## Justboom Amp Zero

When unboxing the Amp Zero, following items were included in the box:

  * two Justboom stickers (yay stickers!)
  * getting started link
  * Max2Play 30-day voucher, a Pi OS for home-entertainment
  * Roon Labs 60-day voucher
  * Amp Zero pHAT
  * DC barrel jack adapter
  * IR receiver
  * four spacers with screws
![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2841.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2850.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2851.jpg)

Connecting the Amp Zero to a Pi Zero requires standard male header pins to be soldered on the Pi. After having screwed on the spacers, the pHAT slides on top of the header pins, onto the Pi Zero, resulting in a very slim package capable of fitting in a small Altoids-like tin.

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2857.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2854.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2856.jpg)

This is how the Pi Zero and Amp Zero pHAT will be integrated into my speaker build.

If you don't feel like building your own enclosure, it is possible to purchase a case to accommodate the Pi Zero and Amp Zero. It makes for a very compact controller for your speakers!

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2843.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2858.jpg)

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/IMG_2871.jpg)

For detailed assembly instructions, be sure to check out the [official guide](https://www.justboom.co/start/set-up-justboom-amp-zero-phat-and-case/)!

### Software

I'm using the latest [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) image, as I require the Scroll pHAT software and some custom scripts to run. If you are using only the Amp Zero, other distributions like [OSMC](https://osmc.tv/) or [Volumio](https://volumio.org/) for example, already have integrated support for the pHAT.

Enabling support for the Amp Zero is a piece of cake though, as it only requires you to add or comment following lines in the _/boot/config.txt_ file:

## Scroll pHAT

The Scroll pHAT is used to display the spectrum of the audio. I based myself on an [example](https://learn.pimoroni.com/tutorial/sandyj/scroll-phat-spectrum-analyser) by Pimoroni, which also contains the installation procedure. Pimoroni's example processes audio files, but with some minor modifications, I was able to have it display the spectrum of an audio stream instead.

To feed the spectrum analyser with an audio stream, a loopback device has been created. This was achieved by modifying the ALSA config in _/etc/asound.conf_:

pcm.dac {

type hw

card 0

}

pcm.both {

type route;

slave.pcm {

type multi;

slaves.a.pcm "plughw:0,0"

slaves.b.pcm "plughw:Loopback,1,0"

slaves.a.channels 2;

slaves.b.channels 2;

bindings.0.slave a;

bindings.0.channel 0;

bindings.1.slave a;

bindings.1.channel 1;

bindings.2.slave b;

bindings.2.channel 0;

bindings.3.slave b;

bindings.3.channel 1;

}

ttable.0.0 1;

ttable.1.1 1;

ttable.0.2 1;

ttable.1.3 1;

}

pcm.!default {

type plug

slave.pcm "both"

}

ctl.!default {

type hw

card SB

}

This means that by default, audio is sent to output device "both", which consists of two outputs: the DAC and a loopback device. The loopback device's counterpart will then be used to feed the stream to the spectrum analyser.

![](http://frederickvandenbosch.be/wp-content/uploads/2016/12/Screen-Shot-2016-12-21-at-22.22.44.png)

The modified code, visualising the spectrum on the Scroll pHAT:

To take into account possible crashes of the spectrum analyser, a script has been created to restart it in case it is not or no longer running.

12345678910111213 
sudo modprobe snd-aloopsleep 5while truedoif ps aux | grep -v "grep" | grep "spectrum" 1>/dev/null;thensleep 1elsesudo /home/pi/spectrum.py &fidone

Inspired by Bob's spiral vase, I attempted to recreate something similar for the speaker. By offsetting square pieces of wood, a spiral is obtained. One of the pieces is larger, serving both as a stand and a place to install the Scroll pHAT in.

The Pi Zero and Amp Zero are housed inside the speaker, exposing the wifi dongle and power connector at the back.

Too special? You be the judge!
