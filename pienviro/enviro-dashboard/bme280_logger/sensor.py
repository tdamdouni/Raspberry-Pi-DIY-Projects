import time
import os

from influxdb import InfluxDBClient

host = os.getenv("INFLUX_HOST")
port = 8086
dbname = os.getenv("DB")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

host_pi = os.getenv("HOSTNAME")  # change this on each Pi
sample_duration = 30  # seconds

client = InfluxDBClient(host, port, user, password, dbname)
client.create_database(dbname)

from Adafruit_BME280 import *

sensor = BME280(mode=BME280_OSAMPLE_8)

def get_cpu_temp():
    path="/sys/class/thermal/thermal_zone0/temp"
    f = open(path, "r")
    temp_raw = int(f.read().strip())
    temp_cpu = float(temp_raw / 1000.0)
    return temp_cpu

try:
    while True:
        temp_cpu = get_cpu_temp()

        degrees = float(sensor.read_temperature())
        pascals = float(sensor.read_pressure())
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()

        iso = time.ctime()
        json_body = [
        {
          "measurement": "ambient_celcius",
          "tags": {"host": host_pi},
          "time": iso,
          "fields": {
             "value": degrees,
             "val": float(degrees)
          }
        },
        {
          "measurement": "cpu_celcius",
          "tags": {"host": host_pi},
          "time": iso,
          "fields": {
             "value": temp_cpu,
          }
        },
        {
          "measurement": "relative_humidity",
          "tags": {"host": host_pi},
          "time": iso,
          "fields": {
             "value": humidity,
          }
        },
        {
          "measurement": "ambient_pressure",
          "tags": {"host": host_pi},
          "time": iso,
          "fields": {
             "value": hectopascals,
          }
        }
        ]
        client.write_points(json_body)
        time.sleep(sample_duration)

except KeyboardInterrupt:
    pass
