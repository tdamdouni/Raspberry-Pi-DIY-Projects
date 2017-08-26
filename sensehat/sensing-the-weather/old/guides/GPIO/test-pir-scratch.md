## Test a PIR Montion Sensor in Scratch

Because we are using the GPIO pins, we need to run a special version of Scratch called 'Scratch GPIO 5'. Double-click this icon on the desktop to run it.

Scratch uses the 'Sensing' blocks to check if there is any input on the GPIO pins. If there is an input, the value of the pin changes from `0` to `1`. As you connected the PIR sensor to pin 7 of the Pi, we need to monitor that. 

- Click on the drop-down menu on the `sensor value` block and choose `pin7`.
- Tick the check-box to the left of the block to display the pin value on screen.

![Scratch sensing blocks](images/sensing-blocks.png)

Test the PIR sensor by waving your hand in front of it. When it detects movement, the value on the screen should change from `0` to `1`.

If the value doesn't change, check that the correct pins are connected.
