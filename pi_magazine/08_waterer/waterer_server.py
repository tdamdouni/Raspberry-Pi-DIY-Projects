from bottle import route, run, template, request
import thread, time
import RPi.GPIO as GPIO
import datetime


# Change these for your setup.
PUMP_PIN = 18

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, 0)

# Glogal variables
start_time = "22:00"
duration = "30"

# Handler for the home page
@route('/')
def index():
    global start_time, duration
    # Change the start_time and duration, but not to nothing.
    local_start_time = request.GET.get('start_time', '')
    if local_start_time != "":
        start_time = local_start_time
    local_duration = request.GET.get('duration', '')
    if local_duration != "":
        duration = local_duration
    return template('home.tpl', start_time=start_time, duration=duration)


def update(thread_name):
    global start_time, duration
    watering = False
    end_timestamp = 0
    while True:
        # Get the time formatted as a string for comparison with the alarm time
        current_time = time.strftime("%H:%M")
        # If its time to start watering, do so, but not if you are already watering
        if current_time == start_time and not watering:
            print("Starting Watering")
            watering = True
            GPIO.output(PUMP_PIN, 1)
            end_timestamp = time.time() + int(duration) * 60
        # Check to see if its time to stop watering
        if watering and time.time() > end_timestamp:
            print("End Watering")
            watering = False
            GPIO.output(PUMP_PIN, 0)
            
        time.sleep(1) # allow other threads to run

# start a separate thread to check the time
thread.start_new_thread(update, ("update_thread",))

# Start the webserver running on port 80
try:
    run(host="0.0.0.0", port=80)
finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
