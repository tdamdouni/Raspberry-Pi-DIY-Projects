from os import system
import serial
import subprocess
from time import sleep
from ISStreamer.Streamer import Streamer

BUCKET_NAME = "Fona GPS"
BUCKET_KEY = "fona"
ACCESS_KEY = "Your_Access_Key"
SECONDS_BETWEEN_READS = 60

# Start PPPD
def openPPPD():
	# Check if PPPD is already running by looking at syslog output
	output1 = subprocess.check_output("cat /var/log/syslog | grep pppd | tail -1", shell=True)
	if "secondary DNS address" not in output1 and "locked" not in output1:
		while True:
			# Start the "fona" process
			subprocess.call("sudo pon fona", shell=True)
			sleep(2)
			output2 = subprocess.check_output("cat /var/log/syslog | grep pppd | tail -1", shell=True)
			if "script failed" not in output2:
				break
	# Make sure the connection is working
	while True:
		output2 = subprocess.check_output("cat /var/log/syslog | grep pppd | tail -1", shell=True)
		output3 = subprocess.check_output("cat /var/log/syslog | grep pppd | tail -3", shell=True)
		if "secondary DNS address" in output2 or "secondary DNS address" in output3:
			return True

# Stop PPPD
def closePPPD():
	print "turning off cell connection"
	# Stop the "fona" process
	subprocess.call("sudo poff fona", shell=True)
	# Make sure connection was actually terminated
	while True:
		output = subprocess.check_output("cat /var/log/syslog | grep pppd | tail -1", shell=True)
		if "Exit" in output:
			return True

# Check for a GPS fix
def checkForFix():
	print "checking for fix"
	# Start the serial connection
	ser=serial.Serial('/dev/serial0', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	# Turn on the GPS
	ser.write("AT+CGNSPWR=1\r")
	ser.write("AT+CGNSPWR?\r")
	while True:
		response = ser.readline()
		if " 1" in response:
			break
	# Ask for the navigation info parsed from NMEA sentences
	ser.write("AT+CGNSINF\r")
	while True:
			response = ser.readline()
			# Check if a fix was found
			if "+CGNSINF: 1,1," in response:
				print "fix found"
				print response
				return True
			# If a fix wasn't found, wait and try again
			if "+CGNSINF: 1,0," in response:
				sleep(5)
				ser.write("AT+CGNSINF\r")
				print "still looking for fix"
			else:
				ser.write("AT+CGNSINF\r")

# Read the GPS data for Latitude and Longitude
def getCoord():
	# Start the serial connection
	ser=serial.Serial('/dev/serial0', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	ser.write("AT+CGNSINF\r")
	while True:
		response = ser.readline()
		if "+CGNSINF: 1," in response:
			# Split the reading by commas and return the parts referencing lat and long
			array = response.split(",")
			lat = array[3]
			print lat
			lon = array[4]
			print lon
			return (lat,lon)


# Start the program by opening the cellular connection and creating a bucket for our data
if openPPPD():
	# Initialize the Initial State streamer
	streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY, buffer_size=20)
	# Wait long enough for the request to complete
	sleep(10)
	
	while True:
		# Close the cellular connection
		if closePPPD():
			print "closing connection"
			sleep(1)
		# The range is how many data points we'll collect before streaming
		for i in range(10):
			# Make sure there's a GPS fix
			if checkForFix():
				# Get lat and long
				if getCoord():
					latitude, longitude = getCoord()
					coord = str(latitude) + "," + str(longitude)
					print coord
					# Buffer the coordinates to be streamed
					streamer.log("Coordinates",coord)
					sleep(SECONDS_BETWEEN_READS)
			# Turn the cellular connection on every 10 reads
			if i == 9:
				print "opening connection"

				if openPPPD():
					print "streaming"
					# Flush the streaming queue and send the data
					streamer.flush()
					print "streaming complete"
