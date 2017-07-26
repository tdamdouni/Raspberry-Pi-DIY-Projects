# unicorn_phat

### Overview

A framework designed to make the Pi's Unicorn HAT/pHAT more useful.

The framework is designed with two concepts in mind: **bars** and **displays**. Bars are little tidbits of information that can be displayed in a row of pixels; displays are what you want to dedicate most of your display to.

You can fill your pixel matrix with bars, if you want, or go with one display and no bars.

---

### An Example

![Here's an example.](https://github.com/tusing/unicorn_phat/blob/images/out.gif?raw=true)

Here, we see one bar and one display. The bar, on the left, represents internet connectivity. It's white when connected, and blue pixels move along it every time the Pi pings the Google DNS servers.

When the Pi disconnects from the internet, the bar turns orange, and white pixels running along it represent failed attempts at pinging Google's DNS servers.

The display steals the show - it's a rainbow, and the speed of the rainbow increases with the load on the CPU.

Both of these examples are included, along with a few more. It should be relatively simple to change each example to represent something else (network UL/DL speeds, for example), or to create your own bars and displays from scratch.

---

### Other Tips

To start this script upon boot, add the following line to your ```/etc/rc.local```: ```(python3 /home/pi/unicorn_phat/functional_threaded.py)&```

A few displays are included:
* ```load_sparkles``` randomly turns pixels on and off, frequency increasing with load^2
* ```load_matrix``` sends randomly-colored pixels flying along the x and y axes of the board, speed increasing with load^2
* ```load_rainbow``` lets a rainbow flow across the board, speed increasing with load

A few bars are also included:
* ```color_bar``` displays a static color
* ```moving_pixel``` displays a pixel moving along a color bar
* ```internet_color``` utilizes the first two to display internet status and ping activity
