from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

# Change these for your setup.
PASSWORD = 'letmein'
MAX_ATTEMPTS = 5  # before you are locked out
OPEN_TIME = 5     # number of seconds for lck to stay open
IP_ADDRESS = '192.168.1.14' # of your Pi

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
LOCK_PIN = 18
GPIO.setup(LOCK_PIN, GPIO.OUT)

# Initialize the number of failed login attempts to 0
attempts = 0;

# Unlock the door by setting LOCK_PIN high for
# OPEN_TIME seconds
def unlock_door():
    GPIO.output(LOCK_PIN, True)
    time.sleep(OPEN_TIME)
    GPIO.output(LOCK_PIN, False)

# Handler for the home page
@route('/')
def index(name='time'):
    return template('home.tpl')
    
# Handler for the 'unlock' page    
@route('/unlock', method='POST')
def new_item():
    global attempts
    # Get the password entered in the password field of the form
    pwd = request.POST.get('password', '').strip()
    # check to see if tehre have been too many failed attemts
    if attempts >= MAX_ATTEMPTS:
        return template('lockout.tpl')
    # unlock the door if the password is correct
    if pwd == PASSWORD:
        attempts = 0
        unlock_door()
        return template('opened.tpl')
    else:
        attempts += 1
        return template('failed.tpl')
        
# Start teh webserver running on port 80
try: 
    run(host=IP_ADDRESS, port=80)
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup()
