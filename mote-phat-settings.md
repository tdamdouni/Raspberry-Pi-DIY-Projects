# The Technical Explanation

Okay. So the APA102 pixels are basically a set of tiny shift registers, each with its own memory. These pixels remember what you told them- so if you say “Be green!” they will happily sit and be green for as long as you like until they’re told to do something else.

Or… if random noise happens to look enough like a signal they might decide to light up or change colour seemingly of their own accord. All they need to assume a signal is valid is a sequence of three 1s 0b111, then the next 5 1s are the brightness, and the following 24 are the colour… so…

If you happen to get any kind of interference close enough to Mote pHAT it’s likely to induce something close to a signal on both the clock and the data line, basically shooting a stream of 1s into the APA102 pixels and making them blindingly 100% on.

This might not be what’s happening in your case, but it’s likely.

# The Fix

As you’ve found out for yourself, the best fix is to simply keep the pixels updated. You suggest every 10 seconds, but ideally you’d just have your while loop constantly update them at a sensible framerate that depends on how smooth you want your brightness transitions to be. Not so fast that your Pi’s CPU is eaten entirely by pixel updates, but fast enough to eliminate the chance of random noise causing rogue lighting output.

And this is what you’ll find most things that drive APA102 or WS2812 pixels will do- constantly update the pixels.

Now I normally don’t rush to give out code examples, but I think this is a good opportunity to demonstrate how I’d accomplish this sort of program- paying particular attention to the smoothness and timing of effects and the need to output constant updates to the pixels:

```python
import motephat
import sys
import select
import time

# Note it's conventional to use ALL_CAPS to denote constant values
# that we don't expect the program to ever change during runtime.

# Updates per second
# A higher number consumes more CPU but gives smoother transitions
FPS = 60

# Speed of the transition, higher is faster
# Due to gamma weirdness, turning on always feels faster than turning off
# since most of the high-end brightness steps are the same
# A higher speed will look smoother at higher frame rates
SPEED = 1.0

# The colour to display
RED = 255
GREEN = 110
BLUE = 40

# Internal state
brightness = 0.0
lights_on = False

motephat.clear()
motephat.show()

print("Press enter to toggle...")

# This is a non-blocking (doesn't stop our code from running while it waits)
# method for getting a character from stdint (Standard Input) which is where
# the text you type into your Python program goes when you hit enter.
# select is a method for checking if there's anything there before we try to read.
def get_char():
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        return sys.stdin.read(1)
    return None

while True:
    # Get a char from the standard input
    char = get_char()

    if char == '\n': # Look for a newline chr(10), ie: enter key pressed
        lights_on = not lights_on # Toggle the lights
        print("Lights {}".format("on" if lights_on else "off")) # Print the current status

    # If lights should be on and the brightness is less than 1.0
    # then start increasing the brightness each step
    if lights_on and brightness < 1.0:
        brightness += 1.0 / 255 / FPS * SPEED * 100
        brightness = min(1.0, brightness)

    # If lights should be off and the brightness is greater than 0.0
    # then start decreasing the brightness each step
    elif not lights_on and brightness > 0:
        brightness -= 1.0 / 255 / FPS * SPEED * 100
        brightness = max(0.0, brightness)

    # Show the current state of the LEDs
    # This happens continuously even when brightness is not changing
    # In this instance we set global brightness to always be 1.0, because the APA102s
    # only have 32 steps of brightness, which doesn't make for smooth transitions at all
    # By scaling the values themselves we approach 256 steps, eight times as many!
    # Note: Global brightness is only really useful as a set-and-forget limit on brightness
    motephat.set_all(int(RED * brightness), int(GREEN * brightness), int(BLUE * brightness), 1.0)
    motephat.show()

    # Sleep a little,
    # In this instance we're working to an approximate framerate, so we
    # we sleep by 1 second, divided by the number of frames we want in a second
    time.sleep(1.0 / FPS)
```


Even this code isn’t perfect. You will probably notice that the LEDs appear to turn off slower than they turn on. They’re actually transitioning through the steps at the same speed each way, but the changes in the higher-end of the brightness are much less perceptible than those in the lower end.

Also, you might notice red/green kicking in first. This is a problem that this method introduces that’s less pronounced when you use global brightness.
