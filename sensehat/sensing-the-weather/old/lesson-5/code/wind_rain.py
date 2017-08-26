#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, math

wind_pin = 5
rain_pin = 6
wind_count = 0
rain_count = 0

def bucket_tipped(channel):
    global rain_count
    rain_count = rain_count + 1
    print (rain_count * 0.2794)

def calculate_speed(r_cm, time_sec):
    global wind_count
    circ_cm = (2 * math.pi) * r_cm
    rot = wind_count / 2.0
    dist_km = (circ_cm * rot) / 100000.0 # convert to kilometres
    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * 3600 # convert to distance per hour
    return km_per_hour * 1.18

def spin(channel):
    global rain_count
    rain_count += 1
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(wind_pin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(rain_pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(wind_pin, GPIO.FALLING, callback=spin)
GPIO.add_event_detect(rain_pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

interval = 5

while True:
    wind_count = 0
    time.sleep(interval)
    print ("Windspeed: ",calculate_speed(9.0, interval), "kph")
    print ("Rainfall: ",rain_count * 0.2794,"mm")
