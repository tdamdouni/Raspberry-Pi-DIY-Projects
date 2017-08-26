from __future__ import division
from subprocess import PIPE, Popen
from envirophat import weather
from ISStreamer.Streamer import Streamer
import time

# --------- User Settings ---------
# Initial State settings
BUCKET_NAME = "pienviro"
BUCKET_KEY = "..."
ACCESS_KEY = "..."
SENSOR_NAME = "envir:cloud: pHAT"
# Set the time between sensor reads
MINUTES_BETWEEN_READS = 2
METRIC_UNITS = False
# ---------------------------------

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

def main():
    streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
    while True:
        cpu_temp_c = get_cpu_temperature()
        temp_c = weather.temperature()
        temp_c_cal = temp_c - ((cpu_temp_c-temp_c)/1.3)
        if (METRIC_UNITS):
            streamer.log(":desktop: CPU Temperature(C)", cpu_temp_c)
        else:
            cpu_temp_f = cpu_temp_c * 9.0 / 5.0 + 32.0
            streamer.log(":desktop: CPU Temperature(F)", str("{0:.2f}".format(cpu_temp_f)))

        if isFloat(temp_c):
            if (METRIC_UNITS):
                # print("Temperature(C) = " + str(temp_c))
                if (temp_c > -15) and (temp_c < 100):
                    streamer.log(":sunny: " + SENSOR_NAME + " Temperature(C)", temp_c)
                    streamer.log(":sunny: Calibrated " + SENSOR_NAME + " Temperature(C)", temp_c_cal)
            else:
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                temp_f_cal = temp_c_cal * 9.0 / 5.0 + 32.0
                # print("Temperature(F) = " + str("{0:.2f}".format(temp_f)))
                if (temp_f > 0) and (temp_f < 110):
                    streamer.log(":sunny: " + SENSOR_NAME + " Temperature(F)", str("{0:.2f}".format(temp_f)))
                    streamer.log(":sunny: Calibrated " + SENSOR_NAME + " Temperature(F)", str("{0:.2f}".format(temp_f_cal)))
            streamer.flush()
        time.sleep(60*MINUTES_BETWEEN_READS)

if __name__ == "__main__":
    main()
