# Live stream to YouTube with your Raspberry Pi and Docker

_Captured: 2017-08-30 at 09:28 from [blog.alexellis.io](https://blog.alexellis.io/live-stream-with-docker/)_

In this guide we'll set up our Raspberry Pi so that we can stream live video to YouTube to either a public, unlisted or private stream.

Using a pre-built Docker image means we know exactly what we're getting and instead of having to go through lots of manual steps we can type in a handful of commands and get started immediately.

![Sample](https://pbs.twimg.com/media/DAIjOKEXUAEvacC.jpg)

_The YouTube live dashboard show my Raspberry Pi cluster and Pimoroni LED blinkt! boards._

> Acknowledgements: thanks to [Richard Gee](https://twitter.com/rgee0) for giving me the idea to live stream with a Raspberry Pi.

### The old way of doing things

Normally this would have involved typing in many manual CLI commands and [waiting up to 9 hours](https://twitter.com/alexellisuk/status/864386779285258240) for some video encoding software (`ffmpeg`) to compile itself. If you got anything wrong you'd have to add on another 9 hours of compilation time (on a PiZero). In fact while compiling this tutorial I left my Pi running over night and it ran out of disk space meaning I had to start all over again.

## The guide

You'll need a Raspberry Pi, I've used a [Pi Zero](https://shop.pimoroni.com/collections/raspberry-pi-zero) here and the accompanying camera cable. Once you've setup the camera according to the [official guide](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/) you're going to be good to go.

Also enable SSH via `raspi-config` and login remotely so you can save yourself some typing.

> This guide work with Raspbian Jessie Lite as well as the full Pixel desktop.

### Step 1. Install Docker

Installing Docker on the Pi is a one-line script:
    
    
    $ curl -sSL https://get.docker.com | sh
    
    $ sudo usermod pi -aG docker
    
    $ reboot
    

### Step 2. Test the camera

To make sure your camera is plugged in properly fire off a test shot. This will also help us gauge whether the orientation is correct:
    
    
    $ sudo raspistill -o tester.jpg
    

You can then use `scp` or `sftp` to copy the file back to your Mac, Linux or Windows machine.

> As a Windows user you may want to install [Git bash](https://git-scm.com/downloads) which provides all the common UNIX-like utilities used with a Linux system.

### Step 3. Pull the image down

The Docker image I produced took almost 9 hours to build, so you have two options now - either rebuild it yourself (over 9 hours) or pull it down from the Docker Hub. It's a 640MB download which will expand to 1.3GB in disk space:
    
    
    $ docker pull alexellis2/streaming:17-5-2017
    

### Step 4. Get your secret streaming key

Now head over to your Youtube live streaming dashboard. Make sure you've filled in all the details and click Reveal to see your key:

![](https://blog.alexellis.io/content/images/2017/05/reveal.png)

Now copy and paste your key (i.e. `xxxx-xxxx-xxxx-xxxx`( into the Raspberry Pi's terminal like this:
    
    
    $ docker run --privileged --name cam -ti alexellis2/streaming:17-5-2017 xxxx-xxxx-xxxx-xxxx
    

You'll now be streaming live to the Internet, so pick wisely whether you want to keep that stream private, unlisted or public.

To cancel the stream just hit `Control + C` or shutdown the Pi.

![](https://pbs.twimg.com/media/DAIkG3pWAAED3va.jpg)

_This is me doing some late night testing for the blog._

**Share your URL!**

You can now share your URL with your audience and check out your statistics in real-time. There may be a delay of a few seconds - this is entirely normal and you can tweak lots of settings on the dashboard.

#### Step 5. Tweaks

**Running in the background**

To run in the background just swap out the `-ti` flag for `-d`:
    
    
    $ docker run --privileged --name cam -d alexellis2/streaming:17-5-2017 xxxx-xxxx-xxxx-xxxx
    

**Managing your container**

If you type in `docker run --name cam ...` a second time you will get an error saying that a container with that name already exists. You can do two things now:

  * Start the container again if it's stopped
    
    
    $ docker start cam
    

  * Stop and remove the container
    
    
    $ docker stop cam
    $ docker rm cam
    

Or in short-hand: `docker rm -f cam`

For a reference of Docker commands checkout my [Docker and Raspberry Pi workshop](https://github.com/alexellis/docker-blinkt-workshop/blob/master/1-SETUP.md).

**Run on boot-up**

To automatically stream every time you power up, then just add the flag `\--restart=always` to the `docker run` command line.

**Altering/extending the Docker image**

Head over to this Gist for instructions on how to hack on the Dockerfile or `entry.sh` shell-script which contains all the parameters for streaming.

  * [HackingOnLiveStreaming Gist](https://gist.github.com/alexellis/b86a91225eabd004573fe09da3fb34b2)

**Add effects to the video**

This is a more advanced step, but you can add effects to change the colour or rotate the picture by editing the [entry.sh](https://github.com/alexellis/raspberrypi-youtube-streaming/blob/master/streaming/entry.sh) file in the provided [Github repository](https://github.com/alexellis/raspberrypi-youtube-streaming).

**Audio**

By default the command-line we used won't be transmitting audio, for that we'd have to recompile ffmpeg using the [Dockerfile](https://github.com/alexellis/raspberrypi-youtube-streaming) and some additional options.

> In our [entry.sh](https://github.com/alexellis/raspberrypi-youtube-streaming/blob/master/streaming/entry.sh) script we set an empty audio channel since YouTube requires us to stream some audio, even if it's empty.

**Positioning your camera**

If you'd like to set your camera up on a window then there are two products I'd recommend which come with mini suction cups.

At the budget end you have the [ZeroView from ThePiHut](https://thepihut.com/products/zeroview) and at the premium end you have the cute [Octocam kit from Pimoroni](https://shop.pimoroni.com/collections/kits/products/octocam-pi-zero-w-project-kit) which contains all the hardware necessary for the project.

## Now I want to learn Docker!

If you'd like to learn more about Docker on the Raspberry Pi then head over to my free [tutorial series](http://blog.alexellis.io/tag/raspberry-pi/) as featured in [Docker Weekly](https://www.docker.com/newsletter-subscription).

There you'll be able to [Build a Timelapse Rig with your Raspberry Pi](http://blog.alexellis.io/raspberry-pi-timelapse/), Create an [Environmental Monitoring Dashboard](http://blog.alexellis.io/environmental-monitoring-dashboard/), get started right at the beginning [with a video](http://blog.alexellis.io/hands-on-docker-raspberrypi/) and much more!

> [Follow me on Twitter for all the latest blogs and tutorials](https://twitter.com/alexellisuk)

### Other Q&A

> Can I tweak the settings of the Dockerfile?

This short Gist gives instructions for editing the Dockerfile and entry script.

  * [HackingOnLiveStreaming Gist](https://gist.github.com/alexellis/b86a91225eabd004573fe09da3fb34b2)

> Can I use a USB camera?

This tutorial is geared up to use the Raspberry Pi camera module. Live-streaming with USB cameras is possible but there are more variables involved depending on the camera. If you'd like to write your own tutorial using a Dockerfile for a USB camera I'll link to it.

> Isn't this faster to build on an RPi3?

Yes it is (around 45-60 minutes including adding libraries) - but there is something brilliant about being able to use the tiny form-factor of the ZeroW which has WiFi built-in.

> Can't I cross-compile on another machine?

Cross-compiling is where you build code for one type of computer from a different one. I.e. code for a Pi Zero from a laptop or desktop machine. In theory you can do this but there a few drawbacks:

  * You need a correctly configured Linux desktop or cloud VM.
  * You have to be an expert with the command-line
  * It's hard to reproduce exactly the same result every time.

Building on the device and shipping an image means the process is as simple as possible.

> Shouldn't there be a `deb` for this?

There are several ways of packaging software including Debian package files, Docker images, binaries and source tarballs (tgz). The `deb` package would assume the target OS is Raspbian (only) - the Docker image we've built should technically run on non-Debian based distributions too such as ArchLinux. Debian packages also need a certain amount of vetting and community involvement to get into the official repositories. The Dockerfile is a quick and easy way to get a repeatable result.
