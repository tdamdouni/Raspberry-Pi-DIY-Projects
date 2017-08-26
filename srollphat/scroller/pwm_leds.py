# Import necessary libraries
import time, threading, random
from gpiozero import LED, PWMLED

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
			time.sleep(0.3)
			self.fade_out_led(the_led, 0.02)
			time.sleep(0.3)

	# PWM the LED value from 0 to 1 (or from 1 to 0) with a 0.1 step
	def fade_in_led(self, led, speed):
		for i in frange(0.0, 1.0, 0.1):
			led.value = i
			time.sleep(speed)

	def fade_out_led(self, led, speed):
		for i in frange(1.0, 0.0, -0.1):
			led.value = i
			time.sleep(speed)

# Start independent threads
# This one lights up a random LED
thread1 = RandomLEDs(1, "Thread-1")
thread1.start()

