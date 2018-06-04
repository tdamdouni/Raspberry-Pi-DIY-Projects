# HomeEnergy - Pi

_Captured: 2018-03-23 at 19:13 from [www.hackster.io](https://www.hackster.io/michael-nigbor/homeenergy-pi-cecfdf?utm_source=Hackster.io+newsletter&utm_campaign=fe36349df9-EMAIL_CAMPAIGN_2017_07_26&utm_medium=email&utm_term=0_6ff81e3e5b-fe36349df9-141949901&mc_cid=fe36349df9&mc_eid=1c68da4188)_

![HomeEnergy - Pi](https://hackster.imgix.net/uploads/attachments/451395/homeenergyprototype_wdOVnsfnxw.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

_**Note: This story is still evolving. I appreciate your patience as I find time to work on making it better.**_

This project got it's start because my local electric utility has started offering time of day rates. If you sign up, you get cheaper rates overnight and pay more during peak hours.

The problem is I have no idea how much power I use by the time of day.

There are expensive commercial solutions out there but I thought, maybe I can build my own using a Raspberry Pi I had laying around.

There are several similar projects on [Hackster.io](http://hackster.io/). Most are Arduino-based but there are a couple of Raspberry-pi based:

Here are the requirements I set out for the project:

  * Measure household electrical energy (in amps and kilowatts) at least once per minute. 
  * Measure the current passively. That is, I don't want to have to disconnect any wiring to hook my system up.
  * Open source hardware and software.
  * Show the most recent power reading
  * Show power as a function over the last 24 hours
  * Show power averaged by the hour of the day
  * Show power used in time buckets that correspond to my utility's TOD usage plan.
  * Be visible on my phone or a browser from anywhere
  * The web application should be secure (use SSL, hash passwords, secure login tokens, etc).
  * The web application should be small enough to run on the free tier of the popular cloud service providers.
  * Be expandable to measure other things in the future

This project means connecting things inside the power panel in your home. It almost goes without saying: _Working with electricity improperly can result seriously injury or death._

The decision to be safe is yours and yours alone. If you are not sure you have the skills and experience to do this, _a licensed electrician would be a great idea_.

  * A basic working knowledge of AC/DC circuits. 
  * [How to use a breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) and, if you decide to commit this to a soldered prototype board, how to solder. 
  * Basic Raspberry Pi skills (including the ability to install software). 

Although I've made my best effort to do a good job, I cannot rule out or accept responsibility for any errors or omissions that might exist in this project. I cannot accept any responsibility for any consequences that might result from those errors

By using this project, you agree to accept all liability.

The circuit shown below has three parts

  * L1 is an inductive current sensor. At 100 amps, it produces a current of 50 milli-amps. The sensor is inductive which means you just clip it isn't directly connected. It senses the magnetic field that surrounds the connector.
  * The circuit converts this current to something less than 5 volts, which the ADC can read.
  * An analog-to-digital converter that reads the voltage, converts it to digital values that the Pi can read.

R1 is a 100 ohm resistor which is placed across the inductive sensor. This so-called burden resistor converts current to voltage. The value is set using [ohm's law](https://en.wikipedia.org/wiki/Ohm%27s_law). At 100 amps, the sensor produces 50 milliamps. The 100 ohm resistor turns this into 5 volts.

The R2 and C1 are a [low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter), which reduces high frequency noise that interferes with accurate measurements. The cutoff frequency is about 70 hz.

The filtered voltage is fed into the analog input of the ADC 1115.

The ADC is controlled by the Python code running on the Pi, which is described more below.

My house, like most, has two phases or legs. That means two of these circuits. Fortunately, the ADC 1115 has 4 analog inputs.

The sampler Python code is designed to be placed in a cron entry. It takes one sample and exits. On my Pi, the sampler runs every minute.

The circuit produces an AC voltage ranging from -5 to 5 volts. The sampler reads these values at 860 times per second, calculates an [RMS](https://en.wikipedia.org/wiki/RMS) value and stores that in the SQLite3 table.

You might be wondering: Why sample AC voltage when you can convert AC to DC using diodes?

It's good question. The problem is that [most diodes need a few tenths of a volt to activate](https://learn.sparkfun.com/tutorials/diodes/real-diode-characteristics). It's surprisingly hard to rectify low voltages.

The transmitter Python script is also designed to be run from cron. It reads up to 20 entries from the table, transmits them to a web destination and then deletes them.

The web application can be anything that accepts an HTTP post with JSON like this:
    
    
    {    'readingdate' : 2018-03-01T13:14:00,    'current1' : 0.0,    'current2' : 0.0}
    

I'm working on a web application that does this and produces graphs and gauges of results.

Log into your Pi as the pi user.

Create a directory called HomeEnergy.

Download the files from the [repository at BitBucket.org](https://bitbucket.org/mnigbor/homeenergy-pi/overview).

Note: if you have software development skills, create a GIT repository in this folder, then use git clone. This makes updates a lot easier.

The sampler should work without any configuration changes. but if you decide to use the transmitter, you will need to configure the software, edit the [HomeEnergy.json](http://homeenergy.json/) file (using nano or any other text editor).

Use the directions on this link to c[onfigure cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md) to run the sampler.

The web application is a [Node.js](http://node.js/) application, so it's written in JavaScript.

![](https://hackster.imgix.net/uploads/attachments/451909/homeenergydashboard_VXp3wtzOQT.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Home Energy Dashboard_

The application uses Bootstrap for responsive design, so it looks good on desktop and mobile browsers alike. It's what's known as a single-page-application. All the data comes from REST endpoints, so the same application could serve data to a future mobile app.

It features a power gauge that updates every minute, a graph of the last 24 hours' usage and several other metrics. The application is still under development, but it already meets basic requirements.

The application runs on the "micro" servers many of the cloud service providers like Google and Amazon provide. It should cost between zero and $6/month to run. Several home energy monitors can publish to the same site.

Data is stored in a MySQL database. Sqlite can't do the complex SQL needed for the graphs.

Security is provided by SSL, hashed passwords and a cryptographically strong session-less token.

You don't need to run this application on the cloud. It should run fine anywhere you can run [Node.js](http://node.js/) and MySQL, including your Raspberry Pi.

The next steps:

  * Commit the breadboard circuit shown in the cover picture to a solder-type prototype board (a Pi hat). The parts are on order so this should be done soon.
  * Get a second current sensor and modify the sampler Python script to do both channels at the same time. It's also on order so it should be done soon.
  * Wire the device to my power panel. I'll take plenty of pictures so you can see how that goes. 
  * Publish the web application to a public GIT repository. It's almost good enough to share, just needs a little more testing.
  * Start measuring voltage in addition to amperage. This will require new circuit that I haven't thought much about. Maybe it could be built into the Pi's power supply.
  * Start researching methods to measure and analyze transients that occur when appliances such as air conditioners, refrigerators, etc turn on and off. It should be possible to "fingerprint" them and start building a power profile for each major appliance in the house.
![Power monitor circuit mogtvyz0ch](https://halckemy.s3.amazonaws.com/uploads/attachments/451367/power_monitor_circuit_MOgtVyZ0CH.PNG)
