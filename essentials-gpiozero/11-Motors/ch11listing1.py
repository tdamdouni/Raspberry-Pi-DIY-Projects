from gpiozero import Motor
from time import sleep

motor = Motor(forward=8, backward=7)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)