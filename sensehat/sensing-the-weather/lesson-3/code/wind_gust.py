from gpiozero import DigitalInputDevice
from time import sleep
import math

count = 0       # Counts how many half-rotations
radius_cm = 9.0 # Radius of your anemometer
interval = 5    # How often (secs) to report speed
ADJUSTMENT = 1.18
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600 
store_speeds = [] # Define a list to store last 4 wind speeds

# Every half-rotation, add 1 to count
def spin():
    global count
    count = count + 1
    print( count )

# Calculate the wind speed given the time interval 
def calc_speed(time_sec):
        global count
        global store_speeds
        circumference_cm = (2 * math.pi) * radius_cm        
        rotations = count / 2.0

        # Calculate distance travelled by a cup in km
        dist_km = (circumference_cm * rotations) / CM_IN_A_KM

        # Speed = distance / time
        km_per_sec = dist_km / time_sec
        km_per_hour = km_per_sec * SECS_IN_AN_HOUR

        # Calculate speed
        final_speed = km_per_hour * ADJUSTMENT

        # Add this speed to the list
        store_speeds.append(final_speed)

        # If that takes the list over 4 items, chop off the first
        if len(store_speeds) > 4:
                store_speeds = store_speeds[1:]
      
        # Show what is in the store_speeds list
        print( str(store_speeds) )
        
        return final_speed

# Check whether the last 20 seconds of readings had any gusts
def check_for_gusts():
        highest = max(store_speeds)
        lowest = min(store_speeds)
        GUST_ABOVE = 29.6       
        GUST_RANGE = 16.7
        if highest > GUST_ABOVE and highest - lowest > GUST_RANGE:
            return highest
        else:
            return 0      

wind_speed_sensor = DigitalInputDevice(5)
wind_speed_sensor.when_activated = spin


# Loop to measure wind speed and report at 5-second intervals
while True:
        count = 0
        sleep(interval)
        print( calc_speed(interval), "kph")
        print("Gust speed " + str(check_for_gusts() + "kph")
