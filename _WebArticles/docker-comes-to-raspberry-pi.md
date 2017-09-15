# Docker comes to Raspberry Pi

_Captured: 2017-08-29 at 10:09 from [www.raspberrypi.org](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/)_

If you're not already familiar with [Docker](https://www.docker.com/), it's a method of packaging software to include not only your code, but also other components such as a full file system, system tools, services, and libraries. You can then run the software on multiple machines without a lot of setup. Docker calls these packages _containers_.

![Mayview Maersk by Flickr user Kees Torn](https://www.raspberrypi.org/app/uploads/2016/08/14907285349_a2a6c87a83_o-768x383.jpg)

> _Mayview Maersk by Flickr user Kees Torn_

Think of it like a shipping container and you've got some idea of how it works. Shipping containers are a standard size so that they can be moved around at ports, and shipped via sea or land. They can also contain almost anything. Docker containers can hold your software's code and its dependencies, so that it can easily run on many different machines. Developers often use them to create a web application server that runs on their own machine for development, and is then pushed to the cloud for the public to use.

While we've noticed [people using Docker on Raspberry Pi for a while now](http://blog.hypriot.com/), the latest release [officially includes Raspbian Jessie installation support](https://github.com/docker/docker/pull/24815). You can now install the Docker client on your Raspberry Pi with just one terminal command:

`curl -sSL https://get.docker.com | sh`

From there, you can create your own container or download pre-made starter containers for your projects. [The documentation](https://docs.docker.com/engine/understanding-docker/) is thorough and easy to follow. You can also follow [this Pi-focused guide](http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/) by Docker captain [Alex Ellis](https://twitter.com/alexellisuk).

## Docker Swarm

One way you can use Raspberry Pi and Docker together is for Swarm. Used together, they can create a computer cluster. With Swarm containers on a bunch of networked Raspberry Pis, you can build a powerful machine and explore how a Docker Swarm works. Alex shows you how in this video:

You can follow along with [Alex's written tutorial as well](http://blog.alexellis.io/live-deep-dive-pi-swarm/). He has even taken it further by using [Pi Zero's USB gadget capabilities](https://www.raspberrypi.org/blog/programming-pi-zero-usb/) to create a tiny Docker Swarm:

> Look ma, no Ethernet! 8 core @Docker 1.12 swarm boom USB OTG @Raspberry_Pi @pimoroni

The Raspberry Pi already makes many computing tasks easier; why not add deploying remote applications to that list with Docker?
