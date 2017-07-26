##### Libraries #####
from sense_hat import SenseHat
from time import sleep

##### Functions #####
def get_angle(x,y):
  x = round(x, 0)
  y = round(y, 0)

  if x == -1:
    angle= 180
  elif x == 1:
    angle= 0
  elif y == -1:
    angle =  90
  else:
    angle = 270

  return angle

##### Pixel Art #####
r = (255, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)
e = (0, 0, 0)

locked = [e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,r,r,r,r,e,e,e,e,e,e,e,e,e,e]

unlocked = [e,e,e,e,e,e,e,e,e,e,e,e,e,w,w,e,e,e,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,e,e,e,e,e,e]


##### Main Program #####
sense = SenseHat()
sense.set_pixels(locked)
sleep(2)

##### Locks #####

## Rotation Lock
sense.set_pixels(locked)
code = [0,180,90,270]
complete = []


while len(code)>0:
  acc = sense.get_accelerometer_raw()
  x = acc["x"]
  y = acc["y"]

  if get_angle(x,y) == code[0]:
    complete.append(code.pop(0))
    sense.set_pixel(0,0,g)
  else:
    code = complete + code
    complete = []
    sense.set_pixel(0,0,r)
  sleep(1)
  sense.set_pixel(0,0,e)
  sleep(1)



##### Unlocked #####
sense.set_pixels(unlocked)
sleep(2)
sense.show_message("This is a secret message",scroll_speed=0.05,text_colour=(255,0,0))
