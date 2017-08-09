# How (and Why) to Assign the .local Domain to Your Raspberry Pi

_Captured: 2017-05-06 at 15:43 from [www.howtogeek.com](https://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/)_

![](https://www.howtogeek.com/wp-content/uploads/2013/07/xraspberrylocalhostheader.jpeg.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.KrPZrvY9l7.jpg)

If you're tired of looking up the IP addresses of devices you frequently access via remote login, SSH, and other means on your home network, you can save yourself a lot of time by assigning an easy to remember `.local` address to the device. Read on as we demonstrate by assigning an easy to remember name to our Raspberry Pi.

## Why Do I Want to Do This?

Most likely your home network uses DHCP IP assignments, which means that each time a device leaves the network and returns a new IP address is assigned to it. Even if you set a static IP for a frequently used device (e.g. you set your Raspberry Pi box to always be assigned to number `192.168.1.99`), you still have to commit that entirely unintuitive number to memory. Further, if you ever need to change the number for any reason you would have to remember a brand new one in its place.

Doing so isn't the end of the world, but it is inconvenient. Why bother with memorizing IP strings when you can give you local devices easy to remember names like `raspberrypi.local` or `mediaserver.local`?

Now, some of you (especially those of you with a more intimate knowledge of DNS, domain naming, and other network address structures) might be wondering what the catch is. Isn't there an inherent risk or problem in just slapping a domain name onto your existing network? It's important here to make note of the _big_ distinction between Fully Qualified Domain Names (FQDNs), which are officialy recognized suffixes for top-level domains (e.g. the `.com` portion of `www.howtogeek.com` that signifies How-To Geek is a commercial web site) and domain names that are either not recognized by the global naming/DNS system or are outright reserved for private network usage.

For example, `.internal` is, as of this writing, not a FQDN; there are no registered domains anywhere in the world that end with `.internal` and thus if you were to configure your private network to use `.internal` for local addresses, there would be no chance of a DNS conflict. That could, however, change (though the chance is remote) in the future if `.internal` became an official FQDN and addresses ending in `.internal` were externally resolvable through public DNS servers.

Conversely, the `.local` domain, has been officially reserved as a Special-Use Domain Name (SUDN) specifically for the purpose of internal network usage. It will never be configured as a FQDN and as such your custom local names will never conflict with existing external addresses (e.g. `howtogeek.local`).

## What Do I Need?

The secret sauce that makes the entire local DNS resolution system work is known as Multicast Domain Name Service (mDNS). Confusingly, there are actually two implementations of mDNS floating around, one by Apple and one by Microsoft. The mDNS implementation created by Apple is what undergirds their popular Bonjour local network discovery service. The implementation by Microsoft is known as Link-local Multicast Name Resolution (LLMNR). The Microsoft implementation was never widely adopted thanks to its failure to adhere to various standards and a security risk related to which domains could be captured for local use.

Because Apple's mDNS implementation Bonjour enjoys a much wider adoption rate, has better support, and a huge number of applications for platforms big and small, we've opted to use it for this tutorial.

If you have computers running Apple's OS X on your network, there's nothing you need to do beyond following along with the tutorial to set things up on the Raspberry Pi (or other Linux device) side of things. You're set to go as your computers already support it.

If you're running a Windows machine that does not have iTunes installed (which would have installed a companion Bonjour client for mDNS resolution), you can resolve the lack of native mDNS support by downloading [Apple's Bonjour Printer Service helper app here](http://support.apple.com/kb/DL999). Although the download page makes it sound like it's a printer-only tool, it effectively adds mDNS/Bonjour support across the board to Windows.

## Installing Bonjour Support on Your Raspberry Pi

The first order of business is to either pull up the terminal on your Pi or connect into the remote terminal (if you have a headless machine) via SSH. Once at the terminal, take a moment to update and upgrade apt-get. (Note: if you've just recently done this as part of another one of our Raspberry Pi tutorials, feel free to skip this step.)

> `sudo apt-get update`
> 
> `sudo apt-get upgrade`

After the update/upgrade process is complete, it's time to install [Avahi](http://www.avahi.org/)-a fantastic little open source mDNS implementation. Enter the following command at the prompt:

> `sudo apt-get install avahi-daemon`

Once the installation process is complete, you don't even have to reboot the device. Your Raspberry Pi will begin immediately recognizing local network queries for its hostname (by default "`raspberrypi`") at `raspberrypi.local`.

The particular machine we used for this test is the same Raspberry Pi we turned into an ambient weather indicator, and then [later changed the local hostname](https://www.howtogeek.com/?p=167195), so when we go to look for the newly minted `.local` address, we'll be looking for `weatherstation.local` instead of `raspberrypi.local`.

Again, for emphasis, the portion that precedes the .local suffix is _always_ the hostname of the device. If you want your Raspberry Pi music streamer to have the local name `jukebox.local`, for example, you'll need to [follow these instructions to change the Pi's hostname](https://www.howtogeek.com/?p=167195).

Go ahead and ping the new `.local` address on the machine you wish to access the device from now:

Success! weatherstation.local resolves to 192.168.1.100, which is the actual IP address of the device on the local network. From now on, any application or service which previously required the IP address of the Raspberry Pi can now use the .local address instead.
