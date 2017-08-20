#!/usr/bin/env python

import os
import stat
import threading
import time

import ambience
import colorsys

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

try: 
    #I made a custom unicornhat library for increased brightness...
    import unicornoverdrive as unicorn
except ImportError:
    import unicornhat as unicorn

control_panel = """
    <table cellspacing="0" cellpadding="0" border-collapse="collapse">"""

for y in range(8):
    control_panel += '<tr>'
    for x in range(8):
        control_panel += '<td data-x="' + str(x) + '" data-y="' + str(y) + '" data-hex="000000" style="background-color:#000000;"></td>'
    control_panel += '</tr>'

control_panel += '</table><div class="mc"></div>'

control_panel += """
    <ul class="tools">
        <li data-tool="paint" class="paint selected"><span class="fa fa-paint-brush"></span></li>
        <li data-tool="pick" class="pick"><span class="fa fa-eyedropper"></span></li>
        <li data-tool="lighten" class="lighten"><span class="fa fa-adjust"></span> Lighten</li>
        <li data-tool="darken" class="darken"><span class="fa fa-adjust"></span> Darken</li>
    </ul>"""


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('paint.html')

@app.route('/clear')
def clear():
    s = threading.Thread(None,unicorn.clear)
    s.start()
    return "ok"

@app.route('/show')
def show():
    s = threading.Thread(None,unicorn.show)
    s.start()
    return "ok"

@app.route('/pixel/<x>/<y>/<r>/<g>/<b>')
def set_pixel(x, y, r, g, b):
    x, y, r, g, b = int(x), int(y), int(r), int(g), int(b)
    unicorn.set_pixel(x, y, r, g, b)
    return "ok"

@app.route('/map/<r>/<g>/<b>')
def set_hat(r, g, b):
    r, g, b = int(r), int(g), int(b)
    for x in range(8):
        for y in range(8):
            unicorn.set_pixel(x, y, r, g, b)
    return "ok"

@app.route('/ambience/<r1>/<g1>/<b1>')
def ambient(r1, g1, b1):
    s = threading.Thread(None,unicorn.clear)
    s.start()
    s.join()

    r1, g1, b1 = int(r1), int(g1), int(b1)
    print r1, g1, b1
    cval = colorsys.rgb_to_hsv(r1/255.0, g1/255.0, b1/255.0)
    print cval
    c = int(cval[0]*360.0)

    s = threading.Thread(None, ambience.color_ambient(c))
    s.start()
    return "OK"

if __name__ == "__main__":
    unicorn.brightness(1)
    app.run(host='0.0.0.0', debug=0)

