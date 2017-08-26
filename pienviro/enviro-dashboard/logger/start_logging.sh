#!/bin/bash

export INFLUX_HOST=192.168.0.3
export PI_HOST=study
export SAMPLE_PAUSE=30
python2 ./monitor.py 

