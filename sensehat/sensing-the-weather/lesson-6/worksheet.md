# Sensing the Weather - Ambient Temperature Worksheet

In this lesson you will:

- Write code to read information from the ambient temperature sensor
- Combine two programs together
- Produce a graph to display information from two sensor sources at once

## How does the ambient temperature sensor work?

![Ambient Temperature Sensor](images/air_board.png)

This sensor (circled in red on the photograph) can detect the ambient temperature of the air surrounding it.

Temperature sensors can detect changes in temperature and humidity because they are made of materials whose properties change depending on the temperature and the amount of water vapour present in the air.


## Reading from the ambient temperature sensor

You are already familiar with using code written by other people to access information from sensors, as we have used this to gather data from both the wind vane and the soil temperature sensor. Here's the basic code to gather information from the ambient temperature sensor, using a library called `HTU21D` which we will refer to with the name `temp_humid`:

```python
import HTU21D as temp_humid

ambient_temp = temp_humid.HTU21D()

current_temp = ambient_temp.read_temperature()
print( str(current_temp) + " degrees Celsius")
```

### Questions

Inspect this code with a partner and answer the following:

- What is `ambient_temp`?
- Which method are we calling on the object to get the temperature reading?
- What units is the temperature given in?

### Answers

- `ambient_temp` is the name of an object we have created to be able to talk to the sensor.
- We call the `read_temperature()` method on the object to get the temperature reading.
- The temperature is given in degrees C.

## Combining the programs

Now that you know how to take a reading from both the ambient temperature sensor and the soil temperature sensor, your challenge is to make a graph with *two* lines, showing the readings from both sensors at once.

1. Save a copy of your soil temperature program as `two_temperature_sensors.py` (or you could start with our [finished code](../lesson-5/code/soil_fancy_graph.py)).

1. Your two lists of values in this code were called `x` and `y`. However, we now want to plot *two* things on the y axis, so change the name of the list `y` to `soil_temp`, then create a new blank list called `amb_temp` where we will store the ambient temperature values.

1. Using the code above for reading from the ambient temperature sensor, alter your program to take a reading from the ambient temperature sensor *as well as* the soil temperature sensor every 5 seconds. Don't forget to set up your sensor before the loop, and take the reading inside the loop.

1. To plot more than one line on your graph, you need to change your plot code slightly:

	```python
	plt.plot(x, soil_temp, 'r', label="Soil Temperature")
	```

	This code will plot `x` (the time values) against `soil_temp`; this is the data from the soil temperature sensor. `'r'` means that the line will be red (can you experiment with other colours?) and `label="Soil Temperature"` gives this line a label which we can use to display a legend. Add this code *instead of* `plt.plot(x,y)`.

1. Add another line of code to plot the data from the ambient temperature sensor in a different colour.

1. Finally, let's display a legend and tell it where to position itself. Make sure that this is before the final line in your code to `show()` the graph you have created.

	```python
	plt.legend(loc="lower right")
	```
1. If you would like to make your y-axis start at zero, you can use the code `plt.ylim(ymin=0)` just before the line of code to display the graph.

1. Run your code and test whether it works. For testing purposes, you can change the temperature readings by holding the soil temperature sensor in your hand to warm it up, or by blowing gently into one of the holes in the air quality sensor board plastic housing.

1. Now run the experiment; run your program but don't alter the temperature of the sensors. Do they record the same temperature?

The [finished code](code/two_temperature_sensors.py) is here so that you can check your code.

## Summary

- You have combined two different programs into one, demonstrating your understanding of how the code works.
- Are the readings from the different sensors the same? If not, discuss possible reasons why there might be differences in the readings from the different sensors.

## What next

- Can you apply your skills to independently create a graph of data gathered from the anemometer?
