from sense_hat import SenseHat
from time import sleep
from time import asctime

sense = SenseHat()

temp = round(sense.get_temperature_from_pressure()*1.8 +32)
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temperature is %d F Humidity is %d percent Pressure is %d mbars' %(temp,humidity,pressure)


sense.show_message(message, scroll_speed=(0.08),text_colour=[200,0,200], back_colour= [0,0,200])
sense.clear()



while True:
    log = open("weather.txt", "a")
    now = str(asctime())
    log.write(now + " " + message + "\n")
    print(message)
    log.close()
    sleep(30)
















    

