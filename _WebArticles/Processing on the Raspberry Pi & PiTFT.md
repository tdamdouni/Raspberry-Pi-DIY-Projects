# Processing on the Raspberry Pi & PiTFT

_Captured: 2015-11-16 at 10:12 from [learn.adafruit.com](https://learn.adafruit.com/processing-on-the-raspberry-pi-and-pitft?view=all)_

This project will show you how to install and use the [Processing programming environment](https://processing.org/) on a Raspberry Pi and PiTFT. Processing is a fantastic tool to create visual programs, and its latest Processing 3.0 release now has support for the Raspberry Pi. With Processing you can create beautiful artwork, prototype interfaces, and much more without having to be an expert programmer. In fact Processing is targeted at artists, students, makers, and anyone who's new to programming.

One cool new feature in Processing 3.0 is support for controlling hardware. This allows you to add interesting new interactivity to your Processing sketches and even prototype hardware interfaces with ease. On a Raspberry Pi you can control the GPIO (general purpose input/output) pins and do things like blink LEDs, read buttons and much more. For example you can create a sketch that turns on or off LEDs by touching a block on the screen:

[ ![raspberry_pi_IMG_4174.jpg](https://learn.adafruit.com/system/assets/assets/000/028/541/medium800/raspberry_pi_IMG_4174.jpg?1447317397) ](https://learn.adafruit.com/assets/28541)

One thing to keep in mind with Processing on the Raspberry Pi is that the Pi hardware is not as fast as a desktop or laptop computer. This means complex Processing sketches with fast animations or processor intensive calculations might not work on the Pi. Keep your sketches simple, like drawing 2D shapes or creating basic user interfaces.

To follow this guide you'll want to somewhat familiar with Processing. Check out the [great tutorials on getting started with Processing](https://processing.org/tutorials/) if you're completely new to using it. It will also help to check out this [introduction to Processing 3.0](https://vimeo.com/140600280) so you can learn about its new features.

You'll also want be familiar with using the Raspberry Pi, like how to load an operating system on it and connect to its command line terminal. Check out [this great series of Raspberry Pi learn guides](https://learn.adafruit.com/../../../../series/learn-raspberry-pi) if you're new to using it.

Continue on to learn about the hardware used in this project.

[ ![raspberry_pi_IMG_4179.jpg](https://learn.adafruit.com/system/assets/assets/000/028/540/medium800/raspberry_pi_IMG_4179.jpg?1447317348) ](https://learn.adafruit.com/assets/28540)

[ ![raspberry_pi_Selection_001.png](https://learn.adafruit.com/system/assets/assets/000/028/574/medium800/raspberry_pi_Selection_001.png?1447376736) ](https://learn.adafruit.com/assets/28574)

> _(if you're curious the ARMv6hf name stands for the ARMv6 architecture with a hardware floating point unit, i.e. the architecture of the Raspberry Pi)_

[ ![raspberry_pi_Screenshot_from_2015-11-12_17_42_14.png](https://learn.adafruit.com/system/assets/assets/000/028/575/medium800/raspberry_pi_Screenshot_from_2015-11-12_17_42_14.png?1447379015) ](https://learn.adafruit.com/assets/28575)

> _Now you can use Processing just like using it on your computer. Type in or load a sketch, click the run button, and watch your sketch execute on the Raspberry Pi._

[ ![raspberry_pi_Screenshot_from_2015-11-12_18_28_21.png](https://learn.adafruit.com/system/assets/assets/000/028/576/medium800/raspberry_pi_Screenshot_from_2015-11-12_18_28_21.png?1447381857) ](https://learn.adafruit.com/assets/28576)

[ ![raspberry_pi_Screenshot_from_2015-11-13_00_05_55.png](https://learn.adafruit.com/system/assets/assets/000/028/580/medium800/raspberry_pi_Screenshot_from_2015-11-13_00_05_55.png?1447401970) ](https://learn.adafruit.com/assets/28580)

> _Then save the file by pressing Ctrl-o then enter, and then Ctrl-x. Reboot the Pi and the change should take affect and prevent the monitor or PiTFT from turning off._

[ ![raspberry_pi_IMG_4177.jpg](https://learn.adafruit.com/system/assets/assets/000/028/581/medium800/raspberry_pi_IMG_4177.jpg?1447402444) ](https://learn.adafruit.com/assets/28581)

[ ![raspberry_pi_IMG_4170.jpg](https://learn.adafruit.com/system/assets/assets/000/028/583/medium800/raspberry_pi_IMG_4170.jpg?1447402617) ](https://learn.adafruit.com/assets/28583)

> _Press a box to turn on or off the LED (the left box controls the red LED and the right box controls the green LED):_

[ ![raspberry_pi_IMG_4174.jpg](https://learn.adafruit.com/system/assets/assets/000/028/584/medium800/raspberry_pi_IMG_4174.jpg?1447402661) ](https://learn.adafruit.com/assets/28584)

> _And press the momentary button to change the screen color to blue while it's pressed:_

[ ![raspberry_pi_IMG_4176.jpg](https://learn.adafruit.com/system/assets/assets/000/028/585/medium800/raspberry_pi_IMG_4176.jpg?1447402709) ](https://learn.adafruit.com/assets/28585)
