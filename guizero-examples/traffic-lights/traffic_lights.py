from guizero import App, Text, PushButton
from gpiozero import TrafficLights

lights = TrafficLights(22, 27, 17)

app = App("Traffic Lights controller", layout="grid")

Text(app, "Red", grid=[0, 0])
PushButton(app, command=lights.red.on, text="on", grid=[0, 1])
PushButton(app, command=lights.red.off, text="off", grid=[0, 2])
PushButton(app, command=lights.red.blink, text="blink", grid=[0, 3])

Text(app, "Amber", grid=[1, 0])
PushButton(app, command=lights.red.on, text="on", grid=[1, 1])
PushButton(app, command=lights.red.off, text="off", grid=[1, 2])
PushButton(app, command=lights.red.blink, text="blink", grid=[1, 3])

Text(app, "Green", grid=[2, 0])
PushButton(app, command=lights.red.on, text="on", grid=[2, 1])
PushButton(app, command=lights.red.off, text="off", grid=[2, 2])
PushButton(app, command=lights.red.blink, text="blink", grid=[2, 3])

Text(app, "All", grid=[3, 0])
PushButton(app, command=lights.red.on, text="on", grid=[3, 1])
PushButton(app, command=lights.red.off, text="off", grid=[3, 2])
PushButton(app, command=lights.red.blink, text="blink", grid=[3, 3])

app.display()
