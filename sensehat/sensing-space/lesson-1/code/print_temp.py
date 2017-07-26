#Import the sense_hat and time libraries
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

    #Set the total time and the pause between temperature readings
pause = 10
total_time = 100

    #For 100 seconds, print the temperature every 10 seconds
for current_time in range(0, total_time, pause):
    temperature = sense.get_temperature()
    print(temperature)
    sleep(pause)
