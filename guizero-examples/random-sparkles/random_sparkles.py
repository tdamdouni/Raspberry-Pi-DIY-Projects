from guizero import App, Text, Slider
from sense_hat import SenseHat  # or use sense_emu
from random import randint
from threading import Thread

sense = SenseHat()
app = App("Random Sparkles", width=170, height=150, layout="grid")

def values():
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, rs.get())
    g = randint(0, gs.get())
    b = randint(0, bs.get())
    return x, y, r, g, b

def update_display():
    while True:
        sense.set_pixel(*values())

low = 1
high = 255

Text(app, "R", grid=[0, 0])
rs = Slider(app, start=low, end=high, grid=[1, 0], horizontal=False)
rs.set(high)
Text(app, "G", grid=[0, 1])
gs = Slider(app, start=low, end=high, grid=[1, 1], horizontal=False)
gs.set(high)
Text(app, "B", grid=[0, 2])
bs = Slider(app, start=low, end=high, grid=[1, 2], horizontal=False)
bs.set(high)

t = Thread(target=update_display)
t.start()

app.display()
