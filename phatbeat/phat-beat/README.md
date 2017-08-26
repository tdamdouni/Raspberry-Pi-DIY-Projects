![pHAT BEAT](phat-beat-logo.png)
https://shop.pimoroni.com/products/phat-beat

Stereo amplifier, buttons and dual RGB VU meter for your Pi.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your pHAT BEAT
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/phatbeat | bash
```

Alternatively, on Raspbian, you can download the `pimoroni-dashboard` and install your product by browsing to the relevant entry:

```bash
sudo apt-get install pimoroni
```
(you will find the Dashboard under 'Accessories' too, in the Pi menu - or just run `pimoroni-dashboard` at the command line)

If you choose to download examples you'll find them in `/home/pi/Pimoroni/phatbeat/`.

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-phatbeat
```

other environments: 

```bash
sudo pip3 install phatbeat
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-phatbeat
```

other environments: 

```bash
sudo pip2 install phatbeat
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/phat-beat
* Function reference - http://docs.pimoroni.com/phatbeat/
* GPIO Pinout - https://pinout.xyz/pinout/phat_beat
* Get help - http://forums.pimoroni.com/c/support

## Third Party Libraries

* Node JS - https://github.com/eminentspoon/phatbeat-node
