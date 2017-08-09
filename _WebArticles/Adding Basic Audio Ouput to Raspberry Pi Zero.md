# Adding Basic Audio Ouput to Raspberry Pi Zero

_Captured: 2015-12-04 at 23:45 from [learn.adafruit.com](https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero?view=all)_

![](https://learn.adafruit.com/system/guides/images/000/001/182/medium800/raspberry_pi_IMG_0074.jpg?1449202288)

[ ![raspberry_pi_2885-06.jpg](https://learn.adafruit.com/system/assets/assets/000/028/852/medium800/raspberry_pi_2885-06.jpg?1449185414) ](https://learn.adafruit.com/assets/28852)

To keep the Raspberry Pi Zero as low cost and small as possible, the Pi foundation didn't include a 3.5mm audio jack. There's also no breakout pads for the audio output. This made us a little :( at first but then we thought "hey you know, we can probably figure out how to get audio out with a little hacking!

The Broadcom chipset used for the Pi does not have a true analog output. Instead, two pins are PWM (pulse-width-modulated) at very high speeds, and filtered. The PWM frequency has to be at least10x as high as the highest frequency we want to replicate in audio. Then, by adjusting the duty cycle of the PWM, we can 'fake' an audio signal.

Audio is 20Hz to 20KHz, and the PWM output from the Pi is 50MHz so we can easily filter the high 50MHz out (and anyways it cant be heard).

Looking at the Pi B schematic, we can see **PWM0_OUT** and **PWM1_OUT** are the left and right channels. **R21** and **R20** are voltage dividers to get the 3.3V signal down to about 1.1V max (that's the max peak-to-peak voltage you want for audio line level.

**C20/C26** works with **R21/R27** to create an "RC low-pass filter". You can calculate the cut-off frequency with 1/(2*pi*RC) = 1/(2*pi*270*33*10-9) = 17865 Hz which is pretty close to 20KHz!

**C48/C34** acts as a DC-filter capacitor, it only allows AC through - speakers and headphones don't like DC voltage!

Finally **8AV99** are ESD protection diodes. That's to protect the Pi from static coming in and zapping the PWM pins..

[ ![raspberry_pi_audiofilter.png](https://learn.adafruit.com/system/assets/assets/000/028/851/medium800/raspberry_pi_audiofilter.png?1449184817) ](https://learn.adafruit.com/assets/28851)

[ ![raspberry_pi_couldntreadall.png](https://learn.adafruit.com/system/assets/assets/000/028/853/medium800/raspberry_pi_couldntreadall.png?1449187450) ](https://learn.adafruit.com/assets/28853)

[ ![raspberry_pi_wiringpisnapshot.png](https://learn.adafruit.com/system/assets/assets/000/028/854/medium800/raspberry_pi_wiringpisnapshot.png?1449187615) ](https://learn.adafruit.com/assets/28854)

> _In case its not available, you can download it by clicking this button:_

[ ![raspberry_pi_copytgz.png](https://learn.adafruit.com/system/assets/assets/000/028/855/medium800/raspberry_pi_copytgz.png?1449187705) ](https://learn.adafruit.com/assets/28855)

> _Re-boot your Pi Zero up, and get back to the command line. Then mv the file over and un-tar it_

[ ![raspberry_pi_mvuntar.png](https://learn.adafruit.com/system/assets/assets/000/028/856/medium800/raspberry_pi_mvuntar.png?1449187755) ](https://learn.adafruit.com/assets/28856)

> _then go into the uncompressed directory and run the compile/install script with_

[ ![raspberry_pi_wiringcompile.png](https://learn.adafruit.com/system/assets/assets/000/028/857/medium800/raspberry_pi_wiringcompile.png?1449187879) ](https://learn.adafruit.com/assets/28857)

[ ![raspberry_pi_compiled.png](https://learn.adafruit.com/system/assets/assets/000/028/858/medium800/raspberry_pi_compiled.png?1449187891) ](https://learn.adafruit.com/assets/28858)

> _OK now you can run the updated version of gpio to read the states of all the pins:_

[ ![raspberry_pi_gpiov.png](https://learn.adafruit.com/system/assets/assets/000/028/859/medium800/raspberry_pi_gpiov.png?1449187945) ](https://learn.adafruit.com/assets/28859)

[ ![raspberry_pi_readall.png](https://learn.adafruit.com/system/assets/assets/000/028/860/medium800/raspberry_pi_readall.png?1449187996) ](https://learn.adafruit.com/assets/28860)

> _The table has a ton of information going on. What you want to look for is BCM pins #18 and #13_

[ ![raspberry_pi_nonalts.png](https://learn.adafruit.com/system/assets/assets/000/028/861/medium800/raspberry_pi_nonalts.png?1449188046) ](https://learn.adafruit.com/assets/28861)

[ ![raspberry_pi_pastegpioalt.png](https://learn.adafruit.com/system/assets/assets/000/028/863/medium800/raspberry_pi_pastegpioalt.png?1449188469) ](https://learn.adafruit.com/assets/28863)

[ ![raspberry_pi_saveit.png](https://learn.adafruit.com/system/assets/assets/000/028/864/medium800/raspberry_pi_saveit.png?1449188479) ](https://learn.adafruit.com/assets/28864)

[ ![raspberry_pi_alted.png](https://learn.adafruit.com/system/assets/assets/000/028/867/medium800/raspberry_pi_alted.png?1449188632) ](https://learn.adafruit.com/assets/28867)

> _Yep! You can see the new ALT settings._

[ ![raspberry_pi_IMG_0074.jpg](https://learn.adafruit.com/system/assets/assets/000/028/869/medium800/raspberry_pi_IMG_0074.jpg?1449189363) ](https://learn.adafruit.com/assets/28869)

> _I'm using a 3.5mm audio jack terminal block to wire up the left & right channels + ground._

[ ![raspberry_pi_audio.png](https://learn.adafruit.com/system/assets/assets/000/028/871/medium800/raspberry_pi_audio.png?1449189746) ](https://learn.adafruit.com/assets/28871)

> _Finally Force 3.5mm (Headphone)_

[ ![raspberry_pi_force.png](https://learn.adafruit.com/system/assets/assets/000/028/872/medium800/raspberry_pi_force.png?1449189753) ](https://learn.adafruit.com/assets/28872)

> _You only have to do this once, you can hit return and then Finish to exit_
