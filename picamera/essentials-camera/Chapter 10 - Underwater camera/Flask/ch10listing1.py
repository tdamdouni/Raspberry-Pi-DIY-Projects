from flask import Flask, render_template,request, redirect, url_for
from envirophat import light,weather
import time, os, shutil
from picamera import PiCamera
from datetime import datetime, timedelta
from threading import Thread

app = Flask(__name__)

def timelapse():  # continuous shooting
    cam = PiCamera()
    cam.resolution = (1640,922)
    for filename in cam.capture_continuous('img{timestamp:%Y%m%d-%H%M%S}.jpg'):
        print('snap taken')
        print(btn1,btn2)
        shutil.copyfile(filename,'/home/pi/Flask/static/latest.jpg')
        if btn1 != 's':
            break
    cam.close()
    print('timelapse thread stopped')

def video(): # record a video
    cam = PiCamera()
    t='{:%Y%m%d-%H%M%S}'.format(datetime.now())
    cam.resolution = (1920,1080)
    cam.start_recording('vid'+t+'.h264')
    while btn1 == 'v':
        print(btn1,btn2)
        pass
    cam.stop_recording()
    cam.close()
    print('video thread stopped')

def snapstart(): # take pictures on demand
    cam = PiCamera()
    cam.resolution = (1640,922)
    print('entered snapshot mode')
    global btn2
    while btn1 == 'q':
        time.sleep(0.1)
        if btn2 == 'a':
            print('taken snap: btn2 =' + btn2)
            t='{:%Y%m%d-%H%M%S}'.format(datetime.now())
            filename = 'snap'+t+'.jpg'
            cam.capture(filename)
            shutil.copyfile(filename,'/home/pi/Flask/static/latest.jpg')
            btn2 = 'o'
            print('btn2 =' + btn2)

    cam.close()
    print('exiting snaphot mode')


# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button

@app.route('/', methods = ['POST','GET'])
def hello_world():

    status = 'off'
    global btn1
    btn1 = 'o'
    global btn2
    btn2 = 'o'
    message = 'All good '

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['submit'] == 'Video':
            print('BP: Recording video')
            status = 'video'
            btn1 = 'v'
            t2 = Thread(target=video)
            t2.start()
            message = 'All good'
        elif request.form['submit'] == 'Video Off':
            print('BP: Video off')
            status = 'Idle'
            btn1 = 'o'
            message = 'All good'
        elif request.form['submit'] == 'Stills':
            print('BP: Recording stills')
            btn1 = 's'
            t1 = Thread(target=timelapse)
            t1.start()
            status = 'stills'
            message = 'All good'
        elif request.form['submit'] == 'Stills Off':
            print('BP: stills off')
            status = 'Idle'
            btn1 = 'o'
            message = 'All good'
        elif request.form['submit'] == 'QuickSnap':
            print('BP: QuickSnap')
            status = 'Ready to snap'
            btn1 = 'q'
            t3 = Thread(target=snapstart)
            t3.start()
            message = 'All good'
        elif request.form['submit'] == 'QuickSnap Off':
            print('BP:QuickSnap off')
            status = 'Idle'
            btn1 = 'o'
            message = 'All good'
        elif request.form['submit'] == 'Take':
            print('BP:Take')
            status = 'Snapshot mode'
            btn1 = 'q'
            btn2 = 'a'
            message = 'All good'
        elif request.form['submit'] == '_Take_':
            print('BP:Take error')
            status = 'Error'
            message = 'Enable QuickSnap first'
            btn1 = 'o'
        else:
            pass

    temp = round(weather.temperature(),2) #temperature from enviro pHat
    press = int(weather.pressure()) # pressure
    lux = light.light() # light levels
    df = os.statvfs('/') # check if we're running out of disk space
    df_size = df.f_frsize * df.f_blocks
    df_avail = df.f_frsize * df.f_bfree
    df_pc = round(100 -(100 * df_avail/df_size),1)
    print(btn1, btn2)

    # the default page to display will be our template with our template variables
    return render_template('index2.html', message= message, status=status, temp=temp, press=press, lux=lux, df_pc=df_pc, btn1 = btn1)

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    # specify port 80 rather than default 5000
    app.run(host='0.0.0.0',port=80,debug=True)