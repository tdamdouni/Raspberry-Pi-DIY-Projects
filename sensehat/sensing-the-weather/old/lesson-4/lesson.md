#  Weather Station Basic I/O - Lesson Plan 4

In this lesson, students will use the weather station expansion board and the anemometer (or simulate it). Students will learn how the anemometer works, use Python code to detect its rotation, and calculate the wind speed using a mathematical formula.

## Learning objectives

- Understand how the anemometer works by triggering electrical signals each rotation
- Count the signals produced by the anemometer and understand this data
- Convert this raw signal into meaningful information about the wind speed

## Learning outcomes

### All students are able to

- Explain how the anemometer works
- Write code with support to count the number of rotations made

### Most students are able to

- Write code to count the number of rotations made
- Use circle theory to convert the rotations made into a wind speed
- With support, present the wind speed in a meaningful unit

### Some students are able to

- Write code to gather anemometer data and calculate wind speed, and present this information in a suitable unit of measurement

## Lesson Summary

- Examine the anemometer and discuss its purpose, how it works and its unit of measurement
- Review understanding of circle theory
- Discuss an algorithm for the anemometer program
- Students code and test the anemometer program
- Students calibrate their sensor to ensure accuracy

## Starter

### How does the anemometer work?

Examine the anemometer sensor and discuss with pupils how it works and measures windspeed. Review the [Anemometer Guide](../guides/weather_station/anemometer.md) for more detailed information. Ask students what they think it does and how they think it works. Open it up and explore the sensor, reed switch and magnet as a group. Once you have explored how the sensor works as a group you should connect it up to a Raspberry Pi in order to demonstrate later in the lesson.

### Circle theory

Depending on time and ability of the class you may also want to recap some basic circle theory, including how to find the circumference of a circle. The [BBC Bitesize guide](http://www.bbc.co.uk/education/guides/z34xsbk/revision/2) has an explanation of the key formulae the students need and some questions to practice with. Students could be given a few questions where they find the circumference of a circle given the radius or diameter.

## Main development

1. Ask students to set up their Raspberry Pi equipment and connect the weather station board and anemometer using the [guide](../guides/weather_station/anemometer.md), turn it on and log into their Pi using the username `pi` and the password `raspberry`. In most classroom situations you might not have an anemometer for every student, in which case you can simulate one using a pair of wires and a button. Follow the [button guide](../guides/GPIO/connecting-button.md) to connect wires up in a similar way to the previous lesson, except this time connect to `pin 5`. Students will be able to simulate the anemometer by pressing the connected button.

1. Before calculating windspeed students will need to be able to count the signals coming from the anemometer. Display the code from the previous lesson:

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

    *Note: The anemometer is connected to pin **5**, so update the code to reflect this.*
    
    Demonstrate to students how to adapt the code by renaming the `bucket_tipped` function to something meaningful like `spin`. *This will need to be done in two places*. The anemometer doesn't require a bouncetime to be set, so remove the option from the event declaration by deleting the `bouncetime=300`. Then change the `print` statement to just print out the `count` variable. Allow students time to adapt and test their code using the [student worksheet](worksheet.md). The code should display the number of half rotations counted. Press `Ctrl + C` to stop the program. If it doesn't work as expected, check code against this [solution](code/wind_interrupt.py). 

1. Discuss with students how they will turn the count of signals received from the sensor into a wind speed. Share or co-devise with pupils an outline of code in a pseudocode style which students can refer to. (example in [guide](../guides/weather_station/anemometer.md)) Students should then implement the planned code in Python and test.

## Plenary

Ask the class the following questions:

1. Why could we not use a pull down circuit to detect the anemometer spinning?
1. Why is calibration important?
1. Have we done enough to calibrate the anemometer?

**Answers:**

1. The weather expansion board has fixed circuitry that we cannot change. The rain gauge has two wires; one is hardwired to GPIO 17 and the other is hardwired to ground, which means we can only short GPIO 17 to ground. If we used a pull down on GPIO 17 we would be shorting ground to ground and this would not produce a detectable change in the `HIGH` or `LOW` state of GPIO 17 when the anemometer spins. It would only ever read `LOW`.
1. Because we want to be confident that our measurements are correct, or are at least within an acceptable tolerance.
1. We know that the higher the wind speed, the less accurate the anemometer becomes. In order to compensate for this, we would need different calibration ratios for different speeds. With the information provided by the datasheet we have done as much as we can.

## Extension

- Students could test their anemometer with a fan or other wind source to ensure consistency.
- Students have used interrupts this lesson to collect inputs from the anemometer. Could they write a program to use continuous polling instead?
- Students could begin to think about the deployment of the weather station. Where would be an ideal location for the sensors? What factors might affect that decision?
