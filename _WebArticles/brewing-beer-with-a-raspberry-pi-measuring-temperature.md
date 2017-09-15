# Brewing Beer With a Raspberry Pi: Measuring Temperature

_Captured: 2017-09-03 at 13:02 from [dzone.com](https://dzone.com/articles/brewing-beer-with-a-raspberry-pi-measuring-temperature#utm_source=RaspberryPi&utm_medium=email&utm_campaign=2017-09-01)_

I have Raspberry Pi 2 with Windows 10 IoT Core, and I plan to use it for some brewing activities. In this blog post, I introduce how to measure temperature with a Raspberry Pi using DS18B20 thermal sensors. This post is also an example of how easy it is to get started with your IoT stuff using Microsoft tooling.

In practice, I use this solution to monitor the freezing of Eisbock beer. Making 20L of beer freeze takes time. Depending on the weather outside, it's 10-18 hours. Using this solution, I don't have to open the bucket after every couple of hours to see if ice is forming, and I can also estimate how long it takes for beer to freeze.

**Update**: The source code of my [TemperatureStation solution](https://github.com/gpeipman/TemperatureStation) is available at [GitHub](https://github.com/gpeipman/TemperatureStation). The solution contains the IoT background service and a web application you can use right away. Readings are reported to MSSQL or Azure IoT Hub. Documentation is available at this [TemperatureStation wiki](https://github.com/gpeipman/TemperatureStation/wiki). Feel free to try out the solution.

## Electronics

This solution is pretty easy if you know at least something about electronics. I used the blog post [Thermal sensor connected via I2C](http://raspberrypi.tomasgreno.cz/thermal-sensor-i2c.html) by [Tomaš Greňo](http://raspberrypi.tomasgreno.cz/) for inspiration. It describes all this stuff in great detail, and if you are using Linux on your Raspberry Pi, then you can find everything you need to read temperatures there.

![RaspberryPi 2 and two thermal sensors solution to control freezing of beer.](http://gunnarpeipman.com/wp-content/uploads/2016/01/raspberrypi2-thermal.jpg)

> _RaspberryPi 2 and two thermal sensors solution to control freezing of beer._

_RaspberryPi 2 and two thermal sensors solution to control the freezing of beer.  
The solution is also ready for my conference trips, and it survives travel._

Some advice:

  1. All these components are cheap, and I found them from local online electronic stores.
  2. DS2482S-100 and MS-DIP-to-SO-8 reduction are so small that you better use the right tools for or ask for help from a friend who has the tools and who knows how to use them.
  3. If you plan to connect more sensors to the DS2482S-100, make sure the DS2482S-100 chip you buy supports the number of sensors you have.
  4. The colors of the DS18B20 wires are described in the component documentation.
  5. When connecting your solution to your Pi, make sure you connect the wires to GPIO pins correctly.
  6. If possible, pack your sensor well so there's not much chance you accidentally break it.

> From this point on, I assume you have your sensor solution done and connected to the Raspberry Pi. Also, I assume you have a development box running on Windows 10 and you also have Visual Studio with Universal Windows Applications and Windows 10 IoT templates installed.

## Reading Temperatures

Run Visual Studio and create a new IoT background application project.

![Visual Studio 2015: Create new Windows IoT Core application](http://gunnarpeipman.com/wp-content/uploads/2016/01/vs2015-create-iot-background-application_thumb.png)

> _Visual Studio 2015: Create new Windows IoT Core application_

When the project is created, open the NuGet package manager and add the Rinsen.OneWire package to your solution. [Rinsen.OneWire](https://github.com/Rinsen/OneWire) is the implementation of the OneWire protocol by [Fredrik Rinsen](https://github.com/Rinsen). It's written in C# and has built-in support for DS18B20 and DS18S20 sensors.

Now let's write some code. In short, we have to write something like this:

  1. When the background application is run, initialize everything to read sensors.
  2. Add the code for the application shutdown so we politely leave the application.
  3. Use a timer to read values from sensors.
  4. Write values somewhere (the debug window in our case).

Here's the sample code for the StartupTask class that Visual Studio creates automatically.

Build it, deploy it to the Raspberry Pi and run it on Visual Studio. You should see output like this:

![Temperature readings from sensors](http://gunnarpeipman.com/wp-content/uploads/2016/01/raspberrypi-temperature-debug-output.png)

> _Temperature readings from sensors_

If you get the following error...

`Exception thrown: 'System.IO.FileNotFoundException' in Rinsen.IoT.OneWire.dll   
WinRT information: Slave address was not acknowledged.`

... then try to play with the ad0 and ad1 arguments of the OneWireDeviceHandler class. By default, these boolean arguments are true. I had to set these to false to make my solution work.

## Wrapping Up

Windows 10 IoT Core and Visual Studio tooling make it very easy to build IoT solutions. Of course, we don't always get away from problems so easily like we did right now, as there aren't libraries for everything we want to do, but still, we have very good tooling that makes development way easier. Although we wrote temperature readings to the debug window, we can go further and send the values to some database or a Microsoft Azure service.

## Brewing Beer With a Raspberry Pi: Table of Contents

  1. **Brewing Beer With a Raspberry Pi: Measuring Temperature**
