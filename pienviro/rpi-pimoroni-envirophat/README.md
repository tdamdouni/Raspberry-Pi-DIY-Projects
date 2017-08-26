# Pimoroni Enviro pHAT Docker Image

Herein lies the `Dockerfile` needed to build a Docker image suitable for running Python 3 scripts using the [Pimoroni Enviro pHAT module](https://shop.pimoroni.com/products/enviro-phat) for the Raspberry Pi.

* [GitHub Repository](https://github.com/jbrisbin/rpi-pimoroni-envirophat)
* [Dockerfile](https://github.com/jbrisbin/rpi-pimoroni-envirophat/blob/master/Dockerfile)

### Pre-requisites

This image builds on the `jbrisbin/rpi-python3` image. Please make sure your Pi can run I2C before continuing. Instructions are in [the README](https://github.com/jbrisbin/rpi-python3).

### Create the Docker Image

Once you're sure that I2C is working on your Pi, build the Docker image using the included `Dockerfile`.

```sh
docker build -t rpi-envirophat .
```

### Run the Docker image

The Docker image assumes you want to mount your executable Python scripts at `/data` (which is defined as a `VOLUME` and the `WORKDIR`) so the `CMD` has been defined as `python3`. To run your scripts, add them to the container via volume, along with the `/dev` directory and add your main script as an argument to the `docker run` command. In this example, inside the working directory `./data` is a script named `read-weather-sensors.py`.

```python
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
```

#### Read the sensor

You can run this script interactively from an SSH session.

```sh
docker run --privileged \
    -v /dev:/dev \
    -v $(realpath ./data):/data \
    rpi-envirophat \
    read-weather-sensors.py
```

#### Run from crontab

Or, you can run this script periodically by setting up a `crontab` entry for every minute that invokes the above `docker run` command and pipes the output to a file somewhere via `>>/data/sensor.log`.