# piwheels: making “pip install” fast

_Captured: 2017-11-09 at 13:05 from [www.raspberrypi.org](https://www.raspberrypi.org/blog/piwheels/)_

_TL;DR `pip install numpy` used to take ages, and now it's super fast thanks to piwheels.  
_

The [Python Package Index](https://pypi.python.org/pypi) (PyPI) is a package repository for Python modules. Members of the Python community publish software and libraries in it as an easy method of distribution. If you've ever used `pip install`, PyPI is the service that hosts the software you installed. You may have noticed that some installations can take a long time on the Raspberry Pi. That usually happens when modules have been implemented in C and require compilation.

![XKCD comic of two people sword-fighting on office chairs while their code is compiling](https://www.raspberrypi.org/app/uploads/2017/11/compiling.png)

> _No more slacking off! pip install numpy takes just a few seconds now \o/_

## Wheels for Python packages

A general solution to this problem exists: [Python wheels](http://pythonwheels.com/) are a standard for distributing pre-built versions of packages, saving users from having to build from source. However, when C code is compiled, it's compiled for a particular architecture, so package maintainers usually publish wheels for 32-bit and 64-bit Windows, macOS, and Linux. Although Raspberry Pi runs Linux, its architecture is ARM, so Linux wheels are not compatible.

![A comic of snakes biting their own tails to roll down a sand dune like wheels](https://www.raspberrypi.org/app/uploads/2017/11/desert-roller-snake.jpg)

> _What Python wheels are not_

Pip works by browsing PyPI for a wheel matching the user's architecture -- and if it doesn't find one, it falls back to the source distribution (usually a tarball or zip of the source code). Then the user has to build it themselves, which can take a long time, or may require certain dependencies. And if pip can't find a source distribution, the installation fails.

## Developing piwheels

In order to solve this problem, I decided to build wheels of every package on PyPI. I wrote some tooling for automating the process and used a postgres database to monitor the status of builds and log the output. Using a Pi 3 in my living room, I attempted to build wheels of the latest version of all 100 000 packages on PyPI and to host them on a web server on the Pi. This took a total of ten days, and my proof-of-concept seemed to show that it generally worked and was likely to be useful! You could install packages directly from the server, and installations were really fast.

![A Raspberry Pi 3 sitting atop a Pi 2 on cloth](https://www.raspberrypi.org/app/uploads/2017/11/IMG_20170921_123822-1-1440x1080.jpg)

> _This Pi 3 was the piwheels beta server, sitting atop my SSH gateway Pi 2 at home_

I proceeded to plan for version 2, which would attempt to build every version of every package -- about 750 000 versions in total. I estimated this would take 75 days for one Pi, but I intended to scale it up to use multiple Pis. Our web hosts Mythic Beasts provide dedicated Pi 3 hosting, so I fired up 20 of them to share the load. With some help from [Dave Jones](https://twitter.com/waveform80), who created an efficient queuing system for the builders, we were able make this run like clockwork. In under two weeks, it was complete! Read ALL about the [first build run drama](http://bennuttall.com/piwheels-building-a-faster-python-package-repository-for-raspberry-pi-users/) on my blog.

![A list of the mythic beasts cloud Pis](https://www.raspberrypi.org/app/uploads/2017/11/piwheels-mission-control.png)

> _ALL the cloud Pis_

## Improving piwheels

We analysed the failures, made some tweaks, installed some key dependencies, and ran the build again to raise our success rate from 76% to 83%. We also rebuilt packages for Python 3.5 (the new default in Raspbian Stretch). The wheels we build are tagged 'armv7l', but because our Raspbian image is compatible with all Pi models, they're really ARMv6, so they're compatible with Pi 3, Pi 2, Pi 1 and Pi Zero. This means the 'armv6l'-tagged wheels we provide are really just the ARMv7 wheels renamed.

![The piwheels monitor interface created by Dave Jones](https://www.raspberrypi.org/app/uploads/2017/11/piwheels-monitor.png)

> _The wonderful piwheels monitor interface created by Dave_

Now, you might be thinking "Why didn't you just cross-compile?" I really wanted to have full compatibility, and building natively on Pis seemed to be the best way to achieve that. I had easy access to the Pis, and it really didn't take all that long. Plus, you know, I wanted to [eat my own dog food](https://en.wikipedia.org/wiki/Eating_your_own_dog_food).

You might also be thinking "Why don't you just apt install python3-numpy?" It's true that some Python packages are distributed via the Raspbian/Debian archives too. However, if you're in a virtual environment, or you need a more recent version than the one packaged for Debian, you need pip.

![](https://www.raspberrypi.org/app/uploads/2017/11/piwheels-website.png)

## How it works

Now that the [piwheels package repository](https://www.piwheels.hostedpi.com/) is running as a service, hosted on a Pi 3 in the Mythic Beasts data centre in London. The pip package in Raspbian Stretch is configured to use piwheels as an additional index, so it falls back to PyPI if we're missing a package. Just run `sudo apt upgrade` to get the configuration change. You'll find that pip installs are much faster now! If you want to use piwheels on Raspbian Jessie, that's possible too -- find the instructions in our [FAQs](https://www.piwheels.hostedpi.com/faq.html). And now, every time you pip install something, your files come from a web server running on a Raspberry Pi (that capable little machine)!

Try it for yourself in a virtual environment:
    
    
    sudo apt install virtualenv python3-virtualenv -y
    virtualenv -p /usr/bin/python3 testpip
    source testpip/bin/activate
    pip install numpy

This takes about 20 minutes on a Pi 3, 2.5 hours on a Pi 1, or just** a few seconds** on either if you use piwheels.

If you're interested to see the details, try `pip install numpy -v` for verbose output. You'll see that pip discovers two indexes to search:
    
    
    2 location(s) to search for versions of numpy:
      * https://pypi.python.org/simple/numpy/
      * https://www.piwheels.hostedpi.com/simple/numpy/

Then it searches both indexes for available files. From this list of files, it determines the latest version available. Next it looks for a Python version and architecture match, and then opts for a wheel over a source distribution. If a new package or version is released, piwheels will automatically pick it up and add it to the build queue.

![A flowchart of how piwheels works](https://www.raspberrypi.org/app/uploads/2017/11/flowchart.png)

> _How piwheels works_

For the users unfamiliar with virtual environments I should mention that doing this isn't a requirement -- just an easy way of testing installations in a sandbox. Most pip usage will require `sudo pip3 install {package}`, which installs at a system level.

If you come across any issues with any packages from piwheels, please let us know in a [GitHub issue](https://github.com/bennuttall/piwheels/issues).

## Taking piwheels further

We currently provide over **670 000 wheels** for more than **96 000 packages**, all compiled natively on Raspberry Pi hardware. Moreover, we'll keep building new packages as they are released.

Note that, at present, we have built wheels for Python 3.4 and 3.5 -- we're planning to add support for Python 3.6 and 2.7. The fact that piwheels is currently missing Python 2 wheels does not affect users: until we rebuild for Python 2, PyPI will be used as normal, it'll just take longer than installing a Python 3 package for which we have a wheel. But remember, [Python 2 end-of-life](https://pythonclock.org/) is less than three years away!

Many thanks to [Dave Jones](https://twitter.com/waveform80) for his contributions to the project, and to [Mythic Beasts](https://www.mythic-beasts.com/) for providing the excellent [hosted Pi service](https://www.mythic-beasts.com/order/rpi).

![Screenshot of the mythic beasts Raspberry Pi 3 server service website](https://www.raspberrypi.org/app/uploads/2017/11/mythic-beasts-pi-hosting.png)

Related/unrelated, check out my poster from the [PyCon UK](http://2017.pyconuk.org/) poster session:

![A poster about Python and Raspberry Pi](https://www.raspberrypi.org/app/uploads/2017/11/PyCon-UK-Poster-A1-1529x1080.png)

Click to download the PDF!
