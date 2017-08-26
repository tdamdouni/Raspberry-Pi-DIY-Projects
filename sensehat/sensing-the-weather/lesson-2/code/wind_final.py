from gpiozero import DigitalInputDevice
from time import sleep
import math

count = 0
radius_cm = 9.0		# Radius of the anemometer
interval = 5		# How often to report speed
ADJUSTMENT = 1.18	# Adjustment for weight of cups
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600

def calculate_speed(time_sec):
    global count
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = count / 2.0

    dist_km = (circumference_cm * rotations) / CM_IN_A_KM

    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * SECS_IN_AN_HOUR

    return km_per_hour * ADJUSTMENT

def spin():
    global count
    count = count + 1
    print (count)

wind_speed_sensor = DigitalInputDevice(5)
wind_speed_sensor.when_activated = spin

while True:
    count = 0
    sleep(interval)
    print ( calculate_speed(interval), "kph")