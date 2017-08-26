# GPIO Pin Numbering

When programming the GPIO pins there are two different ways to refer to them: GPIO numbering and physical numbering. 

#### GPIO numbering

These are the GPIO pins as the computer sees them. The numbers don't make any sense to humans: they jump about all over the place, so there is no easy way to remember them. However, you can use a printed reference or a reference board that fits over the pins to help you out. 

#### Physical numbering

The other way to refer to the pins is by simply counting across and down from pin 1 at the top left (nearest to the SD card). This is 'physical numbering' and it looks like this:

![GPIO layout](images/physical-pin-numbers.png)

#### Which system should I use?

Beginners and young children may find the physical numbering system simpler, as you simply count the pins. You'll still need a diagram like the one above to know which are GPIO pins, which are ground and which are power though. 

Generally we recommend using the GPIO numbering. It's good practice and most resources use this system. Take your pick though: as long as you use the same system consitently within a program then all will be well. Note that what pin numbering system you choose can also depend on the programming language you are using: Scratch GPIO, for example, uses physical pin numbers. In Python, on the other hand, you can choose which system to use.

For more details on the advanced capabilities of the GPIO pins see Gadgetoid's [interactive pinout diagram](http://pi.gadgetoid.com/pinout).
