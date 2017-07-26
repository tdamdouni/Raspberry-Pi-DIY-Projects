# The Joystick

The Sense HAT joystick is mapped to the four keyboard cursor keys, with the joystick middle-click being mapped to the Return key. This means that moving the joystick has exactly the same effect as pressing those keys on the keyboard. Remember that the down direction is with the HDMI port facing downwards.

  ![](images/cursor_keys.jpg)
  
However, you can also access the movement of the joystick with a little Python code.

## Accessing the joystick events

To find out what each joystick event outputs, you can print the events to the shell. This bit of code will print out the direction that the joystick was pushed in, or the direction from which it was released.

```python
from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
```

In the trinket emulator, you can pretend to be moving the joystick using your keyboard's cursor keys.

<iframe src="https://trinket.io/embed/python/ee4e2a3edf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

You should see something like the following printed out, as you press the joystick in various directions.

```python
('up', 'pressed')
('up', 'released')
('down', 'pressed')
('down', 'released')
('left', 'pressed')
('left', 'released')
('right', 'pressed')
('right', 'released')
('middle', 'pressed')
('middle', 'released')
```

## Moving a pixel using the joystick

One example of how you could use this in a program would be to control a pixel on the LED matrix, moving it around and changing its colour, for instance.

You can start by setting the `x` and `y` coordinates for the pixel to be illuminated, providing a list of colours, and then providing a value for which colour in the list to use on the illuminated pixel.

```python
from sense_hat import SenseHat
sense = SenseHat()

x, y = 0, 0
colours = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]
colour = 0
```

Next, you can use the same code as before to detect joystick movements, but set a pixel each time the joystick is moved, instead of printing.

```python
while True:
	for event in sense.stick.get_events():
		sense.set_pixel(x, y, colours[colour])
```

The next stage is to detect when the joystick is pressed, and the direction it's pressed in, and change the `x` and `y` position of the pixel.

```python
while True:
	for event in sense.stick.get_events():
		sense.set_pixel(x, y, colours[colour])
		if event.action == 'pressed' and event.direction == 'up':
			y -= 1
		if event.action == 'pressed' and event.direction == 'down':
			y += 1
		if event.action == 'pressed' and event.direction == 'right':
			x += 1
		if event.action == 'pressed' and event.direction == 'left':
			x -= 1
```

You can try this out if you like, but there's a problem. If the pixel falls off the edge of the matrix, the program will produce an error, so this needs handling in the code.

```python
while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'up':
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            if x > 0:
                x -= 1
```

Lastly, if the joystick's direction is middle, you can change the `colour`. If the `colour` value is longer than the length of the `colours` list, then it needs to reset to `0`.

```python
while True:
    for event in sense.stick.get_events():
        sense.set_pixel(x, y, colours[colour])
        if event.action == 'pressed' and event.direction == 'up':
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            if x > 0:
                x -= 1
        if event.action == 'pressed' and event.direction == 'middle':
            colour += 1
            if colour == len(colours):
                colour = 0
```

<iframe src="https://trinket.io/embed/python/459fe4e4e1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

