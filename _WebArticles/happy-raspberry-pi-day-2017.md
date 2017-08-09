# Happy (Raspberry) Pi Day 2017!

_Captured: 2017-03-15 at 00:31 from [dzone.com](https://dzone.com/articles/happy-pi-day-2017?oid=twitter&utm_content=buffer39376&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)_

Once a year, we get 3.14--it's a big deal here outside of [Princeton](http://www.pidayprinceton.com/about). See, here we were privileged to have Mr. Einstein who was born 3/14. And well, [Pi](http://www.piday.org/million/) is just a cool number.

The weather this year is a bit rough with a late season Winter storm, but it won't stop my new [Raspberry Pi Zero W](https://www.raspberrypi.org/products/pi-zero-w/)! In what could only be credited to numerical magic, my brand new Rasberry Pi Zero W has arrived from Canada just before the storm. I highly recommend everyone get one of these cool little devices, it's only $10 US.

Let's run this cool little device in honor of the brilliant mathematician, cool number, and awesome device. I got two accessories which I think are critical. One is a miniHDMI to HDMI adapter, so I can configure things on the first boot. Another is a microUSB hub that I connected so I could add keyboard and mouse as needed. I have a lot of Raspberry Pi compatible power supplies, so getting plugged in is no problem.

## **Killer Features for $10!?**

  * 802.11 b/g/n wireless LAN (WIFI on board)
  * Bluetooth 4.1
  * Bluetooth Low Energy (BLE) - I will be doing some IoT stuff with this
  * 1GHz, single-core CPU and 512 MB RAM

There is an awesome new tool called [Pi Bakery](http://www.pibakery.org/) which is free for OSX, Linux, and Windows. It lets you easily configure and burn a MicroSD card for the Pi. This was fast and flawless.

Once I had it first set up, I switched over to SSH, which is my preferred mechanism. Just run an **ifconfig** to get your IP address.

Once I was logged in, I started to do some cleanup.

Next step was to make sure Java JDK was up to snuff and then I installed MiniFi to send data to my NiFi server.

I downloaded MiFi from Hortonworks and SCP'd it to Linux.

### **Example Log**

I also wanted MQTT ([GitHub](https://github.com/tspannhw/rpi-sensehat-mqtt-nifi)) because when I IoT, I like me some MQTT. So, I install a few Python [libraries](https://community.hortonworks.com/repos/79539/rpi-sense-hat-sensors-and-mqtt-utilities-for-iot-a.html) because Python is already installed on RPIWZ and is a great language for tiny devices. For some more details on this, see this [article](https://community.hortonworks.com/content/kbentry/55839/reading-sensor-data-from-remote-sensors-on-raspber.html) I wrote.

`pip install paho-mqtt`

`pip install flask`

### **Quick Example Code on RPIWZ**

I have been thinking for a followup I will try to run MXNet, PyTorch, or TensorFlow on this little guy. There's a good GitHub for [tensorflow cross-compile](https://github.com/snipsco/tensorflow-build).

![Image title](https://dzone.com/storage/temp/4640270-img-5904.jpg)

Yes, even in a fancy wood and laser cut plexiglass case, it's barely bigger than 2 US quarters. This little Raspberry Pi is the latest edition to my collection of Raspberry Pis, Microbits, and other assorted small computing factory devices.

I was going to run an infinite calculation of Pi on it, but I am already running a pointlessly long-running TensorFlow training (18,530 of 1,000,000) complete.

![Image title](https://dzone.com/storage/temp/4640452-img-5903.jpg)

## **References**
