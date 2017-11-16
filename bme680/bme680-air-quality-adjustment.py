#!/usr/bin/env python

# https://forums.pimoroni.com/t/bme680-air-quality-low/6293/12

import bme680
import time

sensor = bme680.BME680()

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

start_time = time.time()
curr_time = time.time()

try:
    gas_baseline = INSERT_BASELINE_VALUE_HERE
    hum_weighting = 0.25

    while True:
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            gas_offset = gas_baseline - gas

            hum = sensor.data.humidity
            hum_offset = hum - hum_baseline

            if hum_offset > 0:
                hum_score = (100 - hum_baseline - hum_offset) / (100 - hum_baseline) * (hum_weighting * 100)

            else:
                hum_score = (hum_baseline + hum_offset) / hum_baseline * (hum_weighting * 100)

            if gas_offset > 0:
                gas_score = (gas / gas_baseline) * (100 - (hum_weighting * 100))

            else:
                gas_score = 100 - (hum_weighting * 100)

            air_quality_score = hum_score + gas_score

            print("Gas: {0:.2f} Ohms,humidity: {1:.2f} %RH,air quality: {2:.2f}".format(gas, hum, air_quality_score))
            time.sleep(1)

except KeyboardInterrupt:
    pass
