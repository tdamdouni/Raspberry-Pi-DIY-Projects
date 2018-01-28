# Raspberry Pi Car Audio Player

_Captured: 2017-11-19 at 15:27 from [www.raspberrycoulis.co.uk](https://www.raspberrycoulis.co.uk/home-entertainment/raspberry-pi-car-audio-player/)_

![Raspberry Pi Car Audio Player](https://i2.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/09/image-2.jpeg?w=2448&ssl=1)

## Raspberry Pi Car Audio Player

Now that the Raspberry Pi Zero is easier to get hold of, it makes an ideal choice for a portable car audio player if paired with a suitable DAC, or Digital Analogue Converter.

If you have seen my post on the [Raspberry Pi Audio Player](https://www.raspberrycoulis.co.uk/home-entertainment/raspberry-pi-audio-player/) then you will have seen that there are multiple OS's offering slick user interfaces and support for many of the Raspberry Pi compatible DAC's on the market. As a result, I have been using mOode Audio, combined with my Raspberry Pi B+ and [IQ Audio's Pi-DAC+](http://www.iqaudio.co.uk/audio/8-pi-dac-0712411999650.html) for some time now and I have been impressed with the result.

However, I recently bought a newer car that had a USB port and auxiliary connector in the driver's arm rest which got me thinking. I could use the OEM iPod USB cable (that costs £50 from BMW, I kid you not!), risk a knock off but potentially working cable from eBay, or go full-hog and use this as an excuse to install a Raspberry Pi accompanied with a suitable DAC and upgrade my driving audio experience in one hit? Well, it would be a bit stupid to write a guide on a Raspberry Pi guide website about an iPod cable wouldn't it?!

### Enter Pimoroni's pHAT DAC

The team at [Pimoroni](https://shop.pimoroni.com) are naughty people. They keep making amazing Raspberry Pi accessories that usually results in me spending sums of money with them, then continue enticing me to buy by releasing yet more fantastic goodies! Having seen the [pHAT DAC](https://shop.pimoroni.com/products/phat-dac) before, I resisted temptation until I had a decent project lined up, and here it is.

![Pimoroni's pHAT DAC](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/09/image.jpeg?w=1024&ssl=1)

> _Pimoroni's pHAT DAC_

Costing no more than twelve English pounds, the pHAT DAC is a fantastic addition to any Raspberry Pi enthusiasts arsenal. With some soldering required to attach the header pins (and to attach the optional phono connectors if needed), you simply pop it onto your Pi, following their installation guide and you'll soon have it pumping out crisp sound from your Raspbian setup.

However, if you are planning on installing mOode Audio (or Volumio or Rune Audio) then installation is even easier. You attach the pHAT DAC and then select it from within the settings once your Pi has booted and you have opened the user interface inyour favourite web browser and hey presto!

### mOode Audio, AirPlay and WiFi Access Point

As I am going to be using my Pi in my car, I needed a way of controlling my Raspberry Pi car audio player so when I found out that [mOode now creates](http://moodeaudio.org) a WiFi Access Point (AP) that you can connect to as a way of accessing the user interface - all from a fresh install - I was suitably impressed! This is such a cool feature and solved my next problem before it even started!

### I need MORE USB ports!

So I have the elusive Pi Zero, Pimoroni's pHAT DAC and a WiFi AP to connect to, but the problem was now running out of USB ports, especially as I wanted to connect a slimline USB thumb drive to my Pi containing HD audio tracks (as in 24bit, 96-192khz audio). I then remembered that the guys at UUGear kindly sent me their fantastic [Zero4U](http://www.uugear.com/product/zero4u/), 4 port Raspberry Pi Zero USB hub which would be perfect for this! If you're not sure what the Zero4U is, then take a look at [my review](https://www.raspberrycoulis.co.uk/reviews/review-zero4u-pi-zero-usb-hub/) and see for yourself.

![The Zero4U fully assembled and ready to go](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/IMG_3656-opt.jpg?w=2028&ssl=1)

> _The Zero4U fully assembled and ready to go_

### All assembled

As my Raspbery Pi car audio player will be out of sight, hidden in the driver's arm rest in my car, it did not need to look like a work of art. I did not bother with any form of case, instead being satisfied that the arm rest was small enough to contain the Pi without it rattling around as I drove.

### Turning on and off

The last hurdle I needed to overcome was powering up and turning off the Raspberry Pi car audio player safely, without corrupting the SD card. I am well aware of the fantastic, but expensive to buy if you live outside the US, Mausberry Circuit Switch (I have used one of these in my [Raspberry PiStation build](https://www.raspberrycoulis.co.uk/gaming/build-your-own-raspberry-pistation/)), but given that installing this in a car requires some tinkering with the car's electrics, I decided I didn't want to risk this. Instead, I opted for a micro USB lead with an inline switch. This allows me to manually turn the power on, and once I have stopped and turned off my engine, I can login and shutdown the Raspberry Pi car audio player using the user interface. I can then kill the power using the switch.

### Using it

I am really impressed with my setup. Granted it doesn't look particularly fantastic, but it works excellently. More importantly, the sound quality is much better than an iPod! I tweaked a few options within mOode's settings, specifically to auto-play on boot, so my music now just picks up from where it left off when I shutdown last. It is a shame that I cannot safely queue up songs whilst driving (especially because I value my license and other road users!), but for a Raspberry Pi car audio player for less than £30, you cannot go wrong!
