# Sensing the Weather - Barometric Pressure Worksheet

In this lesson you will:

- Be able to take a reading from the barometric pressure sensor
- Understand what pressure is and the units it's measured in
- Be able to store data in CSV format and access it from other applications

## How does the barometric pressure sensor work?

Here is the barometric pressure sensor supplied with the Raspberry Pi Weather Station kit as part of the air quality sensor board:

![Barometric pressure sensor](images/pressure_sensor.png)

Our barometric pressure sensor measures pressure in pascals (Pa). One pascal is equal to one newton per square metre.

1Pa = 1N/m<sup>2</sup>


## Taking a reading

1. Make sure that the Adafruit BMP library is installed on your Weather Station; ask your teacher how to do this if necessary. Here is the code to read the current pressure value from the sensor in Pa. Start a new Python file, type or paste in the code below, and check you get a reading from the sensor:

	```python
	import Adafruit_BMP.BMP085 as bmp

	bmpsensor = bmp.BMP085()

	print('Pressure = '+ str(bmpsensor.read_pressure()) + "Pa")
	```

## Changes in barometric pressure over time

### Question

Will the pressure value measured by the barometric pressure sensor change over time?

### Answer

Yes, but do you know *why*?

We're going to take a series of readings from the barometric pressure sensor at intervals over time, and record these readings, along with the time and date they were taken, in a format called a CSV file. A CSV file is simply a text file where data are stored, with commas in between them to separate them out. An example of data stored in CSV file might look like this:

```
25/06/16, 14:30, 10345
```

1. Start a new Python file and save it as `bmp_over_time.py`.

1. Start off your file with the lines of code to import the Adafruit BMP library and set up a sensor object, just as you did when testing the sensor:

	```python
	import Adafruit_BMP.BMP085 as bmp

	bmpsensor = bmp.BMP085()
	```

1. We'll need to calculate the time and date that a reading was taken, so that we can store this in the CSV file along with each reading. To do this we will use the Python library called `time`, and specifically the function called `strftime`. Add this line of code next to your other `import` statement to import this function into your program:

	```python
	from time import strftime
	```

1. The `strftime` function is really useful because it generates a time and/or date in whatever format you specify. For example, to generate the current date in the format dd/mm/yy you would use the following code:

	```python
	current_date = strftime("%d/%m/%y")
	```

	Add some code to generate the current date in a format you would like. If you wish, you can change the format (e.g. if you would like to use the US date format). You can use the [Python documentation](https://docs.python.org/2/library/time.html#time.strftime) for `strftime` to find out which other options are available.

1. Now add some more code to generate the current time in a format of your choice, and save it in a new variable called `current_time`.

1. Now add a final variable called `current_pressure` and generate a pressure reading from the sensor. Use the code from the previous section to help you with this.

If you want to check your code so far, it should look something like [this](code/bmp_over_time_part_way.py).


## Saving data to a CSV file

1. We need to save these values to a CSV file, which is basically just a text file where we write the data in a special format. Type in this code at the end of your program to open a file in Python:

	```python
	f = open("bmp_readings.csv", "a")
	```

The first value in the brackets tells Python the name of the file to open (Python will create this file if it doesn't exist). The second part tells Python which mode to open the file in:

	* "r" - read mode, to read contents from the file
	* "w" - write mode, to erase the whole file and write new data into it
	* "a" - append mode, to move to the end of the existing data in the file and write new data

1. Now we will write our data to the file. When we opened the file we created a **file pointer** called `f` which points to where our file is stored in memory. We use this file pointer to access the file and write data into it, like this:

	```python
	f.write("Data")
	```

Add this line of code to your program.

1. Finally, it's important to close the file at the end of the program, so add the following line of code:

	```python
	f.close()
	```

1. Run your program and check that a file called `bmp_readings.csv` is created in the same folder as your code, and that it contains the word "Data". If it has worked, delete the word "Data" from the file and save it as a blank file, as we don't want this test data as one of the barometric pressure readings!

1. To write data in CSV format, we simply add commas between the values. Here we have started creating a string to write to the file, to show you how to add the commas:

	```python
	string_to_write = str(current_date) + ", " +
	```

Find the place in your program where you open the file and after that line, type in the line of code above. Finish off the line of code by adding in the `current_time` and `current_pressure` data, converted to a string and separated by a comma. At the end of the line, add the newline character `"\n"` to tell the file to start the next piece of data on a new line.

1. Now alter the line which currently reads `f.write("Data")` to write the variable `string_to_write` to the file, instead of the string "Data". Check that your data writes correctly to the file.

## Automating the readings

You already know how to automate things happening at an interval. This code is from the lesson on [air quality](../lesson-8/worksheet.md).

```python
while True:
	count = 0
	sleep(interval)
	print( calc_speed(interval), "kph")
	print("Gust speed " + str(check_for_gusts() + "kph")
```

Can you alter this code to make your program write a line to the CSV file every 30 minutes? Don't forget that you'll need to take new readings *within* the loop, otherwise the same values will be written over and over again to your CSV file!

The finished code is [here](code/bmp_over_time.py) if you would like to compare it.

## Summary

- You have taken readings over a time period from the barometric pressure sensor and stored them as a CSV file.
- How could you use this data in another program?
- Why do you think the readings from the pressure sensor change over time?

## What next

- Using the data you have gathered from the barometric pressure sensor, import the CSV file into another application and use that application to analyse the data. Perhaps you could import into Excel or Google Sheets and draw a graph of the pressure readings over time?
