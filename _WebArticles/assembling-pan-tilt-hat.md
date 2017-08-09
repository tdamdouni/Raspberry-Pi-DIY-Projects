# Assembling Pan-Tilt HAT

_Captured: 2017-05-10 at 22:38 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/assembling-pan-tilt-hat)_

This short tutorial will guide you through the assembly of your Pan-Tilt HAT. We'll go through attaching the pan-tilt module, connecting the servos to the board, mounting the camera, and the optional use of an Adafruit Neopixel stick for lighting.

The board has four holes to mount the pan-tilt module, a slot to route the servo cables and camera cable through the PCB, and pins on the bottom to which the servos and light connect.

![Pan-tilt HAT top](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-1.jpg)

![Pan-tilt HAT bottom](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-2.jpg)

## Attaching the pan-tilt module

The pan-tilt module attaches to the top of the PCB with the four black nylon M2 bolts and nuts. First push the nuts through from the top of the base of the pan-tilt module, then push the nuts through the four holes on the PCB.

It's best to orient the module so that the head can rotate around the left edge of the PCB, as it is in the picture below.

Use the nuts to attach everything securely underneath the PCB. It's a good idea to trim the protruding end of the nylon bolt with a pair of scissors or tin snips, so that the board can sit flush with the top of your Pi, or alternatively push the bolts through from the bottom instead and secure on top.

![Pan-tilt module](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-3.jpg)

## Connecting the servos

Route the two servo cables through the slot on the top of the PCB where it says "SERVO CABLES". Underneath, connect the two sets of wires up with the brown wires connected to the ground pins,a s in the picture below.

We connected the pan servo (that moves horizontally) to servo channel 1, and the tilt servo (that moves vertically) to servo channel 2, but they can easily be swapped in software later.

You can use a couple of small cable ties, if you wish, to neaten up the servo cables by attaching them to the plastic frame of the pan-tilt module, but remember to leave enough slack to let the servos move freely.

![Servo wires connection](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-4.jpg)

## Attaching the camera

The camera comes with an acrylic mounting plate, consisting of two black pieces, that screws to your Raspberry Pi camera module with two of the included white nylon M2 bolts and nuts.

![Camera mount](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-5.jpg)

> _The piece with the t-shaped hole goes directly on top of the front face of the camera module with the camera cable protruding from the top edge of the mount (the one with the more rounded corners)._

![Camera mount first piece](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-6.jpg)

> _Place the other plastic piece on top, and then use two of the white nylon bolts and nuts to secure everything._

Again, it's a good idea to trim off the excess nylon bolt with a pair of scissors or tin snips.

![Camera mount second piece](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-7.jpg)

> _Your camera and mount should now clip into the head of the pan-tilt module. Make sure that the cable protrudes from the top (the curves on the mount should match the curves on the head of the pan-tilt module)._

![Camera mounted](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-8.jpg)

> _Route the camera cable through the slot on the PCB marked "CAM CABLE", and then connect it to the camera connector on your Pi._

If you're not using the optional Neopixel stick, then you're done! If you want to use the Neopixel stick, then read on!

## Soldering and mounting a Neopixel stick

You can use one of the 8 pixel Adafruit Neopixel sticks (we like the RGBW ones) to act as a light source for your pan-tilt-mounted camera. We've even provided a little frosted acrylic diffuser to diffuse the light nicely and mounting holes on the camera mount to attach it.

We'd recommend soldering a piece of male header to the pads on the rear of the Neopixel stick, allowing you to use some female-female jumper jerky to connect the stick to the pins on bottom of Pan-Tilt HAT.

![Neopixel pins](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-9.jpg)

The acrylic diffuser fits on top of the Neopixel stick with the two remaining white nylon M2 bolts and nuts. Push the bolts through the diffuser and Neopixel stick, and then through the two holes towards the top of the camera mount, using the nuts to secure the stick and diffuser to the camera mount. The pins should protrude from the right hand side as you look at the front of the camera mount.

![Neopixel diffuser bolts](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-10.jpg)

![Neopixel diffuser mounted](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-11.jpg)

> _Use three pieces of female-female jumper jerky to connect the 5VDC, GND, DIN pins on the Neopixel stick to the 5V, GND, and DATA pins respectively on Pan-Tilt HAT._

![Neopixel stick connected](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-12.jpg)

> _Congratulations! Your Pan-Tilt HAT assembly is complete! Pop it onto the GPIO pins on your Pi, install our Pan-Tilt HAT Python library, and away you go!_

If you're using Pan-Tilt HAT with your Pi in a Pibow Coupe case, then it should sit neatly on top of the Coupe case, but if you're not then it's a good idea to grab [a couple of metal standoffs](https://shop.pimoroni.com/products/brass-m2-5-standoffs-for-pi-hats-black-plated-pack-of-2) and [a couple of nylon M2.5 bolts](https://shop.pimoroni.com/products/pibow-extender-bolt-pack) to hold everything steady.

![Pan-tilt complete](https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-hat-14.jpg)
