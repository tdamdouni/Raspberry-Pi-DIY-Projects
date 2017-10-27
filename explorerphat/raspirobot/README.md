# raspirobot
Scripts to control a raspberry pi robot using Pimoroni's Explorer hat.

Here's my setup for the barebones robot:

* [Raspberry Pi Zero W](https://shop.pimoroni.com/products/raspberry-pi-zero-w)
* [Explorer pHat](https://shop.pimoroni.com/products/explorer-phat)
[Polulu Zumo robot chassis](https://shop.pimoroni.com/products/zumo-chassis-kit-no-motors)
* 2x [Micro Metal Gearmotor](https://shop.pimoroni.com/products/micro-metal-gearmotor-extended-back-shaft) (I went for 298:1 to start with)
* An old usb battery pack

Connect all this lot up (there's a ton of info about. It's dead easy), then connect your Pi Zero W up to a monitor and mouse/keyboard just to get it onto your WiFi network.

When it's on the network, you can unplug everything and run the Pi headless.

Next use ssh to connect to your Pi, copy this project script across, [install the Explorer library](https://github.com/pimoroni/explorer-hat) then run the script!

You can control the robot through ssh using the WASD keys. Space halts the robot, and Q exits the script cleanly.

If you keep getting weird behaviour when you start the script try shutting everything down and starting again.