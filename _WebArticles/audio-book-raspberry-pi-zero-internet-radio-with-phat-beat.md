# Audio Book: Raspberry Pi Zero Internet Radio with pHAT BEAT

_Captured: 2017-08-05 at 19:20 from [www.google.de](https://www.google.de/amp/s/thisisyetanotherblog.wordpress.com/2017/03/23/audio-book-raspberry-pi-zero-internet-radio-with-phat-beat/amp/)_

A couple of days ago I laid my hands on a [pHAT BEAT](https://shop.pimoroni.com/products/phat-beat) and two [small speakers](https://shop.pimoroni.com/products/5w-4-ohm-65mm-full-range-speaker). Together with a [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero) (and an Internet connection of course) this makes building an internet radio easily possible. And yes, inspiration for this project was also the [Pirate Radio Kit](https://shop.pimoroni.com/products/pirate-radio-pi-zero-w-project-kit).  
The pHAT BEAT comes along with stereo output, an amplifier, a couple of buttons for adjusting the volume, playing/pause, forward/backward and powering off and a number of bright and shiny LEDs. Just the perfect audio hardware component for an internet radio.

### Hardware

[Raspberry Pi Zero with Micro SD card and up-to-date OS  
](https://shop.pimoroni.com/products/raspberry-pi-zero)[USB WiFi stick](https://www.amazon.com/Edimax-EW-7811Un-150Mbps-Raspberry-Supports/dp/B003MTTJOY/ref=sr_1_4?ie=UTF8&qid=1488748463&sr=8-4&keywords=mini+usb+wifi+adapter)[ (not needed if a Raspberry Pi Zero W is used)  
](https://shop.pimoroni.com/products/raspberry-pi-zero-w)[pHAT BEAT  
2 ](https://shop.pimoroni.com/products/phat-beat)[small speakers](https://shop.pimoroni.com/products/5w-4-ohm-65mm-full-range-speaker)some cables  
USB power supply

Assemble the hardware as required. This implies some soldering for the headers of the Raspberry Pi Zero and the pHAT BEAT as well as the connections to the speakers. [This tutorial](https://learn.pimoroni.com/tutorial/sandyj/assembling-pirate-radio) is a good guideline to see what to do.

### Software

Once the Raspberry Pi Zero is accessible headless in the local WLAN network (see [this blog post for setup instructions](https://thisisyetanotherblog.wordpress.com/2017/03/06/neopixels-strip-on-raspberry-pi-zero/)) install the [pHAT BEAT Python library](https://github.com/pimoroni/phat-beat).

Luckily the software for an internet radio project already exists. The setup is really made simple by running the setup script only. The setup script installs the required software and adjusts the whole configuration on the Raspberry Pi Zero. See <https://github.com/pimoroni/phat-beat/tree/master/projects/vlc-radio> for further reference.

Once the installation is complete, reboot. After reboot the internet radio will be automatically started and will play some example music.

The pHAT BEAT's buttons directly work with the example projects software. Adjusting the volume or switching between different items on a configurable playlist (see configuration below) is directly possible. Even the off button immediately works: it turns off the radio and fully shuts down the Raspberry Pi Zero.

### Configuration

#### Configure Internet Radio Streams

Collect the URLs of your favourite internet radio streams. Create the file /home/pi/.config/vlc/playlist.m3u . Insert the URLs into the playlist as in this example:

##### Example playlist.m3u
    
    
    #EXTM3U
    #EXTINF:0,station1
    #EXTVLCOPT:network-caching=1000
    http://station1.net/.../...
    #EXTINF:0,station2
    http://station2.com/.../.../mp3/...
    #EXTINF:0,station3
    http://station3.something/...

Alternatively create a playlist containing the radio stream URLs of your choice in VLC and save the playlist to a file. This file can be copied to the Raspberry Pi Zero to /home/pi/.config/vlc/playlist.m3u.

After reboot the forward/backward buttons of the pHAT BEAT can be used to switch between the different internet radio streams.

### Wrapping: The Result

The wrapping was simple in this case: an old book became a nice „audio book"! Similar to my ‚book book shelves' an old book is hollowed inside with a sharp knife so the hardware fits in.  
Surprisingly well is the sound of the speakers inside the book!  
All I need now is to find a way to operate the small buttons of the pHAT BEAT…

![1](https://i1.wp.com/thisisyetanotherblog.files.wordpress.com/2017/03/1.jpg?w=319&h=410&crop&ssl=1)

![2](https://i1.wp.com/thisisyetanotherblog.files.wordpress.com/2017/03/2.jpg?w=278&h=410&crop&ssl=1)

![3](https://i0.wp.com/thisisyetanotherblog.files.wordpress.com/2017/03/3.jpg?w=601&h=448&crop&ssl=1)

### Info & Links

<https://github.com/pimoroni/phat-beat>
