# I built a wifi "walkie" talkie for my kids; now you can too!

_Captured: 2016-09-10 at 23:55 from [projectable.me](http://projectable.me/i-built-a-wifi-walkie-talkie-for-my-kids-now-you-can-too/)_

### Looking for something?

__

[ ![Daniel Chote's Project Blog](/content/images/2016/08/projectable-me-4.png) ](http://projectable.me)

Menu

__

In Featured 

In  [Raspberry Pi](/tag/raspberry-pi/) [talkiepi](/tag/talkiepi/) [golang](/tag/golang/) By  [Daniel Chote](/author/daniel/)

![I built a wifi "walkie" talkie for my kids; now you can too!](/content/images/2016/09/IMG_8925-1.JPG)

## Introducing [talkiepi](https://github.com/dchote/talkiepi)

[talkiepi](https://github.com/dchote/talkiepi) is a wifi "walkie" talkie for your kids and their friends. It provides a very simple "push to talk" interface. When you push the button and talk, all the other talkiepis in the channel will hear what is being said. 

talkiepi uses [Mumble](http://mumble.info) for its voice communication protocol. Mumble is an open source, lightweight, high quality voice chat system designed for use by PC gamers. Mumble lent itself perfectly for this use case. There are already software clients for all platforms (Mac, Win, Linux, IOS, Android), meaning you can talk with your talkiepi using your phone or computer, and you're not limited to just talkiepi devices! By utilizing Mumble channels, user registration, and access control lists, you can configure different groups of talkiepis, just like using different channels on a traditional walkie talkie.

[talkiepi](https://github.com/dchote/talkiepi) is built utilizing a [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/), [USB speakerphone](https://www.amazon.com/USRobotics-USB-Internet-Speakerphone-USR9610/dp/B000E6IL10), some basic electronic components, and a 3D printed enclosure. [talkiepi](https://github.com/dchote/talkiepi) runs a [mumble](http://mumble.info) [client](https://github.com/dchote/talkiepi) that has been designed specifically for push to talk via the push button interface. After it is setup on your wifi network and the software is configured, talkiepi will require little to no maintenance to use.

* * *

### talkiepi software on your Raspberry Pi

I have written an overview of the software and hardware interface at the [github repository for talkiepi](https://github.com/dchote/talkiepi). An install guide can be found at <https://github.com/dchote/talkiepi/blob/master/doc/README.md>, which will step you through installing talkiepi on your Raspberry Pi.

I have added some notes regarding my wifi trouble on the rpi3 [here](http://projectable.me/optimize-my-pi-wi-fi/).

* * *

### Building a talkiepi

##### Build without an enclosure:

You can assemble a talkiepi with or without the 3D printed enclosure. I initially prototyped the GPIO stuff on a breadboard, and that would be more than sufficient to play with if you didn't want to commit to a full build.

![breadboard](/content/images/2016/09/IMG_8844.JPG)

##### Print an enclosure:

If you want to do a full build of talkiepi you can download the 3D models from the [github repository](https://github.com/dchote/talkiepi/tree/master/stl). I printed my parts on my [Monoprice Select Mini 3D Printer](http://www.monoprice.com/product?p_id=15365). I printed in PLA with 100% infill. You _will_ need to rotate the models to print, but if you already have a 3D printer, you probably know what you need to do. If you don't own a 3D printer yet, there are many services that will print and mail you your parts! 

I designed the talkiepi enclosure in Autodesk's [Fusion360](http://www.autodesk.com/products/fusion-360/overview). If anyone would like to tweak the Fusion360 assembly, drop me a tweet [@dchote](https://http://twitter.com/dchote/) #talkiepi.

![fusion360](/content/images/2016/09/14195449_10154470917845419_4831834876665870570_o.jpg)

![](/content/images/2016/09/IMG_8946-1.JPG) ![](/content/images/2016/09/IMG_8947.JPG) ![](/content/images/2016/09/IMG_8939.JPG)

* * *

### talkiepi parts

I ordered most of these components from [Adafruit](https://www.adafruit.com), and a couple of parts from [Amazon.com](https://www.amazon.com). I already had the hookup wire, heat-shrink and resistors.

![talkiepi parts](/content/images/2016/09/IMG_8933.JPG)

  * [Raspberry Pi 3 Model B ~$35](https://www.adafruit.com/products/3055)
  * [Micro SD Card](https://www.amazon.com/SanDisk-Ultra-Micro-Adapter-SDSQUNC-016G-GN6MA/dp/B010Q57SEE/ref=sr_1_3?ie=UTF8&qid=1472828023&sr=8-3&keywords=16G+micro+sd+card)
  * [US Robotics USB Speakerphone (USR9610) between $4 and $12 (really cheap)](https://www.amazon.com/USRobotics-USB-Internet-Speakerphone-USR9610/dp/B000E6IL10/ref=sr_1_2?ie=UTF8&qid=1472828042&sr=8-2&keywords=US+Robotics+usb+speakerphone)
  * [Short right angle / left angle mini USB cable](https://www.amazon.com/gp/product/B01CXT43MQ/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
  * 5 x M3 nylon screws + 1 M3x20 nylon standoff
  * GPIO header connector (there are many options for this)
  * 2 x 5mm LEDs with [5mm LED holders](https://www.adafruit.com/products/2176)
  * [Pushbutton with LED](https://www.adafruit.com/product/1477)
  * 3 x 330ohm resistors
  * 2 x M3x15 + 2 x M3x25 stainless bolts (for the case)
  * 2 x M3x10 stainless bolts + nuts (for the speaker)
  * Hookup wire + heat-shrink
* * *

### The GPIO stuff

The GPIO interface usage is actually very simple. It is a push button with 2 separate LEDs for status indication and 1 LED within the push button that illuminates when it is transmitting.

![](https://github.com/dchote/talkiepi/raw/master/doc/gpio_diagram.png)

You can use any type of header connector. I initially used [one of these](https://www.adafruit.com/product/2222), but using smaller connectors (such as a 8 pin for the LEDs and a 2 pin for the button) makes it easier to fit and assemble.

![](/content/images/2016/09/IMG_8958.JPG)

Solder the 3 resistors to the ground pin, and solder your positive LED wires to the other pins.

![](/content/images/2016/09/IMG_8959.JPG)

Solder your negative LED wires to each of the resistors.

![](/content/images/2016/09/IMG_8960.JPG)

Slip on heat-shrink to protect from shorting. I put a larger piece of heat-shrink around all the resistors to keep them in a nice solid bundle.

Next up put together the button GPIO connector, you can either solder this on to your larger header, or like me, use a smaller 2 pin connector on pins 20 and 22.

Solder the 2 status LEDs on to their respective leads. Don't forget to slip on the LED holder boots and the heat-shrink before you solder!

![](/content/images/2016/09/IMG_8962.JPG)

* * *

### The USB speakerphone

Taking the speakerphone apart is really simple. There are two screws hiding under the rubber feet and two more screws holding the speaker in place.

![](/content/images/2016/09/IMG_8935.JPG) ![](/content/images/2016/09/IMG_8936.JPG) ![](/content/images/2016/09/IMG_8937.JPG)

Leave the foam on the microphone; the talkiepi case actually utilizes that to hold the microphone in place.

### Assembling talkiepi

I designed the enclosure to accommodate the Pi3 and the US Robotics speakerphone PCB specifically. Once you have printed the enclosure parts, I recommend you get a 3mm tap and tap the holes. If you don't have a tap, you can use one of your stainless bolts (carefully avoiding stripping out the holes).

![](/content/images/2016/09/IMG_8940.JPG)

Attach the right/left angle USB cable to the bottom right USB port of your Raspberry Pi. Mount the Raspberry Pi using the nylon screws. Use the standoff in the hole next to the 3.5mm audio jack.

![](/content/images/2016/09/IMG_8872.JPG )

Carefully unclip and disconnect the speaker from the speakerphone PCB and mount the speaker on the front panel using your M3x10 bolts+nuts. You will likely need to drill out the holes on the speaker to 3mm. Connect your GPIO harness to the Raspberry Pi.

![](/content/images/2016/09/IMG_8963-1.JPG)

Place the LED holders through the speaker cover and place the speaker cover and LED holders through the top panel, fastening the LED holders in place with their washers and nuts. Secure the LED push button in place. 

![](/content/images/2016/09/IMG_8964-1.JPG) ![](/content/images/2016/09/IMG_8965-1.JPG)

Now slide the LEDs with boots into the LED holders (_I used a little bit of silicone sealant to ensure they dont push out_).

![](/content/images/2016/09/IMG_8968.JPG)

Now mount the speakerphone PCB with the USB port facing towards the rear of the case (same direction as the Pi USB ports). Use the other two nylon screws to secure (one into the case and one into the standoff). Connect the USB cable to the speakerphone connector, folding/tucking the excess cable in the space behind the USB ports. Ensure your GPIO leads are routed cleanly around the speakerphone PCB, and that nothing could be shorting.

![](/content/images/2016/09/IMG_8969.JPG)

Finally attach the top cover to the bottom. Be sure to feed the wires nicely, and that everything looks tucked out of the way inside. Again, check for any shorts before fastening the top with the M3 bolts.

* * *

### Enjoy your talkiepi!

Thats it! You're ready to talk to another mumble client or, if you made two, your other talkiepi!

![](/content/images/2016/09/IMG_8925-2.JPG) ![](/content/images/2016/09/IMG_8926.JPG) ![](/content/images/2016/09/IMG_8927-1.JPG)

* * *

### Something different?

I attempted to do a paint finish, but I just don't have the patience, or workspace to do a good job of spraying something this small. I do however have a bunch of different colored PLA. Check out this blue print!

![](/content/images/2016/09/IMG_8978.JPG) ![](/content/images/2016/09/IMG_8979.JPG) ![](/content/images/2016/09/IMG_8993.JPG)

### Whats next...

I have a Raspberry Pi Zero, [HubPiWi](https://www.kickstarter.com/projects/1728237598/hubpiwi-raspberry-pi-zero-hub-with-wifi-no-cable-c), and a USB battery pack. 

![](/content/images/2016/09/IMG_8994.JPG)

I am going to attempt to build a much smaller and truly **walkie**, talkiepi. I will update my blog as I make some progress.

[ 0 Comments ](/i-built-a-wifi-walkie-talkie-for-my-kids-now-you-can-too/#disqus_thread) [ 02 September 2016 ](/i-built-a-wifi-walkie-talkie-for-my-kids-now-you-can-too/)

Share

![Daniel Chote](//www.gravatar.com/avatar/7f04e14567c4ec6ea9c28826cc9e3e12?s=250&d=mm&r=x)

### Daniel Chote

#### 

Daniel Chote, the Code Monkey, Cat Herder, Maker, H4x0r, uav pilot, sim racer, bullshit artist and dad. Made in Hastings, New Zealand... Now living in the USA!

** __  State College, PA **

**__ <http://chote.com>**

### Related Post

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript) [Comments powered by Disqus](http://disqus.com)

## Follow us on Instagram

copyright (C) 2015 SoftHopper. All Rights Reserved..
