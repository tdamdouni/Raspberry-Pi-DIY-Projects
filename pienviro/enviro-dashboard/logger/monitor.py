import time
import os
from envirophat import weather, leds, light
from influxdb import InfluxDBClient

influx_host = os.getenv("INFLUX_HOST")
port = 8086
dbname = "environment"
user = "root"
password = "root"
host = os.getenv("PI_HOST")
sleep_time = os.getenv("SAMPLE_PAUSE")

client = InfluxDBClient(influx_host, port, user, password, dbname)
client.create_database(dbname)

def get_cpu_temp():
    path="/sys/class/thermal/thermal_zone0/temp"
    f = open(path, "r")
    temp_raw = int(f.read().strip())
    temp_cpu = float(temp_raw / 1000.0)
    return temp_cpu

def get_data_points():
    temp_cpu = get_cpu_temp()
    temperature = weather.temperature()
    pressure = round(weather.pressure(), 2)
    light_val = light.light()

    iso = time.ctime()
    json_body = [
            {
                "measurement": "ambient_celcius",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": temperature,
                    "val": float(temperature)
                    }
                },
            {
                "measurement": "cpu_celcius",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": temp_cpu,
                    }
                },
            {
                "measurement": "ambient_light",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": light_val,
                    }
                },
            {
                "measurement": "ambient_pressure",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": pressure,
                    }
                }

            ]

    return json_body

try:
    sleep_duration = float(sleep_time)
    while True:
        json_body = get_data_points()
        client.write_points(json_body)
        print (".")
        time.sleep(sleep_duration)

except KeyboardInterrupt:
    pass
