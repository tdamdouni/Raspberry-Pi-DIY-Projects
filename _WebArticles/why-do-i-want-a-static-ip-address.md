# Why do I Want a Static IP Address?

_Captured: 2017-08-24 at 23:34 from [www.tecoed.co.uk](http://www.tecoed.co.uk/static-ip-address.html)_

An** IP Address** _(Internet Protocol) _is a a set of numerical digits that identify a device and its location on a network. It is similar to your house address except that it uses numbers. If your Raspberry Pi is connected your Router then it will automatically be given its own IP address. The issue is that this address will change each time you log on and off. This is know as a **Dynamic Address** \- it changes. A **Static IP **Address remains the same all the time and makes it easier to access your Pi.

## Getting Started

Basically you need to identify your current network settings and modify them so that the IP Address remains static. Firstly check that your address is not already **Static** .  
  
**In the LX Terminal type:**  
**_cat /etc/network/interfaces_ **  
  
This will load an overview of the connected network devices, you are looking for the third line which states: **_iface eth0 inet dhcp _**The **DHCP **means that your **IP Address **is **Dynamic **and will change when you turn the Pi off. 
![Picture](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/4079763_orig.png)

## Collecting the Information: Part 1

The next part is to collect the information relating to the your current **IP Address, **the B**roadcast address **and the **Netmask address, **these are abbreviated to **Inet, Bcast **and **Mask. **All the values are on the same line so it is easy to coppy them down in one go  
  
**In the LX Terminal type:**  
**_ifconfig _**  
  
**_Write these three values down as you will require them later_**  

![Picture](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/5235558_orig.png)

## Collecting the Information: Part 2

The next part is to collect the **Destination **and the **Gateway **address. There are two commands that you can use the access them.  
  
**In the LX Terminal type:**  
**_netstat - nr _****_or _****_route -n  
_**  
**_Write these two values down as you will require them later_**  


## Making the IP Address Static

The final part of the Static IP process is to **open **the original _cat /etc/network/interfaces_ file in edit mode.   
**In the LX Terminal type:**_**sudo nano/etc/network/interfaces**_  
  
Change the iface etho0 inet _dchp_ to **iface etho0 inet static**  
Next enter the previous information you collected in parts 1 and 2 , in a list below the statement **_iface etho0 inet static_, **  
**  
address **192.34..... etc _(inet address)_  
**broadcast **194.34..... etc _(Bcast)_  
**netmask **255.25..... etc _(Mask)_  
**network **192.34..... etc (_Destination_ )  
**gateway 1**92.34..... etc _(Gateway)_  
  
**Remember to replace the addresses with the ones from your network that you collected earlier.**  

![Picture](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/2335529.png?527)

## And to Finish with....

If you are comfortable with IP addressing schemes you can also change the **inet address**, the first one, to one of your choice - or keep it the same as it is. To complete the process reboot your Raspberry Pi,

**In the LX Terminal type:**  
**_sudo reboot_**

You are all finished, you could ping the IP address to check the settings,

**In the LX Terminal type:**  
**_ping 192.156.23.5 c-10_**

The** c-10** only sends 10 pings!
