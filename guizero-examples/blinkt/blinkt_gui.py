from blinkt import *
from guizero import *

app = App(title="Blinkt!", layout="grid")

def update_blinkt(v):
    for pixel, rgb in enumerate(sliders):
        r, g, b = (slider.get() for slider in rgb)
        set_pixel(pixel, r, g, b)
    show()

sliders = [
    [Slider(app, command=update_blinkt, start=0, end=255, grid=[pixel, rgb]) for rgb in range(3)]
    for pixel in range(8)
]

app.display()
