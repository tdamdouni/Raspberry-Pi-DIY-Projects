# http://forums.pimoroni.com/t/pi-zero-explorer-phat-sensor-not-working-on-battery-power/3847/6

# https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

import explorerhat
import time

explorerhat.output.one.off()
time.sleep(2)

while True:

    explorerhat.output.one.on()
    time.sleep(0.00001)
    explorerhat.output.one.off()

    while explorerhat.input.one.read() == 0:
        sendTime = time.time()

    while explorerhat.input.one.read() == 1:
        endTime = time.time()

    duration = endTime - sendTime

    distance = duration * 17150

    #print "Object distance: ",distance,"cm"
    if distance < 20:
        explorerhat.motor.one.backwards()
        explorerhat.motor.two.forwards()
    else:
        explorerhat.motor.one.forwards()
        explorerhat.motor.two.forwards()
