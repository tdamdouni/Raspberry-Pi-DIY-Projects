import Adafruit_BMP.BMP085 as bmp
from time import strftime, sleep

bmpsensor = bmp.BMP085()

interval = 60*30    # Interval of 30 mins (60 seconds * 30)

while True:
   
    # Take new readings
    current_date = strftime("%d/%m/%y")
    current_time = strftime("%H:%M")
    current_pressure = bmpsensor.get_pressure()

    # Open the file and write the new reading
    f = open("bmp_readings.csv", "a")
    string_to_write = str(current_date) + ", " + str(current_time) + ", " + str(current_pressure) + "\n"
    f.write(string_to_write)
    f.close()

    # Wait for the given amount of time
    sleep(interval)



