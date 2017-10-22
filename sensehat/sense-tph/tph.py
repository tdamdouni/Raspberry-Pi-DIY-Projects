from sense_hat import SenseHat
sense = SenseHat()

#sense.set_rotation(180)

def auto_rotate_display():
  # read sensors data to detect orientation
  x = round(sense.get_accelerometer_raw()['x'], 0)
  y = round(sense.get_accelerometer_raw()['y'], 0)

  rot = 0
  if x == -1:
    rot=90
  elif y == -1:
    rot=180
  elif x == 1:
    rot=270

  # rotate the display according to the orientation
  print ("Current orientation x=%s y=%s  rotating display by %s degrees" % (x, y, rot))
  sense.set_rotation(rot)

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    if t < 20:
	bg = (0, 0, 100) # blau
    elif t > 20 and t < 28:
        bg = (0, 100, 0)  # green
    else:
        bg = (100, 0, 0)  # red

    msg = "T : {0}, P : {1}, H : {2}".format(t, p, h)

    sense.show_message(msg, scroll_speed=0.1, back_colour=bg)
