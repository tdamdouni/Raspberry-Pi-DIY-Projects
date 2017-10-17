#Adapted from Adafruit's dotstar python example (https://github.com/adafruit/Adafruit_DotStar_Pi)

from PIL import Image

numpixels = 16         # Number of LEDs in strip
filename  = "hello.png" # Image file to load

from mote import Mote
mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

# Load image in RGB format and get dimensions:
print "Loading..."
img       = Image.open(filename).convert("RGB")
pixels    = img.load()
width     = img.size[0]
height    = img.size[1]
print "%dx%d pixels" % img.size

if(height > mote.get_pixel_count(1)): height = 15

# Calculate gamma correction table, makes mid-range colors look 'right':
gamma = bytearray(256)
for i in range(256):
	gamma[i] = int(pow(float(i) / 255.0, 2.7) * 255.0 + 0.5)

print "Displaying..."

try:
	while True:                              # Loop forever

		for x in range(width):           # For each column of image...
			for y in range(height):  # For each pixel in column...
				value = pixels[x, y]   # Read pixel in image
				mote.set_pixel(1,y, # Set pixel in strip
				gamma[value[0]],     # Gamma-corrected red
				gamma[value[1]],     # Gamma-corrected green
				gamma[value[2]])     # Gamma-corrected blue
			mote.show()             # Refresh LED strip

except KeyboardInterrupt:
	mote.clear()
	mote.show()
	quit()
