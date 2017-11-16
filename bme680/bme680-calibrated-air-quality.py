#!/usr/bin/env python

# https://forums.pimoroni.com/t/bme680-air-quality-low/6293/14

# the average gas resistance readings, as you would need to use your own value here

import bme680
import time

# Define the BME680 sensor
sensor = bme680.BME680()

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.
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
    # Set the gas resistance baseline. It is recommended
    # to run 'read-all.py' for at least 24 hours
    # and then average the resuls for this value.
    gas_baseline = INSERT_BASELINE_VALUE_HERE

    # This sets the balance between humidity and gas reading in the
    # calculation of air_quality_score (25:75, humidity:gas)
    hum_weighting = 0.25

    # Set the humidity baseline to 40%, an optimal indoor humidity.
    hum_baseline = 40.0

    while True:
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            gas_offset = gas_baseline - gas

            hum = sensor.data.humidity
            hum_offset = hum - hum_baseline

            # Calculate hum_score as the distance from the hum_baseline.
            if hum_offset > 0:
                hum_score = (100 - hum_baseline - hum_offset) / (100 - hum_baseline) * (hum_weighting * 100)

            else:
                hum_score = (hum_baseline + hum_offset) / hum_baseline * (hum_weighting * 100)

            # Calculate gas_score as the distance from the gas_baseline.
            if gas_offset > 0:
                gas_score = (gas / gas_baseline) * (100 - (hum_weighting * 100))

            else:
                gas_score = 100 - (hum_weighting * 100)

            # Caclulate air_quality score.
            air_quality_score = hum_score + gas_score

            print("Gas: {0:.2f} Ohms,humidity: {1:.2f} %RH,air quality: {2:.2f}".format(gas, hum, air_quality_score))
            time.sleep(1)

except KeyboardInterrupt:
    pass
