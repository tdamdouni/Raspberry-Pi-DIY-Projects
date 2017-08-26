from gpiozero import DigitalInputDevice

rain_sensor = DigitalInputDevice(6)
BUCKET_SIZE = 0.2794
count = 0

current_state = True
previous_state = True

while True:
	current_state = rain_sensor.value

	if previous_state == True and current_state == False:
	    count = count + 1
	    print ( count * BUCKET_SIZE )

	previous_state = current_state