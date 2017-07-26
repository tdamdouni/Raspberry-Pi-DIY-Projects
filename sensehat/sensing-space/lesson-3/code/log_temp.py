from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
pause = 10
period = 100

#Turn on all LEDs (white)
sense.clear((255,255,255))

#write time and temperature to a csv file
with open('temp_data.html','w') as f:
    for current_time in range(0,period,pause):
        temperature = round(sense.get_temperature(),3)
        string=",".join((str(current_time),str(temperature)))
        f.write(string+"\n")
        sleep(pause)

#Reset the LEDs to off
sense.clear()


