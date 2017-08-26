#  Sensing the Weather - Barometric Pressure Lesson

In this lesson students will learn how to take readings from the barometric pressure sensor and to record this data in CSV format for processing in another application.

## Sensor guide

Here is some background information about the [barometric pressure sensor](../guides/barometric_pressure.md).

## Learning objectives

- Be able to take a reading from the barometric pressure sensor
- Understand what pressure is and the units it's measured in
- Be able to store data in CSV format and access it from other applications

## Cross-curricular applications

- Computer Science - writing to CSV, loops, concatenation, date and time functions
- Mathematics - rearranging equations
- Physics - mass, weight, pressure, newtons, pascals

## Lesson summary

- Talk about what pressure is and how it's measured
- Introduce the barometric pressure sensor and write code to take a reading
- Students write code to read values from the sensor and write them to a CSV file

## Starter

Students may not be aware that air has a weight; introduce this concept and ask them how much they think a 1cm square cross section of air from sea level to the top level of the atmosphere would weigh. (The answer is approximately 10.1 newtons, and the mass of the air is approximately 1.03kg.)

People often confuse mass with weight, largely because the activity involving scales that we describe as "weighing" should more accurately be described as "finding the mass"! Pressure is a measure of the *weight* (the force) relative to the *area* over which it is spread. There is a [BBC Bitesize](http://www.bbc.co.uk/education/guides/zssbgk7/revision) article you could use as a refresher.

The unit of pressure the Weather Station sensor measures in is called the **pascal** and it has the symbol Pa.

1Pa = 1 N/m<sup>2</sup>

## Main development

1. Students boot their Raspberry Pi Weather Station and log in.

1. In order to read from the pressure sensor, the Adafruit BMP library must be installed. Open a terminal window and type in the following command to install the software:

	```bash
	sudo pip3 install adafruit-bmp
	```

1. Here is some basic Python code which reads the current value from the barometric pressure sensor:

	```python
	import Adafruit_BMP.BMP085 as bmp

	bmpsensor = bmp.BMP085()

	print('Pressure = '+ str(bmpsensor.read_pressure()) + "Pa")
	```

1. Students type in the code and check that they can successfully take a reading. They will then follow the [worksheet](worksheet.md) instructions to take multiple readings and store these in a CSV file.

1. You may wish to ask students to use the data collected for analysis with another program.


## Plenary

Ask the class the following question:

What could cause the pressure value measured by the barometric pressure sensor to change?

**Answers:**

Given that we know that pressure is the force exerted by the air over a given area:

**pressure = force / area**

...it follows that for the pressure to increase, the force will have to increase over the same area; either that or the size of the area will decrease, but that seems pretty unlikely!

So, another way to phrase this question could be "what factors could cause the force (weight) of the air above the measurement point to change?".

The first answer is **altitude**. If we were to move our Weather Station to a higher altitude (higher above sea level), the pressure would decrease because the mass of the overlying air decreases.

Secondly, barometric pressure is used to predict the weather conditions. You may have heard weather reports talking about high or low pressure; there is an explanation on the [Met Office website](http://www.metoffice.gov.uk/learning/learn-about-the-weather/how-weather-works/highs-and-lows/pressure). Areas of low pressure are caused by air warming and ascending, and high pressure is caused when the air cools and descends. Low pressure results in changeable weather, whereas high pressure results in settled weather conditions. Whether the weather is likely to change or not is sometimes measured at home using a device called a barometer.


## Extension

- Using the data you have gathered from the barometric pressure sensor, import the CSV file into another application and use that application to analyse the data. Perhaps you could import into Excel or Google Sheets and draw a graph of the pressure readings over time?
