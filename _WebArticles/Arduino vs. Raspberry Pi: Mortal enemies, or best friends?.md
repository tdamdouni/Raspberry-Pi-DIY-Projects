# Arduino vs. Raspberry Pi: Mortal enemies, or best friends?

_Captured: 2015-11-12 at 10:15 from [www.digitaltrends.com](http://www.digitaltrends.com/computing/arduino-vs-raspberry-pi/)_

[ ![RasperryArduinoVersus](http://icdn8.digitaltrends.com/image/rasperryarduinoversus-640x0.jpg) ](http://s3.amazonaws.com/digitaltrends-uploads-prod/2015/02/RasperryArduinoVersus.jpg)

In the DIY maker community, there's no shortage of options designed to provide you with a little electronic control over your projects. Two of the most popular options for doing so are the budget-friendly Raspberry Pi, a system-on-a-chip (SoC) that runs a full version of Linux and was designed with teaching in mind, and the Arduino, a micro-controller with a large community of support and hundreds of expansion chips (aka shields).

However, while the initial announcement of the Raspberry Pi may have led many to proclaim the Arduino obsolete, such a declaration might be premature. The fact is, the two devices have different uses and advantages, each of which is achieved through different methods. The stark specification differences between the two also renders direct comparisons somewhat moot on paper, especially considering the Arduino's 16MHz processor falls a little short of the Pi's 900 MHz chip.

**Related: **[Get under the crust of these 10 fun and easy Raspberry Pi projects](http://www.digitaltrends.com/computing/raspberry-pi-projects/)

### Raspberry Pi

![RaspberryPi2](http://icdn4.digitaltrends.com/image/raspberrypi2-325x325.jpg)

For all intents and purposes, the Raspberry Pi is a fully functional computer. It has all the trappings of a computer, with a dedicated processor, memory, and a graphics driver for output through HDMI. It even runs a specially designed version of the Linux operating system. That makes it easy to install most Linux software, and lets you use the Pi as a functioning media streamer or video game emulator with a bit of effort.

Though the Pi doesn't offer internal storage, you can use SD cards as the flash memory for the entire system, allowing you to quickly swap out different versions of the operating system or software updates to debug. Because of the device's independent network connectivity, you can also set it up for access via SSH, or transfer files to it using FTP.

### Arduino

![Arduino](http://icdn5.digitaltrends.com/image/arduinouno-325x325.jpg)

Arduino boards are micro-controllers, not full computers. They don't run a full operating system, but simply execute written code as their firmware interprets it. You lose access to the basic tools an operating system provides, but on the other hand, directly executing simple code is easier, and is accomplished with no operating system overhead.

The main purpose of the Arduino board is to interface with sensors and devices, so it's great for hardware projects in which you simply want things to respond to various sensor readings and manual input. That might not seem like a lot, but it's actually a very sophisticated system that allows you to better manage your devices. It's great for interfacing with other devices and actuators, where a full operating system would be overkill for handling simple read and response actions.

### Power

The two systems have very different power requirements. The Raspberry Pi requires constant 5V power to stay on, and moreover, should be shut down via a software process like a traditional computer. Arduino, on the other hand, begins executing code when turned on and stops when you pull the plug. To add functionality, you either wire directly into the pins on the Arduino board or stack chips called "shields" on top of the base unit. There are hundreds of shields, each of which is designed to perform a different task, interface with certain sensors, and work with one another to build a complete control unit.

Portability is an issue with the Pi, given it requires more than simply plugging in a couple AA batteries. The device requires you to set up a power supply and some additional hardware in order to provide it with the constant power needed. The process is a bit simpler on the Arduino, as you merely need a battery pack that keeps the voltage above a certain level, along with a basic shield to manage the power. Even if the power drops on the Arduino, you won't end up with a corrupt operating system or other software errors. It will just start running code when it's plugged back in.

### Networking

The Pi has a built-in Ethernet port, which allows easy access to any network with little setup. Wireless Internet on the Pi isn't hard to achieve either, you just have to buy a USB Wi-Fi dongle and install a driver. Once you're connected, you can use the OS to connect to [Web](http://www.digitaltrends.com/web/) servers, process HTML, or post to the Internet. You can even use it as a VPN or print server.

Unfortunately, the Arduino isn't built for network connectivity directly out of the box. It requires a bit more tinkering to set up a proper connection, though it is possible. You'll need an extra chip outfitted with an Ethernet port, and you'll need to do some wiring and coding in order to get everything up and running -- which is enough of a process that some vendors sell comparable versions of the Arduino with built-in Ethernet.

### Sensors

While both the Pi and Arduino have a number of interface ports, it's much easier to connect analog sensors to the Arduino. The microcontroller can easily interpret and respond to a wide range of sensor data using the code you put on it, which makes it great if you intend to repeat a series of commands or respond to sensor data as a means of making adjustments to servos and devices.

The Pi, on the other hand, requires software to effectively interface with these sorts of devices, which isn't always what you need if you're just trying to water plants or keep your beer at the right temperature. It's not uncommon to use both in a project, with the Arduino acting as a control board that executes commands issued by the Pi's software, before the sensor information is fed back for recording or responding to.

### Match made

So which one is right for you? There isn't a clear answer, because it depends heavily on your project.

When should you choose Arduino? When the main task is reading sensor data and changing values on motors or other devices. Given the Arduino's low power requirements and upkeep, it's also a good choice if your device will be constantly running and requires little to no interaction.

When should you go with Raspberry Pi? When you would otherwise complete your task with a personal computer. The Pi makes a slew of operations easier to manage, whether you intend to connect to the Internet to read and write data, view media of any kind, or connect to an external display.

Given the two devices accomplish different tasks, it's best to use both in some instances. There are a number of options for connecting the two devices, which will give you client-side access to the settings and code via the Pi, while the Arduino handles the actuation of devices and gathers data from the sensors. There are a number of ways to go about making the connection, whether you prefer USB, a local network, or by running some of the IO ports on the Arduino into the Pi.
