from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    pitch,roll,yaw = sense.get_orientation().values()
    print("pitch=%s, roll=%s, yaw=%s" % (pitch, yaw, roll))
    time.sleep(0.5)
