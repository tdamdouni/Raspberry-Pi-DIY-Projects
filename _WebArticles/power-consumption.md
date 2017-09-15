# Power Consumption

_Captured: 2017-09-03 at 13:03 from [www.pidramble.com](http://www.pidramble.com/wiki/benchmarks/power-consumption)_

I use the [PowerJive USB Power Meter](https://www.amazon.com/PowerJive-Voltage-Multimeter-chargers-capacity/dp/B013FANC9W/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=mmjjg-20&linkId=6232aca4c54c95cd7dd29bcedea70e2f) to measure power consumption with the Dramble and individual Raspberry Pis, in all cases with nothing plugged into USB (unless otherwise noted). I will be adding power consumption statistics to this page as time goes on.

There are a few different ways you can reduce power consumption on the Pi (any model):

  * Disable HDMI
  * Disable onboard LEDs
  * Minimize accessories

See this post for more information and instructions how to do all of the above: [Conserve Raspberry Pis power consumption](http://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy).

## Raspberry Pi 3 Baseline

Pi State Power Consumption

Idle
260 mA (1.4W)

`ab -n 100 -c 10` (uncached)
480 mA (2.4W)

400% CPU load (`stress --cpu 4`)
730 mA (3.7W)

## Raspberry Pi 2 Baseline

Pi State Power Consumption

Idle
220 mA (1.1W)

`ab -n 100 -c 10` (uncached)
450 mA (~2.3W)

400% CPU load (`stress --cpu 4`)
400 mA (~2.1W)

## Raspberry Pi 2 with external USB 3.0 SSD

Pi State Power Consumption

Powering on, 1x USB 64GB SSD
900-1400 mA (~4.5W)

Idle, 1x USB 64GB SSD
960 mA (~4.8W)

`ab -n 100 -c 10` (uncached), 1x USB 64GB SSD
1100 mA (~5.5W)

400% CPU load, 1x USB 64GB SSD
1250 mA (~6.25W)

## Other Raspberry Pi models

For the below power tests, stock Rasbpian Lite was installed, and the measurement was taken after the Pi had been running idle for 1 minute, with nothing connected except onboard or USB WiFi as noted.

Pi Model Pi State Power Consumption

model 3 B
HDMI off, LEDs off
230 mA (1.2W)

model 3 B
HDMI off, LEDs off, onboard WiFi
250 mA (1.2W)

model 2 B
HDMI off, LEDs off
200 mA (1.0W)

model 2 B
HDMI off, LEDs off, USB WiFi
240 mA (1.2W)

Zero
HDMI off, LED off
80 mA (0.4W)

Zero
HDMI off, LED off, USB WiFi
120 mA (0.7W)

B+
HDMI off, LEDs off
180 mA (0.9W)

B+
HDMI off, LEDs off, USB WiFi
220 mA (1.1W)

A+
HDMI off, LEDs off
80 mA (0.4W)

A+
HDMI off, LEDs off, USB WiFi
160 mA (0.8W)

Also, as a point of reference, when you power off a Raspberry Pi (any model), it typically uses 20-30 mA (0.1W) until you physically disconnect the power.
