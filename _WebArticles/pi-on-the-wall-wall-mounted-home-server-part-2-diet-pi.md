# Pi On The Wall – wall mounted home server – Part 2: Diet Pi

_Captured: 2017-09-12 at 09:23 from [labs.domipheus.com](http://labs.domipheus.com/blog/pi-on-the-wall-wall-mounted-home-server-part-2-diet-pi/)_

_This is Part 2 of a series of blogs regarding the development of a wall-mounted server based on the Raspberry Pi, featuring WiFi and a colour touchscreen. [Part 1 can be found here](http://labs.domipheus.com/blog/pi-on-the-wall-wall-mounted-home-server-part-1-introduction/)._

![case_dims](http://labs.domipheus.com/blog/wp-content/uploads/2014/06/case_dims.jpg)

The enclosure I'm using, a re-purposed room thermostat casing, places some very tight constraints on the dimensions of the Raspberry Pi and [PiTFT](http://www.amazon.co.uk/gp/product/B00H9B1DTA/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00H9B1DTA&linkCode=as2&tag=sorryaboutthe-21) board.The plastic used in the case is quite sturdy, and is at least 2mm in thickness. Therefore the real inner depth of the case is about 12mm. As for the width of the Pi, we need to shave at least 4mm from the side. The Pi itself is 86mm wide, same with the [PiTFT](http://www.amazon.co.uk/gp/product/B00H9B1DTA/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00H9B1DTA&linkCode=as2&tag=sorryaboutthe-21) board, so we will need to find a way of making it closer to 82mm.

![pitft](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pitft.jpg)

The board interconnect that comes with the PiTFT is a tall terminal connector. It is immediately ruled out for use, as it increases the depth of the assembly to well over an inch. Without using that, and bending the pins to grip the I/O on the PiTFT, the depth from SD card housing to top of the TFT is just over 20mm. Still far too much.

![pi_ident](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_ident.jpg)

The main space-wasters on the Pi are easy to identify. The composite out, audio out, USB, HDMI, and the camera and display interfaces all can be removed. The tallest of these, the Composite out, measures over 11mm alone. The only one we need to use is USB, and we can add terminals to enable an off-board connector for that. All the others need to go.

![pi_components](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_components.jpg)

The composite, audio and USB jacks were relatively easy to remove. Solder sucker & solder wick with some wiggling did the trick. The HDMI socket was another matter entirely. There were some components near the socket I didn't want to destroy, and one of the soldered through-hole supports wouldn't budge. Butchery was resorted to, using cutters to chip away at the metal surround and later the plastic. The connector itself is surface mount, and came off fairly easily after that. Once destroyed, the through hole-support gave in and came out with more wiggling. I apologise to all who were involved in designing the Pi for the following image.

![pi_nohdmi](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_nohdmi.jpg)

Some PCB pads came off at the HDMI socket, but I was not concerned, as this was destructive change anyway. The camera and display interface connectors I simply cut away with pliers, again, a few pads came off.

![powerschematic](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/powerschematic.jpg)

C6 is the large silver capacitor near the micro usb socket. This is the last item in the way on the top of the board, and as you can see from the Raspberry Pi schematic, is just a smoothing capactor for the power. It can be safely removed and if needed, put off-board in seperate power circuitry. I've identified D17, a protection diode on the opposite side of the PCB, as we will come back to this later. The board ends up incredibly bare and on the top side it's only a few millimeters tall.

![pi_bare](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_bare.jpg)

After this I put a 90 degree set of terminal pins in the USB location so we can put the socket off-board. If we knew everything was going to work at this point the easiest thing to do would be to solder the PiTFT board directly to the GPIO pins of the PI. However, I wanted to remove the Pi from the TFT board to adjust things in future, so had to come up with a solution without using standard terminal connectors, which are too tall. I decided to try taking a DIP socket and using that, as they are only 3mm tall. The first two pins are not required, so sawing a 24-pin socket in half, inverting it for a flush fit and filing down worked exceptionally well.

![interconnect_bodge](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/interconnect_bodge.jpg)

With this the board is just over 14mm from top of the touchscreen to the bottom of the SD card holder.

![interconnect_height](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/interconnect_height.jpg)

The next thing I attempted was to cut around 5mm from the Pi and PiTFT PCBs closest to where the USB port used to be. Around there, especially on the model A, it's sparce.

![Boardlayout_cut](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/Boardlayout_cut.jpg)

![raspberry_pi_pitftdiagram](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/raspberry_pi_pitftdiagram-e1405117016247.png)

The PiTFT is round the opposite way as the Pi, as you can see, it's simply the adafruit logo mask and there are no important traces to avoid. I just dived right in, marked a line with a stanley knife and got out the hacksaw. After some effort and sanding with a rotary tool it came out pretty well.

![pi_cut](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_cut.jpg)

The PCBs now fit well into the case in terms of width and length, but depth is still a problem. We need to hit 12mm at minimum. The only thing to now do is relocate the SD card socket from the bottom of the board to the space on top where the Display Interface used to be, on top of the logo to the left of the SoC.

![pi_sd_depth_](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_sd_depth_.jpg)

Desoldering the SD card holder was a bit more nasty than I'd imagined. I only have an iron, solder sucker and some wick. Ideally I'd have the correct tools, but for this I resorted to the 'pull enamelled wire through the joint as it is molten' trick, which worked in this case. If you use this method watch out as the pins themselves can come out from the plastic housing very easily.

![wire_sm_desolder](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/wire_sm_desolder.jpg)

After it was removed, I used 0.2mm enamelled copper wire soldered to the existing pads, through the hole in the board to the front side and soldered direct to the holder. It wasn't very well done, I tried to keep the lengths of wire of a similar length but it shouldn't matter too much. The main thing is making sure you have a good clean solder joint and you remove the enamel at the right places. Scraping with side cutters and tinning with too much solder (so much that you waste some) usually does the trick.

![pi_sd](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_sd.jpg)

An interesting thing to note is that the card detect and write protect switches do not seem to have an effect at runtime. The schematic shows the write protect pins are unconnected, so that's expected. The card detect pins are connected to the SoC. My plan was just to short the pads on the underside to save soldering 2 wires that don't really matter. There are two very small SMD components where the SD card holder now sits (C1 & C5), I made tiny holes in the underside plastic of the holder so it can be mounted flush on the PCB without those components being damaged.

Additionally, I removed D17. This protection diode will be mounted off-board when the power system is looked at along with (potentially) C6 that we removed earlier. Note D17 and C6 technically are not needed to run the board, they are for protection, so I can still test via the microUSB socket as in the picture below.

![slim_pi](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/slim_pi.jpg)

At the moment i'm measuring just over 10mm to the end of the terminal pins on the underside of the RPi board. Of course there are some surface mount components also on the back, but they don't change depth much. The D17 diode was the biggest one, and we moved it off-board. I'm going to grind the back of the GPIO pins off a bit just to save some more space, but I think there is no need to go further than 10mm. There is still space between the Pi and PiTFT boards for the USB terminal connector to carry a socket off-board, and also something I'm looking at is heat dissipation from the SoC and whether I need to increase the surface area for some better passive cooling.

**The final dimensions of the unit assembled is 80mm x 56mm x 10.5mm.**

As for the Pi On The Wall project, the next steps are to sort the casing out with the tactile switches matching the switches on the PiTFT, and also affixing the USB socket in the case so a mini USB WiFi stick is flush with the exterior. After that, I'll be running some power consumption tests and heat dissipation tests. I want this to be extremely low power, and will experiment with replacing the regulators, turning off services, possibly even running the whole board off 3.3v instead of 5v, which is said to be possible.

If you have got to this point in the post, I hope you found it interesting. If you have any questions, please either comment here or message me directly on twitter [@domipheus](https://twitter.com/domipheus).

**Update**: Thanks for all the feedback! Here is a taste of things to come in the case fitting:

![pi_casefit](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pi_casefit.jpg)

![pitweet](http://labs.domipheus.com/blog/wp-content/uploads/2014/07/pitweet.jpg)

(used a hub in the usb socket to type for this shot, obviously the idea is once done I'll make some specialized frontend so that's not needed, and all config done over ssh)

[All pictures of the build and more can be seen here on Flickr.](https://www.flickr.com/photos/domipheus/sets/72157645380717811/)
