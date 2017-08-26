# Import necessary libraries
import os, glob, math, time, sys, socket, psutil, threading, random
from gpiozero import LED, PWMLED

def get_operating_system_information():
	os_file = '/etc/os-release'

	f = open(os_file, "r")
	lines = f.readlines()
	f.close()
	
	info = lines[0][13:].strip()
	info = info[:len(info)-1]

	return info

# Set-up LEDs
led_red = PWMLED(17)
led_yellow = PWMLED(27)
led_green = PWMLED(22)
led_blue = PWMLED(10)

# Helper function to iterate over a float
def frange(start, stop, step):
	i = start
	
	if (start < stop):
		while i <= stop:
			yield i
			i += step
			# For some reason, += doesn't always add an exact decimal, so we have to round the value
			i = round(i, 1)
	else:
		while i >= stop:
			yield i
			i += step
			# For some reason, += doesn't always add an exact decimal, so we have to round the value
			i = round(i, 1)

class RandomLEDs(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def run(self):
		while True:
			led_list = [led_blue,led_yellow,led_green,led_red]
			the_led = random.choice(led_list)
			self.fade_in_led(the_led, 0.03)
			time.sleep(0.2)
			self.fade_out_led(the_led, 0.04)
			time.sleep(0.2)

	# PWM the LED value from 0 to 1 (or from 1 to 0) with a 0.1 step
	def fade_in_led(self, led, speed):
		for i in frange(0.0, 1.0, 0.1):
			led.value = i
			time.sleep(speed)

	def fade_out_led(self, led, speed):
		for i in frange(1.0, 0.0, -0.1):
			led.value = i
			time.sleep(speed)

# Try to set-up Scroll pHAT, set flag if not available
try:
	import scrollphat
	scrollphat.set_brightness(5)
	scrollphat_connected = True
except:
	scrollphat_connected = False

try:
	import Adafruit_BMP.BMP085 as BMP085
	BMP = BMP085.BMP085()
	bmp_sensor_okay = True
except:
	print("BMP sensor not working")
	bmp_sensor_okay = False

# Try to connect to network and get IP. If not connected, set flag
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	ip = s.getsockname()[0]
	s.close()
	network_connected = True

except:
	ip = "Not connected"
	network_connected = False

# Set-up external temperature sensor
try:
	os.system("modprobe w1-gpio")
	os.system("modprobe w1-therm")
	base_dir = "/sys/bus/w1/devices"
	device_folder = glob.glob(base_dir + '28*')[0]
	device_file = device_folder + '/w1_slave'
	temp = read_temp()
	ext_temperature_connected = True

except:
	ext_temperature_connected = False

# Read the raw temperature device file (1-wire)
def read_temp_raw():
	f = open(device_file, "r")
	lines = f.readlines()
	f.close()
	return lines

# Convert the raw temp to something understandable (1-wire)
def read_temp():
	try:
		lines = read_temp_raw()
	
		while lines[0].strip()[-3:] != "YES":
			time.sleep(0.2)
			lines = read_temp_raw()
	
		equals_pos = lines[1].find("t=")
	
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			temp_f = temp_c * 9.0 / 5.0 + 32.0
			return temp_c, temp_f
		else:
			return -1.0,-1.0
	except:
		return -1.0,-1.0

# If the Scroll pHAT is connected, scroll the message. If it's not, display to screen
def display(message):
	if scrollphat_connected:
		scrollphat.clear()
		scrollphat.write_string(message + "       ", 11)
		for i in range(0, scrollphat.buffer_len() - 11):
			scrollphat.scroll()
			time.sleep(0.08)
	else:
		print(message)
		time.sleep(0.1)

# Get the CPU temperature by issuing a system command and mining the response
def get_system_temperature():
	f = os.popen("/opt/vc/bin/vcgencmd measure_temp")
	mytemp = ""
	for i in f.readlines():
		mytemp += i
		firstchar  = mytemp[5:-6]
		secondchar = mytemp[6:-5]
		thirdchar  = mytemp[8:-3]

	return firstchar + secondchar + "." + thirdchar + " C"

# Start independent threads
# This one lights up a random LED
thread1 = RandomLEDs(1, "Thread-1")
thread1.start()

# Main loop
while True:
	# Get operating system 'pretty name' and display it
	os_info = get_operating_system_information()
	display("OS: " + os_info)

	if bmp_sensor_okay:
		display("BMP temp = {0:0.2f} *C".format(BMP.read_temperature()))
		display("Pressure = {0:0.2f} Pa".format(BMP.read_pressure()))
		display("Altitude = {0:0.2f} m".format(BMP.read_altitude()))
		display("Sealevel Pressure = {0:0.2f} Pa".format(BMP.read_sealevel_pressure()))

	# Display time if network is connected
	if network_connected:
		f = os.popen("date")
		for i in f.readlines():
			mytime = i[11:-13]
		display("Time: " + mytime)

	# Display IP if network is connected
	if network_connected:
		display("IP: " + ip)
	else:
		display("Not connected to network")

	# Get system temperature and display
	display("Sys temp: " + get_system_temperature())

	# Get temperature from the 1-wire sensor (if connected) and display it
	if ext_temperature_connected:
		temperature_c, temperature_f = read_temp()
		display("Ext temp: " + str(temperature_c) + " C / " + str(temperature_f) + " F")
		time.sleep(1)

