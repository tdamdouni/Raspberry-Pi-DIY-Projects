# Raspberry Pi Zero W fixes networking omission

_Captured: 2017-05-10 at 22:37 from [opensource.com](https://opensource.com/article/17/5/review-raspberry-pi-zero-w)_

![Raspberry Pi Zero W fixes networking omission](https://opensource.com/sites/default/files/styles/image-full-size/public/images/life-uploads/raspbery_pi_zero_wireless_hardware.jpg?itok=0n27bglV)

> _Image credits : Raspberry Pi Foundation, CC BY_

[Issue 40 of the _MagPi_](https://opensource.com/business/15/11/raspberry-pi-zero) magazine changed everything I thought I knew about computing and technology. In the 1990s and early 2000s, tech publications drew subscribers by giving freebies with their magazines. First, with CDs and then DVDs, magazines came with free demos of games, shareware applications, and even limited internet service provider memberships. In the open source world, magazines gave away Linux distributions ready to be booted and installed. Although it's not done as much in the U.S. anymore, a few publications around the world still do it, and I think it is great!

But the 2015 December issue of the official Raspberry Pi magazine, also known as the Christmas issue, was giving a "computer" for free with every print. The Raspberry Pi Zero, a US$ 5 single-board computer, was shipped with issue 40 of the magazine to all subscribers! Since then, this smaller-than-a-credit-card computer has exploded around the world with people using them for all sorts of educational and DIY projects.

![Raspberry Pi Zero's size compared to a quarter](https://opensource.com/sites/default/files/resize/pizerow_82-700x700.jpg)

> _The Pi Zero is not much larger than a 25-cent coin._

But by the time Issue 41 came out a month later, a couple of issues were clear to some Raspberry Pi fans. The first was the scarcity of the product. If you didn't get a magazine in the mail, it was very, very hard to find it online. For many months, especially outside of England, it was difficult to buy one, which led to a lot of people trying to sell the one they got at outrageous prices on the Internet. The second was the fact that many Raspberry Pi fans (including me) wished the Raspberry Pi Zero came with built-in WiFi to avoid the extra dongles and space footprint of the device.

![](https://opensource.com/sites/default/files/resize/img_3079-700x488.jpg)

> _The original Raspberry Pi Zero on the left, and the new Raspberry Pi Zero W on the right_

Fast forward to February 2016, and the [Raspberry Pi Foundation announced the release of the Raspberry Pi Zero W](https://opensource.com/article/17/2/pi-zero-wireless), taking care of the problem since now the single-board computer would come with built-in WiFi and Bluetooth. The foundation also tried to fix the scarcity problem by using some of its [partners around the world](https://www.raspberrypi.org/products/pi-zero-w) to sell the new device on its release day. I bought my Raspberry Pi Zero W from a vendor that limited sales to only one device per customer to make sure its supplies could reach as many people as possible at the price promoted by the foundation. I ordered my Raspberry Pi Zero W on release day, and it arrived on my doorstep a week later.

The compromise was simple: The WiFi is built-in, but the price doubled! :-) Instead of US$ 5, the board was now US$ 10, but I believe it was worth it given that I no longer need a USB hub to plug in a keyboard, mouse, and WiFi adapter. All I needed to get started was a mini-HDMI-to-HDMI adapter for my display and a micro-USB-to-USB adapter for my keyboard and mouse.

![Raspberry Pi Zero W setup](https://opensource.com/sites/default/files/resize/pi_zerow_81_0-700x525.jpg)

> _My Raspberry Pi Zero W setup_

![Raspberry Pi Zero W up and running](https://opensource.com/sites/default/files/resize/pi_zerow_84_0-700x525.jpg)

> _Up and running!_

The Raspberry Pi Zero W uses the same system on a chip, the Broadcom BCM2835, as its predecessor, which means it is as fast as the original Raspberry Pi, version 1. It comes with 512MB RAM, which is the same amount as the Raspberry Pi Model B+.

After downloading the [latest version of NOOBS](https://www.raspberrypi.org/downloads/noobs/) and unzipping it on a FAT 32 formatted Micro SD, I was quickly booting my Pi Zero W, configuring my WiFi, and installing Raspbian. After a few minutes, I was booting into the system and running the Chromium browser surfing the World Wide Web.

I don't recommend trying to use the Raspberry Pi Zero W as a GUI desktop alternative. It works, but it is slow. I mean, you can watch YouTube videos on it, but for an extra $25, you could get a Raspberry Pi 3 that has double the RAM and more horsepower to give you a better and more responsive experience than the Raspberry Pi Zero W.

So, what is the Pi Zero W good for? Well, many things … It is an amazing little device to run server "stuff" around your house or office. It can be a great web, FTP, and proxy server. You can easily connect a camera module and use it as a surveillance server. Even though the Pi Zero and Zero W come with unpopulated pin headers, you can easily buy the pins and solder them on yourself. That way you can port your Raspberry Pi projects to the Pi Zero, potentially reducing your power consumption and space footprint, making your project even more fun and impressive. I would even say that one of the greatest rationales for the Raspberry Pi Zero W (other than the price, of course) would be to run any project where your computing can be done in a headless environment (i.e., with no monitor attached).

From an educational perspective, you can still run Scratch on the Pi Zero W, making the display the most expensive part of the hardware setup. Yet given that so many of us have TV sets with an HDMI input nowadays, just plug it in and have some fun!

For all intents and purposes, the Raspberry Pi Zero W is a Raspberry Pi Zero for people (like me) who would rather pay an extra $5 to have WiFi and Bluetooth capabilities without extra dongles for their projects.

_I would love to hear from anyone who has been using the Raspberry Pi Zero and/or the Raspberry Pi Zero W for DIY projects. Let me know in the comments._
