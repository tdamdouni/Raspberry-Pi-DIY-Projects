#Explorer HAT Pro, Motors, Servos and Steppers

Find this Gist at: tiny.cc/explorerhat

The Motor driver on Explorer HAT Pro can not only drive motors, but a stepper motor too. And just like the Pibrella the outputs can also drive a motor or four, or another stepper.

Explorer HATs outputs sink to ground, meaning that you need to connect whatever you're driving between 5V and the output

#MOTORS

Driving a motor with Explorer HAT is easy, you just import the library:

```python
import explorerhat
```

Hook up a motor to channel 1 or 2, and tell it to go forward, backward or stop:

```python
explorerhat.motor.two.forward()
explorerhat.motor.two.backward()
explorerhat.motor.two.stop()
```

#STEPPERS

Steppers are a little trickier. We're using 28BYJ-48 steppers and they need a "step sequence" in order to function. It also helps to ramp up their speed from a slow sequence to a gradually faster one.

Connect the stepper as follows:

* Red Wire -> 5V
* Yellow Wire -> Output 1
* Orange Wire -> Output 2
* Pink Wire   -> Output 3
* Blue Wire   -> Output 4

The following code will now run through the step sequene and drive the stepper using Explorer HAT's outputs:

```python
 #!/usr/bin/env python

 import explorerhat, time

 sleep_time = 0.1
 min_sleep = 0.001

 step_sequence = [
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
  [1,0,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [0,1,0,1]
 ]

 while True:
     for step in step_sequence:
         for pin in range(4):
             explorerhat.output[pin].write(step[pin])
         time.sleep(sleep_time)
         if sleep_time > min_sleep:
             sleep_time /= 1.1
```


#SERVOS

Driving a servo or two is a little more complicated and requires the use of Pi-blaster: https://github.com/sarfata/pi-blaster

After following the install instructions and running pi-blaster as root, you can control a servo connected to GPIO 18 ( marked PWM on Explorer HAT ) by writing:

```bash
echo 18=0.2 > /dev/pi-blaster
```
In the terminal.

The file /dev/pi-blaster is a FIFO- it's a shared buffer that lets you send commands to pi-blaster from other programs.

To control servos from Python, you need to "open" this FIFO in Python and write commands to it, like so:

```python
servo = open('/dev/pi-blaster')
f.write('18=0.3\n')
f.flush()
```