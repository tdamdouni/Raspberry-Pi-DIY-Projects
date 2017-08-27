from flask import Flask, render_template,request, redirect, url_for
import time, os, shutil
from threading import Thread
from mote import Mote
from colorsys import hsv_to_rgb
import random
import struct

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

app = Flask(__name__)

def hextorgb(hex):
    return struct.unpack('BBB',bytes.fromhex(str(hex)[1:]))

def rainbow():
    while True:
        h = time.time() * 50
        for channel in range(4):
            for pixel in range(16):
                hue = (h + (channel * 64) + (pixel * 4)) % 360
                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                mote.set_pixel(channel + 1, pixel, r, g, b)
        mote.show()
        if btn1 != 'r':
            mote.clear()
            mote.show()
            break
        time.sleep(0.01)

def alert():
    while True:
        for channel in range(4):
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, 255, 0, 0)
            mote.show()
        time.sleep(0.5)
        if btn1 != 'v':
            mote.clear()
            mote.show()
            break
        for channel in range(4):
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, 0, 0, 0)
            mote.show()
        time.sleep(0.5)
        if btn1 != 'v':
            mote.clear()
            mote.show()
            break

def white():
    while True:
        for channel in range(4):
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, 255, 255, 255)
            mote.show()
        time.sleep(0.5)
        if btn1 != 'w':
            mote.clear()
            mote.show()
            break

def sunny():
    while True:
        for channel in range(4):
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, 255, 128, 0)
            mote.show()
        time.sleep(0.5)
        if btn1 != 's':
            mote.clear()
            mote.show()
            break

def sparkles():
    while True:
        for channel in range(4):
            for pixel in range(16):
                r_r = random.randint(0,200)
                g_r = random.randint(0,200)
                b_r = random.randint(0,200)
                mote.set_pixel(channel + 1, pixel, r_r, g_r, b_r)
            mote.show()
        time.sleep(0.2)
        if btn1 != 'p':
            mote.clear()
            mote.show()
            break

def disco():
    colours = [(255,0,0),(0,255,0), (0,0,255), (255,255,0), (255,20,147)]
    while True:
        for channel in range(4):
            rc = random.choice(colours)
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, rc[0], rc[1], rc[2])
            mote.show()
        time.sleep(0.3)
        if btn1 != 'd':
            mote.clear()
            mote.show()
            break

def strobe():
    while True:
        for channel in range(4):
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, 255, 255, 255)
            mote.show()
        time.sleep(0.03)
        if btn1 != 'f':
            mote.clear()
            mote.show()
            break
        for channel in range(4):
            for pixel in range(16):
                mote.set_pixel(channel + 1, pixel, 0, 0, 0)
            mote.show()
        time.sleep(0.03)
        if btn1 != 'f':
            mote.clear()
            mote.show()
            break

def stars():
    while True:
        ran_chans = []
        for y in range(4):
            ran_chans.append(random.randint(1,8))
        ran_pxls = []
        for z in range(2):
            ran_pxls.append(random.randint(0,32))

        for i in range(255):

            for p in ran_pxls:
                if p < 16:
                    for c in ran_chans:
                        if c < 5:
                            mote.set_pixel(c, p, i, i, i)
                time.sleep(0.0005)
                mote.show()
        for i in range(255,0,-1):
            for p in ran_pxls:
                if p < 16:
                    for c in ran_chans:
                        if c < 5:
                            mote.set_pixel(c, p, i, i, i)
                time.sleep(0.0005)
                mote.show()
        time.sleep(0.1)
        if btn1 != 't':
            mote.clear()
            mote.show()
            break

def larson():
    while True:

        for pixel in range(16):
            for channel in range(4):
                mote.set_pixel(channel +1, pixel, 255,0,0)
            mote.show()
            time.sleep(0.05)
            mote.clear()
            mote.show()
        for pixel in range(15,0,-1):
            for channel in range(4):
                mote.set_pixel(channel +1, pixel, 255,0,0)
            mote.show()
            time.sleep(0.05)
            mote.clear()
            mote.show()

        if btn1 != 'k':
            mote.clear()
            mote.show()
            break

def setcol(r,g,b,motes):
    while True:
        for channel in motes:
            for pixel in range(16):
                mote.set_pixel(channel, pixel, r,g, b)
            mote.show()
        time.sleep(0.5)
        if btn1 != 'c':
            mote.clear()
            mote.show()
            break

def pickcol(r,g,b,motes):
    while True:
        for channel in motes:
            for pixel in range(16):
                mote.set_pixel(channel, pixel, r,g, b)
            mote.show()
        time.sleep(0.5)
        if btn1 != 'z':
            mote.clear()
            mote.show()
            break

@app.route('/', methods = ['POST','GET'])
def hello_world():

    status = 'off'
    global btn1
    btn1 = 'o'
    mote1 = 'off'
    mote2 = 'off'
    mote3 = 'off'
    mote4 = 'off'
    set_r = 0
    set_g = 0
    set_b = 0
    picker = '#000000'

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['submit'] == 'RED ALERT':
            status = 'Red Alert'
            btn1 = 'v'
            t2 = Thread(target=alert)
            t2.start()
        elif request.form['submit'] == 'Red Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Rainbow':
            status = 'Rainbow'
            btn1 = 'r'
            t3 = Thread(target=rainbow)
            t3.start()
        elif request.form['submit'] == 'Rainbow Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'White':
            status = 'White'
            btn1 = 'w'
            t3 = Thread(target=white)
            t3.start()
        elif request.form['submit'] == 'White Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Sunny':
            status = 'Sunny'
            btn1 = 's'
            t3 = Thread(target=sunny)
            t3.start()
        elif request.form['submit'] == 'Sun Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Disco':
            status = 'Disco'
            btn1 = 'd'
            t3 = Thread(target=disco)
            t3.start()
        elif request.form['submit'] == 'Disco Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Strobe':
            status = 'Strobe'
            btn1 = 'f'
            t3 = Thread(target=strobe)
            t3.start()
        elif request.form['submit'] == 'Strobe Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Sparkles':
            status = 'Sparkles'
            btn1 = 'p'
            t3 = Thread(target=sparkles)
            t3.start()
        elif request.form['submit'] == 'Sparkles Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Stars':
            status = 'Stars'
            btn1 = 't'
            t3 = Thread(target=stars)
            t3.start()
        elif request.form['submit'] == 'Stars Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Larson':
            status = 'Larson'
            btn1 = 'k'
            t3 = Thread(target=larson)
            t3.start()
        elif request.form['submit'] == 'Larson Off':
            status = 'Idle'
            btn1 = 'o'
        elif request.form['submit'] == 'Manual':
            status = 'manual'
            btn1 = 'c'
            motes = []
            set_r = int((request.form['slider_r']))
            set_g =int((request.form['slider_g']))
            set_b =int((request.form['slider_b']))
            if request.form.get('motes1') == 'on':
                motes.append(1)
                mote1 = 'on'
            if request.form.get('motes2') == 'on':
                motes.append(2)
                mote2 = 'on'
            if request.form.get('motes3') == 'on':
                motes.append(3)
                mote3 = 'on'
            if request.form.get('motes4') == 'on':
                motes.append(4)
                mote4 = 'on'
            t3 = Thread(target=setcol, kwargs={'r': set_r,'g': set_g, 'b': set_b, 'motes':motes })
            t3.start()
        elif request.form['submit'] == 'Manual Off':
            status = 'Idle'
            btn1 = 'o'
            motes = []
            set_r = int((request.form['slider_r']))
            set_g =int((request.form['slider_g']))
            set_b =int((request.form['slider_b']))
            if request.form.get('motes1') == 'on':
                motes.append(1)
                mote1 = 'on'
            if request.form.get('motes2') == 'on':
                motes.append(2)
                mote2 = 'on'
            if request.form.get('motes3') == 'on':
                motes.append(3)
                mote3 = 'on'
            if request.form.get('motes4') == 'on':
                motes.append(4)
                mote4 = 'on'
        elif request.form['submit'] == 'Pick Set':
            status = 'Picker'
            btn1 = 'z'
            motes = []
            if request.form.get('motes1') == 'on':
                motes.append(1)
                mote1 = 'on'
            if request.form.get('motes2') == 'on':
                motes.append(2)
                mote2 = 'on'
            if request.form.get('motes3') == 'on':
                motes.append(3)
                mote3 = 'on'
            if request.form.get('motes4') == 'on':
                motes.append(4)
                mote4 = 'on'
            picker = request.form['colpick']
            rgb = hextorgb(picker)
            set_r = rgb[0]
            set_g = rgb[1]
            set_b = rgb[2]
            t3 = Thread(target=pickcol, kwargs={'r': set_r,'g': set_g, 'b': set_b, 'motes':motes })
            t3.start()
        elif request.form['submit'] == 'Pick Set Off':
            status = 'Idle'
            btn1 = 'o'
            motes = []
            if request.form.get('motes1') == 'on':
                motes.append(1)
                mote1 = 'on'
            if request.form.get('motes2') == 'on':
                motes.append(2)
                mote2 = 'on'
            if request.form.get('motes3') == 'on':
                motes.append(3)
                mote3 = 'on'
            if request.form.get('motes4') == 'on':
                motes.append(4)
                mote4 = 'on'
            picker = request.form['colpick']
            rgb = hextorgb(picker)

    return render_template('index4.html',  status=status, btn1 = btn1,
                                            mote1 = mote1, mote2= mote2,
                                            mote3 = mote3, mote4 = mote4,
                                            slider_r = str(set_r),
                                            slider_g = str(set_g),
                                            slider_b = str(set_b),
                                            picker = picker
                                             )

if __name__ == "__main__":

    app.run(host='0.0.0.0',debug=True)
