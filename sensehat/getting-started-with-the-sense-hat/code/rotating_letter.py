from sense_hat import SenseHat
sense = SenseHat()
import time

sense.show_letter("J")

while True:
  x, y, z = sense.get_accelerometer_raw().values()

  x = round(x, 0)
  y = round(y, 0)

  if x == -1:
      sense.set_rotation(180)
  elif y == -1:
      sense.set_rotation(90)
  elif y == 1:
      sense.set_rotation(270)
  else:
      sense.set_rotation(0)

  time.sleep(0.1)
