# Raspberry Pi Multi-Room Music Player

_Captured: 2017-08-24 at 23:56 from [www.instructables.com](http://www.instructables.com/id/Raspberry-Pi-Multi-Room-Music-Player/)_

![Raspberry Pi Multi-Room Music Player](https://cdn.instructables.com/F7Y/N3UC/I3BH8PS5/F7YN3UCI3BH8PS5.MEDIUM.jpg)

For a long time I have been trying to figure out what I need for a multi-room music set up. Most of the products to buy are a significant cost per room for me considering I all ready have the speakers/amplifiers in place. Spurred on by my children learning about the [Raspberry Pi ](http://www.raspberrypi.org/)at their fantastic Junior School, [St Begh's](http://www.stbeghs.co.uk/) with their teacher Mr Sharkey, I decided to show them that we can build 'stuff' at home that can be just as good (hopefully) as products you can buy in shops.

I looked at existing audio products and costed them up for 4 rooms.

The Pure Jongo A2, now available for £50 each, totals £200\. Whilst it can play high resolution audio, if you want it to stream a music service on its own it uses their own service Pure Connect.

I am already using Spotify on PC, Mobiles and a Smart TV Box, so whatever system I end up with I would like the option to stream Spotify.

The Harman Kardon OMNI Adapt was listed for £100 on their website but looks to have disappeared from it at the point I am writing this and would total £400 for the 4 rooms.

The range that started it all, Sonos, offers the Connect as a means of streaming to existing systems. Priced at £280 this would come to £1,120 in total, an investment. However, it is widely regarded as the best/most useable multi-room system. It can also stream Spotify amongst just about every other service available.

Denon produce the HEOS LINK which looks to me to offer the most adaptability in terms of connections and features and should I come into some money is probably the one I would buy (after I listened to them all!). It is £300 per room so £1,200 for the house and out of my range at the moment.

One step up from this (reportedly) is the Bluesound Node which receives rave reviews and is £400 per room totalling £1,600 for a 4 room set up.

Beyond this you have the likes of Naim Audio and Linn with their in house methods of achieving multi-room music in their high end systems. Looking forward to placing my order after I win the lottery!

So back to the project - put together a 4 room music system to feed my existing equipment, play my music collection from our media server, stream from Spotify and be easy to use and control ........ and sound as good as it can for the target price of £100.

_Digital Music Quality_

If you're just discovering digital music on your computer I would recommend [The Well-Tempered Computer ](http://www.thewelltemperedcomputer.com/)as a place to start, the people at[ Xiph.org ](http://xiph.org/video/)as a place to finish and the forums of [What Hi-Fi ](http://www.whathifi.com/forum)as place to hang around in between. If you do feel you need a voice of experience on all things audio then always read what [Andrew Everard ](http://andreweverard.com/)has to say (alternatively if you need the ultimate gods of audio testing and have a degree in electronics to understand them, then both[ Ken Rockwell ](http://kenrockwell.com/audio/index.htm)and [NwAvGuy](http://spectrum.ieee.org/geek-life/profiles/nwavguy-the-audio-genius-who-vanished) tie closely at the top).

I have done much listening to music on my laptop including a lengthy trial of the new non compressed (16-bit 44.1kHz CD Quality) service Tidal, ripped CD's using various formats and bitrates including lossless. The lower bitrates I can tell the difference, especially if not variable. Once at 320 kbps variable in both mp3 and ogg it gets tricky for me. I think I can tell a very very small difference in some tracks in some places using my headphones but not enough for me to warrant a change up from streaming from Spotify Premium at the moment. Depending on your equipment and/or your ears you may be able to, I have absolutely no problem with that at all. So for this project, for me, as long as the system can distribute up to CD quality audio I'll be happy.

## Step 1: The Plan for the Plan!

![The Plan for the Plan!](https://cdn.instructables.com/F1V/W0UY/I2I3YXDP/F1VW0UYI2I3YXDP.MEDIUM.jpg)

![IMG_0491.JPG](https://cdn.instructables.com/F4Y/XWED/I3BH8JHX/F4YXWEDI3BH8JHX.MEDIUM.jpg)

So first up I tried to explain to the kids what we were trying to come up with, for the most part I think they got it. Our youngest even wanted to draw out a plan. So with a bit of help we end up with the above.

So success for me would be music in the 4 rooms in good quality and in sync and for the kids it would be music that makes you grow a Purple Mohican and say 'Yay' a lot!

I read a lot about the Raspberry Pi and power supplies, the short version is I decided to order a B+ and a supply that everyone says works and supplies enough current for USB devices to be stable. Secondly on the issue of synchronisation I read a lot about clocks and servers and streams and decided to bypass the lot by using a USB DAC that also transmits to its own receiver's. Although this felt a bit like cheating it made the project hardware very simple indeed. Finally I looked through the all the music player software available on the Pi and settled on the one that seemed to have the best USB DAC compatibility - [Pi MusicBox](http://www.woutervanwijk.nl/pimusicbox/).

I came across the [Creative Sound Blaster Wireless Transmitter ](http://uk.creative.com/p/accessories/sound-blaster-wireless-transmitter)(sometimes called Creative Sound Blaster for iTunes Wireless Music Streamer) a while back whilst it was still available from them direct but didn't buy one until I started to look at this project. By then it was discontinued direct but I found some on Amazon, at the time they were slightly cheaper than they are now, so be aware this may cost slightly more than I paid below. Because I found that this was exactly what I was after I stopped looking for alternatives, I think Audioengine do one called the W3 and if you wanted to stream in high resolution you could look to use the D2 but the cost increase is significant. Audio Pro have the WFD200 which I think does the same thing. FiiO, who I have a lot of faith in after owning and loving their D3 DAC and E07K/E09K Desktop DAC and Headphone Amplifier combination, do their Wireless W1 system, though I can't find it for sale in Europe. The [FiiO](http://www.fiio.net/) website is well worth a look for their literal translations from Chinese marketing phrases straight in to English - 'Brings Limitless Splendidness' is how they describe most things. Properly good and good value products though. Maplin do one and I'd guess Lindy will do one, they do most things.

So the parts list for this project is:-

Raspberry Pi B+ Desktop (700MHz Processor, 512MB RAM, 4x USB Port) Amazon £25.60

Raspberry Pi Model B+ Case (OneNineDesign) - WHITE COLOR Amazon £6.25

It has got to look nice as it is on all the time and needs to have a good [WAF](http://en.wikipedia.org/wiki/Wife_acceptance_factor) but your needs may be different, I've seen Supercomputers built of Lego!

The Pi Hut Raspberry Pi UK Micro USB Power Supply Amazon £4.91

Creative Sound Blaster for iTunes Wireless Music Streamer with Wireless Receiver Amazon £29.99

Creative Sound Blaster Wireless Receiver Amazon (x3) £29.97

plus cables to link to your equipment if you don't like the ones that come with the receiver's, and any micro SD cards needed, I had these already.

Total Cost** £96.72**, 'Yay'!

This assumes that you already have a wired Ethernet point available to the Pi where it is going to be used at to provide network and internet access. I haven't gone into the Wi-Fi thing with the Pi but I am sure it is possible.

Order, Pay and Receive.

## Step 2: Assemble the System (Hardware)

![Assemble the System \(Hardware\)](https://cdn.instructables.com/FZB/X5P8/I3BH8JI2/FZBX5P8I3BH8JI2.MEDIUM.jpg)

![IMG_0487.JPG](https://cdn.instructables.com/FPK/U3MT/I3BH8JHT/FPKU3MTI3BH8JHT.SMALL.jpg)

![IMG_0493.JPG](https://cdn.instructables.com/F92/HQQ6/I3BH8JHY/F92HQQ6I3BH8JHY.SMALL.jpg)

![IMG_0495.JPG](https://cdn.instructables.com/FP6/UZL0/I3BH8JI1/FP6UZL0I3BH8JI1.SMALL.jpg)

![IMG_0504.JPG](https://cdn.instructables.com/FQH/PZ8J/I3BH8JIM/FQHPZ8JI3BH8JIM.SMALL.jpg)

This bit I thought would be hard was relatively straight forward.

The Raspberry Pi B+ arrived and was unpacked and fitted in its case within two minutes, no problems. I had decided that I wanted to have the option of moving the USB transmitter around on the surface it was going to live on so I mounted it on a vertical USB extension I had lying around. I have tested it directly in to the Pi and it works just the same. The power supply was plugged in and hidden away, but I stopped short at this point of powering it up. Last thing was to attach the network cable from a router I have in the room it was being used in. Reading on most of the forums the Raspberry Pi works with certain WiFi adapters so if you haven't got a wired Ethernet point handy you can use one of those.

Next up all the receiver's were unpacked and installed in their various locations, they all came with power supplies and cables. The dc power supplies were quite interesting, the UK 3 Pin heads can be mounted either up or down depending on whether you're plugging it in to the left or right of a double socket. I used a mixture of audio RCA cables and 3.5mm stereo jack leads to connect the receiver's to my kit depending on the sockets available. The Creative receiver's come with both types of output connector. I had one into a pair of Creative T20 powered speakers I have in the kitchen. For a cheap set of speakers that allow you to have a true separate stereo sound source these are great. The next one I plugged in to the Yamaha Home Cinema Amplifier in the living room. One was added to my FiiO Headphone Amplifier in the study which also plays through a pair of Focal XS Book powered speakers. Finally one was added to a small Philips docking speaker in the bedroom. All connected and ready to go. Once powered up the green 'connect' switch lights up on the back and the white indicator on each of the units flashes to indicate waiting to receive a signal. Most of the instructions for these assume you're using them with a PC but they seemed to know what they were doing anyway. The software and remote controls supplied were only applicable to PC use so not needed here.

Note: If you use these with your PC just be careful what you actually need to install off the software disk, if you let it get on and do its thing it does try to take over your entire computer (if not the World!) with Creative 'stuff'! I ended up backing out of all of it and just installing the driver only.

So fairly simple so far, Pi waiting for it's operating system with the transmitter plugged in and all the receiver's connected, powered up and raring to go and nobody's hair had turned purple!

## Step 3: Get the OS Up and Running (Software)

![Get the OS Up and Running \(Software\)](https://cdn.instructables.com/FUQ/41VF/I3BH8NAC/FUQ41VFI3BH8NAC.MEDIUM.jpg)

So a bit of internetting and 3 music players seemed to stand out for what I needed the Pi to do, what I hadn't realised was that they came with extra features and full, almost fool proof, instructions. The players I looked at were; [RuneAudio](http://www.runeaudio.com/), [Volumio](http://volumio.org/) and [Pi MusicBox](http://www.woutervanwijk.nl/pimusicbox/). When we drew up the plan we thought we were going to go with RuneAudio, however we ended up settling with Pi MusicBox. They all do roughly the same thing, but in different ways and look quite different when you use them so I would suggest once you've mastered how to get you Pi up and running with them, find which one works and looks best for you.

The extra features I didn't know I wanted were Internet Radio and Airplay. We haven't had a radio playing in our house for a long while, but even as I'm typing this the Pi is playing Absolute 80's (yep, living in the past) around the house. Airplay (or its implementation through Shairport) is still a bit hit and miss at the moment and I'm reading lots of forums in the hope of solving a little bit of dropout we are getting.

So the principle is simple and instruction detailed on each of the websites so I won't repeat them here, but in explaining them to the kids I got to the following summary.

The Pi itself is just a bit of hardware, a computer on its own won't do anything. So it needs an Operating System to tell it how to work and a programme (or application in todays language!) to tell it what to do. In the case of these audio players you get all that rolled in to one and downloaded on to a MicroSD card. The card is then installed in the Raspberry Pi and when it's powered on loads up and starts working. You don't need to connect the Pi to a monitor at all. All three software distributions allow you to use a standard internet browser on anything you've got connected on your network and point it at the Pi to control the software and alter the settings. This is really cool.

So we downloaded the file, unzipped it, put it on the MicroSD card (a full size SD adapter was invaluable here to insert in the laptop) put the card in the Raspberry Pi and plugged in the power.

..............the red (on the B+ Pi) power LED came on and the green activity LED burst into action. After a while we logged on to http://musicbox.local (it'll be different for each player) as directed and up comes the interface. I can't believe the time and effort people put into making stuff this good, they all look awesome. So far so good. Then it was just a case of sorting the settings. I selected the right USB audio device to be used, and put in my Spotify details and the share address of my media server and we were up and running. Wow that was easy.

The LED's on the USB transmitter had come on when the Pi powered up, blue LED for power and the green one to say it had connected to it's receiver's. Each of the receiver's now had a solid white light and when checked were playing music. Job done. Quality, more than acceptable. Cost, bang on. Usability, far more than I ever expected.

![Turn on - Tune in - Drop Out](https://cdn.instructables.com/FLM/SCYJ/I3BH8OJ1/FLMSCYJI3BH8OJ1.MEDIUM.jpg)
