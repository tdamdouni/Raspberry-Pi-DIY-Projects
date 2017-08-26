from gpiozero import DigitalInputDevice

wind_speed_sensor = DigitalInputDevice(5)
count = 0

def spin():
    global count
    count = count + 1
    print(count)

wind_speed_sensor.when_activated = spin