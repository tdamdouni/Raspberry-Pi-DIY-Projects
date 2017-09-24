from gpiozero import Robot
from time import sleep

robot = Robot(left=(8, 7), right=(10, 9))

for i in range(4):
    robot.forward()
    sleep(1)
    robot.right()
    sleep(0.2)