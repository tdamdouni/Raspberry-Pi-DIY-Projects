from sense_hat import SenseHat
import time
from PIL import Image
import os

# Download awesome image file source: http://johanvinet.tumblr.com/image/127476776680

# Open image file
image_file = os.path.join(os.sep,"/home","pi","Sense","pixels.gif")
img = Image.open(image_file)

# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
pixels = list(rgb_img.getdata())
width, height = img.size

# Set variables
border = 36
start = (width*border)
stop = len(pixels)-start
icon_size = 48
pixel_width = 6
gap = 24
step = 72
image_pixels = pixels[start:stop]

# Calculate pixels to sample from image
rows = range(border,len(image_pixels)-border,width*step)
grid = [range(item, item+width-(border*2), step) for item in rows]
image_rows = [range(value,value+(width*icon_size),width*pixel_width) for item in grid for value in item]
sample_pixels = [range(value,value+icon_size,pixel_width) for item in image_rows for value in item]

characters = [image_pixels[value] for item in sample_pixels for value in item]

# Break list into chunks
def chunks(list_data, chunk_size):
    return [list_data[item:item+chunk_size] for item in range(0, len(list_data), chunk_size)]
    
chunk_list = chunks(characters, 64) # select chunk size

# Display characters using LED matrix display on Sense HAT

sense = SenseHat()
sense.set_rotation(r=180)


for chunk in chunk_list:
    sense.set_pixels(chunk)
    time.sleep(1)

sense.clear()


