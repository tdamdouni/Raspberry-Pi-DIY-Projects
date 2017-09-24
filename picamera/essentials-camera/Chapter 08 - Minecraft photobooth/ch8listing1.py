from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
camera = PiCamera()

mc.postToChat("Find the photo booth")

camera.start_preview()
sleep(2)
camera.capture('/home/pi/selfie.jpg')
camera.stop_preview()

while True:
	x, y, z = mc.player.getPos()
	
	sleep(3)
	
	if x >= 10.5 and y == 9.0 and z == -44.3:
		mc.postToChat("You're in the photo booth!")
		sleep(1)
		mc.postToChat("Smile!")
		sleep(1)
		camera.start_preview()
		sleep(2)
		camera.capture('/home/pi/selfie.jpg')
		camera.stop_preview()

	sleep(3)
