# Using Mote with Homekit and Siri

_Captured: 2017-08-30 at 09:41 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/using-mote-with-homekit-and-siri)_

Because Mote was designed for home lighting, like under-shelf or under-cabinet lighting, automating its control opens up a lot of possibilities.

Fortunately, Apple's Homekit API has been extended with an open source project called homebridge, a Node.js library with a bunch of useful plugins for controlling everything from RGB LED lights, like Mote, to Sonos speakers, and even the Xbox One.

Although Apple will shortly be releasing a Home app (alongside iOS 10) to allow you to control Homekit-enabled devices, there are a number of other apps that allow you to do the same. Our favourite is one called Hesperus, that offers a clean, intuitive interface with options for setting up scenes with groups of devices and scheduling actions.

(UPDATE: Apple have now released their Home app, and we can confirm that it works nicely with our Mote API described below)

Here, we'll look at how to set up a [Flask](http://flask.pocoo.org/) API to control Mote, how to install and configure [homebridge](https://github.com/nfarina/homebridge) and the [homebridge-better-http-rgb](https://github.com/jnovack/homebridge-better-http-rgb) plugin, and how to use the [Hesperus](https://hesperus.io/) app and Siri to control Mote.

![hesperus-.gif](https://learn.pimoroni.com/static/repos/learn/sandyj/hesperus.gif)

## Installing the Mote and Flask Python libraries

We need a couple of Python libraries - the Mote and Flask libraries - so let's install those now, before we begin going through the code.

If you're setting this up on a Raspberry Pi, and we'd suggest that this is the best way to do it, then you can use our one line installer to install the Mote library, as follows.
    
    
    curl https://get.pimoroni.com/mote | bash
    

If you're not using a Raspberry Pi, then you can use pip, the Python package installer, to install the Mote library.
    
    
    sudo pip install mote
    

We also need to install the Flask library, and we can also use pip to install that. Type the following to install Flask.
    
    
    sudo pip install flask
    

## Writing a Flask API for Mote

The homebridge plugin that we'll be using to receive messages from Hesperus and Siri is called homebridge-better-http-rgb. It uses a series of endpoints to relay commands to RGB LED lights. Our Flask API will define these endpoints and use them to switch the Mote LEDs on and off, control their brightness, and control their hue.

The endpoints defined by homebridge-better-http-rgb are `on`, `off`, `status` (whether the lights are on or off), `brightness`, and `set` to set the hue. The `brightness` and `set` endpoints, when called without a subsequent value, will return the currently set brightness or hue respectively. Otherwise, values can be passed to those endpoints, for example `brightness/50` to set the brightness to 50% or `set/FF0000` to set the hue to red.

Flask is a super little Python library for building web apps, and can also be used to build simple APIs (application programming interfaces) to let you programmatically control things, whether they be physical devices or web services.

Our Flask API is around 100 lines, so we'll go through it by bit, to see what it all does.

## Imports

First, we need to import a few things that we'll be using for our API.
    
    
    from colorsys import hsv_to_rgb, rgb_to_hsv
    from mote import Mote
    from flask import Flask, jsonify, make_response
    

The `colorsys` functions `hsv_to_rgb` and `rgb_to_hsv` will be used to interconvert HSV and RGB colours (more on that later). We need the `Mote` class to control Mote, and the `Flask` class and `jsonify` and `make_response` functions to build our API.

## Boilerplate

At the very top, we have some boilerplate code that sets up some things that are required by our code, to initialise the Flask app and to set some parameters for Mote.

We configure each of the four channels of our controller each to have 16 pixels, and then create a couple of variables `colour` and `status`, that we'll use later on, with sensible defaults of white for the colour and `0` or off for the status.

## Mote functions

Most of the rest of our code is composed of various functions that we can split into those related to controlling Mote, and the functions that will be used by Flask to create the API endpoints.

Let's have a look at the Mote functions first.

Because our homebridge plugin expects colours in hex, and Mote expects colours to be in RGB, we have the slightly convoluted task of interconverting these. The `colorsys` library has functions to interconvert HSV and RGB values, but unfortunately does not have a function to convert to and from hex values. So, we'll write a simple function to convert hex to RGB.

Our `hex_to_rgb` function takes a `value`, strips off the leading `#` if there is one, and then splits the 6 digit hexadecimal value into three pairs of two digits (one each for red, green and blue) and converts them into integers. The Python `int` function that converts strings or floating point numbers into integers takes an additional argument that tells it which base to use when converting. In this case, we use 16 because we're working with hexadecimal numbers, meaning that our two hexadecimal digits get converted into an integer that takes a value between 0 and 255 (2^16 = 256).

Next, we have a couple of functions that switch Mote on or off. The `mote_on` function takes a single argument - `c` \- the colour as a hex value. It then uses the `hex_to_rgb` function that we just wrote to get the `r`, `g`, and `b` values from the hex colour `c`, and sets all of the pixels across all of the strips to that colour. This function will be used to switch Mote on, and to change the colour of Mote while it is switched on.

Our `mote_off` function is a simple one that turns all of the pixels off.

## Flask API functions

The remaining functions relate to the API itself, and define the endpoints that the homebridge-better-http-rgb plugin will use. As is the convention for APIs, all of our endpoints will begin `/mote/api/v1.0/`, telling us the name of the API, specifying that it is indeed an API as opposed to a webpage, and the version number to provide a means to have legacy support once newer versions are developed.

### On/off/status

The first endpoints that we'll define will be `/mote/api/v1.0/status`, `/mote/api/v1.0/on` and `/mote/api/v1.0/off`. The `status` endpoint allows the API to return the status of Mote - whether it is on or off - so we'll use our `status` variable, that is either `0` when off or `1` when on, and set that as part of a `get_status` function.

Our function defines `status` as a global variable, so that its state persists across all of the code, inside and out of functions. It then loops through all of the pixels on all of the channels and then checks whether they are on or off. If they are on, then `status` is set to `1`, otherwise `status` is set to `0`.

We'll use that function that we just wrote in the first of our routes, in a `set_status` function. In Flask, endpoints are wrapped in a `@app.route` decorator that defines it as a URL route.

Our `app.route` decorator defines the URL structure as `'/mote/api/v1.0/<string:st>'`. The first part - `/mote/api/v1.0/` \- will be common to all of our URL endpoints. The `<string:st>` part is a cunning little trick that Flask uses to grab part of a URL and assign it straight to a variable, and even lets you set what the type is, in this case a string called `st` We also use `methods=['GET']` to specify that this URL will send a get request.

The `set_status` function is passed the `st` variable from the URL and then, depending on whether `st` is `on`, `off` or `status`, acts accordingly. If `st` is equal to `'on'` then the `mote_on` function is called with the global colour that is currently set, and `status` is set globally to `1`, and if it is equal to `off` then the `mote_off` function is called and `status` is set to `0`. If `st` is equal to `'status'`, then we call our `get_status` function.

Finally, we return in JSON format the `status` and `colour`, using the `jsonify` function, passing it a dictionary with the appropriate keys and values. When a get request is sent to this URL route, the JSON-ified dictionary will be returned rather than an HTML page as would normally be the case.

### Getting and setting colour

homebridge-better-http-rgb specifies that the `/set` endpoint will return the currently set colour. We'll write a simple route function that returns the global `colour` value and returns it in the same JSON-ified format as our last route that we wrote.

Again, we use the `@app.route` decorator to set the URL to be `'/mote/api/v1.0/set'` and specify that it will send a get request. The `get_colour` function that is called when the URL is accessed simply returns the JSON-ified dictionary containing the `status` and `colour`.

We also need a `set_colour` function that will be used to... set the colour! It extends the `/set` route with a hex colour, e.g. FF0000 for red.

We grab the hex colour from the URL and assign it straight to a variable `c` as part of the route decorator, then pass it into the `set_colour` function. We specify that `status` and `colour` are globals and then set `colour` to be the same as `c`. If `status` is not currently equal to `0`, i.e. if it is currently on, then we call our `mote_on` function and pass it the colour, then set `status` to `1`. Last, we return a JSON document, as we did with our previous endpoints.

### 404

To do things by the book, we'll use Flask's `@app.errorhandler` decorator to gracefully handle 404 not found errors.

If a route isn't found, then a JSON document will be returned informing the human or non-human user that the route doesn't exist.

## The main function

In Flask apps, the `main` function is run when the app is first run at the command line. As well as actually running the app with `app.run(host='0.0.0.0', debug=True)`, we'll call the `mote_off()` function to switch Mote off when the script is first run. This is a good idea because the state of the pixels, i.e. whether they are on or off and their colour, will only persist as long as the app is running. If they were switched on and the app stopped running, then when the app was run again it would assume they were switched off and had the default white colour. By setting them to off when the app first runs, we get over such problems.

## Testing the API

Now that we've written our API, we can test that the endpoints work as expected. The entire code is below, so copy it and save it in a file called something like `mote_api.py`.

Open a terminal and type 'python mote_api.py'.

Then, open another terminal window or tab, and type the following to test that our API is working as expected.

That _should_ have just turned your Mote strips on! You should also be able to do this remotely, on another machine, replacing the `127.0.0.1` part of the URL with the IP address of the machine on which your API is running. You should also be able to do this in your web browser rather than with curl in the terminal.

Try typing the following to change the colour of the Mote strips to red.

## Setting up homebridge and homebridge-better-http-rgb

The next step is to set up homebridge and homebridge-better-http-rgb on our machine running the Mote API, to complete the circle. homebridge and the homebridge-better-http-rgb plugin provide the means to add Mote as a Homekit device that can be controlled through an app like Hesperus, and send commands to our API and hence to the Mote strips.

The following instructions assume that you're using a Raspberry Pi 3 running the latest version of Raspbian Jessie although, with some modifications, you should be able to run everything on a Mac, a Windows PC, or another Linux machine.

The version of Node.js bundled with Raspbian is a little out of date, so we'll install the latest version before we start to install homebridge, etc.

Open a terminal, and type the following to upgrade to the latest and greatest version of Node.js:

Before we install homebridge, we'll also need to install a couple of dependencies. Type the following to install them:

Now, we can install homebridge itself, as well as the homebridge-better-http-rgb plugin:

Now that everything is installed, we have to do a couple more things to configure homebridge correctly. homebridge is configured through a .json file that _must_ be put into the `/home/pi/.homebridge/` directory. We'll create that directory now:

Here's what our config file looks like:

Copy and paste that, and save it as `config.json` in the `/home/pi/.homebridge/` directory that we just created.

You can change the bridge name and description to whatever you'd like, as well as the accessory name that we've called `"Mote"`. The `username`, `port` and `pin` are all boilerplate values and can be left as they are.

If, at a later date, you wanted to add other accessories using other homebridge plugins, then you'd add them as new accessories in the `accessories` list.

Now that everything's set up, we'll start the Mote API first and then homebridge.

Assuming your Mote API is called `mote_api.py` and is in `/home/pi/`, type the following to start it:

You'll see a few lines telling you the status of the Flask app, including the IP address and port on which it is running.

Now, open another terminal tab or window (leaving the Mote API one open), and type `homebridge` to start homebridge.

You'll see a few lines confirming that the Mote accessory has been loaded successfully and a code that you can enter when configuring your Homekit app on your iPhone. There's no need to write this code down, as it's the same as the one that we configured ourselves in our config file earlier.

Now that the Mote API and homebridge are running, we'll install and configure the Hesperus app on our iPhone and link it up to our Mote accessory.

## Setting up the Hesperus iOS app

Hesperus is a really nice free iOS app for controlling Homekit accessories. The setup described above works really smoothly with Hesperus, but other Homekit apps like Elgato Eve and Homedash (and Apple's own upcoming Home app) should work equally well.

You can download Hesperus in the [iOS App Store](https://itunes.apple.com/us/app/hesperus/id969348892?ls=1&mt=8).

When you first open the app, you'll be greeted by a screen that asks you to "Create Your First Home".

Give your home a name. I went for the imaginatively named "Home".

![Create your home](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-1.jpg)

Once you've done that, you'll be taken to the home page for your Home space. This is where all of the accessories that you add to that space will appear. If you decided that you wanted to get more specific, you could have separate spaces for different rooms in your house like "Living room", "Bedroom", etc. Spaces are accessed by tapping on the icon with four small squares, just below the battery status icon.

Tap the large "+" in the centre to add a new accessory. It'll scan to look for connected accessories and, assuming that the Mote API and homebridge are running, it should find the "Homebridge" bridge. Click on "Identify" to complete the setup of the Mote accessory.

![Adding an accessory](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-2.jpg)

> _It'll display a warning telling you that "This accessory is not certified and may not work reliably with Homekit". Just tap "Add Anyway"._

You'll then see a screen that will allow you to use the camera to scan the PIN code displayed in the terminal window running homebridge (you may need to grant the app access to use your camera). In our experience, the camera detection of this code was a bit iffy, so you may need to click "Enter code manually" and then key in the PIN code.

![PIN code entry](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-3.jpg)

> _Once the accessory has been successully added, you'll be taken back to the home screen for you "Home" space, and the Mote accessory should be visible._

Try clicking on it. The Mote strips should come on!

If you're using an iPhone 6 or later, you can force tap on the Mote icon to pop open a more detailed set of controls to let you change the colour and brightness of Mote.

![Switching Mote on and controlling colours](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-4.jpg)

> _Try tapping on the circle on the left hand side and then drag your finger around the colour palette to change the colour of Mote on the fly._

## Scenes, schedules, and actions in Hesperus

You can do a lot more than just turning on Mote and controlling its brightness! Hesperus lets you set up scenes that can be triggered instantly from the scenes screen. We'll create a scene called "Good morning" that turns Mote on with an orange hue, 75% saturation and 100% brightness.

Tap on the second from left icon on the bottom bar of Hesperus (the two overlapping squares) to access the "Scenes" page. Then tap on the "+" in the top right hand corner to add a new scene.

Call it "Good morning", and tap on the "+" to add the Mote device. Make sure to toggle the power on and select the hue, saturation and brightness that you want, then tap "Save" to save your scene.

![Creating a scene](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-5.jpg)

> _Now that you've added your scene, you can even trigger it through Siri by using its name: "Hey, Siri. Good morning."_

I've added several more scenes called "I'm leaving", "I'm home", and "Good night", that all can trigger actions direct from Siri.

![Scenes](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-6.jpg)

The calendar icon on the bottom bar (third from the left), can be used to create scheduled actions. These let you schedule actions at a specific time and frequency, for instance one called "Morning", similar to our "Good morning" scene that switches the lights on in a pale orange hue at 7am every day.

![Scheduled actions](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-7.jpg)

> _Finally, we can create actions that trigger automatically given certain condtions. For instance, we can create a "Lights On" action that will trigger if we're at home and it's after sunset._

The "Actions" page is the second icon from the right on the bottom bar (the one that looks a bit like an orange sliced through the middle). If you grant access to location data in Settings > Privacy > Location Services > Hesperus, then you can trigger actions when you are within or outside a location.

Then add a resulting action.

![Triggered actions](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-8.jpg)

> _You can also add additional conditions with and or or Booleans, such as before or after a given time, or before or after sunrise or sunset._

![Conditions for triggered actions](https://learn.pimoroni.com/static/repos/learn/sandyj/mote-homekit-9.jpg)

## Controlling Mote with Siri

The other added benefit of having set all this up is that now that we've Homekit-enabled Mote, we can control it with Siri. We can use the name that we gave our Mote accessory in the config file (in our case "Mote") to control it.

If you have "Hey, Siri" enabled, then try saying "Hey, Siri. Turn Mote on.", or press and hold the home button to launch Siri and say "Turn Mote on".

![siri-iphone.gif](https://learn.pimoroni.com/static/repos/learn/sandyj/siri-iphone.gif)

> _There's a little flexibility, so you should also be able to say "Switch Mote on", "Turn the lights on", and perhaps some other ways of phrasing it._

You can also say "Set the brightness to 25%", or "Set Mote to red".

And, as we mentioned earlier, you can also use Siri to trigger scenes that we created in Hesperus, e.g. "Hey, Siri. I'm home." to turn the lights on.

If you have an Apple Watch, then you can also use Siri on it to control your homebridge devices. And with Apple adding Siri to OS X, you should also be able to control them using your Mac soon.

![siri-watch.gif](https://learn.pimoroni.com/static/repos/learn/sandyj/siri-watch.gif)

## Taking it further

We've only covered a basic setup with a single Mote controller, but you could easily extend this, either with additional Mote controllers on the same Pi and extending the API endpoints to include a controller number in the URL, or with additional Pis and controllers on separate IP addresses. You could also modify the API to individually control each strip on each controller.

A simple way to jazz up your Mote API would be to include a short fade up and down when you turn on or off your Mote, to make it look a bit less jarring when turning it on or off.

And, of course, the beauty of homebridge is that you could easily add more plugins and hence accessories so that you could, by triggering a single action, start your Sonos playing some smooth jazz and turn the lights on low. Nice.
