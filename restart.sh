#!/bin/bash

if [ "$(pidof python)" ]
then
  exit
else
  nohup /home/pi/clock.py &>/dev/null &
fi