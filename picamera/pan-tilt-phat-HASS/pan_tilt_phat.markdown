---
layout: page
title: "Pan-tilt HAT"
description: "Instructions on add the Pimoroni Pan-Tilt hat to Home Assistant."
date: 2017-08-29 19:00
sidebar: true
comments: false
sharing: true
footer: true
logo: raspberry-pi.png
ha_category: DIY
ha_release: 0.53
ha_iot_class: "Local Push"
---

The `pan_tilt_phat` platform allows you to control a [Pimoroni Pan-Tilt hat](https://shop.pimoroni.com/products/pan-tilt-hat) mounted on the raspberry-pi running Home Assistant. The platform imports the [pantilthat](https://pypi.python.org/pypi/pantilthat/0.0.4) package by Pimoroni. The hat consists of two servos which can pan and tilt a mounted camera with 180 degrees of motion (+/- 90 degrees) along each axis (vvertical and horizontal). This documentation assumes you have a [raspberry pi camera](https://home-assistant.io/components/camera.rpi_camera/) mounted on the hat, although other brands of camera could be used with some modification to the mounting. The platform adds a sensor which displays the current pan angle (there is currently a bug in the tilt angle)). The platform provides services for setting the angle of each servo, and a service to home the servos to zero degrees on both axis.

To add this platform to your installation, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry,
# which is equivalent to the default setup
sensor:
  - platform: pan_tilt_phat
```
### {% linkable_title Service `home_service` %}

Calling this service returns the servos to their home position, no service data is required.

### {% linkable_title Service `pan_service` %}

Calling this service changes the pan angle (horizontal plane). The angular range is from -90 to 90 degrees.

| Service data attribute | Optional | Description |
| ---------------------- | -------- | ----------- |
| `Pan` | no | An integer in the range -90 to 90


### {% linkable_title Service `tilt_service` %}

Calling this service changes the tilt angle (vertical plane). The angular range is from -90 to 90 degrees.

| Service data attribute | Optional | Description |
| ---------------------- | -------- | ----------- |
| `Tilt` | no | An integer in the range -90 to 90


### {% linkable_title Optional `input_slider & camera configuration` %}

To add the [raspberry pi camera](https://home-assistant.io/components/camera.rpi_camera/) (in the correct orientation for the mount position on the hat) and [input_sliders](https://home-assistant.io/components/input_slider/) to control the pan and tilt servos via the Home Assistant front end, add the following to your `configuration.yaml` file:

```yaml
camera:
  - platform: rpi_camera
    vertical_flip: 1

input_slider:
  pan_control:
    name: Pan
    initial: 0
    min: -90
    max: 90
    step: 1
  tilt_control:
    name: Tilt
    initial: 0
    min: -90
    max: 90
    step: 1
```
Two automations should be created, one each to call the pan/tilt service when there is a state change of the pan/tilt input_slider. The automation could be written in yaml, or alternatively a [python_script](https://home-assistant.io/components/python_script/) could be used, with an example for the pan angle (saved in `pan_slider.py`) given below:

```python
entity_id = 'input_slider.pan_control'
slider_value = int(float(hass.states.get(entity_id).state))
hass.services.call('pan_tilt_phat', 'pan', {"Pan":slider_value})
```
The automation to trigger this service (created using the automations editor) is:

```yaml
- action:
  - data: {}
    service: python_script.pan_slider
  alias: Pan Automation
  condition: []
  id: '12345'
  trigger:
  - entity_id: input_slider.pan_control
    platform: state
```
Repeat for the tilt servo.

TO DO - FEEDBACK TO INPUT SLIDER FROM CURRENT ANGLE
