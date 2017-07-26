#!/usr/bin/env python
# coding=utf-8

# unicorn-scroller - A scrolling information display for the
# Pimoroni Unicorn HAT/PHAT on Raspberry Pi.
#
# By Andrew Wedgbury <wedge@sconemad.com>
# See README.md for more info
# 

import unicornhat as unicorn
from PIL import ImageFont, ImageColor, ImageDraw, ImageFilter, Image
import time, sys, getopt, os, re, subprocess
from random import randint

#
# --- Things you probably want to set ---
#

# Select rotation 0, 90, 180, 270 depending on how you mount the Pi
# i.e. 0 means the HDMI socket is at the bottom
unicorn.rotation(0)

# Display brightness (0...1, 1 is very very very bright)
brightness_min = 0.3
brightness_max = 0.6
estimate_brightness = 1

# Text font
# It's difficult to find a font that looks good at 8 pixels high -
# The best I've found is Minecraftia-Regular, which you can download
# from http://www.dafont.com/minecraftia.font
# Unzip the font into the same directory as the script.
font = ImageFont.truetype("Minecraftia-Regular.ttf", 8)

# Y-shift to apply to the font to make it display correctly
font_offset = -2

# Pause between steps in seconds, defines the scroll speed
# Too fast and you can't read it, or can you?
step = 0.05

# Background colour
back='black'

# Directory containing message scripts
messages_dir = 'messages'

# Directory containing images
images_dir = 'images'

# Detect HAT or PHAT layout and adapt accordingly
# If yours isn't detected properly, then you may need
# to change the following line to say HAT or PHAT
# instead of AUTO:
unicorn.set_layout(unicorn.AUTO)
geom = unicorn.get_shape()
if (geom[0] != geom[1]):
  unicorn.set_layout([
    [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ],
    [8 , 9 , 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31]
  ])
  step *= 2


def set_brightness(pc):
    b = brightness_min + ((brightness_max - brightness_min) * pc / 100.0)
    if (b > brightness_max): b = brightness_max
    if (b < brightness_min): b = brightness_min
    unicorn.brightness(b)

def get_item_size(item):
  width = 1
  frames = 1
  if ('text' in item):
    width += font.getsize(item['text'])[0]
  elif ('image' in item):
    width += item['image'].size[0]
    frames = item['image'].size[1] / 8
  return width,frames

def get_size(items):
  width = 0
  frames = 1
  for item in items:
    w,f = get_item_size(item)
    width += w
    frames = max(f, frames)
  return width,frames

def render(items):
  width,frames = get_size(items)
  image = Image.new('RGB', (width,8), back)
  pos = 0
  for item in items:
    w,f = get_item_size(item)
    if ('text' in item):
      draw = ImageDraw.Draw(image)
      draw.text((pos, font_offset), item['text'], font=font, fill=item['fore'])
    elif ('image' in item):
      image.paste(item['image'], (pos,0))
    pos += w
  return image

def scroll(image):
  width,height = image.size
  for offset in range(-geom[1],width):
    for x in range(geom[1]):
      for y in range(8):
        if ((x+offset < 0) | (x+offset >= width)):
          r,g,b = ImageColor.getrgb(back)
        else:
          r, g, b = image.getpixel((x+offset,y))
        unicorn.set_pixel(x,y, r,g,b)
    unicorn.show()
    time.sleep(step)

def process_line(l):
#  print l
  global colour
  items = []
  global estimate_brightness
  m = re.match(r'^colou?r: *(.+) *$', l)
  if (m):
    try:
      c = ImageColor.getrgb(m.group(1))
      colour = m.group(1)
    except ValueError:
      print 'ERROR: Unknown colour: %s' % m.group(1)
      colour = 'white'
    return

  m = re.match(r'^text:(.+)$', l)
  if (m):
    return {'text':m.group(1), 'fore':colour}

  m = re.match(r'^image:(.+)$', l)
  if (m):
    try:
      im = Image.open(images_dir + '/' + m.group(1))
      return {'image':im}
    except IOError:
      return {'text:<?%s?>' % (m.group(1))}
    return

  m = re.match(r'^estimated-brightness: *(\d+) *$', l)
  if (m and estimate_brightness):
    set_brightness(int(m.group(1)))
    return

  m = re.match(r'^measured-brightness: *(\d+) *$', l)
  if (m):
    set_brightness(int(m.group(1)))
    # Disable brightness estimation if measured
    estimate_brightness = 0
    return

def process_message(f):
  items = []
  global z
  p = subprocess.Popen([f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out,err = p.communicate()
  if (err):
    print "ERROR(%s): %s" % (f,err)
  for l in out.splitlines(0):
    item = process_line(l.decode('utf-8'))
    if (item): items.append(item)
  image = render(items)
  scroll(image)


# Set medium brightness to start
set_brightness(50)

# Main loop
i = 0
while True:
  i += 1
  dir = os.listdir(messages_dir)
  dir.sort()
  for f in dir:
    path = messages_dir + '/' + f
    if (not os.access(path, os.X_OK)): continue
    m = re.match(r'^(\d+)\-(\d+)(\-[^~]+)?$', f)
    if (m):
      d = int(m.group(1))
      e = int(m.group(2))
      if (i % d == e):
        process_message(path)
