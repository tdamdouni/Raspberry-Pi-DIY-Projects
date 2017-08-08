# Pirate Radio Pi Zero W Project Kit review

_Captured: 2017-05-20 at 10:07 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/pirate-radio-kit-review/)_

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/03/pirateradio-square.jpg)

One of the most expensive of the new [Raspberry Pi Zero W project kits](https://shop.pimoroni.com/collections/kits) from Pimoroni, the [Pirate Radio](https://shop.pimoroni.com/collections/kits/products/pirate-radio-pi-zero-w-project-kit) comprises a case full of quality components - everything you need to build your own internet radio. As with the other three kits, the packaging is top-notch and the hinged plastic case can be reused to store other components after the build.

The key electronic items featured in the Pirate Radio kit are a Pi Zero W, with built-in wireless LAN and Bluetooth, and one of Pimoroni's new pHAT BEATs. Also available separately, the latter is a neat bit of kit that crams dual I2S DAC/amplifiers onto a Pi Zero-sized board, and can pump out 3W per channel.

The body of the radio is fairly easy to assemble - from acrylic pieces, legs, retainers, nuts and bolts - using the illustrated [step-by-step online guide](https://learn.pimoroni.com/tutorial/sandyj/assembling-pirate-radio). As long as you follow the guide carefully to get the orientation right, everything slots together neatly. The acrylic pieces are all laser cut, including a neat speaker grille, so there are no nasty rough edges.

The supplied 5W speaker simply slots onto four bolts holding the translucent front acrylic layer in place. Fortunately, the speaker comes with a length of dual wire already connected, so there's no need to solder it. We're not sure why the wire is much longer than required, though; while you could always cut it to size, we just wound it round the bolts at the rear of the radio.

Unless you opt to buy a couple of Pimoroni's ingenious hammer headers separately, you will need to break out the soldering iron to attach the supplied standard male and female headers to the Pi Zero W and pHAT BEAT. The latter then slots onto more bolts at the rear of the radio, with the Zero W mounted on top. The speaker wires are inserted into a couple of the terminal blocks on the pHAT BEAT, with the latter's dip switch set to mono to combine its stereo channels. With that, your internet radio is built!

### Streaming software

The Pi Zero W's built-in wireless connectivity means there's no need to use a WiFi dongle plugged into a USB to micro-USB adapter, which makes for a more streamlined look to the radio. Even so, such an adapter is included in the kit, along with an HDMI adapter. This is presumably to enable you to hook the Zero W up to the monitor to install the software in Raspbian and set up WiFi, although we went the instant headless route by adding ssh and wpa_supplicant.conf (with our router details) files to the microSD card before first boot.

On the software side, Pimoroni has put together guides for three project examples. The first is for an internet radio based on the VLC daemon. As with the other examples, a single command is used to install all the required packages. You can then edit the playlist file to add URLs for your favourite radio stations. With this particular project, everything can be controlled via the pHAT BEAT's five side-mounted buttons: forward/back to select stations, pause/play audio, and volume up/down. The only slight downside is that the buttons are tiny, and a little difficult to locate on the side of the radio at times. The sound quality is good, however, with a decent amount of volume. Its real-time volume level is shown dynamically by the pHAT BEAT's super-bright LED VU meter.

In addition, we followed Pimoroni's tutorial to turn the Pirate Radio into an AirPlay speaker for streaming audio from an iPhone and iPad. Both this and the VLC radio work alongside each other happily, so you can switch from one use to the other. Highlighting the radio's versatility, Pimoroni has also put together a Spotify streaming project using Modipy, controllable from a remote computer or device.

### Last word

5/5

While it's a slight shame that it doesn't make use of the pHAT BEAT's stereo capabilities, this is an excellent kit that is easy to assemble and results in a genuinely useful audio device with good sound quality. As well as internet radio and music streaming, potential uses include an Alexa-style voice assistant (with the addition of a USB mic), a speaker for musical HATs, and a speaking clock.
