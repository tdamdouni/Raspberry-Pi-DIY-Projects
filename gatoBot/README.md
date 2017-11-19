# gatoBot

A web controlled **Raspberry Pi Zero W** robot with live video streaming.

This is something I built in order to bother my cats.

## About Raspberry Pi
Wikipedia:

> The Raspberry Pi is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation to promote the teaching of basic computer science in schools and in developing countries. The original model became far more popular than anticipated, selling outside of its target market for uses such as robotics. Peripherals (including keyboards, mice and cases) are not included with the Raspberry Pi. Some accessories however have been included in several official and unofficial bundles.

[Click here to access the full article](https://en.wikipedia.org/wiki/Raspberry_Pi)

## Main features
- Controlled via web browser.
- Live video streaming.

## Bill of materials
- 1 x Raspberry Pi Zero W board: ~ 10.00 USD.
- 1 x Raspberry Pi compatible camera: ~15.00 USD.
- 1 x 4xAA battery holder: ~1.00 USD.
- 1 x 4.000 mAh USB battery: ~10.00 USD.
- 1 x Robot car chassis with 2 DC motors: ~15.00 USD.
- 1 x L298N dual H bridge DC motor driver: ~4.00 USD.

**Total cost: ~55.00 USD.**

## Schematics

![](https://user-images.githubusercontent.com/22028245/32573518-9223687e-c4ce-11e7-89dd-16900c512cdd.png)

Once you've put everything together, your "robot" will look more or less like this:

![](https://user-images.githubusercontent.com/22028245/32569737-413927ca-c4c2-11e7-825d-7e06fe739141.jpg)

## DC motors direction issues

You may find that the motors are not moving in the direction you expected. If this happens, review the following line in **motors.py** and play with the LOW and HIGH parameters ;)

	def backward():
	        GPIO.output(Motor1A,GPIO.HIGH)
	        GPIO.output(Motor1B,GPIO.LOW)
	        GPIO.output(Motor2A,GPIO.HIGH)
	        GPIO.output(Motor2B,GPIO.LOW)
	
	def forward():
	        GPIO.output(Motor1A,GPIO.LOW)
	        GPIO.output(Motor1B,GPIO.HIGH)
	        GPIO.output(Motor2A,GPIO.LOW)
	        GPIO.output(Motor2B,GPIO.HIGH)
	
	def turnLeft():
	        print("Going Left")
	        GPIO.output(Motor1A,GPIO.HIGH)
	        GPIO.output(Motor1B,GPIO.LOW)
	        GPIO.output(Motor2A,GPIO.LOW)
	        GPIO.output(Motor2B,GPIO.HIGH)
	
	def turnRight():
	        print("Going Right")
	        GPIO.output(Motor1A,GPIO.LOW)
	        GPIO.output(Motor1B,GPIO.HIGH)
	        GPIO.output(Motor2A,GPIO.HIGH)
	        GPIO.output(Motor2B,GPIO.LOW)


## Web interface

Once the Raspberry Pi is up and running, connected to a wifi network and the L298N driver is powered by 4AA batteries, you should be able to control your robot by accessing **http://raspberry_ip:8000/**

![](https://user-images.githubusercontent.com/22028245/32572842-356be6bc-c4cc-11e7-9793-c094f5052fff.jpg)