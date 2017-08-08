# Pirate Radio

_Captured: 2017-05-23 at 18:58 from [bigl.es](http://bigl.es/pirate-radio/)_

For Friday Fun this week I sat down with another of Pimoroni's Pi Zero W powered project kits.

_This kit was won in a competition on Pimoroni's Bilge Tank Youtube channel, but as always this post will be impartial and show the good and bad points in a constructive manner_

_I won it on this video...yay! (14min 14sec onwards)_

Earlier this week I had great fun [building the Mood Light kit](http://www.bigl.es/im-in-the-mood-for-hacking/) but I really wanted to save the Pirate Radio kit for Friday Fun!

![alt](https://farm4.staticflickr.com/3892/33358220365_f536ab190e_z_d.jpg)

Retailing at £40 this is the [most expensive of the kits](https://shop.pimoroni.com/products/pirate-radio-pi-zero-w-project-kit) offered by Pimoroni but it comes with some great quality components.

![alt](https://farm3.staticflickr.com/2927/33202918032_5505307d7a_z_d.jpg)

  * Raspberry Pi Zero W
  * PHAT BEAT DAC 
    * APA102 Based LEDS to visualise the beat of your music
    * I2S based stereo DAC
    * Lovely clips to hold the speaker wire
    * Six buttons to control the music volume, skip tracks, pause and power off
  * Header pins
  * 5W Speaker
  * Laser cut pieces to build the radio
  * USB lead
  * Mini HDMI to HDMI adaptor

## Building the kit

![alt](https://farm4.staticflickr.com/3826/32975635970_8d5fbe2a42_z_d.jpg)

As ever, Pimoroni have used their knowledge of laser cutters to produce a simple kit that can be assembled with great ease. The online instructions are clear and methodical, with great care taken to ensure that the steps can be undertaken by all levels of user.

The trickiest part was assembling the stand as I kept mixing up the blue stand clips...my bad.

![alt](https://farm1.staticflickr.com/729/32975637650_d6d28e515a_z_d.jpg)

> _Colonial Marines and Xenomorph not included_

The speaker comes with lots of slack wire, now this can be cut but you will need to re-tin the wire to ensure that it can be securely inserted into the PHAT BEAT board. You could also cable-tie the wire to shorten it. The choice is yours.

![alt](https://farm4.staticflickr.com/3919/33358303045_864d24eebe_z_d.jpg)

_My trusty Kamasa screwdriver set, and Lagouile pocket knife try and muscle into the shot_

![alt](https://farm1.staticflickr.com/580/33317599806_620858f86e_z_d.jpg)

> _I tucked it into the stand, but I may cut the wires down in the future_

## PHAT BEATS...word on the streets

_Oh dear...I am trying to sound cool_

The PHAT BEAT phat requires soldering, along with the Raspberry Pi Zero W.

![alt](https://farm4.staticflickr.com/3805/32515334254_ffdf505685_z_d.jpg)

I love the PHAT BEAT board, lots of great things going on, but my favourite things are the clips that hold the speaker cable securely. They require some gentle force to push the spring clip down so that the speaker cable can be inserted. Delicate, yet strong connection, bravo!

When soldered the PHAT BEAT looks like this.

![alt](https://farm1.staticflickr.com/763/33358299965_322e449656_z_d.jpg)

This enables your Pi Zero W to be slotted into it, and gives access to the buttons on the edge of the case. This is where I have a little gripe, as when reaching for the buttons I regularly try and press the attached Pi Zero w by accident. This isn't a big deal but just be careful!

## Software

Again the typical Pimoroni software install experience, flawless! It even installed some example code snippets to test the APA102 LEDs. Fun!

I also found a VLC streaming audio player, so I installed it and rebooted the Pi Zero W to load the daemon service so that VLC is running in the background. The speaker sprang into life...at full volume...after a change of pants I stopped Phil @Gadgetoid's choice of music and swapped the streams for BBC Radio 6 and other rather more sedate streams.

FYI the streaming music URLS are stored in
    
    
    /etc/vlcd/default.m3u
    

and they can accept many different MP3 radio streams.

My default.m3u now looks like this, those with # are ignored by VLC
    
    
    http://bbcmedia.ic.llnwd.net/stream/bbcmedia_6music_mf_p  
    http://media-the.musicradio.com:80/SmoothNorthWestMP3
    
    #http://relay4.slayradio.org:8200/
    #http://allstream.rainwave.cc:8000/all.mp3
    #http://tx.sharp-stream.com/icecast.php?i=planetrock.mp3
    #http://s1.viastreaming.net:8000
    

### Other functions

You can also stream audio from your iPhone / iPad using Airplay and Pimoroni have [written a great tutorial](https://learn.pimoroni.com/tutorial/sandyj/streaming-airplay-to-your-pi) Sadly I couldn't try it as I don't have an iPhone...no don't weep for me, seriously I don't want one :)

> [@biglesp](https://twitter.com/biglesp) If you get the mopidy.conf sorted properly, Les, then we'll shout you a Greggs.
> 
> -- pimoroni (@pimoroni) [March 10, 2017](https://twitter.com/pimoroni/status/840172850887708672)

Pimoroni are [looking to use Mopidy](https://www.mopidy.com/) to stream audio from Spotify, Soundcloud, Google Play and your own personal collection.

You can also [use Volumio with this kit](https://volumio.org/), another great open source audio player that works with many different devices.

## Speaker Quality

![alt](https://farm3.staticflickr.com/2927/32975631860_57507d34e8_z_d.jpg)

The 4 Ohm 5W mono speaker is lovely, producing a nice bass sound and it can be turned up quite loud before there is any serious distortion.

## Conclusion

![alt](https://farm4.staticflickr.com/3873/33204101252_247f9ed865_o_d.gif)

Another great kit from the pirates. It is fun to build and there are very few moments where you can go wrong. The speaker is good quality, the PHAT BEAT board is really simple to use and comes with some great code examples. The laser cut kit is easy to build and requires only a screwdriver to tighten the screws.

[You can buy this kit, and others from Pimoroni.](https://shop.pimoroni.com/collections/raspberry-pi-zero)

![alt](https://farm3.staticflickr.com/2916/32920012990_6d9e856fcc_o_d.png)

## Have fun!

![alt](https://farm1.staticflickr.com/720/33358305555_ba8637153d_z_d.jpg)
