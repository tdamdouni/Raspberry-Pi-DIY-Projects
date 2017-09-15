_http://forums.pimoroni.com/t/pan-tilt-lib-for-c-c/5918/2_

Presently there is no documentation on the i2c interface, since the firmware that drives Pan Tilt HAT is completely custom, however briefly:

0x00 = Config
0x01 = Servo 1 (two bytes, most significant first)
0x03 = Servo 2 (ditto)
0x05 = ws2812 pixel data, this goes from register 0x05 to 0x4c
0x4d = update register, trigger an update for the ws2812 pixels

The 2 byte unsigned integers for Servo 1 and Servo 2 represent the time, in microseconds, of the servo high pulse. A pulse is typically something like 500 to 2500 (0.5ms to 2.5ms) microseconds which is repeated every 20 milliseconds.

The config register is as follows, from LSB to MSB:

0 - Enable Servo 1
1 - Enable Servo 2
2 - Enable lights
3 - Light mode - 1 = ws2812, 0 = regular on/off toggle
4 - Light polarity - 1 = active low, 0 = active high

The ws2812 pixel data is 72 bytes long- it doesn’t care if you send 18 sets of RGBW data or 24 sets of RGB data. It also doesn’t care what order the pixels are sent in, but will forward the data you give it directly on to the attached ws2812 or sk6812 pixels. So, use the pixel order and format suitable for whatever you have connected.

Hopefully that should get you started! I should probably codify this in a brief datasheet.
