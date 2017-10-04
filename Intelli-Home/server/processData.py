import sys
from threading import Thread
import pygal

time = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
		"12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]

def processTemperature(data):
	# To store the average temperature readings per hour
	hourlyData = [0] * 24
	# The number of temperature readings in the hour
	hourlyDataPoints = [0] * 24

	if len(data) == 0:
		printMessage("No temperature data found")
		return

	for d in data:
		date, temp = d.split("::")
		hour = int(date.split(':')[1])
		temp = float(temp.split(":")[1])
		hourlyData[hour] += temp
		hourlyDataPoints[hour] += 1

	for i in range(0, 24):
		if hourlyDataPoints[i] != 0:
			hourlyData[i] = float("{0:.2f}".format(hourlyData[i] / hourlyDataPoints[i]))

	print hourlyData
	printMessage("Processed temperature data")

	# Generate graphs
	chart = pygal.Bar()
	chart.title = "Mean temperature"
	chart.x_labels = time
	chart.add('temperature (C)', hourlyData)
	chart.render_to_file('temperature.svg')

def processDoorstatus(data):
	# To store the average temperature readings per hour
	doorstatusData = [0] * 24
	
	if len(data) == 0:
		printMessage("No door status data found")
		return

	for d in data:
		date, door = d.split("::")
		hour = int(date.split(':')[1])
		status = door.split(":")[1]
		if status == "OPENED":
			doorstatusData[hour] += 1

	print doorstatusData
	printMessage("Processed door status data")

	# Generate graphs
	chart = pygal.Bar()
	chart.title = "Door status"
	chart.x_labels = time
	chart.add('Door openings (#)', doorstatusData)
	chart.render_to_file('doorstatus.svg')

def processPhoto(data):
	# To store the average temperature readings per hour
	hourlyData = [0] * 24
	# The number of temperature readings in the hour
	hourlyDataPoints = [0] * 24

	if len(data) == 0:
		printMessage("No photo data found")
		return

	for d in data:
		date, photo = d.split("::")
		hour = int(date.split(':')[1])
		photo = float(photo.split(":")[1])
		hourlyData[hour] += photo
		hourlyDataPoints[hour] += 1

	for i in range(0, 24):
		if hourlyDataPoints[i] != 0:
			hourlyData[i] = float("{0:.2f}".format(hourlyData[i] / hourlyDataPoints[i]))

	print hourlyData
	printMessage("Processed photo data")

	# Generate graphs
        chart = pygal.Bar()
        chart.title = "Light"
        chart.x_labels = time
        chart.add('Light intensity (Lux)', hourlyData)
        chart.render_to_file('lightintensity.svg')

def processData(file_name):
	tempData = []
	doorData = []
	photoData = []
	f = open(file_name, 'r')
	lines = f.readlines()
	for line in lines:
		if "T" in line:
			tempData.append(line.strip('\n'))
		elif "D" in line:
			doorData.append(line.strip('\n'))
		elif "P" in line:
			photoData.append(line.strip('\n'))
	printMessage("Segregrated data")
	printMessage("Starting threads")
	threadTemp = Thread(target=processTemperature, args = (tempData,))
	threadDoor = Thread(target=processDoorstatus, args = (doorData,))
	threadPhoto = Thread(target=processPhoto, args = (photoData,))

	threadTemp.start()
	threadDoor.start()
	threadPhoto.start()

	threadTemp.join()
	threadDoor.join()
	threadPhoto.join()
	printMessage("Threads completed")

def printMessage(msg):
	print "[Intelli-Home] > ",msg

if __name__ == '__main__':
	if len(sys.argv) < 2:
		printMessage("ERROR, wrong number of arguments")
		printMessage("Use : processData <logFile>")
		sys.exit(1)
	else:
		file_name = sys.argv[1]
		processData(file_name)
