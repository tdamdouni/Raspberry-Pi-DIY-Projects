# Enabling Simultaneous AP and Managed Mode WiFi on Raspberry Pi Zero W (Raspbian Stretch)

_Captured: 2017-09-28 at 21:28 from [albeec13.github.io](https://albeec13.github.io/2017/09/26/raspberry-pi-zero-w-simultaneous-ap-and-managed-mode-wifi/)_

![](https://albeec13.github.io/banners/rpizw.jpg)

I recently purchased a pair of Raspberry Pi Zero W boards, and plan to use them for some home automation / IoT-type work. One of myrequirements is that the WiFi on this board be able to run as both a "managed" device (also known as "client" mode) and as an access point, preferrably at the same time. After looking around a bit online, I found several people who claimed to have gotten this working, as well as posts saying it should work, based on the chipset. Despite my best efforts, I was unable to get any of those tutorials to work reliably on their own. By combining some information garnered from each one, along with some trial and error, I was finally able to get AP/Manged mode working, as described below.

## Prerequisites

This tutorial assumes you've already created a bootable MicroSD card running the latest Raspbian Stretch image and have some way of accessing Linux, whether via serial interface, or a monitor and keyboard. If you haven't, a couple of great resources I found online are:

  * [Raspberry Pi Zero W "headless" Setup](https://slippytrumpet.io/posts/raspberry-pi-zero-w-setup/) \- This great tutorial walks you through getting WiFi client mode enabled on your RPi Zero W, without need for an attached monitor or keyboard. You will need a way to modify the contents of the MicroSD card's filesystem, such as a Linux machine, Chromebook with crouton, or VM. There are also ways to do this from Windows, but I'll leave that as an exercise for the reader.
  * [Raspberry Pi Zero OTG Mode](https://gist.github.com/gbaman/50b6cca61dd1c3f88f41) \- Another awesome tutorial, via GitHub gist, which explains how to enable OTG / USB Gadget mode on the RPi Zero / Zero W. OTG mode lets you both power and communicate with the RPi Zero W as a virtual serial device, ethernet device, or mass storage device, among other things, with nothing more than a standard (read: non-OTG) USB cable. I used this to directly access the Raspbian Linux terminal via USB while trying to tweak the WiFi settings so that I wouldn't drop my ssh session from headless mode.

## Adding Udev Rule To Add A Virtual AP Device At Boot Time

Before we can operate our access point, we need a device allocated for it, similar to how systemd allocates a `wlan0` device at boot time. On the build of Raspbian Stretch I'm using, only `wlan0` is available automatically. We create a file caled `/etc/udev/rules.d/70-persistent-net.rules` which contains the following:
    
    
    SUBSYSTEM=="ieee80211", ACTION=="add|change", ATTR{macaddress}=="b8:27:eb:ff:ff:ff", KERNEL=="phy0", \
      RUN+="/sbin/iw phy phy0 interface add ap0 type __ap", \
      RUN+="/bin/ip link set ap0 address b8:27:eb:ff:ff:ff"
    

Note that you must replace both MAC addresses above with that of your own RPi. You can find yours in various ways, such as from your router's client list, or from the RPi's command line via `iw dev`:
    
    
    pi@raspberrypi:~$ iw dev
    phy#0
            Unnamed/non-netdev interface
                    wdev 0x4
                    addr ba:27:eb:07:28:1f
                    type P2P-device
                    txpower 31.00 dBm
            Interface wlan0
                    ifindex 2
                    wdev 0x1
                    addr b8:27:eb:ff:ff:ff
                    ssid <YOUR HOME SSID> 
                    type managed
                    channel 6 (2437 MHz), width: 20 MHz, center1: 2437 MHz
                    txpower 31.00 dBm
    

A number of tutorials I found claimed that the address for the virtual AP must be different from the primary MAC address. I found there to be no difference in behavior, but you should be able to change the last byte, for example, to give your client and AP different MACs.

The device we created above is called `ap0`. We will refer to this elsewhere, so if you decide to change the name, make sure to use the new name everywhere else I reference it, or things won't work correctly.

## Installing Dnsmasq and Hostapd

  * **Dnsmasq** \- This program has extensive features, but for our purposes we are using it as a DHCP server for our WiFi AP.
  * **Hostapd** \- This program defines our AP's physical operation based on driver configuration.

Installing these is an easy affair:
    
    
    $ sudo apt-get install dnsmasq hostapd
    

Wait awhile, and this process should complete. The install process may automatically start the `dnsmasq.service` in systemd right after installation and it will probably fail, since `ap0` does not exist until we reboot. Disregard this for now.

Next, we need to modify 3 files. First we modify `/etc/dnsmasq.conf` by adding the following lines at the end of the file:
    
    
    interface=lo,ap0
    no-dhcp-interface=lo,wlan0
    bind-interfaces
    server=8.8.8.8
    domain-needed
    bogus-priv
    dhcp-range=192.168.10.50,192.168.10.150,12h
    

Once again, notice we reference `ap0` above, so use your device name here if you changed it earlier. I've added Google's DNS server IP here (_8.8.8.8_) but feel free to use one from your router/ISP/or whatever. I've also made the assumption that our DHCP server will give out addresses on the _192.168.10.0/24_ subnet, ranging from _.50_ to _.150_. You can substiute your own subnet here, but be sure to remember it for later, as it should match the static IP we assign your AP. The 12 hour lease time can also be arbitrarily changed to suit your needs.

Next, we need to modify the file at `/etc/hostapd/hostapd.conf`. I found many different parameters that can go in here, but this is what worked for me. Feel free to experiment further by poking around online. Lets do this for now:
    
    
    ctrl_interface=/var/run/hostapd
    ctrl_interface_group=0
    interface=ap0
    driver=nl80211
    ssid=YourApNameHere
    hw_mode=g
    channel=11
    wmm_enabled=0
    macaddr_acl=0
    auth_algs=1
    wpa=2
    wpa_passphrase=YourPassPhraseHere
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP CCMP
    rsn_pairwise=CCMP
    

A couple things to note here:

  1. Replace `YourApNameHere` and `YourPassPhraseHere` with the SSID and Passphrase you wish to use.
  2. I read multiple sources claiming that the channel you use here _must_ match the channel that your `wlan0` iterface is using for its WiFi connection, as reported by `iw dev`. In my testing, it looks like the RPi's AP will dynamically change channels to match whatever channel the `wlan0` interface is currently using. I watched this happen in real time by rebooting the WiFi AP the RPi was using, forcing it to roam and switch to another AP in my house. In the process, `wlan0` switched from channel 11 to channel 6, and `ap0` did the same, without losing connectivity.

Finally, we modify `/etc/default/hostapd` like so:
    
    
    DAEMON_CONF="/etc/hostapd/hostapd.conf"
    

This tells the `hostpad` daemon to use our new conf file. (To be honest, I'm not sure if this matters since we will be launching hostapd manually and pointing to the proper config file, but it shouldn't hurt anything.)

## Modify Our Interfaces File

Next, we need to define our WiFi network interfaces, both for our managed access (`wlan0`) and for our access point (`ap0`). We will also use `wpa_supplicant` to assist with connecting to WPA-encrypted WiFi networks. If you followed the "headless" bring-up tutorial I mentioned in the prereqs, you will have already touched both of the following files and configured `wlan0` as required. In that case, we'll be adding a static IP definition for `ap0`. First, we modify `/etc/wpa_supplicant/wpa_supplicant.conf` as so:
    
    
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    
    network={
        ssid="YourSSID1"
        psk="YourPassphrase1"
        id_str="AP1"
    }
    
    network={
        ssid="YourSSID2"
        psk="YourPassphrase2"
        id_str="AP2"
    }
    

Again, you should replace the SSIDs and Passphrases above with your own. You aren't required to name multiple SSIDs here, but if you add more, the RPi can roam between networks if configured correctly, as we will do below. The `id_str` field can be used as a quick reference name in our interfaces file. You should also change the country code to whatever is appropriate for your region.

Next, we modify `/etc/network/interfaces` to support our new AP:
    
    
    # interfaces(5) file used by ifup(8) and ifdown(8)
    
    # Please note that this file is written to be used with dhcpcd
    # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
    
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d
    
    auto lo
    auto ap0
    auto wlan0
    iface lo inet loopback
    
    allow-hotplug ap0
    iface ap0 inet static
        address 192.168.10.1
        netmask 255.255.255.0
        hostapd /etc/hostapd/hostapd.conf
    
    allow-hotplug wlan0
    iface wlan0 inet manual
        wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface AP1 inet dhcp
    iface AP2 inet dhcp
    

As you can see, we want both `ap0` and `wlan0` to start up automatically, with `ap0` defined to have a static IP of _192.168.10.1_ on the _192.168.10.0/24_ subnet. Recall, the DHCP address range we defined in `/etc/dnsmasq.conf` matched this subnet. Adjust accordingly if you made changes. We also reference our `hostapd` config file here, to direct the AP configuration for `ap0`.

For `wlan0`, we start it using manual mode and point it to our `/etc/wpa_supplicant/wpa_supplicant.conf` file for our WiFi network definitions. The `wpa-roam` designator will allow the interface to move freely between our defined networks. Finally, the last two lines use our friendly names from `wpa_supplicant.conf` to refer to our available networks, and indicate this interface should use DHCP supplied by those APs to assign an address to `wlan0`. **Please note the order here: ap0 must come up before wlan0, or they won't both work at the same time.**

## We're Done! Or Are We…

At this point, I expect everything to work after a reboot. Instead, I end up with `wlan0` UP and `ap0` DOWN (or vice-versa) when checking via `ip addr`, and `dmesg` indicates some errors in the Broadcom driver. After some tinkering, I discovered the following sequence of commands after a reboot would get both interfaces up and working simultaneously, like we wanted all along:
    
    
    $ sudo ifdown --force wlan0
    $ sudo ifdown --force ap0
    $ sudo ifup ap0
    $ sudo ifup wlan0
    

I had to add `\--force` because sometimes hostapd would complain about having a lock on `wlan0` and fail to proceed, so it ensures we get what we want. After bringing down both interfaces, again, with `ap0` going first, followed by `wlan0`, they should both come up:
    
    
    pi@raspberrypi:~$ ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether b8:27:eb:ff:ff:ff brd ff:ff:ff:ff:ff:ff
        inet 192.168.43.37/24 brd 192.168.43.255 scope global wlan0
           valid_lft forever preferred_lft forever
        inet6 fe80::ba27:ebff:fede:3a79/64 scope link
           valid_lft forever preferred_lft forever
    3: ap0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether b8:27:eb:ff:ff:ff brd ff:ff:ff:ff:ff:ff
        inet 192.168.10.1/24 brd 192.168.10.255 scope global ap0
           valid_lft forever preferred_lft forever
        inet6 fe80::ba27:ebff:fede:3a79/64 scope link
           valid_lft forever preferred_lft forever
    

Great! But what about bridging traffic between my AP and client sides to allow a device to access the internet through my RPi? Let's do that:
    
    
    $ sudo sysctl -w net.ipv4.ip_forward=1
    $ sudo iptables -t nat -A POSTROUTING -s 192.168.10.0/24 ! -d 192.168.10.0/24 -j MASQUERADE
    $ sudo systemctl restart dnsmasq
    

Here, we enable ip forwarding to allow packets to be forwarded between interfaces, and we add a postrouting rule to IP tables which routes all packets from the AP-side interface to the client-side interface (where MASQUERADE is necessary, since the IP is dynamic and undefined until `wlan0` connects to an AP). Finally, we restart dnsmasq for good measure, since we previously brought down `ap0` with `ifdown`.

At this point, we should be able to connect a device to our Raspberry Pi Zero W's AP SSID, while we also have our RPi connect to another access point for internet access, _and_ we should be able to access the internet from that device through our RPi. Only one thing left to do…

## Automate The Workaround

Try as I might to debug the issues I was having before manaully reseting the interfaces, I was unable to get the RPi to simply boot up working correctly. So, I decided to script the steps to "fix" everything and set them to run as a root `cron` job with a 30s delay… (Yes, I know this is horrible practice, but I'm open to better suggestions.) I intially tried setting up a `systemd` service to call my script instead of `cron` with a delay, but it didn't seem to work or ran at the wrong time, requiring manual intervention.

Here's the script in it's entirety:
    
    
    pi@raspberrypi:~$ cat ./start-ap-managed-wifi.sh
    #!/bin/bash
    sleep 30
    sudo ifdown --force wlan0 && sudo ifdown --force ap0 && sudo ifup ap0 && sudo ifup wlan0
    sudo sysctl -w net.ipv4.ip_forward=1
    sudo iptables -t nat -A POSTROUTING -s 192.168.10.0/24 ! -d 192.168.10.0/24 -j MASQUERADE
    sudo systemctl restart dnsmasq
    

I simply left the file in my default "pi" user's home directory, but you can move it someplace more appropriate, such as `/sbin`. I then added a `cron` job like so:
    
    
    $ sudo crontab -e
    

And in there I added the line:
    
    
    @reboot /home/pi/start-ap-managed-wifi.sh
    

This causes the script to run at every reboot. In testing, I foud the RPi Zero W boots in under 20s. `Systemd` runs the `cron` service somewhere in that range of time, which eventually runs the script above. To be safe, you can change the 30s delay to something longer, but I found this to be pretty reliable.

Now, after every reboot, even though `ap0` and `wlan0` don't initally play well together, the `cron` job kicks off my script after 30s and magically fixes everything. We have AP and Managed mode running at the same time, and we're bridging traffic between the interfaces to allow for internet sharing through the Raspberry Pi Zero W.

## Special Thanks

The following links were pretty instrumental in getting things moving in the right direction, so please check them out:

Please comment below if this helped you, or if you have any suggestions for improvements!
