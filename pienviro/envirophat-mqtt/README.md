# envirophat-mqtt
Publish sensor updates from Enviro pHat to MQTT

Calibrates the temperature reading for variance caused by heat from the CPU of the Raspberry Pi and smooths the data using a moving average.

A factor of 1.2 works well for me, but may vary depending on case and environment.

## Running

```
sudo npm i -g envirophat-mqtt
envirophat-mqtt
```

Use PM2 or similar to run on startup.

## Configuration

Create a config file at `/etc/envirophatmqtt/config.yml`

Check the available settings and defaults in `config/defaults.yml`.

Example:

```yml
---

mqtt:
  host: '192.168.0.123'
  topic: sensor/loune/input
temperature:
  factor: 1.2
interval:
  duration: 60000
```

## Pre-requisites

1. Pimoroni libs: `curl https://get.pimoroni.com/envirophat | bash`
2. Node js

## Why Node js?

Selfish reason: Because all my existing home automation runs on Node js managed with PM2.

Even though the provided libraries are Python, and it's pretty easy to publish to MQTT from Python, I wrote this so I could run my entire platform on Node js.

