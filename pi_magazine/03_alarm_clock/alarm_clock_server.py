from bottle import route, run, template, request
import thread, time
import RPi.GPIO as GPIO
import datetime
from Adafruit_7Segment import SevenSegment


# Change these for your setup.
IP_ADDRESS = '192.168.1.13' # of your Pi
START_ANGLE = 50 # start angle before moving to bong the lid
END_ANGLE = 73 # end angle this should just be touching the lid
DELAY_IN = 0.5 # delay to allow servo to get to start position
DELAY_OUT = 0.1 # delay at point of bong before returning to start

SERVO_PIN = 18 # control pin of servo
BUTTON_PIN = 23 # pin connected to Cancel button

segment = SevenSegment(address=0x70)

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 100) # start PWM at 100 Hz
pwm.start(0)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Glogal variables
alarm_on = True
alarm_time = ''

# Set the servo to the angle specified
def set_angle(angle):
    if angle < 1.0:
        pwm.ChangeDutyCycle(0) # stop servo jitter when not banging
    else:
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)
    
def bong():
    set_angle(START_ANGLE)
    time.sleep(DELAY_IN)
    set_angle(END_ANGLE)
    time.sleep(DELAY_OUT)

def update_display():
    # Get the time by separate parts for the clock display
    now = datetime.datetime.now()
    hour = now.hour    
    minute = now.minute
    second = now.second
    # Set hours
    segment.writeDigit(0, int(hour / 10))     # Tens
    segment.writeDigit(1, hour % 10)          # Ones
    # Set minutes
    segment.writeDigit(3, int(minute / 10))   # Tens
    segment.writeDigit(4, minute % 10)        # Ones
    # Toggle colon
    segment.setColon(second % 2)              # Toggle colon at 1Hz

# Handler for the home page
@route('/')
def index(name='time'):
    return template('home.tpl')

# Handler for the 'conformation' page
@route('/setconfirmation', method='POST')
def confirm():
    global alarm_time, alarm_on
    # Get the time entered in the time form
    alarm_time = request.POST.get('alarm_time', '')
    alarm_on = True
    # Go to the conformation page
    return template('setconfirmation.tpl', t=alarm_time)
        



def update(thread_name):
    global alarm_on, alarm_time
    while True:
        # Get the time formatted as a string for comparison with the alarm time
        current_time = time.strftime("%H:%M")
        # Bong for as long as the alaem is on and its the right minute
        if current_time == alarm_time and alarm_on:
            bong()
        # Check for the alarm cancel button
        if GPIO.input(BUTTON_PIN) == False:
            alarm_on = False
            set_angle(0)
        update_display()
        time.sleep(0.1) # allow other threads to run

# start a separate thread of execution to update the display and chack the time
thread.start_new_thread(update, ("update_thread",))

# Start the webserver running on port 80
try:
    run(host=IP_ADDRESS, port=80)
finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
