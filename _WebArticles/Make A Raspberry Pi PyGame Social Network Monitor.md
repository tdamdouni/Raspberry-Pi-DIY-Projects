# Make A Raspberry Pi PyGame Social Network Monitor 

_Captured: 2016-01-03 at 23:34 from [www.averagemanvsraspberrypi.com](http://www.averagemanvsraspberrypi.com/2015/07/raspberry-pi-pygame-social-network-monitor.html)_

![Make A Raspberry Pi PyGame Social Network Monitor](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Make-A-Raspberry-Pi-PyGame-Social-Network-Monitor-777x437.jpg)

> _Keep an eye on your followers with your PiTFT!_

It must have been at least a year since I bought my [Adafruit PiTFT.](http://www.amazon.co.uk/gp/product/B00H9B1DTA/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B00H9B1DTA&linkCode=as2&tag=aver03-21&linkId=UA2GNQYQFUNXYS3E) At that time I was reasonably new to the scene but couldn't resist buying what looked like a micro flat-screen TV for my Raspberry Pi.

What followed was a lot of disappointment. Being a Raspberry Pi novice, I assumed this little GPIO-connected display would be 'plug n' play' just like any other HDMI monitor. It's not quite that simple…as many will know. I found the screen difficult to use and couldn't see any real usage for it - so it went to the back of the cupboard.

Zoom forward 12 months and I'm slightly more educated on the Raspberry Pi, and have the confidence to try my hand at more difficult projects and code. I recently decided to return to the PiTFT to try something similar to [MrUkTechReview's Internet Radio](http://home.uktechreviews.com/Raspberry/Pi%20blog/files/RaspberryRadio.html) - using PyGame to make a nice graphical display with buttons and all sorts of magic.

Having [already made](http://www.averagemanvsraspberrypi.com/2013/08/average-mans-raspberry-pi-internet-radio.html) an internet radio, I had a good think about what would be a useful project for me - to warrant having my display on show in the house at all times (regardless of the wife's stroppy protests).

A project was born - I would make a Raspberry Pi PyGame social network monitor!

**A Social Network What?!**

I have a few different social networking accounts, and whilst it's not really that important, I like to keep a check on the number of people following or subscribing to me on these networks. There's something exciting about having thousands of strangers follow your every move!

Whilst I can check my various apps for this information, I thought it would be cool to have a little [Raspberry Pi](http://www.amazon.co.uk/gp/product/B00T2U7R7I/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B00T2U7R7I&linkCode=as2&tag=aver03-21&linkId=PESPXPOWKGSFC5BQ) on display showing the stats that I'm interested in.

![Raspberry Pi social network monitor](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Social-network-monitor-front.jpg)

> _Twitter, Facebook, Google+ and more - data from most websites is easy to display._

**Where To Start?**

My first hurdle - I didn't have a clue how to make any kind of GUI ([Graphical User interface](https://en.wikipedia.org/wiki/Graphical_user_interface)) or display on the PiTFT.

A lot of people said "_Oh just use Tkinter it's simple_" or "_PyGame is really easy just give it a go_". These people do not understand us 'Average' folk. They don't appreciate that we work 9-5 office jobs, have relationships to manage, weight problems to ignore and still think that Python is a snake.

We are the reserves of the coding world - weekend warriors who don't usually remember the function or command they learnt the week before.

So, it was off to Google as always…

![Google Search for PiTFT GUI](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Google-Search.jpg)

> _Even the mighty Google struggled to help…_

**We'll Be Using PyGame**

If you search Google for a PiTFT GUI, you're likely to come across the two main contenders - [Tkinter](https://wiki.python.org/moin/TkInter) and [PyGame](http://www.pygame.org/news.html).

I'm not even going to touch on Tkinter - I had little luck finding any tutorials or guides for that, at least not any pitched at a simple enough level for me to understand.

PyGame seems to have a bit more in the way of supporting materials and examples, but it's still not an easy thing to grasp at first.

I struck gold when I came across [MrUkTechReview's basic sample code](http://home.uktechreviews.com/Raspberry/Pi%20blog/files/pygame-menu.html) for PyGame with the PiTFT. Spencer has kindly uploaded a Python file to DropBox to help get people started, and this is exactly where I kicked off.

**Getting To Grips With Pygame**

First, let's take a look at the sample menu that shows when you run Spencer's file:

![PiTFT Sample PyGame GUI](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Sample-interface.jpg)

> _MrUKTechReview's sample PiTFT GUI using PyGame_

Looks basic enough, the code must be short and simple…right? Not quite.

PyGame wasn't instantly obvious to me, so I had to spend some time working out how the code worked. I took Spencer's menu example and slowly worked out what each line or block of code was doing, why it was doing it and seeing what happened if I changed or removed it.

I'm a bit funny like that - I'm never happy unless I know what's going on in a Python script. This is why I like to comment my Python files to death. I'm sure many would frown at my code commenting style, but it works for me.

**PiTFT Social Network Monitor**

After working out how PyGame works with the PiTFT I started working on my own display, which eventually turned in to my Raspberry Pi social network monitor.

The idea all started after seeing a Kickstarter Tracker tutorial over at [RasPi.TV](http://raspi.tv/2014/programming-a-kickstarter-tracker-in-python-part-1) that looked into a Kickstarter page source code, chose the specific info it was looking for (funded rate etc) and printed it in terminal. I had an idea to do something similar, but instead of Kickstarter I would direct my code to my social networking profiles to pull back the counts of followers and subscribers.

The monitor checks my social networking accounts every 45 seconds and updates the follower/subscribe count for each of them.

It also shows the time, date and the Pi's temperature, as well as a nice little image on the right hand side.

![PyGame date, time and temperature on a PiTFT](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Date-time-and-temperature.jpg)

> _Date, time and Pi temperature are displayed_

So…how did I make it?

**PiTFT Social Network Monitor - Code Breakdown Step By Step**

I'm going to take you through my entire Python file, step by step. That's what I would have liked to have found when I was trying to learn, so I hope this is useful to someone, someday!

The full code won't fit on the page due to the wide indentation, so download and open the [PasteBin file](http://pastebin.com/ch3qFKai) in your favourite text editor to follow along. I use [NotePad++](https://notepad-plus-plus.org/).

The code pasted in this blog has very few of the original '#' comment sections included. I **really recommend** reading the full comments in my Python file as you follow this, they'll help answer any questions as we go along.

Also, you shouldn't need to install anything as the packages being used should all come with Raspbian.

Ready? Let's begin

Imports

As with any Python script, we need to import the modules that we want to use in the script. Pretty self explanatory:

222324252627
`import` `sys, pygame``from` `pygame.``locals` `import` `*``import` `time``import` `subprocess``import` `os``from` `urllib2 ``import` `Request, urlopen, URLError`

PiTFT Setup

After the imports there are a few lines that are required to get the PiTFT working. Anyone who has messed around with this screen before will recognise the 'fbdev' or 'fb1' parts and will know that this is related to getting the PyGame to show via the GPIO rather than HDMI (I think!).

363738
`os.environ[``"SDL_FBDEV"``] ``=` `"/dev/fb1"``os.environ[``"SDL_MOUSEDEV"``] ``=` `"/dev/input/touchscreen"``os.environ[``"SDL_MOUSEDRV"``] ``=` `"TSLIB"`

Start PyGame

A single line here that initiates PyGame. I've been told that nothing will work if you don't include this.

47
`pygame.init()`

Set a Global Font

Here all we're doing is setting up a font and font size that we can easily refer to in the code later on - rather than writing a full line to set the font each time. The name of this is…you guessed it…'font'. I make other fonts later on with different names.

56
`font``=``pygame.font.Font(``None``,``24``)`

Define Touch Screen Areas

Usually with these PyGame/PiTFT projects you would want to have a number of buttons or icons to click on. For these to work, you have to set the areas of the touch screen for each of these buttons.

In this project, I'm simply setting the entire screen as one touch button, so that wherever you click you will trigger the exit script to close down my monitor screen.

Either way, you do this by setting two line coordinates on X and Y to make a right-angle, and then Python completes the shape to make it a rectangle.

For example, this is the first rectangle in Spencer's example code, in the top-left corner of the screen:

`if` `15` `<``=` `click_pos[``0``] <``=` `125` `and` `15` `<``=` `click_pos[``1``] <``=``50``:`

This code first says "Make an invisible line from 15 across to 125 across" (X axis). That's the first part (the X axis) before the "and". It then continues to say "Make another invisible line from 15 down to 50 down" (Y axis).

The first coordinate of both of these is the top left point of your angle (In this case 15,15). All references are ALWAYS from the top-left.

Here's a post-it note to help you get your head around that:

![Post-it note diagram](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Post-it-note-diagram.jpg)

> _15-125 across, and 15-50 down - simple!_

Anyway, here is the next section of my project code using this method, again, mine is using the whole screen. When you do click the screen, it will trigger 'button(0)' which we will come to.

77787980818283
`def` `on_click():``click_pos ``=` `(pygame.mouse.get_pos() [``0``], pygame.mouse.get_pos() [``1``])``# Check to see if screen has been pressed``if` `1` `<``=` `click_pos[``0``] <``=` `320` `and` `1` `<``=` `click_pos[``1``] <``=``240``:``print` `"You pressed exit"``button(``0``)`

Define What Happens When Buttons Are Clicked

When your set buttons are clicked, you need to have a module of code like this to tell PyGame what you want it to do each time. This is what this section does.

We referred to 'button(0)' earlier on. We trigger 'button(0) when we touch the screen, so here we're defining the action to take for my one and only button (close PyGame using 'sys.exit()').

We kind of repeat a set of actions 3 times here, for no reason other than to emulate dots moving across the page.

When this triggers we:

  * Fill the screen black (line 94)
  * Set a font for the line (line 95)
  * Create the label "Closing system." (line 96)
  * Blit (add) this label to the screen (line 97)
  * Wait 0.3 seconds (line 98)

After this short wait, we do this again twice, but with an extra '.' each time, before finally exiting the GUI with the final exit command (line 114).

8990919293949596979899100101102103104105106107108109110111112113114
`def` `button(number):``print` `"User requested to close GUI"``if` `number ``=``=` `0``:``# Part 1``screen.fill(black)``font``=``pygame.font.Font(``None``,``40``)``label``=``font.render(``"Closing system."``, ``1``, (white))``screen.blit(label,(``55``,``110``))``time.sleep(``0.3``)``# Part 2``screen.fill(black)``font``=``pygame.font.Font(``None``,``40``)``label``=``font.render(``"Closing system.."``, ``1``, (white))``screen.blit(label,(``55``,``110``))``time.sleep(``0.3``)``# Part 3``screen.fill(black)``font``=``pygame.font.Font(``None``,``40``)``label``=``font.render(``"Closing system..."``, ``1``, (white))``screen.blit(label,(``55``,``110``))``# Exit the script (back to terminal)``sys.exit()`

Define colours to use in our PyGame GUI

Quite a simple step here - we're just adding RGB colours into our script to use elsewhere for things like label fonts, borders and backgrounds. I used the [Colour-Hex website](http://www.color-hex.com/color-names.html) to find RGB colour codes.

126127128129130
`white ``=` `255``, ``255``, ``255``black ``=` `0``, ``0``, ``0``grey ``=` `238``, ``238``, ``238``gold ``=` `255``, ``215``, ``0``red ``=` `255``, ``0``, ``0`

Set the screen size

This line sets the screen size (resolution?) that you're going to use PyGame with. I've used the PiTFT screen size here:

136
`size ``=` `width, height ``=` `320``, ``240`

Set PyGame to use the defined screen size

In the step above we created a screen size called 'size'. The next line tells PyGame to use this screen size:

142
`screen ``=` `pygame.display.set_mode(size)`

Create an initial 'Loading' screen

The following lines simply give you a black screen with the text "Loading" showing, just for the fun of it (nothing is really loading whilst this shows on screen). You could delete this part and the main monitor would still work.

The code is split into 3 parts (just like the shutdown section above), which are all identical apart from the text being displayed. Part 1 shows "Loading.", part two shows "Loading.." and part three shows "Loading…". Notice the dots after the word? I leave a 0.3 second gap between the parts to make it look like a proper 'Loading' screen.

  * First we fill the screen black (line 155)
  * We then set the font (line 156)
  * Next we set the text to be displayed on screen (line 157)
  * Then we blit (add) this text to the screen (line 158)
  * We then use pygame.display.flip - I think this refreshes the PyGame screen but it's something I'm still not 100% on. Taking it out gives a black start up screen so it's definitely needed to show the text. (line 159)
  * Finally we add a short delay before we repeat this block twice again with the slightly different text. (line 160)

Remember, check out my example file for '#' comments that will explain each line in more detail:

154155156157158159160161162163164165166167168169170171172173174175176
`# Part 1``screen.fill(black)``fontloading``=``pygame.font.Font(``None``,``40``)``label``=``fontloading.render(``"Loading."``, ``1``, (white))``screen.blit(label,(``100``,``110``))``pygame.display.flip()``time.sleep(``0.3``)``# Part 2``screen.fill(black)``fontloading``=``pygame.font.Font(``None``,``40``)``label``=``fontloading.render(``"Loading.."``, ``1``, (white))``screen.blit(label,(``100``,``110``))``pygame.display.flip()``time.sleep(``0.3``)``# Part 3``screen.fill(black)``fontloading``=``pygame.font.Font(``None``,``40``)``label``=``fontloading.render(``"Loading..."``, ``1``, (white))``screen.blit(label,(``100``,``110``))``pygame.display.flip()``time.sleep(``0.3``)`

Set a variable to help with time checking

In a moment I'll show you how I get my while loop to only run every 45 seconds. However, to do this, we need to set a variable up front. It's just giving us a starting number to work with which we don't come back to once the monitor is running:

182
`timelastchecked ``=` `0`

The While Loop

This is the main part - the code that turns our PiTFT into a social network monitor. It's the code that adds all the text, data and images you see on the screen. It's the light in your saber, the cheese on your pizza, the caffeine in your coffee!

This is all part of one big 'while 1' loop, which means it'll run forever until I tell it to stop. It gets a little complicated now, so I'll continue to break it down in sections. In a nutshell though, this is the flow:

  * Load the background, static text and images
  * Check and display the Pi's temperature
  * Check and display the current time
  * Grab Twitter data and display on screen
  * Grab Facebook data and display on screen
  * Grab Google+ data and display on screen
  * Grab Pinterest data and display on screen
  * Lastly, some debugging and exit stuff

While Loop Delay

Our while loop will run over and over and over until we tell it to stop, but we don't want or need it to update the count of social followers every few seconds. That's overkill and would slow down my home internet quite considerably.

To make sure it only runs every 45 seconds, we add a little code to check the time against our variable 'timelastchecked'.

In the lines below, the if statement uses time.time() - which is the current time as a floating point number (a number with no set position for the decimal). It says "If the current time (as a number) is greater than or equal to 'timelastchecked', then continue"

As we set 'timelastchecked' to initially be zero, this if statement will run the first time straight away.

You will also see on line 200 that I turn 'timelastchecked' into the current time + 45 seconds. This means when it runs through the loop (takes a few seconds) and then tries to run the if statement again, it will need to wait for the time to be greater than or equal to 'timelastchecked' - which is 45 seconds ahead of time - giving us a 45 second delay.

Clear as mud, right…?

`while` `1``:``if` `time.time() >``=` `timelastchecked: ``# Explained above...``timelastchecked ``=` `time.time()``+``45`

Set the static elements

A number of things on my social network monitor are static i.e. they don't change, move or do anything. These are things like the image on the right and the gold title headings.

As the PyGame screen refreshes every time our while loop cycles, we add these elements each time. There's probably a better way of doing this, but this worked for me.

  * Once again we're making a black background (line 207)
  * We add a rectangle border next. Mine is black so you can't see it - change this to red to see where it is (line 208)
  * Next we add the social network box image and blit it into position. You need this image to be in the same directory as this script or it won't find it (lines 211-212)
  * The rest of the code adds the labels for each social network. We determine the font then the text, and then blit it to the screen as usual (lines 215-228)

207208209210211212213214215216217218219220221222223224225226227228
`screen.fill(black)``pygame.draw.rect(screen, black, (``0``,``0``,``320``,``240``),``1``)``# load the social icon box image and place into position required``logo``=``pygame.image.load(``"socialmediabox.png"``)``screen.blit(logo,(``210``,``40``))``# Set the Twitter heading text``label``=``font.render(``"Twitter"``, ``1``, (gold))``screen.blit(label,(``5``,``40``)) ``# Set the Facebook heading text``label``=``font.render(``"Facebook"``, ``1``, (gold))``screen.blit(label,(``5``,``105``))``# Set the Google+ heading text``label``=``font.render(``"Google+"``, ``1``, (gold))``screen.blit(label,(``5``,``150``))``# Set the Pinterest heading text``label``=``font.render(``"Pinterest"``, ``1``, (gold))``screen.blit(label,(``5``,``195``))`

Get the Pi's Temperature

In this single line of code, we're running a command to get the Pi's temperature and setting it as 'f'. We will use this in the next section to turn this into text on our PyGame screen. This command grabs a line of information including the temperature, so we'll need to chop this down in the next section:

239
`f``=``os.popen(``"/opt/vc/bin/vcgencmd measure_temp"``)`

Show the Pi's temperature on screen

Now that we have the temperature line saved as 'f', we now use this to show the Pi's temperature on screen.

  * First we read the line 'f' and store this as 'i' (I still struggle with why we can't just use 'f"?) (line 253)
  * We then make a new empty string called 'mytemp' (line 254)
  * Next we take this new empty string 'mytemp' and add the contents of 'i' - our temperature line (line 255)
  * As our string now contains the entire line of temperature information, we need to chop certain characters from the front and back to just get the temperature reading we want. The numbers in the [] brackets are the number of characters we are cutting from the front and back of the string (line 256)
  * The last three lines are what you have seen before - setting a font, setting the string to be displayed as text, then blitting the string to the PyGame screen (lines 257-259)

253254255256257258259
`for` `i ``in` `f.readlines():``mytemp ``=` `""``mytemp ``+``=` `i``mytemp ``=` `mytemp[``5``:``-``1``]``font2``=``pygame.font.Font(``None``,``18``)``label``=``font2.render(mytemp, ``1``, (grey))``screen.blit(label,(``280``,``5``))`

Show the time and date on screen

Next we add the time and date to the screen. This works in the exact same way to the temperature above - run a command to grab a line of text (the date and time command), then set this as a string, manipulate and blit to the PyGame screen.

The time and date command is on line 270:

270
`f``=``os.popen(``"date"``)`

The rest of the code setting the time is in lines 279-285, and runs in the same was as the temperature section above:

279280281282283284285
`for` `i ``in` `f.readlines():``mytime ``=` `""``mytime ``+``=` `i``mytime ``=` `mytime[``4``:``-``13``]``font3``=``pygame.font.Font(``None``,``36``)``label``=``font3.render(mytime, ``1``, (white))``screen.blit(label,(``5``,``1``))`

Reading and displaying Twitter data

This part, in a way, is similar to the temperature and time sections above. I say this because all we're doing is looking at a URL, finding and reading a specific line, then manipulating that line to show as text on screen.

Yes there is more code involved because we're reading URLs rather than simple terminal commands, but the method is similar.

We start off by setting the target URL to look at for data, and defining 'req' to request the URL (lines 303-304):

`someurl``=` `'https://twitter.com/AverageManvsPi'``req ``=` `Request(someurl) ``# Request the URL`

What follows is a section of code that makes our little monitor capable of handling errors - and the most likely error of it not being able to read the URL (WiFi or router down etc). What we don't want is the GUI to crash out just because the internet was down for a couple of minutes.

To do this, we use the [try statement](https://docs.python.org/2/tutorial/errors.html#handling-exceptions) here.

First we try to get a response from the set URL (lines 305-306):

`try``:``response ``=` `urlopen(req)`

Then we have two main outcomes which form our try statement:

  * We don't get a response (it fails)
  * We get a response (success - "happy path")

If we **don't** get a response, the following section of the code handles that, and adds text to our PyGame so that we know something isn't right (lines 307-317). I first saw this over on a RasPi.TV article - [which can be read here](http://raspi.tv/2014/programming-a-kickstarter-tracker-in-python-part-1). I don't fully understand how 'hasattr' or 'e.reason' works, that's something for me to read up on:

307308309310311312313314315316317
`except` `URLError as e:``if` `hasattr``(e, ``'reason'``):``print` `'We failed to reach a server.'``print` `'Reason: '``, e.reason``label``=``font.render(``"No Connection (1)"``, ``1``, (red))``screen.blit(label,(``5``,``60``))``elif` `hasattr``(e, ``'code'``):``print` `'The server couldn\'t fulfill the request.'``print` `'Error code: '``, e.code``label``=``font.render(``"No Connection (2)"``, ``1``, (red))``screen.blit(label,(``5``,``60``))`
![Social network monitor debugging](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Monitor-connection-failed.jpg)

> _Any errors with the URLs/netwrok will show like this, instead of closing the program. A nice trick learnt at RasPi.TV._

If we **do** get a response, happy days, we can look into the lines of that URL and grab the data we want for our display. Read on…

Reading URL data

Whilst the URL method of reading a line and stripping characters is similar to the temperature and time examples above, with this approach we have a whole web page of lines to look at - so we narrow this down by telling the program to look for a certain string of text in the web page and return only that line.

Of course for that to work properly, we need our line to have a unique string of text within it - otherwise we will pull back multiple lines.

For example, to find my Twitter follower count I go to <https://twitter.com/AverageManvsPi>, right-click the page and select 'view page source'. Here's what I'm presented with:

![Twitter page source](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Twitter-View-Source.jpg)

> _Here's the source of my Twitter page - clear as mud…_

I know that I have '1,822' followers, so I need to find that text in this source view. I simply hit ctrl+f and type '1,822' in the search box. Oh look - two lines show up:

![Source code search](http://www.averagemanvsraspberrypi.com/wp-content/uploads/2015/07/Twitter-View-Source-Follower-Count.jpg)

> _Searching for my follower count narrows down the source code a bit…_

I looked at both of the lines, searching for a specific string of text that could uniquely identify one of the lines only. I found that ' Followers"' (with the space at the front) did this perfectly.

So now you know how to do that bit, let's continue…

Grabbing Social Network Data

This is the 'else' part of our try statement i.e. the happy path if there are no errors.

Let me explain the lines:

  * First we make a new string 'followcount' and set that as the lines of the URL (line 319)
  * Next we use a 'for' and 'if' statement to say 'if you find this particular string in a line, give me that line only' (line 320-321)
  * If that particular string is found, we turn our 'followcount' string into that line only, and chop off the characters that we don't need (line 322)
  * We then change 'followcount' again, this time adding some text to the front of it to give it a label as such (line 323)
  * Lastly, as always, we set the font for the string then blit that to the PyGame screen (lines 324-325)

318319320321322323324325
`else``: ``# "If there are no errors"``followcount ``=` `response.readlines()``for` `line ``in` `followcount:``if` `' Followers"'` `in` `line:``followcount ``=` `line[``158``:``-``32``]``followcount ``=` `"Followers: "` `+` `followcount``label``=``font.render(followcount, ``1``, (white))``screen.blit(label,(``5``,``60``))`

Adding more Social Network feeds

This theme of pulling data from social networks continues in the while loop, as further nested 'if' statements running in exactly the same way - just with different URLs, different unique string identifiers and a different number of characters chopped off each time.

Hence - I won't talk through the remaining social network data 'grabs' from line 326 to 442 - it should be quite clear what it's doing now. Drop me a comment below if you get stuck.

Debugging

Lines 428-442 are purely for debugging, something I took from [MrUkTechReview's sample code](http://home.uktechreviews.com/Raspberry/Pi%20blog/files/pygame-menu.html). I may have changed this slightly but it's more or less the same.

This section helps when you need to troubleshoot any iffy behaviour, by printing the touch screen press locations to terminal, and also painting them to the PyGame screen. There's also a section of code here that gives you a safe exit option if needed.

The very last line…

The final line in the Python code is probably the most important line in the whole script:

318
`pygame.display.update()`

It doesn't look much, but this little line makes sure the PyGame GUI updates.

…and that's it! Code done!

**Potential Snags**

It seems the Google+ source code changes almost by the hour (if not more frequently), so where I cut an exact amount of characters from the front and back of a line, it can cause odd characters to show up, and even chop off some of the numbers that I wanted to see.

A good way of dealing with this would be to leave a few non-numeric characters either side of the follower count, and use some kind of Python magic to extract just the numbers from the string. I'll be looking into that.

Similarly, if you went from a 3-digit follower count (999) to a 4-digit (1000) - you would need to change the code as you'll probably be chopping off the 4th character. Again, I wan't to find a smarter way of doing this.

There's also the issue that the touch screen becomes unresponsive when the while loop is running, but that's not an issue for this project as it's intended to be interacted with much.

**Summary**

This is yet another project that I avoided for far too long, but I'm glad I finally got my head around PyGame. The best thing about this, is that the same methods can be used to pull data from any website - gamer stats, news, sport scores - anything!

I hope this post has helped you to get started with PyGame. If you have any questions, please add them in the comments section below.

Until next time…

Average Man
