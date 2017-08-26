from gpiozero import DigitalInputDevice
from time import sleep
import math

count = 0       # Counts how many half-rotations
radius_cm = 9.0 # Radius of your anemometer
interval = 5    # How often (secs) to report speed

# Every half-rotation, add 1 to count
def spin():
	global count
	count = count + 1
	print( count )

# Calculate the wind speed 
def calc_speed(time_sec):
        global count  
        circumference_cm = (2 * math.pi) * radius_cm        
        rotations = count / 2.0

        # Calculate distance travelled by a cup in cm
        dist_cm = circumference_cm * rotations

        speed = dist_cm / time_sec

        return speed


wind_speed_sensor = DigitalInputDevice(5)
wind_speed_sensor.when_activated = spin


# Loop to measure wind speed and report at 5-second intervals
while True:
        count = 0
        sleep(interval)
        print( calc_speed(interval), "cm/h")




