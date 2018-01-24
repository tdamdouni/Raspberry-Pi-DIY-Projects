# Read-Only Raspberry Pi

_Captured: 2017-11-10 at 19:00 from [learn.adafruit.com](https://learn.adafruit.com/read-only-raspberry-pi?view=all)_

Most microcontroller projects have an on/off switch or some quick way to cut power, while computers like the Raspberry Pi require an **orderly shutdown** procedure…otherwise the SD card may become **corrupted** and the system will no longer boot.

Sometimes just cutting power would be a convenient timesaver, or a system may be left to non-technical users. For installations that don't require creating or modifying files -- such as a dedicated slideshow kiosk -- we can configure the operating system to make it **more resistant to unplanned power cuts**.

Linux -- or any substantial computer operating system, Windows and Mac are the same way -- behind the scenes they're reading and writing all manner of temporary data to drives (or the SD card with Raspberry Pi). This is why we normally use the **shutdown** command: all those files are put away in a known valid state. But if power is unexpectedly cut, these lingering half-written files can render a card **unbootable**…one can try patching it up, but sometimes there's no recourse but to **wipe the card and reinstall everything**.

The script we provide here adapts Raspbian to work in a _**read-only**_ mode. Temporary files are stored in RAM rather than on the SD card, making it more robust in this regard. You can just unplug the system when done. The tradeoff…as the _read-only_ name implies…is that **nothing can be written to the card** in this state. Can't install software, can't record pictures. So it's _not_ the solution to every situation, but may be helpful with certain passive tasks…a [slideshow kiosk](https://learn.adafruit.com/../../../raspberry-pi-video-looper), a [Fadecandy](https://learn.adafruit.com/../../../1500-neopixel-led-curtain-with-raspberry-pi-fadecandy) server, a [Halloween display](https://learn.adafruit.com/../../../animated-snake-eyes-bonnet-for-raspberry-pi), etc.

Optionally, you can use a jumper or switch to boot the system into normal read/write mode to install new software or data. And, as normal, you still have easy access to the /boot partition if the SD card is mounted on another computer.

**This guide is based partly on instructions from [petr.io](http://petr.io/en/blog/2015/11/09/read-only-raspberry-pi-with-jessie/), which in turn credits [Charles Hallard](http://hallard.me/raspberry-pi-read-only/) and [Mario Hros](http://k3a.me/how-to-make-raspberrypi-truly-read-only-reliable-and-trouble-free/)…along with community members' contributions in those threads and some changes and additions of our own.**

  * This **does not work** with the **X11** desktop / PIXEL. It's strictly for **Raspbian Lite **right now. Graphical applications are still possible using SDL, Pygame and so forth, just not X11 at the moment.
  * Setting up read-only mode should be the **_very last step_** before deploying a project. Get all your code and data on the system, get software auto-starting as needed, test it normally with the usual boot and shutdown methodology. It's easier up-front. Once you're 100% confident in its operation, _then_ use the script.
  * **Back up** the contents of your SD card first. We've tested on a couple versions of Raspbian, but maybe something's changed, or has been overlooked, and could leave the Pi in a weird intermediate state, or the script might break compatibility with some other software.
  * No really, **back up your stuff**.

Pi should be booted and on the network…like mentioned above, everything already configured and fully functional (and backed up) before taking this step.

**THIS SEQUENCE IS IRREVERSIBLE. We don't have an uninstall script. There's an _option_ to boot into read/write mode, but _nothing_ to back out _all_ these changes.**

From a command line prompt:

The script will repeat all these stern warnings and make you verify at several steps whether to continue. Along the way you'll be presented with a few options:

**Enable boot-time read/write jumper? [y/N]**

This gives you the option to run the system in read/write mode by inserting a jumper across two pins…

  * ![raspberry_pi_gpio-map.png](https://cdn-learn.adafruit.com/assets/assets/000/046/746/medium640/raspberry_pi_gpio-map.png?1506536092)

  * ![raspberry_pi_gpio-map.png](https://cdn-learn.adafruit.com/assets/assets/000/046/746/thumb160/raspberry_pi_gpio-map.png?1506536092)

  * ![raspberry_pi_jumper.jpg](https://cdn-learn.adafruit.com/assets/assets/000/046/751/thumb160/raspberry_pi_jumper.jpg?1506537108)

**Install GPIO-halt utility? [y/N]**

This installs a utility that initiates a proper shutdown when another GPIO pin is touched to ground.

For a read-only system, **you probably don't need this**…but I'm a little paranoid…or, if you have the system booted in read/write mode, this provides an option if you can't log in and run a manual shutdown.

  * ![raspberry_pi_button.jpg](https://cdn-learn.adafruit.com/assets/assets/000/046/754/medium640/raspberry_pi_button.jpg?1506538137)

**Enable kernel panic watchdog? [y/N]**

This option enables software to automatically reboot the system in the event of a kernel panic (a low-level system crash). This is actually pretty rare though, and is not the only way in which programs may crash on the system. You might want to set up your code to auto-restart using **systemd**, but that's a whole book in itself.

_(The selections here are based on comments in the previously-mentioned blog posts…but in practice the impression I'm getting is that it may be related more to the OS version than the specific hardware. This option might change or be removed in the future.)_

One last confirmation before the script runs. It may take 5 to 10 minutes, depending on the processor, network and SD card speed. You'll see a few warnings along the way, these can be ignored.

**Test** the modified system to make sure that the system boots and your application runs as intended. Try a pass with the read/write jumper and/or the gpio-halt button, if you've enabled either of those options.

**Now make an image of the SD card** (using _dd_ or _Apple Pi Baker_ or whatever your backup tool of preference) and, if it's a critical application, **burn _at least_ one spare**. There are other ways cards can go bad…static, brown-outs, falling out and getting lost…this read-only setup won't always save you. SD cards are cheap now! Spares help if you've left a system in someone else's care (let's say a museum kiosk) and it fails for some reason, you can ask them to just swap out the card until you can get there to troubleshoot. I know at least one Burning Man project rendered useless _in the first few minutes_ of the event because their one and only card fell out and was lost on the playa.
