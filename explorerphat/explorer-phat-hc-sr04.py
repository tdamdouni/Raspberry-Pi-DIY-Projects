# https://forums.pimoroni.com/t/unreliable-hc-sr04-with-explorer-hat-pro/641/56

import RPi.GPIO as GPIO
import time
import explorerhat

GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 23

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(1)

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)
#print "Distance:",distance,"cm"
if distance < 20:
    explorerhat.motor.one.backwards()
    explorerhat.motor.two.forwards()
else:
    explorerhat.motor.one.forwards()
    explorerhat.motor.two.forwards()


time.sleep(1)
GPIO.cleanup()
