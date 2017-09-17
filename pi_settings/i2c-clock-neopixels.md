I2C belongs to the faimly of 'clocked' communication protocols: the SCL pin toggles high and low for every bit sent, telling the devices at the other end of the connection when to read the signal on SDA, or when it's safe to write their own signal to SDA.

Having a clock signal makes protocols much less sensitive to signal timing. Everything is driven by the high/low transitions on SCL, and it usually doesn't matter how far apart those transitions are.

NeoPixel data signals belong to the 'self-clocked' family, so the amount of time between high/low transitions determines the value of the bit that was sent. For those, a difference of 150ns changes a color value, and a 50us gap tells the strip to start a new update. There's very little wiggle room.

You can't transmit NeoPixel data for multiple reasons, the biggest being that I2C isn't fast enough. NeoPixel signals travel at 800kHz, and I2C defaults to 100kHz. You can bump I2C up to 400kHz, but that's still too slow by half.
