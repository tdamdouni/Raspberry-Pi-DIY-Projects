from guizero import *
from gpiozero import TrafficHat
from threading import Thread

th = TrafficHat(pwm=True)

app = App("Traffic HAT controller", layout="grid")

def scaled(v):
    return v / 100

def update_lights():
    while True:
        yield (scaled(red.get()), scaled(amber.get()), scaled(green.get()))

def update_button():
    while True:
        button_pressed.value.set(th.button.value)
        button_held.value.set(th.button.is_held)

Text(app, "Lights", grid=[0, 0])
Text(app, "Red", grid=[0, 1])
red = Slider(app, start=100, end=0, grid=[1, 1], horizontal=False)
Text(app, "Amber", grid=[0, 2])
amber = Slider(app, start=100, end=0, grid=[1, 2], horizontal=False)
Text(app, "Green", grid=[0, 3])
green = Slider(app, start=100, end=0, grid=[1, 3], horizontal=False)

Text(app, "Buzzer", grid=[2, 0])
PushButton(app, command=th.buzzer.on, text="on", grid=[2, 1])
PushButton(app, command=th.buzzer.off, text="off", grid=[2, 2])
PushButton(app, command=th.buzzer.beep, text="beep", grid=[2, 3])

Text(app, "Button", grid=[3, 0])
button_pressed = CheckBox(app, "Pushed", grid=[3, 1])
button_held = CheckBox(app, "Held", grid=[3, 2])

th.lights.source = update_lights()

thread = Thread(target=update_button)
thread.start()

app.display()
