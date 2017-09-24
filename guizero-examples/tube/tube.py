from tubestatus import Status
from guizero import App, Text, Waffle
from threading import Thread
from time import sleep

app = App("Tube status", layout="grid")

tube = Status()
lines = list(sorted(tube.list_lines()))

[Text(app, line, grid=[y, 0], align="left") for y, line in enumerate(lines)]
waffles = [
    Waffle(app, height=1, width=1, grid=[y, 1]) for y, line in enumerate(lines)
]

def update():
    while True:
        for line, waffle in zip(lines, waffles):
            status = tube.get_status(line)
            color = {
                'Good Service': 'green',
                'Minor Delays': 'orange',
                'Severe Delays': 'red',
                'Part Closure': 'gray',
                'Service Closed': 'black',
            }[status.description]
            waffle.set_all(color)
        sleep(60)

thread = Thread(target=update)
thread.start()

app.display()