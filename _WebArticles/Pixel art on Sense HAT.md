# Pixel art on Sense HAT

_Captured: 2015-12-22 at 10:05 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/pixel-art-on-sense-hat/)_

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2015/12/2015-12-21-17_00_33-Greenshot-capture-form.png)

We know what you're thinking: 8×8 pixel art doesn't seem like a whole lot of pixels. And if you were thinking that, you'd be right. That's 64 pixels to try to convey something - simple for low-complexity objects, but for proper pixel art it seems like a tall order. If you think back to the early days of gaming, though, there are plenty of examples of sprites that didn't use many pixels at all and looked… passable. The main limitations in those days were the number of colours you could have on screen at once, and with the Sense HAT we have the power to use a full RGB spectrum, utilising every pixel to make something a bit better than on the old Atari 2600. Grab a sprite, and let's go!

_The full article can be found in [The MagPi 39](https://www.raspberrypi.org/magpi/issues/39)_

**STEP-01** Get the Sense HAT ready

If you've upgraded to the newer version of Raspbian, Jessie, all you need to do is switch off the Raspberry Pi, remove the power cable, and then plug the Sense HAT on top of the Pi. Turn it back on and it's ready to use.

If you haven't made the update, you'll need to install a few extra libraries first. Open the terminal and run the following commands:

…and then reboot the Raspberry Pi (which you can also do in the terminal with sudo reboot if you wish!)

**STEP-02** Find some art

There's a few ways you can do this: using Google or searching on something like DeviantArt with the right keywords ('8×8 pixel art' is a good start) and you should be able to find a suitable sprite for showing off on your Sense HAT. You could also experiment with a square picture (from something like Instagram) to see what the code will spit out, or you can draw your own pixel art in something like Swanky Paint. For testing this tutorial, we grabbed one of the 100 characters from a sprite sheet created by [Johan Vinet](http://twitter.com/johanvinet), which can be found on [his blog](http://bit.ly/1jxaJ3m).

**STEP-03** Prepare the art

The Sense HAT can only display 64 pixels, and our code assumes the image you have is going to be exactly that. On a normal computer, use an image editor such as the free software GIMP to prepare the image. Remove any borders (you may need to zoom right in to make sure) by cropping the image and save it to a file name you'll remember with the extension .png or .gif. This is especially important if the 8×8 art you have isn't actually saved as an 8×8 image; for instance, if each 'pixel' in the art is six pixels wide, like in our code.

**STEP-04** Study the pixel art

As mentioned above, your pixel art may not be actually saved by the pixel. In the code we've created, it takes this into account. The easiest way to check the width of the pixels is to look at the resolution of the image. In our case, it's 48×48, which means that each 'pixel' is six real pixels wide (and high, because it's a square). You can check this in GIMP by using a square pixel brush and increasing the size until it's the same as the pixels in your image. Alternatively, once you've cropped the image, you can scale the image to be 8×8; this may not have the desired results, though, as it tries to squash everything together.

**STEP-05** Load it all on the Raspberry Pi

Put the image on the Raspberry Pi and open it in the image viewer to make sure it transferred fine. We did this by plugging the SD card directly into the computer we prepared the image on and copied it to a directory called 'SenseHAT' in the home folder, but you can always put it on a USB stick and copy it over from within the Pi or upload it to your cloud storage and download it to the Pi.

**STEP-06** Write the code!

Follow along to the code listing and tweak it to suit your own pixel art, whether this means you need to change the location of the file in the code (our code assumes you've put it in a folder called 'SenseHAT' in Raspbian's home directory) or if you need to change the width of each pixel to 1 or higher. Press F5 to run the code, and it will then display the image on the Sense HAT for three seconds before turning itself off.

### Code listing

```python 
from sense_hat import SenseHat
import time
from PIL import Image
import os

# Open image file
image_file = os.path.join(
os.sep,"/home","pi","SenseHAT","pixelart.png")
img = Image.open(image_file)

# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())

# Get the 64 pixels you need
pixel_width = 6
image_width = pixel_width*8
sense_pixels = []
start_pixel = 0
while start_pixel < (image_width*64):
    sense_pixels.extend(image_pixels[start_pixel:(
start_pixel+image_width):pixel_width])
    start_pixel += (image_width*pixel_width)

# Display the image
sense = SenseHat()
sense.set_rotation(r=180)
sense.set_pixels(sense_pixels)
time.sleep (3)

sense.clear()
```
