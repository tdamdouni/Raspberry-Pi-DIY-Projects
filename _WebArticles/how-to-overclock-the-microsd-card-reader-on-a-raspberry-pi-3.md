# How to overclock the microSD card reader on a Raspberry Pi 3

_Captured: 2017-08-24 at 23:36 from [www.jeffgeerling.com](https://www.jeffgeerling.com/blog/2016/how-overclock-microsd-card-reader-on-raspberry-pi-3)_

Late last year, I published a blog post with [comprehensive benchmarks of various microSD cards](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-microsd-card) used with the internal Raspberry Pi 2 reader, based on the comprehensive (and always-up-to-date [Raspberry Pi microSD card benchmark](http://www.pidramble.com/wiki/benchmarks/microsd-cards) page I maintain for the [Pi Dramble](http://www.pidramble.com/) project). After publishing the blog post, a few different readers pointed me to some overclocking tweaks that could help boost the speeds further for UHS microSD cards, allowing large file I/O speed to double, and random I/O to get a solid boost as well.

I finally got my hands on a Raspberry Pi 3 and wanted to see how it compares to the Pi 2 (review + benchmarks incoming!), but one of the first things I wanted to test was overclocking the microSD clock for better disk I/O. On average, with all the cards I've tested so far, **overclocking the microSD reader resulted in 25-50% better performance** for real-world disk operations (benchmarks further down in this post). And with a reliable power supply, you shouldn't need to worry about reliability or corruption (in my limited stress testing, I only had one corruption, and that was when I was using my cheaper iClever power supply).

## Overclock the microSD reader with sdhost

> First, a caveat: I generally [treat my Pis as cattle, not pets](https://blog.engineyard.com/2014/pets-vs-cattle), so I do crazy things to them on an hourly basis, and typically rewrite the microSD cards dozens of times trying new configurations, building new servers, etc. If you have anything important on your Pi, **overclocking the reader can cause data corruption**, especially for [non-UHS-certified](https://www.sdcard.org/consumers/speed/) cards. Make a backup! You've been warned!

Add a `dtoverlay` directive to overclock the microSD reader to 100 MHz (it defaults to 50):

`sudo bash -c 'printf "dtoverlay=sdhost,overclock_50=100\n" >> /boot/config.txt'`

Reboot the Raspberry Pi (`sudo reboot`), and you should experience much better disk I/O!

> Note: The above instructions work on the Raspberry Pi 2 and other models as well (assuming you use a valid [integer divisor](http://www.positiveintegers.org/252) of the core clock--on the Pi 2 you could try `84`, `72`, or `63` by default).

## Benchmarking microSD cards

There are a couple benchmark scripts you can run to test the speed and verify the updated microSD clock:

`# Installs and run hdparm, dd, and iozone benchmarks.  
$ curl https://raw.githubusercontent.com/geerlingguy/raspberry-pi-dramble/master/setup/benchmarks/microsd-benchmarks.sh | sudo bash  
  
# Run hdparm and some large file read/write benchmarks.  
$ curl http://www.nmacleod.com/public/sdbench.sh | sudo bash`

Here are a couple quick benchmarks comparing the same cards at normal clock and overclocked:

![Raspberry Pi 3 microSD card performance - overclock with sdhost](https://www.jeffgeerling.com/sites/jeffgeerling.com/files/images/microsd-card-performance-pi3-overclock-io-faster.png)

Random disk I/O performance has the highest impact on most day-to-day Pi usage (especially if you use it as a desktop computer!), so I tend to focus my benchmarking on it; large file operations (e.g. large file reads and writes) basically doubles with the 2x clock speed increase, so if you do things like copy giant files across the network or stream large video files, then the performance boost may be even _more_ noticable. 4K random _writes_ don't benefit as much, mostly because microSD cards typically max out at much lower speeds than would saturate the Pi's bus.

## Potential issues

If you notice the clock is not set at 100 MHz after changing these settings (both of the above benchmark scripts output the current clock setting before running the benchmarks), and you've confirmed the steps above were run correctly, there are two things that could be causing problems:

  * If your power supply can't supply at least 2.4A at a consistent 5V, then the Pi might not even boot, or might automatically under clock the SD reader.
  * If you run `dmesg` after bootup, see if there are any messages relating to `mmc0` and "reducing overclock"; the card might not be able to sustain a full 100 MHz overclock.

Sometimes a simple hard power off and power on will resolve these issues; other times it just means either your card, your Pi, or your power supply won't sustain the overclock setting reliably. You can try other, lower overclock settings, as long as the number is an [integer divisor](http://www.positiveintegers.org/400) of the core clock (default is 400 MHz on the Pi 3), e.g. `50`, `80`, or `100`.

Also, if you experience WiFi issues, or if your Raspbian version doesn't include the `sdhost` overlay inside `/boot/overlays`, you can download `sdtweak-overlay.dtb` manually: `sudo wget -O /boot/overlays/sdtweak-overlay.dtb https://dl.dropboxusercontent.com/u/1221084/share/Raspberry-Pi/sdtweak-overlay.dtb`; it's better to update/upgrade, though, so the sdhost overlay is present. You will also need to change 'sdtweak' to 'sdhost' in the overlay line in config.txt if you do this.

## More info

  * [Pi3 WiFi stopped working](https://www.raspberrypi.org/forums/viewtopic.php?p=928516#p928516) \- more info about the sdtweaks/sdhost/inclusion in Raspbian.
  * [microSD Card Benchmarks](http://www.pidramble.com/wiki/benchmarks/microsd-cards) \- exhaustive resource with all the tests I've run so far.
