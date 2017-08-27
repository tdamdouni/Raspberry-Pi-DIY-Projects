# Automatic orientation of Sense HAT display

_Captured: 2017-08-26 at 15:00 from [yaab-arduino.blogspot.de](http://yaab-arduino.blogspot.de/2016/08/automatic-orientation-of-sense-hat-display.html?m=1)_

In this post I will show you how to automatically detect the position of the Raspberry PI using the Sense HAT accelerometer sensor and rotate the display accordingly.

The _**auto_rotate_display**_ function in the script below is doing all the logic. It's reading sensors data to detect the orientation and rotating the Sense HAT display by calling the set_rotation function.
    
    
    import time from sense_hat import SenseHat MSG_COLOR = [200,0,160] BKG_COLOR = [0,0,0] SCROLL_SPEED = 0.06 MESSAGE = "Can't loose my head" def auto_rotate_display(): # read sensors data to detect orientation x = round(sense.get_accelerometer_raw()['x'], 0) y = round(sense.get_accelerometer_raw()['y'], 0) rot = 0 if x == -1: rot=90 elif y == -1: rot=180 elif x == 1: rot=270 # rotate the display according to the orientation print ("Current orientation x=%s y=%s rotating display by %s degrees" % (x, y, rot)) sense.set_rotation(rot) sense = SenseHat() while True: auto_rotate_display() sense.show_message(MESSAGE, scroll_speed=SCROLL_SPEED, text_colour=MSG_COLOR, back_colour=BKG_COLOR) time.sleep(1) 
