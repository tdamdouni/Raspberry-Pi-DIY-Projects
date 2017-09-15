# How to get Docker working on your favourite ARM board with HypriotOS

_Captured: 2017-08-30 at 16:01 from [blog.hypriot.com](http://blog.hypriot.com/post/how-to-get-docker-working-on-your-favourite-arm-board-with-hypriotos/)_

It all began when Dieter aka [@Quintus23M](https://twitter.com/Quintus23M) started to experiment with the NVIDIA ShieldTV. The ShieldTV is a curious little thing. Sold as a media hub for your living room it does deliver one teraflop of processing power. On top of that it is one of the first 64-bit ARM boards that can be bought for a reasonable price.

Regular readers of our blog know that it is not in Dieter's nature to resist the Sirens voices of such an appealing beauty for long. Read on to learn what happened next…

Last December he started the work to get Docker running on the ShieldTV and [described his journey](http://blog.hypriot.com/post/getting-docker-running-on-a-highend-arm-gaming-console-for-fun-and-profit/) on our blog. The gist of it is that it was quite an involved process of creating his own custom Debian based operating system that supported building Go and Docker for ARM64.

The work of Dieter on the ShieldTV inspired our team to revisit the way we were building our beloved HypriotOS for the Raspberry Pi. Longing to publish the way we build it for quite some time we had been ashamed to actually do it because it was such a complicated mess. Don't get me wrong - it worked well enough and was completely automated with our CI system and even tested, but ultimately it was difficult to understand and change.

So Dieter's work got us thinking: What if we could restructure the build process of HypriotOS in such a way that it would be built in distinct layers that would create distinct build artifacts on their own. What if those artifacts could be tested and published on their own, too? Only to be assembled in a final step at the end to create a fully working SD card image. What if those distinct steps were self-contained and easy to understand?

Last week we had some time at our hands and we started working on a build process that would be the answer to all those questions. It is certainly still a little rough around the edges and needs further tweaking but it produces a working SD card image for the Raspberry Pi. We consider it beta quality and it is not yet completely on par with our stable HypriotOS Hector image, but it already runs very well.

The main repository for building HypriotOS SD card image for the Raspberry Pi can be found at GitHub in the [Image-Builder-Rpi Repository](https://github.com/hypriot/image-builder-rpi).

So what happens in this repository?

Basically it just assembles prepared artifacts into a working SD card image which then can be [easily flashed](https://github.com/hypriot/flash) onto a SD card.

The artifacts that are combined here are produced elsewhere each in their own GitHub repository:

The basic idea is that all these artifacts can be build and tested with the help of Docker. For instance if you look into the [os-rootfs](https://github.com/hypriot/os-rootfs) repository you will find a `Dockerfile` in the root of the project that will allow you to create a build and test environment for the root filesystem.

This makes two important things possible: Firstly it allows others to build the rootfs locally on their own computer and fix or extend the rootfs with ease. And secondly the rootfs is build and tested on [Travis CI](https://travis-ci.org/hypriot/os-rootfs) everytime somebody creates - for instance - a pull request. Combined these two points create a transparent development process with instant feedback.

It turned out that this approach is generic and powerful enough to be applied - you probably already guessed it - to the NVIDIA ShieldTV, too. By publishing the [Image-Builder-NVIDIA-ShieldTV](https://github.com/hypriot/image-builder-nvidia-shieldtv) repository we are making good on Dieter's promise to publish the sources for Dieter's journey with the ShieldTV.

But hold on - that's not all. To proof to ourselves that this process allows to easily port HypriotOS to different development boards we created [another Github repository](https://github.com/hypriot/image-builder-odroid-c1). It builds a SD card image for the very capable [ODROID C1+](http://www.hardkernel.com/main/products/prdt_info.php?g_code=G143703355573) development board. Similar to the Raspberry Pi 2 the ODROID C1+ features a quad core ARMv7 CPU with 1 GB of memory. Distinct from the Raspberry Pi 2 it features a gigabit ethernet port. A highlevel comparision of both devices can be found at [CNX-Software](http://www.cnx-software.com/2015/02/02/raspberry-pi-2-odroid-c1-development-boards-comparison/).

With this third supported board for HypriotOS we proofed to ourselves that this new build process makes it not only feasible but actually quite easy to extend the support of HypriotOS to new development boards.

Overall the relation of the different repositories now looks like this:

![](http://blog.hypriot.com/images/hypriotos-xxx/hypriotos_buildpipeline.jpg)

All these changes also redefined for us what HypriotOS is all about.

**Our old mission statement for HypriotOS was:**  
_"HypriotOS is a minimal operating system for the Raspberry Pi 1 & 2 that provides an optimized environment for running Docker. It is very easy to install and use. HypriotOS prides itself for coming with very recent versions of the Linux kernel and all included software."_

**Our new mission statement is:**  
*"HypriotOS is a minimal Debian-based operating system for **many popular IoT devices** that provides an optimized environment for running Docker. It is very easy to install and use. HypriotOS prides itself for coming with very recent versions of the Linux kernel and all included software."*

It is just a small change but it will have big implications.

One of the biggest downsides of having an ever increasing amount of IoT devices to choose from is fragmentation. Each device comes with varying support for existing operating systems. Take Linux for instance. Even if a vendor provides Linux support for a device from the start - it is often based on an outdated Linux kernel. This in turn often enough means that you can only use old software on top of it. Docker with OverlayFS is such an example. It can only be used with a Linux kernel greater than 3.18. And that's not only a problem of the small vendors, it even happens with big vendors like NVIDIA. The NVIDIA ShieldTV is provided only with a 3.10 Linux kernel while the latest stable Linux kernel is 4.4. Not to mention that the 3.10 kernel is [not supported any more by the kernel maintainers](https://www.kernel.org/category/releases.html).

With this background in mind a major goal of HypriotOS is to provide an operating system that behaves as similar as possible on **different** IoT devices. While I know that this might prove to be a difficult task - especially in regards to support for recent Linux kernels - I think it might prove to be a worthwhile effort that provides much value.

Providing a beta version of HypriotOS that supports three different development boards is a first step into that direction.

Being just able to flash HypriotOS on a SD card and get going in minutes is one of the basic promises of HypriotOS, so without further ado you can download it here:

[HypriotOS for the Raspberry Pi](https://github.com/hypriot/image-builder-rpi/releases)  
[HypriotOS for the NVIDIA ShieldTV](https://github.com/hypriot/image-builder-nvidia-shieldtv/releases)  
[HypriotOS for the ODROID C1+](https://github.com/hypriot/image-builder-odroid-c1/releases)

Hopefully you have a lot of fun trying out what HypriotOS has to offer!  
**Note:** We changed the default username to `pirate` (password `hypriot`) and disabled the `root` user for security reasons.

By adding support for many more boards we think HypriotOS gets a lot more attractive! What do you think?  
And for which board would you want to see support next? Help us to get your favourite ARM board supported by HypriotOS!

As always use the comments below to give us feedback and share it on Twitter or Facebook. You also might wanna discuss this article on [HackerNews](https://news.ycombinator.com/item?id=10926502) or vote it up if you find it interesting.

Govinda aka [@_beagile_](https://twitter.com/_beagile_)
