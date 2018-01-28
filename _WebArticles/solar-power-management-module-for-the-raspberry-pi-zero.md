# Solar Power Management module for the Raspberry Pi Zero

_Captured: 2017-11-16 at 10:24 from [www.pisolman.com](http://www.pisolman.com/)_

PiSolMan can be a very useful module to implement solar powered applications with your Raspberry Pi. Without precise information about the battery state, many times the system runs out of power without previous notice, often when most needed. However, having constant information about the battery state, power consumption, or even charger efficiency you can manage the system in such a way that power is saved when possible and used when most needed.

![](http://www.pisolman.com/images/app1.jpg)

Wireless Camera applications are very demanding in terms of energy. Although the Raspberry Pi Zero energy consumption is relatively small, when adding the Pi Camera module and a wireless modem (3G/4G or WiFi) the situation changes drastically. PiSolMan is capable of powering such a system from solar energy while continuously monitoring and optimising the energy consumption.

A weather station in itself does not consumes too much power. However, if a Wi-Fi or 3G module is needed, the majority of the power is consumed by these devices. With a simple script running on the Raspberry, the connection could be disconnected and used only when needed based on the power level information provided by PiSolMan.
