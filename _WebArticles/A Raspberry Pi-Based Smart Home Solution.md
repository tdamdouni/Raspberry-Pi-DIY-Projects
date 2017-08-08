# A Raspberry Pi-Based Smart Home Solution 

_Captured: 2016-05-19 at 15:10 from [macoscope.com](http://macoscope.com/blog/a-raspberry-pi-computer-based-smart-house-solution/)_

Here at Macoscope, Community is inscribed among our Core Values. Seeing that we don't have either a receptionist or a front desk, and our office is basically a big house, opening the front gate for visitors and deliveries quickly grew into a problem. To open it, we needed to press a button near the main doors, and the inconvenience of having to step away from our work to walk up to the door multiple times a day terribly annoyed us. so it's not convenient and people were annoyed of going to do this multiple times a day. What else could we have done but put our heads together, like a true Community would, and try to solve it with a little bit of technology that we're so good at!

![gatekeeper](http://cdn.macoscope.com/blog/wp-content/uploads/2016/04/raspberry.png)

Well, what if we could check out who's at the front gate and open it directly from our computers? We're developers after all, aren't we?

## The On/Off Switch

Relay is a device that allows us to manipulate the flow of electrical current using signals from the Raspberry Pi. We need to be able to interact with electrical current in order to simulate pushing a button like we normally do to open the front gate. Thanks to the DIY movement there a lot of relays available for Raspberry Pi, so we have that going for us. In our case, a simple single-channel relay with opto-isolation (safety first, kids) will be enough.

## Raspberry Pi Camera Module

Obviously, we want to know who's out there ringing the bell. Is it the postman? Has our weekly delivery of juices arrived? Or maybe one of us forgot their keys? Once again, the DIY and IoT movements came to our rescue with the [Raspberry Pi camera module](https://www.raspberrypi.org/products/camera-module/). It's easy to connect to the Raspberry thanks to a dedicated interface and it works out of the box. However, there's one more thing we need to take care of, and that's video streaming software. That's where [motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) comes in -- it's great piece of open source software with the ability to detect movement, but we'll be using it only as a streaming server. Motion provides a http service with a mJPEG stream, so it works with all major modern browsers.

## Raspberry Pi, Relay, and Camera Setup

![Untitled Sketch_bb](http://cdn.macoscope.com/blog/wp-content/uploads/2016/04/Untitled-Sketch_bb-800x491.png)

> _The picture above is a simplified diagram of how the entire setup is connected together._

Thanks to the mDNS protocol, we don't need to remember what the IP address of our Raspberry is. A relay, a couple of meters of cable, 15 minutes with a screwdriver, a multimeter, and a sip of Scotch, and we had our setup up and running. Lucky for us, most Linux distributions come with Python built-in, and raspbian (it's Debian GNU/Linux ported to Raspberry Pi if you're not familiar with the name) is no different. Believe it or not, that basically covers most of our needs. Python is great for creating Web-based (we used the [Flask](http://flask.pocoo.org) framework) interfaces in a flash, and we also used python-gpio to trigger the relay:
    
    
    import RPi.GPIO as GPIO
    from time import sleep
    
    # set GPIO to to mode BCM to get nice
    # numbers for GPIO ports
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    # relay is attached to GPIO PIN #18
    GPIO.setup(18, GPIO.OUT)
    
    # turn relay on for 5 seconds
    GPIO.output(18, GPIO.LOW)
    sleep(5)
    GPIO.output(18, GPIO.HIGH)

So what's the flow when someone rings the bell? Everyone within earshot can go to their browser of choice, enter the URL to see the video stream and click "Open" to remotely open the gate.

### OS X Menu Bar App

We are a software development company, after all, so we quickly put together an app that sits in the menu bar of OS X and offers the same capabilities that the Web interface does, that is checking out who's at the gate and opening it remotely.

![Screen Shot 2016-04-15 at 16.34.44](http://cdn.macoscope.com/blog/wp-content/uploads/2016/04/Screen-Shot-2016-04-15-at-16.34.44.png)

It's [open sourced](http://github.com/macoscope/GateKeeper) and bundled with the code that is supposed to run on the Raspberry, so it'll run out of the box if you decide to follow a similar setup.

We will be making some improvements to the app over the coming months, including authorization via Google Apps OAuth to prevent malicious requests to the endpoint responsible for opening the gate, even if it's available only on the local network.

### Final Thoughts

  * Because of pre-existing conditions and the design of our setup, we had to connect the Raspberry with the gate using a cable that has to go through the window, so it may cause us some problems in the future. 
  * Our network is a mixed 2.4GHz and 5GHz setup, but it turned out we had to force a 5GHz connection on the Raspberry. Before we realized what needs to be done, we spent nearly 3 weeks trying to figure out why the Pi is constantly dropping the connection (we even started thinking that by some coincidence our office building is surprisingly well shielded when it comes to wireless networks).

### Quirks

  * It is good idea to lower the resolution of the video stream due to bandwidth limitations (imagine 19 people looking at a FullHD stream at the same time on something as simple as Raspberry Pi) 
  * motion, the application we're using to stream video from the Raspberry, has tendency to hang after few days, so it's not a bad idea to restart it via cronjob.

### Setting Up a Smart Home Using a Raspberry Pi

Thanks to the IoT and DIY movements, as well as the wide adoption of platforms like the Raspberry Pi, it is now possible to make your office or home smarter fairly easy using technologies easily available to the majority of good developers.

Got inspired? [Email](mailto:hire-us@macoscope.com) us and see how our design and development services can drive business value for you.
