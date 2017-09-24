from gpiozero import LightSensor

ldr = LightSensor(4)

while True:
    print(ldr.value)
