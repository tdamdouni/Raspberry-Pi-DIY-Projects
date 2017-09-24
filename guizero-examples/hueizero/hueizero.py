from phue import Bridge
from guizero import *

b = Bridge('192.168.86.22')
lights = list(b.lights)

def light_switches(light_number, on=True):
    light = lights[int(light_number)]
    def light_switch():
        light.on = on
    return light_switch

def dimmer_switches(light_number):
    light = lights[int(light_number)]
    def dimmer_switch(value):
        light.brightness = int(value)
    return dimmer_switch

app = App(title="hueizero", layout="grid")

for i, light in enumerate(lights):
    Text(app, light.name, grid=[0, i]),
    PushButton(app, command=light_switches(i, on=True), text="on", grid=[1, i]),
    PushButton(app, command=light_switches(i, on=False), text="off", grid=[2, i]),
    Slider(app, start=0, end=255, command=dimmer_switches(i),
        grid=[3, i], orient="vertical"
    )

app.display()
