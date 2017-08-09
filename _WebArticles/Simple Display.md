# Simple Display

_Captured: 2015-12-05 at 10:47 from [seanmckaybeck.com](https://seanmckaybeck.com/simple-display.html)_

I made a basic setup that displays the current price of silver per ounce.

Materials

  * 1 Raspberry Pi model B
  * 13 female/female jumper wires
  * [1 female DC power adapter](https://www.adafruit.com/products/368)

I used the Arch Linux image for the Raspberry Pi's operating system. Follow [this](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/wiring-the-display) guide for wiring the display to the Pi. Once you have the operating system set up you need the proper software. Use [this](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/testing) guide for installing the necessary software for the display. In order to work with my code you need Python 3.4 and you need `libfreetype` installed. On Arch you can install it with `pacman -S freetype2`. You will also need `Pillow` which can be installed with `pip install pillow`. Make sure you install `libfreetype` before `pillow`. The font used in the code is also based on the path on Arch.

The Code

Note that this must be saved and run from within the install directory of the matrix code. Every ten minutes it will grab the current price per ounce of silver, create a `ppm` image in the specified font, then display it as a scrolling message on the LED matrix.

```Python

import time

from subprocess import Popen

from PIL import ImageFont

from PIL import Image

from PIL import ImageDraw

import requests

from bs4 import BeautifulSoup

URL = 'http://www.silverpriceoz.com/silver-price-per-ounce/'

def get_silver_price():

r = requests.get(URL)

soup = BeautifulSoup(r.content)

price_text = soup.find_all('b')[2].text.lstrip()

return price_text[0:5]

def save_image():

price = get_silver_price()

text = (("Price per ounce $", (0, 255, 0)), (price, (192, 192, 192)))

font = ImageFont.truetype("/usr/share/fonts/TTF/FreeSans.ttf", 16)

all_text = ""

for text_color_pair in text:

t = text_color_pair[0]

all_text = all_text + t

print(all_text)

width, ignore = font.getsize(all_text)

print(width)

im = Image.new("RGB", (width + 30, 16), "black")

draw = ImageDraw.Draw(im)

x = 0;

for text_color_pair in text:

t = text_color_pair[0]

c = text_color_pair[1]

print("t=" \+ t + " " \+ str(c) + " " \+ str(x))

draw.text((x, 0), t, c, font=font)

x = x + font.getsize(t)[0]

im.save("test.ppm")

def main():

while True:

save_image()

p = Popen(['./led-matrix', '1', 'test.ppm'])

time.sleep(600) # 10 minutes

p.terminate()

p.wait()

if __name__ == '__main__':

main()

```

Note that a good chunk of this (the display code) was taken from the Adafruit tutorial.

The Result

I can't get the Imgur gifv or Gfycat images to embed properly here so below are the links (higher quality is better!).

http://gfycat.com/GrotesqueImpishDrafthorse http://i.imgur.com/vXqUxLG.gifv

This entry was tagged as [electronics](https://seanmckaybeck.com/tag/electronics.html) [raspberry-pi](https://seanmckaybeck.com/tag/raspberry-pi.html)
