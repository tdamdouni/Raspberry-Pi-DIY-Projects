# bme680-mqtt
Modifies example by [Pimoroni](https://github.com/pimoroni/bme680/blob/master/examples/indoor-air-quality.py) to publish [bme680](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout) data via MQTT.

To add the MQTT output to [Home-assistant](https://home-assistant.io/), we use an [MQTT-switch](https://home-assistant.io/components/switch.mqtt/). Assuming you have your Home-assistant [config split](https://home-assistant.io/docs/configuration/splitting_configuration/) into seperate files, in your sensors.yaml file, add the following:

```yaml
- platform: mqtt
  name: 'bme680-temperature'
  state_topic: 'bme680-temperature'
  unit_of_measurement: '°C'
- platform: mqtt
  name: 'bme680-humidity'
  state_topic: 'bme680-humidity'
  unit_of_measurement: '%'
- platform: mqtt
  name: 'bme680-pressure'
  state_topic: 'bme680-pressure'
  unit_of_measurement: 'hPa'
- platform: mqtt
  name: 'bme680-air_qual'
  state_topic: 'bme680-air_qual'
  unit_of_measurement: '%'
```

I then created a group, in groups.yaml:

```yaml
BME680:
  entities:
    - sensor.bme680temperature
    - sensor.bme680pressure
    - sensor.bme680humidity
    - sensor.bme680air_qual
```

Finally you may want to [customise](https://home-assistant.io/docs/configuration/customizing-devices/) the look of the sensors in the Home-assistant front end. 

<img src="https://github.com/robmarkcole/bme680-mqtt/blob/master/HA_view.png">
