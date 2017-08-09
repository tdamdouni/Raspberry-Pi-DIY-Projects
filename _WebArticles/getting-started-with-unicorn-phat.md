# Getting Started with Unicorn pHAT

_Captured: 2017-05-19 at 10:06 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-unicorn-phat)_

This tutorial will show you how to install the [Unicorn HAT Python library](https://github.com/pimoroni/unicorn-hat) (Unicorn pHAT uses the same Python library as Unicorn HAT), and then walk through its functionality - how to light pixels, control colour and brightness, and then finish with an example of how to MAKE IT RAINBOW!

If you haven't already soldered the header to your Unicorn pHAT, then you can follow our guide to soldering pHATs [here](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats).

## Installing the software

We always recommend using the most up-to-date version of Raspbian, as this is what we test our boards and software against, and it often helps to start with a completely fresh install of Raspbian, although this isn't necessary.

As with most of our boards, we've created a really quick and easy one-line-installer to get your Unicorn pHAT set up. We'd suggest that you use this method to install the Unicorn HAT Python library.

Open a new terminal, and type the following, making sure to type 'y' or 'n' when prompted:
    
    
    curl https://get.pimoroni.com/unicornhat  | bash
    

Once that's done, it probably a good idea to reboot your Pi to let the changes propagate, if the installer doesn't prompt you to reboot.

## Using the software

Open a new terminal and type `sudo python` to open a new Python prompt.

## Lighting individual pixels

We'll begin by doing the simplest thing you can do, lighting a single pixel red. This will show you how the pixels are organised and the commands needed to light them in a particular colour.

Before we start anything, we have to type the following to import the `unicornhat` library:
    
    
    import unicornhat as uh
    

The `import x as y` just means that we don't have to type the rather long-winded `unicornhat` each time we want to call a function, just `uh`.

Because the Unicorn HAT library is used by both the HAT and pHAT (which is half the size of the HAT), we need to specify that it's the the pHAT that we're using. To do that, just type:
    
    
    uh.set_layout(uh.PHAT)
    

We'll also set the brightness to 50%, since Unicorn pHAT will scorch your retinas at 100% brightness (you were warned!)
    
    
    uh.brightness(0.5)
    

To light a pixel on Unicorn pHAT in a particular colour, we have to do two things: first, we have to use the `set_pixel()` function to specify which pixel we want to light and in what colour and, second, we have to use the `show()` function to update the Unicorn pHAT and actually display the pixel that we set.

Pixels on Unicorn pHAT are organised by their x/y coordinates from the top left hand corner, so the top left pixel is `0, 0` and the bottom right pixel is `7, 3`. Remember that, in Python, things are number from 0 rather than from 1.

The colours of pixels are specified by an RGB colour value. Each colour can be represented by mixing a particular amount of Red, Green, and Blue, from 0 to 255, meaning that you can get over 16 million different colours!! As an example, pure red is `255, 0, 0` and white is `255, 255, 255`.

Let's light the top left pixel red. Type the following:
    
    
    uh.set_pixel(0, 0, 255, 0, 0)
    uh.show()
    

![](https://learn.pimoroni.com/static/repos/learn/sandyj/getting-started-with-unicorn-phat-1.jpg)

> _To clear any pixels that you've set, you can use the clear() function, followed by show() :_
    
    
    uh.clear()
    uh.show()
    

## Lighting all of the pixels using a for loop

To light all of the pixels on Unicorn pHAT, it's just a matter of repeating the process we just did once for each of the 32 pixels. We can make this really quick and easy by using two `for` loops: one to loop through each column, and another to loop through each pixel in each of those columns.

The rough process is: `for x in range(8):` and then `for y in range(4):`, because we have 8 pixels along the x axis and 4 along the y axis.

This time, we'll light the pixels cyan, which is a mix of pure blue and pure green and so can be represented by the RGB colour `0, 255, 255`.

Type the following:
    
    
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, 0, 255, 255)
    uh.show()
    

![](https://learn.pimoroni.com/static/repos/learn/sandyj/getting-started-with-unicorn-phat-2.jpg)

> _All of the pixels on your Unicorn pHAT should just have lit up cyan!_

## Making it blink!

Now we're going to use a `while` loop to make your Unicorn pHAT blink pink. All we have to do is continuously light all of the pixels pink, using the technique we just learned, and clear them again, with a short delay, maybe a quarter of a second in between.

Type the following:
    
    
    import time
    
    while True:
        for x in range(8):
            for y in range(4):
                uh.set_pixel(x, y, 255, 0, 255)
        uh.show()
        time.sleep(0.25)
        uh.clear()
        uh.show()
        time.sleep(0.25)
    

![](https://learn.pimoroni.com/static/repos/learn/sandyj/getting-started-with-unicorn-phat-3.gif)

This is just the same as in the example where we made all of the pixels light in cyan, except we changed the RGB colour to `255, 0, 255` and we added a couple of lines to sleep for a quarter of a second - `time.sleep(0.25)` \- and to clear all of the pixels - `uh.clear()`.

## Making it rainbow!

For our last example, we'll get a little more complex and make a rainbow animate across your Unicorn pHAT. As well as representing colours in RGB, we can also use a system called HSV (hue, saturation, value) that uses the colour wheel to determine the hue of a colour. The colour wheel begins and ends at red, and progresses through all of the other colours of the rainbow in order. Each position on the colour wheel is represented by a compass position in degrees, with red being at 0/360 degrees.

Fortunately, there's a Python library called `colorsys` that lets you convert HSV colour values to RGB colour values that we can feed into the `set_pixel()` function. So, to animate our rainbow we just have to continuously cycle around the colour wheel through all of the colours of the rainbow.

Here's all of the code for our animated rainbow. We'll break down what all of it does after. Type the following:
    
    
    import time
    import colorsys
    
    spacing = 360.0 / 16.0
    hue = 0
    
    while True:
        hue = int(time.time() * 100) % 360
        for x in range(8):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            for y in range(4):
                uh.set_pixel(x, y, r, g, b)
        uh.show()
        time.sleep(0.05)
    

![](https://learn.pimoroni.com/static/repos/learn/sandyj/getting-started-with-unicorn-phat-4.gif)

> _First, we import the time and colorsys libraries. We'll need the colorsys library to convert our HSV colour into an RGB colour._

`spacing = 360.0 / 16.0` means that we'll space half of the colour wheel across the 8 pixel width of Unicorn pHAT at any one time. You can reduce the `16.0` to get more of the colour wheel across your Unicorn pHAT or increase it to get less of it.

`hue = 0` initialises the `hue` variable with a starting value of `0.0`. It will be changed through time inside our `while True:` loop, but we have to initialise it outside our loop.

Our `while True:` loop does several things. Most importantly, it sets the hue by taking the time (in epoch seconds, no need to worry about what that is), multiplying it by 100 to scale it up a little, and then taking the modulo 360 of that result (the remainder after dividing the time x 100).

Then, we have two `for` loops. The first calculates an `offset` from the pixel number `x` and our 22.5 degree `spacing` that we calculated earlier. This offset is added to the `hue`, the modulo `360` is taken again, and the value is divided by `360.0` to get a number between `0.0` and `1.0` that will be accepted by the `colorsys.hsv_to_rgb()` function. The rather complicated line that begins `r, g, b =` is a list comprehension that converts the RGB values returned by `colorsys.hsv_to_rgb()`, which are values between `0.0` and `1.0` to RGB values between 0 and 255.

The second `for` loop just sets all of the pixels in each column (`y`) to the same colour that we just calculated for each `x` pixel, using the `uh.set_pixel()` function.

Finally, we call `uh.show()` outside of our two `for` loops but still inside the `while` loop, and then introduce a small delay of 0.05 seconds to set the animation speed with `time.sleep(0.05)`.

## Taking it further

Why not try to take our rainbow example further and set a different colour for the pixels in each column too? Or just clamp the range to a portion of the colour wheel that you like?

Try setting the colour of your Unicorn pHAT to the current [Cheerlights](http://cheerlights.com/cheerlights-api/) colour, or use your Unicorn pHAT to display your mood on Twitter based upon the sentiment of your recent tweets.
