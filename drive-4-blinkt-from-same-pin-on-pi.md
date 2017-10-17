_https://forums.pimoroni.com/t/blinkt-multiple/5589/14_

Blinkt! should be pretty simple to get up and running with multiple instances yourself- the APA102 pixels just behave like a chain of shift registers- simpler, in fact- so driving them involves just toggling two pins: data and clock.

Now, you could get canny about the pinouts and have all the clock lines of your Blinkt! paired together onto one pin- allowing a theoretical maximum of (I think) 27 Blinkt! running from the same Pi without using an IO expansion. (That number might be a little high, since the i2c pins hardware pullups may cause trouble)

Anyway, I digress- you’re only really interested in this part of the Blinkt! library:

```
def _write_byte(byte):
    for x in range(8):
        GPIO.output(DAT, byte & 0b10000000)
        GPIO.output(CLK, 1)
        byte <<= 1
        GPIO.output(CLK, 0)

def _eof():
    GPIO.output(DAT, 0)
    for x in range(36):
        GPIO.output(CLK, 1)
        GPIO.output(CLK, 0)

def _sof():
    GPIO.output(DAT, 0)
    for x in range(32):
        GPIO.output(CLK, 1)
        GPIO.output(CLK, 0)

def show():
    """Output the buffer to Blinkt!"""
    global _gpio_setup

    if not _gpio_setup:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(DAT, GPIO.OUT)
        GPIO.setup(CLK, GPIO.OUT)
        atexit.register(_exit)
        _gpio_setup = True

    _sof()

    for pixel in pixels:
        r, g, b, brightness = pixel
        _write_byte(0b11100000 | brightness)
        _write_byte(b)
        _write_byte(g)
        _write_byte(r)

    _eof()
```

Which, for the sake of sanity, we can assume the GPIO pins are already set up and express as just:

```
def show():
    """Output the buffer to Blinkt!"""

    # First we output 32 clock pulses with DAT set to 0/LOW to reset the APA102s
    # This gets them ready for the data stream
    GPIO.output(DAT, 0)
    for x in range(32): # Toggle the clock 32 times, easy!
        GPIO.output(CLK, 1)
        GPIO.output(CLK, 0)

    # Loop through each pixel in the array of pixels
    # Each pixel is a tuple of (r, g, b, brightness)
    # Brightness is a 5bit value that's sent along with the pixel start
    # Then we send Blue, Green and Red in turn
    for pixel in pixels:
        r, g, b, brightness = pixel
        _write_byte(0b11100000 | brightness) # Add brightness (0-31) to the start indicator
        _write_byte(b) # Send Blue
        _write_byte(g) # Send Green
        _write_byte(r) # Send Red

     # Finally we output 36 clock pulses with DAT set to 0/LOW to latch the APA102s
    GPIO.output(DAT, 0)
    for x in range(36): # And now 36 times (don't ask!)
        GPIO.output(CLK, 1)
        GPIO.output(CLK, 0)

def _write_byte(byte):
    # All write byte does is set each bit in the byte to the DAT pin, one at a time
    # And then toggle the clock pin HIGH/LOW to clock that bit out
    # We use a mask "0b10000000" to select the highest bit (APA102s are most-significant-bit first)
    # Then we shift the byte left one place, so the next bit becomes the highest
    #
    # So if we want to send 172 (0b10101100) something like this happens:
    # 0b10101100 & 0b10000000 = 1
    # 0b01011000 & 0b10000000 = 0
    # 0b10110000 & 0b10000000 = 1
    # 0b01100000 & 0b10000000 = 0
    # ...  and so on

    for x in range(8): # Loop through 8 bits of our bytes (0-255)
        GPIO.output(DAT, byte & 0b10000000) # Set the MSB to DAT
        GPIO.output(CLK, 1) # Toggle the clock HIGH
        byte <<= 1 # Shift the byte left one place
        GPIO.output(CLK, 0) # Toggle the clock LOW
```

So- challenge time :D

Armed with the breakdown above, can you write some Python code to run your 4 Blinkt! (or however many you have) from different Clock/Dat pins on your Pi? Don’t worry about sharing the clock yet. You can just duplicate, or functionize the code above to substitute CLK/DAT for the pins of each Blinkt!.
