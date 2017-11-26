import subprocess, time
import RPi.GPIO as GPIO
from squid import *

HOSTNAME = "us.mineplex.com"
# HOSTNAME = "google.com"
PING_PERIOD = 3.0 # seconds
GOOD_PING = 0.1   # seconds
OK_PING = 0.3     # seconds

SERVO_PIN = 25 # control pin of servo
MIN_ANGLE = 30
MAX_ANGLE = 150

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 100) # start PWM at 100 Hz
pwm.start(0)

squid = Squid(18, 23, 24)

def map_ping_to_angle(ping_time):
    # ping timeout of 1000 ms sets maximum
    # ping min of 0
    # Fast ping needle over to the right
    angle = ping_time * (MAX_ANGLE - MIN_ANGLE) + MIN_ANGLE
    if angle > MAX_ANGLE :
        angle = MAX_ANGLE
    if angle < MIN_ANGLE :
        angle = MIN_ANGLE
    return angle

# Set the servo to the angle specified
def set_angle(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.2); # give the arm time to move
    pwm.ChangeDutyCycle(0) # stop servo jitter

def ping(hostname):
    try:
        output = subprocess.check_output("ping -c 1 -W 1 " + hostname, shell=True)
        return float(output.split('/')[5]) / 1000.0
    except:
        return -1

try:
    while True:
        p = ping(HOSTNAME)
        # p = input("ping=")  # Use for testing
        print(p)
        set_angle(map_ping_to_angle(p))
    	if p == -1 :
        	squid.set_color(BLUE)
    	elif p < GOOD_PING:
        	squid.set_color(GREEN)
    	elif p < OK_PING:
        	squid.set_color((50, 15, 0)) # Orange
    	else:
        	squid.set_color(RED)
    	time.sleep(PING_PERIOD)
finally:
	GPIO.cleanup()
    