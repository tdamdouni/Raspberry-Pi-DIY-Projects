# Ethernet On Pi Zero – How To Put An Ethernet Port On Your Pi

_Captured: 2015-12-04 at 23:46 from [raspi.tv](http://raspi.tv/2015/ethernet-on-pi-zero-how-to-put-an-ethernet-port-on-your-pi)_

The Pi Zero attracted a huge amount of attention, which is great for the educational mission of the Raspberry Pi Foundation. Whenever a new product is released, people air their opinions in the forums on what they would have liked it to have.

One of the most common "I wish it had"s was an ethernet port. There are reasons why ethernet was not included. The two most obvious ones are cost and board size (it would have almost doubled the size of the Zero)

### So What's To Be Done If You Need Ethernet?

Well the obvious solution would be to buy a B model Pi. B+ is fairly inexpensive these days, but also the Pi2 B has ethernet.

The other option, that we're going to cover today, is to add an external ethernet port using the SPI pins on the Pi.

Some time ago I managed to kill the ethernet/usb hub chip on one of my model B Pis. I thought it was a gonner. With no USB or ethernet, the only way I could log into it was through the serial port. Then someone (I think it was Alex Bradbury) pointed out that you can add ethernet over SPI. I looked into it. There was a forum thread about it, where people had done this, so I bought a little ethernet board for Arduino. It has an ENC28J60 chip on it, an ethernet port, a 25 MHz crystal and some resistors and capacitors…

![ENC28J60 based ethernet board from DX.com](http://raspi.tv/wp-content/uploads/2015/12/ethernet-board2-300x198.png)

> _ENC28J60 based ethernet board from DX.com_

Mine came from DealExtreme and it cost around £3\. [You can still buy them here.](http://www.dx.com/p/pcb-arduino-enc28j60-ethernet-module-blue-140971)

### And Then It Sat In A Box

When it arrived I did a classic geek thing. I looked in the forum post again. It looked hard and a bit scary (nobody had RasPi.TVed the procedure) and I had other stuff to do. So it sat on my desk for a while and eventually went in my box of "Things I'll get around to using one day - perhaps". It's been in that box for a while now.

### But Then Came The Zero

Provoked by the mass of "I want an ethernet port on my Zero" comments, I decided it was time to have a go. Fortunately, in the meantime, a device-tree driver has been produced for this chip, which means there is no need to compile anything, mess about with the kernel or even do very much at all. The procedure has been much simplified thanks to device-tree. (There I did it. I said something nice about device-tree - had to happen one day.)

### It Took Me About Half An Hour

I rummaged in my box of "Things I'll get around to using one day - perhaps" and found the ethernet board surprisingly quickly. As I had not yet soldered a header to my Zero, I decided to try it on an A+ to start with to see if I could get it working.

I wired it up carefully, booted the Pi, tweaked a config.txt line, enabled SPI and rebooted.

And that was it. An `ifconfig` showed me I had an ethernet connection. It was almost boringly easy and took about half an hour. I instantly soldered a header to my Zero and tried it on that. It worked perfectly. So I tweeted this terrible photo with two puns embedded at no extra charge…

> What could this be then? WJDK. Something plucked from the ether perhaps? Add £3 to your [#PiZero](https://twitter.com/hashtag/PiZero?src=hash)'s net value? [pic.twitter.com/0fcDEKqYdj](https://t.co/0fcDEKqYdj)
> 
> -- RasPi.TV (@RasPiTV) [December 1, 2015](https://twitter.com/RasPiTV/status/671745275120263168)

So now you'll want to know how to do it too.

### How Do We Wire It?

Here's an annotated shot of the ethernet port's pin header so you can see which connections you need to make…

![How to wire your ethernet board to GPIO](http://raspi.tv/wp-content/uploads/2015/12/ethernet-board-wiring_700.jpg)

> _How to wire your ethernet board to GPIO_

This is what mine looks like…

![All wired up on the Zero and ready to go](http://raspi.tv/wp-content/uploads/2015/12/ethernet-portsplus_700.jpg)

> _All wired up and ready to go_

As usual, I used one of my [RasPiO Portsplus boards to make wiring easier on the Pi's 40 pin header. You can find those here](http://rasp.io/portsplus).

### How Do We Configure It?

**Ensure SPI Is Enabled**

_Menu > Preferences > Raspberry Pi Configuration_  
Click the _Interfaces_ tab  
Ensure SPI is enabled and click OK

If you changed anything, you'll need to reboot for it to take effect.

**Tweak config.txt**  
Add the following to your /boot/config.txt

`dtoverlay=enc28j60`

Then when you reboot, your ethernet port should 'just work'. If you want to tweak the SPI clock speed or INT port you can use `dtoverlay=enc28j60,int_pin=25,speed=12000000` and tweak those variables. The ethernet chip is specified at 20 MHz maximum, so best avoid going above that.

### Speed Testing

You can use a command line version of speedtest.net if you install it…

`sudo apt-get install python-pip  
sudo easy_install speedtest-cli`

Then run it with `speedtest-cli`

### Speed Test Results

Pi Zero at 12 MHz 3.33 Mbaud down, 2.82 Mbaud up, 39.956 ms latency, 52.19km  
Pi Zero at 16 MHz 3.67 Mbaud down, 2.90 Mbaud up, 37.749 ms latency, 43.57km  
Pi Zero at 20 MHz 3.88 Mbaud down, 3.10 Mbaud up, 42.474 ms latency, 43.57km

Pi2 with ethernet onboard 74 Mbaud down, 5.86 MBaud up

What does that mean in real money? On my LAN, it took 3m 45s minutes to download an 85 MB file from Pi to Macbook Pro and 3m 18s to upload it to the Pi Zero. So it isn't going to win any speed awards, and probably isn't good enough for streaming HD video. But for an Internet of Things (IoT) device or for most purposes it'll be enough.

### It's Not Supposed To Work

Now I've looked at the [datasheet for the chip](http://ww1.microchip.com/downloads/en/DeviceDoc/39662e.pdf), I'm surprised it works at all.

According to that, page 80 states a power usage of 160 mA which is a lot more than the nominal 60 mA 3V3 rail limit on the Pi. It might therefore be better practice to run it from a separate supply. Your mileage may vary. I hope you had fun. I certainly did.

(Update to add) Sources close to RPi have told me unofficially that it will probably be fine to run this ethernet board on the 3V3 rail of the Pi Zero.
