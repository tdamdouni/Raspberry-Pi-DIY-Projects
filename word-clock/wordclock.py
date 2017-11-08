import colorsys
import datetime
import time
import unicornhat
'''

Grid Layout
A T W E N T Y *
Q U A R T E R *
F I V E H A L F
* P A S T O * *
F I V E I G H T
S I X T H R E E
T W E L E V E N
F O U R N I N E

'''

# Constants
NUM_PIXELS   = 64
NUM_ROWS     = 8
PIXEL_SPREAD = 4 * NUM_PIXELS
SHIFT_DELAY  = 100

# Binary Masks
MFIVE    = 0xF00000000000
MTEN     = 0x5800000000000000
AQUARTER = 0x80FE000000000000
TWENTY   = 0x7E00000000000000
HALF     = 0x0F0000000000
PAST     = 0x7800000000
TO       = 0x0C00000000
ONE      = 0x43
TWO      = 0xC040
THREE    = 0x1F0000
FOUR     = 0xF0
FIVE     = 0xF0000000
SIX      = 0xE00000
SEVEN    = 0x800F00
EIGHT    = 0x1F000000
NINE     = 0x0F
TEN      = 0x01010100
ELEVEN   = 0x3F00
TWELVE   = 0xF600

mask = 0x00
pixel_step = 0

def apply_mask():
    global mask # To modify the mask
    global pixel_step
    
    pixel_mask = 1 << NUM_PIXELS - 1

    for pixel in range(0,NUM_PIXELS):
        value = mask & pixel_mask

        if value == pixel_mask:
            # Turn on
            set_color_step(pixel)
        else:
            # Turn off
            unicornhat.set_pixel(pixel%NUM_ROWS,pixel//NUM_ROWS, 0, 0, 0)
            
        pixel_mask = pixel_mask >> 1

    # Display the changes
    unicornhat.show()
    # Increment the animation
    pixel_step = pixel_step + 1
    pixel_step = pixel_step % PIXEL_SPREAD
    # Reset the mask
    mask = 0x00
    
    time.sleep(SHIFT_DELAY/1000.0)

def set_color_step(pixel, value=1.0):
    # Spread HSV values across the matrix.
    # Stretch possible values over the matrix
    rgb = colorsys.hsv_to_rgb((1.0/PIXEL_SPREAD)*((pixel + pixel_step)%PIXEL_SPREAD), 1.0, value)
    r, g, b = [int(x*255) for x in rgb]
    unicornhat.set_pixel(pixel%NUM_ROWS,pixel//NUM_ROWS, r, g, b)

def create_mask():
    global mask # To modify the mask
    
    # Get the time
    the_time = datetime.datetime.now()
    hour   = the_time.hour
    minute = the_time.minute

    # Create the mask
    # Minute
    if   minute >= 5  and minute < 10:
        mask |= MFIVE
        mask |= PAST
    elif minute >= 10 and minute < 15:
        mask |= MTEN
        mask |= PAST
    elif minute >= 15 and minute < 20:
        mask |= AQUARTER
        mask |= PAST
    elif minute >= 20 and minute < 25:
        mask |= TWENTY
        mask |= PAST
    elif minute >= 25 and minute < 30:
        mask |= TWENTY
        mask |= MFIVE
        mask |= PAST
    elif minute >= 30 and minute < 35:
        mask |= HALF
        mask |= PAST
    elif minute >= 35 and minute < 40:
        mask |= TWENTY
        mask |= MFIVE
        mask |= TO
    elif minute >= 40 and minute < 45:
        mask |= TWENTY
        mask |= TO
    elif minute >= 45 and minute < 50:
        mask |= AQUARTER
        mask |= TO
    elif minute >= 50 and minute < 55:
        mask |= MTEN
        mask |= TO
    elif minute >= 55:
        mask |= MFIVE
        mask |= TO

    # Hour
    hour_mod_12 = hour % 12
    if minute < 35:
        if   hour_mod_12 == 1:
            mask |= ONE
        elif hour_mod_12 == 2:
            mask |= TWO
        elif hour_mod_12 == 3:
            mask |= THREE
        elif hour_mod_12 == 4:
            mask |= FOUR
        elif hour_mod_12 == 5:
            mask |= FIVE
        elif hour_mod_12 == 6:
            mask |= SIX
        elif hour_mod_12 == 7:
            mask |= SEVEN
        elif hour_mod_12 == 8:
            mask |= EIGHT
        elif hour_mod_12 == 9:
            mask |= NINE
        elif hour_mod_12 == 10:
            mask |= TEN
        elif hour_mod_12 == 11:
            mask |= ELEVEN
        elif hour_mod_12 == 0:
            mask |= TWELVE
    else:
        if   hour_mod_12 == 1:
            mask |= TWO
        elif hour_mod_12 == 2:
            mask |= THREE
        elif hour_mod_12 == 3:
            mask |= FOUR
        elif hour_mod_12 == 4:
            mask |= FIVE
        elif hour_mod_12 == 5:
            mask |= SIX
        elif hour_mod_12 == 6:
            mask |= SEVEN
        elif hour_mod_12 == 7:
            mask |= EIGHT
        elif hour_mod_12 == 8:
            mask |= NINE
        elif hour_mod_12 == 9:
            mask |= TEN
        elif hour_mod_12 == 10:
            mask |= ELEVEN
        elif hour_mod_12 == 11:
            mask |= TWELVE
        elif hour_mod_12 == 0:
            mask |= ONE

unicornhat.brightness(0.4)

# Main Loop
while (True):
    create_mask()
    apply_mask()



