import time
import os
import subprocess
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from gpiozero import LED,Button
from picamera import PiCamera

yellow = LED(16)
button = Button(15)
dropbox = Button(21)
led_drop = LED(20)
stop = Button(26)
# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0


# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=40
)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load default font.
font = ImageFont.load_default()

logo_raspi = Image.open('/home/pi/gpiozerotest/Raspi128.png').resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')
disp.image(logo_raspi)
disp.display()
time.sleep(2)
draw.text((0,20), 'Press button', font=font)
disp.image(image)
disp.display()
time.sleep(5)
#check to see if button is pressed
if dropbox.is_pressed:
	logo_dropbox = Image.open('/home/pi/gpiozerotest/Dropbox-logo-300x300.jpeg').resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')
	print 'button pressed'
	disp.image(logo_dropbox)
	disp.display()
	led_drop.on()
	time.sleep(2)
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	draw.text((3,0), 'Dropbox', font=font)
	draw.text((3,10), 'Upload', font=font)
	draw.text((3,20), 'in progress', font=font)
	disp.image(image)
	disp.display()
	subprocess.call('/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/photo_output /photos', shell=True)
	draw.text((3,30), 'Completed', font=font)
	subprocess.call('sudo rm  /home/pi/photo_output/*.jpg', shell=True)
	disp.display()
	time.sleep(5)
	led_drop.off()
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        draw.text((3,0), 'Files uploaded', font=font)
        draw.text((3,10), 'Files erased', font=font)
        draw.text((3,20), 'Shutting down', font=font)
        disp.image(image)
        disp.display()
	time.sleep(2)
	subprocess.call('sudo halt', shell=True)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
draw.text((3,0), 'Pi Motion', font=font)
draw.text((3,10), 'Camera', font=font)
draw.text((3,20), 'Spencer Organ', font=font)
disp.image(image)
disp.display()
time.sleep(2)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
draw.text((3,0), 'Camera ready', font=font)
disp.image(image)
disp.display()
print ("Starting camera code")
startup = time.strftime('%X')

with PiCamera() as camera:
        #camera.start_preview()
        path, dirs, files = os.walk('/home/pi/photo_output').next()
	file_count = len(files)
	print (file_count)
	frame = 1 + file_count
        while True:
                if stop.is_pressed:
			draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        		draw.text((3,20), 'Safe stop', font=font)
        		disp.image(image)
        		disp.display()
        		time.sleep(2)
        		subprocess.call('sudo halt', shell=True)
		button.wait_for_press()
                yellow.source = button.values
                draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
		#disp.image(image)
                disp.display()
		draw.text((3,0),'Taking ....', font=font)
		disp.image(image)
                disp.display()
		print ("About to capture photo")
                camera.capture('/home/pi/photo_output/frame%03d.jpg' % frame)
                print (frame)
		draw.text((3,10),'Frames taken:', font=font)
		draw.text((10,20), str(frame), font=font)
                draw.text((0,30), str(startup), font=font)
		disp.image(image)
		disp.display()
		frame +=1



