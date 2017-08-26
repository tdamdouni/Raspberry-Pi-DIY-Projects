FROM alexellis2/python2-gpio-armhf:2-dev
RUN apt-get -qy update && apt-get -qy --no-install-recommends install git python-smbus
WORKDIR /root/

RUN git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
WORKDIR /root/Adafruit_Python_GPIO
RUN python setup.py install

WORKDIR /root/
RUN git clone https://github.com/adafruit/Adafruit_Python_BME280
RUN pip install influxdb

WORKDIR /root/Adafruit_Python_BME280

RUN sed -ie s/0x77/0x76/ Adafruit_BME280.py

ADD ./sensor.py ./sensor.py

entrypoint ["/usr/bin/python", "./sensor.py"]

