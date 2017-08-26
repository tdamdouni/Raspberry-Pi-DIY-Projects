import urandom
import neopixel

class WizardRing:

    def __init__(self, pin, pixel_count, pixel_spacer):
        self.pixel_off = (0, 0, 0)

        # Pin where the NeoPixel ring is located:
        self.pin = pin

        # Number of pixels on the ring:
        self.pixel_count = pixel_count

        # Space between pixels to light:
        self.pixel_spacer = pixel_spacer

        self.offset = 0
        self.randomize_color()

        # https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
        self.pixels = neopixel.NeoPixel(pin, pixel_count, auto_write=False)
        self.pixels.brightness = 0.05

    def randomize_color(self):
        self.red = urandom.randrange(0, 150, 1)
        self.green = urandom.randrange(0, 150, 1)
        self.blue = urandom.randrange(0, 150, 1)

    def set_color(self, color):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]

    def get_color(self):
        return (self.red, self.green, self.blue)

    # Advance one frame of animation:
    def animate(self):

        # Kill previous trailing pixels:
        for target_pixel in range(self.offset - 1, self.pixel_count, self.pixel_spacer):
            self.pixels[target_pixel] = self.pixel_off

        # Light trailing pixels:
        for target_pixel in range(self.offset, self.pixel_count, self.pixel_spacer):
            self.pixels[target_pixel] = (int(self.red / 4), int(self.green / 4), int(self.blue / 4))

        # Increase pixel offset until it hits 6, then roll back to 0:
        self.offset += 1
        if self.offset == self.pixel_spacer:
            self.offset = 0;

        # Light new pixels:
        color = (self.red, self.green, self.blue)
        for target_pixel in range(self.offset, self.pixel_count, self.pixel_spacer):
            self.pixels[target_pixel] = color

        self.pixels.show()
