# Circuit to safely power-down Raspberry Pi

_Captured: 2017-09-01 at 19:29 from [electronics.stackexchange.com](https://electronics.stackexchange.com/questions/60622/circuit-to-safely-power-down-raspberry-pi)_

I want to use a Raspberry Pi as an XBMC server in the car. The XBMC docs say that you should always use the [shutdown](http://wiki.xbmc.org/index.php?title=Raspberry_Pi/FAQ#How_to_properly_sh) command before disconnecting the power. I don't want to have to (tell my wife to) log into the Pi and shut it down before turning the car off - I want to be able to

I've been thinking that it should be possible to create a simple circuit with a capacitor and probably a diode to detect when the power supply was disconnected (and raise an interrupt on one of the GPIO pins) but the capacitor would provide current long enough for the system to shut down properly.

Does this look correct and sufficient?

![second draft](https://i.stack.imgur.com/RNh7c.png)

The circuit will be powered by a car battery - 12.6 to 11.7V. The Raspberry Pi takes 5V (5.25 to 4.75V) and draws 700-1200mA. I haven't timed it yet, but I'm guessing the shut-down process probably takes around 5 seconds.

So I suppose what I need to know is:

  * What kind of capacitor would I need to store enough charge to keep the Pi going long enough for XBMC to shut down properly?

  * Given that the Rasperry Pi's GPIO port takes 3.3V, what's the best comparator/op-amp to use (I suppose I could use a couple of resistors to bring the output down from 5 to 3.3)

  * Would there be any benefit in having the GPIO line normally high or normally low?
