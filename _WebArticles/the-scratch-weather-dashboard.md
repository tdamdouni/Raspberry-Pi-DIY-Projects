# The Scratch Weather Dashboard

_Captured: 2017-05-06 at 16:26 from [www.raspberrypi.org](https://www.raspberrypi.org/learning/weather-station-dashboard/worksheet2/)_

In this next worksheet you will learn how to display some weather data visually, producing a Weather Dashboard. You'll want to start a new Scratch file and enable the remote sensors, just like you did in the first [worksheet](https://www.raspberrypi.org/learning/weather-station-dashboard/worksheet.md).

## Choosing a forecaster

The first thing you'll want to do is to choose a weather forecaster, who will be telling the viewers what the weather is like. Weather forecasters are often called meteorologists.

  1. Choose a new sprite by clicking on the middle button as shown below:

  2. Choose any sprite you like. Here we've gone for the `squaregirl` image:
![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/square-girl.png)

## Your forecaster script

  1. You can start off by making your weather forecaster set the ID of the Weather Station you'll be using, by creating a new variable.

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/set-id.png)

  2. She'll then need to say a little bit about the location of the weather forecast. Use a `join` block (from `Operators`) within a `say` block to begin with, just like you did in [the first worksheet](https://www.raspberrypi.org/learning/weather-station-dashboard/worksheet.md):

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/forecaster-1.png)

  3. Now grab two more `join` blocks. In the right-hand side of one, you can place the `town` the weather forecast is coming from. In the left-hand side of the other, you can place the `country` of the weather forecast:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/forecaster-2.png)

  4. Now the two `join` blocks can be placed together. It may not be obvious in the image, but you should add a single space character between the two `sensor values`:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/forecaster-3.png)

  5. With that done, you can place all three `join` blocks together into the `say` block:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/forecaster-final.png)

  6. Your forecaster is now finished. Next, you can add some graphical elements to help users visualise the weather.

## A weathervane

Next, you can make a weathervane. Weathervanes show the direction of the wind, but yours is also going to visualise the speed of the wind.

  1. Click on the `New Sprite` button to choose another sprite:

  2. In `things` you should see a `Clock-hand` which is basically just an arrow. Import this sprite and delete any scripts that come with it:
![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/clock.png)

  1. When your weather forecast begins, you'll need to set the size and direction that the arrow points:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/arrow-1.png)

  2. In `Motion` you should see a `turn clockwise __ degrees` block. Add this to the bottom of the script. Then choose the `wind_direction` sensor value, and add this block in:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/arrow-2.png)

  3. To visualise the wind speed, you can change the size of the arrow. Find the `change size by __` block (in `Looks`) and add this to your script:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/arrow-3.png)

  4. To finish off, find the `__ * __` block in `Operators` and use it to multiply the `wind_speed` by `10`. You can choose a different number if you like, though:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/arrow-4.png)

  5. This can then be added into the `change size by __` block:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/arrow-final.png)

## Adding a thermometer

  1. Next, you're going to produce a working thermometer. You'll need a graphic to represent it, and the one below should be good enough. You can get a large version of it [here](https://www.raspberrypi.org/learning/weather-station-dashboard/images/therm-sprite.png).

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/therm-sprite-small.png)

  2. Import this sprite into your Scratch program. You'll need to place this sprite in a very particular place, so it's best to add this into the script. You're also going to use the pen tool to draw the mercury inside the thermometer, but because you can't draw over the top of sprites, you need to stamp the sprite's image to the canvas first, and then hide it. This is the only script you'll need on the thermometer:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/thermometer.png)

You'll notice the `broadcast` at the end. This is going to be used to tell the pen to start filling in the mercury inside the thermometer.

## Drawing the mercury

  1. Now you're going to need a new and very tiny sprite. Click on the leftmost button in the `New Sprite` menu:

  2. All you need is a single white dot in the middle of the screen. Draw a white dot and then click OK.

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/canvas.png)

  3. Now you're going to get this tiny pixel to draw a red line of mercury inside the thermometer. When the pixel receives a message to draw, it needs to set up its pen:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-1.png)

  4. How the mercury is drawn will depend on whether the temperature is higher or lower than `0`. You write the code for temperatures above `0` first:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-2.png)

  5. The first thing to do is to make the pen go all the way to the bottom of the thermometer, and for the pen to be placed `down` on the canvas:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-3.png)

  6. Next, the pen can move up to the `0` degrees mark on the thermometer:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-4.png)

  7. Then, depending on the temperature, the pen can move upwards on the `y` axis. You might want to tweak the values a little, but 1.7 pixels per degree seems to work fairly well:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-5.png)

  8. If the temperature is below zero, the pen needs to move to the `-30` degree mark:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-6.png)

  9. Then the pen needs to again move in the `y` direction. This can be achieved using a little bit of maths:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-7.png)

  10. The pen can then be placed into the finished script:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/pixel-8.png)

## What next?

In [worksheet three](https://www.raspberrypi.org/learning/weather-station-dashboard/worksheet3.md) you'll learn how to fetch the weather from more than one Weather Station, giving you a global weather dashboard.

In this relatively short worksheet, you'll learn how to access random Weather Stations from all around the world.

## The Python script

Make sure your Python script is still running in the background. The script is constantly listening out for a `broadcast` with the name `new-station`. Each time the script hears the `new-station broadcast`, it chooses a new and random station to collect the data from.

## Getting a new station

You can start on the last sprite you created, the one that was just a single dot in the middle of the page. All you need to do in this script is create a loop that broadcasts `new-station` every 10 seconds or so. (You can choose your own timing):

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/loop.png)

## Removing the flags

For all your other sprites, you just need to change the `green flag clicked` blocks for `when I receive new-station` blocks:

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/thermometer-broadcast.png)

![](https://www.raspberrypi.org/learning/weather-station-dashboard/images/arrow-broadcast.png)

## Running your script

When you click on the green flag, your script should start working straight away. It will tell you the area where the station is located, and then the latest temperature and wind readings.

## What next?

There are lots of other sensors that you could have a go at visualising in the dashboard. Why not have a look at humidity, or try to make a visualisation of a barometer to tell you the air pressure? Perhaps you could show a little column of water to visualise how much rain has fallen?

If you'd like to have a go at some other Weather Station resources, then you can have a look at [Fetching the Weather](https://raspberrypi.org/learning/fetching-the-weather), to have a go at accessing weather data in Python.
