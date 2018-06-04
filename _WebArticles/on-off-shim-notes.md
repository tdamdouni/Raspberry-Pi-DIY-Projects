This is correct- the press-and-hold to shutdown is to prevent an accidental press from issuing a shutdown. When it’s off, there’s no software involved and it’s just triggering a latching circuit.

OnOff SHIM has a weak ~10Mohm onboard pull-up resistor to prevent the need for a long press. Otherwise without the shutdown pin connected it would be floating and potentially subject to random noise induced shutdowns.

You should be able to change your pin in the device tree overlay to an input with no pull, and allow it to be set up and asserted by the shutdown script only. I’m guessing it being set up as an output is what caused your problems - in retrospect I wasn’t paying as much attention to your overlay as I should have.

I’ve updated the Pinout.xyz documentation to reflect the need for 3.3v which, despite my disagreeing with myself, it actually does require.

It should be easy enough to add a power-down button but it wont be able to power the Pi back on again, since LiPo SHIM doesn’t have the facility for the Pi to cut power ( it doesn’t have the latching power switch that OnOff SHIM does ).

That sounds sensible enough, although you would have to adapt cleanshutdown to monitor both the LiPo SHIMs automatic shutdown pin and your button.

I’m actually working on a python replacement to this script at the moment, which might be easier to modify when it’s finished depending on what you’re more familiar with.

See work in progress here: https://github.com/pimoroni/clean-shutdown/blob/python/daemon/usr/bin/cleanshutd

On/Off SHIM could still function as an off button. With no ability to cut the power from the Zero Stem, though, you’re never going to get proper On/Off functionality, because it’s not possible to shut it completely off. You could possibly use a USB extension cable and splice the power wire with a switch to solve this, but that may be a little convoluted. If you’re plugging directly into a USB port, though, you’re somewhat out of luck.

On/Off SHIM works by using a latching power circuit that a pin toggle from the Pi can latch into the OFF state and completely cut power to the Pi.