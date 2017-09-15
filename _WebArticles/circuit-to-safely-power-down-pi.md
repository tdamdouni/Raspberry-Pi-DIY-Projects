# Circuit to safely power-down Pi

_Captured: 2017-09-06 at 18:46 from [raspberrypi.stackexchange.com](https://raspberrypi.stackexchange.com/questions/5372/circuit-to-safely-power-down-pi)_

I want to use my Pi as an XBMC server in the car. The XBMC docs say that you should always use the [shutdown](http://wiki.xbmc.org/index.php?title=Raspberry_Pi/FAQ#How_to_properly_shutdown.2Fdisconnect) command before disconnecting the power.

I've been thinking that it should be possible to create a simple circuit with a capacitor and probably a diode to detect when the power supply was disconnected (and raise an interrupt on one of the GPIO pins) but the capacitor would provide current long enough for the system to shut down properly.

![first draft](https://i.stack.imgur.com/R23kU.png)

> _Does this look correct and sufficient?_

...Actually, I think it would probably be more like this:

![second draft](https://i.stack.imgur.com/RNh7c.png)

What kind of capacitor would I need to store enough charge to keep the Pi going long enough for XBMC to shut down properly?

For the record, this question was also asked [on SE Electrical Engineering](https://electronics.stackexchange.com/questions/60622/circuit-to-safely-power-down-raspberry-pi).

# [Circuit to safely power-down Pi](/questions/5372/circuit-to-safely-power-down-pi)

I want to use my Pi as an XBMC server in the car. The XBMC docs say that you should always use the [shutdown](http://wiki.xbmc.org/index.php?title=Raspberry_Pi/FAQ#How_to_properly_shutdown.2Fdisconnect) command before disconnecting the power.

I've been thinking that it should be possible to create a simple circuit with a capacitor and probably a diode to detect when the power supply was disconnected (and raise an interrupt on one of the GPIO pins) but the capacitor would provide current long enough for the system to shut down properly.

![first draft](https://i.stack.imgur.com/R23kU.png)

Does this look correct and sufficient? 

...Actually, I think it would probably be more like this:

![second draft](https://i.stack.imgur.com/RNh7c.png)

What kind of capacitor would I need to store enough charge to keep the Pi going long enough for XBMC to shut down properly?

* * *

For the record, this question was also asked [on SE Electrical Engineering](https://electronics.stackexchange.com/questions/60622/circuit-to-safely-power-down-raspberry-pi).

[gpio](/questions/tagged/gpio) [power-supply](/questions/tagged/power-supply) [kodi](/questions/tagged/kodi) [electronics](/questions/tagged/electronics)

![](https://www.gravatar.com/avatar/a007be5a61f6aa8f3e85ae2fc18dd66e?s=32&d=identicon&r=PG)

![](https://www.gravatar.com/avatar/3166c937f1b99e4518fdeccb22d1e5bc?s=32&d=identicon&r=PG)

[Nicholas Albion](/users/6007/nicholas-albion)

What is with the "GPIO 3.3V"? In the first circuit it will just pull down the 3.3V rail with the bottom resistor, and the second connecting the output of an Op-amp running from 5v single-ended supply to GPIO with the inputs as set will have the op-amp driving its output close to 5V as hard as it can - which is not going to help the 3.3V supply to the Pi (**it may kill the Pi**). The use of a Linear Power regulator (7805) is just going to waste the limited charge in the ?? capacitor. I would "-1" this but the question is good even if your suggestions are poor. - [SlySven](/users/36970/slysven) Dec 20 '15 at 19:31

I dont think any kind of capacitor will do as it may take up to 30 seconds to shut down a Pi. You may need to look at a tiny UPS system instead. Or you cant try this, but its a 90USD project. [instructables.com/id/…](http://www.instructables.com/id/The-Forever-Rechargeable-VARIABLE-Super-Capacitor-/) - [ppumkin](/users/894/ppumkin) Dec 20 '15 at 21:03

[ active](/questions/5372/circuit-to-safely-power-down-pi?answertab=active#tab-top) [ oldest](/questions/5372/circuit-to-safely-power-down-pi?answertab=oldest#tab-top) [ votes](/questions/5372/circuit-to-safely-power-down-pi?answertab=votes#tab-top)

Projects to **add shutdown and startup functionality to Pi**:

  * <http://hackaday.com/2013/01/17/raspberry-pi-power-controller-adds-shutdown-and-startup-functionality>
  * <http://www.kickstarter.com/projects/pisupply/pi-supply-intelligent-power-switch-for-raspberry-p>

There is also a solution to **switch Pi on/off but it does not cut the power** so it is not suited for a car:

  * <http://raspi.tv/2012/making-a-reset-switch-for-your-rev-2-raspberry-pi>

[share](/a/5379)|[improve this answer](/posts/5379/edit)

![](https://www.gravatar.com/avatar/596452a0f491324d3012c3d445f2da4e?s=32&d=identicon&r=PG)

[avra](/users/638/avra)

UPDATE: [lowpowerlab.com/atxraspi](http://lowpowerlab.com/atxraspi) - [avra](/users/638/avra) Jan 6 '14 at 16:23

The best solution on my opinion is to use the [UPS Pico](http://www.pimodulescart.com/shop/item.aspx?itemid=5) , a specially designed for Raspberry Pi UPS, that offer a plenty of other features.

It is low cost, includes battery, no need for any extra cable, just put it on top of RPi. 

Running on a car, and automatic shutdown, also running on XBMC.

![](https://www.gravatar.com/avatar/364dbd3a9c5a5062631f78e9a51ce538?s=32&d=identicon&r=PG)

[Alexander](/users/31162/alexander)

Comparator's output goes to GPIO pin (in this circuit there is placed multimeter instead) so that Raspberry could check if car's ignition is still on. Everything else is explained by the previous speaker. "S2" is a reset buttun - just in case. In the picture you can see XMH4, XMM1,.. Don't care about it. I've used it only to check interesting parameters while testing circuit in Multisim. My only question is reaction to rising temperature. Perhaps, there will be need to change the values of resistors in voltage dividers.

Edit: I've realised that in spite of the fact that the cirucit is surely correct in the theory, it is useless. Cost of such a big capacitor (1F, 12V) is unacceptabe high. Another solution might be connecting voltage regulatior stright to acculumator and using voltage comparator between car's ignition and the battery.

![enter image description here](https://i.stack.imgur.com/3zFRp.png)

[share](/a/24910)|[improve this answer](/posts/24910/edit)

[edited Dec 21 '14 at 0:49](/posts/24910/revisions)

answered Dec 9 '14 at 16:32

![](https://www.gravatar.com/avatar/5fa8fc51e607297b2d72a6b2a8aa3cad?s=32&d=identicon&r=PG)

[swojczak](/users/23143/swojczak)

Hello and welcome! Thank you for your contribution. Care to explain the workings of your circuit? - [Ghanima♦](/users/19949/ghanima) Dec 9 '14 at 16:36

It may be possible to design a suitable circuit with a set of "super-capacitors" [batteryuniversity.com](http://batteryuniversity.com/learn/article/whats_the_role_of_the_supercapacitor) article & [Wikipedia](https://en.wikipedia.org/wiki/Supercapacitor) entry and something like what you get from an on-line auction site if your search for a "3V to 5V 1A DC-DC Boost Converter" - you would another (say 5-25V in to 5V 2A(?) output Buck-Boost") converter to drop the 12V (well 13.8V) Car Supply to the 3 to 5 Volts needed to keep the capacitors charged - then the first converter uses that to power the Pi.

You'd want to monitor the incoming 12V to detect it being switched off and to tell the Pi to shut-down (like the UPiS devices in the other answer does!)

You would also need some inrush prevention in the circuit as the super-caps will take a large surge current (from the 12V converter) when voltage is applied to them and they are discharged.

For the record: individual super-caps usually have a maximum voltage of less than 5V but you can now buy units that have two in-series to operate with 5V volts - however it is not a good ideal to put more than 2 or 3 in series without extra "voltage-balancing" circuitry which just make the design more complex - the reason to use a "boost" converter is that it will keep producing 5V when the voltage from the capacitors drops below that...


