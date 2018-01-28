# What is a Raspberry Pi?

_Captured: 2017-12-04 at 01:28 from [opensource.com](https://opensource.com/resources/raspberry-pi)_

![Open source resources](https://opensource.com/sites/default/files/styles/image-full-size/public/lead-images/OSDC_Resource_Main_Page.png?itok=BS2hUvA5)

> _Open source resources_

A Raspberry Pi is a credit card-sized computer originally designed for education, inspired by the 1981 BBC Micro. Creator Eben Upton's goal was to create a low-cost device that would improve programming skills and hardware understanding at the pre-university level. But thanks to its small size and accessible price, it was quickly adopted by tinkerers, makers, and electronics enthusiasts for projects that require more than a basic microcontroller (such as Arduino devices).

The Raspberry Pi is slower than a modern laptop or desktop but is still a complete Linux computer and can provide all the expected abilities that implies, at a low-power consumption level.

To learn more about the basics of the Raspberry Pi, watch this short video.

## Is the Raspberry Pi open hardware?

The Raspberry Pi is open hardware, with the exception of the primary chip on the Raspberry Pi, the [Broadcomm SoC](http://www.raspberrypi.org/documentation/hardware/raspberrypi/) (System on a Chip), which runs many of the main components of the board-CPU, graphics, memory, the USB controller, etc. Many of the projects made with a Raspberry Pi are open and well-documented as well and are things you can build and modify yourself.

## What are the differences in Raspberry Pi models?

The Raspberry Pi Foundation has just recently released a new model, the Raspberry Pi 2, which supersedes some of the previous boards, although the older boards will still be produced as long as there is a demand for them. It is generally backwards compatible with previous versions of the board, so any tutorials or projects you see which were built for a previous version of the board should still work.

There are a two Raspberry Pi models, the A and the B, named after the aforementioned BBC Micro, which was also released in a Model A and a Model B. The A comes with 256MB of RAM and one USB port. It is cheaper and uses less power than the B. The current model B comes with a second USB port, an ethernet port for connection to a network, and 512MB of RAM.

The Raspberry Pi A and B boards been upgraded to the A+ and B+ respectively. These upgrades make minor improvements, such as an increased number of USB ports and improved power consumption, particularly in the B+. The A+ and B+ have been reviewed on Opensource.com here.

If you have a Raspberry Pi and aren't sure which version you have, plug it in and from the terminal window, and run:

cat /proc/cpuinfo

The output will include a revision code. The numbers indicate further differences, but if it is 0002-0006, it is an older Model B with 256MB of RAM. If it is 0007-0009, it is a Model A. The newer Model Bs are listed as 000d-000f. The B+ is 0010, and the A+ is 0012. (Revision 0011 was used for the Raspberry Pi Compute Module.)

## What kind of operating system does the Raspberry Pi run?

The Raspberry Pi was designed for the Linux operating system, and many Linux distributions now have a version optimized for the Raspberry Pi.

Two of the most popular options are [Raspbian](http://www.raspbian.org/), which is based on the Debian operating system, and [Pidora](http://pidora.ca/), which is based on the Fedora operating system. For beginners, either of these two work well; which one you choose to use is a matter of personal preference. A good practice might be to go with the one which most closely resembles an operating system you're familiar with, in either a desktop or server environment.

If you would like to experiment with multiple Linux distributions and aren't sure which one you want, or you just want an easier experience in case something goes wrong, try NOOBS, which stands for New Out Of Box Software. When you first boot from the SD card, you will be given a menu with multiple distributions (including Raspbian and Pidora) to choose from. If you decide to try a different one, or if something goes wrong with your system, you simply hold the Shift key at boot to return to this menu and start over.

There are, of course, lots of other choices. OpenELEC and RaspBMC are both operating system distributions based on Linux that are targeted towards using the Raspberry Pi as a media center. There are also non-Linux systems, like RISC OS, which run on the Pi. Some enthusiasts have even used the Raspberry Pi to learn about operating systems by designing their own.

## What are alternatives to the Raspberry Pi?

The Raspberry Pi is not the only small computing device out there. In fact, there are many more options available than we could list here. We've reviewed some of the choices before, [here](https://opensource.com/life/12/1/linux-hardware-race-tiniest-and-cheapest-15-cheap), but let's talk about some of the ones you may have heard of before.

The Arduino is another hobbyist board, which is geared towards those wanting to build out electronics projects. But, while the Raspberry Pi is a fully functional Linux computer, the Arduino is only a microcontroller. This means it does not run an operating system, but instead, runs very specific, small blocks of code written by the person using the device. There are numerous add-on boards that give it more capabilities, but out of the box, it's less ready-to-go than a Raspberry Pi. Another option is the Beaglebone series of boards, which are more similar to the Raspberry Pi, but a little bit more powerful (and a little bit more costly, too).

One advantage of using the Raspberry Pi over some other alternatives is the size of the community. If you have a question regarding a project you are working on, there are a lot of people who might be able to help you because of the large reach of the community.

## Where can I learn more?

We have covered a number of projects which make use of the Raspberry Pi for learning, teaching, conducting research, and just for fun. Here are a few of our favorites:

  * Read about Matt Jadud's experience learning and using the [Occidentalis](https://opensource.com/education/12/9/occidentalis-raspberry-pi-story) Linux distribution on his Raspberry Pi.

  * Hear from Luis Ibañez about [Coder](https://opensource.com/education/14/11/learning-web-programming-everyone-coder), a project from Google to use the Raspberry Pi to teach web programming to beginners and kids.

  * Learn how SUNY Albany is using the Raspberry Pi as an [alternative to textbooks](https://opensource.com/life/12/10/raspberry-pi-team-announces-open-source-arm-userland) for teaching college students.

  * Hear firsthand, from young maker [Lauren Egts](https://opensource.com/life/13/6/young-maker-lauren-egts), about how the Raspberry Pi has helped her learn to build cool things.
  * Explore the seven favorite Raspbery Pi [projects](https://opensource.com/life/14/3/favorite-raspberry-pi-projects) from Ruth Suehle, author of the book _[Raspberry Pi Hacks_](http://shop.oreilly.com/product/0636920029083.do).

  * See how the Raspberry Pi is being used to [light up](https://opensource.com/life/14/8/how-i-lit-jugglers-performance-my-raspberry-pi) a juggler's performance.

  * Learn how National Geographic Explorers are bringing the Raspberry Pi [to the wilderness](https://opensource.com/life/14/12/interview-shah-selbe-national-geographic-explorers) to gather data for conservation.
