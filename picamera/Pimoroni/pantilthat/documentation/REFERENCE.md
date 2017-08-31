# PanTilt HAT Function Reference

First import pantilthat:

```python
import pantilthat
```

The HAT will automatically be set up for you with some defaults.

## Servos

You can move a servo by giving it an angle between -90 and 90:

```python
pantilthat.servo_one(45)
pantilthat.servo_two(-73)
```

If you've got a datasheet for your servos, you can calibrate the min/max pulses
in microseconds for servos 1 and 2 like so:

```python
pantilthat.servo_pulse_min(1, 1000)
pantilthat.servo_pulse_max(1, 2000)
pantilthat.servo_pulse_min(2, 1000)
pantilthat.servo_pulse_max(2, 2000)
```

If you want to turn the servos off to save battery power for example, you can:

```python
pantilthat.servo_enable(1, False)
pantilthat.servo_enable(2, False)
```

## Lights

PanTilt HAT supports either up to 24 WS2812 LEDs, or a ring/strand of PWM-dimmable LEDs:
IE the kind of lighting ring you'd get to power and control directly from the Pi.

To pick lighting mode:

```python
pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_mode(pantilthat.PWM)
```

### PWM

PWM controlled LEDs have only brightness control from 0 to 255:

```python
pantilthat.brightness(255)
```

### WS2812

With WS2812 LEDs connected (A NeoPixel ring, for example) you can set the colour of each LED:

```python
pantilthat.set_pixel(0, 255, 0, 255)
```

The arguments are: index, from 0 to 23, followed by amount of red, green and blue which range from 0 to 255.

Once you've set the colours you want, you must send the pixel data to PanTilt HAT with:

```python
pantilthat.show()
```
