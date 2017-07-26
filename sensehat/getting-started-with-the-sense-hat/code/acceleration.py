from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
  x, y, z = sense.get_accelerometer_raw().values()

  x = round(x, 0)
  y = round(y, 0)
  z = round(z, 0)

  print("x=%s, y=%s, z=%s" % (x, y, z))
  time.sleep(0.1)
