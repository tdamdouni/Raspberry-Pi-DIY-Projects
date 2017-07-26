from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
  x, y, z = sense.get_accelerometer_raw().values()

  x = abs(x)
  y = abs(y)
  z = abs(z)

  if x > 1 or y > 1 or z > 1:
      sense.show_letter("!", text_colour=[255,0,0])
  else:
      sense.clear()
  time.sleep(0.1)
