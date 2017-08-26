import Adafruit_BMP.BMP085 as bmp
from time import strftime

bmpsensor = bmp.BMP085()

current_date = strftime("%d/%m/%y")
current_time = strftime("%H:%M")
current_pressure = bmpsensor.get_pressure()
