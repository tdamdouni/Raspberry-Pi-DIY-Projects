_https://forums.pimoroni.com/t/lipi-shim-with-adafruit-lipo-charger/6166/2_

If you’re intending to try and charge while drawing power from the battery/charger then no- that would be unwise.

The charger relies on the behaviour of the battery throughout its charge cycle in order to regulate the input voltage. If you attach some other load in parallel with the LiPo then the charger at best wont be able to do its job properly and in the worst case may try to output voltages that could damage that load, the LiPo or both.

_https://forums.pimoroni.com/t/on-off-shim-with-zero-lipo/4892/2_

Zero LiPo will assert BCM 4 when the battery starts to run low- you can use this to trigger a soft shutdown, there's no need for OnOff SHIM.

OnOff SHIM is designed to cut the power from an external microUSB supply, and wouldn't bring much to the table in this case.

After soft-shutdown your Pi will fire up again when you reconnect your charged battery.

Our Clean Shutdown script supports Zero LiPo: https://github.com/pimoroni/clean-shutdown17

This is set up automatically when you install Zero LiPo via: curl https://get.pimoroni.com/zerolipo | bash

Since the "Low Battery" warning doesn't do anything more complicated than pull GPIO #4 low, you could wire a regular push button between GPIO #4 and Ground (conveniently located right next to each other). Pushing down that button would initiate exactly the same soft shutdown procedure as the low battery warning.
