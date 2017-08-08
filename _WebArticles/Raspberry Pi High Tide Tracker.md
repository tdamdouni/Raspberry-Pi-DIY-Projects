# Raspberry Pi High Tide Tracker 

_Captured: 2016-01-03 at 23:37 from [www.averagemanvsraspberrypi.com](http://www.averagemanvsraspberrypi.com/2015/12/raspberry-pi-high-tide-tracker.html)_

![Raspberry-Pi-High-Tide-Tracker](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/Raspberry-Pi-High-Tide-tracker-2-777x437.jpg)

> _Next high tide is at 03:53...maybe I'll give this one a miss..._

Many of you will know that I live in sunny [Southend-on-Sea](https://en.wikipedia.org/wiki/Southend-on-Sea), and from the name of my home town you can guess that I live pretty close to the water.

Due to our close proximity to the ocean, weekends usually involve a family walk along the seafront taking in the views and fresh sea air. Unfortunately we're usually quite unlucky with the timing of these leg stretching excursions, mostly seeing a muddy estuary due to the tide being out.

I started thinking about how I could keep an eye on tide times, and also remind myself to put down the electronics and get out of the house once in a while. Of course the [Raspberry Pi](http://www.amazon.co.uk/gp/product/B00T2U7R7I/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B00T2U7R7I&linkCode=as2&tag=aver03-21) came to mind - because we all love an excuse to make a little project don't we!

I ended up making a display that checks the next high tide and pushes that to a 7-segment display connected to my Raspberry Pi. Let me show you what I made…

![Southend seafront](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/Southend-Seafront.jpg)

> _Southend: It's not all amusements, rides and crime after all…_

## Hardware Used

### RasPiO 7-Seg

There are lots of ways I could display the high tide information, but I decided to try it out on my new [RasPiO 7-seg kit](http://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python) which uses a 4 digit 7-segment display running solely on GPIO pins (no IC required). I've tried displays that run off ICs, so it was fun to try something new and also finally use more of the 40 GPIO pins the latest Pis offer.

The kit also gave me everything I needed to prototype with, which was an added bonus.

![RasPiO 7-Seg Kit](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/7-seg-kit.jpg)

> _The 7-Seg kit from RasPiO_

### ProtoPal

I also used one of my own products - the [ProtoPal](http://www.protoboards.co.uk/2014/11/ProtoPal.html) - to fit all the parts into a nice small soldered package. I designed this board to make it easier to turn breadboard projects into more permanent items on the new breed of Raspberry Pi - you'll see how later on in this post.

![ProtoPal Board for Raspberry Pi](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/ProtoPal-for-Raspberry-Pi.jpg)

> _My very own ProtoPal board. Very handy for making projects more permanent._

### Laser Cut Casing

A bit of a new obsession of mine, I made a simple 2-piece casing with spacers to mount the project inside. The smoked black panels let the light of the display shine through, making a nice subtle and tidy display unit.

Later on in this post I explain how to get your own casing cut.

![Raspbery Pi 7 segment display casing](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/Laser-cut-Raspberry-Pi-casing.jpg)

> _Stealthy: When the display isn't lit the unit is very minimalist_

## The Project - High Tide Tracker

So how does it work? Let's take you through it…

### It's Simple!

The code used in this project is actually a mash-up of the Python I learnt from two previous projects - my [Raspberry Pi Social Network monitor](http://www.averagemanvsraspberrypi.com/2015/07/raspberry-pi-pygame-social-network-monitor.html) (based on the RasPi.TV [Kickstarter tracker project](http://raspi.tv/2014/programming-a-kickstarter-tracker-in-python-part-1)) and the clock example that came with the 7-Seg kit. It's great to learn programming from others, but it's even better if you learn them well enough to remember, re-use and combine that code later on as well.

First let's first summarise what my code does:

  1. Setup - Imports, GPIOs, segment characters etc
  2. URL check (every hour or so) - check the URL and pull back next high tide time
  3. Display next high tide time on the display

It really is that simple - start up, check the URL and display data. I haven't added anything else at this stage which means it's still a bit 'rustic', although I may work on another version that includes more features with buttons/LEDs etc.

## Wiring

As you would expect, I prototyped and tested this project on a [breadboard](http://www.amazon.co.uk/gp/product/B0040Z4QN8/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B0040Z4QN8&linkCode=as2&tag=aver03-21) before going anywhere near my soldering iron.

The wiring for the display is similar to the example clock project for the 7-Seg kit I'm using, as I had used that project as a starting point to get the display up and running (I just changed some pins to make things easier to solder). You can read more about that example project over at [RasPi.TV](http://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python) which will show you the default pin mapping etc.

![7-Segment display kit breadboarded](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/7-seg-prototyping.jpg)

> _My 7-Seg kit wired to a breadboard_

## The Code

Time to get our hands dirty. This project is an interesting one as it combines code from two example projects over at RasPi.TV. Alex Eames is always posting useful 'codey stuff' over on his blog, which I usually recreate at home to learn a bit more Python.

I borrowed code from his [Kickstarter Tracker project](http://raspi.tv/2014/programming-a-kickstarter-tracker-in-python-part-1), and also his [7-Seg display project](http://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python) (which is where I got my display kit from), and then merged the two examples with a few other changes.

Feel free to [download my code from PasteBin](http://pastebin.com/rGr4PwEX) before looking at the notes below. I have added quite a lot of comments to help you along.

### Import Lines

First let's take a look at the imports section. There are some obvious ones - we import GPIO of course, then our old friend time.

Then we come to a few not-so-common imports. 'subprocess' and 'os' are used, but I'm not sure exactly which part of the code they run. Usually I associate these with the 'os.system' style commands, but we don't use any here?

The final 'urllib2' import is the part that lets us scrape a URL for lines.

678910
`import` `RPi.GPIO as GPIO``import` `time``import` `subprocess``import` `os``from` `urllib2 ``import` `Request, urlopen, URLError`

### Setup Lines

Lines 12-41 runs the setup section, getting everything in place and ready for our main code to run.

First we set the GPIO mode (I've opted for BCM), then define which GPIO ports will be used for the 8 LED segment pins on the display. I think the order of these pins is important here, so if you copy this project and change the pins make sure you replace them in the right order.

1213141516
`# SET GPIO MODE``GPIO.setmode(GPIO.BCM)``# GPIO PORTS FOR THE 7SEG PINS (I think the order is important, in case you change these)``segments ``=` `(``17``,``9``,``13``,``5``,``11``,``27``,``19``,``6``) ``# ALL HAVE RESISTORS`

Next we set the segment ports to outputs. We do this because we want the Pi to send power to each LED segment when requested.

18192021
`# SET THE SEGMNENT DISPLAY GPIO PORTS TO OUTPUTS``for` `segment ``in` `segments:``GPIO.setup(segment, GPIO.OUT)``GPIO.output(segment, ``0``) ``# SET ALL SEGMENTS TO LOW`

After that we set the remaining 4 GPIO port numbers. These are the GPIO pins that activate each character on the display, and require no resistor. We then set these to outputs just like the LED pins.

23242526272829
`# GPIO PORTS FOR THE DIGIT 0-3 PINS ``digits ``=` `(``3``,``22``,``10``,``26``) ``# NO RESISTORS``# SET THE DIGIT PINS TO OUTPUTS ``for` `digit ``in` `digits:``GPIO.setup(digit, GPIO.OUT)``GPIO.output(digit, ``1``) ``# SET ALL SEGMENTS TO HIGH`

Lastly in this section we define the '1s' and '0s' to set different LEDs on/off to make numbers on our display. Play with those numbers and you'll see different segments light up. Luckily this has already been done for me in the example code that came with my 7-Seg kit.

3132333435363738394041
`num ``=` `{``' '``:(``0``,``0``,``0``,``0``,``0``,``0``,``0``),``'0'``:(``1``,``1``,``1``,``1``,``1``,``1``,``0``),``'1'``:(``0``,``1``,``1``,``0``,``0``,``0``,``0``),``'2'``:(``1``,``1``,``0``,``1``,``1``,``0``,``1``),``'3'``:(``1``,``1``,``1``,``1``,``0``,``0``,``1``),``'4'``:(``0``,``1``,``1``,``0``,``0``,``1``,``1``),``'5'``:(``1``,``0``,``1``,``1``,``0``,``1``,``1``),``'6'``:(``1``,``0``,``1``,``1``,``1``,``1``,``1``),``'7'``:(``1``,``1``,``1``,``0``,``0``,``0``,``0``),``'8'``:(``1``,``1``,``1``,``1``,``1``,``1``,``1``),``'9'``:(``1``,``1``,``1``,``1``,``0``,``1``,``1``)}`

Next let's jump into the main program.

### Main Program

My main program is in a try/except block, which just means it'll do everything we ask it to do in the 'try' block, but if something goes wrong (almost guaranteed!) it will always run the code in the 'except' block.

This is very helpful as it means we can make sure tasks like cleaning up the GPIO pins are always completed before the program throws its toys out of the pram.

43
`try``:`

126
`except` `KeyboardInterrupt:`

The main program within this 'try' block is made up of a few 'ifs' and 'else' blocks that do the following:

  1. Check if the time is right to check the URL again for an updated tide tme
  2. If the time is right, request and open the URL
  3. Pull back the URLs source code lines (same as using 'view source' in your browser)
  4. Find the line that includes the unique string we have asked it to look for
  5. Split that line up to leave us with 4 characters (the next high tide time)
  6. Push the new high tide time to the display
  7. Ask the program to wait an hour before checking again

There are some exceptions built into this which will run if the WiFi is down or the Pi isn't getting a response from the website.

I have posted that section of the code below (you'll need to expand it) but I'm not going to post line by line explanations here as the comments in the [PasteBin file](http://pastebin.com/rGr4PwEX) should explain everything. If you get stuck, please add a comment below.

There is a 'def' section (module) below this that defines what the display should show if there is an error (the error section refers to this module). I set this to be a square of LEDs, just to let me know that something has gone wrong.

It's using the same method as in the setup section - set digits to high to activate characters, then define the individual LED segments to turn on:

108109110111112113114115116117
`def` `errsquare():``# Set digits to low to activate digit``GPIO.output(``3``, ``0``)``GPIO.output(``22``, ``0``)``GPIO.output(``10``, ``0``)``GPIO.output(``26``, ``0``)``# Set segment high to activate segment``GPIO.output(``17``, ``1``)``GPIO.output(``5``, ``1``)`

At the end of this 'try' block there is a short line of code that is actually very important. It tells the 'try' block to run the main program module when it starts:

`#Run main program:``mainprog()`

### Except Block

Finally we have the except block that I mentioned earlier. It's pretty simple, just cleaning up the GPIOs and printing a few lines to let us know what's going on:

122123124125126127128129130131132133134135136137138139
`#======================================================================``# EXCEPT BLOCK``# This will run if there is an error or we choose to exit the program``except` `KeyboardInterrupt: ``# USE THIS OPTION FOR DEBUGGING``print` `"EXIT SCRIPT"``time.sleep(``0.5``)``# Clean up GPIOs``print` `"PERFORMING GPIO CLEANUP"``time.sleep(``0.5``)``GPIO.cleanup() ``# Clean up the gpio pins ready for the next project.``# Exit program``print` `"\--- EXIT NOW ---"``time.sleep(``0.5``)``quit()`

That's the code finished. Whilst some sections might look a bit scary ("if hasattr(e, 'reason'):" for example) it's actually very simple if you look at it in terms of blocks of functions/commands rather than line by line.

If you have any questions just add a comment.

## Soldering The Project

With the wiring and code working, it was time to make it a little more permanent.

Lately I'm just not happy with a project unless it's usable in a realistic way. This project works fine on a breadboard but it's not practical to have this out on display 24/7.

This is where add-on prototyping boards come in, and it's also why I created the [ProtoPal](https://shop.pimoroni.com/products/protopal) board. Projects need to be released into the real world, but not everyone has the skills or funds to make a custom PCB for every project they make. Perfboard works fine, but chopping up a big ol' generic panel of perf can look uglier than Pete Burns!

![ProtoPal soldering](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/ProtoPal-board-Soldering.png)

> _Plan and take it slow, one wire at a time!_

Using a prototyping board, designed to fit the Raspberry Pi and break out the GPIO pins in a neat little package, let's you get as close to the real thing as you can, and looks great too.

My only advice here is to plan it in your head as much as possible, working out which wires need to be soldered first, last etc.

![ProtoPal Soldered](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/ProtoPal-7-segment-display.png)

> _All soldered up and code working_

## Making a Case

I now had a pretty cool soldered project that I can clip on and off of my Pi, but I wanted something suitable for display at home at all times. I had taught myself how to design SVG files for laser cutting as part of my [Pi Wars robot project](http://www.averagemanvsraspberrypi.com/tag/pi-wars), so I decided to make something similar for my tide tracker as well.

![High-tide-tracker-case](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/High-tide-tracker-inside.jpg)

> _The inside of my casing: It's a simple construction mad of 2 acrylic panels and spacers/bolts_

I wanted it to be cheap and simple, so I used the same construction method as I used with my AverageBot robot - two panels of acrylic with spacers in between. It doesn't sound like much but the end result is effective and easily changed when you want to add more such as switches, engraving etc.

![High-tide-tracker-casing-cut-outs](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/12/High-tide-tracker-rear.jpg)

> _The rear of my casing has cut outs for the SD card and power connection_

If you have an [A+ Raspberry Pi](http://www.amazon.co.uk/gp/product/B00Q8MM4PI/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B00Q8MM4PI&linkCode=as2&tag=aver03-21), a [ProtoPal](https://shop.pimoroni.com/products/protopal) and want to get your own laser cut casing made as well, here is the SVG file. You can edit it in Inkscape and get them cut online at places like [RazorLab](http://www.razorlab.co.uk/make-a-product/) who will give you a price online for the material and colour of your choice, and then post it to you as well.

_Remember: the front section can't be a solid colour or you won't be able to see the display through it._

**SVG casing file:** [click here to download](https://www.dropbox.com/s/2yovgp67qbb4b38/7seg%20chassis%200.1.svg?dl=0).

You'll also need 4x 25mm M2.5 spacers and 8x 6mm M2.5 bolts. I opted for hex socket allen head screws as they look good.

## Summary

Winter walks to the seafront will now be better than ever thanks to my new high tide tracker!

It's a bit of an odd project, but I couldn't resist making something with the two example RasPi.TV projects put together - URL line hunting code mixed with the 7-seg kit running off the GPIO.

The best bit is that I can change the code to track whatever I like - currency, share prices, time, Kickstarter campaign progress and lots more.

The hardest part of this project though, is getting my wife to let me have this on display in the house. It's like negotiating with terrorists at times…

Until next time…
