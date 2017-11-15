# https://forums.pimoroni.com/t/pimoroni-explorer-hat-pro-velleman-hc-sr05-ultrasonic-sensor/6262/6

import RPi.GPIO as GPIO
import time
import explorerhat

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

TRIG = 31
ECHO = 16

print (“Distance Measurement In Progress”)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print(“Waiting For Sensor To Settle”)
time.sleep(1)

while True:
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print ("Distance:",distance,"cm")

time.sleep(1)
GPIO.cleanup()
