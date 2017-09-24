from gpiozero import LightSensor, Buzzer
from time import sleep

ldr = LightSensor(4)
buzzer = Buzzer(17)

while True:
    sleep(0.1)
    if ldr.value < 0.5:
        buzzer.beep(0.5, 0.5, 8)
        sleep(8)
    else:
        buzzer.off()
