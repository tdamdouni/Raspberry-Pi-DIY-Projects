from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer

logger = Streamer(bucket_name="Sense Hat Environment Stream", access_key="zLahwAUqKbNKv6YvuT5JuO58EiUOavDa")

sense = SenseHat()
sense.clear()
var = 14400

O = (0, 255, 0) # Green
X = (0, 0, 0) # Black

creeper_pixels = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, X, X, O, O, X, X, O,
    O, X, X, O, O, X, X, O,
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O
]

black_pixels = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X
]

while var > 0:
  temp = sense.get_temperature()
  temp = round(temp, 1)
  logger.log("Teperature C",temp)
  humidity = sense.get_humidity()
  humidity = round(humidity, 1)
  logger.log("Humidity :",humidity)
  pressure = sense.get_pressure()
  pressure = round(pressure, 1)
  logger.log("Pressure:",pressure)
  var = var -1
  logger.log("Seconds Until Script Exit",var)
  sense.set_pixels(creeper_pixels)
  time.sleep(5)
  sense.set_pixels(black_pixels)
  time.sleep(25)
  sense.clear()
  if var == 0:
    sys.exit()
