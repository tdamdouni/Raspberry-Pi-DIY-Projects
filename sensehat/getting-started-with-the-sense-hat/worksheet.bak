# Getting Started with the Sense Hat

The Sense HAT is an add-on board for the Raspberry Pi, made especially for the [Astro Pi](http://astro-pi.org/) competition. The board adds the ability to sense all kinds of things and output information using a built-in 8x8 LED matrix. You can find out more about what the Sense HAT can do by following the [Astro Pi Guide](https://www.raspberrypi.org/learning/astro-pi-guide/), which will show you how to connect and test your Sense HAT. It also has some helpful explanations and examples of what the different inputs and outputs can do.

Once you are set up and have run your first program using the guide, you can begin to experiment further using this worksheet.

## Displaying text

Start by opening Python3 from the main menu.

When following the [guide](https://www.raspberrypi.org/learning/astro-pi-guide/) you will have written a sample program which scrolls text across the LED matrix. The program contains two crucial lines, which import the Sense HAT software and create a `sense` object which represents the Sense HAT.

```python
from sense_hat import SenseHat

sense = SenseHat()
```

The third line is the one that makes the Sense HAT do something:

```python
sense.show_message("Hello my name is Tim Peake")
```

<iframe src="https://trinket.io/embed/python/308a373b5c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

You have probably already discovered that you can easily change the message to your own text, but there are more things that we can do.

1. We can expand the `sense.show_message` command to include some extra **parameters** which will change the behaviour of the message.

    | Parameter | Effect |
    | --- | --- |
    | **scroll_speed** | The *scroll_speed* parameter affects how quickly the text moves on the screen. The default value is 0.1. The bigger the number, the **slower** the speed |
    | **text_colour** | The *text_colour* parameter alters the colour of the text and is specified using 3 values for Red, Green, Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |
    | **back_colour** | The *back_colour* parameter alters the colour of the background and works in the same way as the *text_colour* |

    So this program would display the text `Astro Pi is awesome!!` more slowly, with the text in yellow **[255,255,0]** and the background in blue **[0,0,255]**:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.show_message("Astro Pi is awesome!!", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
    ```

    You could also make the message repeat using a while loop like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    while True:
        sense.show_message("Astro Pi is awesome!!", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`loop_text.py`](code/loop_text.py), then press **F5** to run.

1. The LED matrix can also display a single character, rather than an entire message, using the `sense.show_letter` function which also has some optional **parameters**.

    | Parameter | Effect |
    | --- | --- |
    | **scroll_speed** | The *scroll_speed* parameter affects how quickly the text moves on the screen. The default value is 0.1. The bigger the number, the **slower** the speed |
    | **text_colour** | The *text_colour* parameter alters the colour of the text and is specified as 3 values for Red, Green, Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |
    | **back_colour** | The *back_colour* parameter alters the colour of the background and is specified as 3 values for Red, Green, Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |

    So this program would display a single Red "J":

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.show_letter("J",text_colour=[255, 0, 0])
    ```

    And this program would add the **sleep function** to display letters separated by a brief pause:

    ```python
    from sense_hat import SenseHat
    import time

    sense = SenseHat()

    sense.show_letter("O",text_colour=[255, 0, 0])
    time.sleep(1)
    sense.show_letter("M",text_colour=[0, 0, 255])
    time.sleep(1)
    sense.show_letter("G",text_colour=[0, 255, 0])
    time.sleep(1)
    sense.show_letter("!",text_colour=[0, 0, 0], back_colour=[255, 255, 255])
    time.sleep(1)
    sense.clear()
    ```

    Click **File** -- **Save As**, give your program a name eg [`omg.py`](code/omg.py), then press **F5** to run.

    For added interest you could use a random number generator to choose a number between 0 and 255 for the colours:

    ```python
    from sense_hat import SenseHat
    import time
    import random

    sense = SenseHat()

    r = random.randint(0,255)
    sense.show_letter("O",text_colour=[r, 0, 0])
    time.sleep(1)

    r = random.randint(0,255)
    sense.show_letter("M",text_colour=[0, 0, r])
    time.sleep(1)

    r = random.randint(0,255)
    sense.show_letter("G",text_colour=[0, r, 0])
    time.sleep(1)

    sense.show_letter("!", text_colour=[0, 0, 0], back_colour=[255, 255, 255])
    time.sleep(1)
    sense.clear()
    ```

1. Click **File** -- **Save As**, give your program a name eg [`random_omg.py`](code/random_omg.py), then press **F5** to run.

    In both these programs the `sense.clear()` method has been used at the end to clear the matrix.

### Ideas

 - Could you use the ideas used so far to tell a joke via the LED screen?
 - All the examples so far could be made shorter, while still achieving the same thing. Can you find ways to make these shorter and more efficient?
 - How would you choose a totally random colour, rather than just a random shade of a colour?
 - If your Sense HAT is connected to the internet you could use a Twitter library to make it display incoming tweets!

## Displaying images

The LED matrix can display more than just text! We can control each LED individually to create an image. We can accomplish this in a couple of ways.

1. The first approach is to set pixels (LEDs) individually; we can do this using the `sense.set_pixel()` method. First, we need to be clear about how we describe each pixel.

    The Sense HAT uses a coordinate system like the one shown below; crucially the numbering begins at **0**, not 1. Also, the origin is in the **top left** rather than the bottom left as you may be used to.

    ![Coordinates](images/coordinates.png)

    - the blue pixel is at coordinates (0, 2)
    - the red pixel is at coordinates (7, 4)

    To replicate the above diagram you would enter a program like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.set_pixel(0, 2, [0, 0, 255])
    sense.set_pixel(7, 4, [255, 0, 0])
    ```

    Can you guess what the following code creates?

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.set_pixel(2, 2, [0, 0, 255])
    sense.set_pixel(4, 2, [0, 0, 255])
    sense.set_pixel(3, 4, [100, 0, 0])
    sense.set_pixel(1, 5, [255, 0, 0])
    sense.set_pixel(2, 6, [255, 0, 0])
    sense.set_pixel(3, 6, [255, 0, 0])
    sense.set_pixel(4, 6, [255, 0, 0])
    sense.set_pixel(5, 5, [255, 0, 0])
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`simple_image.py`](code/simple_image.py), then press **F5** to run.

1. Setting pixels individually can work brilliantly, but it gets rather complex when you want to set more pixels. There is another method which can set all the pixels in one go called `sense.set_pixels`. Its use is quite straightforward; we just give a list of colour values for each pixel in the matrix.

    We could enter something like...

    ```python
    sense.set_pixels([[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0],......])
    ```

    ...but this would take ages and be really complex.

    Instead, you can use some variables to define your colour palette (in this example we're using the 7 colours of the rainbow):

    ```python
    r = [255, 0, 0]
    o = [255, 127, 0]
    y = [255, 255, 0]
    g = [0, 255, 0]
    b = [0, 0, 255]
    i = [75, 0, 130]
    v = [159, 0, 255]
    e = [0, 0, 0]  # e stands for empty/black
    ```

    We can then describe our matrix by creating a 2D list of colour names:

    ```python
    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,r,r,o,o,r,r,e,
    r,o,o,y,y,o,o,r,
    o,y,y,g,g,y,y,o,
    y,g,g,b,b,g,g,y,
    b,b,b,i,i,b,b,b,
    b,i,i,v,v,i,i,b
    ]
    ```

    We then give the `image` list to the `sense.set_pixels` method and draw the image. The finished program would look like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    r = [255,0,0]
    o = [255,127,0]
    y = [255,255,0]
    g = [0,255,0]
    b = [0,0,255]
    i = [75,0,130]
    v = [159,0,255]
    e = [0,0,0]

    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,r,r,o,o,r,r,e,
    r,o,o,y,y,o,o,r,
    o,y,y,g,g,y,y,o,
    y,g,g,b,b,g,g,y,
    b,b,b,i,i,b,b,b,
    b,i,i,v,v,i,i,b
    ]

    sense.set_pixels(image)
    ```
1. Click **File** -- **Save As**, give your program a name e.g. [`rainbow.py`](code/rainbow.py), then press **F5** to run.

    You should have a beautiful rainbow displayed on your LED matrix.

### Ideas

- Now you can create images on your LED matrix in two different ways, try creating your own images or sprites.
- Can you alternate between images to create an animation? Check out this [Geek Gurl Diaries](https://www.youtube.com/watch?v=b84EywkQ3HI) video for some inspiration.

## Setting orientation

So far, all our text and images have appeared the same way up, assuming that the HDMI port is at the bottom. However, this may not always be the case (especially in space) so you may want to change the orientation of the matrix. To do this, you can use the `sense.set_rotation()` method and inside the brackets enter one of four angles (0, 90, 180, 270).

To rotate your screen by 180 degrees you'd use this line:

```python
sense.set_rotation(180)
```

1. When used in the rainbow program it would look like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    r = [255, 0, 0]
    o = [255, 127, 0]
    y = [255, 255, 0]
    g = [0, 255, 0]
    b = [0, 0, 255]
    i = [75, 0, 130]
    v = [159, 0, 255]
    e = [0, 0, 0]

    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,r,r,o,o,r,r,e,
    r,o,o,y,y,o,o,r,
    o,y,y,g,g,y,y,o,
    y,g,g,b,b,g,g,y,
    b,b,b,i,i,b,b,b,
    b,i,i,v,v,i,i,b
    ]

    sense.set_pixels(image)
    sense.set_rotation(180)
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`rainbow_flip.py`](code/rainbow_flip.py), then press **F5** to run.

2. You could also create spinning text using a **for** loop:

    ```python
    from sense_hat import SenseHat
    import time

    sense = SenseHat()

    sense.show_letter("J")

    angles = [0, 90, 180, 270, 0, 90, 180, 270]
    for r in angles:
        sense.set_rotation(r)
        time.sleep(0.5)
    ```

    This program displays the letter "J" and then sets the rotation to each value in the angles list with a 0.5 second pause.

1. Click **File** -- **Save As**, give your program a name e.g. [`spinning_j.py`](code/spinning_j.py), then press **F5** to run.

1. You can also flip the image on the screen, either horizontally or vertically, using these lines:

    ```python
    sense.flip_h()
    ```

    or

    ```python
    sense.flip_v()
    ```

    With this example you could create a simple animation by flipping the image repeatedly:

    ```python
    from sense_hat import SenseHat
    import time

    sense = SenseHat()

    w = [150, 150, 150]
    b = [0, 0, 255]
    e = [0, 0, 0]

    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    w,w,b,e,e,w,w,b,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

    sense.set_pixels(image)

    while True:
        time.sleep(1)
        sense.flip_h()
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`eyes.py`](code/eyes.py), then press **F5** to run.

### Ideas

- Create a spinning image, using one of the drawing techniques shown already, and then use the `sense.set_rotation` method to make it spin.
- Using what you've done so far, you should be able to make an electronic dice like the one shown here:

[![Sense HAT Dice](https://img.youtube.com/vi/4jT7GyyudP4/0.jpg)](https://www.youtube.com/watch?v=4jT7GyyudP4)

This dice makes use of:

- Displaying text
- Timing
- Setting rotation
- Random numbers
- Variables

## Sensing the environment

The Sense HAT has a set of environmental sensors for detecting the conditions around it. It can detect:

- Pressure
- Temperature
- Humidity

We can collect these readings using three simple methods:

- `sense.get_temperature()` - This will return the temperature in Celsius.
- `sense.get_pressure()` - This will return the pressure in millibars.
- `sense.get_humidity()` - This will return the humidity as a percentage.

1. Using these, we could create a simple scrolling text display which could keep people informed about current conditions.

    ```python
    from sense_hat import SenseHat
    sense = SenseHat()

    while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t,p,h)

        sense.show_message(msg, scroll_speed=0.05)
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`env.py`](code/env.py), then press **F5** to run.

1. You could now use some colour to let the astronauts know whether conditions are within sensible ranges.

    According to some [online documentation](http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf), the International Space Station maintains these conditions at the following levels:

    - Temperature (18.3 - 26.7 Celsius)
    - Pressure (979 - 1027 millibars)
    - Humidity (around 60%)

    You could use an `if` statement in your code to check these conditions, and set a background colour for the scroll:

    ```python
    if t > 18.3 and t < 26.7:
        bg = [0, 100, 0] # green
    else:
        bg = [100, 0, 0] # red
    ```

    Your complete program would look like this:

    ```python
    from sense_hat import SenseHat
    sense = SenseHat()

    while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        if t > 18.3 and t < 26.7:
            bg = [0, 100, 0]  # green
        else:
            bg = [100, 0, 0]  # red

        msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t, p, h)

        sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`scrolling_env.py`](code/scrolling_env.py), then press **F5** to run.

### Ideas

- Currently, the scrolling program only warns about abnormal temperature. Can you add the same behaviour for pressure and humidity?
- You could create a simple graphical thermometer which outputs different colours / patterns depending on the temperature.
- If you haven't done so already, experiment with a bottle and the [pressure sensor](https://www.raspberrypi.org/learning/astro-pi-guide/sensors/pressure.md).

## Detecting movement

The Sense HAT has a set of sensors that can detect movement. It has an IMU (inertial measurement unit) chip which includes:

- A gyroscope (for detecting which way up the board is)
- An accelerometer (for detecting movement)
- A magnetometer (for detecting magnetic fields)

Before you start experimenting with motion sensing, it's important to understand three key terms covered in the [guide](https://github.com/raspberrypilearning/astro-pi-guide/blob/master/sensors/movement.md) and in this [video](https://www.youtube.com/watch?v=pQ24NtnaLl8).

The three axes uses to describe motion are:

- Pitch (like a plane taking off)
- Roll (the plane doing a victory roll)
- Yaw (imagine steering the plane like a car)

![Sense HAT Orientation](images/orientation.png)

You can find out the orientation of the Sense HAT using the `sense.get_orientation()` method:

```python
orientation = sense.get_orientation()
pitch = orientation['pitch']
roll = orientation['roll']
yaw = orientation['yaw']
```

This would get the three orientation values (measured in degrees) and store them as the three variables `pitch`, `roll` and `yaw`.

1. You can explore these values with a simple program:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    while True:
	    orientation = sense.get_orientation()
		pitch = orientation['pitch']
		roll = orientation['roll']
		yaw = orientation['yaw']
        print("pitch=%s, roll=%s, yaw=%s" % (pitch,yaw,roll))
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`orientation.py`](code/orientation.py), then press **F5** to run.

    **Note: When using the movement sensors it is important to poll them often in a tight loop. If you poll them too slowly, for example with `time.sleep(0.5)` in your loop, you will see strange results. This is because the code behind needs lots of measurements in order to successfully combine the data coming from the gyroscope, accelerometer and magnetometer.**

1. Another way to detect orientation is to use the `sense.get_accelerometer_raw()` method which tells you the amount of g-force acting on each axis. If any axis has ±1g then you know that axis is pointing downwards.

    In this example, the amount of gravitational acceleration for each axis (x, y, and z) is extracted and is then rounded to the nearest whole number:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    while True:
	    acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']

        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)

        print("x=%s, y=%s, z=%s" % (x, y, z))
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`acceleration.py`](code/acceleration.py), then press **F5** to run.

    As you turn the screen you should see the values for x and y change between -1 and 1. If you place the Pi flat or turn it upside down, the z axis will be 1 and then -1.

1. If we know which way round the Raspberry Pi is, then we can use that information to set the orientation of the LED matrix. First you would display something on the matrix, then continually check which way round the board is, and use that to update the orientation of the display.

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.show_letter("J")

    while True:
        x = sense.get_accelerometer_raw().['x']
		y = sense.get_accelerometer_raw().['y']
		z = sense.get_accelerometer_raw().['z']

        x = round(x, 0)
        y = round(y, 0)

        if x == -1:
            sense.set_rotation(180)
        elif y == 1:
            sense.set_rotation(90)
        elif y == -1:
            sense.set_rotation(270)
        else:
            sense.set_rotation(0)
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`rotating_letter.py`](code/rotating_letter.py), then press **F5** to run.

    In this program you are using an `if, elif, else` structure to check which way round the Raspberry Pi is. The `if` and `elif` test three of the orientations, and if the orientation doesn't match any of these then the program assumes it is the "right" way round. By using the `else` statement we also catch all those other situations, like when the board is at 45 degrees or sitting level.

1. If the board is only rotated, it will only experience 1g of acceleration in any direction; if we were to shake it, the sensor would experience more than 1g. We could then detect that rapid motion and respond. For this program we will introduce the `abs()` function which is not specific to the Sense HAT library and is part of standard Python. `abs()` gives us the size of a value and ignores whether the value is positive or negative. This is helpful as we don't care which direction the sensor is being shaken, just that it is shaken.

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    while True:
	    acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            sense.show_letter("!", text_colour=[255, 0, 0])
        else:
            sense.clear()
    ```

1. Click **File** -- **Save As**, give your program a name e.g. [`shake.py`](code/shake.py), then press **F5** to run.

    You might find this is quite sensitive, but you could change the value from 1 to a higher number.

### Ideas

  - You could write a program that displays an arrow (or other symbol) on screen; this symbol could be used to point to which way is down. This way the astronauts (in low gravity) always know where the Earth is.
  - You could improve the dice program from earlier in this activity, so that shaking the Pi triggers the dice roll.
  - You could use the accelerometer to sense small movements; this could form part of a game, alarm system or even an earthquake sensor.

## Putting it all together

Now that you've explored most of the features of the Sense HAT, you could combine them to create a project. Here's an example reaction testing game, which could be used by the astronauts to test their reflexes.

The game will display an arrow on the LED matrix and select a random orientation for it. The player must rotate the board to match the arrow. If they match it in time the arrow turns green and their score increases; if not their arrow turns red and the game ends, telling them their score. The game keeps showing arrows in new orientations until the player loses, and each turn gets faster.

This idea combines:

  - Showing messages and images on the LED matrix
  - Setting and detecting the orientation
  - Use of variables, randomisation, iteration, and selection

As this is more complicated than previous programs it's worth planning out the steps involved in **pseudocode**.

  > import the required libraries (sense_hat, time, random)  
  > create a sense object
  >
  > Set up the colours needed  
  > Create 3 different arrows (white, green, red)  
  > Set a variable **pause** to 3 (the initial time between turns)  
  > Set variables **score** and **angle** to 0  
  > Create a variable called **play** set to `True` (this will be used to stop the game later)  
  >  
  > Begin a loop which continues while `play == True`  
  > Set a new random angle (use **random.choice()** method)  
  > Show the white arrow and sleep for current pause length  
  > Check whether orientation matches the arrow  
  > ---if it does then add a point and turn the arrow green  
  > ---otherwise set play to `False` and turn the arrow red  
  > Shorten the pause duration slightly  
  > Pause before the next arrow  
  >  
  > When loop is exited, display a message with the score  

If you turned this into Python it could look like this:

```python
from sense_hat import SenseHat
import time
import random

sense = SenseHat()

# set up the colours (white, green, red, empty)

w = [150, 150, 150]
g = [0, 255, 0]
r = [255, 0, 0]
e = [0, 0, 0]

# create images for three different coloured arrows

arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

arrow_red = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

pause = 3
score = 0
angle = 0
play = True

sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

while play:
    last_angle = angle
    while angle == last_angle:
        angle = random.choice([0, 90, 180, 270])
    sense.set_rotation(angle)
    sense.set_pixels(arrow)
    time.sleep(pause)
	acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']
        
    x = round(x, 0)
    y = round(y, 0)

    print(angle)
    print(x)
    print(y)

    if x == -1 and angle == 180:
        sense.set_pixels(arrow_green)
        score += 1
    elif x == 1 and angle == 0:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == -1 and angle == 90:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == 1 and angle == 270:
      sense.set_pixels(arrow_green)
      score += 1
    else:
      sense.set_pixels(arrow_red)
      play = False

    pause = pause * 0.95
    time.sleep(0.5)

msg = "Your score was %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])
```

1. Click **File** -- **Save As**, give your program a name e.g. [`reaction_game.py`](code/reaction_game.py), then press **F5** to run.

Here's a video showing it being demonstrated:

[![Sense HAT Dice](https://img.youtube.com/vi/k1ZB8jORb74/0.jpg)](https://www.youtube.com/watch?v=k1ZB8jORb74)

### Ideas

There are lots of potential developments for this game:
- Include shake actions as well as orientation.
- Make use of the humidity sensor to detect breath; the player could be prompted to breathe on the board as an action.
- Include more than 4 directions; players have to hold at 45 degrees.

## What next?

- Now that you have explored the basics of the Sense HAT, you might investigate the Python library itself to see some other functions it offers.
- Try out the 3D Soyuz Demo which allows you to use the Sense HAT to move a virtual 3D model. Why not try creating your own models with [Sketchup](http://www.sketchup.com/) or [Blender](https://www.blender.org/)?
- Link the the Sense HAT sensor data with [minecraft-pi](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/).
