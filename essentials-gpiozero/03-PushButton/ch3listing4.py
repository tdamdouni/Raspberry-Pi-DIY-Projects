from gpiozero import LED, Button
from time import sleep

led = LED(25)
button = Button(21)

button.wait_for_press()
led.on()
sleep(3)
led.off()