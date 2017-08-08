# Laser tripwire with a photocell and breadboard

_Captured: 2017-05-18 at 00:26 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/laser-tripwire-lrd-photocell/)_

Learn how to use a Raspberry Pi with a LDR: light-dependent resistor by making a laser tripwire

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/laser-tripwire.jpg)

> _This laser tripwire project is a great introduction to digital making with a Raspberry Pi and breadboard circuit._

The Raspberry Pi can easily detect a digital input via its GPIO pins: any input that's approximately below 1.8V is considered off, and anything above 1.8V is considered on.

An analogue input can have a range of voltages from 0V up to 3.3V, however, and the Raspberry Pi is unable to detect exactly what that voltage is. One way of getting around this is by using a capacitor, and timing how long it takes to charge up above 1.8V.

By placing a capacitor in series with a light-dependent resistor (LDR), the capacitor will charge at different speeds depending on whether it is light or dark. We can use this to create a laser tripwire!

**This article was written by Phil King and appears in The MagPi 57. Download your [free copy of the magazine here](http://magpi.cc/2pNsUVP).**

You'll need:

  * GPIO Zero
  * 1× solderless breadboard
  * 1× light-dependent resistor (LDR)
  * 1× 1μF capacitor
  * 1× laser pointer
  * 5× male-to-female jumper wires
  * 5× female-to-female jumper wires (optional)
  * 1× drinking straw
  * 1× plastic box

### Build a Laser Tripwire circuit

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/laser-tripwire-breadboard.png)

An LDR (also known as a photocell) is a special type of electrical resistor whose resistance is very high when it's dark, but reduced when light is shining on it. With the Raspberry Pi turned off, place your LDR into the breadboard, then add the capacitor.

It's essential to get the correct polarity for the latter component: its longer (positive) leg should be in the same breadboard column as one leg of the LDR. Now connect this column (with a leg of both components) to GPIO 4. Connect the other leg of the LDR to a 3V3 pin, and the other leg of the capacitor to a GND pin. Your circuit should now resemble the diagram above.

### Test the LDR circuit

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/ch8-caption1.jpg)

On the Pi, open IDLE from the Main Menu: Menu Programming Python 3 (IDLE). Create a new file by clicking File New File, enter the code from ch8listing1.py, then save it. At the start, we import the LightSensor class from GPIO Zero.  
We then assign the variable ldr to the LDR input on the GPIO 4 pin. Finally, we use a never-ending while True: loop to continually display the current value of the light sensed by the LDR, which ranges from 0 to 1. Try running the code and then shining your laser pointer on it to vary the light level.

### Enclose the LDR

Unless you're working in a darkened room, you'll probably notice little difference between the measured light level when the laser pointer is directed onto the LDR and when it's not. This can be fixed by reducing the amount of light that the LDR receives from other light sources in the room, which will be essential for our laser tripwire device to work effectively. We'll achieve this by cutting off a short section - between 2cm and 5cm - of an opaque drinking straw, and inserting the head of the LDR into one end. Now try the test code again and see how the measured light level changes when you shine the laser pointer into the other end of the straw. You should notice a larger difference in values.

### Wire up the buzzer

To create an audible alarm for our laser tripwire, we'll add a piezo buzzer to the circuit. Again, the polarity has to be correct: connect the column of the buzzer's longer leg to GPIO 17, and the shorter leg to a GND pin. Let's test whether it is working. In IDLE, create a new file, enter the code from ch8listing2.py, and save it. At the top, we import the Buzzer class from GPIO Zero. Next, we assign the buzzer variable to the buzzer output on GPIO 17. Finally, we use  
buzzer.beep to make the buzzer turn on and off repeatedly at the default length of one second. To stop it, close the Python shell window while it is off.

### Test the tripwire

We'll now put it all together so that laser pointer shines at the LDR through the straw, and whenever the beam is broken, the buzzer sounds the alarm. In IDLE, create a new file, enter the code from ch8listing 3.py, and save it. At the start, we import the Buzzer and LightSensor classes from GPIO Zero. We also import the sleep function from time; we'll need this to slow the script down a little to give the capacitor time to charge. As before, we assign variables for the buzzer and LDR to the respective devices on GPIO pins 4 and 17. We then use a while True: loop to continually check the light level on the LDR; if it falls below 0.5, we make the buzzer beep. You can change this number to adjust the sensitivity; a higher value will make it more sensitive. Try running the code. If you break the laser beam, the buzzer should beep for eight seconds. You can adjust this by altering the buzzer.beep parameters and sleep time.

### Package it up

Once everything is working well, you can enclose your Raspberry Pi and breadboard in a plastic box (such as an old ice cream tub), with the drinking straw poking through a hole in the side. If you prefer, you can remove the breadboard and instead connect the circuit up directly by poking the legs of the components into female-to-female jumper wires, with the long capacitor leg and an LDR leg together in one wire end, connected to the relevant pins. Place the tub near a doorway, and place the laser pointer on the other side, with its beam shining into the straw. Run your code and try walking through the doorway: the alarm should go off!
