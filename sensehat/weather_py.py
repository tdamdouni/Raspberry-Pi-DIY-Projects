# Created by brendan-lewis@hackster
# Once it loads, it logs data to Dropbox
# Designed for a remote weather station

# This code is imperfect, please comment if you have a suggestion
# or something doesn't work and I will try to fix it

import sense_hat, time, dropbox

db = dropbox.Dropbox('MY_ACCESS_TOKEN') # replace MY_ACCESS_TOKEN with your access token
sense = sense_hat.SenseHat()
sense.clear()

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
W = (255,255,255)
Y = (255,255,0)
P = (255,0,255)
N = (0,0,0)

LOADING_ICONS = [[N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,G,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N],
                 [N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,G,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N],
                 [N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,G,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N],
                 [N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,G,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N,
                  N,N,N,N,N,N,N,N]]

GREEN_CHECK = [N,N,N,N,N,N,N,G,
               N,N,N,N,N,N,G,G,
               N,N,N,N,N,G,G,N,
               G,N,N,N,G,G,N,N,
               G,G,N,G,G,N,N,N,
               N,G,G,G,N,N,N,N,
               N,N,G,N,N,N,N,N,
               N,N,N,N,N,N,N,N]

YELLOW_CHECK = [N,N,N,N,N,N,N,Y,
                N,N,N,N,N,N,Y,Y,
                N,N,N,N,N,Y,Y,N,
                Y,N,N,N,Y,Y,N,N,
                Y,Y,N,Y,Y,N,N,N,
                N,Y,Y,Y,N,N,N,N,
                N,N,Y,N,N,N,N,N,
                N,N,N,N,N,N,N,N]

RED_CROSS = [R,N,N,N,N,N,N,R,
             N,R,N,N,N,N,R,N,
             N,N,R,N,N,R,N,N,
             N,N,N,R,R,N,N,N,
             N,N,N,R,R,N,N,N,
             N,N,R,N,N,R,N,N,
             N,R,N,N,N,N,R,N,
             R,N,N,N,N,N,N,R]

LEFT_ARROW = [N,N,N,W,N,N,N,N,
              N,N,W,N,N,N,N,N,
              N,W,N,N,N,N,N,N,
              W,W,W,W,W,W,W,W,
              W,W,W,W,W,W,W,W,
              N,W,N,N,N,N,N,N,
              N,N,W,N,N,N,N,N,
              N,N,N,W,N,N,N,N]

RIGHT_ARROW = [N,N,N,N,W,N,N,N,
               N,N,N,N,N,W,N,N,
               N,N,N,N,N,N,W,N,
               W,W,W,W,W,W,W,W,
               W,W,W,W,W,W,W,W,
               N,N,N,N,N,N,W,N,
               N,N,N,N,N,W,N,N,
               N,N,N,N,W,N,N,N]

def loading_icn(secs, sense):
  if secs < 0: return
  while secs != 0:
    for pic in LOADING_ICONS:
      sense.set_pixels(pic)
      time.sleep(0.25)
    secs -= 1
  sense.clear()

loading_icn(2, sense)
sense.show_message("Weather Monitor - by brendan-lewis@hackster", scroll_speed = 0.05)

def main():
  loading_icn(2,sense)
  notDone = True

  while notDone:
    sense.set_pixels(GREEN_CHECK)
    data = str(sense.get_temperature()) + "|"
    data = data + str(sense.get_humidity()) + "|"
    data = data + str(sense.get_pressure()) + "\n"
    db.files_upload(data, "/")
    for event in sense.stick.get_events():
      notDone = False
    if notDone: time.sleep(10) # interval time in seconds

  sense.set_pixels(YELLOW_CHECK)
  time.sleep(2)
  sense.set_pixels(RED_CROSS)
  time.sleep(2)
  ev = None
  notDone = True
  while notDone:
    sense.show_message("Press", scroll_speed = 0.07)
    sense.set_pixels(LEFT_ARROW)
    time.sleep(0.7)
    sense.show_message("to exit. Press", scroll_speed = 0.07)
    sense.set_pixels(RIGHT_ARROW)
    time.sleep(0.7)
    sense.show_message("to restart.", scroll_speed = 0.07)
    for event in sense.stick.get_events():
      ev = event
      notDone = False
  if ev.direction == "right": main()
  elif ev.direction == "left":
    leave()

def leave():
  POWER = [N,W,W,W,W,W,W,N,
           W,N,N,W,W,N,N,W,
           W,N,N,W,W,N,N,W,
           W,N,N,W,W,N,N,W,
           W,N,N,W,W,N,N,W,
           W,W,N,N,N,N,W,W,
           W,N,W,W,W,W,N,W,
           N,W,W,W,W,W,W,N]
  sense.set_pixels(POWER)
  time.sleep(1)
  sense.clear()
  exit(0)

main()