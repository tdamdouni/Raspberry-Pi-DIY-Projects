# Hands on with the AIY Projects Voice Kit

_Captured: 2017-11-09 at 23:06 from [medium.com](https://medium.com/@aallan/hands-on-with-the-aiy-projects-voice-kit-7c810856faaf)_

# Hands on with the AIY Projects Voice Kit

## Machine Learning on a Raspberry Pi is now available for pre-order!

In the closing days of 2015 the Raspberry Pi Foundation did something unprecedented, they [gave away a computer](https://www.raspberrypi.org/magpi/issues/40/) on the front cover of a magazine.

Growing up, the free toys on the covers of magazines were made of plastic. They were cheap, and cheerful. Yet the last thirty years has [reduced the price of computing](https://medium.com/@aallan/capable-computing-50867847a8d8) to the point where cheap and cheerful plastic toys have been replaced by a computer, one powerful enough that it would have been amongst the fastest super-computers on the planet back then.

Two months ago, along with Google, they did it again. This time it [was a project kit](https://www.raspberrypi.org/magpi/google-aiy-voice-magpi-57/) that let you add voice interaction to your Raspberry Pi. Together they packaged machine learning, and the ability for a machine to think and reason, free on the cover of a magazine. Well not quite the cover, they had to put the magazine into a box. But I guess it's the thought that counts.

The magazine sold out in hours, and everyone that missed out on getting one [has been waiting](https://www.raspberrypi.org/magpi/buy-aiy-projects-voice-kit/) to see if there would be another run of the kit. Today we found out that there will be, and it has just been **made available for ****[pre-order at Micro Center**](http://www.microcenter.com/site/content/Google_AIY_Preorder.aspx?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder). It'll be available for pre-order from them, and then should be available for sale from them--and their resellers--when it hits shelves in October, and after that there could well be more kits to come.

> "The positive reception to Voice Kit has encouraged us to keep the momentum going with more AIY Projects. We'll soon bring makers the 'eyes,' 'ears,' 'voice' and sense of "balance" to allow simple, powerful device interfaces."_ -- __[Google_](https://www.blog.google/topics/machine-learning/aiy-voice-kit-inspiring-maker-community/)_._

![](https://cdn-images-1.medium.com/max/1600/1*F_8tRGDehVKT-uLXmwiL-A.jpeg)

> _Issue 57 of the MagPi, and the Google AIY Projects Kit._

I managed to [pick up a copy](https://twitter.com/aallan/status/860402482756943877) of the magazine when it came out, but the kit has sat on my shelf ever since. However, ahead of today's preorder announcement, it was very much time to take it out the box and put it together.

#### Opening the Box

Inside of the box there is [issue 57 of the MagPi](https://www.raspberrypi.org/magpi-issues/MagPi57.pdf), and underneath the magazine is the kit itself. I've been told that the kits arriving on the shelves will come in a similar looking cardboard box. It's just this time around, there won't be a magazine.

![](https://cdn-images-1.medium.com/max/1600/1*SUwlRJEdjQkxcOVf7MIvzQ.jpeg)

> _Contents of the box._

The kit consists of a voice HAT board that'll connect directly to the GPIO header of your Raspberry Pi, a microphone add-on daughter board, a speaker, a (disassembled) big arcade button, and a variety of wires and headers.

![](https://cdn-images-1.medium.com/max/1600/1*41H5XFGFJ_gZ8TalG7mr0w.jpeg)

> _The AIY Voice Kit._

Finally there's also a cardboard case for the project build which, after [Google Cardboard](https://vr.google.com/cardboard/), has become almost synonymous with Google's own prototyping efforts.

![](https://cdn-images-1.medium.com/max/1600/1*6M9px4zyZiJkucBBv9aDFA.jpeg)

> _The cardboard case included with the Voice Kit._

All you need to provide is a Raspberry Pi 3. Although if you don't have one, the kit should also work with a Raspberry Pi 2 or a Raspberry Pi Zero.

#### Gathering your Tools

For this project all you'll need is a small Philips "00" watch maker's screwdriver, some scotch tape (aka sellotape), and possibly a craft knife or scissors. No soldering is required to build the main part of the project.

#### Getting Ready

Grabbing a fresh Raspberry Pi 3 and [a power supply](https://www.raspberrypi.org/magpi/power-supply/) off the shelf, I went ahead and made a couple of the standard tweaks that I almost always do before starting a project with the Raspberry Pi. Both of them are small things, but it's all about quality of life.

![](https://cdn-images-1.medium.com/max/1200/1*5eDRjWuDBDztjSSv-0FUtQ.jpeg)

> _Raspberry Pi 3 with a small passive heat sink._

It might be unnecessary, but since the discovery of possible [thermal problems](http://makezine.com/2016/03/02/raspberry-pi-3-not-halt-catch-fire/) with the Raspberry Pi 3 when under heavy loads, I tend to add a [small passive heatsink](https://www.digikey.com/product-detail/en/wakefield-vette/624-25ABT4E/345-1098-ND/1099044). Also, since I rarely go to the trouble of using a case I also normally add [rubber bumper feet](https://www.adafruit.com/product/550) underneath the Pi. They're cheap, and with components on the bottom, they make for a more stable build platform.

#### Burning the Card Image

The [magazine](https://www.raspberrypi.org/magpi-issues/MagPi57.pdf) has a fairly detailed walkthrough for putting the kit together, but the new kit won't have the magazine. Fortunately Google also has put together [an assembly guide](https://aiyprojects.withgoogle.com/voice/#assembly-guide), and their claim is that the whole project can be put together in around an hour and a half.

![](https://cdn-images-1.medium.com/max/1200/1*goIhcOvHjP8RWNf6aY-yRw.jpeg)

> _An 8GB micro SD Card with adaptor._

The first thing you need to do is grab [a micro SD Card](http://amzn.to/2iAtPda). You'll need one that's at least 8GB, and despite the added cost it's a good idea to get a named brand high speed card. Because like power supplies, there really are [big differences](http://www.pidramble.com/wiki/benchmarks/microsd-cards) between the seemingly identical cards. Choosing [the wrong one](http://www.makeuseof.com/tag/5-mistakes-avoid-buying-next-microsd-card/) can mean long access times or even a card that just doesn't work or fails quickly under normal use.

While Google has already had open APIs and SDKs available to use their Voice Assistant service, the image is a preconfigured Raspbian distribution that means a much reduced amount of setup, so go ahead and download the Voice Kit [card image](https://dl.google.com/dl/aiyprojects/voice/aiyprojects-latest.img.xz).

These days I'd generally recommend [Etcher](https://etcher.io/), made by the folks at [Resin.io](https://resin.io/), for [burning card images](https://www.raspberrypi.org/documentation/installation/installing-images/README.md). It's cross platform--it works on Windows, Linux and mac OS--and lets you burn an image in four clicks.

![](https://cdn-images-1.medium.com/max/1200/1*TyYpL1a4IZZPhbYxatK62w.png)

> _Burning the aiyprojects-2017-05-03.img.xz card image using Etcher._

But if you're a command line person like me you can either download and install the [experimental Etcher command line tools](https://etcher.io/cli/), or you can do it the old fashioned way.

The instructions here are for the Mac, because that's what I have on my desk, but instructions [for Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md) are similar.

Go ahead and insert the micro SD card into the adaptor, and the card and the adaptor into your Macbook. Then open up a Terminal window and type `df -h`, and remember the device name for your SD Card. In my case it's `/dev/disk1`, and we'll need to use the corresponding raw device, `/dev/rdisk1`.

Go ahead and unmount the card from the command line,
    
    
    **$ **sudo diskutil unmount /dev/disk1s1

rather than ejecting it by dragging it to the trash. Then we can go ahead and install the card image. Unfortunately there isn't a command line tool to uncompress `.xz` files available by default on macOS. However if you have [Homebrew](https://brew.sh) installed, you can `brew install` the [xz command line tool](http://brewformulas.org/Xz).
    
    
    **$** brew install xz  
    **$** xz -d aiyprojects-2017-05-03.img.xz

Then in the Terminal window change to the directory with your downloaded disk image and type,
    
    
    **$** unzip 2017–01–11-raspbian-jessie-lite.zip  
    **$** sudo dd bs=1m if=2017–01–11-raspbian-jessie-lite.img of=/dev/rdisk1

if the above command reports an error `dd: bs: illegal numeric value`, change `bs=1m` to `bs=1M`. The card should automatically remount the image's boot partition, when `dd` is done, but if it doesn't--or you've used Etcher to image the card--you'll need to open Disk Utility and remount the boot partition. Or alternatively you can just pull the card out, and reinsert it, which should mount the boot partition automatically.

We need the card mounted because recent releases of the Raspbian operating system have the SSH server [disabled on boot](https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/), and since we're intending to run the board without a monitor or keyboard, we need to renable it. Make sure the partition is mounted and navigate to the boot partition,
    
    
    **$** cd /Volumes/boot  
    **$** touch ssh  
    **$** cd ~

The contents of the `ssh` file don't matter. When the Pi first boots, it looks for this file; if it finds it, it will enable SSH and then delete the file.

Eject the card with the command,
    
    
    **$** sudo diskutil eject /dev/rdisk1

and you should have a working card image.

#### Assembling the Voice HAT

The [first thing you need to do](https://aiyprojects.withgoogle.com/voice/#assembly-guide-2-assemble-the-hardware) is grab the two plastic spacers that come with the kit. They're not strictly necessary, but they're going to add a lot of stability. The Raspberry Pi has four mounting holes, the two spacers go into the holes furthest from the header block.

Once both spacers are in place push the Voice HAT down onto the Raspberry Pi headers, making sure there isn't a gap and it sits firmly on the Pi. You should then be able to snap the two spacers into the HAT. Afterwards the entire thing should be pretty solid without any flex.

![](https://cdn-images-1.medium.com/max/1600/1*o_ZIaGgufMTrSl_sK0dPeg.jpeg)

> _The Voice HAT on top of a Raspberry Pi 3, one of the plastic spaces is visible at the bottom (left of center)._

Next we need to attach the speaker, this should have a red and a black wire. The wires goes into the screw terminals on top of the shield, with the red wire going to the terminal labelled with a + sign, the one furthest from the Ethernet and USB sockets.

![](https://cdn-images-1.medium.com/max/1600/1*7CnCdo23OzNlgW3p8yEzZQ.jpeg)

> _Attaching the speaker, the +ve (red) wire goes furthest away from the Ethernet and USB sockets._

Once inserted screw them down and give them a gentle tug to make sure they're not going anywhere.

Next we need to attach the wiring harness. There are two cables in the kit, the first has a white 4-pin plug on one else and is terminated with individual metal contacts at the other. This is the wiring for the arcade button.

The other cable has two white 5-pin plugs, one at each end. This is the wiring for the small thin daughter board labelled "Voice HAT Microphone."

![](https://cdn-images-1.medium.com/max/1600/1*aXfYeoI6n8L1O19405RZYg.jpeg)

> _Plugging the two cables into the Voice HAT._

Go ahead and plug both of these cables into the Voice HAT board. Each of the sockets on the HAT have two cut outs on one side, these cut outs correspond to raised ridges on the plugs. In other words, there's only one way around to insert the cables, if you're doing it right they should slot into place with almost no force. If you're having to force them into the sockets, they're probably the wrong way around.

![](https://cdn-images-1.medium.com/max/1600/1*tX-nXzI7IYE2zZYCrSoj5w.jpeg)

> _Plugging the other end of the cable into the Voice HAT Microphone daughter board._

Now go ahead and connect the microphone board to the other end of the 5-pin cable. The socket and plug again have cut outs and ridges, so again there's only one way to attach it.

#### Building the Cardboard Box

The cardboard case to hold the Voice Kit comes in two parts, and outer box, and an inner frame, and while it might look like a nightmare of origami, or worse yet Ikea flat-packed furniture it's not too hard to construct if you follow [the instructions](https://aiyprojects.withgoogle.com/voice/#assembly-guide-3-1--build-the-box).

![](https://cdn-images-1.medium.com/max/1200/1*1mXpSs308YA2KHHds9mGpA.jpeg)

> _Folding down the the four flaps, the final flap tucks into the slot on the first flap._

The outer box is the larger of the two cardboard pieces, and by far the simpler of the two to put together.

Fold along the creases, and then fold the numbered flaps over one at a time.

The fourth flap tucks neatly into the slot in the first and forms the bottom of the case.

![](https://cdn-images-1.medium.com/max/1200/1*lzXUESP0d3hMSWCVmURImQ.jpeg)

> _The inner frame form a U-shape to hold the speaker, with three flaps to hold the Pi._

Unfortunately the inner frame, while not exactly tricker to put together, certainly is a bit more fiddly.

Fold the two flaps labelled "1" and "2" inwards, and then push the U-shaped cut out through and out.

Then fold the rest of the flap outwards, and the "fold up" tab so that it's flat against the desk.

At this point, the cardboard will not hold its shape. Don't worry, it'll mostly come together once it's inside the box.

Grab the hardware and slide the speaker into the U-shaped pocket on the frame, then take the Raspberry Pi and Voice HAT and slide it into the bottom of the frame below the two flaps--with flap "2" sliding just behind the the USB/Ethernet port end of the Pi.

![](https://cdn-images-1.medium.com/max/1600/1*l1JJiuzeMAkXYry04Rj_Yw.jpeg)

> _The hardware inside the frame._

With the Raspberry Pi and speaker inside the frame it should be a lot more stable, enough so that you can insert the whole thing inside the outer box. Make sure the the speaker faces the side of the box with the seven speaker holes.

![](https://cdn-images-1.medium.com/max/1600/1*dIZ3egE2n3yR-W-KJf56Lw.jpeg)

> _Inserting the frame into the box._

If you've already inserted your micro SD Card into the Pi, remove it before sliding the hardware into the cardboard as you stand a good chance of breaking something -- the box, the card, or perhaps even the Pi -- if you don't as there isn't room for it until the Raspberry Pi is in place.

![](https://cdn-images-1.medium.com/max/1600/1*VmtRA0RZry1RkpSsSjkSsA.jpeg)

> _All the ports of the Raspberry Pi should be accessible via the cut outs on the sides of the box._

Once everything is in it should all be fairly stable with the Raspberry Pi sitting on the bottom of the box, and you should be able to see all the ports through the various cut outs around the base of the box.

![](https://cdn-images-1.medium.com/max/1200/1*T8XyKxaXJECeNacC3dCLoA.jpeg)

> _The arcade button._

Now we need to assemble our arcade button. The button shell consists of the button itself, a spacer, and a nut.

Unscrew both the spacer and the nut and insert the button into the top flap of the box.

![](https://cdn-images-1.medium.com/max/1200/1*tXuKst5IPaN2j0JwHFp6EQ.jpeg)

> _Inserting the button into the pre-cut hole in the box lid._

Thread the spacer back onto the button and then screw it firmly in place with the nut.

Once it is secured we need to assemble the internals of the button. There are three components, a lamp, the holder, and a microswitch.

You now need to insert the lamp into the lamp holder. The two contacts at the bottom of the lamp correspond to two clamps inside the holder.

![](https://cdn-images-1.medium.com/max/1200/1*2KHR27OCzqB6bUhy4Wj2nA.jpeg)

> _The components of the button; lamp (left), micro-switch (middle), and lamp holder (right)._

Unfortunately because the lamp is [a LED](https://learn.adafruit.com/all-about-leds/what-is-an-led) that means that you can only put it in one way around, and it's pretty hard to figure out which way round you need to insert it.

![](https://cdn-images-1.medium.com/max/1200/1*xiF-8diREYaBPcRUu7WN2A.jpeg)

> _Assembling the button, the lamp is visible (bottom)._

If you look closely at the legs wound around the base of the plastic shell around the LED you should notice one of these is slightly longer than the other. This is going to be the +ve leg (the anode), while the other will be the -ve leg (the cathode).

The cathode, the shorter of the two legs, is the one that should go to ground. However since we're inserting the LED into the holder, and then flipping the holder upside-down, and then rotating it slightly afterwards and neither the lamp or the holder is labelled things get awkward.

However if you peer down inside the plastic shell of the lamp you'll see a resistor in line on one of the LED's legs. That means it's not going to be the end of the world if we get it wrong -- we're not going to blow the LED if we get it wrong. In which case it's probably easiest, and quickest, to cross our fingers and pick a direction. We can always sort it later.

Next insert the microswitch. The holder has two pins that correspond to the two holes near the edges of the microswitch, it seems to be easiest to slip the bottom pin into corresponding hole on the switch, and then pry the top of the holder slightly backwards and push the microswitch down so that the second pin and hole line up. When they do it should all snap securely together, but it can take some force to make that happen.

Once assembled you need to secure the lamp assembly in place inside the button. If you look carefully at the button at 90° from the two white plungers there are two small plastic flanges. These correspond to the groves in the side of the lamp holder. Insert the completed lamp into the button pushing it down so that the flanges slide up the groves, and twist right-ward to lock it in place.

![](https://cdn-images-1.medium.com/max/1600/1*0TLyMd0SBikEKiYj4okt1g.jpeg)

> _Inserting the completed lamp assembly into the button._

However despite what it [says in the instructions](https://aiyprojects.withgoogle.com/voice/#assembly-guide-4-put-it-all-together) I found that the assembly slide smoothly around and locked in place without the application of much force. If you're having to use a lot of force make sure the flanges on the button, and the groves on the lamp holder are lined up correctly.

Assembling the arcade button is probably the most fiddly part of the entire kit, but I've been told that the new kits should an improved arcade button with assembled LED, micro switch and better connectors. Hopefully it'll be easier to assemble.

Once that's done you need to attach the wiring harness to the microswitch.

![](https://cdn-images-1.medium.com/max/1600/1*5oUK3KBlgRsLxdT01m-zQg.jpeg)

> _Attaching the wiring harness to the microswitch._

Which wire goes where matters, so follow the picture above, and slide the metal sleeves on the end of the wires over the contacts on the microswitch.

Once that's done we've reached the final stage, attaching the microphone daughter board. This board sits just below the button on the top flap of the box, with the two (left/right) microphones lined up with the top holes in the flap.

![](https://cdn-images-1.medium.com/max/1600/1*fnywzOOZAGX7pG7alrqlyA.jpeg)

> _Taping the Voice HAT Microphone daughter board in place._

The instructions say to tape the board in place, however I found that to be fairly ineffective. The solder from the 5-pin socket stuck out so far from the back of the board that it wouldn't lie flat on the the flap and had a tendency to pop off unless I used a lot of tape. Even then it didn't stay attached for long, with the weigh of the board, and the torque from the joints pressing against the flap, slowly peeling it away from the cardboard. While it'll work for now, if you're going to be using the Voice Kit in the cardboard box for the duration, you'll need to find another way to attach it--perhaps a dab of superglue would do the trick?

However what I do love about the mic board is that it's exactly that, a separate board on the end of a cable--that if needed could be extended. That adds a lot of flexibility once the Voice Kit comes out of its cardboard box and you integrate it into your own builds.

That's it, we're done.

![](https://cdn-images-1.medium.com/max/1600/1*3sq5ZLq5_Za7Qechmb3j6g.jpeg)

> _The finished Project Kit._

Close up the box, and now the Raspberry Pi is safely in place you should insert the micro SD Card into the slot, through the cut out in the cardboard.

#### Booting the Project Kit with a Monitor

If you're following along [with the official instructions](https://aiyprojects.withgoogle.com/voice/#assembly-guide-5-connect-and-boot-the-device) this is the point where you're going to go in search of an spare keyboard, mouse, and HDMI monitor. Once you've plugged everything else together, plug in the power supply and hopefully the Pi should boot.

If you see [a yellow lightning bolt appear](https://www.raspberrypi.org/magpi/power-supply/) at the top right of your screen your power supply isn't providing enough power--the Raspberry Pi 3 can need up to 2.5 Amps and a lot of USB power supplies top out at 2 Amps.

If all goes well however, after a little while you should arrive at the desktop, and just before it opens the button on top of the Voice Kit should start slowly pulsating.

![](https://cdn-images-1.medium.com/max/1600/1*7I9LWs7eow15q7las20KGg.gif)

> _The AIY Project Kit after booting._

If it doesn't you've [probably inserted the lamp the wrong way](https://aiyprojects.withgoogle.com/voice/#assembly-guide-7-appendix) around -- don't worry about this you haven't broken it. Pop the lid of the box -- there's no real need to power down the Raspberry Pi--and twist the switch assembly to the left to detach it from the button. Then just pull the lamp out of the holder, and flip it around. When you put it back in it should start pulsating in your hands, at which point you can put everything back together again.

![](https://cdn-images-1.medium.com/max/1600/1*rTcp9slI_qGCyTbiX0kVwg.png)

> _The button's light can tell you a lot about what's going on with the Voice Kit process._

#### Booting the Project Kit without a Monitor

Of course you're faced with a slight problem if you don't have a spare monitor to hand, especially if your main computer is made by Apple and your monitor has a Thunderbolt connector so you can't just "repurpose" it for a short while.

Not to worry, it's perfectly possible to bootstrap using the command line to the point where we can use VNC to remotely view the Raspberry Pi desktop. You will however have to plug the board to your wired network, so you'll need to go and find a spare Ethernet cable.

Plug the board into the Ethernet, and then connect the power to start it booting. After it finishes booting the Raspberry Pi should advertise itself using mDNS, with the default name of `raspberrypi.local`, allowing you to find it easily on the network. The easiest way to find it on the network will be to see if it responds to a `ping` request.
    
    
    **$** ping raspberrypi.local  
    PING raspberrypi.local (192.168.1.159): 56 data bytes  
    64 bytes from 192.168.1.159: icmp_seq=0 ttl=64 time=4.079 ms  
    64 bytes from 192.168.1.159: icmp_seq=1 ttl=64 time=4.223 ms  
    64 bytes from 192.168.1.159: icmp_seq=2 ttl=64 time=6.717 ms  
    ^C  
    — — raspberrypi.local ping statistics — -  
    3 packets transmitted, 3 packets received, 0.0% packet loss  
    round-trip min/avg/max/stddev = 4.079/5.006/6.717/1.211 ms

If the Raspberry Pi doesn't respond to a ping request the next easiest thing to do will be to log on to your network router and search for the IP address it was allocated using DHCP.

Once you find the Pi, go ahead and login with `ssh`--the default username and password are "`pi`" and "`raspberry`" respectively.

After logging in we can put our Raspberry Pi onto the local network using the internal wireless adaptor. First of all we need to find our wireless network. Go ahead and type,
    
    
    **$** sudo iwlist wlan0 scan

This is perform a scan for networks. Depending on where you are you may find only a few, or in the middle of a busy city, a much larger number and while I know my network uses WPA2 encryption, scrolling through the output I can confirm that. If you're unsure what sort of encryption your network is using, look for a line something like this,
    
    
    IE: IEEE 802.11i/WPA2 Version 1

associated with your network which should tell you. Once you have a network SSID, and encryption method we can go ahead and put our Raspberry Pi onto the network. On the assumption you're using WPA2, open the `/etc/wpa_supplicant/wpa-supplicant` file in your editor of choice, e.g.
    
    
    **$** sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Go to the bottom of the file and add the following:
    
    
    network={  
     ssid=”SSID”  
     psk=”PASSWORD”  
    }

Where SSID is the ESSID of your home network, and PASSWORD is the WPA2 password for your network. As a side note, if you want to configure two (or more) wireless networks you can do so by adding an `id_str` to each, e.g.
    
    
    network={  
     ssid=”OFFICE”  
     psk=”OFFICEPASSWORD”  
     id_str=”office”  
    }
    
    
    network={  
     ssid=”HOME”  
     psk=”HOMEPASSWORD”  
     id_str=”home”  
    }

and when booted the Raspberry Pi should associate with either network. Additionally if both networks are present you can add a priority key, and the network with the highest priority will be used first.

After saving the configuration file wpa-supplicant should notice a configuration change has been made and, within a few seconds, should try and connect to your (priority) wireless network. Generally however, it doesn't, and you should type the following,
    
    
    **$** sudo ipdown wlan0  
    **$** sudo ifup wlan0

Wait a few seconds and then,
    
    
    **$** ifconfig wlan0  
    wlan0 Link encap:Ethernet HWaddr b8:27:eb:c2:99:b1  
    inet addr:192.168.1.217 Bcast:192.168.1.255 Mask:255.255.255.0  
    inet6 addr: fe80::9380:71d4:4917:9b65/64 Scope:Link  
    UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1  
    RX packets:441 errors:0 dropped:416 overruns:0 frame:0  
    TX packets:20 errors:0 dropped:0 overruns:0 carrier:0  
    collisions:0 txqueuelen:1000  
    RX bytes:126262 (123.3 KiB) TX bytes:3634 (3.5 KiB)

The interface should have acquired an IP address, it should get it back on boot. At this point we can go ahead and [install a VNC server](https://www.raspberrypi.org/documentation/remote-access/vnc/). Type,
    
    
    sudo apt-get update  
    sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer

to install the server. Once it's installed we can enable it using the Raspbian configuration utility. Type,
    
    
    % sudo raspi-config

at the prompt to open the configuration manager. Using the Up/Down cursor keys navigate to `Interfacing Options` and the Enter key to select it. Then scroll down and select `VNC`, and then answer `Yes` when prompted. This will turn on the server, and return you to the main menu.

Now navigate to Advanced Options, then select Resolutions, and pick a workable resolution. I generally go with 1600×1200 as it fits nicely on my Mac's desktop.

We need to do this because--as we're connecting to a headless Pi--the VNC server will default to the smallest safe resolution, typically the same as a standard definition TV, which isn't going to be particularly usable.

Then use the Left/Right cursor keys to navigate to `Finish` and hit the Enter key. You'll be asked whether you want to reboot now, answer `Yes.`

While you're waiting for the Pi to reboot, you can pull the Ethernet cable out. Now we've set up wireless networking, we shouldn't need it any more.

![](https://cdn-images-1.medium.com/max/1200/1*5F6Hyr6bUj9tt1Sv5LV0mQ.png)

> _Connecting to the Raspberry Pi using the Real VNC Viewer application._

Once the Pi has rebooted you should log back in as before using `ssh` to make sure everything is working correctly.

Unfortunately the version of VNC that we're now running on the Pi isn't compatible with the built in screen sharing on macOS. However RealVNC offers [a VNC Viewer application](https://www.realvnc.com/en/connect/download/viewer/) for Windows, Linux, and macOS--as well as a number of other platforms.

So go ahead and [download](https://www.realvnc.com/en/connect/download/viewer/) the application and install it on your laptop.

![](https://cdn-images-1.medium.com/max/1600/1*u_FU1KbWpcPue5yK0Ap2vg.png)

> _The Real VNC Viewer running under mac OS showing the Raspberry Pi desktop._

Once installed you should now just be able to connect to `raspberrypi.local` with the default username and password again. If everything has worked, you should see the Raspberry Pi desktop in a window.

#### Is this Thing on..?

Now we're connected to the network we have to [check that everything is working](https://aiyprojects.withgoogle.com/voice/#assembly-guide-6-1--check-audio). If you look there are three document icons on the left of the desktop. We're going to use two of them right now to check the network connection back to Google, and the audio hardware.

First of all go ahead and double click on the `Check WiFi` icon on the desktop, a terminal window will open and a script will run. If everything is okay and your Voice Kit can talk to Google you should see,
    
    
    The WiFi connection seems to be working

and you can press Enter to close the window.

Now go ahead and double click on the `Check Audio` icon on the desktop. This will also open a terminal window and run a script. This time when the script runs an audio sample will play, which you need to acknowledge you heard okay. After this it'll ask you to push Enter and then speak a phrase, if everything goes okay, it should then play the phrase back to you and you should see the message,
    
    
    The audio seems to be working

and you can press Enter to close the window. At this point we've assembled and tested the Voice Kit, now we have to [connect it to the Google Cloud](https://aiyprojects.withgoogle.com/voice/#users-guide).

#### Connecting to the Cloud

Open up a web browser by clicking on the globe icon in the menu bar at the top of the screen and then go to `[console.cloud.google.com](https://console.cloud.google.com)`. Even if you've never used Google Cloud Platform before, you can use your normal Google account to sign in.

![](https://cdn-images-1.medium.com/max/1600/1*HUgwbiWkSTmMxCvD_5nk8w.png)

> _The Google Cloud Platform "Getting Started" screen._

Unfortunately things immediately started to diverge from [the instructions](https://aiyprojects.withgoogle.com/voice/#users-guide-1-1--connect-to-google-cloud-platform), because after logging into Google Cloud Platform it looked rather different than expected.

It's possible this was because I'm already a registered developer, and have used their Compute Engine and other cloud services before. It's actually possible that things look different because I'm based in the UK rather than the US--sometimes Google looks a bit different between countries. Or it's even possible things have changed over the last couple of months between the instructions being written, and me building the Voice Kit.

However this may, or may not, be a problem for you. Just bear in mind that when configuring the Google Assistant API you might see something that looks [a little different](https://aiyprojects.withgoogle.com/voice/#users-guide-1-1--connect-to-google-cloud-platform).

![](https://cdn-images-1.medium.com/max/1600/1*dpcnfXJ2FrokW2r9TIIFDg.png)

> _Select, or create, a project._

Clicking on the "Select a Project ▾" menu to the right of the Google Cloud platform logo didn't give me a drop down menu as expected. Instead I was presented with a popup window, and hitting the + button let me create a new project.

![](https://cdn-images-1.medium.com/max/1600/1*AzGfQY7UsWQRDPyJGwdDTw.png)

> _Creating a new project._

Hitting "Create" returned me to the home screen, where clicking on the "Select a Project ▾" menu item showed the same popup, but this time with my new project.

![](https://cdn-images-1.medium.com/max/1600/1*-tIsq3FrJH2OJsr5k65wgg.png)

> _The now populated list of projects._

From there clicking on "AIY Project" took me to my project page which shown the name and associated resources.

![](https://cdn-images-1.medium.com/max/1600/1*rp23TXcrZPDAsc0WrJX6vw.png)

> _The new AIY Project._

At this point, now I have a working project, I needed to [enable the "Google Assistant API"](https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview) which is the service that lies behind the Voice Kit.

![](https://cdn-images-1.medium.com/max/1600/1*SQlYi-Fv_uRW-TAYnuhMBg.png)

> _Enabling the Google Assistant API_

Once the Google Assistant API was enabled, I then needed to generate some create credentials so that the Voice Kit could talk to it.

![](https://cdn-images-1.medium.com/max/1600/1*mXa8f6_OTJCWYSKGRKjrsQ.png)

> _The Google Assistant API has been enabled._

Clicking on the "Credentials" menu item on the left brings me to back to a screen I recognise from the instructions, and from [here onwards](https://aiyprojects.withgoogle.com/voice/#users-guide-1-2--turn-on-the-google-assistant-api) what I was seeing now looked the same as Google's documentation.

So I went ahead and selected "OAuth Client ID" as my credential type.

![](https://cdn-images-1.medium.com/max/1600/1*b0s-XXCFFzzjHLYdXBtEOA.png)

> _Creating an OAuth client ID._

However since this was the first time creating a client ID I needed to configure the application's Consent Screen.

![](https://cdn-images-1.medium.com/max/1600/1*DUNK_uGu9LCnTtcZlP_X1A.png)

> _Before creating a client ID the application's Consent Screen needs to be configured._

Hitting "Configure consent screen" brings you to a page that asks for details about your application. The only thing you need to fill in here is the project's name--the one presented to users of the application in the authorisation step--although you can optionally add other metadata like associated URLs and logos.

![](https://cdn-images-1.medium.com/max/1600/1*osAcm3Jdj0w2BNXiAXzqiw.png)

> _Configuring the Consent Screen._

Saving the Consent Screen details brings us back to the credential creation screen. Selecting other and adding a reasonably memorable name, you should hit "Create"

![](https://cdn-images-1.medium.com/max/1600/1*2uv2viaSsUTEJoYiydZyfQ.png)

> _Creating credentials._

A popup window will then appear with your credentials, don't panic when this disappears as this isn't your only chance to grab them. Dismissing the pop up by clicking "OK" leaves you in a credentials list with your newly generated credentials.

![](https://cdn-images-1.medium.com/max/1600/1*z6ZqM7Fmn_MKMiEF6q-uYA.png)

> _The generated Oauth credentials, ready for downloading._

Click on the down arrow with the line underneath to download the credentials as a JSON file. Find the JSON file you just downloaded, it'll be named`client_secrets_XXXX.json`, and rename it to `assistant.json`. Then move it to `/home/pi/assistant.json`.

You'll now need to go to your Google account's [Activity Controls](https://myaccount.google.com/activitycontrols) panel. This is where you can configure the information that Google stores about you, and you need to enable "Web & App Activity," "Location History," "Device Information," and "Voice & Audio Activity."

![](https://cdn-images-1.medium.com/max/1600/1*J2bQNktZGUPlhGh0ISMX0A.png)

> _My Google Account's Activity Controls panel._

Note that under "Web & App Activity" you must also tick the additional box to "Include Chrome browsing history and activity from websites and apps that use Google services."

If you're doing this from a different browser make sure you're logged into the same Google account as when you were configuring the application.

Now go back to the desktop, click on the "Start dev terminal" icon and type,
    
    
    **$** sudo systemctl stop voice-recognizer

this will manually bring the voice recognizer service to a halt. We'll need to start it up [from the command line](https://aiyprojects.withgoogle.com/voice/#users-guide-3-2--manage-the-service) to allow us to configure it.

#### Configuring the Device

In the dev terminal type,
    
    
    src/main.py

to start the recognizer. Starting up for the first time, it should automatically open a browser window and let you choose an account to authorise. If you are logged to multiple Google accounts make sure you pick the same account as the one where you set up your Activity Controls.

![](https://cdn-images-1.medium.com/max/1600/1*hxoEb8a8xe7Am9p6o-7hOA.png)

> _Authorising account access for the AIY Project Kit application._

If everything goes okay you should be presented with the text,
    
    
    The authentication flow has completed, you may close this window.

in the browser window. The button should also stop pulsing, instead it will briefly blink every few seconds to show that the Voice Assistant is ready to use.

> _"How much wood can a woodchuck chuck?"_

Hitting `^C` in the dev terminal will stop the voice recognizer service.

#### Starting the Voice Service on Boot

As an alternative to running the application manually, you can also run it as a system service. You start the service by entering,
    
    
    **$** sudo systemctl start voice-recognizer

and you can stop the service by entering,
    
    
    **$ **sudo systemctl stop voice-recognizer.

Starting the application as a service also lets you to have it start up when the Raspberry Pi boots. To do so you need to enable the voice recognizer service like so,
    
    
    **$ **sudo systemctl enable voice-recognize

and next time you boot the Raspberry Pi the voice recognizer should start automatically in the background.

#### Adding a Shutdown Button

I run most of my projects headless, which means one thing I do all the time to my Raspberry Pi boards is shut them down improperly. This means that, at least from time to time, I have a tendency [get corrupt SD Cards](http://ideaheap.com/2013/07/stopping-sd-card-corruption-on-a-raspberry-pi/).

![](https://cdn-images-1.medium.com/max/1200/1*ST2v056hMMZW4_WeMsTutw.jpeg)

> _A 5 pin male header soldered onto the I2C (left) on the Voice HAT._

![](https://cdn-images-1.medium.com/max/1200/1*WP9dIgvFv9HXDej-ijzlkQ.jpeg)

> _The Monk Makes [Squid Button](http://amzn.to/2xFFrOx)._

Unfortunately I just can't be bothered to figure out what their IP address is and `ssh` into them to shut them down every time I need to turn them off and on again.

I really should keep a list of IP addresses on my office whiteboard, but things are continually hoping on and off my network. It'd never be up to date, so there's little point.

Then I remember a post by [Inderpreet Singh](http://twitter.com/ip_v1) who had [reverse engineered](http://hackaday.com/2017/05/30/diy-google-aiy/) the AIY Project Kit soon after it was released so that he could put together [a DIY version](https://github.com/inderpreet/DIY-AIY).

In amongst generating KiCAD schematics for the Voice HAT he had a quick hack to add a shutdown button.

Then I looked at the box, there's a perfect unused cutout on the side with the SD Card slot. Presumably it was intended for other things that the team at Google never got around to, but it's a perfect fit for a small push button.

So I quickly pulled the cardboard box apart, and soldered some male headers to the [I2C pinout on top of the Voice HAT](https://aiyprojects.withgoogle.com/voice#makers-guide-4-1--connecting-additional-sensors). Then, following the same procedure as we did with the arcade button, I hooked up a spare Monk Makes [Squid Button](http://amzn.to/2xFFrOx) that I had sitting on my shelves to the SDA and GND pins on the I2C header.

Then I grabbed [Inderpreet](http://twitter.com/ip_v1)'s [Python code](https://gist.github.com/aallan/c2578d33082f124c6d7049d37fc4ed08) and saved it in `/home/pi` as `shutdown.py`.
    
    
    #!/bin/python  
    # Script for shutting down the Raspberry Pi by pressing a button.  
    # by Inderpreet Singh (30 May 2017)  
    # <http://hackaday.com/2017/05/30/diy-google-aiy/>  
       
    import RPi.GPIO as GPIO  
    import time  
    import os  
       
    # Use the Broadcom SOC Pin numbers  
    # Setup the Pin with Internal pullups enabled and PIN in reading mode.  
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(02, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
       
    # Our function on what to do when the button is pressed  
    def Shutdown(channel):  
     os.system("sudo shutdown -h now")  
       
    # Add our function to execute when the button pressed event happens  
    GPIO.add_event_detect(02, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)  
       
    # Now wait!  
    while 1:  
     time.sleep(1)

We can test this at the command line. Open up a normal terminal window, from the top menu bar--rather than a dev terminal window from the desktop icon, as that has a custom version of Python in the path--and run the script,
    
    
    **$** python shutdown.py &

and then go ahead and push the button. The Raspberry Pi should spin down cleanly to a halt. To restart it, just pull the USB cable out and push it back in again.

> _"Is this thing on..?"_

We can also make sure that the script is running every time the Raspberry Pi is rebooted by adding it to the `/etc/rc.local` file.
    
    
    #!/bin/sh -e  
    #  
    # rc.local
    
    
    python /home/pi/shutdown.py &
    
    
    exit 0

Now every time the Raspberry Pi boots the script will be run in the background and sit there monitoring the GPIO connected to the button and waiting for us to turn it off.

#### Where Now?

There are really two use cases for the AIY Voice Kit. First of all you can build your own device connected to Google's Voice Assistant -- in other words you can build your own [Google Home](https://madeby.google.com/home/). That's more or less what we've done here, and there have been some really interesting builds done with the AIY Voice Kit putting it in different enclosures, my favourite so far has to be the [1986 Google Pi Intercom](https://www.instructables.com/id/1986-Google-Pi-Intercom/) by [Martin Mander](https://twitter.com/martinwmander?lang=en).

> _A retro computing build with the AIY Voice Kit. (Video credit: [Martin Mander](https://www.youtube.com/channel/UC3i6LvRQvIO3_wdPTyJUpKA))_

However I'm far more interested in the other use case. Using the kit to [provide a voice interface](https://aiyprojects.withgoogle.com/voice#makers-guide-3-1--change-to-the-cloud-speech-api) to your own project--in other words giving your Raspberry Pi a custom vocabulary.

In the last few months we've seen the [start of a sea change](https://blog.hackster.io/deep-learning-on-a-usb-stick-29c117cf93e2) about how we think about machine learning, and how the Internet of Things might be built, with the potential to put the smarts on the smart device, rather than in the cloud.

Since the release of the AIY Voice Kit a couple of months ago Google's has also gone ahead and [open sourced some speech recognition datasets](https://research.googleblog.com/2017/08/launching-speech-commands-dataset.html).

Allowing you to build basic, but still useful, voice interfaces for machine learning applications on the device, the availability of these datasets are a step to making "smart objects" actually smart--rather than just network connected clients for machine learning algorithms running in remote data centres--and do [on-device voice recognition](https://research.googleblog.com/2017/08/launching-speech-commands-dataset.html) with TensorFlow.

Which is where I guess I'll go next, because I'm not done with the Google Voice Kit quite yet.

#### Available to Preorder

If the reaction to [the Pi Hut](https://thepihut.com/) getting their hands on some copies of Issue 57, returned by brick and mortar stores for cosmetic damage, is anything to go by--they [sold out in just 17 minutes](https://twitter.com/aallan/status/897548861262135296)--then the new run of AIY Project Voice Kits are probably going to move off the shelves fairly briskly.

The new kits are being [produced by Google](https://www.blog.google/topics/machine-learning/aiy-voice-kit-inspiring-maker-community/), and will be sold by [Micro Center](http://www.microcenter.com/) and through resellers like [Adafruit](https://www.adafruit.com/), and [SeeedStudio](https://www.seeedstudio.com/). It will be priced at $25 on its own, but will also come free if you order a Raspberry Pi 3 at $35 for in-store pickup from Micro Center.

While [pre-orders opened today](http://www.microcenter.com/site/content/Google_AIY_Preorder.aspx?utm_source=medium&utm_medium=google_aiy&utm_campaign=Google_AIY_preorder) the kits themselves aren't expected to be on shelves till nearer the end of October. That is, if they make it as far as the shelves, and don't sell out before that.

**UPDATE: **The new retail version of AIY Projects Voice Kit will be available in the United Kingdom [through Pimoroni](https://shop.pimoroni.com/products/google-aiy-voice-kit), and cost £25\. You can expect shipping dates for kits ordered in through them to be similar to those ordered from Micro Center.

_This post was sponsored by Google._
