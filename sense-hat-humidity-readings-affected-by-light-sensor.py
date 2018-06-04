# https://forums.pimoroni.com/t/sense-hat-sensor-wierdness/7573

import os
import time, datetime
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
        
sense = SenseHat()
sense.set_rotation(180)
sense.set_imu_config(False, False, False)
sense.low_light = True

s=(0.065) # scroll speed
w=(0) # color all white toggle
x=(2) #shutdown variable

# is really stick down
def pushed_up(event):
    if event.action == ACTION_PRESSED:
       sense.low_light = True
        
# is really stick up
def pushed_down(event):
    if event.action == ACTION_PRESSED:
       sense.low_light = False

#is really stick right
def pushed_left(event):
    global w
    if event.action == ACTION_PRESSED:
        w = (255)
        
# is really stick left
def pushed_right(event):
    global w
    if event.action == ACTION_PRESSED:
        w = (0)

def pushed_middle(event):
    global x
    if event.action == ACTION_PRESSED:
        x = 0

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle

while True:

    dateString = "%A %B %-d %-I:%M:%p"
    msg = "It is %s" % (datetime.datetime.now().strftime(dateString))
    sense.show_message(msg, scroll_speed=s, text_colour=(w, 255, 255))

    t = sense.get_temperature()
    t = round(t)
          
    if t <= 0: 
        tc = [w, w, 255]  # Blue
    elif t > 0 and t < 13:
        tc = [255, 255, w]  # Yellow
    elif t >= 13 and t <= 25:
        tc = [w, 255, w]  # Green
    elif t > 25:
        tc = [255, w, w]  # Red                 
    msg = "and %sc" % (t)
    sense.show_message(msg, scroll_speed=s, text_colour=tc)

    h = sense.get_humidity()
    h = round(h)

    if h < 0:
        h = 0

    if h > 100:
        h = 100

    if h < 30:
        hc = [255, w, w]  # Red
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)
    elif h >= 30 and h <= 60:
        hc = [w, 255, w]  # Green
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)
    elif h > 60 and h < 80:
        hc = [255, 255, w]  # Yellow
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)
    elif h >= 80:
        hc = [255, w, w]  # Red
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)

    p = sense.get_pressure()
    p = round(p)
        
    if p > 0 and p < 985:
        pc = [255, w, w]  # Red
        msg = "- Barometer is Very Low @ %smb - Storm Watch" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 985 and p < 1005:
        pc = [255, 255, w]  # Yellow
        msg = "- Barometer is Low @ %smb - Possible Percipitation" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 1005 and p < 1025:
        pc = [w, 255, w]  # Green
        msg = "- Barometer is Mid Range @ %smb" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 1025 and p < 1050:
        pc = [w, w, 255]  # Blue
        msg = "- Barometer is High @ %smb" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 1050:
        pc = [255, w, w]  # Red
        msg = "- Barometer is Very High @ %smb - Expect Dry Conditions" % (p) 
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
        
    if x == 0:
        sense.clear()
        os.system("sudo shutdown now -P")
        time.sleep(30)
    elif x == 1:
        sense.clear()
        raise SystemExit
        time.sleep(30)

# Last edited on April 19th 2018
# run sudo crontab -e
# add
# @reboot python3 /home/pi/THP.py &