# 7” Portable Multitouch Raspberry Pi Tablet

_Captured: 2015-10-24 at 00:39 from [learn.adafruit.com](https://learn.adafruit.com/7-portable-raspberry-pi-multitouch-tablet?view=all)_

In this project, we'll show you how to build a portable Raspberry Pi 2, using a 7" capacitive multitouch display, an Adafruit PowerBoost 1000C and a 2500mAh battery. Our 3D printed enclosure fits all of the components making an all-in-one, compact Raspberry Pi tablet.

In this build, we're using the official 7" multitouch display from the Raspberry Pi foundation. It features a beautiful IPS display and includes the drivers to work on a Raspberry Pi 2.

The 3D printed enclosure gives you access to all of the ports. Instead of stacking all of the boards on top of each other, this design allow the components to be spread out, making a slim package.

[ ![hacks_parts.jpg](https://learn.adafruit.com/system/assets/assets/000/028/088/medium800/hacks_parts.jpg?1445266345) ](https://learn.adafruit.com/assets/28088)

Below is a list of parts used in this project. You can optionally choose to make it portable by including an Adafruit PowerBoost 1000c and a 2500mAh lithium polymer battery. You will also need some hardware screws to mount the components to the enclosure.

Here's a list of tool used to get this project completed. If you don't have access to a 3D printer, you can send your parts to [3DHubs.com](https://learn.adafruit.com/3dhubs.com) to have them printed and shipped to you.

[ ![hacks_hero-ports.jpg](https://learn.adafruit.com/system/assets/assets/000/028/110/medium800/hacks_hero-ports.jpg?1445280871) ](https://learn.adafruit.com/assets/28110)

[ ![hacks_3d-parts.jpg](https://learn.adafruit.com/system/assets/assets/000/028/089/medium800/hacks_3d-parts.jpg?1445266365) ](https://learn.adafruit.com/assets/28089)

7inTouchCase.stl

7inTouchLid.stl

7inTouchFrame.stl

7inTouchBat.stl

230c Extruder

2mm Retraction

10% infill

2 Shells

60mm/s print speed

90mm/s travel speed

about 6 hours to print all parts.

The parts were tested with common printing settings (listed in the table). With a parameter of 2 shells, theres only a few areas where tolerances really matters - the port cutouts and the mounting holes.

Test fit the parts by inserting the top enclosure part over the Raspberry Pi. Check to see if the cutouts fit over the USB and ethernet ports. If the cutout is too tight, you can loosen it with a filing tool.

The standoffs with counter bores should fit the machine screws listed in the BOM. These can be threaded by fastening in the appropriate sized screw.

[ ![hacks_circuit-diagram.jpg](https://learn.adafruit.com/system/assets/assets/000/028/112/medium800/hacks_circuit-diagram.jpg?1445287882) ](https://learn.adafruit.com/assets/28112)

**PowerBoost1000C**

The slide switchs connect to the **EN** and **GND** pins the Adafruit PowerBoost1000C.

The 2500mAh batteries plugs into the **JST** connector on the PowerBoost1000C. You can charge the battery by connecting a microUSB cable.

**Raspberry Pi 2:**

**Positive+** and **-Negative** pins on the PowerBoost1000C connect to the Pi on **GPIO #2** for **5V power **and** GPIO # 6** for ground.

**Display Driver:**

**+Positive** and **-Negative** pins on the Driver Board connect from **5V** and **GND** labeled on the Display Driver to the Pi on GPIO pins **#4** for **Power** and **#9** for **Ground**

[ ![hacks_attch-frame-1.jpg](https://learn.adafruit.com/system/assets/assets/000/028/090/medium800/hacks_attch-frame-1.jpg?1445266408) ](https://learn.adafruit.com/assets/28090)

[ ![hacks_board-frame-screw-in.jpg](https://learn.adafruit.com/system/assets/assets/000/028/091/medium800/hacks_board-frame-screw-in.jpg?1445266450) ](https://learn.adafruit.com/assets/28091)

[ ![hacks_driver-solder.jpg](https://learn.adafruit.com/system/assets/assets/000/028/095/medium800/hacks_driver-solder.jpg?1445266782) ](https://learn.adafruit.com/assets/28095)

[ ![hacks_driver-attach-1.jpg](https://learn.adafruit.com/system/assets/assets/000/028/092/medium800/hacks_driver-attach-1.jpg?1445266707) ](https://learn.adafruit.com/assets/28092)

[ ![hacks_driver-attach-2.jpg](https://learn.adafruit.com/system/assets/assets/000/028/093/medium800/hacks_driver-attach-2.jpg?1445266727) ](https://learn.adafruit.com/assets/28093)

[ ![hacks_driver-screw-in.jpg](https://learn.adafruit.com/system/assets/assets/000/028/094/medium800/hacks_driver-screw-in.jpg?1445266754) ](https://learn.adafruit.com/assets/28094)

[ ![hacks_powerboost-soldered.jpg](https://learn.adafruit.com/system/assets/assets/000/028/096/medium800/hacks_powerboost-soldered.jpg?1445266845) ](https://learn.adafruit.com/assets/28096)

Cut one of the leads from the slide switch (far left or right, not middle). We only need two leads.

Secure the slide switch to a set of helping third hands.Tin the two leads by adding a bit of solder.

Measure and cut two 26AWG silicone coated stranded wires. Strip and tin tips of each wire.

Solder wires to the leads on the slide switch

Solder one wire from slide switch to **EN** pin, and the other to **GND** on the Adafruit PowerBoost 1000C.

Measure and cut another set of 26AWG silicone coated wires. Strip and tin the tips of the wires. Solder one to the positive pin and the other to the negative labled pin on the PowerBoost 1000C.

[ ![hacks_powerboost-screw-in.jpg](https://learn.adafruit.com/system/assets/assets/000/028/097/medium800/hacks_powerboost-screw-in.jpg?1445266862) ](https://learn.adafruit.com/assets/28097)

[ ![hacks_pi-screw-in.jpg](https://learn.adafruit.com/system/assets/assets/000/028/098/medium800/hacks_pi-screw-in.jpg?1445266971) ](https://learn.adafruit.com/assets/28098)

[ ![hacks_battery-position-for-mounting.jpg](https://learn.adafruit.com/system/assets/assets/000/028/100/medium800/hacks_battery-position-for-mounting.jpg?1445267188) ](https://learn.adafruit.com/assets/28100)

[ ![hacks_battery-zipped.jpg](https://learn.adafruit.com/system/assets/assets/000/028/101/medium800/hacks_battery-zipped.jpg?1445267214) ](https://learn.adafruit.com/assets/28101)

[ ![hacks_battery-attach.jpg](https://learn.adafruit.com/system/assets/assets/000/028/102/medium800/hacks_battery-attach.jpg?1445267249) ](https://learn.adafruit.com/assets/28102)

[ ![hacks_solder-pins-to-pi.jpg](https://learn.adafruit.com/system/assets/assets/000/028/099/medium800/hacks_solder-pins-to-pi.jpg?1445267146) ](https://learn.adafruit.com/assets/28099)

[ ![hacks_connect-display-cable.jpg](https://learn.adafruit.com/system/assets/assets/000/028/103/medium800/hacks_connect-display-cable.jpg?1445267323) ](https://learn.adafruit.com/assets/28103)

[ ![hacks_slide-switch-insert.jpg](https://learn.adafruit.com/system/assets/assets/000/028/109/medium800/hacks_slide-switch-insert.jpg?1445267557) ](https://learn.adafruit.com/assets/28109)

Insert the slide switch into the cutout on the enclosure casing.

If the slide switch doesn't fit into the cutout, use a hobby knife to remove some material from the cutout to widen it.

You can use a pair of flat pliers to insert the slide switch through the cutout.

Don't force the slide switch all the way through, just enough to protrude half way through the port.

If the slide switch is loose, use hotglue or E6000 to permanently secure it in place.

[ ![hacks_lid-align.jpg](https://learn.adafruit.com/system/assets/assets/000/028/105/medium800/hacks_lid-align.jpg?1445267409) ](https://learn.adafruit.com/assets/28105)

[ ![hacks_lid-screw.jpg](https://learn.adafruit.com/system/assets/assets/000/028/106/medium800/hacks_lid-screw.jpg?1445267427) ](https://learn.adafruit.com/assets/28106)

[ ![hacks_remove-film.jpg](https://learn.adafruit.com/system/assets/assets/000/028/107/medium800/hacks_remove-film.jpg?1445267478) ](https://learn.adafruit.com/assets/28107)

[ ![hacks_hero-ports.jpg](https://learn.adafruit.com/system/assets/assets/000/028/108/medium800/hacks_hero-ports.jpg?1445267533) ](https://learn.adafruit.com/assets/28108)
