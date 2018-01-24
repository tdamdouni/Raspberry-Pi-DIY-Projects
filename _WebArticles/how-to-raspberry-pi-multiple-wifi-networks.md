# How To: Raspberry Pi Multiple WiFi Networks

_Captured: 2017-11-19 at 15:38 from [www.raspberrycoulis.co.uk](https://www.raspberrycoulis.co.uk/hints-tips/raspberry-pi-multiple-wifi-networks/)_

![Raspberry Pi Multiple Wifi Networks](https://i1.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/raspberry_pi_multiple_wifi-opt.png?w=1000&ssl=1)

Getting WiFi working on Raspberry Pi must be one of the most searched topics since the popular board was released. Thankfully, this is now a pretty simple process even for beginners! However, as the Raspberry Pi is portable, many people like to take it with them wherever they go. This presents a new challenge, which is providing Internet access without access to a monitor or an Ethernet cable. Like other Internet connected devices, people want to set up Raspberry Pi multiple WiFi networks.

Firstly, did you know that there is a quick way to set up WiFi on your Raspberry Pi before the first boot?

## Setup Raspberry Pi WiFi Before Boot

Until recently, you had to boot your Pi with an Ethernet cable connected and then make all the necessary edits to system files to setup WiFi. However, there is now a way to setup WiFi before you power on your Pi for the very first time. In order to do this, you need to create a file called **"wpa_supplicant.conf"** and then transfer it to the boot folder on your SD card. You can do this in any basic text editing software, but Notepad++ is recommended.

**Notepad++** is a free text editor and is a suped-up version of the standard Windows Notepad. However, it is great for creating or editing code because it helps with formatting - such as indentation, brackets and so on. You can download [Notepad++ from their website](https://notepad-plus-plus.org/download/).

#### WPA Supplicant

First, open Notepad++ and add the following code to it:

1234567
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdevupdate_config=1network={ssid="YOUR_WIFI_NETWORK"psk="YOUR_WIFI_PASSWORD"key_mgmt=WPA-PSK}

You need to add your own details to this document, and they are pretty self-explanatory:

  1. SSID = Your WiFi network name
  2. PSK = Your WiFi password

#### Encryption

The last section, **"key_mgmt"**, is set depending on the encryption method your WiFi network uses. If you are using a relatively modern WiFi router, then the chances are it will be WPA-PSK. For the curious, this stands for **WiFi Protected Access Pre-Shared Key.** Older routers (as in 10+ years) may use WEP, or **Wired Equivalent Privacy**, but this is no longer recommended as a relatively inexperienced [hacker could crack this in a few minutes if they wanted to](https://www.quora.com/Which-can-easily-be-hacked-WPA-or-WEP)!

Once you have added your WiFI network name and password, save your file as **"wpa_supplicant.conf"** (without the quotation " " marks and ensuring it is lower-case). This is what you can now transfer to the boot folder on your SD card. Now when you boot your Pi, it should automatically connect to your WiFi network!

What actually happens is that your Pi copies the "wpa_supplicant.conf" file to the proper location on the Pi itself. This is typically "/etc/wpa_supplicant", and if you want to make any additional changes, you can find the "wpa_supplicant.conf" file here.

![Make sure you set ](https://i0.wp.com/www.raspberrycoulis.co.uk/wp-content/uploads/2016/08/encryption-opt.jpg?w=1352&ssl=1)

> _Make sure you set "key_mgmt" depending on the encryption method used by your WiFi router!_

### Hang on though!

You have come here because you want to establish **Raspberry Pi multiple WiFi networks! **To do this, you follow the same steps as above, except you need to add a few more networks to your "wpa_supplicant.conf" file. There is also an additional step required, especially if you want to prioritise the networks so that your Pi prefers to connect to a specific network over another.

## Raspberry Pi Multiple WiFi Networks

To do this, you will obviously need to know the details of all the WiFi networks you want your Raspberry Pi to connect to. This may well be your home network, your school or work network and maybe a phone-tethered network (i.e. for when you want to get your Pi online outside the reach of other WiFi networks). Once you have the SSID and passwords for your WiFi networks, you need to add them to your "wpa_supplicant.conf" file:

1234567891011121314151617181920212223
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdevupdate_config=1network={ssid="HOME_WIFI_NETWORK"psk="HOME_WIFI_NETWORK_PASSWORD"key_mgmt=WPA-PSKid_str="home"priority=1}network={ssid="WORK_WIFI_NETWORK"psk="WORK_WIFI_NETWORK_PASSWORD"key_mgmt=WPA-PSKid_str="work"priority=2}network={ssid="PHONE_TETHER_NETWORK"psk="PHONE_TETHER_NETWORK_PASSWORD"key_mgmt=WPA-PSKid_str="phone"priority=3}

If you look carefully at the new details above, you may notice a few things. Firstly, we have created three networks - one for home, one for work and one for tethering to your phone's WiFi hotspot. In order to help your Raspberry Pi understand which network is which, we have also added the **"id_str"** string, which you will notice has been assigned a name - either "home", "work" or "phone". **This is a crucial step for Raspberry Pi multiple WiFi networks, as you will need them for the next part, so remember them.**

#### Setting priorities

You may also notice a **"priority"** string, along with a number. This is pretty self-explanatory - this tells your Raspberry Pi to try and connect to your networks in a specific order. First of all, the numbers associated are not as logical as you would expect! This is because **the higher the number, the higher the preference.** In the example above, our Raspberry Pi will try to connect to the networks in the following order:

  1. Phone (priority of 3)
  2. Work (priority of 2)
  3. Home (priority of 1)

As a result, our example places the "phone" network at the top because we may want to connect to our Raspberry Pi in the office, but want to avoid connecting to the "work" network if the "phone" network is present. You might want to experiment with the priorities yourself, and you can do this by simply changing the numbers associated with the "priority" string.

### Almost there…

There is one more adjustment required to get Raspberry Pi Multiple WiFi Networks, and that is to add a couple of lines to the **"/etc/network/interfaces"** file, because this tells your Raspberry Pi how to connect to any networks present:

1234567891011121314151617181920212223
# interfaces(5) file used by ifup(8) and ifdown(8)# Please note that this file is written to be used with dhcpcd# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'# Include files from /etc/network/interfaces.d:source-directory /etc/network/interfaces.dauto loiface lo inet loopbackiface eth0 inet manualallow-hotplug wlan0iface wlan0 inet manualwpa-conf /etc/wpa_supplicant/wpa_supplicant.confallow-hotplug wlan1iface wlan1 inet manualwpa-conf /etc/wpa_supplicant/wpa_supplicant.confiface home inet dhcpiface work inet dhcpiface phone inet dhcp

The key lines here are the bottom three:

  1. iface home inet dhcp
  2. iface work inet dhcp
  3. iface phone inet dhcp

Remember the **"id_str"** names we added earlier? If not, then it might be worth going back and getting them as this is where we add them to our interfaces file. You now just need to add your "id_str" here, along with the prefix **"iface"** and the suffix **"inet dhcp"**, especially if your IP addresses are set by DHCP.

## Last step!

Once you have added your network strings to the interfaces file, simply save it (do this by pressing Ctrl+X if using Nano) and then reboot your Raspberry Pi! If all goes well, you should have setup Raspberry Pi Multiple WiFi Networks, along with prioritised connections!
