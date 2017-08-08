# Node Pan-Tilt HAT library

_Captured: 2017-05-17 at 21:00 from [npmdaily.com](https://npmdaily.com/pkg/pan-tilt-hat)_

Node Pan-Tilt HAT library (C) 2017 Roger Hardiman

This library provides an easy way for NodeJS applications to use the Raspberry Pi Pan-Tilt HAT (made by Pimoroni) with the AdaFruit Pan/Tilt assembly. It spawns a background Python process to communicate with the Pan-Tilt HAT and this Python process make use of Pimoroni's Python libraries. You must install Python and install the Pimoroni Pan-Tilt HAT Python libraries before using this code.

This library provides two APIs

  1. Pimoroni API The library impements pan(angle) tilt(angle) servo_one(angle) servo_two(angle)

  2. Continual Move API The API is based on analogue CCTV systems where a a command will start the pan or tilt motors moving and the motors contiune to move until a stop command is issued. The API commands are pan_left(speed) pan_right(speed) tilt_up(speed) tilt_down(speed) stop() The library constantly re-computes the absolute angle for the pan and tilt based on the previous position and the current speed.

## Applications

The library is being used in the Raspbery Pi ONVIF Server project (RPOS) that turns a Pi + Pi Camera + Pan-Tilt HAT + AdaFruit Pan/Tilt assembly into an ONVIF Profile S CCTV Camera.
