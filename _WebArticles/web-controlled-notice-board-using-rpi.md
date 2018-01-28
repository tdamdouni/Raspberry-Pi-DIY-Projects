# Web Controlled Notice Board Using RPi

_Captured: 2017-11-04 at 21:53 from [www.hackster.io](https://www.hackster.io/ruchir1674/web-controlled-notice-board-using-rpi-cd452d)_

![Web Controlled Notice Board Using RPi](https://hackster.imgix.net/uploads/attachments/371149/web-controlled-notice-board-using-raspberry-pi-block-diagram_uje9wBh7a4.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

In this I have shown how to send the message from web browser to the LCD which is connected to Raspberry Pi. As message is sent through the web browser, so it can be sent using Computer, smart phone or tablet.

In web controlled notice board, I have created a local web server for demonstration. At the Raspberry Pi, we have used 16x2 LCD to display message and Flask for receiving the message over network. Whenever Raspberry Pi receives any wireless message from Web browser, it displays on the LCD.

![](https://hackster.imgix.net/uploads/attachments/371151/web-controlled-notice-board-using-raspberry-pi-block-diagram_RtB9AYlMhB.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Flask is a micro framework for Python.Flask depends on two external libraries:

[Jinja2 ](http://jinja.pocoo.org/)template engine and the [Werkzeug ](http://werkzeug.pocoo.org/)WSGI toolkit. To install Flask use pip:
    
    
    pip install Flask 
    

Connection of RPi with LCD

LCD RPi

RS => pin 18 (GPIO)

RW => GND

EN => pin 23

D4 => pin 24

D5 => pin 16

D6 => pin 20

D7 => pin 21

![](https://hackster.imgix.net/uploads/attachments/371090/web-controlled-notice-board-using-raspberry-pi-circuit-diagram_frI76GE7kG.png?auto=compress%2Cformat&w=680&h=510&fit=max)

![](https://hackster.imgix.net/uploads/attachments/371100/image_IXK0oeMFJR.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Make an empty python file (test.py)

======================================================================

*******************************************************************************************************

from flask import Flask

from flask import render_template, request

import RPi.GPIO as gpio

import os, time

app = Flask(__name__)

RS =18

EN =23

D4 =24

D5 =16

D6 =20

D7 =21

HIGH=1

LOW=0

OUTPUT=1

INPUT=0

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)

gpio.setup(RS, gpio.OUT)

gpio.setup(EN, gpio.OUT)

gpio.setup(D4, gpio.OUT)

gpio.setup(D5, gpio.OUT)

gpio.setup(D6, gpio.OUT)

gpio.setup(D7, gpio.OUT)

def begin():

lcdcmd(0x33)

lcdcmd(0x32)

lcdcmd(0x06)

lcdcmd(0x0C)

lcdcmd(0x28)

lcdcmd(0x01)

time.sleep(0.0005)

def lcdcmd(ch):

gpio.output(RS, 0)

gpio.output(D4, 0)

gpio.output(D5, 0)

gpio.output(D6, 0)

gpio.output(D7, 0)

if ch&0x10==0x10:

gpio.output(D4, 1)

if ch&0x20==0x20:

gpio.output(D5, 1)

if ch&0x40==0x40:

gpio.output(D6, 1)

if ch&0x80==0x80:

gpio.output(D7, 1)

gpio.output(EN, 1)

time.sleep(0.0005)

gpio.output(EN, 0)

# Low bits

gpio.output(D4, 0)

gpio.output(D5, 0)

gpio.output(D6, 0)

gpio.output(D7, 0)

if ch&0x01==0x01:

gpio.output(D4, 1)

if ch&0x02==0x02:

gpio.output(D5, 1)

if ch&0x04==0x04:

gpio.output(D6, 1)

if ch&0x08==0x08:

gpio.output(D7, 1)

gpio.output(EN, 1)

time.sleep(0.0005)

gpio.output(EN, 0)

def lcdwrite(ch):

gpio.output(RS, 1)

gpio.output(D4, 0)

gpio.output(D5, 0)

gpio.output(D6, 0)

gpio.output(D7, 0)

if ch&0x10==0x10:

gpio.output(D4, 1)

if ch&0x20==0x20:

gpio.output(D5, 1)

if ch&0x40==0x40:

gpio.output(D6, 1)

if ch&0x80==0x80:

gpio.output(D7, 1)

gpio.output(EN, 1)

time.sleep(0.0005)

gpio.output(EN, 0)

# Low bits

gpio.output(D4, 0)

gpio.output(D5, 0)

gpio.output(D6, 0)

gpio.output(D7, 0)

if ch&0x01==0x01:

gpio.output(D4, 1)

if ch&0x02==0x02:

gpio.output(D5, 1)

if ch&0x04==0x04:

gpio.output(D6, 1)

if ch&0x08==0x08:

gpio.output(D7, 1)

gpio.output(EN, 1)

time.sleep(0.0005)

gpio.output(EN, 0)

def lcdprint(Str):

l=0;

l=len(Str)

for i in range(l):

lcdwrite(ord(Str[i]))

begin()

lcdprint("Welcome")

lcdcmd(0xc0)

lcdprint("Ruchir")

time.sleep(5)

@app.route("/")

def index():

return render_template('index.html')

@app.route("/change", methods=['POST'])

def change():

if request.method == 'POST':

# Getting the value from the webpage

data1 = request.form['lcd']

lcdcmd(0x01)

lcdprint(data1)

return render_template('index.html', value=data1)

if __name__ == "__main__":

app.debug = True

app.run('0.0.0.0', port=5000,debug=True)

=====================================================================

*****************************************************************************************************

def lcd_init() function is used to initialize LCD in four bit mode, def lcdcmd(ch) function is used for sending command to LCD, def lcddata(ch) function is used for sending data to LCD and def lcdstring(Str) function is used to send data string to LCD.

Make html file (index.html)

======================================================================

******************************************************************************************************

<h1>Web Control Notice Board</h1>

</div> <div data-role="content">

<form method="post" action="change">

<label for="slider-1">Notice Message:</label>

<input type="text" name="lcd" id="lcd" />

<br />

<input type="submit" value="Submit" />

</form>

{% if value %}

<p>Notice Submitted Successfully: {{ value }}</p>

{% endif %}

</div>

=======================================================================

*********************************************************************************************************

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

![Web controlled notice board using raspberry pi circuit diagram rfgycrbxtw](https://halckemy.s3.amazonaws.com/uploads/attachments/371137/web-controlled-notice-board-using-raspberry-pi-circuit-diagram_rfGyCrBXTW.png)
    
    
    app = Flask(__name__)
    
    
    gpio.setup(RS, gpio.OUT)
    gpio.setup(EN, gpio.OUT)
    gpio.setup(D4, gpio.OUT)
    gpio.setup(D5, gpio.OUT)
    gpio.setup(D6, gpio.OUT)
    gpio.setup(D7, gpio.OUT)
    
     
    def lcdcmd(ch): 
      gpio.output(D4, 0)
      gpio.output(D5, 0)
      gpio.output(D6, 0)
      gpio.output(D7, 0)
    
      gpio.output(D4, 0)
      gpio.output(D5, 0)
      gpio.output(D6, 0)
      gpio.output(D7, 0)
      
      gpio.output(D4, 0)
      gpio.output(D5, 0)
      gpio.output(D6, 0)
      gpio.output(D7, 0)
      gpio.output(D4, 0)
      gpio.output(D5, 0)
      gpio.output(D6, 0)
      gpio.output(D7, 0)
     
      for i in range(l):
        lcdwrite(ord(Str[i]))
    @app.route("/change", methods=['POST'])
       data1 = request.form['lcd']
     return render_template('index.html', value=data1)
        app.run('0.0.0.0', port=5000,debug=True)
    
