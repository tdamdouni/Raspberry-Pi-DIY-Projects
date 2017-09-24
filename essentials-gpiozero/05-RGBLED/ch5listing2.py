from gpiozero import RGBLED
import psutil, time

myled = RGBLED(14,15,18)

while True:
    cpu = psutil.cpu_percent()
    r = cpu / 100.0
    g = (100 - cpu)/100.0
    b = 0
    myled.color = (r, g, b)
    time.sleep(0.1)
