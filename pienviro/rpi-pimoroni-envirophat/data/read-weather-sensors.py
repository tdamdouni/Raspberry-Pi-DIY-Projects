#!/usr/bin/env python3
from envirophat import weather, light
from subprocess import PIPE, Popen
import sys, time, csv

def get_cpu_temp():
	process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
	output, _error = process.communicate()
	return float(output[5:9])

def read_sensor():
	fields = ['timestamp', 'cpu_temp', 'weather_temp', 'weather_pressure', 'light_r', 'light_g', 'light_b', 'light_level']
	w = csv.DictWriter(sys.stdout, fieldnames=fields)

	lr, lg, lb = light.rgb()
	data = {
		'timestamp': time.time(),
		'cpu_temp': get_cpu_temp(),
		'weather_temp': weather.temperature(),
		'weather_pressure': weather.pressure(),
		'light_r': lr,
		'light_g': lg,
		'light_b': lb,
		'light_level': light.light()
	}
	w.writerow(data)

if __name__ == '__main__':
	read_sensor()