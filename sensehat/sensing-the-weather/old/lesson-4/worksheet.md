# Weather Station Basic I/O - Measuring wind speed

In this lesson you will:

- Simulate an anemometer and collect data using the Raspberry Pi GPIO pins
- Use interrupt handling to detect inputs from the sensor
- Use simple circle theory to convert the collected data into meaningful measurement information

## How does the anemometer work?

Today you will be using the anemometer sensor to collect data about windspeed. The sensor has three arms with buckets on the end which "catch" the wind, causing the arms to spin. If you were to dismantle the sensor you would find a small magnet attached to the underside.

![](images/anemometer_with_magnet.png)

At two points within the magnet's rotation, it triggers a reed switch which produces a `LOW` signal we can detect. So for each full rotation of the arms, the sensor will produce two detectable signals.

![](images/anemometer_reed.png)

So let's start collecting data from the sensor!

## Getting Setup

In order to get started we need to setup the anemometer or simulate it, depending on the situation.

### You have a weather station and anemometer to yourself

Connect the weather station board and anemometer using the [guide](../guides/weather_station/anemometer.md)

### You don't have a weather station and anemometer to yourself

In most classroom situations you won't have a anemometer, or at least one to yourself, in which case you can simulate one using a pair of wires and a button.

1. Follow the [button guide](../guides/GPIO/connecting-button.md) to connect your wires up in a similar way to the previous lesson, except this time connect to pin 5.

    ![](images/gpio-setup.png)

1. Now you can simulate the anemometer by pressing the button.

## Detecting anemometer interrupts

Before we begin calculating windspeed we need to be able to count the signals coming from the anemometer. To do this we can reuse some of our code from last lesson.

1. Setup your Raspberry Pi and ensure you are in desktop mode.

1. Launch the LXterminal window

    ![LX Terminal](images/lxterminal.png)

1. Move to the `weather station` directory by typing `cd weather_station` and pressing `enter`

1. Copy our previous program to a new file called `wind_interrupt.py` using the command `cp rain_interrupt.py wind_interrupt.py` followed by `enter`.

1. Open you program by typing `sudo idle3 wind_interrupt.py`

The code will currently look a little like this:

    ```python
    #!/usr/bin/python3
    import RPi.GPIO as GPIO

    pin = 6
    count = 0

    def bucket_tipped(channel):
        global count
        count = count + 1
        print (count * 0.2794)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

        input("Press enter to stop logging\n")
    ```

1. The anemometer is connected to pin **5**, so update the code to reflect this.

1. Rename the `bucket_tipped` function to something meaningful like `spin`. *This will need to be done in two places*.

1. The anemometer doesn't require a bouncetime to be set, so remove the option from the event declaration by deleting the `bouncetime=300`.

1. Change the `print` statement to just print out the `count` variable.

1. Test your code! Press **F5** and save when prompted

Your code should display the number of half rotations counted. Press `Ctrl + C` to stop the program. If it doesn't work as expected, check your code against this [solution](code/wind_interrupt.py).

We can now count the signals from the anemometer; next we need to calculate the wind speed.

## Calculating wind speed

We can count the number of rotations of the sensor by doubling the detected inputs. But how do we change that into a speed?

1. Let's start by considering the formula for calculating [speed](http://www.bbc.co.uk/education/guides/zwwmxnb/revision):


    **Speed = distance / time**

  Imagine we counted the number of signals over the course of 5 seconds. We now have the time but we also need the distance traveled.

1. The distance traveled by one of the cups will be equal to the number of revolutions * the distance around the edge of the circle (circumference). So we could write:


    **Speed = Revolutions * Circumference / Time**

1. The circumference can be calculated if we know either the **radius** or **diameter** of the circle.

    ![](images/pi_diagram.png)

We can measure the radius of the circle made by the anemometer by measuring the distance from the centre to the edge. Knowing the radius, we can find the circumference with **2 x pi x r**. We also know that the revolutions are half the number of signals detected, so our formula becomes:


    **Speed = (Signals/2) * (2 * pi * r) / Time**

This formula should enable us to calulate the speed of the wind in cm/s.

## Updating the code

Now that we are able to calculate the wind speed from the information we can collect, we need to add the code to make this work.

1. Measure the radius (in cm) of the anemometer for use in your program.
1. Decide on the time interval for calculating average windspeed, at least 5 seconds.
1. Copy your existing code by clicking **File** --> **Save As** and calling it `wind_calc.py`

1. Adapt your code using the following solution as a guide:

    > import GPIO, time, math  
    > pin 5  
    > count = 0  
    >
    > FUNCTION spin (channel)  
    > --- increment global count variable  
    > --- display count  
    >
    > FUNCTION calcspeed  
    > --- using r = **???**, your time interval, count and math.pi  
    > --- calculate windspeed  
    > --- return windspeed  
    >
    > Set up GPIO and interrupt which has spin as its callback function.  
    >
    > INFINITE LOOP  
    > --- reset global count to 0  
    > --- wait **delay** sec  
    > --- call calcspeed to get value  
    > --- display windspeed value  

- The first three lines set up the different variables and required libraries.
- The **spin** function is called every time an interrupt is detected, adds 1 to the count variable and prints it.
- The **calcspeed** function uses all the right information to calculate the wind speed and returns it.
- The next line sets up the GPIO callback function for pin 5 and sets the function to spin.
- The final loop is set to wait for a time period before calculating the speed, printing it and then starting again.

Can you convert this program plan to a working Python program? (A solution can be found [here](code/wind_calc.py))

## Measurement units

Currently, the program we have created will measure the wind speed in **cm** per **second**, however this is not particularly useful. A more practical unit would be **km** per **hour**. In order to convert our units we will need to:

1. Convert cm -> km by **dividing** by the number of cm in 1km
1. Convert seconds -> hours by **multiplying** by the number of seconds in 1 hour

Adapt your code so that it displays the windspeed in km/h.

## Calibration

Our program should now display the wind speed in km/h, but is it accurate? The [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf) says that if it rotates once a second that should equate to 2.4 km/h. So in the example interval of 5 seconds, 5 spins (10 signals) should equal the same 2.4 km/h.

1. Run your program and spin the anemometer 5 times within the first 5 seconds. What wind speed value is reported?

  ```bash
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  2.03575203953 kph
  ```

  That's not quite right! This loss of accuracy is due to something called the *anemometer factor* and is a result of some of the wind energy being lost in turning the arms. To compensate for this, we are going to have to multiply the reading generated by our program by a factor of **1.18** which should correct this error. Update the final line in the `calculate_speed` function to read:

  ```python
  return km_per_hour * 1.18
  ```

  Your final code should now look something like [this](code/wind_final.py).

1. Re-run the code and this time you should get a value closer to 2.4:

    ```
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    2.40218740664 kph
    ```

## What's next?

Now that you have a working anemometer program there are some other things you could do:

- Test your anemometer with a wind source such as a fan to ensure it works consistently.
- This device measures wind speed, so what kind of location would be most suitable for this device? What factors should be considered? Height, isolation, proximity to buildings? Where in your school or site would be the best place for it?
- In this lesson we have used interrupts to manage the data coming from the sensor. Can you write a program that uses continuous polling?
