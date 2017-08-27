# Raspberry Pi Wearable Time Lapse Camera

_Captured: 2017-08-27 at 13:27 from [learn.adafruit.com](https://learn.adafruit.com/raspberry-pi-wearable-time-lapse-camera?view=all)_

![camera_hero-lanyard.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/249/large1024/camera_hero-lanyard.jpg?1466541077)

Worn on a lanyard or clipped to a pocket or pack, this adorable camera snaps a photo every few seconds. Slide the SD card into your computer to review the day's activities or merge all the images into a timelapse animation.

Powered by the diminutive and affordable Raspberry Pi Zero, this DIY project is eminently configurable and customizable!

![camera_parts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/069/large1024/camera_parts.jpg?1466383794)

> _Parts and Tools Required_

**The "canonical" build in this guide is illustrated with the following parts:**

  * Soldering iron, wire and related paraphernalia
  * 3D printer and filament
  * Craft glue such as E6000 or Krazy Glue®.

The first three listed items are available in packs with either a [regular](https://www.adafruit.com/products/3170) or [infrared](https://www.adafruit.com/products/3171) camera.

The example software will run on _any_ Raspberry Pi computer. Since Pi Zero supplies are constrained…or if you just want to use a different board or battery, or create your own enclosure in another medium…you might instead consider:

  * [Raspberry Pi Model A+](https://www.adafruit.com/products/2266) (_any_ Pi can work, but most are bulkier and draw more power)
  * All but the Pi Zero can use the standard flex cable already included with the camera. [Custom cables for novel form-factors are optional](https://www.adafruit.com/products/2087).
  * You can skip the PowerBoost and power the Pi directly from a [USB phone charger battery](https://www.adafruit.com/products/1565).
  * For the LED sequin, you can substitute a regular through-hole LED (any color) and resistor (75 to 500 Ohm).
  * Likewise, most any pushbutton or switch can be substituted if you're not using the 3D-printed case.

The **500 mAh** battery is good for about **2 hours** run time. If you want to keep it going all day, you could design an enclosure around a larger battery…or simply **plug the PowerBoost into a USB phone charger** to greatly extend its life!

You may need some additional parts depending on the installation procedure used (perhaps a USB flash card reader, or a second Raspberry Pi during setup, etc.). **Read through the whole guide and check your parts stash before making any purchasing decisions.**

![camera_hero-tripod.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/250/large1024/camera_hero-tripod.jpg?1466541090)

![camera_hero-face.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/251/large1024/camera_hero-face.jpg?1466541105)

![camera_hero-pocket.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/252/large1024/camera_hero-pocket.jpg?1466541228)

![camera_3d-parts.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/067/large1024/camera_3d-parts.jpg?1466383687)

![camera_switch-wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/144/medium640/camera_switch-wires.jpg?1466512746)

![camera_LED-wires-\(70mm\).jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/146/medium640/camera_LED-wires-%2870mm%29.jpg?1466512835)

![camera_button-wires.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/149/medium640/camera_button-wires.jpg?1466512906)

![camera_pb-pi-wires-\(80mm\).jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/155/medium640/camera_pb-pi-wires-%2880mm%29.jpg?1466513120)

![camera_pb-switch-wired.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/154/medium640/camera_pb-switch-wired.jpg?1466513033)

![camera_pb-pi-wires-soldred.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/156/medium640/camera_pb-pi-wires-soldred.jpg?1466513195)

![camera_GPIO-Diagram.png](https://cdn-learn.adafruit.com/assets/assets/000/033/435/large1024/camera_GPIO-Diagram.png?1467093851)

![camera_LED-wired-pi.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/159/medium640/camera_LED-wired-pi.jpg?1466513543)

![camera_3170-00.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/436/medium640/camera_3170-00.jpg?1467095232)

![camera_test-circuit.jpg](https://cdn-learn.adafruit.com/assets/assets/000/033/160/large1024/camera_test-circuit.jpg?1466513646)
