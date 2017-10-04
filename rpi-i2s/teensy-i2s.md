# Teensy I2S Notes

Audio data uses I2S signals, TX (to headphones and/or line out) and RX (from line in or mic), and 3 clocks:

```
LRCLK - 44.1 kHz - Pin 23
BCLK  - 1.41 MHz - Pin 9
MCLK  - 11.29 MHz - Pin 11
```
