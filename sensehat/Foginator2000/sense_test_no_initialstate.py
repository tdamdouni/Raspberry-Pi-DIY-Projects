from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()

var = 30

while var > 0:
  temp = sense.get_temperature()
  temp = round(temp, 1)
  print("Teperature C",temp)
  humidity = sense.get_humidity()
  humidity = round(humidity, 1)
  print("Humidity :",humidity)
  pressure = sense.get_pressure()
  pressure = round(pressure, 1)
  print("Pressure:",pressure)
  time.sleep(1)
  var = var -1
  if var == 0:
    sys.exit()
