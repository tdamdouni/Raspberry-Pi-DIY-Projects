# Live Deep Dive - Docker Swarm Mode on the Pi

_Captured: 2017-08-29 at 10:01 from [blog.alexellis.io](https://blog.alexellis.io/live-deep-dive-pi-swarm/)_

I've been putting Docker to work on the Raspberry Pi since I first heard about it in mid-2015. Two of the most rewarding things I've done this year are: writing a [tutorial on Docker Swarm for Linux User Magazine](http://blog.alexellis.io/linux-user-developer-magazine/) and building an [IoT sensor network for Dockercon '16](http://blog.alexellis.io/dockercon-2016-speaker-notes/) using the 5USD Pi Zero.

With the release of [Docker 1.12 GA and Swarm Mode](https://docs.docker.com/engine/swarm/) it made sense to start building out a Raspberry Pi cluster to explore the new features. Over several weeks I tested out Docker 1.12 with a mix of Raspberry Pi 2/3s (ARMv7) and Pi Zeros (ARMv6). I looked at things like OTG networking, building Docker from source on the Pi as a dynamic and static binary and various Linux distributions.

> A lot of that effort was simplified when a Debian package was made available officially by the Docker team through the `curl -sSL get.docker.com | sh` installation method.

#### Are you new to Docker?

If you're new to Docker please follow my guide to [Getting Started with Docker and Raspberry Pi](http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/) which covers how to build your first images and even use GPIO for Physical Hardware from Docker!

### Live Deep Dive

This live video covers:

  * Creating a Swarm with 7x Raspberry Pi 2s
  * Running through a `ping` service
  * Testing a hello-world web-service and a GUID generating micro-service
  * Testing multi-host communication with a redis-based hit counter scaled across all the hosts
  * A look at the Swarm Visualizer from Dockercon re-built on ARM

For the full suite of test scenarios **fork** my [alexellis/swarmmode-tests](https://github.com/alexellis/swarmmode-tests/tree/master/arm) repo on on Github.

### Feedback & questions

It would be great to hear from you. Please get in touch with your questions about the cluster, video, Raspberry Pi or just Docker in general through the comments or via [@alexellisuk on Twitter](https://twitter.com/alexellisuk).

### See Also:
