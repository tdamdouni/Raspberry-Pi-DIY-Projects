#import io
import time
#import psutil
#import signal
#import sys
#import bmp180

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

#from PIL import Image
#from PIL import ImageDraw
#from PIL import ImageFont

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

CONTRAST=20

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=CONTRAST)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('fonts/MiniPower.ttf', 8)

try:
	while 1:
  
    for con in range(10,90,10):
      disp.set_contrast(con)
      draw.text((0,20), "Contrast:"+str(con), font=font)
		  disp.image(image)
		  disp.display()
      time.sleep(2)
except:
	draw.rectangle((0,0,83,47), outline=255, fill=255)
	# Display image.
	disp.image(image)
	disp.display()
