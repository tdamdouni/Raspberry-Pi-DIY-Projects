_http://forums.pimoroni.com/t/help-unicorn-hat-doesnt-turn-off-on-shutdown/3614/14_

yes, unless the EEPROM can be read (physical pin 27-28 are connected) then the library will assume you have a pHAT, so if select wiring you do indeed have to override unicornhat.AUTO

for future reference, if you ever want to run a script on shutdown that clears your Unicorn, on a systemd-based system such as Raspbian Jessie (including latest Retropie which is based on it), you can do it as follows:
create a script (its name does not matter, say clear-unicorn) with something like this:

```
#! /bin/sh

case "$1" in
    halt) sudo python -c 'import unicornhat; unicornhat.clear()';;
    poweroff) sudo python -c 'import unicornhat; unicornhat.clear()';;
    reboot) sudo python -c 'import unicornhat; unicornhat.clear()';;
esac
```

don't forget to chmod +x to make it executable, and then drop it in /lib/systemd/system-shutdown/

... from there on, every time the system goes for a poweroff (halt or reboot, though which options trigger the clear are down to you) the Unicorn will go off.