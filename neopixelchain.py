# NeoPixel chain class.  Allows you to concatenate multiple NeoPixel objects
# into one long chain with the same interface (get, set, fill, write).  Great
# for when you have disparate sets of pixels that need to act like one long
# chain.
# Example usage:
#   import neopixel
#   import neopixelchain
#   # Construct your neopixels objects:
#   np1 = neopixel.NeoPixel(...)
#   np2 = neopixel.NeoPixel(...)
#   np3 = neopixel.NeoPixel(...)
#   # Create the chain by passing all the neopixel objects to the initializer:
#   chain = neopixelchain.NeoPixelChain(np1, np2, np3)
#   # The chain has the same interface as the NeoPixel object:
#   chain.fill((0,0,0))
#   chain.write()
#   chain[0] = (255, 0, 0)             # First pixel red
#   chain[chain.n//2] = (0, 255, 0)    # Middle pixel green
#   chain[chain.n-1] = (0, 0, 255)     # Last pixel blue
#   chain.write()
# Author: Tony DiCola


class NeoPixelChain:

    def __init__(self, *pixels):
        # Enumerate all the NeoPixel objects and count up their total length.
        self.n = 0
        for np in pixels:
            self.n += np.n
        self._pixels = pixels

    def _find_pixel(self, index):
        # Given an index into the chain, find the strip and index within that
        # strip of the pixel.  Returns a 2-tuple of strip index, pixel index
        # (relative to the strip) for the specified pixel.  If the index is
        # outside the range of the chain then (None, None) is returned.
        if index < 0 or index >= self.n:
            return (None, None) # Ignore indices outside the allowed range.
        # Find the pixel strip that has the pixel at the specified index.
        for i in range(len(self._pixels)):
            if index < self._pixels[i].n:
                # Found the strip with the pixel.
                return (i, index)
            else:
                # Didn't find the pixel in this strip, decrement index and move
                # to next strip.
                index -= self._pixels[i].n
        # Should never get here, but just in case return (None, None) since the
        # index couldn't be found.
        return (None, None)

    def __setitem__(self, index, val):
        strip, index = self._find_pixel(index)
        if strip is None:
            return
        self._pixels[strip][index] = val

    def __getitem__(self, index):
        strip, index = self._find_pixel(index)
        if strip is None:
            return
        return self._pixels[strip][index]

    def fill(self, color):
        for np in self._pixels:
            np.fill(color)

    def write(self):
        for np in self._pixels:
            np.write()
