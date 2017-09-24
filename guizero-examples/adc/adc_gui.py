from gpiozero import MCP3008
from guizero import App, Slider
from threading import Thread

app = App("ADC GUI")
adc = [MCP3008(i) for i in range(8)]

sliders = [Slider(app, 0, 100) for pot in adc]

def update():
    while True:
        for slider, pot in zip(sliders, adc):
            slider.set(pot.value * 100)

thread = Thread(target=update)
thread.start()

app.display()
