# Raspberry Pi ON/OFF Power Controller Power up your Raspberry Pi with a latching push-button controlled MOSFET switch

_Captured: 2017-09-01 at 19:28 from [www.mosaic-industries.com](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/raspberry-pi/on-off-power-controller)_

It would be convenient to use a momentary contact push button switch to turn ON and turn OFF your Raspberry Pi (RPi). A press of a button should apply power to the micro USB header, and keep it ON while the Raspberry Pi initializes and starts its application programs. There should be several options for powering OFF the Raspberry Pi:

  * The RPi should be able to turn itself OFF fully autonomously, under program control, automatically on an internal timer, or in response to a network signal. 
  * You should be able to initiate a turn OFF sequence by momentarily pressing an OFF button. The Raspberry Pi should then shut-down its application program in an orderly way, and turn itself OFF. 
  * If the RPi fails to turn itself OFF or crashes, you should be able to press the button longer to force it OFF. 

A soft power switch with this behavior can be implemented using a high-side latching MOSFET power switch. The latching and toggle ON/OFF power switch circuit for controlling microcontrollers shown [here](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/electronic-circuits/push-button-switch-turn-on/microcontroller-latching-on-off) is easily adapted for controlling a Raspberry Pi in this manner. Here's the electronic circuit to use:

![Latching power switch circuit for the Raspberry Pi](http://www.mosaic-industries.com/embedded-systems/_media/microcontroller-projects/raspberry-pi/raspberry-pi-on-off-circuit.png)

> _Push button ON/OFF latching MOSFET power switch circuit for the Raspberry Pi_

The schematic shows you two options[1)](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/raspberry-pi/on-off-power-controller) for applying the switched 5V power to your Raspberry Pi. You can apply it through the micro USB connector, in which case it passes through a PolySwitch™ resettable fuse (rated at 1.1 A)[2)](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/raspberry-pi/on-off-power-controller) before being applied to the rest of the RPi circuitry, or, you can apply it to header `P1`, in which case it bypasses the fuse. The advantage of applying power to P1 and bypassing the fuse is that the 5V is then passed on to the USB connectors unimpeded, where it can drive high current USB devices.[3)](http://www.mosaic-industries.com/embedded-systems/microcontroller-projects/raspberry-pi/on-off-power-controller)

Whichever pins you choose for applying the 5V to the board, you should use the GPIO 4 signal on P1 pin 7 for feedback to the circuit. The Raspberry Pi is then able to shut itself OFF by driving that pin low.

The power controller conveniently uses two MOSFETs packaged together, the [IRF7319](http://www.mosaic-industries.com/embedded-systems/_media/microcontroller-projects/electronic-circuits/irf7319pbf-datasheet-hexfet-power-dual-mosfet.pdf), which allows you to build a very small circuit.
