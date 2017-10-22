from sense_hat import SenseHat
import time

sense = SenseHat()

number = [
0,1,1,1, # Zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, # One
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, # Two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, # Three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, # Four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, # Five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, # Six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, # Seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, # Eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, # Nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

celcius_color = [255,0,0] # Red
fahrenheit_color = [0,255,0] # Green
negative_celcius_color = [0,255,255] # Cyan
negative_fahrenheit_color = [0,0,255] # Blue
empty = [0,0,0] # Black

display = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

while True:
    celcius = int(round(sense.get_temperature()))
    fahrenheit = int(round(1.8 * celcius + 32))

    if celcius < 0:
        celcius = abs(celcius)
        celcius_color = negative_celcius_color
    if fahrenheit < 0:
        fahrenheit = abs(fahrenheit)
        fahrenheit_color = negative_fahrenheit_color

    # Map digits to the display array
    pixel_offset = 0
    index = 0
    for index_loop in range(0, 4):
        for counter_loop in range(0, 4):
            display[index] = number[int(celcius/10)*16+pixel_offset]
            display[index+4] = number[int(celcius%10)*16+pixel_offset]
            display[index+32] = number[int(fahrenheit/10)*16+pixel_offset]
            display[index+36] = number[int(fahrenheit%10)*16+pixel_offset]
            pixel_offset = pixel_offset + 1
            index = index + 1
        index = index + 4

    # Color the temperatures
    for index in range(0, 64):
        if display[index]:
            if index < 32:
                display[index] = celcius_color
            else:
                display[index] = fahrenheit_color
        else:
            display[index] = empty

    # Display the temperatures
    sense.low_light = True # Optional
    sense.set_pixels(display)
    time.sleep(1)
