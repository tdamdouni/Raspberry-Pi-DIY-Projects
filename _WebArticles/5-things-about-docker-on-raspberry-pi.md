# 5 things about Docker on Raspberry Pi

_Captured: 2017-08-29 at 10:15 from [blog.alexellis.io](https://blog.alexellis.io/5-things-docker-rpi/)_

Here are 5 things you need to know about using Docker on the Raspberry Pi from **Docker Captain Alex Ellis** [@alexellisuk](https://twitter.com/alexellisuk/)

> If you're new to Docker then visit my Hands-On Docker online workshop: [Hands-On Docker labs](https://github.com/alexellis/HandsOnDocker)

## 1\. Install Docker with one command

Today there is no need to brace yourself for pages of hacks or technical jargon to get [Docker](https://www.docker.com/) onto your device. One command does it all (through `apt-get` behind the scenes) - you can even memorise the command:

On Raspbian enter:
    
    
    curl -sSL https://get.docker.com |sh  
    

Providing you're running Debian or a derivative you're now good to go. The folks at the [Docker](https://www.docker.com/) project build [docker/docker](https://github.com/docker/docker) from source through CI which includes quality gates around unit and integration tests.

## 2\. Know your Architecture

The Raspberry Pi hardware architecture is called ARM and differs from the architecture behind your regular PC, laptop or cloud instance.

> What does that mean? A binary built for either system will not execute on the other.

The `helloworld` container will not work on the RPi. I'd suggest starting with my tutorial [Get started with Docker on your RPi](http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/). It recommends a good set of base images to build what you need - whether that be Go, Node.js, Python, Nginx or something completely different.

The following shortcut will show you the architecture on a Pi or regular Linux machine:
    
    
    $ uname -a
    Linux alexellis 4.4.19-v7+ #906 SMP Tue Aug 23 15:53:06 BST 2016 armv7l GNU/Linux  
    
    
    
    $ uname -a
    Linux 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:33:37 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux  
    

_Output from my Raspberry Pi and an Azure cloud instance of Ubuntu_

All Pis are compatible with ARMv6 architecture so for simplicity's sake I recommend you build your code through an ARMv6 base image and only pull in official distribution binaries from the likes of Golang, Nodejs, InfluxDB etc where they target that architecture.

> What does this mean? It means you can't `docker run -d -p 80:80 nginx:latest` \- read on for the workaround.

## 3\. You can't trust anyone (yet)

This may seem like a harsh thing to say - but in a climate where even baby monitors and lightbulbs can be taken over to participate in [DDOS attacks](http://www.theregister.co.uk/2016/06/28/25000_compromised_cctv_cameras/) we need to get smart.

  * Don't use an image unless it's official

There are no truly official images but `resin/rpi-raspbian` is used by thousands of devices and curated by [resin.io](https://resin.io/). I would recommend creating all your images from this as a base.

The Docker team are working on a set of semi-official images under the namespace [armhf](https://hub.docker.com/r/armhf/) and you will see those images coming into play in the [Dockerfile.armhf](https://github.com/docker/docker/blob/master/Dockerfile.armhf) in the [docker/docker](https://github.com/docker/docker) repo.

> [Anil](https://twitter.com/avsm) from the Docker Inc. team in Cambridge told me how his team are procuring ARM servers like they were going out of fashion in order to create a build-farm to support ARM devices. That infrastructure will enable autobuild support on the public Docker Hub.

  * Don't run any binaries you that didn't compile yourself

Even if it takes 2 days to compile PhantomJS - it's still way better than relying on a tar.gz provided by someone you know nothing about on the internet.

> [Docker Security](https://www.oreilly.com/ideas/five-security-concerns-when-using-docker) by Adrian Mouat coins the term _poison image_ for an image tainted with malware.

I have provided a set of Dockerfiles on Github for common software such as Node.js, Python, Consul and Nginx:

If you want to create a Docker image for software such as [Prometheus.io](https://prometheus.io/download/), [Node.js](https://nodejs.org/en/download/) or [Golang](https://golang.org/dl/) then head over to their download page and locate the official binary package for ARM - then add it into one of the base images we covered above.

> If no binary exists then take the time to re-build from source and don't take any risks. Google the build instructions if you run into issues - they can often be found from a 5-minute search. 

## 4\. Get physical

The Raspberry Pi excels at interfacing with hardware through it's 40-pin header. You can talk to just about any electrical component directly or through add-on boards - if it's rated for 3.3v/5v that's a good start. Manufacturers like [Pimoroni](http://blog.pimoroni.com/) have a wealth of purpose-built sensor and LED boards which mean no trailing wires or complicated code libraries.

Have you seen my IoT demo from Dockercon and [Container.Camp](https://container.camp/) yet?

_Pre-recorded demo for Dockercon break glass in case of laptop failure._

All the Dockerfiles, Python code and build instructions are publicly available. I couldn't have done any of this without the Pi's support for physical hardware.

  * [Container Camp write-up](http://blog.alexellis.io/contain-yourself-in-london/) including my IoT demo.

> Getting live demonstrations from [@alexellisuk](https://twitter.com/alexellisuk) at [@AgilePBoro](https://twitter.com/AgilePBoro) [@docker](https://twitter.com/docker) [#ctmtech](https://twitter.com/hashtag/ctmtech?src=hash) [pic.twitter.com/6o1Ju0u5lm](https://t.co/6o1Ju0u5lm)
> 
> -- comparethemarkt_tech (@comparemkttech) [September 21, 2016](https://twitter.com/comparemkttech/status/778671369689133057)

## 5\. Build a super-computer

Building a cluster has never been easier than with the built-in [Swarm Mode](https://docs.docker.com/engine/swarm/) from Docker 1.12 onwards. Take it from me because I spent weeks rebuilding the Swarm, Consul binaries etc to set up a [28-CPU swarm](http://blog.alexellis.io/linux-user-developer-magazine/) for Linux User magazine.

Now I type in one command on my manager and another on the workers. What's more the managers can also do useful work, where as in the original swarm mode that was harder to achieve.

See Docker's presentation from Container.Camp right here - it literally takes two commands to begin building a super-computer.

> Want a secure [@docker](https://twitter.com/docker) cluster? No problem, it's built-in: two commands and you're set. [@containercamp](https://twitter.com/containercamp) [pic.twitter.com/viZ3CEy47g](https://t.co/viZ3CEy47g)
> 
> -- Alex Ellis (@alexellisuk) [September 9, 2016](https://twitter.com/alexellisuk/status/774195186998140928)

> The second most common question I get asked is: can I run a minecraft-super-server with a Pi cluster? The short answer is no and the long answer is yes.

You probably won't be playing a graphics-intensive game at a better FPS rate over your new Pi cluster and it probably won't make loading Chrome any quicker, but it's an invaluable learning tool.

You can can deploy your distributed application at an _infrastructure_ rather than at a specific set of servers. For instance:

  * Deploy an application on real hardware
  * Simulate network/power failures
  * Code against the Docker remote API
  * Track down bottle-necks and show scaling different services increases throughput (or not)

### Where next?

Connect with me on Twitter [@alexellisuk](https://twitter.com/alexellisuk) to go deeper with Docker, DevOps and containers.

There's over 28 Raspberry Pi and Docker tutorials on my blog. Explore them all here - ranging from time lapses to IoT sensor monitoring to learning Golang:

  * [Raspberry Pi tutorial series](http://blog.alexellis.io/tag/raspberry-pi/)

> Want to learn the basics of Docker in a hands-on way? Visit or fork my online workshop: [Hands-On Docker labs](https://github.com/alexellis/HandsOnDocker)
