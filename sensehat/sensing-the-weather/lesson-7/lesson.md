#  Sensing the Weather - Relative Humidity Lesson

In this lesson students will learn how to take readings from the relative humidity and ambient temperature sensor, and use this data to find the dew point of the current environment.

## Sensor guide

Here is some background information about the [relative humidity sensor](../guides/relative_humidity.md).

## Learning objectives

- Be able to take temperature and relative humidity readings from the relative humidity sensor
- Be able to write code to solve a given equation for a chosen variable
- Be able to look up values in a dictionary and return a corresponding statement

## Cross-curricular applications

- Computer Science - dictionaries
- Geography - climate, humidity, heat index, saturation, water vapour
- Mathematics - solving equations for dew point

## Lesson summary

- What is relative humidity?
- What is the dew point?
- Use readings of relative humidity and temperature to calculate the dew point
- Look up this value using a dictionary and provide some advice about how this will feel to humans

## Starter

Discuss the concepts of relative humidity and the dew point, using the [further information about the sensor](../guides/relative_humidity.md). Before beginning the main part of the task, students should understand what they are trying to achieve with this program: they will calculate the dew point from the humidity and temperature values, and then use this to display a statement about how this will feel to humans, read from a dictionary.

## Main development

1. Students boot their Raspberry Pi Weather Station with the air quality sensor board attached.

1. Guide students through the basic code for gathering a relative humidity reading from the sensor. This is almost the same as the ambient temperature reading, except that we call a different method on the sensor object, so it should be very familiar.

1. Introduce the code for calculating the dew point. This is a "plug and play" equation for the students; the explanation of how it's calculated is outside the scope of this lesson. The formula is a version of the Magnus formula and it provides an *approximation* of the dew point.

	```python
	dew_point = ((humidity / 100) ** 0.125) * (112 + 0.9 * temp) + (0.1 * temp) – 112
	```
	[[Formula source](http://www.ajdesigner.com/phphumidity/dewpoint_equation_dewpoint_temperature.php#ajscroll)]

1. Students follow the [worksheet](worksheet.md) to calculate and print the dew point for the relative humidity and temperature levels in their current environment. The code for this is [here](code/calculate_dewpoint.py).

1. Introduce the concept of a dictionary and show students how to create one. Dictionaries have **keys** and corresponding **values**. Here is a dictionary of values taken from the [Wikipedia page](https://en.wikipedia.org/wiki/Dew_point) on dew points. The number represents a threshold temperature in degrees C, and the corresponding statement is the one which will be printed if the dew point temperature has exceeded that threshold.

	```python
	dew_description = { 0 : "A bit dry for some",
	                    12 : "Very comfortable",
	                    16 : "Comfortable",
	                    18 : "Upper edge of comfortable",
	                    21 : "Somewhat uncomfortable",
	                    24 : "Quite uncomfortable",
	                    26 : "Extremely uncomfortable",
	                    27 : "Severely high to deadly" }
	```

1. We can get a list of all of the **keys** from the dictionary with this line of code:

	```python
	thresholds = list( dew_description.keys() )
	thresholds.sort()
	```

The first line returns a list containing all of the numbers. We then call the `sort()` function because of the way that dictionaries store their data. Although when we typed in the values they were in numerical order, the dictionary uses a hash function to store and retrieve its data, so if you were to print out the `thresholds` list without calling the `sort()` function, you would see that the numbers were no longer in ascending order.

1. Students should iterate through the list and find the highest number exceeded by the dew point they calculated. For example, if the dew point is calculated as 17 degrees C then the threshold of 16 has been exceeded but the threshold of 18 has not been exceeded. The message displayed should be `"Comfortable"`.

	```python
	threshold_exceeded = 0

	# Loop through all thresholds and set threshold_exceeded to the highest exceeded
	for temp in thresholds:
	    if dewpoint >= temp:
	        threshold_exceeded = temp

	# Print out the corresponding message from the dictionary
	print( dew_description[threshold_exceeded] )
	```

1. The finished program is [here](code/calculate_dewpoint_message.py).


## Plenary

Ask the class the following questions:

1. What does a relative humidity measurement mean?
1. What is the dew point?
1. In what situations might it help people to know the relative humidity or the dew point temperature of their environment?

**Answers:**

1. The relative humidity is the amount of water vapour present in the air, expressed as a percentage of the total amount of vapour the air is capable of holding at the current temperature.
1. The dew point is the temperature at which the water vapour in the air will condense to form liquid dew.
1. There are many applications, ranging from keeping people healthy inside their homes to calculating the likelihood of condensing water forming ice and causing issues for a plane. Students could research some of these online.

## Extension

- Advanced students may be able to create a GUI with sliders or input boxes, so that the temperature and relative humidity values can be changed via the interface, and the resultant dew point is automatically recalculated as the values change.
