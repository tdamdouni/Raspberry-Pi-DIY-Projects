# [Unicorn Hat](https://shop.pimoroni.com/products/unicorn-hat) FFT audio visualizer
If you're looking for something to use with [PiGlow](https://shop.pimoroni.com/products/piglow), [check this out](https://gist.github.com/daniel-j/f1406e301ab2c38ba53c)! It's all Python!

## Demo!
Click to watch demo on YouTube

[![YouTube video demo](http://img.youtube.com/vi/g3sxXgLr1uQ/0.jpg)](http://www.youtube.com/watch?v=g3sxXgLr1uQ)

## Install and build
```
# Install dependencies
sudo apt-get update && sudo apt-get install libfftw3-dev

# Important to clone recursive to get unicorn-hat lib!
git clone --recursive https://github.com/daniel-j/unicorn-fft.git

cd unicorn-fft

# Compile unicorn-fft and unicorn-hat lib. Use just 'make' to build only unicorn-fft
make all
```
You can then try the examples `examples/arecord.sh` and `examples/radio.sh`

`unicorn-fft` expects a raw/PCM stream in the format `Signed 16 bit Little Endian, Rate 44100 Hz, Mono`

## Thanks
This project uses code from [raspberry-vu](https://github.com/rm-hull/raspberry-vu) which is a fork of [Impulse](https://github.com/ianhalpern/Impulse), which I base my FFTW function calls on.

Also special thanks to Damien for his guide [FFT Averages](http://code.compartmental.net/2007/03/21/fft-averages/), which makes it all prettier!
