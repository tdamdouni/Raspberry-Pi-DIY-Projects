# Ultimate Raspberry Pi Home Server

# Ultimate Raspberry Pi Home Server

_Captured: 2015-12-15 at 11:59 from [www.instructables.com](http://www.instructables.com/id/Ultimate-Pi-Based-Home-Server/?ALLSTEPS)_

[ ![Picture of Ultimate Raspberry Pi Home Server](http://cdn.instructables.com/FVQ/YDJS/HKPXB5RM/FVQYDJSHKPXB5RM.MEDIUM.jpg) ](http://www.instructables.com/file/FVQYDJSHKPXB5RM/)

> _[Picture of Ultimate Raspberry Pi Home Server](http://www.instructables.com/file/FVQYDJSHKPXB5RM/)_

[ ![100_2820.JPG](http://cdn.instructables.com/FPB/IIHX/HJF2JXN1/FPBIIHXHJF2JXN1.MEDIUM.jpg) ](http://www.instructables.com/file/FPBIIHXHJF2JXN1/)

[ ![100_2900.JPG](http://cdn.instructables.com/F05/V686/HKM90SZZ/F05V686HKM90SZZ.MEDIUM.jpg) ](http://www.instructables.com/file/F05V686HKM90SZZ/)

> _Show All Items_

Welcome reader.

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

[ ![Picture of Plan](http://cdn.instructables.com/F37/NHQW/HJF2JXNB/F37NHQWHJF2JXNB.MEDIUM.jpg) ](http://www.instructables.com/file/F37NHQWHJF2JXNB/)

> _[Picture of Plan](http://www.instructables.com/file/F37NHQWHJF2JXNB/)_

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

___

by [DrWilson](/member/DrWilson/)

![Featured](/static/img/instructable/award-featured.png) ![I Could Make That Contest](/intl_static/img/instructable/award-contest.png)

__[ Download](/id/Ultimate-Pi-Based-Home-Server/?download=pdf)

__ 30 Steps  __

__

  * Flag As:
  * Wrong Category
  * Inappropriate
  * Incomplete
  * Spam

__ Share 

__ Favorite __  I Made it! __ __ Collection 

Intro 

![Ultimate Raspberry Pi Home Server](http://cdn.instructables.com/FVQ/YDJS/HKPXB5RM/FVQYDJSHKPXB5RM.SQUARE2.jpg)

#### Intro: Ultimate Raspberry Pi Home Server

Welcome reader. First please note: This instructable can be done within a day, but a weekend is certainly recommended. In this instructable I hope to teach you key ...

1 

![Plan](http://cdn.instructables.com/F37/NHQW/HJF2JXNB/F37NHQWHJF2JXNB.SQUARE2.jpg)

#### Step 1: Plan

First things first - Plan. There are many aspects involved with planning, and often when people over plan, they quickly lose interest in the actual task. So, a ...

2 

![Features](http://cdn.instructables.com/FDO/LA0F/HJGE1N63/FDOLA0FHJGE1N63.SQUARE2.jpg)

#### Step 2: Features

There are many available features avaiable to add to a home server, some free, some paid. I have narrowed down a shortlist of free features that you will ...

3 

![Hardware Setup](http://cdn.instructables.com/F05/V686/HKM90SZZ/F05V686HKM90SZZ.SQUARE2.jpg)

#### Step 3: Hardware Setup

The hardware basics are a Pi, SD card and power supply. You'll also need your LAN Ethernet cable. When I began I used a basic Pi case zip ...

4 

![Before we begin...](http://cdn.instructables.com/F3I/JI74/HKJRZI9O/F3IJI74HKJRZI9O.SQUARE2.jpg)

#### Step 4: Before we begin...

Before we begin, I'd just like to give you a quick idea of the planning and note taking I did. Below are some of the notes pages I ...

5 

![Burn The Image](http://cdn.instructables.com/F4A/KZB9/HJGE1N7S/F4AKZB9HJGE1N7S.SQUARE2.jpg)

#### Step 5: Burn The Image

The first step is often found tricky and complicated. I aim for it to be quick and simple, so we can move onto the fun part sooner.   ...

6 

![Install The OS](http://cdn.instructables.com/FRZ/YGI6/HJGE1N7V/FRZYGI6HJGE1N7V.SQUARE2.jpg)

#### Step 6: Install The OS

Installing the OS is a nice place to start, besides it being the first chronological step, it is a fairly simple one. The user (you) doesn't really have ...

7 

![Update Webmin](http://cdn.instructables.com/F2N/4703/HJGE1N82/F2N4703HJGE1N82.SQUARE2.jpg)

#### Step 7: Update Webmin

In this step we will login to Webmin for the first time. When this is done, we will update Webmin to the latest version using the integrated updater.  First, type ...

8 

![Shell Login](http://cdn.instructables.com/F85/E6EU/HJGE1N81/F85E6EUHJGE1N81.SQUARE2.jpg)

#### Step 8: Shell Login

In this step we will learn how to login to the shell interface via the browser.  Type the ip address of the RPi into the browser, then port ...

9 

![How to Reboot](http://cdn.instructables.com/FUY/PMW8/HJGE1N80/FUYPMW8HJGE1N80.SQUARE2.jpg)

#### Step 9: How to Reboot

Now we know how to access the command line, let's try a few things. First let's learn how to reboot. Login to the terminal as normal or if ...

10 

![Changing the Server Name \(Hostname\)](http://cdn.instructables.com/FDT/P8N5/HKJRZI9N/FDTP8N5HKJRZI9N.SQUARE2.jpg)

#### Step 10: Changing the Server Name (Hostname)

Our server is currently named CORE. Boring right? We're going to change it. First we can type hostname into the shell in the box terminal (after sucsessful login) ...

11 

![Mount the Hard Drive](http://cdn.instructables.com/FM1/HIXN/HJGE1N7O/FM1HIXNHJGE1N7O.SQUARE2.jpg)

#### Step 11: Mount the Hard Drive

If you are using ay external storage such as a USB hard drive or USB stick with the server, we must configure it to mount at boot. If ...

12 

![Mount the Hard Drive Continued](http://cdn.instructables.com/FQN/XPJU/HJGE1N7P/FQNXPJUHJGE1N7P.SQUARE2.jpg)

#### Step 12: Mount the Hard Drive Continued

Head back over to Webmin to continue mounting the storage media. From the top navigation bar click Disks and Network Filesystems  from within the System  dropdown. This will ...

13 

![My SQL](http://cdn.instructables.com/FTK/0HKZ/HKJRZI9L/FTK0HKZHKJRZI9L.SQUARE2.jpg)

#### Step 13: My SQL

Next we're are going to install MySQL. MySQL is a free tool that allows us to host online databases that are secure, and accessible by PHP scrips. This ...

14 

![Add a database to My SQL \(ownCloud prep\)](http://cdn.instructables.com/F2Y/J5CE/HKJRZI9K/F2YJ5CEHKJRZI9K.SQUARE2.jpg)

#### Step 14: Add a database to My SQL (ownCloud prep)

So now we're going to add a database to MySQL for ownCloud to use. Within the database ownCloud will store information within tables and fields. Moo . The information will ...

15 

![Add a user To My SQL \(ownCloud prep\)](http://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.SQUARE2.jpg)

#### Step 15: Add a user To My SQL (ownCloud prep)

MySQL is a multi-user database management system. This means that there can be more than one user that can gain access to the various databases and the data within ...

16 

![Install PHP](http://cdn.instructables.com/FEM/4BHD/HKJRZI9J/FEM4BHDHKJRZI9J.SQUARE2.jpg)

#### Step 16: Install PHP

In this step we'll install PHP and the various add-on's so its compatible with services such as MySQL, which we installed in an earlier step. For more info ...

17 

![Install ownCloud](http://cdn.instructables.com/FXT/C560/HKJRZI9H/FXTC560HKJRZI9H.SQUARE2.jpg)

#### Step 17: Install ownCloud

The installation for ownCloud can be done via the GUI (Graphical User Interface) within webmin. Head over to webmin and select system software packages from the System dropdown menu. ...

18 

![ownCloud: Pre-setup](http://cdn.instructables.com/FM1/HIXN/HJGE1N7O/FM1HIXNHJGE1N7O.SQUARE2.jpg)

#### Step 18: ownCloud: Pre-setup

Before setting up our ownCloud instance we need to create a folder on the hard drive for our data to rest within. Quickly open up a shellinabox session and ...

19 

![Configure ownCloud](http://cdn.instructables.com/FXT/C560/HKJRZI9H/FXTC560HKJRZI9H.SQUARE2.jpg)

#### Step 19: Configure ownCloud

So we've installed ownCloud, let's set it up then test it. Head over to 192.168.*.*/owncloud You'll be greeted by this:    Click next, you may then be asked ...

20 

![Creating an ownCloud User](http://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.SQUARE2.jpg)

#### Step 20: Creating an ownCloud User

ownCloud has loads of features so it would take a whole lot of time to explain each one and how to use it. That my friends, is another ...

21 

![Let's all do the Samba](http://cdn.instructables.com/FAG/KR97/HKJRZI9G/FAGKR97HKJRZI9G.SQUARE2.jpg)

#### Step 21: Let's all do the Samba

Samba will allow us to share documents with windows PC's on the same network. This will allow the server to be used as a central file server within ...

22 

![Configure Samba Drives](http://cdn.instructables.com/FAG/KR97/HKJRZI9G/FAGKR97HKJRZI9G.SQUARE2.jpg)

#### Step 22: Configure Samba Drives

So now we'll setup ad configure the samba instance. Samba operates on the windows file share protocol, so integration into a windows network (or singular PC) is seamless. ...

23 

![Add a Samba User](http://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.SQUARE2.jpg)

#### Step 23: Add a Samba User

I often find the WebGUI for adding samba users to be buggy and unreliable. Because of this, I'm going to teach you to add a user the terminal ...

24 

![Accessing the share](http://cdn.instructables.com/FUB/D1ON/HKJRZI9F/FUBD1ONHKJRZI9F.SQUARE2.jpg)

#### Step 24: Accessing the share

Welcome back.  Now lets mount the share as a volume in windows. Open up My computer. Click Map network Drive. (Locations are as follows: Windows 8: top toolbar ...

25 

![Install Transmission \(Bit Torrent\)](http://cdn.instructables.com/FEY/I1Y4/HKJRZI9C/FEYI1Y4HKJRZI9C.SQUARE2.jpg)

#### Step 25: Install Transmission (Bit Torrent)

Transmission is a torrent/download manager. You simply visit the port the service is running on to open the web UI. From there you can simply copy and paste ...

26 

![The Principal](http://cdn.instructables.com/F94/RIUG/HKJRZI9B/F94RIUGHKJRZI9B.SQUARE2.jpg)

#### Step 26: The Principal

This step will explain how we will achieve worldwide access for the server. We will use two fundamental elements. The first: no-ip, is a free service available to ...

27 

![Install no-ip](http://cdn.instructables.com/FZ1/2CTL/HKJRZI9D/FZ12CTLHKJRZI9D.SQUARE2.jpg)

#### Step 27: Install no-ip

To install no-ip, open a new shell session. Type: cd /usr/local/src To make the current working directory (folder) src.   Now download the tar file to the directory, ...

28 

![Port Forwarding](http://cdn.instructables.com/FX1/7A38/HKJRZI9E/FX17A38HKJRZI9E.SQUARE2.jpg)

#### Step 28: Port Forwarding

Setting up port forwarding is different on every router, because of this i'll just give you a general idea of which ports to forward and where. For more ...

29 

![Final: Backup](http://cdn.instructables.com/F4A/KZB9/HJGE1N7S/F4AKZB9HJGE1N7S.SQUARE2.jpg)

#### Step 29: Final: Backup

Now we've almost finished. The final procedure is to unplug the power, remove the SD and create a back-up image of the OS in it's current state. This ...

30 

![Congratulations - Felicitaciones - Glückwünsche - 恭喜](http://cdn.instructables.com/F94/RIUG/HKJRZI9B/F94RIUGHKJRZI9B.SQUARE2.jpg)

#### Step 30: Congratulations - Felicitaciones - Glückwünsche - 恭喜

Over 6,000 words and more than 170 illustrative diagrams and images later, we have reached the end. If you made it this far, well done. I hope you ...

[ ![Picture of Ultimate Raspberry Pi Home Server](http://cdn.instructables.com/FVQ/YDJS/HKPXB5RM/FVQYDJSHKPXB5RM.MEDIUM.jpg) ](/file/FVQYDJSHKPXB5RM/)

[ ![100_2820.JPG](/intl_static/img/pixel.png) ![100_2820.JPG](http://cdn.instructables.com/FPB/IIHX/HJF2JXN1/FPBIIHXHJF2JXN1.MEDIUM.jpg) __ ](/file/FPBIIHXHJF2JXN1/)

[ ![100_2900.JPG](/intl_static/img/pixel.png) ![100_2900.JPG](http://cdn.instructables.com/F05/V686/HKM90SZZ/F05V686HKM90SZZ.MEDIUM.jpg) __ ](/file/F05V686HKM90SZZ/)

[ ![100_2817.JPG](/intl_static/img/pixel.png) ![100_2817.JPG](http://cdn.instructables.com/FIW/6KLY/HJF2JXN7/FIW6KLYHJF2JXN7.MEDIUM.jpg) ](/file/FIW6KLYHJF2JXN7/)

[ ![100_2816.JPG](/intl_static/img/pixel.png) ![100_2816.JPG](http://cdn.instructables.com/F37/NHQW/HJF2JXNB/F37NHQWHJF2JXNB.MEDIUM.jpg) ](/file/F37NHQWHJF2JXNB/)

Show All Items  
__

Welcome reader.

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

  * [Dedicated Amazon EC2 turnkey servers](http://www.turnkeylinux.org/docs/ec2)
  * [Belkin routers that offer built in apps](http://www.belkin.com/networking/apps/)
  * Online cloud services such as [Google Cloud](https://cloud.google.com/products/cloud-storage)
  * NAS servers such as [this](http://www.amazon.co.uk/Buffalo-LinkStation-Network-Attached-Storage/dp/B000ZNUZAM). 

The server we'll setup will cost far less than each of these services in the long run and only a fraction of the cost of the combined services. Setting up your own server is not only custom and cheap, its very rewarding. I will be a happy guy if somebody benefits from what this instructable contains or become inspired by what I have done. It took ages to plan and write this instructable. If you learn anything at all or feel this instructable is well written or well documented, please vote for me in the Weekend Projects Contest or the I could make that contest.  
  
I would also like to point out that this is not a comprehensive tutorial on designing a server case. There are details of my case on step 3, however this guide is intended to be a comprehensive software tutorial. So if you get stuck or feel a step isn't too clear, just let me know and i'll be happy to help.

A few tips: Because this takes more than one day, don't just fall asleep and forget what you were planing on doing next. Instead have a pile f post-it notes. This way before you ZzZzzzz... you can jot down anything that needs doing during the next session. I had loads. All over the walls, floors, chairs, desks - you name it! Okay slight exaggeration, but on a serious note they do help. I did use a full stack. Another tip would be to follow the steps on order. Don't just think "Hmm I like the sound of my own cloud network lets do that first!" The steps are in such an order that each before is most likely required for the current, if that makes sense. Just stick to the order, it'll make life easier. A final tip: don't be limited to what is taught here. Do Think of this as a base for inspiration. Adding more services such as those listed on the turnkey website is easily done using the search APT function within the Webmin Package manager.

Okay, Confused? Then let's learn...  

_ Caution! This instructable contains 30 steps. Proceed at your own risk. _

## Step 1: Plan

[ ![Picture of Plan](http://cdn.instructables.com/F37/NHQW/HJF2JXNB/F37NHQWHJF2JXNB.MEDIUM.jpg) ](/file/F37NHQWHJF2JXNB/)

[ ![plan.png](/intl_static/img/pixel.png) ![plan.png](http://cdn.instructables.com/FI1/7QBS/HJGE1N7Y/FI17QBSHJGE1N7Y.MEDIUM.jpg) ](/file/FI17QBSHJGE1N7Y/)

Show All Items  
__

First things first - **Plan**. There are many aspects involved with planning, and often when people over plan, they quickly lose interest in the actual task.

So, a brief plan is as follows.

 

_Components:_

 

        1 x Raspberry Pi  (B model)

 

        1 x External USB 2.5' HDD   (Capacity of your choice, mine is 1TB) 

 

         1 x Raspberry Pi Case of your choice   (Mine is a cheap £3 laser cut, clear acrylic, self assembly kit from )

 

  2 x Heat sinks for the processor on the Pi  (Mine were free with the case)

 

       1 x Ethernet Cable 

 

   1 x USB cable for the hard drive 

 

       1 x SD Card  (8GB or above strongly recommended. Also ensure you copy everything off the card as all data will be deleted.)

 

       Relevant power supplies for the Pi and HDD 

 

 

_OS:_

 

  We will be using the operating system image from  [Ghoulmann](http://gonzotech.tumblr.com/post/35816630624/server-core-for-raspberry-pi).We'll download it later. The image is based on Raspian, which is a Debian flavor adapted for the Pi, that runs turnkey out the box.

 

Plan done. Proceed .

## Step 2: Features

[ ![Picture of Features](http://cdn.instructables.com/FDO/LA0F/HJGE1N63/FDOLA0FHJGE1N63.MEDIUM.jpg) ](/file/FDOLA0FHJGE1N63/)

[ ![features.jpg](/intl_static/img/pixel.png) ![features.jpg](http://cdn.instructables.com/F9L/CJLR/HJFSY8CS/F9LCJLRHJFSY8CS.MEDIUM.jpg) ](/file/F9LCJLRHJFSY8CS/)

Show All Items  
__

There are [many](http://www.turnkeylinux.org/all) available features avaiable to add to a home server, some **free**, some paid. 

I have narrowed down a shortlist of _f_ree_ f_eatures that you will be able to add to your home server following the steps in_ this_ instructable  .

 

  *     Webmin Admin Interface  (This could be considered the heart of the operation) 

Webmin is a state of the art server management web user interface. It allows the installation, management and control of the various services you may wish to add to the server. The interface is great fore first timers as it minimalizes the required use of the command line interface.

[More Info](http://www.webmin.com/)

  *     Shell In A Box (This could be considered the backend) 

'Shellinabox' is a web based interface for SSH'ing into the server. It runs on java and CSS so it's compatble with all the best browsers without any additional plugins.

[More Info](https://code.google.com/p/shellinabox/)

  *     Samba Windows File Server 

Samba is software that can be run on a platform other than Microsoft Windows, for example, Linux. Samba uses the TCP/IP protocol that is installed on the host server. When correctly configured, it allows the host to interact with a Microsoft Windows client as if it is a Windows file and print server.

[More Info](http://www.samba.org/)

  *     ownCloud 

ownCloud gives you universal access to your files through a web interface. It also provides a platform to easily view & sync your contacts, calendars and bookmarks across all your devices and enables basic editing right on the web. ownCloud is extendable via a simple but powerful API for applications and plugins. Many of which are avaiable [here](http://apps.owncloud.com/).

[More Info](https://owncloud.com/)

  *     Transmission BitTorrent WebUI 

Transmission is designed for easy, powerful use. It's web user interface allows torrent's to be remotley added, then downloaded to the default torrent location. This location ca the be shared via samba/ownCloud to allow remote streaming of downloaded content.

 [More Info](http://www.transmissionbt.com/)

  *     Apache Webserver 

The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems such as Linux. The goal of this project is to provide a secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards.

[More Info](http://www.apache.org/)

  *     PHP5 

PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language. PHP is now installed on more than 244 million websitesand 2.1 million web servers. This is required for owncloud and any other webpages you wish to host.

[More Info](http://www.php.net/)

  *     MySQL Database 

Many of the world's largest and fastest-growing organizations including Facebook, Google and Adobe rely on MySQL to save time and money powering their Web sites. That why we'll be using it. It's also required for ownCloud.

[More Info](http://www.mysql.com/)

  *     no-ip Sync Client  

The no-ip sync client will allow us to give the server a 'static address', such as "yourname.no-ip.biz". The sync client will update the current ip your ISP's allocated you every ten or fifteen minutes. You must first create a free account at no-ip.biz, but more on that later.

[More Info](http://freedns.no-ip.com/)

 

Once you've understood the purpose of each element of the server, continue to the next step. 

## Step 3: Hardware Setup

[ ![Picture of Hardware Setup](http://cdn.instructables.com/F05/V686/HKM90SZZ/F05V686HKM90SZZ.MEDIUM.jpg) __ ](/file/F05V686HKM90SZZ/)

[ ![100_2820.JPG](/intl_static/img/pixel.png) ![100_2820.JPG](http://cdn.instructables.com/FPB/IIHX/HJF2JXN1/FPBIIHXHJF2JXN1.MEDIUM.jpg) __ ](/file/FPBIIHXHJF2JXN1/)

[ ![100_2896.JPG](/intl_static/img/pixel.png) ![100_2896.JPG](http://cdn.instructables.com/FDG/YXHR/HKM90SZU/FDGYXHRHKM90SZU.MEDIUM.jpg) __ ](/file/FDGYXHRHKM90SZU/)

[ ![100_2897.JPG](/intl_static/img/pixel.png) ![100_2897.JPG](http://cdn.instructables.com/FRX/EI0K/HKM90SZV/FRXEI0KHKM90SZV.MEDIUM.jpg) __ ](/file/FRXEI0KHKM90SZV/)

[ ![100_2898.JPG](/intl_static/img/pixel.png) ![100_2898.JPG](http://cdn.instructables.com/F0B/11PG/HKM90SZW/F0B11PGHKM90SZW.MEDIUM.jpg) __ ](/file/F0B11PGHKM90SZW/)

[ ![100_2899.JPG](/intl_static/img/pixel.png) ![100_2899.JPG](http://cdn.instructables.com/FVL/LVCU/HKM90SZX/FVLLVCUHKM90SZX.MEDIUM.jpg) __ ](/file/FVLLVCUHKM90SZX/)

[ ![100_2902.JPG](/intl_static/img/pixel.png) ![100_2902.JPG](http://cdn.instructables.com/FDI/VLZQ/HKM90T00/FDIVLZQHKM90T00.MEDIUM.jpg) __ ](/file/FDIVLZQHKM90T00/)

[ ![100_2909.JPG](/intl_static/img/pixel.png) ![100_2909.JPG](http://cdn.instructables.com/FK7/1MLZ/HKM90T03/FK71MLZHKM90T03.MEDIUM.jpg) __ ](/file/FK71MLZHKM90T03/)

Show All Items  
__

The hardware basics are a Pi, SD card and power supply. You'll also need your LAN Ethernet cable. When I began I used a basic Pi case zip tied to my 1TB portable USB HDD.

My ideas developed. In my setup I wanted two mounted hard drives to offer more storage.  One was a Segate desktop 3.5" 320GB HDD. The other was a Turo Portable 2.5" 1TB HDD.

This offers loads of storage so I can carry out backups and so on.

When I decided on what hardware I wanted to add on, I came to an instant realization that some sort of case would be necessary. Due to the flashing LED's that indicate status on all three main hardware parts, I knew I wanted something partly transparent. I also wanted the case to look the part. As I struggle for desk space all too often, I also decided to make the server a wall mountable unit. This way I would have a self contained, Transparent server case.

_When designing your case you can be as basic or as simple as you wish. For me, it was very satisfying to have an end product that expressed some professional quality. _

To manage power, I simply mounted a 3-way socket into the case. I then spliced the end and soldered it onto an appropriately rated switch and IEC socket. This again leaves a pro like finish. _The transformers within the enclosure do not exceed the rated current of the wires._ For additional finish, I mounted an Ethernet and USB socket to the top. By using USB hub inside, I am able to host an external socket. This is useful as USB drives can be plugged in when necessary without having to undo the 6 sprung screws that hold the hinged door closed. Pictures are annotated below.

## Step 4: Before we begin...

[ ![Picture of Before we begin...](http://cdn.instructables.com/F3I/JI74/HKJRZI9O/F3IJI74HKJRZI9O.MEDIUM.jpg) ](/file/F3IJI74HKJRZI9O/)

Show All Items  
__

Before we begin, I'd just like to give you a quick idea of the planning and note taking I did. Below are some of the notes pages I made during the process. There are also a few of the many post-it notes that are more readable than others. They are still quite scruffy however. Due to the pace of writing and times of night, the writing isn't so desirable, but it just gives a quick idea. I may also add: some notes here are not relevant. I was also setting up my port forwarding for a web address. This involved forwarding subdomains to specific ports within the router manager (port forwarding) and the DNS file editor with my domain name provider (godaddy.com).

_Note: Monsters are contagious, do not stare for long._

           

## Step 5: Burn The Image

[ ![Picture of Burn The Image](http://cdn.instructables.com/F4A/KZB9/HJGE1N7S/F4AKZB9HJGE1N7S.MEDIUM.jpg) ](/file/F4AKZB9HJGE1N7S/)

[ ![1.11.png](/intl_static/img/pixel.png) ![1.11.png](http://cdn.instructables.com/F6Y/Z7J9/HJF2JXXT/F6YZ7J9HJF2JXXT.MEDIUM.jpg) ](/file/F6YZ7J9HJF2JXXT/)

[ ![1.1.png](/intl_static/img/pixel.png) ![1.1.png](http://cdn.instructables.com/FIV/UIW8/HJF2JXY2/FIVUIW8HJF2JXY2.MEDIUM.jpg) ](/file/FIVUIW8HJF2JXY2/)

[ ![1.2.png](/intl_static/img/pixel.png) ![1.2.png](http://cdn.instructables.com/FTM/J2S7/HJF2JXY1/FTMJ2S7HJF2JXY1.MEDIUM.jpg) ](/file/FTMJ2S7HJF2JXY1/)

Show All Items  
__

###  The first step is often found tricky and complicated. I aim for it to be quick and simple, so we can move onto the fun part sooner.

 

  * First download the Win32 Disk Imager from [here](http://downloads.sourceforge.net/project/win32diskimager/Archive/win32diskimager-v0.8-binary.zip?r=&ts=1374499756&use_mirror=netcologne)

This will allow us to burn an operating system image to our SD card.

  * Next download the ISO of the Raspian Turnkey mix from [here](https://github.com/downloads/ghoulmann/Raspliance-Core/raspliance-core-02.img.tar.gz).           `Credit to ``[Ghoulmann](http://gonzotech.tumblr.com/post/35816630624/server-core-for-raspberry-pi) for the image.`

Turnkey is an optimized OS package that is perfect for a home server.

The basic package includes [Webmin](http://www.webmin.com/) Dashboard and [Shell In A Box](https://code.google.com/p/shellinabox/).

  * Extract the downloaded file and open the application called _Win32DiskImager.exe_

  

  * When the application opens, we need to do two things. Firstly locate the downloaded ISO image file. by Clicking the **file **icon.
  * Next ensure the correct drive letter is selected by cross comparing the drive letters in My Computer with the ones available in the dropdown box.
  * Finally Click Write.
  * A message informing that the drive can be corrupted will appear. Don't panic, this is standard procedure, just click _Y_es.

 

  * The Image will the begin to write. It will take about eight minutes in total. Once the image has been written to the SD card, a Write Successful Dialog appears. Close it off and place the SD into your Pi. 

  
  

## Step 6: Install The OS

[ ![Picture of Install The OS](http://cdn.instructables.com/FRZ/YGI6/HJGE1N7V/FRZYGI6HJGE1N7V.MEDIUM.jpg) ](/file/FRZYGI6HJGE1N7V/)

Show All Items  
__

Installing the OS is a nice place to start, besides it being the first chronological step, it is a fairly simple one. The user (you) doesn't really have to do much the setup scrips take care of that.  
  
No extensive hardware is required for the setup process. All you need is a spare USB Keyboard (or just borrow one - it wont be long), A TV with HDMI or Composite input and the relevant cable. You'll also need your Pi power supply (Just a regular micro USB phone charger will do).

  
  
First plug the HDMI or Composite cable into the back of the TV, then set the TV to the correct input. This is because the Pi detects whether HDMI is plugged in then using that information chooses whether to output composite or not. Then plug the cable into the Pi.

Next insert the SD card we prepared earlier.

 

Plug in the keyboard. Then finally plug in the micro USB power. The Pi will the boot. Setup scripts will run automatically. This will take a few minutes, before being asked for a root password.

 

When prompted for a password, choose a secure one. Don't use one that is already used for your email account or similar. Use [howsecureismypassword.net](https://howsecureismypassword.net/) to find a secure password. Aim for something that takes around **10 octillion septuagintillion years **to crack. No but_ seriously_, choose something secure.

 

Setup may ask some other questions. Just input logical answers. After the Q&A is over setup will continue doing its thing for around 5 min.

 

At the end you'll be told the eth5 connection failed. That because we don't have a internet connection yet. Once setup is complete, unplug the power cable and re-locate your Pi server into its final resting position.

That's all there is to it, you no longer need the keyboard or monitor/TV. We are officially [headless](http://en.wikipedia.org/wiki/Headless_system) my friend.

## Step 7: Update Webmin

[ ![Picture of Update Webmin](http://cdn.instructables.com/F2N/4703/HJGE1N82/F2N4703HJGE1N82.MEDIUM.jpg) ](/file/F2N4703HJGE1N82/)

[ ![3.2.png](/intl_static/img/pixel.png) ![3.2.png](http://cdn.instructables.com/FHJ/22U9/HJGE1I0I/FHJ22U9HJGE1I0I.MEDIUM.jpg) ](/file/FHJ22U9HJGE1I0I/)

Show All Items  
__

In this step we will login to Webmin for the first time. When this is done, we will update Webmin to the latest version using the integrated updater. 

First, type in the ip of the server (RPi) followed by ":12321". This is the default port that Webmin is running on.

 

So for example I would type in "_192.168.2.12:12321_". 

Yours could look like this "_192.168.1.2:12321_" or "_192.168.2.5:12321_".

Notice how the port remains the same, despite the ip address changing. 

A quick explanation. The ip address is the string of numbers that defines any device connected to the internet. The router in your home has a function called DCHP  (Dynamic Host Configuration Protocol). This auto assigns the

devices on the LAN (Local Area Network) an ip following the default format of 192.168.1.*

This means that your Pi could be any ip address through 192.168.1.2 to 192.168.1.255 (It won't be 192.168.1.1 because that's usually the routers ip address).

Usually there is a chronological order of working, therefore unless you have over 20 devices on the network, you wont be going higher than 192.168.1.20

 

If you don't know how to determine the ip of a device on the network, I strongly recommend [this](http://download.cnet.com/SoftPerfect-Network-Scanner/3000-2085_4-10205180.html) tool. It's free and extremely handy if your less computer savvy than others. It works by scanning all the possible ip's on a network, then gathers information about the devices on the other end.

Once you've done that, your going to get that scary security warning we all hate. It looks like this:

    

This warning usually indicates a website that's has insecure certificates. This means the data sent to the server isn't nesacerily sent to the server, instead a fake server, trying to capture sensitive data. Usually you'd turn back here, but don't. This message is only displayed as we have not yet installed a SSL certificate on the server. These are expensive, so instead we'll just disable SSL (HTTPS://). That's later on though. For now just click proceed anyway. 

Once your proceeded you'll meet the Webmin Login page for the first time. Isn't she wonderful.

Here enter the username_ root _and the password you entered during the Linux installation. Then click_ Login_

The interface will then load.

        

 

At the bottom of the home page, you'll notice the _Upgrade Webmin Now_ button.

 

Click the button and Webmin does the rest. Just for reassurance, Here are images of how the process should look:

This is the updated package downloading.

 

This is the script carrying out the update.

 

This final image shows the update is complete. After this is the stage you're at, continue to the next step.

## Step 8: Shell Login

[ ![Picture of Shell Login](http://cdn.instructables.com/F85/E6EU/HJGE1N81/F85E6EUHJGE1N81.MEDIUM.jpg) ](/file/F85E6EUHJGE1N81/)

[ ![4.2.png](/intl_static/img/pixel.png) ![4.2.png](http://cdn.instructables.com/FNJ/EWAC/HJGE1IDG/FNJEWACHJGE1IDG.MEDIUM.jpg) ](/file/FNJEWACHJGE1IDG/)

Show All Items  
__

In this step we will learn how to login to the shell interface via the browser. 

Type the ip address of the RPi into the browser, then port :12320 - it will look like 192.168.1.*:12320

Again we'll see the untrusted website page.

Click Proceed anyway, remember we know it's safe because it's your server. This will load the shell interface.

You may be asking what is 'shell' and thinking 'I thought computers sand and water don't mix'. I'll explain. Shell is the Linux version of Command Prompt (which is probably familiar to you windows users). It basically offers access into the server via command line, which can be very useful for tasks such as adding samba users, or editing a file using nano (nano is a command line text file editor).

So once the interface has loaded it will look like this. Very basic I may add.

Again, here I'll offer some level of explanation. The 'core login:' is just the server hostname 'core' (we can change this later) followed by login:

This means the server requires us to login before carrying out any tasks. 

To login simply type your username (root) press return/enter then enter the password for the root account. Your password wont be displayed for obvious security reasons, such as the guy stood behind you looking over your shoulder. Take _that**_.

You will the be greeted by a login message explaining how warranties are not this nor that.

_**this is not a reference to the British band  
  
  
As posted by member __[rjanssen2_](http://www.instructables.com/member/rjanssen2/)

> _To fix the session closed after the prompt login, you need to change /etc/hosts.  
> Enter the following:  
> nano /etc/hosts  
> Then change the core in the line 127.0.1.1 to your hostname._

_Thanks for the help there!_

## Step 9: How to Reboot

[ ![Picture of How to Reboot](http://cdn.instructables.com/FUY/PMW8/HJGE1N80/FUYPMW8HJGE1N80.MEDIUM.jpg) ](/file/FUYPMW8HJGE1N80/)

[ ![5.2.png](/intl_static/img/pixel.png) ![5.2.png](http://cdn.instructables.com/FIZ/CW8X/HJGE1JEM/FIZCW8XHJGE1JEM.MEDIUM.jpg) ](/file/FIZCW8XHJGE1JEM/)

Show All Items  
__

Now we know how to access the command line, let's try a few things.

First let's learn how to reboot.

Login to the terminal as normal or if you already have an open session ensure the bottoms most line reads username@hostname ~#_ _in essence,_ _root@core ~# 

Type_ reboot_

 

Then press enter

You'll receive a broadcast message informing all users of the system reboot.

 

That's all there is too it. This is one of the most basic procedures you'll need to carry out. During the server configuration and setup you'll be doing this quite a lot.

 

Continue to the next step where you will learn how to use _nano_ to edit files.

## Step 10: Changing the Server Name (Hostname)

[ ![Picture of Changing the Server Name \(Hostname\)](http://cdn.instructables.com/FDT/P8N5/HKJRZI9N/FDTP8N5HKJRZI9N.MEDIUM.jpg) ](/file/FDTP8N5HKJRZI9N/)

Show All Items  
__

Our server is currently named CORE. Boring right? We're going to change it.

First we can type hostname into the shell in the box terminal (after sucsessful login) to print the current hostname. We can see it's 'CORE'.

So let's go ahead and change it. 

Type nano /etc/hostname

Press return which will open the text file located in the /etc directory on the SD card named hostname, with the terminal text file editor nano. On boot the setup scripts read the file contents and use it to set the hostname of the server.

So to change it, simply delete the contents of the text file and type your desired hostname.

Press shift and X to exit.

 

Press Y to save the changes.

 

Just hit return to save over the old file.

 

Now just reboot the server (covered in step 8) for changes to take effect. When you look in network location from a windows file browser you'll see your server has been renamed.

## Step 11: Mount the Hard Drive

[ ![Picture of Mount the Hard Drive](http://cdn.instructables.com/FM1/HIXN/HJGE1N7O/FM1HIXNHJGE1N7O.MEDIUM.jpg) ](/file/FM1HIXNHJGE1N7O/)

Show All Items  
__

If you are using ay external storage such as a USB hard drive or USB stick with the server, we must configure it to mount at boot. If your drive is formatted with the NTFS file system, follow the guide below. If it has any other type of formatting such as FAT 32, then skip to the next step.

 

Drives with Windows NTFS formatting can be tricky to mount within Linux.

To allow the drive to be mounted, we must install NTFS-3g. This irradiates any issues I know of.

So, open up a tab within your browser. Point it to the address and port of shell in a box, i.e, a new terminal session.

 

First type apt-get ntfs-3g

 

   

apt-get is the command to grab a package from the repository and install it.

The terminal may then begin to look like a scene from the matrix. This is just the downloading and installation of the package.

Below are images of how the process should look:

  

Your done when you see the root@core ~# message again. This is just the servers way of saying "I'm ready for my next command master."

## Step 12: Mount the Hard Drive Continued

[ ![Picture of Mount the Hard Drive Continued](http://cdn.instructables.com/FQN/XPJU/HJGE1N7P/FQNXPJUHJGE1N7P.MEDIUM.jpg) ](/file/FQNXPJUHJGE1N7P/)

Show All Items  
__

Head back over to Webmin to continue mounting the storage media.

From the top navigation bar click_ Disks and Network Filesystems_  from within the _System_  dropdown.

This will load the applet where we can select and mount the drive. To begin mounting click the dropdown box just above the file system table and select the format of the drive you are mounting. Mounting a drive within Linux will not remove your data, however it's always best to have a backup. 

This next page will allow you to name the mount and choose the location. We will create out mount in the location /media/serverhdd . Select Disk and there should only be one option within the dropdown to choose from. Choose No where you have the option for read only. Keep the default settings for everything else. 

Once you have the same settings as above, click create. This will take us back to an updated file system table.

Notice the fourth entry, this is the one we just created.

## Step 13: My SQL

[ ![Picture of My SQL](http://cdn.instructables.com/FTK/0HKZ/HKJRZI9L/FTK0HKZHKJRZI9L.MEDIUM.jpg) ](/file/FTK0HKZHKJRZI9L/)

Show All Items  
__

Next we're are going to install MySQL. MySQL is a free tool that allows us to host online databases that are secure, and accessible by PHP scrips. This means that a login page (such as the ownCloud login page) can use a PHP script to check login details such as user and password, thus allowing it to serve you the correct files and ultimately allowing you to login.

Without further ado, let's begin.

To install:

Login the Webmin admin console, hover over the unused modules category.

From there Select the MySQL entry.

This will serve a page informing us we either don't have the module configured correctly or don't have it installed. We don't have it installed do click the option that says 'click here to have it installed by apt'. Just for your information, apt is a Linux package manager that can be used to install and remove packages (basically software applications).

 

 

 The package will then be installed. Lots of code will be running in the webpage. Leave it to run its course. It will inform you at the bottom of the webpage when the package has been added.

 

After its installed, go back, and from the servers dropdown in webmin, select the MySQL Database server entry. This will load the interface.

    

 

Continue to the next step to learn how to add a database.

## Step 14: Add a database to My SQL (ownCloud prep)

[ ![Picture of Add a database to My SQL \(ownCloud prep\)](http://cdn.instructables.com/F2Y/J5CE/HKJRZI9K/F2YJ5CEHKJRZI9K.MEDIUM.jpg) ](/file/F2YJ5CEHKJRZI9K/)

Show All Items  
__

So now we're going to add a database to MySQL for ownCloud to use. Within the database ownCloud will store information within tables and fields. Moo . 

The information will range from usernames and passwords, to file size limits and file paths for each user. It's really quite clever.

 

 

Its quick and easy to add a table. First from within the MySQL database manager page in webmin click add a database.

 

The new database page will then load. Here name the database and leave all other options default. I've called mine owncloud for easy reference. (You'll need to note down the name for later.) We don't need to ad any tables or data because ownCloud will populate the database during it's installation process.

 

Click Create at the bottom of the page.  You'll then be taken back to the management page, where you'll see the new table.

 

Pretty easy right? Next: adding a user.

## Step 15: Add a user To My SQL (ownCloud prep)

[ ![Picture of Add a user To My SQL \(ownCloud prep\)](http://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.MEDIUM.jpg) ](/file/FMC60Q0HKJRZI9I/)

Show All Items  
__

MySQL is a multi-user database management system. This means that there can be more than one user that can gain access to the various databases and the data within them. This is useful as we can assign different permissions to the different users. 

_Why would we want to do that?_

This feature is implemented for a number of reasons. The first most obvious being a security breach. For example if someone somehow hacks access to a service or program's code which relies on a database within MySQL, they may be able de-crypt the login credentials to the MySQL database server. This means they could access sensitive data within other databases and cause havoc. **But wait** hold on, don't panic. Because with multi user functionality, the database server will be safe. We can know this because we are creating separate accounts that will range from managing the server to reading, modifying and even creating tables. If somebody ever did gain access, (which is highly unlikely) they would only have certain permissions within the delegated database/s. This way we are not compromising other services that rely on the SQL server. 

Another reason is if a piece of code within a service malfunctioned (also very unlikely) somehow losing control and beginning to erase and delete the databases. This wouldn't be possible because the program would only have access to its own database. All is not lost, Eh?

Very Clever I must point out.

 

So, lets lean how to create a user then. The user account we will create will be later used for ownCloud so use a logical username and password, that will be identifiable in the future.

Open up the MySQL database server manager if you haven't already. Which you probably have because your twitching with excitement at the concept.

 

So first, we need to click _User Permissions. _This will navigate us towards our goal. On the page you'll see a list of user and their corresponding info.

 

 

Sorry to ruin your fun Mr.Hacker. Anyway, on the above page click _Create New User_.

As you will soon see, this has loaded the add user page. Here we'll be able to add our ownCloud  database access user. Input the above information into the fields, which is: Username: owncloud

Password: choose one but remember it

Select all permissions besides Superuser. Quick tip - Click the top entry, scroll down, hold shift, click the bottom entry. Then deselect the Superuser entry by clicking whist holding ctrl.

Change the maximum concurrent logins to 15 (we wont be having more than 15 users at a time connected.

Leave other options default then_ Create_.

 

This will create the new user and then navigate us back to the user accounts page.

Here you will see the added user credentials.

I've blanked out the password for obvious reasons.

That's it, we've created our new user. During the ownCloud setup, ownCloud will tie the account to the specified database. (Remember the one we created earlier named cloud?)

Let's continue.

## Step 16: Install PHP

[ ![Picture of Install PHP](http://cdn.instructables.com/FEM/4BHD/HKJRZI9J/FEM4BHDHKJRZI9J.MEDIUM.jpg) ](/file/FEM4BHDHKJRZI9J/)

Show All Items  
__

In this step we'll install PHP and the various add-on's so its compatible with services such as MySQL, which we installed in an earlier step.

For more info on PHP [click here](http://en.wikipedia.org/wiki/PHP)

Begin by opening up a terminal session with shellinabox (Port 12320)

Login then type 

apt-get install php5 php-pear php5-mysql

Then press enter.

 

This will carry out the installation of PHP and other required dependencies for ownCloud and Transmission.

When you reach the above point just hit Y. This check is common practice and it's essentially just APT asking for permission to use up the specified amount of disk space to istall the requested programs.

Above we can see the files being fetched from the mirrors.

And remember when you see root@core ~#, you're all done!

Continue to the next step to being setting up ownCloud.

 

## Step 17: Install ownCloud

[ ![Picture of Install ownCloud](http://cdn.instructables.com/FXT/C560/HKJRZI9H/FXTC560HKJRZI9H.MEDIUM.jpg) ](/file/FXTC560HKJRZI9H/)

Show All Items  
__

The installation for ownCloud can be done via the GUI (Graphical User Interface) within webmin.

Head over to webmin and select system software packages from the System dropdown menu.

This will take us to the install package webpage.

Here focus on the second section: _Install a New Package_. Here select the _Package from APT_ radio button. (Which is one of these  [ Try Me! ] )

Type into the corresponding box _owncloud,_ like this: 

Then hit Install.

 

The script has finished, thus, ownCloud has been successfully installed.

Continue to the next step to configure and setup up ownCloud.

## Step 18: ownCloud: Pre-setup

[ ![Picture of ownCloud: Pre-setup](http://cdn.instructables.com/FM1/HIXN/HJGE1N7O/FM1HIXNHJGE1N7O.MEDIUM.jpg) ](/file/FM1HIXNHJGE1N7O/)

Show All Items  
__

Before setting up our ownCloud instance we need to create a folder on the hard drive for our data to rest within.

Quickly open up a shellinabox session and type these three commands separately:

1 cd /media/serverhdd

2 mkdir cloud

3 chmod 750 /media/serverhdd/cloud

This will create the folder and change the permissions so owncloud can write to it.

You can now continue.

## Step 19: Configure ownCloud

[ ![Picture of Configure ownCloud](http://cdn.instructables.com/FXT/C560/HKJRZI9H/FXTC560HKJRZI9H.MEDIUM.jpg) ](/file/FXTC560HKJRZI9H/)

Show All Items  
__

So we've installed ownCloud, let's set it up then test it.

Head over to 192.168.*.*/owncloud

You'll be greeted by this: 

 

Click next, you may then be asked if you want to install into a subdirectory, just delete the text in the field and click next. If not just carry on.

 

Here is the important part. This page is where we will specify a folder for the data to go into, and admin account, and the SQL information.

Input a Username and password.

Click the _advanced_ button

Type //media/serverhdd (or whatever you mounted your hard drive as) followed by /cloud. So it'll look like this: //media/serverhdd/cloud 

Next click the MySQL button and the page will expand, revealing options for the database.

Here type in the MySQL username and password for the owncloud user we made.

Type in the database name of which you wish to use (we also created one earlier)

Type Localhost in the final box.

Finally click _Finish setup_.

This will finalize the setting and load up the owncloud service.

Ta Dahh!!

 

Everything is beginning to come together now. Lets learn how to create a user account. Next Step.

## Step 20: Creating an ownCloud User

[ ![Picture of Creating an ownCloud User](http://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.MEDIUM.jpg) ](/file/FMC60Q0HKJRZI9I/)

Show All Items  
__

ownCloud has loads of features so it would take a whole lot of time to explain each one and how to use it. That my friends, is another instructable for another day. Have a look [here](http://owncloud.org/features/) for a list and usage.

Creating a user is _fairly*_ simple so I'll show you how.

Click the user options button in the top corner then click on Users from the dropdown.

Then you'll be taken to the user management page.

 

To create a new user, type a username and password into the appropriate boxes above the table view of current users.

 

Then click the groups dropdown box. 

 

Here you will see an admin entry and an _+add group_ entry.

Click _+add group_, then type a group name for standard user accounts. This only has to be done once.

 

Then press enter (Keyboard key). This will create and select the new group.

 

Next click the _create_ button.

Now we need to set the data limit for the user. Do this using the _Storage_ drop down on the row of the user. The top option sets the default.

 

Set to whatever meets your needs.

 

Once you have done all this, you've created your new user account. Logout (user button in top right > logout) then log back in as the new user to test things out.

Next, lets samba.

 

*The term fairly and any other reference to simplicity or difficulty throughout this instructable is subjective, however this instructable is intended for anyone who understands the basic operation of a PC, so most should be able to follow it. 

## Step 21: Let's all do the Samba

[ ![Picture of Let's all do the Samba](http://cdn.instructables.com/FAG/KR97/HKJRZI9G/FAGKR97HKJRZI9G.MEDIUM.jpg) ](/file/FAGKR97HKJRZI9G/)

Show All Items  
__

Samba will allow us to share documents with windows PC's on the same network. This will allow the server to be used as a central file server within your home. This is useful if you have more than one PC within the network.

Installation begins with opening the module from the Un-used modules category within webmin.

So go ahead and select _Samba Windows File Sharing_

 

You will then be told "Sorry Mr, you don't have that module," or something like that anyway. Just click __click here__ to install it_._

 

The package will then install.

 

The samba package and any other dependencies have been installed. Continue to the next step to set it up.

## Step 22: Configure Samba Drives

[ ![Picture of Configure Samba Drives](http://cdn.instructables.com/FAG/KR97/HKJRZI9G/FAGKR97HKJRZI9G.MEDIUM.jpg) ](/file/FAGKR97HKJRZI9G/)

Show All Items  
__

So now we'll setup ad configure the samba instance. Samba operates on the windows file share protocol, so integration into a windows network (or singular PC) is seamless.

First open up Samba from the servers category in webmin.

 

Next select the checker boxes along the left hand side of the default directory mounts.

 

Click the _delete selected drives _button located below the table. The page should now look like this:

 

Click _create a new file share._ to begin mounting your directories.

Here we can now define a name, and file location. We can also set permissions for samba users.

Create your share with the options:

Share name : Relevant share name of your choice

Directory to share: /media/serverhdd/* (here * is a wild card. Mount any folder of your choice. We've already created our cloud data folder so lets mount that.)

Directory to share: /media/serverhdd/cloud

Auto create directory: Yes

Owner: root

Permissions: 755

Group: Root

Available: Yes

Browseable: Yes

Add a share comment if desired. Then Click Create.

 

Here you can see the mounted drive. Mine is a users folder I created on the hard drive.

 

Now we need to edit an option. Click on the share you've just made. From there click the _Security access and control_ button from the bottom.

 

Here change the attribute _Writable?_ to _Yes_

 

Then Save.

 

Return to the samba config homepage, and continue until you have mounted all the shares you wish to add.

In the next step we will create a user so we can login to the shares via windows explorer.

 

## Step 23: Add a Samba User

[ ![Picture of Add a Samba User](http://cdn.instructables.com/FMC/60Q0/HKJRZI9I/FMC60Q0HKJRZI9I.MEDIUM.jpg) ](/file/FMC60Q0HKJRZI9I/)

Show All Items  
__

I often find the WebGUI for adding samba users to be buggy and unreliable. Because of this, I'm going to teach you to add a user the terminal way. 

First, a shellinabox session.

Before we continue it is important to note: to add a samba user there must be an exsisting Unix account that you can link to. The samba config will rely on the Unix user account for permissions. Name the samba user the same as the Unix user account.

Now type in pdbedit -a -u *username here*

 

Now you'll need to enter a password then confirm it.

 

Nice and Tidy. For changes to take effect, you'll need to restart the samba service. This is easily done via the GUI with the restart button ant the bottom of the page.

All done. Now Head over to your windows PC for the next part, _accessing the share. _  
Full details on the tool pdbedit are available [here](http://linuxcommand.org/man_pages/pdbedit8.html).

## Step 24: Accessing the share

[ ![Picture of Accessing the share](http://cdn.instructables.com/FUB/D1ON/HKJRZI9F/FUBD1ONHKJRZI9F.MEDIUM.jpg) ](/file/FUBD1ONHKJRZI9F/)

Show All Items  
__

Welcome back. 

Now lets mount the share as a volume in windows. Open up My computer.

Click Map network Drive. (Locations are as follows: Windows 8: top toolbar under Computer group. Windows 7: On the toolbar below the filepath. Windows Vista: Within the Tools... dropdown that is located on the toolbar below the filepath. Windows XP: Left click white space.)

 

First Specify the drive letter. All available ones will be within the dropdown.

Next location, Which will be in the format \\\\*your server name here\\*samba share name here*

Check the Reconnect at sign-in and Connect using different credentials options.

Click Finish.

 

The Credentials window will then open.

Here type the user name and password for samba.

Check the _Remeber_ option then finish.

 

Once that has been done, the share can be used like a normal storage media from within Windows.

 

 

Next we'll install Transmission.

 

 

## Step 25: Install Transmission (Bit Torrent)

[ ![Picture of Install Transmission \(Bit Torrent\)](http://cdn.instructables.com/FEY/I1Y4/HKJRZI9C/FEYI1Y4HKJRZI9C.MEDIUM.jpg) ](/file/FEYI1Y4HKJRZI9C/)

Show All Items  
__

Transmission is a torrent/download manager. You simply visit the port the service is running on to open the web UI. From there you can simply copy and paste URL magnet links, file links, torrent file links and more. The interface is super simple to use.

To install open up a shellinabox session and type: apt-get install transmission

This will begin the install.

Here we caan see the files being downloaded and added to the filesystem.

Once the package has installed, we need to stop the daemon (package) from running. This is important to do or the setting file may become corrupt.

Type: /etc/init.d/transmission-daemon stop to stop the daemon.

Next we need to configure the username and password for the instance. You'll use these credentials to login to the web user interface.

Type: nano /etc/transmission-daemon/settings.json to edit the config file with nano.

 

Edit the User and password enteries to whatever you wish. the password entry is named rpc-password and user is rpc-username. Hit shift and X to exit and press Y to save changes.

 

Next we will restart the daemon. Type: /etc/init.d/transmission-daemon start

 

Now visit 192.168.2.*:9091. Here you'll hit  login dialog. Enter the credentials and login.

After that, a sucsessful login will load the interface. Simply use the add file icon to pase a link for the manager to download. Again full usage guides are available on the trasmission website.

## Step 26: The Principal

[ ![Picture of The Principal](http://cdn.instructables.com/F94/RIUG/HKJRZI9B/F94RIUGHKJRZI9B.MEDIUM.jpg) ](/file/F94RIUGHKJRZI9B/)

Show All Items  
__

This step will explain how we will achieve worldwide access for the server.  
  
We will use two fundamental elements.  
  
The first: no-ip, is a free service available to anyone. It comes in two forms, the sync client and the online service account. The accounts are free from the no-ip website. Create an account [here](http://www.noip.com/newUser.php).  
  
The second element is a function built into almost all home routers: port forwarding. This function allows us to redirect incoming requests to other devices on the network, i.e., the server. This has to be done as any incoming connection from outside your home network will just direct us to the router management page. We need to land on our servers services page.  
  
To do this the two features work together to provide a simpler way to connect to the server.  
  
no-ip works like this:

  
Port forwarding works like this sketch:  
  

Continue to setup these tools.

## Step 27: Install no-ip

[ ![Picture of Install no-ip](http://cdn.instructables.com/FZ1/2CTL/HKJRZI9D/FZ12CTLHKJRZI9D.MEDIUM.jpg) ](/file/FZ12CTLHKJRZI9D/)

Show All Items  
__

To install no-ip, open a new shell session.

Type: cd /usr/local/src To make the current working directory (folder) _src._

 

Now download the tar file to the directory, from no-ip.com with: wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz

 

Change the cd (current directory) to no-ip folder using:  cd noip-2.1.9-1      Then make the files with: make

 

Then install with: make install

During the install you'll need your no-ip registerd email address and password to hand. Leave the default update period as 30.

When asked say no to running a script on sucsessful update, using N key.

Then login to no-ip.com to confirm the client carried out it's first update

Configure port forwarding on the next step.

## Step 28: Port Forwarding

[ ![Picture of Port Forwarding](http://cdn.instructables.com/FX1/7A38/HKJRZI9E/FX17A38HKJRZI9E.MEDIUM.jpg) ](/file/FX17A38HKJRZI9E/)

Show All Items  
__

Setting up port forwarding is different on every router, because of this i'll just give you a general idea of which ports to forward and where. For more specific details on your routers port forwarding feature (aka Virtual Hosts) visit [portforward.com](http://portforward.com/english/routers/port_forwarding/routerindex.htm). 

Okay so the basic idea is that you type in username.no-ip.biz:* and wind up at the service allocated for *. 

So we need to set this up for four instances: ownCloud, Transmission, Webmin and shell in a box.

The ports on the server (forward to private port) are as follows 

  * Webmin - Port 12321 
  * Owncloud - Port 80 (also requires /cloud or whatever sub directory you chosen earlier i.e. username.no-ip.biz:80/owncloud) 
  * Transmission - Port 9091 
  * Shell - Port 12320 

The incoming ports can be different to the outgoing ports, so you could have userame.no-ip.biz:1 leading to webmin, userame.no-ip.biz:2 leading to ownCloud and so on. This makes it more convenient to remember.

This means your port forwarding table should be filled out like the illustration below.

## Step 29: Final: Backup

[ ![Picture of Final: Backup](http://cdn.instructables.com/F4A/KZB9/HJGE1N7S/F4AKZB9HJGE1N7S.MEDIUM.jpg) ](/file/F4AKZB9HJGE1N7S/)

Show All Items  
__

Now we've almost finished. The final procedure is to unplug the power, remove the SD and create a back-up image of the OS in it's current state. This way if something goes wrong you have a basic fresh custom set-up to return to.

Simply place the SD card into a reader and open up win32diskimager.

In the text field type the location of the desktop followed by \backup.iso (something like this C:\Users\Dillon\Desktop\backup.iso). This will tell the software to read the file and save it to the desktop.

Then** instead** of write, click read.

This animated GIF shows a write taking place, but the process is the same.

This will take around 5-10 minutes. After it's done, put the SD back into the Pi and rest at ease. If you ever need to refresh your system (system restore) use the backup you created to write the ISO to the card, as in step 5. This means all will not be lost. For extra sense of peace, after any major system changes, perform a new backup and save it with a date. This way you'll have different revisions of backups to choose from.

## Step 30: Congratulations - Felicitaciones - Glückwünsche - 恭喜

[ ![Picture of Congratulations - Felicitaciones - Glückwünsche - 恭喜](http://cdn.instructables.com/F94/RIUG/HKJRZI9B/F94RIUGHKJRZI9B.MEDIUM.jpg) ](/file/F94RIUGHKJRZI9B/)

Show All Items  
__

Over 6,000 words and more than 170 illustrative diagrams and images later, we have reached _the_ end.

If you made it this far, well done. I hope you found it an awesome journey. The learning curve may have been steep, but i encourage you to fly from the nest and begin to lean more about the Linux world. 

 

If you have any issues or questions, drop one below. I hope you enjoyed reading and learning as much as I did writing.

 

###  Thank _you_.

Can I use a wifi dongle instead of Ethernet?

<p>What drive format would you recomend?<br></p>

<p>Could I use a RPi 2 instead of a model B? Thanks for the answers</p>

<p>Could I use a RPi 2 instead of a model B? Thanks for the answers</p>

<p>Hi, New owner of a RPI v2. and using MacOS. Trying to follow the instructions &quot;This will allow us to burn an operating system image to our SD card.</p><ul><br><li>Next download the ISO of the Raspian Turnkey mix from <a href="https://github.com/downloads/ghoulmann/Raspliance-Core/raspliance-core-02.img.tar.gz" rel="nofollow">here</a>. <tt>Credit to </tt><tt><a href="http://gonzotech.tumblr.com/post/35816630624/server-core-for-raspberry-pi" rel="nofollow">Ghoulmann</a> for the image.&quot;</tt></ul><p>Used dd command to burn to new mico sdd. sudo dd bs=2m if=/Users/robbab2/Downloads/Installers/RPI/raspliance-core-02.img of=/dev/rdisk3</p><p>it creates two partitions: one &quot;untitled&quot; and one &quot;disk3s2&quot; Looks like untitled is MS-FAT 16 and disk3c2 is linux. Whats up and PI can't read?</p><p>Thank you for your Answer.</p><p>wc</p>

<p>you can go <a href="http://www.aakeys.com" rel="nofollow"> www.aakeys.com </a> to get good windows, it is genuine and cheap</p>

<p>Am i able to run this server alongside my existing vpn server on the same raspberry pi?</p>

<p>Any one with issues to access OwnCloud due to permissions, here's the code I had to use. (Using HDD formatted to ext4)</p><p>sudo chmod 770 /media/serverhdd/cloud</p><p>chown www-data:www-data /media/serverhdd/cloud</p>

<p>Okay I have been at this for two day, I changed the partition from ntfs to fat32 to eventually ext4 (so that permissions existed by default) but STILL can not get one cloud to work! it keeps telling me that :&quot;</p><p>Data directory (/media/serverhdd/cloud) not writable by ownCloud<br><br> <br> <br></p><p>Permissions can usually be fixed by giving the webserver write access to the ownCloud directory&quot;</p><p>For the love of God, please someone help me this is causing me to go insane</p>

<p>Hi, you have to change the permissions for the 'www-data' user, not 'root'.</p><p>If chown doesn't work (as mine didn't), change the '/etc/fstab' file to add the options to the automatic mout. I found good informations in here:</p><p><a href="http://www.linux.com/learn/tutorials/309527-understanding-linux-file-permissions" rel="nofollow">http://www.linux.com/learn/tutorials/309527-unders...</a></p><p><a href="http://askubuntu.com/questions/223016/setting-permission-for-ntfs-partition" rel="nofollow">http://askubuntu.com/questions/223016/setting-perm...</a></p><p>You can get the correct 'gid' and 'uid' typing 'id www-data' in the terminal</p><p>Mine is working properly now.</p><p>I hope it helps!</p><p><br></p>

<p>VERY well done. I have some friends planning their first foray into Raspberry Pi, and Linux in general as a result of this article.<br><br>I have a serious concern though: I would strongly encourage y'all to keep TLS/SSL *ON* -- especially if you plan to turn on port-forwarding on your routers (step 27), thereby exposing your server to the public internet -- and all that comes along with it (individual and state-sponsored hackers). Even the self-signed certificate, with the accompanying initial error prompt, is far better than having none at all (at least you're encrypted -- if not properly validated); and if you want a fully legitimate and validated TLS/SSL certificate, a basic one is NOT expensive -- unless you consider $9.99/year expensive (see NameCheap's Comodo PositiveSSL certificate) in which case I'd question what such a person is doing buying a Pi to begin with. Also, keep an eye on &quot;<a href="https://letsencrypt.org" rel="nofollow">https://letsencrypt.org&quot; </a> which aims to make TLS/SSL ubiquitous and free, automated, and open.<br><br>These instructibles are *great* but when it comes to technology -- especially internet-connected technology -- it's on YOU to educate yourselves instead of blindly following a set of instructions.<br><br>Have FUN... just keep your digital condom (TLS/SSL) on while doing it.</p>

<p>One of the best articles I ever seen on internet. Congratulations ... sorry my english.</p>

<p>I'm confused on the Users comment about needing a unix account to match for samba. Where am i creating these accounts? I've got 5 people in the house that will be accesing this.</p>

You forgot to mention to unpack the tar.gz file. <br>After downloading type: <br>tar xzf noip-duc-linux.tar.gz <br> <br>After this you can continue with the tutorial. <br>

<p>thanks</p>

<p>Hey guys, signed up here to be able to comment and hopefully help people out. I just followed this guide and am up and running smooth now, but it involved pulling information from a lot of various resources. So, first and foremost, I don't take credit for all of this. Some helpful information I found while digging through everyone one of these comments, and some I found through hours of consulting Google.</p><p>For everyone's information, I am running a Raspberry Pi 2.</p><p>To start, getting the image on the SD card, I followed this:<br><a href="http://www.instructables.com/id/Raspberry-PI-THE-HOME-SERVER-TURNKEY-LINUX/" rel="nofollow">http://www.instructables.com/id/Raspberry-PI-THE-H...<br></a>Which has a link to download the Raspbian image itself from the official site. To write the image to the SD card, however, I used the image writing software mentioned in this guide, then continued with the instructions in the link above to get it running Turnkey Linux. You will get the # UNCONFIGURED INTERFACES error mentioned at the bottom of the guide on the above link. To fix it, I read online about how to make an interfaces file for Linux. Mine is as follows:</p><p># UNCONFIGURED INTERFACES</p><p>auto lo</p><p>iface lo inet loopback</p><p>auto eth0</p><p>iface eth0 inet static</p><p> address 192.168.x.x</p><p> netmask 255.255.255.0</p><p> gateway 192.168.x.x</p><p>Then I reran the tklpatch-apply / ./core/ command that generated this error and all went well.</p><p>Then, I came back to this guide and picked up on step 7, which is updating Webmin. By default, Webmin is not set to start on boot, which means you have to run sudo service webmin start to get it up and running, so you can access on port 12321 (192.168.x.x:12321).</p><p>In regards to shellinabox, the default port is 4200, not 12320 (at least for the Turnkey image that we loaded onto our SD card with the instructions I mentioned above)</p><p>Everything else went well, actually. I am loving the functionality of my Pi. If anyone is interested, you can also set up a VPN, which is pretty nifty itself. The guide I followed to do this is:<br><a href="http://readwrite.com/2014/04/10/raspberry-pi-vpn-tutorial-server-secure-web-browsing" rel="nofollow">http://readwrite.com/2014/04/10/raspberry-pi-vpn-t...<br></a>I use it to encrypt my sensitive internet traffic as well as to access my home network's shared drive that contains data that I do not want accessible via the internet.</p><p>I hope this was able to help some of you! I saw some of the more recent comments, so it motivated me to write this.</p>

<p>Thanks jaxpr3394. I could not get the image given in this post written on my card. Then I followed your comment. And it was a breeze. However, I faced problem at the &quot;Updating webmin&quot; step. There was warning that &quot;the program <a href="https://192.168.1.15:12321/webmin/edit_referers.cgi" rel="nofollow">https://192.168.1.15:12321/webmin/edit_referers.cgi</a> was linked to from an unknown URL, which appears to be outside the Webmin server.&quot; Even editing from the config module gave the same message. What I did was,</p><p>&gt; edit the /etc/webmin/config file with &quot;vi /etc/webmin/config&quot; command.<br>&gt; Find the line referers_none=1 and change it to referers_none=0.<br>&gt; Save the file and restart webmin.</p><p>(for new linux users, this is how you edit files in command line: https://www.howtoforge.com/faq/how-to-edit-files-on-the-command-line)</p>

<p>THANK YOU!!! I've got to try this with a Pi 2 that I have for testing but which of course wouldn't run the pre-built image.</p>

<p>You are some kind of saint. I just started this project today and had to follow your instructions here to get things running. Muchly appreciated.</p>

<p>Great! I am glad I could help someone else and save from the headaches I faced. Thank you again for the creator of the guide itself as well as all of the resources I pulled from!</p><p>Enjoy.</p>

<p>I forgot to mention, you can also enable SSL following this guide:</p><p><a href="https://hallard.me/enable-ssl-for-apache-server-in-5-minutes/" rel="nofollow">https://hallard.me/enable-ssl-for-apache-server-in...</a></p><p>Also, I just realized that you could format your text in these comments, I apologize for the poor formatting of my previous post.</p>

<p>After running without problems for a long time, suddenly Shellinabox doesnt recognize/accept my password anymore. Still can log in through Webmin so the password is ok.<br>When i make new user with a known password or even without a password, the problem still persistst. Anybody having any idea what is wrong?</p>

<p>Same problem. Can anyone tell my why I can use my password in webmin or ssh but not in shell in a box?</p>

<p>I still haven't found an answer. I have just done a complete new install of raspbian and separately installed webmin, apache, php, mysql.<br>Shellinabox seems to be the only terminal available and will try to install that too once I found a decent source.<br>at least it brings webmin back to port 10000 as it is with my other linux systems</p>

<p>Perhaps it is the keyboard locale settings on the pi? I've run into that problem before, where everything seemed to type as I wanted it to, with the exception of a few of the special characters (@#$) and it was due to the keyboard locale settings. Just a thought.</p>

<p>thanks but i doubt it as all my other passwords still worked and the problem with shellinabox happened on all computers.<br>Thanks for yr suggestion though</p>

<p>just a general tip.<br>using the dns name of the raspberry (or any other computer) in your browser to go to a webpage on the raspberry or to go to webmin or shellinabox, such as e.g.<br><a href="http://raspberrypi:12321" rel="nofollow">http://raspberrypi:12321 </a> doesnt always work and your browser may insist that actually you mean &quot;www.raspberrypi.com:12321&quot;. Having to use the internal 192.168.x.yyy address is a a drag<br>However if you do &quot;raspberrypi.local:12321&quot; it always seems to work</p>

<p>This will only work if you are running Mac or Linux, or if you are running Windoze and have iTunes installed. (Apple wrote their own mDNS client for the Windoze version of iTunes (which they call Bonjour), which gets installed when you install iTunes.) Also, you might need to add .local to the end of the address depending on how your router is set up, like http://raspberrypi.local:12321.</p>

<p>yes http://raspberrypi.local:12321 is what i suggested. It works on my windows and I do not have iTunes</p>

<p>What browser and Windows version are you using, and have you ever had any Apple software installed? Also, using Ubuntu and Chromium, for me http://raspberrypi:12321 NEVER works, even if I make sure to go to that actual address. It always gives &quot;DNS_PROBE_FINISHED_NXDOMAIN&quot;. The only way that could possibly work is if your router's configured in a specific way.</p>

<p>windows 10 using chrome, edge IE and firefox.<br>Ubuntu12.04 with firefox<br>Did never get the error you mentioned.<br>did not configure my router in any specific way<br>never downloaded Apple softwar</p>

<p>Hey guys, I have a quick question about ownCloud. Downloading and installing it shows version 4.0.4 in the ownCloud dashboard and running an apt-get update and apt-get upgrade does not detect anything newer, but version 8 is currently out. Can anyone shed any light on how to go about upgrading from 4.0.4? I would prefer not to have to start over with it and would gladly upgrade step by step until I get to the latest version if that is what it takes.</p>

<p>Disregard, I was having a moment. I just went to their Web site and found the answer that I was looking for by using the oBS method mentioned. For anyone else that is going to do that - when I first did it, it gave me a 404 error when trying to access /owncloud. To fix it, I just ran the sudo apt-get purge owncloud command, which removed (I am assuming) some of the files of the second installation that resulted from the oBS method. When I did this, it was up and running with the newest version. Strange and I know I could understand it better if I put the time into the research, but I haven't had a chance to as of yet, but I just wanted to let anyone else know that was curious about upgrading from 4.0.4 to 8.1.1. :)</p>

<p>hey drwilson i'm done with it thanks for the steps and the idea this is mine project</p>

<p>This step didn't work for me initially, but once I set &quot;rpc-whitelist-enabled&quot; to false it worked perfectly.</p>

<p>Thanks for the info!</p>

<p>Hey. I'm kinda having a problem with </p><p>/etc/init.d/transmission-daemon stop</p><p>All I get is</p><p>-bash: /etc/init.d/transmission-daemon: No such file or directory </p><p>and when I try to access </p><p>nano /etc/transmission-daemon/settings.json</p><p>It's just blank </p><p>Can someone please enlighten me :) </p>

<p>Ran into the same problem, Elliot. Uninstall the package by running</p><p>apt-get remove transmission</p><p>Then, run</p><p>sudo apt-get install transmission-cli transmission-common transmission-daemon</p><p>That should do the trick. If not, let me know!</p>

<p>Thanks man!</p>

<p>Yeah it worked. Thank you so much Garrett :) </p>

<p>Not a problem, Elliot!</p>

Thanks man I'll give that a try and let you know ?

<p>I had some &quot;failed to mout bla bla bla&quot;... error<br>The solution was found in:<br>https://www.raspberrypi.org/forums/viewtopic.php?t=74776&amp;p=536000</p>

<p> i've been looking for a good server set up for the raspberry pi for a while now and I really like the looks of this one! Made it to step eight no problem but now when I try to start the Shell from a browser I can't connect to it. I can connect to Webmin just fine in the browser but not to the Shell. Any help would be appreciated. </p>

<p>Well, there were a couple stumbles along the way, and an important item or 2 left out, but I've gotten it working now. Thank you so much!</p>

<p>the monitor cannot detect i</p>

Can you make a tutorial on how to make a box for it?!

Very good

__More Comments

### About This Instructable __

__ 1,050,445 views

__ 3,497 favorites

**License:**  
![](/intl_static/img/license/by-nc-nd_small.png)

![DrWilson profile picture](http://cdn.instructables.com/F5O/JBVC/H9G16IFS/F5OJBVCH9G16IFS.SQUARE.jpg)

[DrWilson](/member/DrWilson/) Follow 411

**Bio:** Student. Usually I'm making things - electronics, computer programming, woodwork, DIY and all things awesome.! 

**More by DrWilson:** ![Ultimate Raspberry Pi Home Server](http://cdn.instructables.com/FVQ/YDJS/HKPXB5RM/FVQYDJSHKPXB5RM.SQUARE2.jpg) ![The Box Short Film](http://cdn.instructables.com/F8D/CUK5/HBXWSRD7/F8DCUK5HBXWSRD7.SQUARE2.jpg) ![Extreme Loft Conversion](http://cdn.instructables.com/F5K/RWJ3/GZACJ7BU/F5KRWJ3GZACJ7BU.SQUARE2.jpg)

**Tags:** [raspberry pi](/tag/type-id/keyword-raspberry%20pi/) [server](/tag/type-id/keyword-server/) [linux](/tag/type-id/keyword-linux/) [cheap server](/tag/type-id/keyword-cheap%20server/) [cloud](/tag/type-id/keyword-cloud/) [port forwarding](/tag/type-id/keyword-port%20forwarding/) [terminal](/tag/type-id/keyword-terminal/) [diy](/tag/type-id/keyword-diy/) [learn](/tag/type-id/keyword-learn/) [basic](/tag/type-id/keyword-basic/) [easy](/tag/type-id/keyword-easy/) [owncloud](/tag/type-id/keyword-owncloud/) [ssh](/tag/type-id/keyword-ssh/) [samba](/tag/type-id/keyword-samba/) [webmin](/tag/type-id/keyword-webmin/) [media](/tag/type-id/keyword-media/) [nas](/tag/type-id/keyword-nas/) [raspberry](/tag/type-id/keyword-raspberry/) [ultimate](/tag/type-id/keyword-ultimate/) [home](/tag/type-id/keyword-home/) [office](/tag/type-id/keyword-office/) [apache](/tag/type-id/keyword-apache/) [sql](/tag/type-id/keyword-sql/) [database](/tag/type-id/keyword-database/) [web](/tag/type-id/keyword-web/) [gui](/tag/type-id/keyword-gui/) [cms](/tag/type-id/keyword-cms/)

**Add instructable to:**

__ Contest __ Group

### Related

  * [ ![Raspberry PI, THE SERVER \(TURNKEY LINUX\)](http://cdn.instructables.com/F0C/DMNO/I169RBX2/F0CDMNOI169RBX2.SQUARE2.jpg) ](/id/Raspberry-PI-THE-HOME-SERVER-TURNKEY-LINUX/)

[Raspberry PI, THE SERVER (TURNKEY LINUX)](/id/Raspberry-PI-THE-HOME-SERVER-TURNKEY-LINUX/)  
by [MortezaP](/member/MortezaP/)

  * [ ![FerretPi: Using Raspberry Pi as a Secure FTP Server](http://cdn.instructables.com/FY4/DNTD/HR0AQB24/FY4DNTDHR0AQB24.SQUARE2.jpg) ](/id/FerretPi-Using-Raspberry-Pi-as-a-Secure-FTP-Server/)

[FerretPi: Using Raspberry Pi as a Secure FTP Server](/id/FerretPi-Using-Raspberry-Pi-as-a-Secure-FTP-Server/)  
by [CHaynes2013](/member/CHaynes2013/)

  * [ ![Raspberry Pi Video Streaming](http://cdn.instructables.com/FPW/G5PC/IDUR8FIR/FPWG5PCIDUR8FIR.SQUARE2.jpg) ](/id/Raspberry-Pi-Video-Streaming/)

[Raspberry Pi Video Streaming](/id/Raspberry-Pi-Video-Streaming/)  
by [JoseBarreiros](/member/JoseBarreiros/)

  * [ ![Python Web Server for your Raspberry Pi](http://cdn.instructables.com/FX1/N3R7/I7XR7Y52/FX1N3R7I7XR7Y52.SQUARE2.jpg) ](/id/Python-Web-Server-for-your-Raspberry-Pi/)

[Python Web Server for your Raspberry Pi](/id/Python-Web-Server-for-your-Raspberry-Pi/)  
by [knexpert1700](/member/knexpert1700/)

  * [ ![Personal ARM Cloud Server](http://cdn.instructables.com/FG6/TW8S/H5EDUDJD/FG6TW8SH5EDUDJD.SQUARE2.jpg) ](/id/Personal-ARM-Cloud-Server/)

[Personal ARM Cloud Server](/id/Personal-ARM-Cloud-Server/)  
by [greenyouse](/member/greenyouse/)

FEATURED CHANNELS

  * [

Woodworking

](/tag/type-id/category-workshop/channel-woodworking/)

  * [

CNC

](/tag/type-id/category-technology/channel-cnc/)

  * [

Arduino

](/tag/type-id/category-technology/channel-arduino/)

  * [

Intel IoT

](/id/intel/)

  * [

Indoor Gardening

](/howto/indoor+gardening/)

  * [

Lighting

](/tag/type-id/category-workshop/channel-lighting/)

  * [

Sewing

](/tag/type-id/category-craft/channel-sewing/)

  * [

Parties

](/tag/type-id/category-craft/channel-parties-and-weddings/)

  * [

Star Wars

](/howto/star+wars/)

![robot](/static/img/footer/footer-robot.png)

### Newsletter

Join 2 million + to receive instant inspiration in your inbox.

I'm in!

### Mobile

Download our apps!

  * [Android »](https://play.google.com/store/apps/details?id=com.adsk.instructables)
  * [iOS »](https://itunes.apple.com/app/instructables/id586765571)
  * [Windows »](http://apps.microsoft.com/windows/en-us/app/7afc8194-c771-441a-9590-54250d6a8300)

### About Us

  * [Who We Are](/about/)
  * [Advertise](/advertise/)
  * [Contact](/about/contact.jsp)
  * [Jobs](/community/Positions-available-at-Instructables/)
  * [Help](/id/how-to-write-a-great-instructable/)

### Find Us

  * [Facebook](http://www.facebook.com/instructables)
  * [Youtube](http://www.youtube.com/user/instructablestv)
  * [Twitter](http://www.twitter.com/instructables)
  * [Pinterest](http://www.pinterest.com/instructables)
  * [Google+](https://plus.google.com/+instructables)
  * [Tumblr](http://instructables.tumblr.com)

### Resources

  * [For Teachers](/teachers/)
  * [Artists in Residence](/air)
  * [Gift Pro Account](/account/give?sourcea=footer)
  * [Forums](/community/)
  * [Answers](/tag/type-question/?sort=RECENT)
  * [Sitemap](/sitemap/)
* * *
  * [Terms of Service](http://usa.autodesk.com/adsk/servlet/item?siteID=123112&id=21959721)|
  * [Privacy Statement](http://usa.autodesk.com/adsk/servlet/item?siteID=123112&id=21292079)|
  * [Legal Notices & Trademarks](http://usa.autodesk.com/legal-notices-trademarks/)|
  * [Mobile Site](http://m.instructables.com)
  * ![autodesk](/static/img/footer/autodesk-logo.png)

© 2015 Autodesk, Inc.

x

### login

Facebook Google+ Twitter Autodesk

OR

Login

![go pro for discounts](/static/img/gopro/go-pro-login1.png)

![go pro to remove ads](/static/img/gopro/go-pro-login2.png)

![go pro to download pdfs](/static/img/gopro/go-pro-login3.png)

![go pro to download ebooks](/static/img/gopro/go-pro-login4.png)

[Sign Up »](/account/register/) [Forgot Username/Password »](/account/forgot/)

x

### forgot?

Forgot your username or password?   
It happens.

Enter the email associated with your account and we will send you your username and a temporary password.

Send it now, please!

Not a member? [Sign Up »](/account/register/)

x

### reset password

We have sent you an email with a password reset code. Please enter it below.

Reset and Sign In

Not a member? [Sign Up »](/account/register/)

x

### go pro

that's a pro feature! want to go pro?

[I want to go pro!](/account/gopro/) No thanks

Already a member? [Login »](/account/login/)

x

### go pro

That's a pro feature!

Want to go pro?

First step is to sign up.

Facebook Google+ Twitter Autodesk

OR

By clicking "Sign me up!" you are indicating that you have read and agree to the [Terms of service.](http://usa.autodesk.com/adsk/servlet/item?siteID=123112&id=21959721)

Sign me up!

Already a member?" [Login »](/account/login/?sourcea=goproSignupModal&nxtPg=/id/Ultimate-Pi-Based-Home-Server/%3FALLSTEPS))
