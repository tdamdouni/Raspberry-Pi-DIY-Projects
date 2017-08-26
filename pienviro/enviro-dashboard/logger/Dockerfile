FROM alexellis2/python2-gpio-armhf:2
RUN pip2 install envirophat 
RUN apt-get update -qy && apt-get install -qy python-smbus
RUN pip install influxdb
ADD ./monitor.py ./monitor.py

ENTRYPOINT []
CMD ["python2", "monitor.py"]
