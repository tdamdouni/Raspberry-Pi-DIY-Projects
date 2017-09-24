# Passive infrared motion sensor (PIR)

Humans and other animals emit radiation all the time. This is nothing to be concerned about, though, as the type of radiation we emit is infrared radiation (IR), which is pretty harmless at the levels at which it is emitted by humans. In fact, all objects at temperatures above absolute zero (-273.15C) emit infrared radiation.

A PIR sensor detects changes in the amount of infrared radiation it receives. When there is a significant change in the amount of infrared radiation it detects, then a pulse is triggered. This means that a PIR sensor can detect when a human (or any animal) moves in front of it.

![pir](images/pir_module.png)

## Wiring a PIR sensor

The pulse emitted when a PIR detects motion needs to be amplified, and so it needs to be powered. There are three pins on the PIR: they should be labelled **Vcc**, **Gnd**, and **Out**. These labels are sometimes concealed beneath the Fresnel lens (the white cap), which you can temporarily remove to see the pin labels.

![wiring](images/pir_wiring.png)

1. As shown above, the **Vcc** pin needs to be attached to a **5V** pin on the Raspberry Pi.
1. The **Gnd** pin on the PIR sensor can be attached to **any** ground pin on the Raspberry Pi.
1. Lastly, the **Out** pin needs to be connected to **any** of the GPIO pins.

## Tuning a PIR

Most PIR sensors have two potentiometers on them. These can control the sensitivity of the sensors, and also the period of time for which the PIR will signal when motion is detected.

![pir pots](images/pir_pots.jpg)

In the image above, the potentiometer on the right controls the sensitivity, and the potentiometer on the left controls the timeout. Here, both are turned fully anti-clockwise, meaning that the sensitivity and timeout are at their lowest.

When the timeout is turned fully anti-clockwise, the PIR will output a signal for about 2.5 seconds, whenever motion is detected. If the potentiometer is turned fully clockwise, the output signal will last for around 250 seconds. When tuning the sensitivity, it is best to have the timeout set as low as possible.

## Detecting motion

You can detect motion with the PIR using the code below:

```python
from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("You moved")
	pir.wait_for_no_motion()
```

## What Next?

- Now you know how to use a PIR, why not have a go at building a [Parent Detector](https://www.raspberrypi.org/learning/parent-detector)?
- Continue to the next worksheet on using an [Ultrasonic Distance Sensor](distance.md).
