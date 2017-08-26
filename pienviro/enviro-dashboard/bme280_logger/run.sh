#!/bin/bash

docker rm -f env1 || :

docker run --name env1 --privileged \
--restart=always \
-e INFLUX_HOST=192.168.0.x -e DB=environment -e USER=ROOT -e PASSWORD=root -e HOSTNAME=sensor2 \
-d alexellis2/bme280-influxclient-armhf:1
