import RPi.GPIO as GPIO
import time
import os, json
import ibmiotf.application
import uuid

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

client = None

def myCommandCallback(cmd):
    if cmd.event == "light":
        payload = json.loads(cmd.payload)
        command = payload["command"]
        print command
        if command == "on":
            GPIO.output(17, True)
        elif command == "off":
            GPIO.output(17, False)

try:
    options = ibmiotf.application.ParseConfigFile("/home/pi/device.cfg")
    options["deviceId"] = options["id"]
    options["id"] = "aaa" + options["id"]
    client = ibmiotf.application.Client(options)
    client.connect()
    client.deviceEventCallback = myCommandCallback
    client.subscribeToDeviceEvents(event="light")

    while True:
        GPIO.wait_for_edge(18, GPIO.FALLING)
        print "Button Pushed"
        myData = {'buttonPushed' : True}
        client.publishEvent("raspberrypi", options["deviceId"], "input", "json", myData)
        time.sleep(0.2)

except ibmiotf.ConnectionException  as e:
    print e

