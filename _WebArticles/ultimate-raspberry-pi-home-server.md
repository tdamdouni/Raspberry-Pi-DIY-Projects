# Ultimate Raspberry Pi Home Server

_Captured: 2017-05-23 at 18:51 from [www.instructables.com](http://www.instructables.com/id/Ultimate-Pi-Based-Home-Server/)_

![Ultimate Raspberry Pi Home Server](https://cdn.instructables.com/FVQ/YDJS/HKPXB5RM/FVQYDJSHKPXB5RM.MEDIUM.jpg?width=614)

![100_2820.JPG](https://cdn.instructables.com/FPB/IIHX/HJF2JXN1/FPBIIHXHJF2JXN1.SMALL.jpg?width=319.8763796909492)

![100_2900.JPG](https://cdn.instructables.com/F05/V686/HKM90SZZ/F05V686HKM90SZZ.SMALL.jpg?width=294.1236203090508)

![100_2817.JPG](https://cdn.instructables.com/FIW/6KLY/HJF2JXN7/FIW6KLYHJF2JXN7.LARGE.jpg)

![100_2816.JPG](https://cdn.instructables.com/F37/NHQW/HJF2JXNB/F37NHQWHJF2JXNB.LARGE.jpg)

Welcome reader.

**Follow me on twitter **[here](https://twitter.com/dilwil_talk)** for similar projects; tweet me for any help with this one**!

**First please note: This instructable can be done within a day, but a weekend is certainly recommended.**

In this instructable I hope to teach you key skills involved with setting up and configuring a Linux Server. The knowledge used here can be applied to almost all PC architectures so if you don't own a Pi_ (Why not dude?)_ or it's tied up in another project, any old or unused PC will work. In more detail the main skills taught will be:

  * Burning an ISO image to an SD for the Pi 
  * Installing an OS 
  * Setting up A web server 
  * Setting up An SQL instance 
  * Deploying a custom cloud network 
  * Managing users for the cloud network 
  * Setting up a SAMBA File sharing network, which will integrate into an established windows based home or office network 
  * Controlling SAMBA users 
  * Establishing a static IP whilst using a non-static IP internet connection 
  * Using Webmin Console to install packages 
  * Using Command line terminal to install packages 
  * Carrying out basic commands such as rebooting (terminal) 
  * Editing system files with Nano terminal based editor 
  * Permanently mounting hard drives within the Linux file system table via webmin 
  * Understanding the principal of the Port forwarding function on a home router 
  * Setting up a web interfaced bit torrent manager 
  * Being an overall IT nerd. 

If you're interested then carry on reading. If not, give it a try; you may discover a new hobby.

As the above list demonstrates there's a lot to learn. I definitely feel this is a weekend project. I've followed this process several times and it takes a couple of days at least. Its good to take long breaks because your eyes may begin to become strained and you may suddenly become unenthusiastic about the whole thing. This instructable offers functions of many different store purchasable products, such as:

The server we'll setup will cost far less than each of these services in the long run and only a fraction of the cost of the combined services. Setting up your own server is not only custom and cheap, its very rewarding. I will be a happy guy if somebody benefits from what this instructable contains or become inspired by what I have done. It took ages to plan and write this instructable. If you learn anything at all or feel this instructable is well written or well documented, please vote for me in the Weekend Projects Contest or the I could make that contest.

I would also like to point out that this is not a comprehensive tutorial on designing a server case. There are details of my case on step 3, however this guide is intended to be a comprehensive software tutorial. So if you get stuck or feel a step isn't too clear, just let me know and i'll be happy to help.

A few tips: Because this takes more than one day, don't just fall asleep and forget what you were planing on doing next. Instead have a pile f post-it notes. This way before you ZzZzzzz... you can jot down anything that needs doing during the next session. I had loads. All over the walls, floors, chairs, desks - you name it! Okay slight exaggeration, but on a serious note they do help. I did use a full stack. Another tip would be to follow the steps on order. Don't just think "Hmm I like the sound of my own cloud network lets do that first!" The steps are in such an order that each before is most likely required for the current, if that makes sense. Just stick to the order, it'll make life easier. A final tip: don't be limited to what is taught here. Do Think of this as a base for inspiration. Adding more services such as those listed on the turnkey website is easily done using the search APT function within the Webmin Package manager.

Okay, Confused? Then let's learn...

_ Caution! This instructable contains 30 steps. Proceed at your own risk. _

## Step 1: Plan

![Plan](https://cdn.instructables.com/F37/NHQW/HJF2JXNB/F37NHQWHJF2JXNB.MEDIUM.jpg?width=614)

![plan.png](https://cdn.instructables.com/FI1/7QBS/HJGE1N7Y/FI17QBSHJGE1N7Y.LARGE.jpg)

First things first - **Plan**. There are many aspects involved with planning, and often when people over plan, they quickly lose interest in the actual task.

So, a brief plan is as follows.

_Components:_

1 x Raspberry Pi (B model)

1 x External USB 2.5' HDD (Capacity of your choice, mine is 1TB)

1 x Raspberry Pi Case of your choice (Mine is a cheap £3 laser cut, clear acrylic, self assembly kit from )

2 x Heat sinks for the processor on the Pi (Mine were free with the case)

1 x Ethernet Cable

1 x USB cable for the hard drive

1 x SD Card (8GB or above strongly recommended. Also ensure you copy everything off the card as all data will be deleted.)

Relevant power supplies for the Pi and HDD

_OS:_

We will be using the operating system image from [Ghoulmann](http://gonzotech.tumblr.com/post/35816630624/server-core-for-raspberry-pi).We'll download it later. The image is based on Raspian, which is a Debian flavor adapted for the Pi, that runs turnkey out the box.

Plan done. Proceed .

## Step 2: Features

![Features](https://cdn.instructables.com/FDO/LA0F/HJGE1N63/FDOLA0FHJGE1N63.LARGE.jpg)

![features.jpg](https://cdn.instructables.com/F9L/CJLR/HJFSY8CS/F9LCJLRHJFSY8CS.LARGE.jpg)

There are [many](http://www.turnkeylinux.org/all) available features avaiable to add to a home server, some **free**, some paid.

I have narrowed down a shortlist of _f_ree_ f_eatures that you will be able to add to your home server following the steps in_ this_ instructable .

  * Webmin Admin Interface (This could be considered the heart of the operation) 

Webmin is a state of the art server management web user interface. It allows the installation, management and control of the various services you may wish to add to the server. The interface is great fore first timers as it minimalizes the required use of the command line interface.

  * Shell In A Box (This could be considered the backend) 

'Shellinabox' is a web based interface for SSH'ing into the server. It runs on java and CSS so it's compatble with all the best browsers without any additional plugins.

  * Samba Windows File Server 

Samba is software that can be run on a platform other than Microsoft Windows, for example, Linux. Samba uses the TCP/IP protocol that is installed on the host server. When correctly configured, it allows the host to interact with a Microsoft Windows client as if it is a Windows file and print server.

  * ownCloud 

ownCloud gives you universal access to your files through a web interface. It also provides a platform to easily view & sync your contacts, calendars and bookmarks across all your devices and enables basic editing right on the web. ownCloud is extendable via a simple but powerful API for applications and plugins. Many of which are avaiable [here](http://apps.owncloud.com/).

  * Transmission BitTorrent WebUI 

Transmission is designed for easy, powerful use. It's web user interface allows torrent's to be remotley added, then downloaded to the default torrent location. This location ca the be shared via samba/ownCloud to allow remote streaming of downloaded content.

  * Apache Webserver 

The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems such as Linux. The goal of this project is to provide a secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards.

  * PHP5 

PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language. PHP is now installed on more than 244 million websitesand 2.1 million web servers. This is required for owncloud and any other webpages you wish to host.

  * MySQL Database 

Many of the world's largest and fastest-growing organizations including Facebook, Google and Adobe rely on MySQL to save time and money powering their Web sites. That why we'll be using it. It's also required for ownCloud.

  * no-ip Sync Client 

The no-ip sync client will allow us to give the server a 'static address', such as "yourname.no-ip.biz". The sync client will update the current ip your ISP's allocated you every ten or fifteen minutes. You must first create a free account at no-ip.biz, but more on that later.

Once you've understood the purpose of each element of the server, continue to the next step.

![Hardware Setup](https://cdn.instructables.com/F05/V686/HKM90SZZ/F05V686HKM90SZZ.MEDIUM.jpg?width=614)

![100_2820.JPG](https://cdn.instructables.com/FPB/IIHX/HJF2JXN1/FPBIIHXHJF2JXN1.LARGE.jpg)

![Before We Begin...](https://cdn.instructables.com/F3I/JI74/HKJRZI9O/F3IJI74HKJRZI9O.LARGE.jpg)

![Burn the Image](https://cdn.instructables.com/F4A/KZB9/HJGE1N7S/F4AKZB9HJGE1N7S.LARGE.jpg)

![Install the OS](https://cdn.instructables.com/FRZ/YGI6/HJGE1N7V/FRZYGI6HJGE1N7V.LARGE.jpg)

![Update Webmin](https://cdn.instructables.com/F2N/4703/HJGE1N82/F2N4703HJGE1N82.LARGE.jpg)

![3.2.png](https://cdn.instructables.com/FHJ/22U9/HJGE1I0I/FHJ22U9HJGE1I0I.LARGE.jpg)

![Shell Login](https://cdn.instructables.com/F85/E6EU/HJGE1N81/F85E6EUHJGE1N81.LARGE.jpg)

![4.2.png](https://cdn.instructables.com/FNJ/EWAC/HJGE1IDG/FNJEWACHJGE1IDG.LARGE.jpg)

![How to Reboot](https://cdn.instructables.com/FUY/PMW8/HJGE1N80/FUYPMW8HJGE1N80.LARGE.jpg)

![5.2.png](https://cdn.instructables.com/FIZ/CW8X/HJGE1JEM/FIZCW8XHJGE1JEM.LARGE.jpg)

![Changing the Server Name \(Hostname\)](https://cdn.instructables.com/FDT/P8N5/HKJRZI9N/FDTP8N5HKJRZI9N.LARGE.jpg)

![Mount the Hard Drive](https://cdn.instructables.com/FM1/HIXN/HJGE1N7O/FM1HIXNHJGE1N7O.LARGE.jpg)

![Mount the Hard Drive Continued](https://cdn.instructables.com/FQN/XPJU/HJGE1N7P/FQNXPJUHJGE1N7P.LARGE.jpg)

![My SQL](https://cdn.instructables.com/FTK/0HKZ/HKJRZI9L/FTK0HKZHKJRZI9L.LARGE.jpg)

![Add a Database to My SQL \(ownCloud Prep\)](https://cdn.instructables.com/F2Y/J5CE/HKJRZI9K/F2YJ5CEHKJRZI9K.LARGE.jpg)

![Add a User to My SQL \(ownCloud Prep\)](https://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.LARGE.jpg)

![Install PHP](https://cdn.instructables.com/FEM/4BHD/HKJRZI9J/FEM4BHDHKJRZI9J.LARGE.jpg)

![Install OwnCloud](https://cdn.instructables.com/FXT/C560/HKJRZI9H/FXTC560HKJRZI9H.LARGE.jpg)

![Let's All Do the Samba](https://cdn.instructables.com/FAG/KR97/HKJRZI9G/FAGKR97HKJRZI9G.LARGE.jpg)

![Accessing the Share](https://cdn.instructables.com/FUB/D1ON/HKJRZI9F/FUBD1ONHKJRZI9F.LARGE.jpg)

![Install Transmission \(Bit Torrent\)](https://cdn.instructables.com/FEY/I1Y4/HKJRZI9C/FEYI1Y4HKJRZI9C.LARGE.jpg)

![The Principal](https://cdn.instructables.com/F94/RIUG/HKJRZI9B/F94RIUGHKJRZI9B.LARGE.jpg)

![Install No-ip](https://cdn.instructables.com/FZ1/2CTL/HKJRZI9D/FZ12CTLHKJRZI9D.LARGE.jpg)
