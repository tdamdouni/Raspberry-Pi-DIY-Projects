import datetime
import time
import csv
from sense_hat import SenseHat

dt_format="%Y-%m-%d %H:%M:%S"
log_csv='sensehat.csv'
interval_seconds=60*5
max_readings=288

with open(log_csv, 'wb') as csvfile:
	sensor_writer=csv.writer( csvfile )
	sensor_writer.writerow(["TIME", "TEMPERATURE", "HUMIDITY", "PRESSURE"])
	sense=SenseHat()
	for reading in range(0,max_readings):
		dt=datetime.datetime.now()
		sensor_writer.writerow(	[dt.strftime(dt_format),
					sense.get_temperature(),
					sense.get_humidity(),
					sense.get_pressure() ]
					)
		time.sleep( interval_seconds )
