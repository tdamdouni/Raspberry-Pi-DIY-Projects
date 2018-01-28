_https://forums.adafruit.com/viewtopic.php?f=50&t=126235_

Getting NeoPixels to work with a RasPi is a challenge.

NeoPixels use self-clocked data signals.. basically an 800kHz square wave where the width of the high pulse says whether the bit is a 0 or a 1. The difference between those values is about 150ns.

Linux is a time-sliced operating system that gives each process about 10ms on the CPU, then suspends it, stores the data it was using, and gives the next process a turn. That works for things moving at human speed like keyboard and mouse input, but makes it hard for the RasPi to handle signals faster than about 100Hz.

In general, it's easier to use a microcontroller to control NeoPixels, and to let the RasPi communicate with the microcontroller. A Trinket or Gemma can run a NeoPixel ring without any problems, and can watch one of the RasPi's GPIO pins if you just want an on/off signal.
