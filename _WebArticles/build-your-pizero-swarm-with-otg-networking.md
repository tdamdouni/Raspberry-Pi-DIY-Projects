# Build your PiZero Swarm with OTG networking

_Captured: 2017-08-30 at 16:19 from [blog.alexellis.io](https://blog.alexellis.io/pizero-otg-swarm/)_

So I unleashed a picture on the Internet several weeks ago which combined Docker, the Pi Zero and OTG networking. A lot of you responded to the post and wanted to try it out for yourself so I've put a new tutorial together.

The Raspberry Pi foundation's [Matt Richardson](https://twitter.com/MattRichardson) also bundled up the original tweet along with some of my best Docker material and posted it onto the official blog below:

  * [Docker comes to the Raspberry Pi](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)

**If you have no idea what Docker is, check out the post from the Raspberry Pi foundation above**

> Look ma, no Ethernet! 8 core [@Docker](https://twitter.com/docker) 1.12 swarm boom USB OTG [@Raspberry_Pi](https://twitter.com/Raspberry_Pi) [@pimoroni](https://twitter.com/pimoroni) [pic.twitter.com/frlSQ9ePpr](https://t.co/frlSQ9ePpr)
> 
> -- Alex Ellis (@alexellisuk) [August 13, 2016](https://twitter.com/alexellisuk/status/764518552154042369)

Before we get into the guide, I wanted to give you a bit of background.

### Q&A

OTG networking uses a gadget module in the Linux Kernel and can be used as a stand-in for Ethernet. Docker will run on an OTG network in the same way it would any other - providing that the various hosts have connectivity with each other.

#### Why would I use OTG networking?

OTG networking when done right means that a Pi Zero can be connected to almost any host device (PC, Pi 3, Laptop) with a single USB cable to create a fully-workable network.

This saves on network switches, cables, power supplies and bulk. That would have been a handy saving @ [Container.Camp](https://Container.Camp):

> -- Nicolas De loof (@ndeloof) [September 9, 2016](https://twitter.com/ndeloof/status/774284729755500544)

#### So how does it work?

You will get your hands messy by editing system config files and setting up static IP addresses and subnets. Once complete you will have in theory the equivalent of a USB ethernet adapter.

> If hacking on system files is not for you, then you may find the ClusterHAT (which comes with pre-flashed images) to be an easier alternative. See below.

#### But Docker, though?

Once your networking is fully configured you can set up a Docker Swarm in exactly the same way you would with an Ethernet configuration with my other Deep Dive guide.

> If you're wondering what a Swarm is, this is the best place to start:

Here is an example from last night when I ran through the instructions and created a brand new OTG cluster with Docker:

> Tutorial underway: [@Raspberry_Pi](https://twitter.com/Raspberry_Pi) OTG networking with [#pizero](https://twitter.com/hashtag/pizero?src=hash) to create ethernet-free [@docker](https://twitter.com/docker) swarm. [#testeverything](https://twitter.com/hashtag/testeverything?src=hash) [pic.twitter.com/7CXIhrz1wM](https://t.co/7CXIhrz1wM)
> 
> -- Alex Ellis (@alexellisuk) [September 13, 2016](https://twitter.com/alexellisuk/status/775798793736511488)

### OK.. how do I do this?

Follow the QuickStart guide on Github.com:

> Please send your comments, questions and suggestions my way on Twitter or via the comments section. 

### Who else is doing this?

There is a very cool product called the [ClusterHAT](https://shop.pimoroni.com/products/cluster-hat) which can be mounted onto a Pi's GPIO header to provide a USB hub for your Pi Zeros. Docker can also be used with this setup.

[James](http://raspberryjamberlin.de/zero360-part-1-building-the-zero360/) from Raspberry Pi Berlin Meetup has built a 360-degree camera using Pi Zeros and OTG networking. I'm still trying to convince him to try out Docker. It makes building, deploying and updating your software so much easier than manual hacking and scripts.

### What could go wrong?

The reason for the air-gap between my initial Tweet and these instructions is due to the sheer amount of unreliability I've experienced with OTG. The power supply needs to be just right, the host needs to be just right, the cables have to be perfect quality - and if the planets align you may be able to boot up 4x Pi Zeros at once.

> Don't let this put you off - I would like to improve the solution so please send in your comments, questions and suggestions.

The bandwidth may also be more limited when using 4x OTG devices through the shared USB host than through Ethernet ports. It would be good to see how this plays out in practice - if you want to do some benchmarking with [Docker Swarm](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/) that would be really interesting to see.

## See Also:

I host my blog on a Raspberry Pi 3 using Docker. You can find out more below:

If you want to find Pi Zeros then check out [stockalert.alexellis.io](http://stockalert.alexellis.io) and the write-up below:

  * [Using Docker to find Pi Zero Stock](http://blog.alexellis.io/rapid-prototype-docker-compose/)
