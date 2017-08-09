# WD Labs, Raspberry Pi, ownCloud and Ubuntu

_Captured: 2017-05-19 at 11:42 from [owncloud.org](https://owncloud.org/blog/wd-labs-raspberry-pi-owncloud-and-ubuntu/)_

![Box on the left our last prototype - we've got something entirely different in development now.](https://owncloud.org/wp-content/uploads/2016/03/devices.jpg)

> _Box on the left our last prototype - we've got something entirely different in development now._

Last year, [we reported](https://owncloud.org/blog/western-digital-and-owncloud-team-up-to-bring-owncloud-to-home-users/) that [WD Labs](http://wdlabs.wd.com/) approached the ownCloud community to create something together. Since [our last update](https://owncloud.org/blog/update-about-the-western-digital-and-owncloud-pi-project/), we've been at it and [first test images built on Snappy Ubuntu Core 16.04 are available now](https://mailman.owncloud.org/pipermail/devel/2016-March/002273.html). We're looking for help in the ownCloud, Ubuntu, Raspberry Pi and WD Labs communities for help to test and improve them and will be able to make available a first batch of about 30 devices at the end of next week!

## Raspberry Pi 3, WD Labs and Ubuntu Snappy

The last weeks have been exciting. The Raspberry Pi 3 was released, bringing 64bit computing to the world of tiny boards. This is great for our project as the 32bit version created a limitation for ownCloud: PHP is unable to handle files larger than 2 to 4GB without some nasty tricks. We might, thus, go for the Raspberry Pi 3 if we ship this as a pre-assembled device in the future. Of course, right now, we keep working on Pi 2's for compatibility reasons.

WD Labs has some exciting news on their own - you might have noticed that on Pi Day (March 14) they [released a 314GB Pi Drive](http://wdlabs.wd.com/products/wd-pidrive-314gb/) bringing a small hard drive for the Pi to an even lower price point. We're building our current prototypes on the PiDrive kit and enclosure they [also offer on their website](http://wdlabs.wd.com/) and while these should be compatible with the final software we are developed, there will be a different case. Indeed, we're now prototyping an entirely new case specifically for ownCloud, flat and square with rounded corners rather than the standing, open-on-top case shown [in earlier blogs](http://blog.jospoortvliet.com/2016/02/fosdem-2016-and-owncloud-kolab-kde-and.html). No pictures yet, it will be a surprise!

Third, we're building on [Snappy Ubuntu Core](https://developer.ubuntu.com/en/snappy/) 16.04. This brings a very familiar operating system to the device and a full stack solution all the way to the Cloud. We won't have to maintain the stack and security updates are delivered with rock solid transactions which means that more time can be spent on a great user experience. In addition the work done can be easily reused on anything from a drone to a home router that also runs Snappy Ubuntu Core.

## Where are we now

As a reminder: the goal of this project is to create a product home users can buy to easily and quickly get their ownCloud up and running, based on a Raspbery Pi (or something like that!) and a hard drive (or more). Something they will be able to buy from a easy store online, receive home, plug in, configure in some easy steps and - done.

Right now, we've settled some basic decisions:

  * The image will be a Snap running on Ubuntu Core 16.04. This isn't officially released yet but close and will be a great platform going forward.
  * We'll work [in github](https://github.com/owncloud/pi-image/issues) on the scripts that generate the Snappy. Right now, we built on the [Ubuntu ownCloud Snap](https://github.com/kyrofa/owncloud-snap/tree/rolling) but this will be forked into the ownCloud repo when we start to integrate apps specific for our project. Thanks to the github forking mechanism we can stay in sync with the official image, just adding what we need.
  * We provide a easy way to find the device on the network with mDNS naming it 'owncloud.local'. This works with most Linux, all Mac and all Windows 10 systems. Help with finding a solution for older Windows systems would be welcome!

The test image provides exactly this. You can [grab them here](http://people.canonical.com/~kyrofa/owncloud-pi/) and help us test - and get involved improving them, the [scripts are here](https://github.com/owncloud/pi-image/tree/master/image-creation-tools). There are three images, one for the SD card (the small one), one for the storage drive and one combined image for on SD cards in case you have no hard drive attached.

## Get your device!

So what's next? If testing the coming days shows the image works, Western Digital will create a batch of some 30 devices you'll be able to order online and run with. They will be preloaded with these images and made available for sale to anybody who wants to get on board early. Of course, getting on board now means you'll have to be up for a slightly rockier ride than the later devices - we're only getting started! But future images should be compatible with your device and thanks to the transactional update capabilities of Snappy Ubuntu, upgrades can be quite safe and easy. As Snappy Ubuntu Core is still a moving target, you might want to hold off on going full production on the system yet as it is still possible a re-flash might be needed but that should become clear in the next few weeks.

You'll be the first with your own safe home for your data, built from Ubuntu and ownCloud!

## Moving forward

On the software side, we'll continue making the image easier to deploy. The plan now is to integrate a tool to get you through your router onto the world wide web. One contributor wrote [an ownCloud app for this](https://github.com/miska/ocipv6) and this should be the base for a introduction wizard to get new users set up. Anybody with some PHP skills and interested in helping with writing this wizard - please, get in contact!

Another high priority is performance tuning for the Pi - making this fast and smooth! There is plenty of room for improvement here and we more than welcome [pull requests to the repo](https://github.com/owncloud/pi-image/tree/master/image-creation-tools).

Once we're happy with the progress, we will do another test run. When we feel the basics are all there and are stable enough we can take this to a first, serious production run of about 500 devices. After that - the sky is the limit!
