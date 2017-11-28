import RPi.GPIO as GPIO 
import time 
import explorerhat

GPIO.setmode(GPIO.BCM) 

TRIG = 31 
ECHO = 23 

print "Distance Measurement In Progress" 

GPIO.setup(TRIG,GPIO.OUT) 
GPIO.setup(ECHO,GPIO.IN) 

GPIO.output(TRIG, False) 
print "Waiting For Sensor To Settle" 
time.sleep(1) 

while True:
	GPIO.output(TRIG, True) 
	time.sleep(0.00001) 
	GPIO.output(TRIG, False) 
	
	while GPIO.input(ECHO)==0:
	  pulse_start = time.time() 
	
	while GPIO.input(ECHO)==1:
	  pulse_end = time.time() 
	
	pulse_duration = pulse_end - pulse_start 
	
	distance = pulse_duration * 17150 
	
	distance = round(distance, 2) 
	
	if distance < 10:
		explorerhat.light.off()
		explorerhat.light[0].on()
		explorerhat.light[1].on()
		explorerhat.light[2].on()
		explorerhat.light[3].on()
	elif distance < 20:
		explorerhat.light.off()
		explorerhat.light[0].on()
		explorerhat.light[1].on()
		explorerhat.light[2].on()
	elif distance < 30:
		explorerhat.light.off()
		explorerhat.light[0].on()
		explorerhat.light[1].on()
	elif distance < 40:
		explorerhat.light.off()
		explorerhat.light[0].on()
	else:
		explorerhat.light.off()
		
	print "Distance:",distance,"cm" 
	
	time.sleep(1)



GPIO.cleanup()