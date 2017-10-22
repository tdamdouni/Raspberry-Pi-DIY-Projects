# Timelapse-Pi
# A backpack-mounted all-day timelapse project with the Raspberry Pi Zero
# Author: Matthew Timmons-Brown (The Raspberry Pi Guy)
# 19/03/2017

import time
import os
import subprocess
from gpiozero import PWMLED, Button

path = "/home/pi/timelapse-pi/images/img"
pic_count = 0
shutdown = ["sudo", "shutdown", "now"]

rate = "1000"

led = PWMLED(14, True, 0, 100)
button = Button(15, False, None, 3, False)

def starting_flash(light):
	light.blink(0.3, 0.3, 0, 0, 5, False)
	light.on()

def off_pulse(light):
	light.pulse(0.5, 0.5, 3, False)

def when_held():
	off_pulse(led)
	subprocess.call(shutdown)

def take_pic(output_path):
	subprocess.call(["raspistill", "-vf", "-q", "100", "-t", rate, "-o", output_path])

button.when_held = when_held

def main():
	stop = False
	pic_count = 0

	while True:
		starting_flash(led)
		button.wait_for_press(None)
		led.off()
		stop = False
		while not stop:
			new_path = (path + "%s.jpg" % pic_count)
			while os.path.exists(new_path):
				pic_count += 1
				new_path = (path + "%s.jpg" % pic_count)
				print(new_path)

			take_pic(new_path)

if __name__ == "__main__":
	main()
